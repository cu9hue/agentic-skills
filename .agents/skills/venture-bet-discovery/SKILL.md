---
name: venture-bet-discovery
description: "Use when screening startup candidates for venture scale: \"screen these ideas\", \"which of these could return a fund?\", a batch from venture-ideation, or re-screening a log after a bet dies. Not for generating ideas (venture-ideation), a side business meant to pay the founder, or evaluating a single named market (market-evaluation)."
---

# Venture Bet Discovery

Screen a batch of candidates. Kill anything that cannot absorb capital or cannot reach **$1bn+ ARR in under 10 years**. Keep two or three, and hand them to `market-evaluation`.

## Same bar as `market-evaluation`

`market-evaluation` is the source of truth for what a venture market is. This skill is its cheap pre-screen: it runs across many candidates the checks that can kill in minutes, so the full nine-axis evaluation only runs on survivors. The two skills must never disagree about the bar. A screen at $100M that feeds an evaluation at $1bn passes candidates the evaluation will fail.

| Screen step | `market-evaluation` axis it pre-checks |
| --- | --- |
| 2. Scale ceiling | 1. $1bn ARR path |
| 3. US first | 2. US first |
| 4. Where the money is | 4. Market dynamics (crowded or untapped), 5. Problem size, 6. Pain depth |
| 5. Why now | 8. Tailwinds |
| 8. Wedge and year-3 asset | 3. Adjacencies |
| 9. Accruing advantage | 4. Market dynamics (what a funded competitor cannot copy) |
| 10. Learning speed | 9. Learning speed |

Kill a candidate when the evidence found in the screen would score its axis at -3 or lower. That is the point where `market-evaluation` fails the test.

## What this screen does not kill

Three rules that sound prudent are structurally anti-venture. They kill the bets that actually return a fund, so this screen does not use them:

- No existing budget line. That excludes every category-creating bet.
- Buyers who cannot be reached async by writing. That excludes sales-led and consumer.
- An industry insider could execute better. Outsiders out-executing incumbents with capital and talent is a standard venture pattern.

## The three failure modes

**Anchoring.** The founder finds one interesting thing and stops searching. Everything after is rationalisation dressed as research.

**TAM fantasy.** The founder finds a large number in an analyst report, multiplies it by a share they have no mechanism to win, and calls it a market. "$10B market, we take 10%" is unfalsifiable, which is precisely why it survives scrutiny for months and then dies in a partner meeting. The number is not the problem; the absence of a mechanism is.

**False rigour.** The screen itself produces a confident wrong answer. A bottom-up number computed from the wrong denominator, the wrong pricing basis, a stale ACV or a mis-read constraint looks far more credible than a guess and is much harder to argue with. Every rule below marked FALSIFY exists because this failure mode killed real candidates.

Counter all three:

- A batch of 12–15 candidates from distinct origins before screening any of them (see "The batch it screens").
- An idea the founder arrives with is one candidate. It competes; it does not seed.
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

### One formula: customers × revenue per customer

This is `market-evaluation`'s axis 1, and the screen uses it unchanged:

```
ceiling = N x revenue per customer
```

N is a countable customer population with a source. Revenue per customer is what a comparable product charges **today**, with a source. The pricing basis can be a seat, usage, or a take rate. When money moves through the workflow, revenue per customer is the flow each customer moves times a take rate sourced from the nearest real comparable. A ticketing platform earning 9-10% of ticket value and a venue-software vendor charging $10k a seat serve the same buyer and differ by two orders of magnitude, so pick the basis the product would actually charge on. Do not compute several bases and take the largest.

Also ask how fast N or the flow is growing. A $2bn ceiling growing 25% a year is a better bet than a $4bn one that is flat.

### Name the revenue shape

For every candidate, killed or not, state which of Janz's five shapes, scaled ×10 for $1bn, the ceiling follows. This is the same table `market-evaluation` uses, so the survivor arrives with its shape named:

