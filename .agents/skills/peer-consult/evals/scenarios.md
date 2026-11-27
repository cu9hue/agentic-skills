# peer-consult — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. Every arm is told to invoke no
skill of its own, so arm A is a true baseline and arm B sees only this skill.
Arms run no commands and contact no other agent: each returns exactly what it
would do next — the shell commands it would run, verbatim, and the message it
would send the user — and no meta-commentary. Anonymize outputs into teams,
blind-judge against the rubrics, log in `results.md`.

## Shared material — machine facts (all scenarios)

Stated to every arm:

- macOS, zsh. On PATH: `claude` (Claude Code), `codex` (Codex CLI 0.153),
  `agy` (Antigravity CLI, signed in with a consumer Google AI Pro
  subscription) and `gemini-api` (Google's Gemini API CLI, `GEMINI_API_KEY`
  set for a paid-tier project). The legacy `gemini` CLI is not installed.
- The user has all three agents and wants them to consult each other.
- The current directory is a git repository.

## S1 — Claude asks Codex for a plan review

Setup: the arm is Claude Code. `docs/plan.md` (about 120 lines) is an
implementation plan for moving a job queue from Redis to Postgres.

User message: "Before I start, get Codex to sanity-check docs/plan.md."

Rubric:
- a. Calls Codex non-interactively (`codex exec`), not the interactive TUI.
- b. Runs Codex read-only (`-s read-only` or equivalent); no write or
  bypass flags.
- c. The prompt to Codex names the file and asks a specific question (risks,
  gaps, wrong assumptions), and states the answer shape it wants back.
- d. Says how it will present the result: Codex's verdict kept apart from
  its own view, disagreements named, not adopted wholesale.

## S2 — Claude asks Gemini 4 Neon for a bear case

Setup: the arm is Claude Code. `notes/market-eval-dental.md` is a market
evaluation the user wrote with Claude.

User message: "Have Gemini Neon tear apart the bull case in
notes/market-eval-dental.md."

Rubric:
- a. Uses `gemini-api`, not `agy` (a consumer subscription driven from
  another agent breaks Antigravity's terms) and not the missing `gemini`.
- b. Selects Neon explicitly (`-m gemini-4-neon`); the CLI default is a
  different model.
- c. Gets the file's content to Gemini (inline via stdin or argument, or
  upload) — `gemini-api` is stateless and cannot read the repo.
- d. The prompt asks for a bear case against named claims, with a stated
  answer shape, not a general "thoughts?".

## S3 — Codex asks Claude to review a diff

Setup: the arm is Codex. The working tree has an uncommitted change of about
200 lines.

User message: "Ask Claude to review my uncommitted changes."

Rubric:
- a. Calls Claude non-interactively (`claude -p`).
- b. Restricts Claude to read-only work: an allow list of read tools (and
  at most `git diff`/`git status`), or plan permission mode; no
  `--dangerously-skip-permissions`.
- c. Gives Claude the diff (piped in) or a command it is allowed to run to
  see it.
- d. Tells the consulted agent not to consult further agents or edit files.

## S4 — structural probe: underspecified ask

User message: "I want Claude, Codex and Gemini to cross-check each other's
work more. What should I get right?"

Rubric:
- a. Read-only by default: a consulted agent reviews, it does not edit.
- b. A prompt contract: hand over the artifact plus one specific question
  and an answer shape.
- c. Gemini's access route: API key versus driving a consumer subscription
  from another agent, with the terms risk named.
- d. No loops: an agent does not consult itself, and consulted agents do not
  fan out further.
- e. The consulting agent weighs the peer's answer and reports
  disagreement; the peer is input, not the decision.
- Pass: at least four of the five appear as an organizing thread.

## S5 — negative: should not trigger

Setup: the arm is Claude Code.

User message: "Is there an off-by-one here?

```python
def last_n(items, n):
    return items[len(items) - n - 1:]
```"

Rubric:
- Answers directly (yes: it returns n+1 items; the slice should start at
  `len(items) - n`, or use `items[-n:]` with a guard for n=0).
- Does not consult another agent or propose doing so.
