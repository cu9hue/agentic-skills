# coding-standards — eval results

Append-only. Newest at the bottom.

## 2026-07-19 — backfill A/B, obsolescence check (skill as of fcb4361)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof. Scenarios
authored by an orchestrator agent, arms re-run directly after an API
incident killed the first attempt.

- S1 (write fetch/retry module): **B, 7/7 vs 5/7** — baseline used
  abbreviated `res`/`err` (banned class, marginal) and left one arrow
  function's return type unannotated; both parallelized, named constants,
  handled errors
- S2 (review, 8 planted violations): **tie, 8/8 both** — baseline's review
  was actually deeper (caught wasted pre-check fetches and the ambiguous
  return contract); skill arm cited line numbers as asked
- S3 (refactor): **B, 6/6 vs 5/6** — the delta is immutability-by-default:
  baseline honored "keep behavior identical" literally and delivered the
  mutating version (flagged, with immutable alternative); skill arm
  delivered immutable and flagged the deviation. Judge: defensible reading,
  not a blunder.
- S4 (negative, PATCH vs PUT): **tie** — both direct, no ceremony

Judge verdict: skill arm 21/21 lines, baseline 18/21; all three baseline
misses are soft (style-class naming, one annotation, a judgment call).
Obsolescence: PARTIAL — the base model has the substance (reviews were
equally deep); what the skill still buys is defaults under ambiguity:
immutability first, full annotation, unabbreviated names. Keep/retire is a
judgment call on whether those defaults matter to the user.
