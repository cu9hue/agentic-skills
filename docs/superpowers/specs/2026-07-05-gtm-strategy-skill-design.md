# gtm-strategy skill — design

**Date:** 2026-07-05
**Status:** approved, pending implementation

## Purpose

A skill that acts like a paid GTM advisor for a bootstrapped, founder-led SaaS.
It interrogates the founder, researches where evidence is missing, and produces
a go-to-market strategy doc: positioning, a sharp ICP, one channel bet, pricing
motion, and a 90-day plan with kill criteria.

Governing principle: **a strategy is a set of falsifiable bets, not a wish
list.** Every claim in the output is tagged evidence-backed or assumption;
every bet ships with the threshold that would falsify it.

## Decisions (from brainstorming)

- **Deliverable:** full GTM strategy doc — the thinking layer. Execution is
  handed off to existing skills (`landing-copy`, `seo`).
- **Stage-aware:** diagnoses pre-launch / first users / early revenue and
  adapts questions and plan.
- **Interaction:** interrogate + challenge. Advisor-style, one question at a
  time, demands evidence over opinion, refuses to synthesize while load-bearing
  claims are pure guesses (they become tagged assumptions instead).
- **Research:** yes, targeted — fired only where a gap is load-bearing
  (competitor positioning, where the ICP congregates, channel benchmarks).
  Findings cited in the doc.
- **Bootstrapped constraints hard-coded:** one channel at a time; founder time
  is the scarcest resource; no playbooks assuming a sales team or ad budget.
  Mismatches (VC-funded playbook, enterprise motion) are flagged, in the style
  of `landing-copy`'s business-model defaults.
- **Name:** `gtm-strategy`.

## Phases

**Phase 0 — Stage diagnosis.** Three stages, each with a dominant question:

- *Pre-launch:* who exactly, and where do I find the first 10?
- *First users (~0–10 customers):* why did they buy, and do they stay?
- *Early revenue:* which single channel can scale, and what's leaking in the
  funnel?

The stage gates which Phase 1 questions get asked and what the plan optimizes.

**Phase 1 — Evidence interrogation.** One question at a time. Covers: ICP and
problem urgency, what buyers use today (the real competitor is usually the
status quo), willingness to pay, why-now, and what evidence actually exists
(conversations, signups, churn, revenue). Pushes back on opinion-shaped
answers ("how do you know?").

**Phase 2 — Targeted research.** Only load-bearing gaps: competitor
positioning scan, where the ICP actually congregates, channel benchmarks for
the ACV range. Each finding cited.

**Phase 3 — Strategy synthesis.** Fixed doc sections:

- Positioning, Dunford-style: competitive alternative → unique attribute →
  value → who cares most.
- ICP sharp enough to name 10 real prospects.
- **One** channel bet, chosen from a channel-fit table (channel × ACV ×
  founder-fit × where the ICP already looks for solutions).
- Pricing motion (self-serve vs sales-assisted, driven by ACV).
- Funnel from stranger to paying user.

**Phase 4 — 90-day plan + kill criteria.** One primary metric, a weekly
founder-time budget, 3–5 concrete moves, explicit kill/pivot thresholds ("if X
hasn't happened by week N, the channel bet is falsified"). Saved as a Markdown
strategy doc in the product repo, default `docs/gtm-strategy.md` unless the
user names another location.

## Anti-pattern catalog

Tell/antidote table, in the spirit of `landing-copy`'s conversion-killer
catalog: "build it and they will come"; five channels at 20% each; positioning
for everyone; vanity metrics; copying VC-funded playbooks; mistaking
politeness in user interviews for demand.

## Quality gate

Before delivering, confirm:

- every claim tagged evidence or assumption
- exactly one channel bet, with reasoning from the channel-fit table
- kill criteria present for every bet
- ICP passes the "name 10 prospects" test
- hand-offs to `landing-copy` / `seo` named where execution follows
- no anti-pattern catalog tell survives in the strategy
- prose follows the `writing` skill's anti-slop rules

## Shape

Single `SKILL.md` under `.agents/skills/gtm-strategy/`, ~200 lines. No
`references/`, no scripts — channel selection is a compact table inside the
file. Cross-links: `landing-copy`, `seo` (execution hand-offs).

## Implementation

Author with the `writing-skills` skill. Single prose file; a full
writing-plans → executing-plans cycle is unnecessary overhead for the
artifact.
