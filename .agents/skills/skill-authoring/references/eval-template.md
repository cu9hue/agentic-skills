# Eval template

Copy into `<skill>/evals/` as two files. Keep scenarios lean — 3–5, each
single-shot testable (the subagent returns one deliverable that a judge can
score against the rubric without running a whole session).

## scenarios.md

```markdown
# <skill> — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
skill loaded), identical prompts otherwise. Anonymize outputs into teams,
blind-judge against the rubrics, log the verdict in `results.md`.

## Shared material

<Any input the scenarios need — an article, a diff, a repo state. Describe
it precisely enough to reconstruct; inline it if short.>

## S1 — <name>

User message: "<verbatim>"

<Optional transcript/setup so the scenario is single-shot.>

Rubric:
- <observable pass/fail check>
- <observable pass/fail check>

## S2 — …

## S<n> — structural probe: underspecified ask

User message: "<a vague 'I'm doing X this week, what should I get right?'
ask in the skill's domain, naming no axis and no requirements>"

Rubric:
- <the skill's core concerns structure the answer unprompted — name the
  2-4 topics that must appear for a pass>
- <the concerns are an organizing thread, not one bullet>

## S<n> — negative: should not trigger

User message: "<a nearby request the skill must leave alone>"

Rubric:
- behaves as if the skill were absent (no ceremony, no withheld deliverable)
```

## results.md

```markdown
# <skill> — eval results

Append-only. Newest at the bottom.

## <YYYY-MM-DD> — <initial A/B | regression for <edit>> (commit <sha>)

Arms: <A = no skill, B = skill | B = pre-edit, C = post-edit>. n=<k> per
cell — signal, not proof.

- S1: **<winner>** <one line: what separated the arms>
- …

Judge verdict: <one line>. Obsolescence: <yes/no — did the no-skill arm pass
everything?>
```
