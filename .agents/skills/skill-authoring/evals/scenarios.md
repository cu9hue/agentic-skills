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
- scenario set includes an underspecified structural probe (a vague
  no-axis-named ask testing whether the skill's concerns surface
  unprompted)
- blind/anonymized judging with per-scenario rubrics; honest sample size
- lean-skill rules observed: triggers-only description, references/ for
  heavy material, origin attribution
- sizing guidance coherent: skill sized to its binding directives, no
  padding toward any line target, under the 500-line cap

## S2 — edit to an evals-less legacy skill

User message: "The landing-copy skill's 'The Principle' section feels
wordy — tighten it without changing what it mandates."

(Was ankify until 2026-11-27; ankify has evals now, so it no longer tests
the backfill path. Move this to another evals-less skill if landing-copy
gets evals.)

Rubric:
- reruns persisted evals as the regression net; finding none, backfills
  `landing-copy/evals/` rather than inventing a throwaway scratchpad test
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

## S4 — the default model changed (added 2026-11-27)

User message: "We just moved our default model from Opus 5.5 to Fable 5.2.
Do any of our skills need attention?"

Rubric:
- plans to rerun each skill's no-skill arm (its structural probe and at
  least one execution scenario) against the new model, not only to read
  the skills and judge by eye
- logs each rerun in that skill's `evals/results.md`
- no retirement on execution scenarios alone; a retirement verdict cites
  the structural probe
- a prompt or config audit, if mentioned, is a first pass, not the verdict

## S5 — a rule that cannot be taken back (added 2026-11-27)

User message: "Add a skill that keeps the agent from force-pushing or
running `git reset --hard` in my projects."

Rubric:
- the plan enforces the rule in the harness (a PreToolUse hook that blocks
  the command, or a deny rule in settings), not only in skill prose; the
  skill sets up or names that mechanism
- if a hook must send the agent back, the plan uses exit code 2, or
  otherwise makes the block actually stop the command
- the planned skill wording is plain: no IMPORTANT, NEVER, CRITICAL or
  all-caps emphasis
- the eval mandate still applies: scenarios first, a no-skill baseline, a
  negative and a structural probe

## S6 — third-party skill copied in (added 2026-11-27)

User message: "Copy the `prototype` skill from mattpocock/skills (MIT)
into this repo so I can use it in Claude Code and Codex. Keep it as he
wrote it."

Rubric:
- credits the source: an `origin:` naming the upstream repo and commit,
  and the upstream license file in the skill's folder
- does not author evals or run an A/B for an unchanged third-party copy
- says that changing what the skill tells the agent to do would bring it
  under the eval mandate
