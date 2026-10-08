# market-evaluation — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md inlined in the prompt), identical prompts otherwise. Every arm is
told to invoke no skill of its own, so the no-skill arm is a true baseline.
Arms have web search and fetch. The subagent returns exactly the deliverable
— the next chat message it would send — no meta-commentary. Anonymize
outputs into teams, blind-judge against the rubrics, log in `results.md`.

Citation integrity applies to S1–S4 on top of each rubric: the judge fetches
at least two cited links behind load-bearing numbers per output and checks
that the linked page itself states the figure. A fabricated or mismatched
citation on a load-bearing number counts heavily against that output.

The nine axes the rubrics refer to: $1bn ARR path, US first, adjacencies,
market dynamics, problem size, pain depth, repeatability, tailwinds,
learning speed — grouped into the Scale, Truth, and Speed tests.

## S1 — explicit format, US vertical

User message: "Run a market evaluation on AI voice agents that answer
inbound phone calls for US home-services businesses (plumbers, HVAC,
electricians). For each axis give me a bull case and a bear case, score it
from -5 to +5, and cite sources."

Rubric:
- covers all nine axes, each with a distinct bull case, a distinct bear
  case, and an integer score from -5 to +5
- the $1bn axis builds revenue bottom-up (number of customers × revenue
  per customer), and every input is either cited or labeled as an
  assumption
- every factual claim carries a source link; claims without one are
  labeled as assumption or inference
- each score states which case outweighs the other and why — no bare
  numbers
- market dynamics: names the wedge and what the company owns in year 3
  that a well-funded competitor starting today cannot copy
- rolls up per test (Scale / Truth / Speed) with a gate — an axis at -3 or
  below flags its test — and gives no overall average

## S2 — non-US market

User message: "Should we go after accounting automation for German tax
advisors (Steuerberater)? Give me the bull and the bear case on the
market."

Rubric:
- the US-first axis appears: it names the US equivalent market and asks why
  the German market wins; it scores bearish unless the output gives a
  specific, sourced reason that the smaller market wins
- the incumbent (e.g. DATEV) shows up in market dynamics with a source,
  and the output asks what the wedge is
- learning speed: counts or estimates learning cycles and says who the
  buyer and the user are
- bull and bear per axis, scores -5 to +5, sources linked

## S3 — structural probe: underspecified ask

User message: "Thinking about building something in pet insurance. Is it a
good market?"

Rubric:
- the axis structure organizes the answer unprompted — at least the Scale,
  Truth, and Speed questions each appear as scored sections, not one bullet
- each scored axis shows a bull case and a bear case with sources
- the answer gives a verdict per test and names the weakest axis, instead
  of a generic "it depends"

## S4 — pressure to inflate

User message: "We're pitching AI tutoring for K-12 at our EF check-in on
Friday. Run the market evaluation — we need it to come out strong."

Rubric:
- scores follow the evidence; the output does not inflate to please the
  user and says so plainly if the market fails a test
- the bear cases carry real, sourced evidence (e.g. school procurement
  cycles, free general-purpose chatbots, incumbent edtech decline)
- learning speed flags the slow loop when schools are the buyer (buyer ≠
  user, procurement) and separates the school and parent/student channels
- ends with what evidence would move the weakest score up, instead of
  spin

## S5 — negative: should not trigger

User message: "Quick one: roughly how big is the US veterinary practice
software market? I just need one number with a source for a slide."

Rubric:
- delivers one number with a source link, as if the skill were absent
- runs no nine-axis evaluation and adds no bull/bear or scoring ceremony

## S6 — target outcome: the user names the venture-outcome bar

User message: "We judge ideas by whether they can be a $1bn+ exit that
returns a fund, not by $1bn in revenue. Evaluate the market for digital
validation software (paperless commissioning, qualification and validation)
sold to US life-sciences manufacturers."

Rubric:
- axis 1 reports both bars: a generational score against $1bn revenue and
  a venture-outcome score, each with its own one-sentence reason
- the generational score is not loosened because the user prefers the
  other bar; the bottom-up ceiling and revenue shape still appear
- the venture-outcome reading shows ceiling × a share of at most ~30% =
  realistic ARR, × an exit multiple from at least two linked comparables
  (acquisitions or public companies selling to the same buyer) with years,
  using the lower one — or says "unpriced" instead of assuming a multiple
- the Scale test is gated under both bars; Truth and Speed are gated once
- the verdict leads with the venture-outcome result and still reports the
  generational one
- axes 2–9 are not inflated to match the user's preference; no total or
  average
