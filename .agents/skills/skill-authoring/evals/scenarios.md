# skill-authoring — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
skill loaded), identical prompts otherwise. Each scenario asks for an ordered
plan, not execution ("state the exact steps you would take, in order; make no
file changes") — judge the process, cheaply. Anonymize outputs into teams,
blind-judge against the rubrics, log in `results.md`.

## Shared material

The subagent works in this repo's root and is told: skills live in
`.agents/skills/<name>/SKILL.md`, shared to Claude Code and Codex; it may
look around the repo.

## S1 — new skill

User message: "Add a new skill to this repo: a skill for writing good git
commit messages."

Rubric:
- eval scenarios are authored BEFORE the skill is drafted, and the no-skill
  baseline runs before drafting (test-first, not draft-then-test)
- evals persist in the skill's own `evals/` directory (scenarios + results
  log committed with the skill) — scratchpad-only tests fail
- scenario set includes a negative should-not-trigger case
- blind/anonymized judging with per-scenario rubrics; honest sample size
- lean-skill rules observed: triggers-only description, references/ for
  heavy material, origin attribution

## S2 — edit to an evals-less legacy skill

User message: "The ankify skill's 'value bar' section feels wordy — tighten
it without changing what it mandates."

Rubric:
- reruns persisted evals as the regression net; finding none, BACKFILLS
  `ankify/evals/` rather than inventing a throwaway scratchpad test
- pre-edit vs post-edit arms compared blind
- rerun appended to `evals/results.md`; no commit until the post-edit arm
  holds
- mentions the obsolescence signal (no-skill arm passing everything)

## S3 — negative: cosmetic change, no ceremony

User message: "The README's one-line description of the ankify skill is out
of date — refresh it to match what the skill actually does. Don't touch the
skill itself."

Rubric:
- plans a surgical README edit and commit; does NOT require evals, A/B
  runs, or a results-log entry for a change that alters no skill behavior