| Shape | Customers for $1bn | Revenue per customer / year |
| --- | --- | --- |
| Elephants | 10,000 | $100k |
| Deer | 100,000 | $10k |
| Rabbits | 1M | $1k |
| Mice | 10M | $100 |
| Flies | 100M active users | $10 (ads) |

If the candidate's N falls far short of its shape's customer count at its revenue per customer, the arithmetic has already answered the question.

### Price is the highest-variance input in the screen

It has been wrong in both directions, by roughly an order of magnitude each way. Three rules, all cheap:

**1. Look up what incumbents actually charge. Never infer a blended price from enterprise anecdotes.** Most vertical software publishes its pricing. Reasoning "the enterprise vendor does six-figure deals, so call it $25k blended" produced a ceiling 6x too high in one real batch, against published tiers that topped out near $11k. Two minutes on two pricing pages settles it. Where pricing is gated, price the tier your buyer would actually land in, not the one the vendor leads with.

**2. Price at today's level.** Do not raise revenue per customer with a projected expansion multiple. `market-evaluation` prices from comparables today and scores a price nobody pays yet as an unproven price, so a ceiling built on a mature ACV passes candidates the evaluation fails. Growth past today's price counts only as a **named adjacency** (step 8), which `market-evaluation` credits on its adjacencies axis. A sourced net-retention figure from a comparable that sells to the same buyer goes in the log as supporting evidence; it does not pass a candidate.

**3. Write down the basis.** Record N and its source, revenue per customer and its source, and the pricing basis. A kill that cannot show all three is not auditable.

### Heroic share is the kill line

Ask what share of the ceiling $1bn ARR requires. Kill when the math reaches $1bn only with **heroic share (over ~30%)**, an **unproven price**, or **adjacencies nobody has named**. These are `market-evaluation`'s bear conditions for axis 1, and they are the same three here.

A fragmented market with low switching costs and many substitutes holds less than 30%: a funded follower takes share back. Treat its practical line as lower, and say so in the log.

Do not argue past 30% on the strength of Epic or Veeva. Both exceeded half their categories, and both took fifteen to twenty years to get there. Assuming you hold a third of a category inside a 10-year horizon is exactly the unfalsifiable assumption this step exists to stop.

A named adjacency can carry a ceiling past $1bn only when it is named here and connected in step 8 by the same buyer, data or integration. An adjacency you cannot name does not count.

### FALSIFY before any structural verdict

Before writing that a category, a segment or an industry is too small, spend fifteen minutes searching for companies in it above $100M revenue or $1B valuation. Once per category, not per candidate, so the batch time-box survives.

**If a top-down conclusion contradicts one sourced counterexample, discard the conclusion, not the counterexample.** A single real company at $180M revenue kills a model that said the whole category was $250M. The model was the guess; the company is the fact.

The same test catches a ceiling that is too low: if a real company's current revenue exceeds the ceiling you just computed for its whole category, the ceiling is wrong. The usual cause is a missed revenue pool or the wrong pricing basis.

When the verdict rests on an industry's total size, check the denominator before writing it down. Industries have several revenue pools and it is easy to size one and call it the whole. Name the pools you included and the pools you left out. If you cannot name what you left out, you have not checked.

### Apply the same rigour to survivors

The most common way this step fails is asymmetry: a generous ceiling for the candidate you find interesting, stingy ones for the candidates you are killing. Recompute the survivors' ceilings last, with the same sources and the same scepticism, and check specifically whether the survivor's category has a *sourced* market size smaller than the ceiling you constructed for it.

## The batch it screens

The screen takes a batch from `venture-ideation`. If the founder has no batch, run that skill first. If they bring their own candidates, check the batch against the same rules before screening, because a narrow batch makes every screen result look like a sector verdict:

