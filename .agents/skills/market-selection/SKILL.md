---
name: market-selection
description: "Use when a founder is choosing where to look next rather than judging one idea: \"what should I explore next?\", \"where should I look?\", \"what directions or trends fit my edge?\", between bets, or when every idea so far has been killed. Not for scoring one named market (market-evaluation) or mapping a single problem space (market-map)."
origin: "Shift-first framing and the 100-messages test from an Entrepreneur First principal's feedback session (2026-10); edge lens from Alice Bentinck, \"Ideas Pt I/II\" (EF); thesis format from EF's Fall26 guide \"How to Think About Market Selection\"; widening question (\"is X the only segment that cares?\") from the same EF session"
---

# Market Selection

Find **directions** worth a founder's next month: a dated shift in the world, the
buyer it creates pain or budget for, and where the founder's edge changes the
outcome. End every direction in a belief and a cheap test against real buyers.

This skill widens before it narrows. Its predecessors screened narrow candidates
at a desk and killed nearly all of them, because almost every real market has a
competitor and almost every competitor fails a desk screen. A competitor is
evidence that buyers pay. The kill belongs to the test, run against people,
not to the screen.

**When the request names one market to judge** ("is X a good market?",
"score X"), this skill does not apply: evaluate that market, or hand it to
`market-evaluation`. Do not answer with alternative directions.

## Never block on questions

Ask before working **only** when the request carries neither a domain nor a
founder profile ("where should I look?" and nothing else). In every other
case, infer what is missing, label each inference *(assumed)*, deliver the
full output, and end with one short "To sharpen this" list of the 2–3
answers that would most change the ranking. A reply that only asks questions,
when the founder gave a domain or a profile, has failed.

## Step 0 — set the bar before anything else

Ask one question when the request carries nothing to infer from; otherwise
infer the bar (a solo founder who mentions no raise implies bootstrap; a
raise or a co-founder pitching investors implies venture) and label it:

> Are you building toward venture scale, or a business you can bootstrap? If
> venture: what ceiling should directions be held to — $1bn ARR in under 10
> years, a $1bn exit, or your own number?

- **Bootstrap bar:** a profitable business the founder can run, reached within
  12–18 months from revenue, not capital. Ask for the income target if it
  matters; a few dozen to a few hundred paying customers is often enough.
  Small buyer populations are fine. A slow, procurement-heavy sale is not,
  unless the founder says they can afford it.
- **Venture bar:** the ceiling the founder names. Default to $1bn ARR in under
  10 years when they name none, and say so.

Ask only when the bar type is unknown. When the type is known but the ceiling
is not, use the default ceiling, label it *(assumed)*, and continue. When you
do ask, ask the bar and Step 1's inputs in the same single message, and add
the 2–3 kinds of shift you would look at first given what you already know,
so the founder gets something useful from the first reply.

If the founder says "just go" or gives no answer, assume the bar their profile
implies, label it *(assumed)* at the top, and continue. Write the bar at the
top of the output. It changes which directions rank first, how big a buyer
pool must be, and how each test is sized. Never switch it mid-run.

**Geography travels with the bar.** Take it from the brief. When the brief
gives none, infer it from the profile only if the profile names a region;
otherwise assume **US**, or **global** for a product sold online with no
local rule behind it. Write it beside the bar as *(assumed)*, and put it
first in "To sharpen this". Shifts, buyers and tests
stay inside that geography; at most one direction may sit outside it, marked
*(outside your geography)* with the reason it is worth the exception. A
region the founder ruled out is a stated constraint: never rank a direction
there.

## Step 1 — collect the founder's inputs

Use what the request gives; infer the rest and label it. Ask for these only
in the no-domain, no-profile case, in **one** message:

1. **Edge.** What can you build or do that few founders can? What rare insight
   do you hold? Compare against the founder population, not colleagues.
2. **Constraints.** Solo or team; B2B or consumer; geography; values (for
   example "net positive", or buyers you will not serve); runway.
3. **Already explored.** Ideas already tried or killed, and why. Treat them as
   evidence for patterns, not as a list to re-screen.

Restate the edge as **capabilities that travel** (what the founder can do,
stripped of the industry they did it in). An edge stated as an industry
generates the founder's last job twelve times.

## Step 2 — collect shifts, not ideas

A **shift** is something more true this year than last, with a date: a cost
collapse, a capability crossing a threshold, a rule or deadline, a new rail or
platform, an incumbent retreating or repricing, a failure or scandal that
brings new scrutiny, a behaviour already happening at scale with no product.

Gather 8–12 shifts across at least four of those types. Sources, best first:

- Primary text: the rule, the changelog, the pricing page, the filing.
- Money already moving: job ads for the same narrow task at unrelated
  companies, "we built this in-house" posts, fixed-price service packages.
- Pain inside a proven budget: two- and three-star reviews of paid tools,
  migration threads, incident post-mortems.
- Fringe behaviour: spreadsheets, group chats and hobbyist tools doing a job
  at scale.

Trend articles and "top N" lists are pointers to primary data, never evidence
themselves.

