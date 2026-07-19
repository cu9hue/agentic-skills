# python-patterns — eval results

Append-only. Newest at the bottom.

## 2026-07-19 — backfill A/B, obsolescence check (skill as of 8f12d44)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof. Primary
question: obsolescence.

- S1 (write config loader): **tie, 6/6 both** — baseline produced a frozen
  dataclass, full type hints, chained specific exceptions, safe resource
  handling, unprompted
- S2 (review planted anti-patterns): **tie, 7/7 both** — baseline flagged
  every planted anti-pattern (star import, mutable default, type()==,
  O(n²) concat, handle leak, bare except, ==None) plus extras
- S3 (make it Pythonic): **B, 4/4 vs 3/4** — the only separation in the
  whole eval: baseline suggested type hints in prose instead of delivering
  them in code
- S4 (negative, GIL question): **tie** — no ceremony either arm

Judge verdict: baseline 17/18 rubric lines, skill arm 18/18. Obsolescence:
NEAR — the base model has absorbed effectively all of this 749-line skill
(which also exceeds the 500-line cap). The one binding directive left is
"add type hints without being asked." Flagged for retirement or reduction
to a micro-skill; strict retire rule (baseline passes everything) missed by
one soft line.
