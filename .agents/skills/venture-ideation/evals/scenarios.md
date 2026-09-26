# venture-ideation — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md read by the arm), identical prompts otherwise. Every arm is told to
invoke no skill of its own and to use **no web search or fetch**, so the
generation method is under test, not research luck; sources may be labeled
as assumptions. The subagent returns exactly the deliverable — the next chat
message it would send — no meta-commentary. Anonymize outputs into teams,
blind-judge against the rubrics, log in `results.md`.

The failure this skill targets: generation driven only by visible spend
("countable buyer + workflow + budget") produces a batch of workflow
automation and cost-recovery ideas — Tempting Ideas that are easy to start
and crowded. The rubrics check that the batch spans distinct origins of
ideas and that the founder's edge generates candidates rather than being
appended as a fit note.

## Shared material: founder profile F

Built a real-time risk engine for a leveraged, multi-asset trading exchange;
built data pipelines for quant research and set up quant research agents;
published NLP research (machine translation, transformers); depth in
linguistics and small-data / low-resource learning; light topological data
analysis; ML inference-performance work. Currently in Entrepreneur First. No
stated constraints.

## S1 — generate a batch

User message: "Here's my background: (profile F). Generate a batch of
venture-scale startup candidates I can then screen."

Rubric:
- 10–15 candidates
- the batch spans distinct origins: no single origin (visible spend on an
  existing workflow, automation, or recovering lost money) supplies more than
  about a third, and at least one candidate each comes from the founder's
  capability (edge), a specific non-consensus thesis (X becomes true when Y,
  Y is happening because Z), an expired dogma or moved wall, and a hard idea
- each candidate names a countable buyer and a population N (a labeled
  assumption is fine) and says which origin it came from
- the founder's edge generates candidates (capability → who is blocked
  without it), not only a "fit" line appended to spend-driven ideas
- at least three candidates sit outside the founder's own industries
- hands the batch on for screening rather than ranking winners itself

## S2 — founder arrives with an idea

User message: "Background: (profile F). I already want to build an AI
receptionist for dental clinics. Give me a batch of candidates around it."

Rubric:
- the receptionist idea is candidate zero and competes; the batch is not a
  set of receptionist variants: no more than two rows share its product shape
  (a voice agent answering or making calls), whatever the vertical
- the batch still spans distinct origins, and the founder's edge generates
  at least two candidates unrelated to receptionists
- 10–15 candidates, each with a countable buyer and N

## S3 — structural probe: underspecified ask

User message: "I'm between bets. Help me come up with ideas."

Rubric:
- organizes ideation by distinct origins of ideas (edge, thesis, expired
  dogma, hard idea, idea maze, overlooked markets, fringe behaviour, visible
  spend), not only by spend surfaces or industry lists
- asks the founder-dependent questions those origins need (what can you
  build that few can; which received wisdom in your field has expired; what
  would you love to do that seems impossible), or states assumptions and
  proceeds
- does not open with a generic list of trendy ideas

## S4 — negative: evaluate one market

User message: "Is pet insurance a good market to build a startup in?"

Rubric:
- does not generate a candidate batch or run ideation lenses
- answers the market question directly (or routes to a market evaluation)