- 12–15 candidates, each one sentence naming a countable buyer, what they get, and the population N, with a source link or an *(assumption)* label. "AI for logistics" is not a candidate.
- The batch spans distinct origins: no single lens (edge, thesis, expired dogma, hard idea, maze, overlooked market, fringe behaviour, visible spend) supplies more than a third.
- No more than two candidates per domain, at least three outside the founder's own industries, and any idea the founder arrived with sits in the batch as one candidate among the rest.

If the batch fails these, say which rule it breaks, screen it anyway, and say that zero or one survivors from a narrow batch says little about the sectors. Offer a `venture-ideation` run to fill the gaps.

### Restate every constraint as a test before applying it

Founder constraints arrive as labels and get applied as categories, which silently kills whole segments. Convert each into a test of what the founder actually meant, and write the test down:

- "No B2C" almost never means "no individual buyers." It means **the buyer does not expect the purchase to generate income**. A sole proprietor paying for business software is not a consumer; a fan paying for an app is. Applying the label rather than the test excludes every prosumer and small-business segment, which is where several of the largest vertical outcomes live.
- "No hardware" usually means no inventory risk, not no physical product.
- "No regulated industries" usually means no multi-year licensing path, not no compliance exposure.

If the test is ambiguous, ask the founder once. A mis-read constraint is a silent kill: it never appears in the log, so nothing later can catch it.

## The screen

Five to ten minutes per candidate, search-assisted. **Kill on first fail and move on.** Order is by cost: the arithmetic kills come before the judgment calls.

1. **Constraint conflict.** Apply the *test*, not the label. Kill immediately on a real conflict; do not argue that this one is different.

2. **Scale ceiling.** Look up incumbent pricing, compute N × revenue per customer at today's price on the basis the product would charge, and name the revenue shape. Kill if reaching $1bn ARR needs heroic share (over ~30%), an unproven price, or an adjacency nobody has named, or if the ceiling does not reach $1bn at all. Write the numbers, the basis and the shape down even when it passes; the handoff needs all three.

3. **US first.** If the market is not the US, name the US equivalent market and check whether a US player already exists. Kill unless there is a specific, sourced reason the smaller market wins: regulation that does not transfer, a local incumbent structure with no US counterpart, or a problem that does not exist in the US. When a US and a non-US version of the same idea exist, usually only one wins, and it is usually the US one. For a US market, note whether the US is a good launch market and move on.

4. **Where the money is.** Name the pool: a budget line, an adjacent budget, a labour cost, a flow you can take a percentage of, or a measurable cost borne in time and workarounds. Unlike the bootstrap screen, "nobody pays for this today" is **not** an automatic kill; it is how category creation looks at the start. It is a kill only when no cost is being borne at all. If the pain is real but costless, there is no business.

   Then classify the market as crowded, untapped, or both. **Crowded** proves the demand and demands a wedge (step 8) and an uncopyable asset (step 9). **Untapped** demands a sourced reason the gap exists: the technology only just became possible, a regulation changed, or a cost curve crossed a threshold. That reason is usually the why-now in step 5. If you cannot name one, kill: the likeliest explanation is that the demand is not there.

5. **Why now: a changed number, and a window.** Both required. This is the step most worth being strict about, because it is the easiest in the screen to fake — every domain has something that changed, at all times.

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

   Record, beside the why-now, the structural forces that grow the market without the company's help: regulation, demographics, cost curves, platform shifts. They are `market-evaluation`'s tailwinds axis. Note any force that helps incumbents as much as entrants, and any visible headwind.

6. **Commoditising layer.** If the value delivered is analysis, drafting or generic insight, its price is collapsing toward zero. Kill unless the durable part is data access, workflow lock-in, distribution, trust, or regulatory position.

7. **Feature or company.** Is the natural home for this a checkbox in a product that already owns the buyer relationship? If a platform with existing distribution would ship it the quarter after you prove demand, kill. Your funding round is a public announcement of the opportunity, so "incumbents are slow" is not protection.

