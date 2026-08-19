# prepare-pr — eval results

Append-only. Newest at the bottom.

## 2026-08-19 — initial A/B (base 77bc264)

Arms: A = no skill, B = SKILL.md. n=1 per cell — signal, not proof. One blind
judge per scenario; teams shuffled per scenario so neither arm kept a fixed
name. RED ran before the skill was drafted, and the drafting worked from the
recorded baseline failures.

Platform note: both arms ran on Claude Code. Every arm was told to invoke no
skill of its own, so A is a true baseline. No arm reached for
`superpowers:finishing-a-development-branch` or `requesting-code-review`.

Environment note: `git filter-repo` is not installed on this machine. The
`filter-branch` fallback in gate 1 is the path that will actually run here.

- S1 (branch carrying a plan and a spec): **B wins, 6/6 vs 1/6.** A kept the
  dated `docs/specs/` file on its own judgement, then removed the plan file
  with `git reset --soft` and one squashed commit — which drops the file but
  flattens a commit structure nobody asked it to touch. A never named a push
  flag, never audited comments, and never mentioned CI. A did two things
  better: it wanted to run the tests before rewriting anything, and it offered
  a `.gitignore` line for the plan path. Both folded in.
- S2 (comment audit): **B wins, 6/6 vs 4/6.** Both arms deleted the restated
  comment, kept the `time.monotonic` reason, and caught that the `rejected`
  counter does not exist. A lost on the class-level narrative: it rewrote the
  history into a fresh four-line rationale comment instead of deleting it,
  breaking the two-line ceiling. A framed the missing counter as a possible
  dropped feature rather than a stale sentence — folded in.
- S3 (PR body with a deployment concern): **B wins, 5/5 vs 4/5.** Both carried
  a deployment note naming the variable and the migration. A reprinted the diff
  as a five-bullet "What changed" list. A stated the consequence of the default
  for existing traffic — folded in.
- S4 (underspecified structural probe): **B wins, 3/3 vs 0/3.** A answered with
  generic pre-PR hygiene: read your diff, tidy "wip" commits, run the suite
  locally, write a description, flag soft spots, split scope. It never reached
  AI documents, comment currency, or CI, and it treated a local green suite as
  the verification step. B put all four gates on the agenda unprompted.
- S5 (negative: push, no PR): **B wins on restraint, and does not over-trigger.**
  B committed and pushed and stopped — no history rewrite, no `.md` scan, no
  comment audit, no PR body, no trailing advice. A stopped short of pushing at
  all and asked permission for a plan it had already decided.

Protocol deviation: in the S5 judge prompt, one bullet of arm A's output was
transcribed wrong and came out as a duplicate of the bullet above it. The judge
flagged it. The scenario turned on rubric line 1 (act versus ask), which the
error does not touch, so the verdict stands as logged.

Judge verdict: the skill arm wins all five, including the negative. Landing.
Obsolescence: no. The baseline failed a rubric line in four of five scenarios
and scored 0/3 on the structural probe — left alone it prepares a PR by
squashing the plan file away and calling a local test run verification.

### Regression — S1 after the fold-ins

The three fold-ins from arm A (pre-rewrite test baseline, `.gitignore` offer,
missing-identifier-as-dropped-feature) changed what gate 1 mandates, so S1 was
rerun against the edited skill. n=1. All six rubric lines still pass; the arm
now asks for the repo's test command before rewriting and names the
`filter-branch` fallback explicitly. S2–S5 were not rerun — the fold-ins do not
touch what they score.
