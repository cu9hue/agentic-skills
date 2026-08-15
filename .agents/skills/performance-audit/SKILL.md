---
name: performance-audit
description: Use when profiling or optimizing CPU- or memory-bound native code (C, C++, Rust) — a hot loop, a slow benchmark, a data structure that misses cache, or a "make this faster" ask over native code. Not for web, database, or I/O latency.
origin: Ulrich Drepper, "What Every Programmer Should Know About Memory" (2007) for the memory hierarchy and layout material; Agner Fog's optimization manuals for microarchitecture, branches, and vectorization; Ahmad Yasin, "A Top-Down Method for Performance Analysis and Counters Architecture" (2014) and Intel's TMA docs for the localization backbone
---

# Performance Audit

You already know cache lines, false sharing, branch misprediction, and SIMD.
What you do not do unprompted is measure before you optimize. This skill makes
a number appear before a fix does.

It has a second job of equal weight. Most "make it faster" questions do not
deserve an audit. Demanding a profile for work that cannot matter, or reaching
for cache lines when the time is in a database, costs the reader more than a
plain wrong answer would. Decide which case you are in before anything else.

## First: does this ask deserve the audit?

Pick one of four outcomes and say which one you picked.

**Wrong layer — answer there and stop.** The time is in I/O, a database, the
network, GC, or a managed or interpreted runtime. Name the layer and answer at
it: query plans, indexes, N+1 queries, connection pooling, serialization,
caching, round trips. Do not name a TMA bucket, do not write a `perf` command,
do not mention a cache line. This skill's machinery does not apply, and
importing it makes the answer worse. There is no audit ceremony and nothing is
withheld — give the answer the question asked for.

**Too small to measure — answer directly and stop.** Bound the total cost
before you ask anyone for anything: total operations times an order-of-magnitude
per-operation cost from `references/cost-model.md`. Work that runs once per
process, a bounded collection of tens of items, a path whose total operation
count is fixed and small — the bound lands in microseconds and no change to it
can matter. Say that in a sentence, say which option you would pick on
readability grounds, and stop. Do not demand a profile. Do not offer an audit.
Do not open a gate. Demanding a profile of a bounded once-per-process path is a
worse answer than an unmeasured opinion, because it spends the reader's time to
learn nothing.

State the bound in one line — "a bounded parse that runs once at startup is
microseconds either way" — then answer the question that was asked, in a few
sentences.

**An agenda, not a fix — answer from the agenda section.** The ask is what to
get right across a body of native code, with no named hot path, no benchmark,
and no number to beat. The gates do not run on a whole library. Go to "When the
ask is an agenda, not a fix" near the end of this file and answer from there.

**Native and real — run the gates.** A hot loop, a slow benchmark, a data
structure that misses cache, a named native function on a path that runs enough
times to matter. A whole library or directory with no named hot path is the
previous outcome, not this one.

When you cannot tell the small case from the real one, ask this: at the
workload the user actually runs, can this region's total cost reach a
noticeable share of runtime? If it cannot, it is the small case. The threshold
is the reader's attention, not a counter.

## The five gates

Run them in order. A gate that has not produced its artifact blocks the next
one. Do not skip ahead because the source looks obvious — a pattern you
recognize in the source is not evidence, and matching a remembered fix to
unmeasured code is the most common way an audit goes wrong.

Run the commands yourself when you can. That is the default, and nothing below
substitutes for it. When you genuinely cannot reach the machine, the bar does
not drop: write the exact command, say what number you expect to read from it,
say what that number would rule in and rule out, and ask the user to run it.
The claim then stands where gate 3 puts an entry nobody could confirm — a
`hypothesis`, ranked below anything that was measured, never a finding.
Waiting on a measurement is the correct state. Asserting past one is not.

### Gate 1 — Baseline

Produce a number before you produce an opinion. The baseline needs four
things, and all four go in the report:

- the workload — size, data, and how it was generated
- the metric — wall time, throughput, or cycles, with the target number beside
  it
- a reproducible command that anyone can rerun
- at least 5 runs, with the spread reported

**One reported number is not a baseline.** A single timing handed to you fixes
the workload, not the spread, and you cannot tell a later improvement from
noise without the spread. Re-run it at least 5 times, or ask the user to, and
report the spread before you build anything on it.

**No benchmark exists?** Writing one is your first deliverable, not a
prerequisite you wait on. `criterion` for Rust, Google Benchmark or `nanobench`
for C++. Ask for the workload size and the target number in the same turn.
Until that number exists, everything you say about the code is a `hypothesis`
and is labeled one.

While you wait on the number, you may still produce the gate-4 report shape —
ranked items, each labeled `hypothesis`, each carrying the experiment that
would settle it. What you may not do is call any of it a finding, or apply it.

Build with optimization on plus `-g -fno-omit-frame-pointer`. Never baseline a
debug build, and never change the build between the baseline and the
re-measure.

**Before you leave gate 1, settle complexity.** Read the hot path for a
superlinear pattern: a linear scan inside a loop over items, a repeated sort, a
containment test against an unindexed collection, a quadratic join. If one is
there, name it and settle it first. No bucket in the sections below fixes a
wrong algorithm, and a microoptimization layered over one is wasted work. This
is the one question you may raise from reading the source — raise it as the
question to settle, not as a finding.

