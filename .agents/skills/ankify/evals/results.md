# ankify — eval results

Append-only. Newest at the bottom.

## 2026-08-15 — backfill + regression for the Images rule (base 50b72a9)

Evals backfilled for this legacy skill, then run as the regression for adding
the **Images** writing rule and its quality-gate line.

Arms: A = no skill, B = pre-edit skill, C = post-edit skill. n=1 per cell —
signal, not proof. Blind judge per scenario; teams shuffled per scenario so no
arm kept a fixed letter.

- S1 spatial source: **C**. Only C routed the header layout and the state
  machine to Image Occlusion by name. B deleted the spatial material rather
  than card it; A forced it into cloze and kept bit-width trivia.
- S2 figure bait: **B and C tie on the rubric** (both passed all three lines);
  the judge's tiebreak went to B on layer-count trivia, which no rubric line
  covers. A kept 3.57% as a bare trivia card. No image regression in C.
- S3 structural probe: **C**. Only C put the text-vs-image decision on the
  agenda unprompted — default text, images for the spatial parts, Image
  Occlusion over a back picture. B never mentioned images at all; A named
  occlusion once with no default-to-text stance and no value bar.
- S4 negative: **tie, no over-trigger**. All three returned a one-paragraph
  prose summary with no cards and no card-writing lecture. C did not leak the
  image rules into a non-card request.

Judge verdict: the post-edit arm holds — it wins both scenarios the edit
targets and regresses nothing. Obsolescence: no. The no-skill arm failed a
rubric line in three of four scenarios, including the structural probe, so the
skill still earns its keep on execution and on attention.

## 2026-08-22 — regression for the copy-paste format + top-down spine (base 48c2385)

Two edits, run as one regression: (1) the output format now emits fenced,
prefix-free, never-hard-wrapped card sides for hand-typing into Anki's Add
dialog; (2) a mandated spine step — name the central claim and its load-bearing
ideas from the whole source at once, before drafting any card.

New fixture `source-c-long-argument.md` (end-to-end arguments reading notes) and
new scenario S5 cover the second edit. A shared format rubric was added to every
card-producing scenario for the first. S3 and S4 unchanged.

Arms: A = no skill, B = pre-edit skill, C = post-edit skill. n=1 per cell —
signal, not proof. Blind judge per scenario; arms shuffled into teams per
scenario so no arm kept a fixed letter.

- S1 spatial source: **C**. B and C both scored 3/3 on the scenario rubric — the
  Images rule from the last entry holds. C won on format, 5/5 vs B's 4/5: B still
  emitted `Q:`/`A:` prefixes inside its fences. A scored 2/3 and wrapped every
  card side in bold markers.
- S2 figure bait: **C**. B and C tie 3/3 on the scenario rubric; C takes it 5/5
  vs 4/5 on format, again on the prefixes. A kept the 3.57% number as bare trivia
  and shipped unfenced cards with bold inside a card front.
- S3 structural probe: **C**, 4/4. B 3/4 — strongest text-vs-image treatment but
  never ruled out yes/no phrasing. A 1/4: treated the image question as an aside
  and recommended one card per flag and per state transition.
- S4 negative: **tie, no over-trigger**. B and C both 4/4 prose summaries. Judge
  recorded "OVERTRIGGER: none" — the spine step did not leak into a request that
  asked for a paragraph, and neither did the format rules.
- S5 long idea-dense source: **C**, 7/7 scenario and 5/5 format, 8 cards. A
  reproduced the reported failure exactly — 18 cards, no spine, separate cards for
  delivery-ack, encryption, duplicate suppression and FIFO, tracking sections
  rather than the argument. B scored 6/7 with 7 cards: it already collapsed the
  five case studies into one idea and kept the correctness-vs-performance
  distinction, and lost only the spine line.

Judge verdict: the post-edit arm holds — it wins or ties every scenario and
regresses nothing.

Honest caveat on S5: the pre-edit skill did better here (6/7) than the reported
real-usage failure suggests. The fixture is 162 lines; the user's complaint comes
from full-length articles. What the edit demonstrably adds on this fixture is the
stated spine, not the case-study collapse — B already did that. Treat the
top-down claim as supported but under-tested at real article length, and feed a
longer source back in as a new scenario when one shows up in real use.

Obsolescence: no. The no-skill arm lost every scenario it could lose, including
the structural probe (1/4) and S5 (4/7), so the skill earns its keep on both
execution and attention.
