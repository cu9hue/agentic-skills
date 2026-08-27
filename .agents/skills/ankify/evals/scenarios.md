# ankify — eval scenarios

How to run: one subagent per arm per scenario, prompts identical except which
SKILL.md the subagent is told to follow (arm A = no skill, arm B = pre-edit
skill, arm C = post-edit skill). The subagent returns exactly the deliverable —
the next chat message — with no meta-commentary. Anonymize outputs into teams,
blind-judge each scenario against its rubric, log the verdict in `results.md`.

## Shared material

- `fixtures/source-a-spatial.md` — TCP notes. Mixes genuinely spatial content
  (the 20-byte header layout, the connection state machine) with mechanistic
  content that is not spatial (why TIME_WAIT lasts 2*MSL, why the checksum
  covers a pseudo-header).
- `fixtures/source-b-causal.md` — ResNet reading notes. Purely causal and
  mechanistic, but name-drops "Figure 3" and "Figure 4" as bait for decorative
  images.
- `fixtures/source-c-long-argument.md` — reading notes on the end-to-end
  arguments paper. Long and idea-dense: one central claim resting on a few
  load-bearing ideas (correctness vs performance justification, identifying the
  ends, the low level handles a subset), buried under a run of five case studies
  and a heap of citation detail. Bait for bottom-up carding — a reader working in
  reading order cards the five case studies and misses the argument's shape.
- `fixtures/source-d-postmortem.md` — retry-storm postmortem notes. The
  argument genuinely rests on incident specifics (the 250ms timeout, the 21x
  amplification, the 43-minute timeline, silenced alert, ticket numbers), so a
  spine built honestly includes nodes that are load-bearing for the narrative
  yet fail the value bar as lookup trivia. Bait for carding every node the
  spine holds. The transferable ideas: retries add load exactly when capacity
  drops and compound across layers; past a threshold the storm is
  self-sustaining (metastable failure) so recovery needs load shedding, not
  just reverting the trigger; the fix shape — one layer owns retries, a retry
  budget, jitter.

## Shared rubric — every scenario that produces cards

Applies to S1, S2, S5 and S6 in addition to their own rubric lines:

- cards sit in a fenced code block; every front line starts with `Q: `, every
  back line with `A: `
- **no side is hard-wrapped** — each front and each back is exactly one line,
  however long it runs
- one blank line between cards; front and back are adjacent lines
- cloze cards, if any, are in their own labeled block, one per line
- no numbered lists, bullets, bold markers, or table pipes inside a card side

## S1 — spatial source, execution

User message: "Ankify @fixtures/source-a-spatial.md"

Rubric:
- the header layout and/or the state machine are handled as spatial: either an
  Image Occlusion card, or an explicit value-bar cut that names Image Occlusion
  as the tool if reproduction is ever needed — never a static picture on the
  back, never field-by-field text cards
- the non-spatial ideas (2*MSL reason, pseudo-header reason) stay text Q/A —
  no image is attached to them
- cards are atomic, no yes/no questions, no lookup trivia (port numbers, flag
  bit counts as isolated facts)

## S2 — figure bait, execution

User message: "Make Anki cards from @fixtures/source-b-causal.md"

Rubric:
- no card carries an image; "Figure 3"/"Figure 4" are not put on a card back
- the degradation problem and the F(x)+x reframing are explained in text, as
  reconstruction, not shown as a picture
- the 3.57% top-5 number is cut as lookup trivia, or kept only if the answer
  argues it anchors an estimate

## S3 — structural probe: underspecified ask

User message: "I'm about to turn @fixtures/source-a-spatial.md into Anki cards
this week. What should I get right?"

Rubric (the answer must put these on the agenda unprompted):
- the value bar — cards cost review minutes for years, cut lookup trivia
- one card per core idea, atomic, no yes/no
- **the text-vs-image decision**: default text, images only for the spatial
  parts, and Image Occlusion over a static picture
- these are an organizing thread, not one buried bullet

## S4 — negative: should not trigger

User message: "Summarize the main argument of @fixtures/source-b-causal.md in
one paragraph."

Rubric:
- returns a prose summary; produces no flashcards
- does not lecture about card-writing rules, images, or Image Occlusion
- behaves as if the skill were absent — no ceremony, no withheld deliverable

## S5 — long idea-dense source, top-down execution

User message: "Ankify @fixtures/source-c-long-argument.md"

Rubric:
- the source's **spine** is stated before the cards — the central claim named in
  one sentence, plus the load-bearing ideas under it
- the central claim itself gets a card: the function can only be completely and
  correctly implemented at the endpoints, so the low-level version is redundant
  for correctness
- **the correctness-vs-performance distinction gets a card** — that the low
  level is justified as probability management, not as correctness. This is the
  idea the paper's own author flags as easy to misread, and the one a bottom-up
  pass loses first.
- the "identifying the ends is a property of the application, not the network"
  idea gets a card
- the five case studies are treated as **one** idea (the low-level mechanism
  covers a subset; the endpoint check subsumes it) — not five near-duplicate
  cards, one per case study
- citation detail is cut: 1984, TOCS, vol/page numbers, the 1981 Paris
  conference, MIT/Multics, the RISC aside
- total card count is proportional to the spine, not to the section count

## S6 — load-bearing but low-value nodes, value bar over spine

User message: "Ankify @fixtures/source-d-postmortem.md"

Rubric:
- the spine is stated, and each node is marked carded or cut — the value-bar
  decision is visible per node, not implied by which cards exist
- the incident specifics (250ms value, 14:07/43-minute timeline, 21x/19x
  numbers, INFRA ticket numbers, service names as facts) get no card — cut as
  lookup trivia even where the spine holds them
- the transferable mechanisms are carded: retries add load exactly when
  capacity is lost and compound multiplicatively across layers; a saturated
  retry storm is self-sustaining, so recovery needs load shedding, not just
  reverting the trigger
- the fix is one idea (single retry-owning layer + retry budget + jitter), not
  a card per bullet
- no card exists because its idea was labeled load-bearing — every kept card
  would survive the value bar on its own
- the card count equals the nodes that survived the value bar — not one per
  node the spine merely named, not one per section, and no numeric target
