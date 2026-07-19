# skill-authoring — eval results

Append-only. Newest at the bottom.

## 2026-07-18 — initial A/B (pre-commit)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof. Scenarios
judged as ordered plans, not executions.

- S1: **B**, 5/6 rubric lines vs 1/6 — baseline drafted then tested, kept
  evals in scratchpad, had no negative scenario and no stop-if-baseline-
  passes condition
- S2: **B**, 4/4 vs 1/4 — baseline invented a throwaway test instead of
  backfilling ankify/evals/, produced no results log, ran no obsolescence
  probe
- S3: **tie** — both arms made a surgical README edit with no ceremony; the
  skill arm correctly cited the cosmetic exemption (no over-triggering)

Judge verdict: skill arm decisive on both positive scenarios, clean on the
negative. Obsolescence: no — baseline failed most of S1/S2.

## 2026-07-19 — regression: line-norm edit (pre-edit ef58fe7 vs post-edit)

Edit under test: authoring rule "repo norm is ~100 lines" replaced with
"200–500 is the healthy range for a substantive skill (per Schmid); size to
the directives that bind; never pad toward the range". Arms: pre-edit vs
post-edit skill, all three scenarios as ordered plans, blind judge. n=1 per
cell — signal, not proof.

- S1: **post-edit**, by a hair — both fully process-compliant; judge flagged
  pre-edit's "~100 lines" target as a padding attractor while post-edit's
  "sized to what binds" read coherently
- S2: **post-edit**, narrowly — on an incidental mechanic (post-edit arm
  preserved pre-edit text via git show; pre-edit arm's plan couldn't run as
  written), unrelated to the norm change
- S3: tie — cosmetic exemption held in both arms, no ceremony

Judge verdict: post-edit wins narrowly, zero rubric-level regressions in
either direction. Edit holds — committed. Note: the sizing rubric line was
added to S1 for this run.
