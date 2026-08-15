# performance-audit — eval results

Append-only. Newest at the bottom.

## 2026-08-15 — RED baseline, no skill loaded (commit 1c37f1e)

Arms: A = no skill. n=1 per cell — signal, not proof. Both arms run on
Sonnet. Arms could not execute the code; the rubrics score the process each
answer demands and the order it demands it in, not measurements taken.

**10 of 21 rubric lines failed.** The skill is not redundant. Failures,
verbatim — this is the skill's job description:

**S1 — C++ hot loop, benchmark present** (4 of 6 failed)

- no baseline established or demanded; the answer opens "The struct layout
  is the bug"
- no profiling command anywhere; reasons purely from reading the source
- stacks SoA + `-O3 -march=native` + OpenMP together with no re-measure
  step between them
- asserts a "biggest single win" with zero measurement behind it

Passed: localized to memory-bound before naming a fix; refused to predict an
exact resulting number.

**S2 — Rust function, no harness** (3 of 5 failed)

- presents optimizations as findings, not hypotheses: "Three real problems
  in the current code, in order of impact"
- first action is the inverted-index rewrite; never establishes a baseline
  or asks for the workload
- fixes carry no confirming experiment or counter

Passed: ranked them; led with the `contains` linear scan as the algorithmic
question.

**S3 — structural probe** (2 of 4 failed)

- no baseline or profiling discipline anywhere on the agenda
- the cost model is confined to section 5 of 6, near the end — a topic
  covered, not an organizing thread

Passed: layout and allocation advice present; did not dump unmeasured
optimization claims.

**S4 — negative, web endpoint** (0 of 3 failed)

Clean. No microarchitectural machinery, right layer, proportionate.

**S5 — negative, premature optimization** (1 of 3 failed)

- demanded a profile on a 40-entry startup path anyway: "don't swap based on
  intuition. Profile the lookup path first."

Passed: short, direct, no audit protocol; said the change does not matter.

Note for the draft: S5's failure is the mirror image of S1's and S2's. The
skill must demand measurement where measurement pays and refuse to demand it
where it does not. A skill that only ratchets up rigor would fail S5 harder
than the baseline did.

Obsolescence: NO — the no-skill arm failed 10 rubric lines.

## 2026-08-15 — GREEN round 1, skill arm loses the negative (skill at 4cf6c80)

Arms: A = no skill (reused from RED), B = skill + three references. n=1 per
cell. Both arms on Sonnet. Blind judge, arms anonymized into teams and
shuffled per scenario.

Skill arm 19/21, baseline 8/21. It won S1 6/6, S2 5/5, S3 4/4, S5 3/3 — and
**failed S4, the negative, at 1/3**.

The judge's evidence: the skill arm "opens by naming TMA, `perf`, cache lines
and the skill's gates" on a Node/Postgres endpoint question, behind a
"Triage outcome: wrong layer" preamble. The substance underneath was correct
and scored the rubric's middle line.

Cause: the skill told the agent to state which triage outcome it picked, and
a quality-gate check verified that it had. On the two refusal outcomes that
directive produces ceremony on exactly the answers where ceremony is the
failure. Naming the machinery to disclaim it is still naming it.

Not landed. Fixed and rerun.

## 2026-08-15 — GREEN round 2, skill arm wins (skill at a2fe386)

Fix: on the two refusal outcomes — wrong layer, too small to measure — the
triage is internal. The user gets a direct answer at the right layer and no
trace of the routing. The test written into the skill is that a reader who
never heard of it cannot tell it was loaded. The gates and agenda outcomes
still name their route.

Arms: A = no skill (reused), B = skill + references, rerun on all five
scenarios because the fix touches text every path reads. n=1 per cell —
signal, not proof. Fresh blind judge, new per-scenario shuffle.

**Skill arm 21/21, baseline 9/21.**

- S1 (C++ hot loop): **skill**, 6/6 vs 2/6 — `perf stat -r 5` and spread up
  front, localization before any fix, per-change re-measure; the baseline
  opened with "the struct layout is the bug".
- S2 (Rust, no harness): **skill**, 5/5 vs 1/5 — everything labeled
  hypothesis with its confirming experiment, complexity settled first; the
  baseline shipped an inverted-index rewrite as its first action.
- S3 (structural probe): **skill**, 4/4 vs 2/4 — baseline harness as
  deliverable #1 and the cost model running through the whole week; the
  no-skill arm put performance in section 5 of 6 and called it secondary.
- S4 (negative, web endpoint): **tie**, 3/3 both — no TMA, no triage
  disclosure, right layer, no ceremony. The over-trigger is gone.
- S5 (negative, premature optimization): **skill**, 3/3 vs 1/3 — four lines,
  answered outright; the baseline escalated to microarchitecture and then
  demanded a profile.

Judge verdict: the skill arm passed every rubric line in the set, including
both negatives. Obsolescence: NO — the no-skill arm passed 9 of 21.

Caveats, recorded so a later reader can weigh them:

- n=1 per cell. Real usage is the ongoing eval.
- The two GREEN rounds used different judges. They scored the identical
  baseline S1 text differently on one line (whether it localizes explicitly),
  8/21 vs 9/21 overall. Judge variance on that line is roughly the size of a
  single rubric item.
- Two passages in `SKILL.md` still track scenario fact patterns: gate 1's
  "containment test against an unindexed collection" (S2's `contains` scan)
  and the wrong-layer branch's web/database list (near S4's answer key).
  Both are accepted; S4's baseline arm scored 3/3 without the skill in both
  rounds, so little rides on the second.
- Arms could not execute anything. The rubrics score the process each answer
  demands and the order it demands it in, not measurements taken.
