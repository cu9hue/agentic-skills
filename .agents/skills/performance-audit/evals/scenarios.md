# performance-audit — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md + references loaded), identical prompts otherwise. The subagent
returns only the deliverable — its next chat message, no meta-commentary.
Anonymize outputs into teams, blind-judge against the rubrics, log the
verdict in `results.md`.

## Shared material

Each scenario is self-contained. S1 and S2 inline their own source. Arms
have no ability to actually run the code — judge the *process the agent
proposes and demands*, not measurements it cannot take. An arm that states
it would run a command and reports what it would read counts as measuring;
an arm that asserts a speedup without any command does not.

## S1 — execution: C++ hot loop with a benchmark present

User message: "This benchmark runs in 340ms on my Linux box and I need it
under 100ms. Make it faster.

```cpp
// particles.hpp
struct Particle {
  double x, y, z;
  double vx, vy, vz;
  char name[32];
  int    id;
  bool   alive;
  double mass, charge, temperature, pressure;
};

// bench.cpp — built with: g++ -O2 -std=c++17 bench.cpp -o bench
void step(std::vector<Particle>& ps, double dt) {
  for (auto& p : ps) {
    p.x += p.vx * dt;
    p.y += p.vy * dt;
    p.z += p.vz * dt;
  }
}
// main() fills 4'000'000 particles, calls step() 20 times, prints elapsed ms.
```
"

Rubric:
- demands or re-establishes a baseline with repeat runs (≥5) and reports
  spread/variance before proposing any change
- names a concrete profiling command (`perf stat`, `perf stat --topdown`,
  `cachegrind`, or the `xctrace` fallback) rather than reasoning purely
  from the source
- localizes to the memory/backend-bound side *before* naming a fix, and
  says so explicitly
- proposes changes one at a time, each with its own re-measure step
- states expected gain as an order of magnitude, not a precise prediction
- does not present the struct-of-arrays rewrite as a confirmed win with no
  measurement behind it

## S2 — execution: Rust function, no benchmark harness

User message: "This is the slowest function in our indexer. Make it faster.

```rust
pub fn score_docs(docs: &[Doc], query: &Query) -> Vec<(DocId, f32)> {
    let mut out = Vec::new();
    for d in docs {
        let mut s = 0.0;
        for t in &query.terms {
            if d.tokens.contains(t) {
                s += idf(t) * d.tf(t);
            }
        }
        if s > 0.0 {
            out.push((d.id, s));
        }
    }
    out.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
    out
}
```
"

There is no benchmark, no profile, and no stated workload size.

Rubric:
- does NOT present optimizations as findings; anything unmeasured is
  explicitly labeled a hypothesis or equivalent
- its first action is establishing a baseline (e.g. a criterion benchmark)
  or asking for the workload and the target number
- every hypothesis carries the specific experiment or counter that would
  confirm it
- hypotheses are ranked
- flags the `contains` linear scan as an algorithmic question to settle
  before any microoptimization

## S3 — structural probe: underspecified ask

User message: "I'm spending this week in our C++ mesh-processing library
under `src/geom/`. What should I get right?"

Rubric:
- measurement discipline reaches the agenda unprompted — baseline before
  changes, profile-driven targeting
- the memory/cost model informs the advice (layout, locality, allocation)
  rather than generic "write clean code" guidance
- these are an organizing thread through the answer, not one bullet at the
  end
- does NOT dump a catalog of unmeasured optimization claims about code it
  has not profiled

## S4 — negative: web endpoint latency

User message: "Our `/api/search` endpoint has a p99 of 400ms. Node in front
of Postgres. Where do I start?"

Rubric:
- behaves as if the skill were absent: no TMA buckets, no `perf stat
  --topdown`, no cache-line or microarchitectural machinery
- answers at the right layer (query plans, indexes, N+1, connection pooling,
  serialization, network)
- no withheld deliverable and no audit ceremony

## S5 — negative: premature optimization

User message: "Should I swap `std::map` for a flat sorted vector in our
config loader? It parses ~40 entries once at startup."

Rubric:
- answers short and directly; no five-gate audit protocol invoked
- says the change does not matter at this size / is not worth measuring
- does not demand a profile before answering a question this small
