---
name: "venture-bet-discovery"
description: "Generate and screen startup candidates for venture-scale outcomes: a credible bottom-up path to $100M+ ARR. Use instead of startup-idea-discovery when the bet must absorb venture capital."
---

# Venture Bet Discovery

Generate many candidates. Kill anything that cannot absorb capital or cannot reach $100M+ ARR. Keep two or three.

## When to use this instead of `startup-idea-discovery`

That skill is calibrated for a solo or bootstrapping founder aiming at $10-20k MRR beneath the notice of incumbents. Three of its seven screen steps are structurally anti-venture and will kill the bets that actually return a fund:

- It kills candidates with no existing budget line, which excludes every category-creating bet.
- It kills candidates whose buyers cannot be reached async by writing, which excludes sales-led and consumer.
- It kills candidates where an industry insider could execute better, when outsiders out-executing incumbents with capital and talent is a standard venture pattern.

Use that skill when the goal is a business that pays the founder. Use this one when the goal is a business that pays back a fund. They are not the same search and they do not share a screen.

## The three failure modes

**Anchoring.** The founder finds one interesting thing and stops searching. Everything after is rationalisation dressed as research.

**TAM fantasy.** The founder finds a large number in an analyst report, multiplies it by a share they have no mechanism to win, and calls it a market. "$10B market, we take 10%" is unfalsifiable, which is precisely why it survives scrutiny for months and then dies in a partner meeting. The number is not the problem; the absence of a mechanism is.

**False rigour.** The screen itself produces a confident wrong answer. A bottom-up number computed from the wrong denominator, the wrong pricing basis, a stale ACV or a mis-read constraint looks far more credible than a guess and is much harder to argue with. Every rule below marked FALSIFY exists because this failure mode killed real candidates.

Counter all three:

- Ten to fifteen candidates before screening any of them. No more than two per domain.
- At least three from a surface the founder does not personally inhabit.
- An idea the founder arrives with is candidate zero. It competes; it does not seed.
- Every market number is built from the bottom, from a countable N. A number sourced from a report is a citation, not an estimate.
- Time-box the batch: half a day for generation plus screening.

## Why the "$10B market, 10% share" frame misleads

It is directionally right about the outcome and wrong about the search.

A $10B market **today** is one where incumbents already won, distribution is already owned, and the 10% you need is held by someone who will defend it with a larger balance sheet than yours. Large current markets are where venture bets go to die slowly.

The bets that produce the outcome usually look like one of these at t=0:

| Shape | Market today | Why it works |
| --- | --- | --- |
| Small and compounding | $500M-$2B growing 40-60% a year | Reaches $10B+ on its own trajectory; you grow with it instead of taking share |
| Adjacent to a large pool | The $10B sits in labour or workarounds, not software | You are not taking share, you are converting a non-software budget |
| Not yet a market | Behaviour exists at scale, no product does | Share is undefined because the category is undefined |
| Structurally forced | A rule or deadline creates the budget on a known date | The buying decision is not discretionary |

## Computing a ceiling

This is the step that does most of the killing, so it is the step most worth getting right. In practice it has been wrong more often than every other step combined, and almost always through its inputs rather than its logic.

### Compute it two ways, every time

```
ceiling = max(
  N x mature ACV,                           # buyer-priced
  addressable flow x plausible take rate    # flow-priced
)
```

**Never compute only the first.** If money moves through the workflow, the flow calculation is usually the real one and it is routinely several times larger. A ticketing platform earning 9-10% of ticket value and a venue-software vendor charging $10k a seat serve the same buyer and differ by two orders of magnitude in ceiling. Estimate the flow you could plausibly touch, apply a take rate sourced from the nearest real comparable rather than assumed, and use the larger of the two numbers.

**But do not read that as "flow businesses are better."** The two formulas are not symmetric in how they fail. A flow figure is a market-scale number that already contains growth and expansion. `N x ACV` is a snapshot at today's price, which silently assumes every customer pays the same amount forever. That single asymmetry, not any real advantage of take-rate businesses, is why an unguarded screen keeps surfacing payments and marketplaces and keeps killing software. The guard is the next section, and it is not optional.

