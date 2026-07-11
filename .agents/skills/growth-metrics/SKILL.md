---
name: growth-metrics
description: "Use when wiring up product analytics or funnel tracking for a bootstrapped SaaS, defining an activation event or a tracking plan, instrumenting PostHog on a Next.js + Vercel + Supabase + Stripe stack, or running a weekly growth readout against the kill criteria in a GTM strategy doc. Also when growth numbers are being eyeballed ad hoc with no scorecard behind them. Pairs with gtm-strategy (upstream, source of kill criteria) and saas-deploy-readiness (env handling)."
origin: designed to close the measurement loop gtm-strategy opens; PostHog-on-Vercel conventions hardened from baseline testing
---

# Growth Metrics

`gtm-strategy` produces bets with numeric, dated kill criteria. This skill
produces the numbers those criteria compare against. Without it, every session
reinvents event names, funnel definitions, and scorecard formats, and nothing
persists where next week's readout can find it. The failure mode is not bad
analytics advice; it is good advice that evaporates. The fix is fixed
artifacts: one tracking plan, one event catalog, one scorecard log.

## The Principle

> **A metric exists to trigger a decision.** If no decision changes when the
> number moves, delete the metric.

## Modes

- **Setup** (first run): Phases 0–3 below, in order.
- **Readout** (recurring; "run my growth readout", "how are the bets doing"):
  the Readout procedure only, appending to the scorecard log.

## Phase 0: Bind to the strategy

If `docs/gtm-strategy.md` exists, read it first. Extract the primary metric,
the funnel stages, and every kill criterion. Everything defined below must
trace to one of them; a metric that traces to nothing is deleted or gets a
written justification. If the doc names an activation definition, use it; if
it doesn't, write the one chosen in Phase 1 back into it.

If the doc does not exist, run a compressed interview (one question at a
time): the one primary metric for the next 90 days, what activation means for
this product, and which channel is currently being tested with what threshold.
Note that `gtm-strategy` would sharpen all three, and move on.

## Phase 1: The tracking plan

Written to `docs/tracking-plan.md`. Rules:

1. **Exactly one activation event**, defined as observed value delivery: the
   moment the user gets the thing they came for (first report generated,
   first chaser email sent). Never signup, login, or onboarding-complete —
   those measure motion, not value.
2. **One event per funnel stage.** Map stranger → aware → trial → activated →
   paying to exactly one named event each. More than one event per stage means
   the stage boundary is fuzzy; sharpen the definition instead of adding
   events.
3. **Naming: snake_case `object_verb`** ("trial_started", "report_generated").
   Past tense, the object first.
4. **Every event carries its decision question.** The plan is a table:

   | Event | Fires | Properties | Decision it informs |
   |-------|-------|------------|---------------------|
   | `chaser_sent` | server, chaser job | `invoice_total_usd` | is activation delivering value worth $19/mo? |

   An event whose "decision" column you cannot fill is curiosity, not
   measurement. Cut it.
5. **Ten events maximum** at this stage. The cap forces the decision-question
   test; a founder with three customers does not have ten decisions to make
   from telemetry.
6. **Two populations never mix.** If the product has a second population
   (embed viewers, form respondents, invitees of the paying user), their
   events are captured server-side, anonymous, keyed by resource id — not
   identified, not mixed into customer funnels.

## Phase 2: Instrument

The pinned stack: PostHog on Next.js + Vercel + Supabase + Stripe. Opinionated
on purpose, like `saas-deploy-readiness`. When this is wrong, see Boundaries.

- **Client:** `posthog-js`, initialized once, with a Next.js rewrite proxying
  `/relay/*` → PostHog ingestion. Adblockers eat third-party analytics
  requests, and the users they eat are disproportionately the organic-search
  visitors the channel bet is measuring. No proxy, no trustworthy attribution.
- **Identify on auth** with the Supabase user id. This stitches the anonymous
  first visit (and its `$initial_referrer` / `$initial_utm_source`, which is
  where channel attribution lives) to the account. Test it end to end:
  incognito visit with a UTM → sign up → the person in PostHog shows the
  initial referrer.
- **Server:** `posthog-node` with `flushAt: 1, flushInterval: 0` — serverless
  functions die before batched events flush.
- **Revenue events fire server-side from the Stripe webhook** —
  `subscription_started`, `subscription_canceled` — never from the client. The
  client lies: page closed before capture, adblocked, or spoofed.
- **All captures go through one typed event catalog.** One module, one
  exported function per event, no raw event-name strings anywhere else:

  ```ts
  // lib/analytics.ts — the only file that knows event names
  import { PostHog } from "posthog-node";

  const ph = new PostHog(process.env.NEXT_PUBLIC_POSTHOG_KEY!, {
    flushAt: 1,
    flushInterval: 0,
  });

  export const trialStarted = (userId: string) =>
    ph.capture({ distinctId: userId, event: "trial_started" });

  export const chaserSent = (userId: string, invoiceTotalUsd: number) =>
    ph.capture({
      distinctId: userId,
      event: "chaser_sent",
      properties: { invoice_total_usd: invoiceTotalUsd },
    });
  ```

  A raw `capture("some_string")` at a call site is how "signup", "Signed Up",
  and "user_signup" end up as three different metrics.
