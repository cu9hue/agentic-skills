# grill-with-docs — eval scenarios

How to run: one subagent per arm per scenario, identical prompts except which
SKILL.md the arm is given. Every arm is told to invoke no skill of its own.
The skill is user-invoked, so each user message starts with the command. The
subagent returns exactly the next chat message it would send. Anonymize,
blind-judge against the rubrics, log in `results.md`.

S1, S2 and S4 come from the former design-decision-tree skill, whose capped
round now lives here; its history is in `design-decision-tree-results.md`.

## Shared material

**Spec used by S3** — give the arm this file as `docs/notify-spec.md`:

```markdown
# Notification service

## Goal
Users get told when a job they started finishes, succeeds or fails.

## Delivery
Send by email. Add push later. Users can turn notifications off.

## Storage
Keep a record of what we sent so we can show a history page.

## Failure handling
If sending fails, retry. Don't lose the notification.
```

## S1 — capped round on demo-shaped task text

User message: "/grill-with-docs Hackathon this weekend, demo Sunday
afternoon, two days of work. I want to build a tool that watches our Slack
support channel and surfaces recurring customer complaints as a ranked list.
Grill me on it."

Rubric:
- returns at most 6 questions in one message, not one per turn
- every question carries a concrete default (a specific thing the agent will
  do), not a restated preference
- the top slots go to the widest-span, genuinely uncertain decisions: batch
  over an export vs live, what "recurring" means and who decides, whether
  anything persists between runs, Slack bot vs standalone page
- no slot goes to a predictable answer or a library pick
- at least one question is about what the audience sees Sunday or what fits
  in two days
- how the user will know the ranked list is right sits in a numbered slot
- everything cut by the cap appears below the line with its default
- ends with the answering contract: answer a subset, skipped means default,
  "go" means all defaults
- ordered most-ambiguity-removed first, with one line naming the ranking

## S2 — explicit lower cap

User message: "/grill-with-docs We're adding an audit log: every write to
the billing tables gets recorded. Give me 3 questions."

Rubric:
- returns exactly 3 questions, each with a concrete default
- the remaining candidates appear below the line with defaults
- the 3 remove the most ambiguity (what counts as a write and what a record
  holds; where the log lives and whether it shares the write's transaction;
  who reads it and whether it is append-only)

## S3 — a spec routes to full grilling

User message: "/grill-with-docs docs/notify-spec.md — I don't want the
implementer guessing at anything."

Rubric:
- runs full grilling: asks the whole current frontier as one numbered round,
  each with a recommended answer, and waits for answers
- does not answer with a capped round and the "go = all defaults" contract
  and stop
- holds back questions that depend on answers not yet given
- challenges at least one fuzzy term in the spec ("notification", "record",
  "turn off", "lose") and offers to record settled terms in `GLOSSARY.md`
- offers no ADR yet, or only for a decision that is hard to reverse,
  surprising and a real trade-off

## S4 — structural probe: underspecified ask

User message: "/grill-with-docs I'm building a rate limiter for our public
API this week. What should I get right?"

Rubric:
- answers with ranked open decisions, each with a default, not a generic
  best-practice checklist
- the order shows ambiguity removed (span times uncertainty), not a flat list
- reaches the decisions that reshape the system (per-key vs per-IP vs
  per-account, where counter state lives, what happens when the store is
  down, enforce vs observe first) rather than stopping at algorithm choice
- asks the user for no fact it could look up

## S5 — negative: nothing worth grilling

User message: "/grill-with-docs Add a `--verbose` flag to this CLI that
prints the resolved config path before running."

Rubric:
- says there is little or nothing to decide, and asks at most the one thing
  it cannot determine, or proposes to just make the change
- no six-question round, no below-the-line block, no glossary or ADR
