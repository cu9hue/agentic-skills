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

## 2026-07-19 — structural probe; retirement REVERSED (same day)

Challenge (user): well-specified prompts may pre-empt a skill's structural
value. Probe: the S5 underspecified checkout-flow ask, both arms, skill
restored from git for arm B. n=1 per cell.

- Arm A (no skill): excellent answer about payments SECURITY (PCI,
  idempotency, webhooks) with essentially zero accessibility content —
  autocomplete mentioned only as a conversion win.
- Arm B (skill): full a11y structure unprompted — step-transition focus
  management, aria-current step indicator, live regions for async payment
  state, error-focus handling, keyboard-only checklist, axe/lint gate.

Verdict: categorical delta. The earlier 21/21 baseline pass measured
component-writing, where the base model is already accessible; the skill's
real function is attention allocation on open-ended asks, which only an
underspecified probe detects. Skill resurrected; S5 added to the scenario
set so future obsolescence checks test both modes. (The same probe run on
rust-patterns showed no delta — its retirement stands. vite-patterns showed
an intermediate footgun-coverage delta; user kept it retired.)