### Gate 2 — Localize

Measure the split and name one bucket. The vocabulary is fixed and you use it
verbatim: `retiring`, `bad speculation`, `frontend bound`, `backend bound`.

Read `references/tma.md` and follow it from the file, not from memory. It
carries the buckets and their drill-downs, its own rules for entering, the
share thresholds that decide which bucket you chase, the PMU access checks, the
`perf` invocations, `toplev`, `cachegrind`, the counter-ratio fallback for CPUs
with no `--topdown`, and the macOS `xctrace` path. When you fall back, keep the
gate and follow the weaker-evidence shape it gives.

Two rules bind with that file closed:

- Do not name a bucket you did not measure. Reading the source is not
  localization.
- One bucket. Drill into the dominant one and leave the rest alone.

Gate 2's artifact is one line: bucket, number, tool, confidence. `tma.md`
closes with the shape. Never write a bucket with no number and no tool beside
it.

### Gate 3 — Confirm the cause

The bucket names a shortlist. A second targeted measurement, run on the
unmodified baseline build, picks which entry on that list is yours.

Enter `references/catalog.md` at the **section** for your bucket, and read the
section header before you read any entry:

- `backend bound` — memory bound
- `backend bound` — core bound
- `bad speculation`
- `frontend bound`
- `retiring`

Enter at the section, never at an entry. The core-bound header and the
`bad speculation` header both carry carve-outs that route you out to an entry
filed under a different section, and an entry read on its own hides them. Land
straight on the entry whose symptom matches the source and you will confirm a
cause that cannot be yours. Read the header first, every time.

`catalog.md`'s own header states the rules for entering. Two of them survive
with the file closed:

- If the confirming measurement does not fire, the entry is wrong. Drop it. Do
  not weaken it to a maybe and keep it in the report.
- If you cannot run the confirming measurement on this machine, the entry is
  not available to you. Say so, and rank it below every entry you confirmed.

### Gate 4 — Report

Stop here and report. Do not apply anything yet.

Rank the findings by measured impact. Each one carries, all six:

1. the evidence line — the counter, the number, the tool, the run count
2. the TMA bucket it sits in
3. the proposed change, stated concretely
4. the expected gain, as an order of magnitude
5. the command that re-measures it
6. the cost in readability or portability

Derive the expected gain with the arithmetic in `references/cost-model.md`,
section "Ranking with this file — gate 4": events you would eliminate times
cycles per event, then bounded by the bucket's slot share, by out-of-order
overlap, and by Amdahl. Take the event count from your own counters. State the
result as an order of magnitude and as a bound — "at most a few percent" — and
never as a predicted runtime.

Anything not confirmed by a measurement ships labeled `hypothesis`, ranked
below everything confirmed, carrying the specific experiment or counter that
would settle it. Never present a hypothesis as a finding.

Never write "the biggest single win" without the gate-4 arithmetic and the
counters printed beside it. The ranking orders what you test next. It does not
tell the reader what they will get.

### Gate 5 — Fix on approval

The user picks what to apply. You do not pick for them.

- One change at a time. No batches, ever. A layout rewrite plus new compiler
  flags plus threading teaches you nothing about any of the three.
- Re-measure after each change with gate 1's exact command and run count.
- Keep or revert on the number. A delta inside the spread is not an
  improvement — revert it and keep the simpler version.
- After a change you keep, every other confirming measurement is stale. Retake
  the one for the next entry before you touch it.

## Hard rules

These hold across all five gates.

- **No fix without a number.** An unmeasured claim ships labeled `hypothesis`,
  ranked, carrying the experiment that would settle it — never presented as a
  finding.
- **One change per measurement.** No batches.
- **Report run count and spread.** An improvement inside the noise is not an
  improvement.
- **Do not touch what the profile does not show.** Code that is not in the
  dominant bucket is not in scope, however bad it looks.
- **Check algorithmic complexity before any microoptimization.**
- **Revert anything that does not beat noise**, and keep the simpler version.

## When the ask is an agenda, not a fix

Triage outcome 3 lands here. The ask names a body of code and asks what to get
right in it, rather than naming something to make faster. Answer with the
discipline, not with the catalog. Do not open gate 1 and demand a benchmark for
a library with no named hot path — there is nothing yet to baseline.

Put measurement first on the agenda: a baseline and a repeatable workload
before any change, profile-driven targeting rather than a checklist walk, and
one change per measurement. Let the memory cost model run through the whole
answer — layout, locality, allocation, the working set against the cache
levels — rather than appearing as a bullet at the end.

Do not dump catalog entries as claims about code you have not profiled. Naming
a plausible fix for unprofiled code is exactly the failure this skill exists to
prevent, and it is not less of one because the question was open-ended.

## Quality gate

Confirm the first check on every answer. Confirm the other six when the triage
sent you to the gates.

- the triage outcome was stated, and no gate, bucket, or `perf` command appears
  under the wrong-layer or too-small outcome
- a baseline number with run count and spread exists before any finding
- every finding cites a measurement; everything else is labeled `hypothesis`
  and carries its confirming experiment
- the TMA bucket is named, and only that bucket's causes were investigated
- fixes applied one at a time, each re-measured
- changes inside noise reverted
- expected gains stated as orders of magnitude, never as precise predictions
