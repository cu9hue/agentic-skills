# Global Instructions

Cross-project, cross-agent instructions. Shared by both Claude Code and Codex
via `@import` from `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md`.

Canonical source: `<repo>/.agents/GLOBAL.md`, surfaced at `~/.agents/GLOBAL.md`
through the `~/.agents` symlink. Edit here once; both agents pick it up in every
project.

Keep this file agent-agnostic. Agent-specific guidance (e.g. Claude-hook or
RTK-proxy details) stays in the separately-imported `RTK.md`.

These rules bias toward caution over speed. For trivial changes, use judgment.
Some guidance adapts Andrej Karpathy's observations on LLM coding pitfalls
(<https://x.com/karpathy/status/2015883857489522876>).

## Before you write code

- State your assumptions. If uncertain, ask instead of guessing.
- If multiple interpretations exist, present them. Don't pick one silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop and name what's confusing.

## Keep it minimal

- Write the minimum code that solves the problem. Nothing speculative.
- No features, abstractions, configurability, or error handling that wasn't
  asked for or can't happen.
- Ship a complete, working solution first, then iterate.
- If you wrote 200 lines and it could be 50, rewrite it.

## Work with the grain of the repo

- Follow existing patterns. Write idiomatic code with clear separation of
  concerns and interfaces that support testing.
- Search the repo before adding anything. Reuse existing helpers. Don't
  introduce a new pattern when one already exists.
- Make surgical edits: every changed line traces to the request. Match the
  existing style even if you'd do it differently.
- Don't refactor what isn't broken. Mention unrelated dead code, don't delete it.
- Remove only the imports, variables, and functions your own change orphaned.

## Tests

- Tests call the real code. Never reimplement or rewrite business logic in a
  test.
- Reproduce a bug with a failing test, then make it pass.
- Pipe test output to a file, then grep the file, so there's a saved record.

## Comments and docs

- Comments explain what isn't obvious from the code. Skip the rest.
- Don't create new Markdown docs unless explicitly asked.

## Finish the job

- Turn the task into verifiable success criteria, then loop until they pass.
- Fully complete the work. No TODOs, no deferring to a follow-up PR.