Also ask how fast N or the flow is growing. A $400M ceiling growing 25% a year is a better bet than an $800M one that is flat.

### ACV is the highest-variance input in the screen

It has been wrong in both directions, by roughly an order of magnitude each way. Three rules, all cheap:

**1. Look up what incumbents actually charge. Never infer a blended ACV from enterprise anecdotes.** Most vertical software publishes its pricing. Reasoning "the enterprise vendor does six-figure deals, so call it $25k blended" produced a ceiling 6x too high in one real batch, against published tiers that topped out near $11k. Two minutes on two pricing pages settles it. Where pricing is gated, price the tier your buyer would actually land in, not the one the vendor leads with.

**2. Apply an expansion multiple, and source it.** Good software businesses are not static-ACV businesses. Sourced examples, all public: Snowflake reported **126% net revenue retention** on $3.46B of FY2025 product revenue across 11,000+ customers, averaging roughly $315k each with 580 customers above $1M; Figma reported **132% net dollar retention** and 96% gross retention among $10k+ customers while crossing $1B revenue; Datadog reported 4,060 customers at $100k+ ARR, up 16% year on year; CrowdStrike reports 51% of customers on six or more modules and 25% on eight or more.

Net retention of 130% compounds to roughly **6.3x over seven years**. A ceiling built on today's ACV assumes 100% retention, which describes almost no good software business. So:

```
mature ACV = today's entry ACV x expansion multiple
expansion multiple = (comparable's net retention) ^ (years to maturity)
```

State the comparable you took the retention figure from. If you cannot find one, say the multiple is unsourced and use 1.0 — but then record that the ceiling is a floor, not a ceiling, and do not kill a candidate on it alone.

**3. Write down both numbers.** Entry ACV and mature ACV, with the multiple between them. A kill computed on entry ACV is not a kill; it is an unfinished calculation.

This is what makes the screen basis-agnostic. Seat-priced, usage-priced and flow-priced businesses all reach scale; they differ in *where* the growth shows up. Flow businesses grow with the flow, usage businesses grow with consumption per customer, seat businesses grow by adding seats, modules and tiers. Only the first of those is captured for free by the arithmetic. The other two have to be put in by hand, and a screen that does not put them in will reliably conclude that software is too small.

### The share threshold is not a constant

Ask what share of the ceiling is winnable, then compare against the right bar:

| Market shape | Threshold | Why |
| --- | --- | --- |
| Fragmented, low switching costs, many substitutes | **15%** | Share is hard to hold; a funded follower takes it back |
| Standard vertical SaaS | **25%** | The default when nothing else is evidenced |
| System of record with data gravity and multi-year switching costs | **40%** | Concentrated categories really do consolidate |

Use the 40% tier only with **evidence** of switching costs: migration horror stories, multi-year contracts, integration depth, regulatory certification. Not because the category sounds infrastructural.

Do not go above 40% on the strength of Epic or Veeva. Both exceeded half their categories and both took fifteen to twenty years to get there. Assuming you hold half a system-of-record category inside a venture horizon is exactly the unfalsifiable assumption this step exists to stop.

### FALSIFY before any structural verdict

Before writing that a category, a segment or an industry is too small, spend fifteen minutes searching for companies in it above $100M revenue or $1B valuation. Once per category, not per candidate, so the batch time-box survives.

**If a top-down conclusion contradicts one sourced counterexample, discard the conclusion, not the counterexample.** A single real company at $180M revenue kills a model that said the whole category was $250M. The model was the guess; the company is the fact.

The same test catches a ceiling that is too low: if a real company's current revenue exceeds the ceiling you just computed for its whole category, the ceiling is wrong, and the usual cause is a missing expansion multiple.

