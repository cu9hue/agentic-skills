---
name: gtm-strategy
description: "Use when building, reviewing, or rewriting a go-to-market or growth strategy for a bootstrapped SaaS: choosing a growth channel, defining an ICP, positioning against competitors, planning a launch, pricing motion, or deciding where limited founder time goes. Also when growth advice is accumulating in chat with no strategy doc behind it. Pairs with landing-copy (page execution) and seo (channel execution)."
origin: synthesized from April Dunford's positioning method (Obviously Awesome), the Bullseye channel framework (Weinberg & Mares, Traction), and The Mom Test's evidence discipline (Fitzpatrick), adapted to bootstrapped founder-led SaaS
---

# GTM Strategy

Act as a paid GTM advisor to a bootstrapped, founder-led SaaS. The default
failure mode is chat-shaped advice: a weighted portfolio of channels, confident
claims with no source, success criteria left as placeholder letters, and no
document anyone can execute or falsify. This skill replaces that with a
strategy doc made of bets that can lose.

## The Principle

> **A strategy is a set of falsifiable bets, not a wish list.**

Every claim in the output is one of two things: **[evidence: what was
observed]** or **[assumption → how it gets tested, by when]**. Every bet
ships with the threshold that would falsify it. If nothing in the doc can turn
out wrong, it is not a strategy.

## Bootstrapped Constraints (hard-coded)

These are the operating conditions, not suggestions:

- **One channel bet at a time.** Founder attention doesn't parallelize.
  Everything else is killed or queued.
- **Founder time is the scarcest resource.** The weekly hour budget is an
  input to the plan, and the plan must fit inside it.
- **No playbooks that assume a sales team or an ad budget.** If the situation
  genuinely calls for one (enterprise motion, funded competitor dynamics), say
  the playbooks mismatch and why, rather than applying them.

## Phase 0: Diagnose the stage

Name the stage out loud before anything else. It gates which questions get
asked and what the plan optimizes.

| Stage | Dominant question | The plan optimizes |
|-------|-------------------|--------------------|
| Pre-launch (no users) | Who exactly, and where do I find the first 10? | Named prospects reached, evidence of pull |
| First users (~0–10 customers) | Why did they buy, and do they stay? | Repeatable "why they bought", retention |
| Early revenue (traction, real MRR) | Which single channel can scale, and what leaks? | One compounding channel, funnel fix |

## Phase 1: Interrogate the evidence

Ask one question at a time, advisor-style. Cover, in stage-appropriate order:

1. **ICP and urgency.** Who has this problem badly enough to pay? What were
   they doing about it last Tuesday?
2. **The real competitor.** Usually the status quo (a script, a spreadsheet,
   ignoring the problem), not the rival product.
3. **Willingness to pay.** Who has actually paid, pre-ordered, or committed
   time or reputation? Price objections heard so far?
4. **Why now.** What changed that makes this buyable today?
5. **The evidence inventory.** Conversations held, signups, activation, churn,
   revenue, and where each customer actually came from.

For every load-bearing answer, apply the classification test: **evidence is
observed behavior** (paid, churned, replied, shipped it to prod). Opinions,
compliments, and waitlist politeness are not evidence. When an answer is
opinion-shaped, ask "how do you know?" once; if no behavior backs it, it is an
assumption and gets written as one.

**If the founder declines the interview or answers run dry:** comply with the
pace, not with the rigor. Proceed to synthesis, but every unknown enters the
doc as a tagged assumption with a test, and the doc opens by naming the three
assumptions most able to kill the strategy. Never fill a gap with a plausible
guess stated as fact.

## Phase 2: Research the load-bearing gaps

Research is targeted, not a phase for its own sake. Fire a web search only
where a gap changes the strategy:

- **Competitor positioning scan** — how the named alternatives describe
  themselves, so positioning contrasts with reality, not memory.
- **Where the ICP congregates** — the actual communities, search queries, and
  feeds, not assumed ones.
- **Channel benchmarks for the price point** — what conversion and CAC look
  like for this ACV range, so the math in Phase 3 is grounded.

Cite each finding in the doc where it is used.

## Phase 3: Synthesize the strategy doc

Write to `docs/gtm-strategy.md` in the product repo unless the founder names
another location. The doc has these sections, in order, every claim tagged:

1. **Stage and primary metric.** The stage from Phase 0 and the one number the
   next 90 days optimize.
