# design-decision-tree — eval scenarios

How to run: one subagent per arm per scenario, identical prompts except which
SKILL.md the arm is given. Every arm is told to invoke no skill of its own, so
the no-skill arm is a true baseline. The subagent returns exactly the
deliverable — the next chat message it would send — and no meta-commentary.
Anonymize outputs into teams, blind-judge against the rubrics, log in
`results.md`.

Arms for a regression run: B = pre-edit SKILL.md (full walk only), C =
post-edit SKILL.md (two paths). Arm A = no skill runs alongside as the
obsolescence probe.

## Shared material

**Spec used by S3** — hand the arm this file at `docs/notify-spec.md`:

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

**CLI used by S5** — hand the arm this file at `cli.py`:

```python
import argparse, os, sys
from app.config import load_config

def main():
    p = argparse.ArgumentParser(prog="jobctl")
    p.add_argument("--config", default=os.environ.get("JOBCTL_CONFIG"))
    p.add_argument("command", choices=["run", "status"])
    args = p.parse_args()
    cfg_path, cfg = load_config(args.config)
    return {"run": run, "status": status}[args.command](cfg)

if __name__ == "__main__":
    sys.exit(main())
```

`load_config(path)` returns `(resolved_path, config_dict)`.

## S1 — capped triage on demo-shaped task text

User message: "Hackathon this weekend, demo Sunday afternoon, two days of work.
I want to build a tool that watches our Slack support channel and surfaces
recurring customer complaints as a ranked list. Grill me on it."

Rubric:
- returns at most 6 questions in **one** message — does not drip one per turn
- every question carries a concrete default: a specific thing the agent will do
  ("run over a JSON export of the last 90 days, no live connection"), not a
  restated preference ("choose a suitable ingestion approach")
- the top slots go to the widest-span, genuinely uncertain decisions —
  batch-over-export vs live stream, what "recurring" means and who decides it,
  whether anything persists between runs, whether the demo surface is a Slack
  bot or a standalone page
- no slot is spent on a question whose answer is predictable from the task text
  or from ordinary practice; a predictable answer sits below the line as a
  default however consequential it is
- no library or framework pick ("which embedding model", "Flask or FastAPI")
  occupies a top slot
- at least one question is scored on what the audience sees Sunday or on what
  fits in two days
- anything cut by the cap appears in a below-the-line block with its assumed
  default — nothing is dropped silently
- ends with the answering contract: answer a subset, skipped means default,
  "go" means all defaults
- the questions are ordered most-ambiguity-removed first, and one line says
  what the ranking is on — build order does not stand in for rank
- the defaults are coherent as a set: no two of them describe systems that
  contradict each other
- no default branches ("if X, do A, otherwise B") and none rests on another
  slot's answer without restating the assumption inside itself
- how the user will know the ranked list is right sits in a numbered slot, not
  below the line — the output is a judgment, so checking it is a tier-1 decision
- any default that assumes an unconfirmed stack or capability says so in its
  cost line
- if the defaults taken together walk away from the user's own framing (a
  batch job over an export is not a tool that "watches" a channel), that drift
  is raised as its own question rather than arrived at by two silent defaults

## S2 — explicit lower cap

User message: "We're adding an audit log: every write to the billing tables
gets recorded. Give me 3 questions."

Rubric:
- returns 3 questions, not 6
- the remaining candidates appear below the line with defaults rather than
  vanishing
- each of the 3 carries a concrete default
- the 3 chosen remove the most ambiguity — widest span, least predictable
  answer (what counts as a write and what a record contains; where the log
  lives and whether it is in the same transaction as the write; who can read it
  and whether it is append-only) rather than three easy or predictable ones

## S3 — document input still routes to the full walk

User message: "Interrogate docs/notify-spec.md — I don't want the implementer
guessing at anything."

Rubric:
- routes to the exhaustive path: builds and presents a decision tree with a
  count and branch structure before resolving anything
- does **not** answer with a capped round of six questions and stop
- processes decisions in dependency order and says what blocks what
- reaches the document rewrite as the endpoint, and does not write to disk
  without approval

## S4 — structural probe: underspecified ask

User message: "I'm building a rate limiter for our public API this week. What
should I get right?"

Rubric:
- answers with the open decisions that are not yet made, ranked, each with a
  default — not a generic checklist of rate-limiting best practice
- the ranking is by how much ambiguity each answer removes — span times
  uncertainty — and the reply shows that ordering rather than listing
  decisions flat
- reaches the decisions that reshape the system (per-key vs per-IP vs
  per-account, where the counter state lives, what happens when the store is
  down, whether limits are enforced or observed first) rather than stopping at
  algorithm choice
- does not ask the user for facts it could look up in the repo

## S5 — negative: should not trigger

User message: "Add a `--verbose` flag to this CLI that prints the resolved
config path before running."

Rubric:
- makes the change, or asks the one thing it genuinely cannot determine
- no question round, no cap, no blast-radius ranking, no below-the-line block
- behaves as if the skill were absent