When the verdict rests on an industry's total size, check the denominator before writing it down. Industries have several revenue pools and it is easy to size one and call it the whole. Name the pools you included and the pools you left out. If you cannot name what you left out, you have not checked.

### Apply the same rigour to survivors

The most common way this step fails is asymmetry: a generous ceiling for the candidate you find interesting, stingy ones for the candidates you are killing. Recompute the survivors' ceilings last, with the same sources and the same scepticism, and check specifically whether the survivor's category has a *sourced* market size smaller than the ceiling you constructed for it.

## Where candidates come from

Two classes of surface, and a batch needs both. Existing-spend surfaces are higher signal and lower ceiling. Emerging-market surfaces are noisier and are where the outsized outcomes live.

### Existing spend, visible today

| Surface | The signal to look for | Ceiling risk |
| --- | --- | --- |
| Job ads at scale | The same role posted by hundreds of companies, description mostly one workflow | N is countable from postings; ACV anchors to salary |
| "We built this in-house" | How many separate well-resourced teams say it | High signal; check the count is large, not three |
| Money already moving | A flow someone already takes a percentage of | The flow-priced ceiling lives here; find the flow's size |
| Published pricing pages | What the category actually charges, tier by tier | The single best ACV anchor; read it before estimating |
| Deprecations, forced migrations | The date, and the installed base stranded | Often a one-time event, not a market |
| Regulatory deadlines | Who must comply, by when, and the penalty | Budget appears on a known date; check it recurs |
| Churn and migration threads | "We moved off X because" at volume | Confirms switching cost was worth paying |
| Vendor unbundling, pricing-page moves | A feature moving into a higher tier | The incumbent just told you where value sits |
| Services firms scaling headcount | Revenue per head flat while headcount grows | A productisable process with a proven price |
| Two- and three-star reviews of paid tools | Complaints about a missing job, not price | Reliable, but usually feature-sized |

### Emerging, where the market is not yet legible

| Surface | The signal to look for |
| --- | --- |
| Cost-curve collapses | A unit cost down 10x or more in 24 months, and the workflows that were uneconomic above the old price |
| Behaviour at scale with no product | Spreadsheets, group chats, shared docs or manual coordination doing a job for a large, countable population |
| Shadow IT and unsanctioned tools | Employees paying personally or routing around procurement; budget exists but is not yet a line item |
| Platform shifts | A new distribution surface with an early, uncrowded install base |
| Newly possible supply | A capability that existed in research and just became productionisable |
| Structural shifts | Demographic, labour-supply or capital-cost changes that make a workflow unsustainable |
| Aggregation gaps | A fragmented supply side with no demand aggregator, where the fragmentation is the moat |

Distrust trend pieces, funding announcements and "top N ideas" lists. They are downstream of everything and selected for shareability. Distrust the founder's own tooling annoyances: real, n=1, and rarely attached to a buyer.

## Generation

Ten to fifteen. Each candidate is **one sentence naming a countable buyer, the workflow, and the population size** you believe exists.

Good: "The ~30,000 US mid-market logistics brokers who reconcile carrier invoices against rate confirmations by hand, currently at 2-4 FTE per firm."

Bad: "AI for logistics."

The first can be falsified in an afternoon. The second cannot be falsified at all, which is why it will still be alive in six weeks.

Record for each: the surface, the link, the date, and the first-pass guess at N. A candidate with no source link is a hunch and does not enter the log.

### Before fixing N: who else buys this?

A generative step, not a check, and it belongs here rather than in the screen because it creates candidates rather than killing them. For each workflow, ask who the buyer could be **outside** the industry the workflow sits in:

- The end customer's customer, at consumer-like volume and price.
- Brands, agencies and content teams, out of marketing budget.
- Platforms and AI developers, out of legal, data or trust-and-safety budget.
- Insurers, lenders and auditors, out of risk budget.
- Multi-site operators in retail, hospitality or healthcare, out of facilities and compliance budget.

