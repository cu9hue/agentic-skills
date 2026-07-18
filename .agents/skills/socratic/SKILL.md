---
name: socratic
description: Use when the user wants to test and deepen their understanding of material they have read — a paper, article, chapter, or doc — through Socratic dialogue. Triggers like "run a socratic session on this", "quiz me on this paper", "check my understanding". Not for material the user has not read yet.
origin: question taxonomy from UConn CETL, "Socratic Questions" (cetl.uconn.edu/resources/teaching-your-course/leading-effective-discussions/socratic-questions/); session protocol synthesized here
---

# Socratic

Run a questioning session that makes the user do the reasoning. Deep
understanding means they can state an idea in their own words, defend it,
attack it, and connect it — reciting the text back proves none of that. Your
questions are the instrument; you never lecture between them.

## When to Use

- the user has read a paper, article, chapter, or doc and wants their
  understanding tested and deepened
- "run a socratic session", "quiz me on this", "check my understanding"

Not for material the user has not read, and not rote recall — every question
should require reasoning, not retrieval.

## How it runs

1. **Read the source.** For a research paper, run the `digest-paper` skill
   first if you have not — its passes surface the load-bearing claims.
   Otherwise read directly.
2. **Extract the core ideas** — the load-bearing concepts the source is built
   on, same bar as `ankify`. This list is your coverage checklist. Keep it
   private during the session: showing it leaks answers. Tell the user they
   can steer at any time with "next", "go deeper", or "wrap up".
3. **Interrogate one idea at a time, one question per turn.** Never bundle
   questions. Open an idea with a clarification question, then escalate
   through the categories as the answers warrant: assumptions → reasons and
   evidence → implications → viewpoints and counterarguments → occasionally
   questioning the question itself. Stems for all six categories:
   `references/question-bank.md`. Coverage of ideas drives the session;
   categories are technique. Ask for the claim before you interrogate it:
   the user states the idea in their own words first — a question that quotes
   the source's answer to a point not yet probed has already graded it
   correct. An idea is covered when the user has stated it
   in their own words and survived at least one push on its weakest point —
   when they nail it fast, move on. Never pad.
4. **Wrong or stuck: probe, then reveal.** Respond with a counter-question,
   counterexample, or hint that narrows the search without containing the
   answer. After 2–3 failed probes on the same point, explain it plainly and
   mark it a gap — a guessing game teaches nothing. Track every reveal and
   every shaky answer; they feed the close.
5. **Close with a gap report.** When the checklist is covered or the user
   wraps up, report per idea: solid or gap, what specifically tripped them
   up, and which part of the source to reread for each gap.
6. **Hand off to `ankify`.** After the report, run the `ankify` skill over
   all covered ideas — solid and gapped alike; solid understanding still
   fades without review. Phrase gap cards to target the exact miss from the
   session, not the generic concept.

## Tone

Questions short and concrete, adapted to this text — never generic stems
verbatim. Acknowledge a good answer in one line, without flattery, then move.
The user reasons; you steer.

## Quality gate

- one question per turn, every turn
- every question requires reasoning about the material, not recall of it
- no question hands the user a claim they have not yet produced themselves
- no explanation given before 2–3 probes failed; none withheld after
- every core idea covered or explicitly skipped by the user
- gap report names what tripped the user up and what to reread
- ankify runs at the end, over solid ideas too, unless the user declines
