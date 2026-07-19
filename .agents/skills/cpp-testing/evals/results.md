# cpp-testing — eval results

Append-only. Newest at the bottom.

## 2026-07-19 — backfill A/B, obsolescence check (skill as of 241df13)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof.

- S1 (write GoogleTest tests): **tie, 5/6 both** — and both failed the SAME
  line, parameterization: 22 (one arm) and 12 (other) copy-pasted TESTs, no
  TEST_P or table anywhere. The skill mandates parameterized tests and did
  not move the one line where it could have separated the arms.
- S2 (review, 7 planted violations): **tie, 7/7 both** — both caught the
  fixture leak, the swallowed catch(...), the UB-on-empty-vector fetch
- S3 (structural probe): **tie, 5/5 both** — both organized around testing
  discipline: FetchContent + gtest_discover_tests, unit/integration split,
  ASan/UBSan in CI, DI/fakes, flakiness guardrails, coverage-as-trend
- S4 (negative): **tie** — both one correct sentence

Judge verdict: "rubric-indistinguishable — same passes, same single
failure, same failure mode"; differences are stylistic noise. Obsolescence:
YES, on both execution and the probe. Retired.