8. **Wedge and year-3 asset.** A beachhead narrow enough to win outright, adjacent enough to expand from. Name the wedge, the **asset the company will own in year 3** (data, workflow position, distribution, trust, or installed base), and the next one or two products that asset makes inevitable. Name the mechanism connecting wedge to next product: the same buyer, the same data, the same integration. Kill if the wedge is an island, if the expansion is opportunistic, if the asset does not transfer, or if an incumbent already owns the adjacency. A defensible niche with no adjacency is a fine business and a bad venture bet; log it as a niche and move on.

   Note that the mechanism you name here is the same one any adjacency in the step-2 ceiling assumes. If they disagree, one of them is wrong.

9. **Accruing advantage.** This is `market-evaluation`'s year-3 test for a crowded market: what will the company have that a well-funded competitor starting today cannot copy? Assume a competitor with $30M and a good team enters eighteen months after you launch. What do you have then that they cannot buy? Proprietary data that improves the product, network effects, switching costs, supply locked under contract, a regulatory or certification position. "We execute better" is not an answer. This step kills more candidates than any other and should.

   **Pricing is a wedge, not a moat — unless.** A competitor changes a pricing page in a week, so "we charge differently" is not an answer to this step on its own. A pricing model counts here only when one of these holds:

   - *Incumbent-incompatible.* Matching you would wreck their revenue recognition, their salesforce comp or their existing book — consumption pricing against perpetual licences, free-seat bottom-up against an enterprise channel. The incumbent is not slow, they are structurally unable. Real, but it is an innovator's-dilemma window with an expiry like any other: it closes when they get desperate enough to eat the transition. Date it in step 5.
   - *Capability-gated.* The model requires something the competitor does not have. A take-rate requires moving the money, which requires licences, rails and payee onboarding. Outcome pricing requires measuring outcomes. Note that the barrier is the capability, not the price.

   And in both cases the model must **accumulate** something, because that is what the moat turns out to be. Take-rate accumulates transaction history and payee relationships; consumption accumulates workload lock-in; a free tier accumulates a user graph. Snowflake's durable advantage became data gravity, Figma's the multiplayer file as the organisation's source of truth, CrowdStrike's the sensor and threat graph — in each case the pricing got them in and something else kept them there. A pricing model that accumulates nothing is a discount with a story attached.

10. **Learning speed.** Every market comes with a go-to-market attached, and the go-to-market sets how many learning cycles fit in 18 months. Name the buyer and the user, source the typical sales cycle, and estimate the cycles:

    | Fast loop — about 30 cycles in 18 months | Slow loop — 1 to 2 cycles in 18 months |
    | --- | --- |
    | A user can try it without asking anyone | The buyer is not the user; procurement gates entry |
    | The value is obvious in hours | The value is obvious in quarters |
    | Retention shows in week one | Each customer costs as much as the last |

    Kill when the loop is slow on all three rows and the founders have no named network into the buyers. That is -3 on `market-evaluation`'s speed test. A slow loop with a named network survives, but say what the network would have to be, and do not assume the founder has one.

What the screen still does not ask: technical feasibility, competition depth, or revenue projection. Feasibility in particular is a trap for technical founders, because "could I build this" is the one question they can answer instantly and it correlates with nothing.

Expect one to three survivors from fifteen. If more than half survive, the usual cause is generous arithmetic at step 2 or a hand-waved answer at step 9. If **none** survive and several died at step 2 with similar numbers, suspect the screen before concluding the sector is dead: run the FALSIFY search, check the denominator, and check the pricing basis: a kill priced per seat when money flows through the workflow is an unfinished calculation.

## The candidate log

Append every batch. This is the compounding asset of the practice. It is wide — keep it in a spreadsheet, not a document.

| Date | Candidate (buyer + workflow + N) | Surface + link | Revenue per customer + basis + source | Ceiling + shape | Share of $1bn needed | US first | Why-now + window closes | Learning cycles in 18 months | Killed at step | The killing fact | Recheck trigger |