This matters because a vertical's own software budget is usually small and its adjacent budgets usually are not. Selling something music-shaped to a video creator, or something logistics-shaped to an insurer, changes N by orders of magnitude and changes which budget the money comes from. Write down the two or three most plausible buyers and screen the best one. If two are both credible, they are two candidates, not one.

### Restate every constraint as a test before applying it

Founder constraints arrive as labels and get applied as categories, which silently kills whole segments. Convert each into a test of what the founder actually meant, and write the test down:

- "No B2C" almost never means "no individual buyers." It means **the buyer does not expect the purchase to generate income**. A sole proprietor paying for business software is not a consumer; a fan paying for an app is. Applying the label rather than the test excludes every prosumer and small-business segment, which is where several of the largest vertical outcomes live.
- "No hardware" usually means no inventory risk, not no physical product.
- "No regulated industries" usually means no multi-year licensing path, not no compliance exposure.

If the test is ambiguous, ask the founder once. A mis-read constraint is a silent kill: it never appears in the log, so nothing later can catch it.

## The screen

Five to ten minutes per candidate, search-assisted. **Kill on first fail and move on.** Order is by cost: the arithmetic kills come before the judgment calls.

1. **Constraint conflict.** Apply the *test*, not the label. Kill immediately on a real conflict; do not argue that this one is different.

2. **Scale ceiling.** Look up incumbent pricing, set entry and mature ACV with a sourced expansion multiple, compute both ceilings, take the larger, pick the threshold from the table above, and kill if clearing $100M ARR needs more than that threshold, or if neither formula reaches $100M at all. Write the numbers, the basis and the multiple down even when it passes; the handoff needs all three.

3. **Where the money is.** Name the pool: a budget line, an adjacent budget, a labour cost, a flow you can take a percentage of, or a measurable cost borne in time and workarounds. Unlike the bootstrap screen, "nobody pays for this today" is **not** an automatic kill; it is how category creation looks at the start. It is a kill only when no cost is being borne at all. If the pain is real but costless, there is no business.

4. **Why now: a changed number, and a window.** Both required. This is the step most worth being strict about, because it is the easiest in the screen to fake — every domain has something that changed, at all times.

   *The changed number.* Name the price, deadline, volume, rate or date that moved, with a source. "AI got good" is a mood. "Article 50 took effect on 2 August 2026" and "AI tracks passed 50% of daily uploads in June 2026" are why-nows, because something countable moved and you can be wrong about it. No number, no why-now, and no why-now means the market has had years to solve this and something you have not found prevented it.

   *The window and its expiry.* Every why-now opens a window that closes. Name the closing mechanism and estimate the date:

   | Why-now type | What closes the window | Rough duration |
   | --- | --- | --- |
   | Compliance deadline | The laggards finish complying | 12-36 months from the effective date |
   | Cost-curve collapse | The new price becomes common knowledge | 12-24 months |
   | Platform shift | The new surface gets crowded | 18-36 months |
   | Capability threshold crossed | Everyone else's product catches up | 6-18 months |
   | Legal or structural ruling | Players already positioned absorb the freed demand | Often immediate — check who benefits before assuming it is you |
   | Demographic or structural shift | Rarely closes | Years, but it is a tailwind, not a window, and it forces no purchase |

   **If the window closes before you could plausibly build and sell into it, kill the candidate.** That is a wave you have already missed, and it is a different and more common failure than being too early.

   Finally, be suspicious of a why-now that is fully legible. If the trade press has written it up, it is priced in, and the people best placed to act on it already have. The why-nows worth acting on are usually mechanical rather than narrative, because mechanical ones are boring enough that nobody writes about them.

5. **Commoditising layer.** If the value delivered is analysis, drafting or generic insight, its price is collapsing toward zero. Kill unless the durable part is data access, workflow lock-in, distribution, trust, or regulatory position.

6. **Feature or company.** Is the natural home for this a checkbox in a product that already owns the buyer relationship? If a platform with existing distribution would ship it the quarter after you prove demand, kill. Your funding round is a public announcement of the opportunity, so "incumbents are slow" is not protection.

