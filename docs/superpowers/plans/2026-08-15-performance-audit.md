# Performance Audit Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship `.agents/skills/performance-audit/` — a measurement-driven audit process for CPU- and memory-bound native code — with persisted evals proving it beats the no-skill baseline.

**Architecture:** A `SKILL.md` holding five ordered gates and six hard rules, plus three `references/` files carrying the heavy material (the TMA decision tree, a dated cost model, a symptom→cause→fix catalog). The skill's value is discipline, not recall, so the eval rubrics score whether a number precedes every fix — not whether the agent can name a cache line.

**Tech Stack:** Markdown only. No code ships. Evals run as subagents (one per arm per scenario) with a separate blind judge, per `skill-authoring`.

**Spec:** `docs/superpowers/specs/2026-08-15-performance-audit-design.md`

## Global Constraints

- `SKILL.md` hard cap 500 lines; target ~250. Verbatim and heavy material goes to `references/`.
- `description:` is trigger conditions only, ≤~500 chars, with one "not for" boundary.
- Directives, not suggestions: "run the baseline", never "consider running".
- `origin:` frontmatter credits Drepper ("What Every Programmer Should Know About Memory", 2007), Agner Fog (optimization manuals), and Yasin 2014 / Intel for TMA.
- Skill lives at `.agents/skills/performance-audit/`. Never write to `.claude/skills/` — it is a symlink.
- **Order is binding (`skill-authoring`):** scenarios → RED baseline → draft → GREEN rerun. Drafting any part of `SKILL.md` or `references/` before Task 2 records the baseline invalidates the eval.
- Baseline minimum: 5 runs, spread reported.
- Primary platform Linux + `perf`; macOS falls back to `xctrace` + `sample` with gate 2 degraded to counter ratios.

---

### Task 1: Eval scenarios

**Files:**
- Create: `.agents/skills/performance-audit/evals/scenarios.md`

**Interfaces:**
- Consumes: nothing.
- Produces: five scenarios `S1`–`S5` with rubrics. Task 2 runs S1–S5 arm A, Task 6 runs arm B. The rubric lines are the contract the skill body must satisfy.

- [ ] **Step 1: Create the scenarios file**

Follow `.agents/skills/skill-authoring/references/eval-template.md` structure. Write exactly these five scenarios:

````markdown
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
````

- [ ] **Step 2: Verify the scenario set meets the mandate**

Confirm by reading: 5 scenarios; S3 is an underspecified structural probe naming no axis; S4 and S5 are negatives; every rubric line is an observable pass/fail check, not a matter of taste.

- [ ] **Step 3: Commit**

```bash
git add .agents/skills/performance-audit/evals/scenarios.md
git commit -m "performance-audit: eval scenarios (pre-baseline)"
```

---

### Task 2: RED — run the no-skill baseline

**Files:**
- Create: `.agents/skills/performance-audit/evals/results.md`
- Create: scratch transcripts under the session scratchpad (not committed)

**Interfaces:**
- Consumes: `scenarios.md` S1–S5.
- Produces: a RED section in `results.md` listing, per scenario, exactly which rubric lines the baseline failed. Task 4 and Task 5 draft *only* against these recorded failures.

- [ ] **Step 1: Dispatch five arm-A subagents**

One subagent per scenario, in a single message so they run concurrently. Each gets the scenario's verbatim user message and nothing else — no skill, no mention that a skill exists, no hint about performance methodology. Prompt each with: "Reply to this message as you normally would. Return only your reply — no meta-commentary."

- [ ] **Step 2: Score each baseline output against its rubric**

For each scenario, mark every rubric line pass or fail. Record the failures verbatim — these are the skill's job description.

- [ ] **Step 3: Check the stop condition**

If the baseline passes every rubric line across all five scenarios, the skill is unnecessary. STOP, report that to the user, and do not draft it. (`skill-authoring`: "If baseline already passes everything, the skill is unnecessary: stop.")

- [ ] **Step 4: Write the RED record**

Create `evals/results.md` with the append-only header from the eval template and a first section dated today, arms stated (A = no skill), `n=1 per cell — signal, not proof`, and a per-scenario list of failed rubric lines.

- [ ] **Step 5: Commit**

```bash
git add .agents/skills/performance-audit/evals/results.md
git commit -m "performance-audit: RED baseline, no skill loaded"
```

---

### Task 3: TMA reference

**Files:**
- Create: `.agents/skills/performance-audit/references/tma.md`

**Interfaces:**
- Consumes: the RED failures from Task 2 (only write what the baseline got wrong).
- Produces: the bucket names `retiring`, `bad speculation`, `frontend bound`, `backend bound` — used verbatim by `SKILL.md` gate 2, by `catalog.md` section headers, and by S1's rubric.

