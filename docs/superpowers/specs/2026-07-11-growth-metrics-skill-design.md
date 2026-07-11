# growth-metrics skill — design

**Date:** 2026-07-11
**Status:** approved, pending implementation

## Purpose

A skill that closes the measurement loop `gtm-strategy` opens: that skill
demands numeric, dated kill criteria on every bet, but nothing in the stack
defines the activation event, instruments the funnel, or produces the weekly
number those criteria compare against. Without measurement, falsifiable bets
degrade back into the wish list `gtm-strategy` exists to prevent.

Governing principle: **a metric exists to trigger a decision.** Every event
tracked answers a named question; every scorecard row carries the kill
threshold it is compared against; a falsified bet is reported as falsified.

## Decisions (from brainstorming)

- **Scope: define + instrument + readout.** Three layers — define the
  activation event and funnel metrics, write the tracking code in the app,
  and run a weekly scorecard against the kill criteria. An unread metric is
  as useless as an unmeasured one.
- **Tool: PostHog, pinned.** Opinionated on purpose, same as
  `saas-deploy-readiness`. Funnels and cohort retention built in, first-class
  Next.js SDK, free tier a bootstrapped founder won't outgrow quickly. One
  "when this is wrong" note (strict-privacy products → Plausible + events in
  Supabase) instead of a tool-selection table.
- **Coupling to `docs/gtm-strategy.md`: soft dependency**, conditional on an
  observable predicate. If the doc exists, every metric must trace to a kill
  criterion or funnel stage in it — orphan metrics are deleted or justified.
  If it doesn't, run a compressed definition interview and note that
  `gtm-strategy` would sharpen it.
- **Readout mechanics: template + API when available.** The skill defines the
  scorecard format. If `POSTHOG_API_KEY` is present, the agent fetches the
  numbers via PostHog's API and delivers verdicts itself; otherwise it emits
  the template naming the exact insight each number comes from.
- **Name:** `growth-metrics`.

## Modes

Two entry modes, one skill:

- **Setup mode** (first run): Phases 0–3 below.
- **Readout mode** (recurring; "run my growth readout", "how are the bets
  doing"): executes only the scorecard step and appends a dated entry.

## Phases

**Phase 0 — Bind to the strategy.** If `docs/gtm-strategy.md` exists, extract
the primary metric, funnel stages, and kill criteria; everything defined later
traces to them. If not, compressed interview: the one primary metric, the
activation definition, the channel being tested.

**Phase 1 — Tracking plan** (written to `docs/tracking-plan.md`):

- Exactly **one activation event**, defined as observed value delivery — the
  moment the user gets what they came for. Never signup or login.
- The funnel stranger → aware → trial → activated → paying maps to exactly
  one named event per stage, snake_case `object_verb` ("trial_started",
  "report_generated").
- Every event answers a named decision question. A plan exceeding ~10 events
  at this stage is tracking curiosity, not decisions.

**Phase 2 — Instrument** (PostHog on Next.js + Vercel + Supabase + Stripe):

- `posthog-js` client, `posthog-node` server.
- Revenue/paying events fire **server-side from the Stripe webhook**, never
  the client.
- `identify` on auth with the Supabase user id.
- All captures go through one **typed event-catalog module** (`analytics.ts`
  exporting typed helpers) so names can't drift. Autocapture is noise; named
  events only.
- Env vars classified per `saas-deploy-readiness`: `NEXT_PUBLIC_POSTHOG_KEY`
  build-time, `POSTHOG_API_KEY` runtime secret.
- Setup is not done until events are verified flowing: drive the real flow,
  see the event arrive in PostHog.

**Phase 3 — Scorecard + readout.** Funnel and cohort-retention insights built
in PostHog; scorecard format defined in the tracking plan. Each row: metric →
this week's number → kill threshold → deadline → weeks left → verdict
(on-track / at-risk / falsified). Weekly readouts append dated entries to
`docs/growth-scorecard.md` so bet history accumulates. A falsified verdict is
stated plainly with the gtm doc's named fallback — never softened.

## Anti-pattern catalog

Tell/antidote table, house style: activation defined as signup;
track-everything / autocapture as strategy; vanity rows (pageviews,
followers); metric defined after the experiment started; client-side revenue
events; event-name drift ("signup", "Signed Up", "user_signup"); scorecard
rows without thresholds; orphan metrics tracked but on no scorecard; "we'll
look at the data later."

## Quality gate

Before delivering, confirm:

- every scorecard row traces to a kill criterion or funnel stage (when the
  gtm doc exists)
- exactly one activation event, defined as value delivery
- revenue events captured server-side
- a typed event catalog exists; no inline event-name strings
- events verified flowing in PostHog before setup is called done
- every scorecard row has a numeric threshold and date; no placeholders
- readout delivers a verdict per bet, including falsified ones
- env vars classified per `saas-deploy-readiness`
- prose follows the `writing` skill's anti-slop rules

## Boundaries and cross-links

- `gtm-strategy` — upstream; source of kill criteria and funnel stages.
- `saas-deploy-readiness` — env-var classification and deploy discipline.
- `dashboard-builder` — explicit boundary: operational metrics (latency,
  errors, saturation) stay in Grafana/SigNoz; this skill owns the product
  funnel only.

## Shape

Single `SKILL.md` under `.agents/skills/growth-metrics/`, ~230 lines, no
`references/`, no scripts. One code example: the typed event-catalog helper.
If drafting exceeds ~250 lines, split a PostHog implementation reference out
then — not preemptively.

## Implementation

Author with the `writing-skills` skill. Single prose file; a full
writing-plans → executing-plans cycle is unnecessary overhead for the
artifact.
