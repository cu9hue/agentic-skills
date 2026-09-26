---
name: venture-ideation
description: "Use when a founder needs startup candidates rather than a verdict: \"I need ideas\", \"what could I build?\", \"give me a batch\", between bets, or when every idea so far looks the same. Not for screening a batch you already have (venture-bet-discovery) or for judging one named market (market-evaluation)."
origin: "Edge lens from Alice Bentinck, \"Ideas Pt I\" and \"Ideas Pt II\" (Entrepreneur First); hard-idea lens from Alex Crompton, \"Hard Ideas\"; maze lens from Chris Dixon, \"The Idea Maze\" (2013); timestamp, overlooked-market and fringe lenses from Elad Gil in First Round Review, \"Future Founders, Here's How to Spot and Build in Nonobvious Markets\"; thesis and pull lenses from Entrepreneur First's Fall26 guide \"How to Think About Market Selection\""
---

# Venture Ideation

Produce a batch of 12–15 startup candidates that come from **different origins**, in a format `venture-bet-discovery` can screen. This skill generates. It does not rank, score or kill; the screen does that.

## Why origins, not surfaces

A generator that only looks at visible spend (job ads, pricing pages, money already moving) produces one kind of idea: automate an existing workflow, or recover money being lost. Those are Tempting Ideas — easy to picture starting, so they need explaining ("if it's easy to start, why has nobody done it?"), and they crowd fast. Entrepreneur First abandoned problem-hunting for this reason: it "created ideas, but it didn't create defensible and globally important ideas."

Ideas originate in several distinct ways, and each produces a different kind of candidate. A batch that spans them is the defence against a monoculture.

## Step 1 — collect the founder's inputs

Four lenses run on the founder, not on research. Ask for these in **one** message, and say that short answers are fine:

1. **Edge.** What do you know that few others know? What can you build that few others can? What rare insight do you hold? (Compare against the founder population, not colleagues.)
2. **Timestamp.** Which pieces of received wisdom in your fields ("never do X, it's too hard") have you seen go stale?
3. **Hard idea.** What would you love to work on that seems impossible?
4. **Fringe.** What are the smartest people you know doing on weekends or at the edges of their jobs?

Also ask for any idea they already hold (it becomes candidate zero) and any constraints.

If the founder has already given a profile, or says "just go", do not block: infer the answers from the profile, label them *(inferred)*, and proceed.

## Step 2 — run every lens

| Lens | Generating question | Candidate template |
| --- | --- | --- |
| **Edge** | What does the founder's capability unblock, for whom? Start from the skill and search outward for a problem. | "[capability few have] lets [countable buyer] do [thing they cannot do well today]" |
| **Thesis** | "Most people don't realise X; X becomes true when Y happens; Y is happening now because Z." Specific, or nothing: "AI will be big" is not a thesis. | "If [X], then [countable buyer] will need [thing]" |
| **Timestamp** | Which "don't do X" was a correct inference about a world that no longer exists? When was it last true, and what changed? | "[dogma] held while [condition]; [condition] ended by [date or number]; so [buyer] can now [X]" |
| **Hard idea** | What stays undone because it looks too hard or unpleasant (complex industries, regulation, hardware, hard software, long timelines, capital)? The difficulty explains the vacuum. | "[buyer] still lacks [X] because [the hard part]; [founder] can do the hard part" |
| **Maze** | Pick a category with famous casualties. What did they get wrong, and which wall — technology, cost, regulation, distribution — has moved since? | "[category] failed for [reason]; [wall] moved; [buyer] is reachable now via [path]" |
| **Overlooked** | Three shapes: a curve people fail to extrapolate; a market that looks crowded but whose incumbents are bad or penetration is low; a market that looks niche because it is boring, high-end, or unfamiliar to most founders. | "[market] looks [small / crowded / boring] but [evidence]" |
| **Fringe** | What behaviour exists at scale with no product — spreadsheets, group chats, hobbyist tools, things that look like toys? | "[population] already does [X] by hand / for fun; nothing serves it" |
| **Pull** | Where is money already spent on a job done badly? Surfaces: the same role posted by hundreds of companies, "we built this in-house", money already moving, published pricing pages, forced migrations, regulatory deadlines, services firms scaling headcount at flat revenue per head, two- and three-star reviews of paid tools. | "[countable buyer] pays [spend] for [job] done badly" |

For every candidate, then ask **who else buys this**, outside the industry the idea sits in: the end customer's customer; brands and agencies (marketing budget); platforms and AI developers (legal, data, trust-and-safety budget); insurers, lenders and auditors (risk budget); multi-site operators (facilities and compliance budget). A different buyer changes N by orders of magnitude. Two credible buyers are two candidates.

## Step 3 — hold the quotas

- **12–15 candidates.**
- **No lens supplies more than a third** of the batch. Pull is the lens that overflows; cap it first.
- **At least one each from Edge, Thesis, Timestamp and Hard idea.** These are the lenses a spend-driven search never reaches.
- **No more than two candidates per domain** (industry or buyer type), and **no more than two per product shape**. A voice agent that answers calls is one shape whether it serves dentists, vets or plumbers.
- **No single founder capability drives more than a third** of the batch. An edge that shows up in every row has stopped generating and started repeating.
- **At least three candidates outside the founder's own industries.** An Edge candidate counts when it carries the founder's capability to a *different* industry's buyer — that is where an edge compounds instead of repeating the founder's last job.
- **Candidate zero competes; it does not seed.** An idea the founder arrives with is one row. Its product moved into another vertical is a variant, and variants count against its product shape's two slots.

## Step 4 — write each candidate as a screenable row

Every row carries:

- **Lens**, and the **origin sentence** in that lens's template (the thesis, the dogma, the capability, the casualty).
- **The candidate**: one sentence naming a countable buyer, what they get, and the population N. "The ~30,000 US mid-market freight brokers who reconcile carrier invoices by hand" is a candidate. "AI for logistics" is not.
- **N's source**, or *(assumption)*. N counts buyers — firms, teams or people who would pay — not products, vendors or transactions.
- **An honest lens label.** The origin sentence must actually come from that lens. Candidate zero's product in a new vertical is not a Timestamp or Overlooked candidate because the row says so.
- **Domain**, for the quota check.

A thesis or a hard idea with no countable buyer yet is not a hunch to discard: run "who else buys this" until one appears. If none does, list it under **Theses without a buyer** below the batch, not in it.

## Step 5 — hand off

Output the batch as a table (#, lens, origin, candidate, N and source, domain), then one coverage line: candidates per lens, domains used, the largest product-shape and capability clusters, and how many sit outside the founder's industries. Then hand the batch to `venture-bet-discovery` for screening.

Do not rank, score or pick favourites. Ranking at generation time lets the most familiar idea win before any evidence is in.

## Anti-patterns

- **Pull monoculture.** Every candidate is "automate X" or "recover lost money". Symptom: the batch reads like a list of job ads.
- **The home-industry edge.** The founder's capability generates twelve variants of their last job. The edge should travel.
- **Seeding.** The batch is candidate zero plus its variants — including the same product relabelled for other verticals or other lenses.
- **The generic thesis.** "AI will change X" has no Y and no Z. Rewrite it or drop it.
- **Contrarian by reflex.** The timestamp lens asks when a belief was last true, not whether its opposite sounds clever.
- **Ranking inside generation.** Winners picked before the screen runs.
- **Trend lists.** "Top N ideas" pieces and funding announcements are downstream of everything and selected for shareability.
