# second-brain-retrieval — eval results

Append-only. Newest at the bottom.

## 2026-08-31 — initial A/B (base 275519d)

Arms: **A** = no skill (baseline, RED ran before the skill was drafted),
**B** = SKILL.md inlined. n=1 per cell — signal, not proof. Live service
during the run; all calls read-only, no arm called `/capture`. One blind
judge scored anonymized, per-scenario-shuffled outputs.

- S1: **B** — A grepped the vault on disk, cited the `_sources/` PDF, no
  chunk IDs; B searched the service, retrieved, cited path › heading ›
  chunk ID.
- S2: **B** — A read the skills repo's git history and never touched the
  service; B used `/recent` and marked its re-read picks as inference.
- S3: **B** — A read vault files directly (good content, no chunk IDs, no
  service); B cited chunk IDs for every claim with inference fenced off,
  wrote nothing.
- S4: **B** — A grepped local files; B searched the service three ways,
  stated a clean miss, and only offered capture.
- S5: **tie** — both delivered the curl loop with no retrieval ceremony; B
  did not over-trigger.

Judge verdict: "in every knowledge scenario the winner is simply whichever
output actually queried the second-brain HTTP service" — decoded, that is B
4–0 with the negative a tie. Obsolescence: no — the no-skill arm never used
the service, cited no chunk IDs, and surfaced `_sources/` (S1); the
structural probe (S3) shows the same mechanism gap.

Known service issue at eval time: `POST /related` returned HTTP 500 for
every request-body shape tried (`chunk_id`, `note_path`, `id`, `path`); the
skill documents it per the API contract. Re-verify the example once the
endpoint is fixed.
