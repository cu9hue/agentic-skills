# venture-bet-discovery — eval scenarios

How to run: one subagent per arm per scenario (arm B = pre-edit SKILL.md
inlined in the prompt, arm C = post-edit SKILL.md inlined), identical prompts
otherwise. Every arm is told to invoke no skill of its own and to use **no
web search or fetch**: each scenario supplies the facts it needs, so the
screen itself is under test, not research luck. The subagent returns exactly
the deliverable — the next chat message it would send — no meta-commentary.
Anonymize outputs into teams, blind-judge against the rubrics, log in
`results.md`.

`market-evaluation` is the source of truth for the bar and the axes. The
rubrics check that discovery screens against the same bar ($1bn ARR in under
10 years, Janz shapes ×10, heroic share above ~30%), pre-checks the
market-evaluation axes that can kill cheaply (US first, learning speed,
year-3 asset), and hands survivors to `market-evaluation`.

## Shared material: candidate facts (S1, S2)

Treat these as sourced facts; the arms may not look anything up.

- **K1 — export-control ownership screening.** US exporters must screen
  affiliates 50%-owned by Entity List parties (rule snaps back 10 Nov 2026).
  7,795 "large" US exporters of 271,250 total (Census, 2024). Closest
  incumbent: ~$15k revenue per customer (Visual Compliance, 2019). An
  ownership-graph vendor raised $235M. No net-retention comparable found.
  Buyer: export-compliance manager; typical sales cycle 6–9 months with
  procurement and legal review. Second market named: import-side
  forced-labor due diligence, same buyer.
- **K2 — German tax-advisor practice software.** ~52,000 Steuerberater firms
  in Germany at a published ~€3,000/yr per seat, ~4 seats per firm; DATEV
  dominates. No US company named. Buyer = partner, also the user; trials
  self-serve in a week.
- **K3 — AI phone agents for US home-services SMBs.** ~500,000 US
  plumbing/HVAC/electrical firms; comparable products publish $300–$500/month.
  Buyer = owner = user; self-serve signup; value visible in the first week of
  calls. Net retention comparable: none found.
- **K4 — utility wildfire shutoff decisioning.** 170 US utilities file
  wildfire mitigation plans; comparable contracts ~$1M/yr (assumption);
  PUC approves spending; sales cycles 12–24 months; no founder network in
  utilities.

## S1 — screen a supplied batch

User message: "Here are four candidates from this week's batch (facts
below). Run the venture screen on them and tell me which survive."

(Inline the four candidate facts.)

Rubric:
- the bar is $1bn ARR in under 10 years (not $100M), and each ceiling shows
  bottom-up customers × revenue per customer and names a Janz revenue shape
  scaled ×10 (elephants/deer/rabbits/mice/flies)
- K1 does not pass the scale step as stated: $1bn needs more than ~30% share
  or unnamed adjacencies, so it is killed or explicitly flagged "fails the
  $1bn bar unless …" with the adjacency that would have to hold
- K2 gets a US-first check: names the US equivalent market and kills or
  flags it bearish absent a specific reason the German market wins
- K4 gets a learning-speed check (buyer vs user, 12–24 month cycles, 1–2
  learning cycles in 18 months, no network) that counts against it
- K3's fast loop is credited, and its ceiling is computed honestly (Rabbits/
  Deer shape; states the share it needs at today's price)
- every ceiling is N × revenue per customer at today's sourced price on one
  pricing basis; no projected expansion multiple raises a ceiling or rescues
  a candidate from a kill
- no scores are summed or averaged into a total

## S2 — handoff of a survivor

User message: "OK, K3 survived. What happens next with it?"

(Transcript setup: the arm's own S1 output is not available; tell the arm
only that K3 survived a venture screen with the facts above.)

Rubric:
- routes the survivor to the full `market-evaluation` (nine axes, bull/bear,
  -5..+5, gate per test) before any build
- the handoff carries the ceiling arithmetic, the Janz shape, the year-3
  asset / adjacency, and the learning-speed estimate forward
- does not present an advocacy pitch for K3

## S3 — structural probe: underspecified ask

User message: "I'm between bets and want to find something venture-scale
this month. How should I run the search?"

Rubric:
- the answer is organized by the screen, unprompted: a $1bn-in-10-years
  bar with bottom-up sizing and revenue shape, a why-now with a date, a
  year-3 asset/adjacency, US-first, and learning speed all appear as
  screen steps, not one bullet
- generation comes first as a batch of 12–15 candidates from distinct
  origins (via `venture-ideation`), then the kill-on-first-fail screen
- ends with the hand-off to `market-evaluation` for survivors

## S4 — negative: bootstrapped side business

User message: "I want a side business that pays me about $10k a month
within a year. No investors. Where should I look?"

Rubric:
- does not apply the venture screen or the $1bn bar; says this is a
  bootstrap search (e.g. applies bootstrap criteria:
  existing budget line, reachable buyers, small niches)
- gives a usable answer rather than withholding it
