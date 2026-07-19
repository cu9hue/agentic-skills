# cpp-coding-standards — eval results

Append-only. Newest at the bottom.

## 2026-07-19 — backfill A/B, obsolescence check (skill as of 1bc330e)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof. First
check run under the structural-probe mandate.

- S1 (TempFile RAII class): **tie, 6/6 both** — near-identical move-only
  RAII deliveries; std::exchange moves, system_error, EINTR loop, const
  observers in both arms
- S2 (review, 8 planted violations): **tie, 8/8 both** — both caught the
  rule-of-five double-delete, macro-collision enum, ownership-leaking
  raw returns; baseline's extras marginally richer (chrono units,
  embedded-NUL)
- S3 (structural probe): **B, 5/5 vs 2/5 strict** — baseline organized its
  answer around tooling (sanitizers, CI, clang-format) and compressed
  const/type-safety defaults into one closing paragraph; skill arm
  organized around the guidelines in retrofit-pain order. Judge: citations
  flipped zero lines; the delta is organization, not knowledge.
- S4 (negative, std::move): **tie** — near-word-identical clean answers

Judge verdict: execution fully absorbed by the base model; the probe shows
the skill still sets the organizing structure of open-ended C++ advice.
Obsolescence: NO per the probe rule — kept. Caveats: the delta is emphasis
(baseline mentioned every concern), and baseline's tooling-first spine
carried real value the skill arm omitted (sanitizers, CI). If a future
model's probe answer organizes around the guidelines unaided, retire.
