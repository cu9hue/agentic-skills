# market-selection — eval scenarios

Five scenarios. Three execution, one underspecified structural probe, one negative.
Sources for the rubrics: the Entrepreneur First market selection guide, Bentinck's
Edge posts, Crompton's Hard Ideas, Dixon's Idea Maze, and Gil via First Round,
all ingested in the second-brain vault on 2026-09-03.

---

## S1 — Evaluate a candidate with a hidden fatal criterion (execution)

**Prompt:** "I'm thinking of building a tool that lets quant funds backtest
strategies much faster. I spent five years in hedge funds and I know the pain
firsthand. Is this a good direction?"

**Rubric:**
- Names the buyer-concentration problem as potentially fatal, not merely as a risk.
  A structurally capped number of buyers is the guide's own example of a
  deal-killer.
- Distinguishes the strength of the edge from the quality of the market. Five years
  of domain pain is an edge claim, not a market claim.
- Asks what existing spend is being replaced, in budget-line terms.
- Does NOT simply validate because the founder has domain experience.

## S2 — The graveyard discriminator (execution)

**Prompt:** "Loads of startups have tried consumer AI note-taking and none of them
got big. I still think there's something there. Am I walking into a tarpit?"

**Rubric:**
- Applies a three-way discriminator rather than a binary tarpit warning: the market
  architecture is broken, or a constraint broke recently, or the earlier teams
  fumbled a winnable position.
- Demands a named mechanism, not a vibe. Which specific constraint, broken when.
- Names at least one structural property to check: unit economics, entrenched
  behaviour change, free competition from platform incumbents.
- Does NOT answer "yes it's a tarpit" or "no, go for it" without the discriminator.

## S3 — Underspecified structural probe (attention)

**Prompt:** "I've got an idea for a dev tools startup. What should I be thinking
about?"

No axis is named. This tests whether the skill puts market concerns on the agenda
unprompted, rather than answering with generic startup advice.

**Rubric:**
- Raises at least four of: existing spend being replaced, where the product sits
  relative to a control point, whether acquisition gets cheaper over time, feedback
  loop speed, what makes the next product inevitable, why now.
- Asks for the why-now as a specific constraint that broke, not a trend.
- Treats "developers will adopt it bottom-up" as a hypothesis to test rather than
  an assumption.
- Does NOT produce a generic checklist of startup advice with no market structure in it.

## S4 — Generate candidates from a stated edge (execution)

**Prompt:** "My background is inference performance engineering, with research ML
above it and low-latency systems below it. I don't know what to build. Give me
directions worth exploring."

**Rubric:**
- Searches outward from the edge to problems, rather than proposing generic AI
  infrastructure ideas that any founder could pursue.
- Produces multiple candidates, plural, and does not converge prematurely on one.
- For each, names who has the problem and what they currently spend to deal with it.
- Flags at least one candidate as edge-strong but market-weak, since that is the
  common failure for technical founders.
- Does NOT evaluate before generating. Generation first, filtering second.

## S5 — Negative: adjacent but not market evaluation (must not over-trigger)

**Prompt:** "Write the hero section copy for my API monitoring product. The
audience is backend engineers at mid-size SaaS companies."

**Rubric:**
- Writes the copy. That is the deliverable.
- Does NOT interrogate the market, score the direction against criteria, or ask
  whether the founder has an edge.
- At most one short line of market-adjacent observation is acceptable; a criteria
  walkthrough is a failure.