**Search with Exa only.** Never use WebSearch, and never query a search
engine through curl. Use `mcp__plugin_exa_exa__web_search_exa` with
descriptive queries (describe the page you want: "2026 job ads for
settlement analysts at US battery storage owners", not keywords), and
`mcp__plugin_exa_exa__web_fetch_exa` to open the page itself. Load both with
ToolSearch if they are deferred. Use treg only for data Exa cannot reach
(X posts, paid datasets), and quote its price before the first call.

A search result is a lead, not a source. Before a shift goes in the table,
open its page with `web_fetch_exa` and confirm the date or number is on it;
batch several URLs in one fetch call. When calls are limited, fetch the
pages behind the shifts you keep before running more searches. A shift you
could not open gets *(not opened)* beside its link. Without Exa in the
session, write *(needs source)* next to the shift. A shift
with no date is a theme, and themes go in a separate line, not the table.

## Step 3 — look for patterns

Read the shifts and the founder's already-explored ideas together and ask
what keeps recurring. A **pattern** is the same underlying need showing up in
unrelated industries or signals: for example, three different automated
systems whose vendors grade their own homework, so buyers pay a person to
check them.

Name 1–3 patterns, each with the signals it rests on. A pattern seen in three
or more unrelated signals is the strongest output of the run, stronger than
any single direction, because it survives the death of any one buyer. When the
founder brought killed ideas, extract what the dead ideas share first; that is
usually where the over-constraint is hiding.

## Step 4 — turn shifts and patterns into directions

A direction is one sentence:

> [Shift] creates [pain or budget] for [countable buyer], and [edge
> capability] changes the outcome because [reason].

Produce 3–6. When the founder arrives with several ideas already killed,
produce **at most 3**, keep the shift table to the shifts those directions
use, and open the directions with the one test to start: an over-constrained
founder needs a commitment, not a longer list. Before settling each buyer,
**widen**: ask "is this the only
segment that feels this pain?" Run the buyer list outward: the end customer's
customer; whoever carries the loss (insurer, lender, sponsor bank, auditor);
platforms whose trust-and-safety or compliance budget the pain lands in;
multi-site operators. A different buyer can change the size and speed of the
sale by an order of magnitude. If widening finds a better buyer, swap it in.

Hold these quotas:

- At least two directions where the edge is the reason the founder wins, not
  merely relevant. Test: would the product work the same without the edge? If
  yes, the edge is decoration.
- At least one direction outside the founder's own industries, carrying a
  capability to a new buyer.
- No more than two directions from the same shift.

## Step 5 — rank, do not kill

Order the directions. Drop one only when it breaks a constraint the founder
stated (wrong buyer type, a value they named, a bar it structurally cannot
reach); say which constraint. Everything else stays in the ranking with its
main risk named.

Rank on three things, in this order:

1. **Shift strength.** Forced beats discretionary (a dated rule or deadline
   beats a preference); a dated shift beats an undated one; a shift with money
   already moving beats one with only talk.
2. **Edge fit.** The edge changes the buyer's outcome, not just the build.
3. **Bar fit.** Under the bootstrap bar: can the founder reach buyers and sell
   within months, without capital? Under the venture bar: can the buyer pool
   plausibly reach the ceiling, given the shift's trajectory?

Competition is a risk to name, not a reason to drop. "Funded startups are
crowding the horizontal version" is a reason to go narrower, which is a
direction rewrite, not a kill.

## Step 6 — a belief and a test for every direction

Each direction carries:

- **Belief:** "I believe [buyer] will pay for [outcome] because [shift], and
  this is true by [date]." Say it as a bet, not a hedge.
- **Test against real buyers:** who to contact (role and company type), how
  many, the one question that would reveal the pain, a pass threshold, and a
  time box. Defaults: 100 targeted messages with a pass at 3 or more replies
  that describe a real incident or spend, inside 2 weeks; or 10–15
  conversations with the person who carries the loss, with a pass when at
  least a third describe a cost they already pay.
- **What would kill it:** the specific result of the test that ends the
  direction. The kill comes from the test, never from a desk search.

## Step 7 — hand off

- **Bootstrap:** recommend the one direction to test first and why, and the
  test to start this week. Offer `market-map` to map the chosen direction's
  workflow after the first replies arrive. Stop there.
- **Venture:** recommend the 1–2 directions worth a full `market-evaluation`,
  and pass the ceiling the founder chose. Run the tests first where they are
  cheap; the evaluation is better with buyer evidence in hand. Do not score
  the nine axes here.

## Output

```
**Bar:** <bootstrap | venture, ceiling> <(assumed) if so>
**Geography:** <region> <(assumed) if so>
**Edge as capabilities:** <2–5 that travel>

## Shifts
| Shift | Type | Date | Source |

## Patterns
- <pattern> — signals: <a>, <b>, <c>

## Directions (ranked)
### 1. <direction sentence>
- Why it ranks here: <shift strength, edge fit, bar fit>
- Main risk: <one line>
- Belief: <...>
- Test: <who, how many, the question, pass threshold, time box>
- Kill result: <...>

## This week
<the one test to start, and the handoff>
```

## Anti-patterns

- **The desk kill.** Dropping a direction because a search found a competitor
  or a free tool. That is a risk line, or a reason to narrow.
- **Ending at zero.** A run that leaves the founder with nothing to test has
  failed, whatever its rigour.
- **Narrow candidates disguised as directions.** Twelve product ideas in
  twelve verticals are a batch, not a map. Directions are fewer and wider.
- **The undated trend.** "AI agents are taking off" is a theme. Find the date,
  the rule, the price or the count behind it.
- **The decorative edge.** The edge is mentioned in every direction but would
  not change who wins any of them.
- **The home-industry map.** Every direction is the founder's last employer's
  problem.
- **Tests with no threshold.** "Talk to some buyers" cannot fail, so it cannot
  teach.
- **Evaluating inside selection.** Nine-axis scoring and ceiling arithmetic
  belong to `market-evaluation`, after a direction earns it.
