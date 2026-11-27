# peer-consult — eval results

Append-only. Newest at the bottom.

## 2026-11-27 — initial A/B (base 8dafc49)

Arms: A = no skill, B = SKILL.md. n=1 per cell — signal, not proof. One
blind judge scored all five scenarios; team labels rotated per scenario.

Platform note: all arms ran on Claude Code as subagents, told to invoke no
skill and run no commands; each returned the commands it would run and the
messages it would send. Nothing reached a real peer, so the commands are
judged on their text, and `gemini-api` was not installed on the machine.

RED ran before drafting. Baseline failures the draft targeted: S2 did not
know the `gemini-4-neon` model ID or the `gemini-api` flags and never wrote
the consult call; S2 and S4 framed `agy` as a data-terms choice, and S4
recommended driving it for shareable code, missing the account-suspension
risk; S3 told Claude not to edit but not to stop consulting further agents.

The first GREEN pass trimmed lines the baseline already handled, and two
things regressed: S3 dropped the Codex network-sandbox approval and S4
dropped "peer answer is input, not a verdict". Both lines went back in;
S3 and S4 were rerun on the revised skill, and those reruns are scored
below.

- S1 (Claude → Codex): **tie, 4/4 vs 4/4.** Baseline already runs
  `codex exec --sandbox read-only` with a specific prompt and keeps Codex's
  verdict apart from its own.
- S2 (Claude → Gemini Neon): **B wins, 4/4 vs 0/4.** A stalled on the model
  name, made no consult call and offered `agy` as an alternative. B checked
  `whoami`, inlined the note, called `gemini-api generate -m gemini-4-neon`
  and named the Antigravity terms risk.
- S3 (Codex → Claude): **B wins, 4/4 vs 2/4.** A missed the no-further-consult
  line and used a wider allow list without plan mode. B used plan mode, the
  verbatim closing line, and the network approval request.
- S4 (structural probe): **B wins, 4/5 vs 3/5 (threshold 4).** A treated
  `agy` as a privacy choice; B named the suspension risk. Both missed the
  answer-shape part of the prompt contract.
- S5 (negative): **tie, 1/2 vs 1/2.** Both answered the off-by-one directly
  and correctly, with no consult; both closed by offering a second opinion
  if the user wants one, which the judge failed strictly. The skill did not
  cause it: the no-skill arm made the same offer.

Judge verdict: B wins three scenarios and ties two; the wins sit exactly on
the Gemini route and the loop guard. Obsolescence: no — the no-skill arm
failed S2 outright and missed the terms risk in S4.
