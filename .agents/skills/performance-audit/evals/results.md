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