- [ ] **Step 1: Write the top-down tree**

Level 1 buckets with the standard interpretation and drill-down for each: bad speculation → branch mispredicts, machine clears; frontend bound → fetch latency (i-cache, iTLB) vs fetch bandwidth (µop cache, decode); backend bound → core bound (ports, dependency chains, divider) vs memory bound (L1/L2/L3/DRAM/store buffer); retiring → the "not stalled" bucket, where the win is doing less work or vectorizing.

- [ ] **Step 2: Write the command section**

Exact invocations: `perf stat --topdown -a`, `perf stat -e cycles,instructions,cache-references,cache-misses,branch-misses,dTLB-load-misses`, `perf record`/`perf report` for attribution, `perf c2c` for false sharing, `valgrind --tool=cachegrind`, and `toplev` for full multi-level TMA. State that `--topdown` needs Intel or recent AMD and what to do when it is absent.

- [ ] **Step 3: Write the fallback section**

Two fallbacks. (a) No `--topdown`: derive the picture from ratios — IPC, cache-miss rate per instruction, branch-miss rate, TLB miss rate — and state the thresholds that redirect the audit. (b) macOS: `xctrace record --template 'CPU Counters'`, `xctrace record --template 'Time Profiler'`, and `sample <pid>`. Say plainly that Apple Silicon does not expose the TMA tree, so gate 2 degrades to counter ratios and the audit must say which fallback it used.

- [ ] **Step 4: Commit**

```bash
git add .agents/skills/performance-audit/references/tma.md
git commit -m "performance-audit: TMA localization reference"
```

---

### Task 4: Cost model and catalog references

**Files:**
- Create: `.agents/skills/performance-audit/references/cost-model.md`
- Create: `.agents/skills/performance-audit/references/catalog.md`

**Interfaces:**
- Consumes: bucket names from `references/tma.md`.
- Produces: `catalog.md` sections keyed by the four TMA buckets; `SKILL.md` gate 3 points at them by name.

- [ ] **Step 1: Write `cost-model.md`**

A table of order-of-magnitude anchors in both cycles and nanoseconds: L1 hit, L2 hit, L3 hit, local DRAM, remote-NUMA DRAM, branch mispredict, dTLB miss with and without a page walk, atomic RMW uncontended and contended, false-sharing round trip, syscall, and a 4 KiB `memcpy`. Head the table with an explicit stamp: the machine class and the month the numbers describe (`2026-08`, modern x86-64 server class).

Directly under the table, two required paragraphs: (1) these are anchors for ranking hypotheses, never measurements, and no finding may cite them as evidence; (2) how to re-derive them on the target machine — `lmbench`, `perf bench mem`, and a short pointer-chase loop with stride sweep for the cache-level boundaries.

- [ ] **Step 2: Write `catalog.md`**

Four sections, one per TMA bucket, each entry in symptom → cause → fix → confirming measurement form.

- *Backend bound / memory* (Drepper): array-of-structs when the loop touches few fields → SoA or hot/cold split; pointer chasing → flattened or arena layout; false sharing → padding to a cache line, confirmed with `perf c2c`; capacity misses → blocking/tiling; TLB pressure on large working sets → huge pages; NUMA-remote access → first-touch placement and `numactl`; misaligned or split loads → alignment; regular strided misses the prefetcher cannot see → software prefetch, with Drepper's own caution that it usually loses.
- *Backend bound / core* (Fog): long loop-carried dependency chains → accumulator splitting; division and `sqrt` in a hot loop → reciprocal or strength reduction; port saturation → instruction mix change; denormals → flush-to-zero.
- *Bad speculation* (Fog): unpredictable data-dependent branch → branchless select or sorting the data; indirect call in a hot loop → devirtualization.
- *Frontend bound* (Fog): over-inlining blowing i-cache → inline discipline; µop-cache misses from huge unrolled bodies → less unrolling; cold-path code inline with hot path → move cold paths out of line.
- *Retiring*: nothing is stalled — the only wins left are doing less work, better vectorization, or a better algorithm.

Every entry states its cost in readability or portability. No entry claims a numeric speedup.

- [ ] **Step 3: Commit**

```bash
git add .agents/skills/performance-audit/references/cost-model.md .agents/skills/performance-audit/references/catalog.md
git commit -m "performance-audit: cost model and fix catalog"
```

---

### Task 5: SKILL.md

**Files:**
- Create: `.agents/skills/performance-audit/SKILL.md`

**Interfaces:**
- Consumes: bucket names from `tma.md`; section names from `catalog.md`; the RED failure list from Task 2.
- Produces: the skill itself. Task 6 loads exactly this file plus `references/` as arm B.

- [ ] **Step 1: Write the frontmatter**