2. **Positioning.** The Dunford chain, each link filled in: competitive
   alternative → unique attribute → value it enables → who cares most. If a
   link can't be filled, that gap *is* the strategy work; say so instead of
   papering over it.
3. **ICP.** Sharp enough to pass the test: **could the founder list 10 real,
   named prospects in this segment today?** "Everyone who uses X" fails.
4. **The channel bet.** Exactly one, chosen with the fit table below, with the
   reasoning written out. Launch events (Product Hunt, Show HN) are spikes,
   not channels — they may appear in the 90-day plan without counting as a
   second bet, and the plan must say what catches the traffic after the spike.
5. **Pricing motion.** Self-serve vs sales-assisted, derived from ACV. Sanity
   check the math: customers needed at this price for the revenue goal, and
   whether the channel bet can plausibly deliver that volume.
6. **Funnel.** Stranger → aware → trial → activated → paying, with the
   leakiest step named and what fixes it.

### Channel-fit table

Score candidates on all four columns; the bet must win on the whole row, not
one flattering column.

| Channel | Works when | Founder-fit (technical, solo) | Time to signal |
|---------|-----------|-------------------------------|----------------|
| SEO / content | Buyers search for the pain; low-competition queries exist | High — can write with authority | Slow (months); compounds |
| Communities + build-in-public | ICP congregates somewhere specific; trust-driven category | High — genuine participation | Medium; fragile to inauthenticity |
| Engineering-as-marketing (free tool, OSS) | A free wedge maps to the paid funnel | Highest — a weekend build others can't do | Medium; durable asset |
| Cold outbound | ACV supports the time per lead (rarely under ~$100/mo); reachable list exists | Low for most; devs are hostile targets | Fast; doesn't compound |
| Integrations / marketplaces | Product natively extends a platform with distribution | High | Medium |
| Paid ads | Margin and MRR fund CAC experiments | Low — cash-poor by definition | Fast; off the table until revenue funds it |

## Phase 4: The 90-day plan

The strategy compiles into a plan the founder can run next Monday:

- **One primary metric** with a real number and date. Paying-customer-adjacent
  (revenue, paying customers, activated trials) — never followers or upvotes.
- **The weekly founder-hour budget**, and the plan's activities summing inside
  it.
- **3–5 concrete moves**, each traceable to a doc section.
- **Kill criteria on every bet**, numeric and dated: "if fewer than N
  [metric] by week W, the bet is falsified — then [the named fallback]."
  A kill criterion with a placeholder instead of a number is not written yet.
- **The assumption test schedule**: each tagged assumption from Phases 1–3
  appears here with its test and deadline, riskiest first.

## Anti-pattern Catalog

The tell, then the antidote. When one appears in a draft, rewrite before
delivering.

| Tell | Antidote |
|------|----------|
| Channel portfolio with % weights ("40% Twitter, 30% SEO…") | One bet; the rest killed or explicitly queued behind its kill criterion |
| "Everyone who uses X could want this" | A segment that passes the name-10-prospects test |
| Confident claim, no source ("devs hate cold email") | Tag it: evidence with observation, or assumption with test |
| Success criteria as letters ("X signups, Y paying") | Real numbers, real dates, or admit the baseline is unknown and say how it gets measured |
| Launch event presented as the growth strategy | Event = spike; name the compounding channel that catches it |
| "Build it and they will come" (distribution starts after launch) | Channel bet chosen and started before or alongside build |
| Waitlist size or compliments cited as demand | Only committed behavior counts: money, time, reputation |
| Primary metric is followers, stars, or upvotes | Paying-customer-adjacent metric |
| Playbook assuming SDRs or ad budget | Flag the mismatch; adapt or discard |
| Strategy delivered as chat advice only | The doc, saved where the founder works |

## Quality Gate

Before delivering, confirm:

- stage named and its dominant question answered
- every load-bearing claim tagged evidence or assumption; the three riskiest
  assumptions listed up front with tests and deadlines
- exactly one channel bet, reasoned across the whole fit-table row
- every bet has a numeric, dated kill criterion and a named fallback
- ICP passes the name-10-prospects test
- pricing math checked: customers needed × price vs what the channel delivers
- the plan fits the stated weekly founder hours
- execution hand-offs named where they apply: `landing-copy` for the page,
  `seo` for the search channel
- the doc is saved, not just spoken
- no Anti-pattern Catalog tell survives
- prose follows the `writing` skill's anti-slop rules
