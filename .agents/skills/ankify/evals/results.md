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

## 2026-08-27 — regression for Q:/A: prefixes + value bar over spine (base 21f45b8)

Two edits, one regression: (1) card sides now carry `Q: ` / `A: ` prefixes —
still one line per side — after the user asked for a visual marker; the shared
format rubric flipped from forbidding prefixes to requiring them. (2) The spine
is now a cap, not a quota: at most one card per node, every node must pass the
value bar on its own, and the presented spine marks each node carded or cut
with its reason. Reported failure this targets: the model carded every
"load-bearing" idea and never ran the value bar.

New fixture `source-d-postmortem.md` and scenario S6 cover the second edit: a
retry-storm postmortem whose spine honestly includes load-bearing-but-lookup
nodes (timeline, config values, ticket numbers) as bait for carding the whole
spine.

Arms: A = no skill, B = pre-edit skill, C = post-edit skill. n=1 per cell —
signal, not proof. Blind judge per scenario; arms shuffled into teams per
scenario. Arm-A transcripts were checked for contamination (the skill files sat
in the same directory as the fixtures): zero reads.

- S1 spatial source: **C**, 5/5 format, 3/3 scenario. B 4/5+3/3 — the missing
  prefixes, as expected. A 4/5+2/3 with one compound card.
- S2 figure bait: **C**, 5/5+3/3. B and A both 4/5+3/3, losing only the prefix
  line. All three cut 3.57% with a stated reason.
- S3 structural probe: noisy. First run C 1/4, B 3/4, A 4/4; a full rerun with
  fresh arms and a fresh judge came back 4/4 across the board with C taking the
  tiebreak on image-decision completeness. Verdict: the first-run loss did not
  reproduce — no regression established. Notable: the no-skill arm passed this
  probe 4/4 in both runs; the base model has largely absorbed the skill's
  attention value here.
- S4 negative: **tie**, all 4/4, "OVERTRIGGER: none". Neither the prefixes nor
  the carded/cut spine leaked into a summary request.
- S5 long argument: **C**, 5/5+7/7, 6 cards behind a carded/cut triage. B
  4/5+6/7 with 9 cards — spine treated as a quota, nothing cut: the reported
  failure, reproduced by the pre-edit skill itself. A 4/5+7/7, 8 cards.
- S6 postmortem (new): **C**, 5/5+5/6, 6 cards, 4 of 10 spine nodes cut with
  stated reasons; incident numbers kept off card backs. B 4/5+1/6 — carded all
  7 nodes it named and put 250ms/21x/19x on answers. A 4/5+2/6, 9 cards, one
  per node. Residual C miss: the fix (owner layer + budget + jitter) shipped as
  two cards, not one.

Judge verdict: the post-edit arm wins every card-producing scenario and holds
the negative; its one loss (S3 first run) vanished on rerun.

Obsolescence: no, but narrower than before. Baseline now passes the structural
probe, so the skill earns its keep on execution — the copy-paste format and the
spine-as-cap discipline — both of which the no-skill arm failed (S1 2/3, S6
2/6).