```markdown
---
name: performance-audit
description: Use when profiling or optimizing CPU- or memory-bound native code (C, C++, Rust) — a hot loop, a slow benchmark, a data structure that misses cache, or a "make this faster" ask over native code. Not for web, database, or I/O latency.
origin: Ulrich Drepper, "What Every Programmer Should Know About Memory" (2007) for the memory hierarchy and layout material; Agner Fog's optimization manuals for microarchitecture, branches, and vectorization; Ahmad Yasin, "A Top-Down Method for Performance Analysis and Counters Architecture" (2014) and Intel's TMA docs for the localization backbone
---
```

- [ ] **Step 2: Write the five gates**

One section per gate, in order, each stating what it requires before the next may start: (1) baseline — workload, metric, reproducible command, ≥5 runs, spread reported; (2) localize — TMA bucket named, dominant bucket only; (3) confirm — a second targeted measurement picks the catalog entry; (4) report — ranked findings, each with evidence line, bucket, proposed change, order-of-magnitude gain, re-measure command, readability/portability cost; (5) fix on approval — user picks, one change at a time, each re-measured, kept or reverted on the number.

Point gate 2 at `references/tma.md`, gate 3 at `references/catalog.md`, and gate 4's expected-gain column at `references/cost-model.md`.

- [ ] **Step 3: Write the hard rules**

Verbatim from the spec, as directives: no fix without a number (unmeasured ships labeled `hypothesis`, ranked, carrying its experiment); one change per measurement; report run count and spread, and an improvement inside noise is not an improvement; do not touch what the profile does not show; check algorithmic complexity before any microoptimization; revert anything that does not beat noise and keep the simpler version.

- [ ] **Step 4: Write the scope boundary**

An explicit section: when the bottleneck is I/O, database, network, or GC, say so and stop — this skill's machinery does not apply. Name the S5 case too: work small enough that no measurement is warranted gets a direct answer, not an audit.

- [ ] **Step 5: Write the quality gate**

The six checks from the spec's quality-gate section, as a closing checklist.

- [ ] **Step 6: Check the line count**

Run: `wc -l .agents/skills/performance-audit/SKILL.md`
Expected: ≤500, ideally ~250. If over, move material to `references/`.

- [ ] **Step 7: Commit**

```bash
git add .agents/skills/performance-audit/SKILL.md
git commit -m "performance-audit: skill body, five gates and hard rules"
```

---

### Task 6: GREEN — A/B rerun and blind judge

**Files:**
- Modify: `.agents/skills/performance-audit/evals/results.md`

**Interfaces:**
- Consumes: arm-A outputs from Task 2, the drafted skill from Tasks 3–5.
- Produces: the verdict. No README entry and no merge until the skill arm wins.

- [ ] **Step 1: Dispatch five arm-B subagents**

One per scenario, concurrently. Each receives the full contents of `SKILL.md` and the three `references/` files, then the scenario's verbatim user message. Same closing instruction as arm A: return only the reply.

- [ ] **Step 2: Anonymize into teams**

Relabel arm A and arm B outputs as Team 1 / Team 2, shuffled per scenario so the same team label is not always the same arm.

- [ ] **Step 3: Dispatch the blind judge**

One judge subagent, given the rubrics and the anonymized pairs, told nothing about which team is which and nothing about a skill existing. Instruct it to score each rubric line pass/fail per team, harshly, with no credit for style or length, and to name a per-scenario winner or a tie.

- [ ] **Step 4: Check the verdict**

Arm B must win S1, S2, and S3, and must not over-trigger on S4 or S5. If it loses or over-triggers, fix the skill against the specific rubric line that failed and rerun from Step 1. Do not proceed on a loss.

- [ ] **Step 5: Append the GREEN result**

Append a dated section to `results.md`: arms, `n=1 per cell — signal, not proof`, per-scenario winner with a one-line reason, judge verdict, and the obsolescence line (did the no-skill arm pass everything?).

- [ ] **Step 6: Commit**

```bash
git add .agents/skills/performance-audit/evals/results.md
git commit -m "performance-audit: GREEN A/B verdict"
```

---

### Task 7: README entry

**Files:**
- Modify: `README.md`

**Interfaces:**
- Consumes: the winning verdict from Task 6.
- Produces: nothing downstream.

- [ ] **Step 1: Add the skill to the README**

Add a `### Performance` section after `### Languages`, with one bullet in the established house style: bold skill name, em dash, what it does, then the sources credited with links (Drepper, Agner Fog, Yasin's TMA paper).

- [ ] **Step 2: Verify the layout claim still holds**

Run: `ls .agents/skills/performance-audit`
Expected: `SKILL.md`, `evals/`, `references/`.

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "README: add performance-audit"
```
