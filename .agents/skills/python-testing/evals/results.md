# python-testing — eval results

Append-only. Newest at the bottom.

## 2026-07-19 — backfill A/B, obsolescence check (skill as of ff73da3)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof. Run under
the structural-probe mandate.

- S1 (write tests): **A, 6/6 vs 5/6** — skill arm shipped one case table as
  copy-pasted functions; otherwise near-identical parametrized suites
- S2 (review, 7 planted violations): **tie, 7/7 both** — both nailed the
  mock-the-function-under-test tautology and the swallowed assertion
- S3 (structural probe): **B, 5/5 vs 4/5** — both arms organized entirely
  around testing discipline with near-identical rollback fixtures and
  dependency_overrides; the single delta is the coverage stance: skill arm
  ratchets an enforced CI gate (the skill's 80%+ mandate transmitting),
  baseline argued "reported, not worshipped"
- S4 (negative): **tie** — both answered `-x` in a line

Judge verdict: 18/19 lines each, split 1-1, skill arm by a nose on the
probe's coverage-gate line. Obsolescence: NEAR — execution fully absorbed;
the probe delta is one contested stance (enforce a coverage threshold), not
organization or coverage of concerns. The one surviving opinion could live
as a single line elsewhere if the skill retires.
