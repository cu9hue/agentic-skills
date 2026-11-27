---
name: peer-consult
description: Use when one coding agent should consult another — "ask Codex", "have Gemini review this", "get Claude's take", "second opinion from Neon", "cross-check with another model" — or when the user asks how to set up cross-checks between Claude, Codex and Gemini. Not for subagents of the same agent, and not for a question you can answer by reading the code.
origin: commands checked against claude 2.x and codex-cli 0.153 --help on 2026-11-27; gemini-api flags from aistudio.google.com/docs/cli and two hands-on guides (eraofminds.com, bettertoken.ai), Nov 2026; Antigravity terms from antigravity.google FAQ via leanopstech.com
---

# Peer Consult

One agent asks another for a read-only review and brings the answer back.
Claude Code, Codex and the Antigravity CLI all read this file from
`.agents/skills`, so the same rules hold in every direction.

## Pick the peer

- You are Claude: consult Codex or Gemini. You are Codex: consult Claude or
  Gemini. You are Gemini in `agy`: consult Claude or Codex.
- Reach Gemini through `gemini-api` with an API key. Do not drive `agy` from
  another agent: on a consumer Google AI plan, Antigravity's terms forbid
  third-party wrapping, and accounts were suspended for it in November 2026.
  This is an account risk, not a data-privacy preference, so it holds for
  public code too. To enforce it in Claude Code, add `Bash(agy:*)` to
  `permissions.deny`.
- If `gemini-api` is missing (`command -v gemini-api` prints nothing), tell
  the user and stop. Install docs: https://aistudio.google.com/docs/cli. Do
  not fall back to `agy` or the legacy `gemini` CLI.

## Commands

Every consult runs read-only. Write the prompt to a file first and pass it
in, so quoting stays sane and the run is reproducible.

| Peer | Command |
|---|---|
| Codex | `codex exec -s read-only -o "$OUT" "$(cat "$PROMPT")" < /dev/null` |
| Claude | `claude -p --permission-mode plan --allowedTools "Read,Grep,Glob,Bash(git diff:*),Bash(git status:*),Bash(git log:*)" "$(cat "$PROMPT")" > "$OUT"` |
| Gemini, text up to ~500 KB | `gemini-api generate -m gemini-4-neon "$(cat "$PROMPT")" > "$OUT"` |
| Gemini, PDF or large file | `URI=$(gemini-api files upload ./file --wait)` then `gemini-api analyze -i "$URI" -m gemini-4-neon "$(cat "$PROMPT")" > "$OUT"` |

Gemini facts the commands depend on:

- `gemini-api` is a stateless API client. It cannot read the repo, so the
  prompt file must contain the artifact itself: paste the file or the
  `git diff` output into it.
- Name the model on every call. The default for `generate` and `analyze` is
  Gemini 4 Hydrogen, not Neon. Use `gemini-4-carbon` when the user asks for
  Carbon.
- Neon and Carbon are not on the free tier: $3 / $15 per million tokens for
  Neon. Mention the cost when the artifact is large.
- Run `gemini-api whoami` once before the first call. An exported
  `GEMINI_API_KEY` overrides the key in the keychain and can bill a
  different project.

When Codex is the caller, its default sandbox blocks the network that
`claude` and `gemini-api` need: ask the user to approve that one command.

## The prompt

Give the peer the artifact (a path Codex or Claude can read, or the content
itself for Gemini), one specific question, and the answer shape you want
back. End every prompt with this line, verbatim, so consults never chain
into loops:

> You are being consulted read-only. Do not edit files, and do not consult
> any other agent or model.

The peer's answer is input, not a verdict. Check each finding against the
artifact, and report it under the peer's name with your agreement or
disagreement beside it.