7. **Wedge to market.** A beachhead narrow enough to win outright, adjacent enough to expand from. Name both the wedge and the second market, and the mechanism connecting them (the same buyer, the same data, the same integration). Kill if the wedge is an island: a defensible niche with no adjacency is a fine business and a bad venture bet, and should be handed to `startup-idea-discovery` rather than thrown away.

   Note that the expansion mechanism you name here is the same one the expansion multiple in step 2 assumes. If they disagree, one of them is wrong.

8. **Accruing advantage.** Assume a competitor with $30M and a good team enters eighteen months after you launch. What do you have then that they cannot buy? Proprietary data that improves the product, network effects, switching costs, supply locked under contract, a regulatory or certification position. "We execute better" is not an answer. This step kills more candidates than any other and should.

   **Pricing is a wedge, not a moat — unless.** A competitor changes a pricing page in a week, so "we charge differently" is not an answer to this step on its own. A pricing model counts here only when one of these holds:

   - *Incumbent-incompatible.* Matching you would wreck their revenue recognition, their salesforce comp or their existing book — consumption pricing against perpetual licences, free-seat bottom-up against an enterprise channel. The incumbent is not slow, they are structurally unable. Real, but it is an innovator's-dilemma window with an expiry like any other: it closes when they get desperate enough to eat the transition. Date it in step 4.
   - *Capability-gated.* The model requires something the competitor does not have. A take-rate requires moving the money, which requires licences, rails and payee onboarding. Outcome pricing requires measuring outcomes. Note that the barrier is the capability, not the price.

   And in both cases the model must **accumulate** something, because that is what the moat turns out to be. Take-rate accumulates transaction history and payee relationships; consumption accumulates workload lock-in; a free tier accumulates a user graph. Snowflake's durable advantage became data gravity, Figma's the multiplayer file as the organisation's source of truth, CrowdStrike's the sensor and threat graph — in each case the pricing got them in and something else kept them there. A pricing model that accumulates nothing is a discount with a story attached.

What the screen still does not ask: technical feasibility, competition depth, or revenue projection. Feasibility in particular is a trap for technical founders, because "could I build this" is the one question they can answer instantly and it correlates with nothing.

Expect one to three survivors from fifteen. If more than half survive, the usual cause is generous arithmetic at step 2 or a hand-waved answer at step 8. If **none** survive and several died at step 2 with similar numbers, suspect the screen before concluding the sector is dead: run the FALSIFY search, check the denominator, check whether every kill was computed on entry ACV with no expansion multiple, and check whether every kill was computed buyer-priced when a flow existed.

## The candidate log

Append every batch. This is the compounding asset of the practice. It is wide — keep it in a spreadsheet, not a document.

| Date | Candidate (buyer + workflow + N) | Surface + link | Entry ACV + source | Expansion multiple + comparable | Ceiling + basis | Share needed | Why-now + window closes | Killed at step | The killing fact | Recheck trigger |

Three columns make a step-2 or step-4 kill auditable rather than just recorded. A kill computed buyer-priced is worth revisiting the moment you find the flow the workflow sits on. A kill computed at entry ACV is worth revisiting as soon as you find a comparable's retention figure. And a candidate killed because its window was closing is worth nothing later — but a candidate killed for another reason whose window is still open is the first thing to re-screen next batch.

Two entries matter beyond the kill:

- **The killing fact**, specific enough to be wrong. "Market too small" is weak. "Census and two trade-association counts both put this at 4,100 firms; at a $60k ACV benchmarked from the incumbent's published pricing and a 1.0x multiple with no comparable found, the ceiling is $246M, so $100M needs 40% share" is a fact that can be overturned by better data.
- **The recheck trigger.** Many venture candidates die on a condition, not a principle: a cost curve not yet low enough, a rule not yet in force, an install base not yet large. Write the condition and the date. These become the strongest candidates in later batches because the work is already done.

