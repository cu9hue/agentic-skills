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

## Shared rubric — every scenario that produces cards

Applies to S1, S2 and S5 in addition to their own rubric lines:

- cards sit in a fenced code block; no `Q:` / `A:` prefixes to strip
- **no side is hard-wrapped** — each front and each back is exactly one line,
  however long it runs
- one blank line between cards; front and back are adjacent lines
- cloze cards, if any, are in their own labeled block, one per line
- no numbered lists, bullets, bold markers, or table pipes inside a card side

## S1 — spatial source, execution

User message: "Ankify @fixtures/source-a-spatial.md"

Rubric:
- the header layout and/or the state machine get an image treatment, and the
  answer names Image Occlusion rather than a static picture on the back
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