- **First-time events emit on a transition**, gated on a column
  (`activated_at` on the user row): set the column and emit only when it was
  null. Idempotent under retries and double-fires.
- **Autocapture is noise.** Pageviews stay on; everything else is a named
  event from the catalog.
- **Env vars classified per `saas-deploy-readiness`:**
  `NEXT_PUBLIC_POSTHOG_KEY` is build-time; `POSTHOG_API_KEY` (a private API
  key, used only by readouts) is a runtime secret and never ships to the
  client.
- **Setup is not done until events are verified flowing.** Drive each real
  flow — sign up, activate, subscribe in Stripe test mode — and see each event
  arrive in PostHog with the right person attached. An instrumented-but-
  unverified event is a bug that surfaces at week 6, when it is too late to
  backfill.

## Phase 3: Scorecard

Build two insights in PostHog: the funnel (the Phase 1 stage events, broken
down by initial referrer/UTM) and weekly cohort retention on the activation
event. Then define the scorecard in `docs/tracking-plan.md`, one row per kill
criterion and per funnel stage:

| Metric | This week | Kill threshold | Deadline | Weeks left | Verdict |
|--------|-----------|----------------|----------|------------|---------|
| activated trials from organic (cum.) | — | ≥ 8 | week 6 | — | — |

A row missing its threshold or deadline is not written yet; go back to the
gtm doc (or the founder) and get the number. Verdicts are exactly one of:
**on-track**, **at-risk**, **falsified**.

## Readout procedure

1. Read `docs/tracking-plan.md` and `docs/gtm-strategy.md` (if present) for
   the current thresholds and named fallbacks.
2. **If `POSTHOG_API_KEY` is available**, fetch this week's numbers from the
   PostHog API (query the saved insights). **If not**, emit the scorecard
   with numbers blank and each row naming the exact PostHog insight it comes
   from, for the founder to fill.
3. Fill the row, compute weeks left, assign the verdict.
4. **A met kill criterion is reported as falsified, in those words, with the
   gtm doc's named fallback.** Leading indicators (impressions, backlinks,
   "it feels like it's picking up") do not override a criterion on the
   metric it was set on; they may be noted as context for a dated re-entry
   condition, never as a reason to keep the bet alive.
5. Append the dated entry to `docs/growth-scorecard.md` — newest first, never
   overwrite. The log is the falsification record; its history is the point.

## Anti-pattern Catalog

The tell, then the antidote. When one appears in a draft, rewrite before
delivering.

| Tell | Antidote |
|------|----------|
| Activation defined as signup or login | value delivery: the first moment the product did its job |
| "Track everything, decide later" | every event carries the decision it informs; ten-event cap |
| Scorecard row with pageviews, followers, or stars | rows trace to kill criteria and funnel stages |
| Metric or threshold defined after the experiment started | thresholds come from the gtm doc, dated before the bet runs |
| Revenue event captured client-side | Stripe webhook, server-side |
| Raw event-name strings at call sites | the typed catalog is the only file that knows event names |
| Tracked event on no scorecard and answering no question | delete it or write its justification into the plan |
| Scorecard row with a blank threshold "to fill in later" | the row is not written until the number and date exist |
| "Impressions doubled, let's give it a few more weeks" | the criterion stands; note context as a dated re-entry condition |
| Numbers reported in chat, no log updated | the dated entry in `docs/growth-scorecard.md` is the deliverable |

## Boundaries

- **`gtm-strategy`** owns the strategy: kill criteria, funnel stages, and
  fallbacks come from there, not from this skill.
- **`dashboard-builder`** owns operational metrics — latency, errors,
  saturation stay in Grafana/SigNoz. This skill owns the product funnel only.
- **`saas-deploy-readiness`** owns env-var classification and deploy checks.
- **When PostHog is wrong:** a strict-privacy product (or a founder who won't
  add a third-party processor) gets Plausible for traffic plus an events
  table in Supabase for the funnel. Say the trade: funnels and retention
  become hand-written SQL. Flag the mismatch; don't force the default.

## Quality Gate

Before delivering, confirm:

- every scorecard row traces to a kill criterion or funnel stage (when the
  gtm doc exists); orphan metrics deleted or justified in writing
- exactly one activation event, defined as value delivery
- revenue events captured server-side from the Stripe webhook
- a typed event catalog exists and call sites contain no raw event names
- every event was verified arriving in PostHog before setup is called done
- every scorecard row has a numeric threshold and a date; no placeholders
- readout delivers a verdict per bet — falsified bets called falsified, with
  the named fallback
- `docs/tracking-plan.md` written and `docs/growth-scorecard.md` appended,
  not just chat output
- env vars classified per `saas-deploy-readiness`
- prose follows the `writing` skill's anti-slop rules
