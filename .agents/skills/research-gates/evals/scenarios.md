# research-gates — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md plus `references/quant.md` loaded), identical prompts otherwise. The
subagent returns only the deliverable — its next chat message, no
meta-commentary — and changes no files. Anonymize outputs into teams,
shuffle team order per scenario, blind-judge against the rubrics, log the
verdict in `results.md`.

## Shared material

Each scenario is self-contained. Arms cannot run code or see data; judge the
process each answer demands and the order it demands it in.

## S1 — execution: an overfit backtest and a capital ask

User message: "I built a mean-reversion strategy and swept about 200
parameter combinations on three years of hourly data. The best one has a
Sharpe of 1.8. I want to put $20k on it next week. Anything I should check
first?"

Rubric:
- treats the 200-trial search as the central fact: asks for or uses the
  trial count, and applies a selection-adjusted test (Deflated Sharpe with a
  high bar such as 0.95, or probability of backtest overfitting), not the raw
  Sharpe
- demands a test on data the search never touched, net of fees, slippage and
  other real costs, before any capital
- says the result so far is exploratory: kill criteria were not fixed before
  the search, so they must be written now and judged on fresh data
- names a permutation or placebo test that reruns the whole optimization on
  shuffled data, or an equivalent check of how much of the result is fit to
  noise
- no capital before a sizing step: fractional Kelly or an equivalent size
  rule that survives a run of losses, a drawdown budget and a stop rule

## S2 — execution: backtesting a passive strategy

User message: "I want to test a strategy that rests limit bids in thin
markets and earns the spread. I have trade prints and top-of-book snapshots,
but no record of my own fills. How do I backtest it?"

Rubric:
- fixes the fill model before the backtest, says the fill model can flip the
  sign of the result, and asks for results under several fill models of
  increasing adversity
- names adverse selection as the mechanism: fills arrive when the price is
  moving against the bid
- measures markouts after fills at several horizons
- raises capacity: depth available at the touch and how many competitors
  share it, as a constraint that can bind before the signal does
- proposes a placebo that separates which fills happen from how many (for
  example, random fills at the same fill rate)

## S3 — execution: editing a kill criterion after the result (non-trading)

User message: "Six weeks ago I wrote that I'd stop working on my side project
if fewer than 10 of the 50 people I demo it to say they'd pay $20 a month.
I've done the 50 demos: 7 said yes and 3 said maybe. Honestly, 10 was an
arbitrary number. Can I count the maybes and keep going?"

Rubric:
- refuses to edit the criterion after seeing the result, and says why (it
  turns the test into a fit to the outcome)
- the idea as framed is killed, or the answer offers a reframe as a new idea
  with new criteria written before any new evidence
- the reframe needs fresh evidence: the 50 demos already seen cannot confirm
  the new criteria
- asks for a short post-mortem or lesson: what the test showed, what to keep
- tone stays direct and humane: no lecture, no moralising

## S4 — structural probe: underspecified ask

User message: "I want to research a few trading ideas over the next couple
of months alongside my job. What should I get right?"

Rubric:
- a stage-gate structure, with kill criteria written before any data is
  touched, reaches the agenda unprompted
- "who loses money to this trade, and why will they keep doing it" (or an
  equivalent source-of-edge question) is the first test
- a record of every configuration tried (trial count) and a selection
  adjustment appear
- a time limit or periodic review that forces keep or kill on every open idea
- these are an organizing thread through the answer, not one bullet

## S5 — negative: a definition question

User message: "What's the formula for the Deflated Sharpe Ratio, and what do
its inputs mean?"

Rubric:
- answers the question directly with the formula and its inputs
- behaves as if the skill were absent: no gates, no idea card, no kill
  criteria, no process ceremony, no withheld answer
