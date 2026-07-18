# Skill-Authoring Skill — Design

Approved 2026-07-18.

## Purpose

Formalize this repo's skill-writing practice: mandatory persisted evals for
every skill, plus authoring rules. Incorporates the eval methodology from
Phil Schmid, "Testing Agent Skills" (philschmid.de/testing-skills) and the
existing pressure-testing convention (blind A/B subagent tests).

Motivation: eval scenarios are currently authored ad hoc in session
scratchpads and thrown away; edits to skills have no regression net. Codex
has no superpowers plugin, so this repo skill is also the only skill-writing
guidance on that side.

## Form

Self-contained repo skill at `.agents/skills/skill-authoring/`:

- `SKILL.md`
- `references/eval-template.md` — skeleton for a skill's `evals/` files

Named `skill-authoring` to avoid colliding with `superpowers:writing-skills`
in Claude's listing. On Claude it complements superpowers (which keeps the
deep TDD/bulletproofing theory — cross-reference, don't duplicate); on Codex
it stands alone.

## SKILL.md content

1. **Authoring rules.** Hard cap 500 lines for SKILL.md; repo target stays
   far leaner (~100). Description = trigger conditions only, never a workflow
   summary, under ~500 chars. Name short and plain. Heavy or verbatim
   material goes to `references/`; external sources credited in the
   `origin:` frontmatter line.
2. **Eval mandate.** New skill: write 3–5 scenarios including at least one
   negative should-not-trigger case; run the no-skill baseline BEFORE writing
   the skill (RED); then A/B with a blind judge; no commit until the skill
   arm wins. Skill edit: rerun that skill's persisted evals as regression;
   add a scenario when the edit targets new behavior.
3. **Eval format + runner protocol.** Per skill, inside the skill dir:
   - `evals/scenarios.md` — shared setup/material, then per-scenario user
     message, expected behaviors, judge rubric.
   - `evals/results.md` — append-only log: date, commit, per-scenario
     winner, one-line judge verdict.
   Runner is agent-native, no code: one subagent per arm per scenario
   (arm A = no skill, arm B = with skill), outputs anonymized into teams,
   blind judge scores against the rubric. Honest sample-size note required
   (n=1 per cell is signal, not proof).
4. **Obsolescence check.** The no-skill arm doubles as it: on any rerun, if
   the baseline arm passes everything, flag the skill for retirement — the
   base model absorbed its value.

## Migration and wiring

- Rescue today's socratic A/B test from scratchpad into
  `.agents/skills/socratic/evals/` as the worked example; seed its
  `results.md` from today's run.
- README: add `skill-authoring` entry.
- Update the `skill-edits-pressure-tested` memory to point at the skill as
  the canonical form of the convention.

## Verification

Dogfood: skill-authoring itself gets baseline-tested (RED on the new-skill,
edit, and negative scenarios), ships with its own `evals/`, and the A/B
result is logged in its `results.md`.
