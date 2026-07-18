# Socratic Skill — Design

Approved 2026-07-18.

## Purpose

A study skill that runs a Socratic questioning session over material the user
has read (paper, article, chapter, doc) to test and deepen their understanding.
Sibling to `ankify` and `digest-paper`. Based on the UConn CETL Socratic
questions taxonomy
(https://cetl.uconn.edu/resources/teaching-your-course/leading-effective-discussions/socratic-questions/).

## Trigger / scope

- `name: socratic`
- Use when: "run a socratic session on this", "quiz me on this paper",
  "check my understanding of this article".
- Not a lecture, not rote recall — it interrogates understanding of material
  the user has already read.

## Session protocol

1. **Read the source.** For a research paper, run `digest-paper` first (same
   move as `ankify`). Otherwise read directly.
2. **Extract core ideas** — the load-bearing concepts, same bar as `ankify`.
   Keep the list private during the session (showing it leaks answers); it is
   the coverage checklist.
3. **Dialogue.** One question per turn, never multi-part. Per idea, open with
   clarification and escalate through categories as answers warrant:
   assumptions, probing evidence, implications, viewpoints/counterarguments,
   occasionally questioning the question. Coverage of ideas drives the
   session; categories are technique. If the user nails an idea quickly, move
   on — never pad. User can steer: "next", "go deeper", "wrap up".
4. **Wrong or stuck: probe, then reveal.** Counter-question, hint, or
   counterexample — at most 2–3 probes on the same point, then explain plainly
   and mark it a gap. No guessing games.
5. **Tone.** Questions short and concrete; never lecture between questions;
   acknowledge good answers in one line without flattery; the user does the
   reasoning.
6. **Close: gap report + ankify handoff.** Report per idea: solid vs. gap,
   what tripped the user up, what to reread. Then invoke `ankify` over ALL
   covered ideas — solid and gapped alike — with gap cards phrased to target
   the exact miss.

## Structure

- `.agents/skills/socratic/SKILL.md` — protocol + one-line summary per
  category, pointing to the bank.
- `.agents/skills/socratic/references/question-bank.md` — the six UConn
  categories with example question stems verbatim, cited to the CETL page.
- Frontmatter `origin:` credits UConn CETL, per repo convention.

## Quality gate (in SKILL.md)

- one question per turn
- questions probe understanding, not recall
- reveal after ≤3 failed probes on a point
- every core idea covered or explicitly skipped by the user
- report covers every idea
- ankify runs at the end unless declined

## Verification

Blind A/B pressure test with subagents before committing the skill
(arm A = no skill, arm B = with skill), judged on Socratic quality:
one-question turns, probing over lecturing, adaptive escalation.
