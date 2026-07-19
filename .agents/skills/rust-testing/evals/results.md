# rust-testing — eval results

Append-only. Newest at the bottom.

## 2026-07-19 — backfill A/B, obsolescence check (skill as of 241df13)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof.

- S1 (write tests): **17/18 lines each overall**; one arm missed a
  whitespace case (deferred it as an explicit question), the other covered
  it. Both asserted exact ParseError variants, used #[cfg(test)] mods, no
  should_panic.
- S2 (review, 7 planted violations): **7/7 vs 6/7** — one arm missed the
  real-side-effects/no-fakes plant; both nailed static-mut-as-UB, the
  parallel-execution race, and should_panic-without-expected
- S3 (structural probe): **tie, 5/5 both** — both unprompted: cfg(test) vs
  tests/ split, trait seams + mockall, fmt/clippy/test/llvm-cov ratcheted
  CI gate, error-path rigor with matches!, proptest
- S4 (negative): **tie** — both terse, no lecture

Judge verdict: "evidence points to obsolescence, not a delta" — identical
totals, misses on different marginal lines within run-to-run noise, all 5
strict probe lines hit unaided by both arms. Obsolescence: YES. Retired.
