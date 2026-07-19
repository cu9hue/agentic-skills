# frontend-a11y — eval results

Append-only. Newest at the bottom.

## 2026-07-19 — backfill A/B, obsolescence check (skill as of fcb4361)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof. S4 arm B
reused from the earlier orchestrator fleet (same scenario prompt).

- S1 (signup form): **tie, 6/6 both** — baseline delivered full label/id
  pairing, aria-required with aria-hidden asterisks, describedby-linked
  role="alert" errors, aria-invalid, real submit button, unprompted
- S2 (review, 8 planted violations): **tie, 8/8 both** — baseline found
  more extras (uncontrolled inputs, missing type="button")
- S3 (confirm dialog): **rubric tie, 6/6 both** — skill arm shipped a
  manual focus trap; baseline knowingly punted ("use focus-trap-react"),
  the one real above-rubric delta
- S4 (negative, memoization): **tie** — neither bolted a11y onto a perf
  question

Judge verdict: 21/21 rubric lines passed by BOTH arms; all separation lives
outside the rubric. Obsolescence: YES — the no-skill arm passed everything.
Retired per the strict rule; if resurrecting, the scenario set needs a
focus-trap rubric line in S3, the only place a delta appeared.
