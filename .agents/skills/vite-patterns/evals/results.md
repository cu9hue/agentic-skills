# vite-patterns — eval results

Append-only. Newest at the bottom.

## 2026-07-19 — backfill A/B, obsolescence check (skill as of fcb4361)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof. S1 arm A
reused from the earlier orchestrator fleet (same scenario prompt).

- S1 (author config): **tie, 7/7 both** — near-identical configs: tsconfig
  paths plugin, full proxy wiring, host:true, react-vendor chunk, checker
  plugin, coherent rolldown-era versioning
- S2 (review, 7 planted mistakes): **tie, 7/7 both, no false positives** —
  baseline additionally caught the scoped-package/.pnpm parsing bug in the
  planted manualChunks
- S3 (library mode + VITE_ secret): **tie, 6/6 both** — both externalized
  react/react-dom/jsx-runtime, prescribed dts, refused the secret with the
  correct server-side/opt-in pattern
- S4 (negative, useDebounce): **A** — skill arm appended process narration
  ("I read the vite-patterns skill first…"); marginal pass on the letter,
  cost it the scenario

Judge verdict: baseline passed all 24 rubric lines and won overall by S4
discipline. Obsolescence: YES — the no-skill arm passed everything and
matched or beat the skill arm per scenario. Retired.