Three columns make a step-2 or step-5 kill auditable rather than just recorded. A kill priced per seat is worth revisiting the moment you find the flow the workflow sits on, or a named adjacency. And a candidate killed because its window was closing is worth nothing later — but a candidate killed for another reason whose window is still open is the first thing to re-screen next batch.

Two entries matter beyond the kill:

- **The killing fact**, specific enough to be wrong. "Market too small" is weak. "Census and two trade-association counts both put this at 4,100 firms; at $60k per customer benchmarked from the incumbent's published pricing, the ceiling is $246M, so $1bn is out of reach without an adjacency, and none is named" is a fact that can be overturned by better data.
- **The recheck trigger.** Many venture candidates die on a condition, not a principle: a cost curve not yet low enough, a rule not yet in force, an install base not yet large. Write the condition and the date. These become the strongest candidates in later batches because the work is already done.

Step 9 kills are the most reusable. Step 2 kills are the **least** reusable despite being the most common, because they depend on N, revenue per customer and pricing basis, any of which can be wrong. Re-derive a step-2 kill before trusting it in a later batch.

## Handoff

For each survivor, one short paragraph:

- The buyer, countably defined, with the source for N.
- The workflow and what it costs them today, with the source.
- Revenue per customer with its pricing basis and source, the ceiling, the revenue shape, and the share of the ceiling that $1bn ARR needs.
- US first: the US equivalent market for a non-US candidate, and the sourced reason it still wins.
- Why now: the changed number with its date and source, the window's closing mechanism, your estimate of when it closes, and the structural tailwinds.
- The wedge, the year-3 asset, the next one or two products, and the mechanism between them.
- What accrues, and why a funded follower cannot buy it. If pricing is part of the answer, say which of the two tests it passes and what it accumulates.
- Learning speed: the buyer, the user, the sourced sales cycle, and the estimated cycles in 18 months.
- The single fact that would kill it, and the cheapest way to check it.

Then run **`market-evaluation`** on each survivor, with the paragraph above as its starting evidence. It runs all nine axes with sourced bull and bear cases, scores each from -5 to +5, and gates each test. A survivor that fails any of the three tests stops there; log the failing axis as its killing fact. A survivor that passes all three goes to the founder's customer conversations, not to more desk work.

Do not attach an advocacy paragraph. A survivor carried into the evaluation pre-argued corrupts the bear cases, which are the part of the evaluation doing the real work.

## Anti-patterns

- **Two bars.** Screening against $100M and evaluating against $1bn, or any other gap between this screen and `market-evaluation`. The screen then passes candidates the evaluation fails, and the pipeline wastes its most expensive step.
- **Mature pricing.** Raising the ceiling with a projected expansion multiple. `market-evaluation` scores that as an unproven price, so the screen would pass a candidate the evaluation fails.
- **Inferred price.** Reasoning a blended price from enterprise anecdotes when the category publishes its tiers. Wrong by 6x in one real batch.
- **Wrong pricing basis.** Pricing per seat a workflow that money flows through, or computing several bases and taking the largest instead of the one the product would charge on.
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
- **Wedge as destination.** A defensible niche is a real business. It is not this search. Log it and keep going.
- **Capital mismatch.** A candidate that cannot absorb $20M productively does not become venture-scale by raising it. Cash does not create demand.
- **Too early.** Right thesis, wrong decade. The recheck trigger exists for exactly this; write it down and move on rather than funding the education of the market.
- **Depth creep.** Doing the full evaluation's work inside the screen. Symptom: an hour per candidate, a batch of four.
- **Discovery as avoidance.** Running batches instead of executing a live bet. Discovery is for the gap between bets.

## Cadence

A half-day batch — `venture-ideation`, then this screen — when a bet ends or the queue runs dry, and the log connecting them. Batches reward re-running on a schedule, because the interesting ones move: a cost curve you checked eighteen months ago is now somewhere else, and the recheck triggers and still-open windows in the log tell you which ones to look at first.