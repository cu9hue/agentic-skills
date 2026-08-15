# Performance Audit Skill — Design

Approved 2026-08-15.

## Purpose

A measurement-driven audit process for CPU- and memory-bound native code.
Synthesized from Ulrich Drepper, "What Every Programmer Should Know About
Memory" (2007), and Agner Fog's optimization manuals, with Intel's Top-Down
Microarchitecture Analysis (TMA, Yasin 2014) as the localization backbone.

The base model already knows cache lines, false sharing, branch misprediction,
and SIMD. It does not, unprompted, measure before it optimizes. The skill's
value is discipline, not knowledge transfer: it must make the agent produce a
number before it produces a fix. The evals judge that, not recall.

## Trigger / scope

- `name: performance-audit`
- Use when: profiling or optimizing CPU/memory-bound native code (C, C++,
  Rust) — a hot loop, a slow benchmark, a data structure that misses cache, a
  "make this faster" ask over native code.
- Not for: web, database, or I/O latency; not for code with no measurable hot
  path.

## Triage — four outcomes, ahead of the gates

(Amended 2026-08-15, after the GREEN rounds. The approved design opened the
skill at gate 1. What shipped opens with this triage, and it is the largest
structural feature of the file — recorded here so the spec describes the
skill that exists.)

Most "make it faster" asks do not deserve the audit. The RED baseline failed
S5 by demanding a profile for a 40-entry startup path, so a skill that only
adds rigor would fail that scenario harder than no skill at all. SKILL.md
therefore opens by picking one of four outcomes:

1. **Wrong layer** — the time is in I/O, a database, the network, GC, or a
   managed runtime. Answer there, in full, and stop.
2. **Too small to measure** — bound the total cost first (operations times an
   order-of-magnitude per-operation figure from `cost-model.md`). If the bound
   lands in microseconds, say so, answer the question asked, and stop.
3. **An agenda, not a fix** — a body of native code with no named hot path, no
   benchmark, and no number to beat. The gates do not run on a whole library.
4. **Native and real** — run the five gates below.

The two refusal outcomes are **internal**: the reader gets a direct answer with
no gate, no bucket, no `perf` command, and no statement of which outcome was
picked. GREEN round 1 failed S4 because an earlier draft required the outcome
to be stated, which put TMA vocabulary on a Node/Postgres answer;
`evals/results.md` carries the round and the fix.

Outcome 3 is answered from a separate section, "When the ask is an agenda, not
a fix", near the end of SKILL.md: measurement first on the agenda, the memory
cost model running through the whole answer, and no catalog entries dumped as
claims about unprofiled code.

## Audit protocol — five gates, in order

1. **Baseline.** Requires a workload, a metric, a reproducible command, and at
   least 5 runs with the spread reported. No baseline means no audit: establishing one
   is the skill's first action, not a prerequisite it waits on.
2. **Localize with TMA.** `perf stat --topdown` splits cycles into retiring /
   bad speculation / frontend bound / backend bound. Drill into the dominant
   bucket only. This is the ordering rule the whole audit hangs on — it
   replaces walking a checklist top to bottom.
3. **Confirm the cause.** The bucket names a shortlist in the catalog; a
   second targeted measurement (cache-misses, dTLB-load-misses, branch-misses,
   cachegrind) picks which entry. Drepper's material sits under backend bound;
   Fog's under frontend bound and bad speculation.
4. **Report.** Findings ranked by measured impact. Each carries: the evidence
   line, the TMA bucket, the proposed change, an order-of-magnitude expected
   gain, the re-measure command, and the cost in readability or portability.
5. **Fix on approval.** The user picks. One change at a time, re-measured
   individually, kept or reverted on the number.

## Hard rules

- No fix without a number. An unmeasured claim ships labeled `hypothesis`,
  ranked, carrying the experiment that would settle it — never presented as a
  finding.
- One change per measurement. No batches.
- Report run count and spread. An improvement inside the noise is not an
  improvement.
- Do not touch what the profile does not show.
- Check algorithmic complexity before any microoptimization.
- Revert anything that does not beat noise, and keep the simpler version.

## Platform

Linux with `perf` is the primary path. On macOS, `perf` does not exist: the
skill falls back to `xctrace` counter templates plus `sample`. Apple Silicon
does not expose the TMA tree the way Intel does, so the fallback is weaker by
construction — the skill says so, keeps the gate structure, and degrades gate 2
to counter ratios rather than pretending to a topdown breakdown.

## Structure

- `.agents/skills/performance-audit/SKILL.md` — the five gates and the hard
  rules. Target ~250 lines, 500 hard cap.
- `references/tma.md` — the top-down tree, thresholds, `perf` invocations, the
  `xctrace` macOS fallback, and counter-ratio fallbacks for CPUs without
  `--topdown`.
- `references/cost-model.md` — latency and throughput anchors (L1/L2/L3/DRAM,
  NUMA-remote, branch miss, TLB miss, syscall), each stamped with machine and
  month, flagged as order-of-magnitude anchors rather than measurements, with
  the commands to re-derive them on the target machine.
- `references/catalog.md` — symptom → cause → fix, filed under TMA buckets.
  Drepper supplies layout, false sharing, prefetch, NUMA, huge pages,
  alignment; Fog supplies dependency chains, branch layout, µop cache,
  vectorization, call overhead.
- Frontmatter `origin:` credits Drepper, Fog, and Yasin/Intel for TMA.

## Quality gate (in SKILL.md)

(Amended 2026-08-15: seven bullets shipped, not six. The triage bullet below
was added with the triage section, and it is the only one checked on every
answer — the rest are checked when the triage sent the answer to the gates.)

- the triage ran and the answer matches the outcome it picked; on the
  wrong-layer and too-small outcomes no gate, bucket, `perf` command, or
  triage announcement appears anywhere in the answer
- a baseline number with run count and spread exists before any finding
- every finding cites a measurement; everything else is labeled `hypothesis`
  and carries its confirming experiment
- the TMA bucket is named, and only that bucket's causes were investigated
- fixes applied one at a time, each re-measured
- changes inside noise reverted
- expected gains stated as orders of magnitude, never as precise predictions

## Evals

Per `skill-authoring`: `evals/scenarios.md` written first, RED baseline run
before drafting, blind judge, verdict appended to `evals/results.md`.

1. **Execution** — cache-hostile array-of-structs hot loop in C++ with a
   benchmark present. Does it measure, localize, change one thing, re-measure?
2. **Execution** — slow Rust function, no benchmark harness. Does it refuse to
   present fixes as findings, label hypotheses, and name the experiment?
3. **Structural probe (underspecified)** — "what should I get right here?"
   over a performance-sensitive file with no performance framing. Does
   measurement discipline reach the agenda without inventing unmeasured
   claims?
4. **Negative** — slow web endpoint, p99 400ms. The skill must not trigger the
   microarchitectural machinery.
5. **Negative** — premature optimization ask on code with no hot path. Does it
   answer directly and decline the audit? (Corrected 2026-08-15: this line
   originally read "push back and demand a baseline". The RED baseline refutes
   it — the no-skill arm demanded a profile for a 40-entry startup parse and
   failed the rubric for it. Demanding measurement where measurement cannot pay
   is a failure mode of this skill, not a success.)

## Verification

Blind A/B with subagents, one per arm per scenario, prompts identical except
skill presence, judged per-scenario rubric by a separate blind judge. Sample
size stated in `results.md`. No commit until the skill arm wins.
