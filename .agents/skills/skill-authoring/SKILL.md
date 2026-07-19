---
name: skill-authoring
description: Use when creating a new skill in this repo, editing what an existing skill mandates, or backfilling evals for a legacy skill. Not for cosmetic changes that leave behavior untouched — typos, README blurbs, formatting.
origin: eval methodology adapted from Phil Schmid, "Testing Agent Skills" (philschmid.de/testing-skills); the 200-500-line range is from Schmid's talk, reporting Gemini-team testing across a skill corpus; process merged with the superpowers writing-skills RED-GREEN-REFACTOR practice
---

# Skill Authoring

Every skill in this repo ships with persisted evals, and no behavior change
commits until it wins a blind A/B. Skills are prompts, and prompts regress
silently — the evals in each skill's directory are the regression net. On
Claude, `superpowers:writing-skills` holds the deeper TDD and bulletproofing
theory; this skill is the repo's binding process. On Codex it stands alone.

## Authoring rules

- SKILL.md hard cap: 500 lines; 200–500 is the healthy range for a
  substantive skill (per Schmid). Size to the directives that bind: never
  pad a thin skill toward the range, and move verbatim or heavy reference
  material into `references/` regardless of length.
- `description:` = trigger conditions only — situations and symptoms, "use
  when…" — never a summary of the workflow (agents follow summaries instead
  of reading the body). Under ~500 chars, with one "not for" boundary.
- `name:` short and plain; check the skill listing for collisions with
  plugin skills before choosing.
- Verbatim external material and heavy reference go to `references/`;
  credit sources in the `origin:` frontmatter line.
- Directives, not suggestions: "ask one question per turn", never
  "consider asking".

## The eval mandate

**New skill:**

1. Write `<skill>/evals/scenarios.md` first — 3–5 scenarios, at least one
   negative (a request where the skill should NOT change behavior) and at
   least one underspecified structural probe: a vague "what should I get
   right?" ask that names no axis. Well-specified prompts pre-empt a
   skill's attention value — the base model writes accessible forms when
   told to build a form, but only a vague probe shows whether the skill
   puts its concerns on the agenda unprompted. Test both execution and
   attention. Skeleton: `references/eval-template.md`.
2. RED: run every scenario against baseline (no skill) BEFORE drafting the
   skill, and record what failed — those failures are what the skill must
   say. If baseline already passes everything, the skill is unnecessary:
   stop.
3. Draft the skill against the recorded failures.
4. GREEN: rerun the scenarios with the skill loaded, blind-judge against the
   baseline outputs, fix and retest until the skill arm wins.
5. Append the verdict to `evals/results.md`. Commit skill and evals
   together.

**Skill edit (any change to what it mandates):**

1. Rerun the skill's persisted evals as regression — pre-edit arm vs
   post-edit arm. Legacy skill with no `evals/`? Backfill scenarios first;
   never invent a throwaway test in scratchpad instead.
2. If the edit targets behavior no scenario covers, add a scenario for it.
3. Append the rerun to `results.md`. No commit until the post-edit arm
   holds.

**Cosmetic changes** — typos, README blurbs, formatting — commit plainly.
No ceremony.

## Runner protocol (agent-native, no code)

- One subagent per arm per scenario, prompts identical except skill
  presence. The subagent returns exactly the deliverable (e.g. the next
  chat message), no meta-commentary.
- Anonymize arms into teams. A separate blind-judge subagent scores each
  scenario's rubric — harsh, no credit for style.
- Log per-scenario winner and a one-line verdict in `evals/results.md`,
  append-only, with date and commit.
- State the sample size: n=1 per cell is a signal, not proof. Real usage is
  the ongoing eval — feed observed failures back in as new scenarios.

## Obsolescence check

Every rerun's no-skill arm doubles as an obsolescence probe: if baseline now
passes every rubric, the base model has absorbed the skill's value — flag it
for retirement rather than keeping it loaded. No retirement on execution
scenarios alone: the structural probe must also show no delta, or the skill
may still be earning its keep as attention allocation (frontend-a11y was
retired and reversed the same day on exactly this).

## Quality gate

- `evals/scenarios.md` and `evals/results.md` committed with the skill
- baseline ran before drafting (new) or before landing (edit)
- at least one negative scenario, and the skill arm does not over-trigger
  on it
- at least one underspecified structural probe, and retirement verdicts
  cite its result
- blind judge, per-scenario rubrics, sample size stated in the log
- description is triggers-only and ≤~500 chars; SKILL.md ≤500 lines
- external sources credited in `origin:`