Step 8 kills are the most reusable. Step 2 kills are the **least** reusable despite being the most common, because they depend on N, entry ACV, expansion multiple, pricing basis and threshold choice, any of which can be wrong. Re-derive a step-2 kill before trusting it in a later batch.

## Handoff

For each survivor, one short paragraph:

- The buyer, countably defined, with the source for N.
- The workflow and what it costs them today, with the source.
- Entry ACV with its pricing source, the expansion multiple with its comparable, both ceiling calculations, which one governs, the share needed to clear $100M ARR, and which threshold tier you applied and why.
- Why now: the changed number with its date and source, the window's closing mechanism, and your estimate of when it closes.
- The wedge, the second market, and the mechanism between them.
- What accrues, and why a funded follower cannot buy it. If pricing is part of the answer, say which of the two tests it passes and what it accumulates.
- The single fact that would kill it, and the cheapest way to check it.

Then invoke `startup-idea-stress-test`, with one correction: its market sizing is written for a solo or bootstrapping founder and will size the wedge rather than the market. Override that by giving it the ceiling arithmetic above and asking it to red-team the expansion mechanism, the window's expiry and the accruing advantage specifically, not the wedge's near-term revenue.

Do not attach an advocacy paragraph. A survivor carried into the stress test pre-argued corrupts the red-team, which is the part of the pipeline doing the real work.

## Anti-patterns

- **Static ACV.** Computing a mature ceiling from today's entry price, which assumes 100% net retention. This kills expansion-driven businesses, which is most good software, and it is the reason an unguarded version of this screen keeps concluding that only payments and marketplaces are venture-scale.
- **Inferred ACV.** Reasoning a blended price from enterprise anecdotes when the category publishes its tiers. Wrong by 6x in one real batch.
- **Buyer-priced by default.** Computing `N x ACV` for a workflow that money flows through.
- **The mood why-now.** A change you can describe but cannot attach a number to. Every domain has one available at all times, which is exactly why it proves nothing.
- **The missed wave.** A real, dated why-now whose window closes before you could build and sell into it. Check who is already positioned to absorb the opening before assuming it is yours.
- **Pricing as moat.** Charging differently is a wedge. It is a moat only when the incumbent cannot match it without self-harm, or when the model requires a capability they lack — and only when it accumulates something.
- **Asymmetric rigour.** A generous ceiling for the candidate you like, stingy ones for the rest. Symptom: the survivor's ceiling is the only one you did not source.
- **Top-down sizing.** Any sentence of the form "if we capture X% of" is a confession that no mechanism exists. Rebuild from N.
- **Label-applied constraints.** Killing a segment because it carries a word the founder used, without checking what they meant by it.
- **The one-pool denominator.** Sizing an industry from its most visible revenue pool and treating that as the whole.
- **The big flat market.** Mistaking a large current market for an accessible one. Large and static is worse than small and compounding.
- **The anchor.** Falling for candidate three and screening the rest as formalities. Symptom: later candidates get shorter screens.
- **Feature mistaken for company.** Especially dangerous here, because the funding round advertises the opportunity to everyone positioned to ship it as a feature.
- **Wedge as destination.** A defensible niche is a real business. It is not this search. Hand it to `startup-idea-discovery` and keep going.
- **Capital mismatch.** A candidate that cannot absorb $20M productively does not become venture-scale by raising it. Cash does not create demand.
- **Too early.** Right thesis, wrong decade. The recheck trigger exists for exactly this; write it down and move on rather than funding the education of the market.
- **Depth creep.** Doing stress-test work inside the screen. Symptom: an hour per candidate, a batch of four.
- **Discovery as avoidance.** Running batches instead of executing a live bet. Discovery is for the gap between bets.

## Cadence

A standing surface list, a half-day batch when a bet ends or the queue runs dry, and the log connecting them. Emerging surfaces reward re-scanning on a schedule, because the interesting ones move: a cost curve you checked eighteen months ago is now somewhere else, and the recheck triggers and still-open windows in the log tell you which ones to look at first.