# writing — eval results

Append-only. Newest at the bottom.

## 2026-07-19 — backfill A/B (skill as of f6c594a)

Arms: A = no skill, B = skill + voice-guide. n=1 per cell — signal, not
proof. Mechanical em-dash check ran before judging: clean in S1–S3 for both
arms (baseline avoids em dashes unprompted; keep the check anyway).

- S1: **B**, narrow — both arms invented personal backstory (see gap below);
  A fabricated a checkable "using it daily for a couple of weeks" timeline,
  B's inventions were vaguer
- S2: **B** — A invented a "colorized output" feature not in the brief;
  B stayed on the given facts
- S3: **B**, decisive — A laundered "studies show" into "by some estimates"
  (fake authority survives) and kept the comments-bait close as "tell me
  about it in the comments"; B cut both
- S4: **tie** — both gave a direct two-sentence answer; no over-triggering

Judge verdict: B wins 3–0–1; the de-slop rewrite (S3) is where the skill
pays hardest. Obsolescence: no — baseline failed invented-facts and two of
the hardest S3 tells.

**Known gap fed back from this run:** Core Rule 4 ("never invent facts")
did not fully bind on the personal launch note — arm B still invented "I use
it daily" and a backstory of tools tried. A future edit should strengthen
the rule for narrative pieces (e.g. "in personal pieces, every biographical
claim must come from the brief"); S1's rubric already covers it, so the
regression rerun will show whether the fix lands.

## 2026-07-19 — regression: sourcing/biography edit (pre-edit 1ed5ba3 vs post-edit)

Edit under test: Core Rule 4 rewritten as every-claim-has-a-source (brief or
named research; line adapted from blader/humanizer), new Rule 5 "biography
is claims too", quality-gate line extended, voice-guide guard against
manufactured lived experience. Arms: pre-edit vs post-edit skill, same four
scenarios, blind judge. n=1 per cell — signal, not proof.

- S1: **post-edit** — the target defect is gone: no fabricated usage
  timeline or tools-tried backstory; remaining first-person claims judged
  grantable builder-ran-it inferences. Pre-edit fails the same line it
  failed in the initial A/B.
- S2: tie, both clean
- S3: **pre-edit** by a marginal call — post-edit generalized the fake stat
  to "a big share of most developers' time" (population claim, source
  stripped) where pre-edit personalized it ("my week"); rubric permits
  weakening, so this is a judgment call, not a hard regression
- S4: tie — negative case stays clean, no over-triggering

Judge verdict: post-edit wins on severity (16/17 lines each; a fabrication
survives no reading, the S3 miss survives a lenient one). Edit holds —
committed. Watch S3-style unnamed population claims in future runs; if it
recurs, add a scenario line for it.

## 2026-07-19 — regression: humanizer harvest (pre-edit e436984 vs post-edit)

Edit under test: banned patterns restructured — full tell catalog moved to
references/ai-tells.md (harvested from blader/humanizer: -ing analysis
chains, copula avoidance, AI vocabulary, aphorism formulas, structure tells,
cluster-over-isolation and preserve-human-signals meta-rules), SKILL.md
slimmed to six core rules + pointer. S3 scenario extended to seed the new
tells ("serves as a testament", "streamlining…transforming…" chain, "let's
delve") and its sourcing line hardened against laundering (codifies last
run's watch item). Arms: pre-edit vs post-edit, all four scenarios, blind
judge, mechanical dash check (zero in both arms). n=1 per cell.

- S1: tie, 6/6 both — no fabrications in either arm (the earlier fix keeps
  holding)
- S2: **post-edit**, narrowly — fully brief-bounded; pre-edit needed a
  judgment call on a performance generalization
- S3: **pre-edit**, narrowly — both arms removed every planted tell
  including the new catalog ones and neither laundered the stat; pre-edit
  retained slightly more of the original's information
- S4: tie — negative case clean, no over-triggering

Judge verdict: post-edit by the narrowest margin; honest reading is a dead
tie. Zero rubric failures either side → no regression, edit committed.
**Caveat logged:** the new catalog tells did not separate the arms at n=1 —
the pre-edit skill + base model already cleaned them in a rewrite task where
they're conspicuous. The catalog costs nothing until loaded and hardens the
audit path, but its necessity is unproven; if a future run shows baseline
passing all tells, consider slimming it (obsolescence rule).

## 2026-07-19 — regression: corpus-derived voice guide (pre-edit ef58fe7 vs post-edit)

Edit under test: voice-guide.md rewritten from the author's real notes
corpus (128 files, ~38k words) — archetype theory replaced with seven
observed mechanics (compressed verdicts, dash-thought converted at polish,
flat opinions, mixed register, operational self-honesty, structure habits,
inside-the-work on the brief's facts), corpus lines as examples. Qualifier
diagnostic and manufactured-experience guard kept. Dash policy decided:
ban stays, dashes convert at polish. Arms: pre-edit vs post-edit, four
scenarios, blind judge scoring standard rubrics (gate) + five voice-match
criteria (tiebreaker). n=1 per cell.

Round 1: post-edit won voice decisively (21.5 vs 17.5 of 25 — compressed
verdicts and no framing-announcements landed; pre-edit's essayist
constructions scored worst) but FAILED the gate: S3 laundered the stat into
"most developers' time" and S1 invented a jq-usage habit. Pre-edit took the
gate with one soft invented fact.

Fix: two voice-guide additions — "own the stat or kill it" (population
claims convert to first person or die) and "habits and preferences are
biography too". Targeted retest of S1 and S3: both clean — S3 owns the stat
in first person, S1 invents no habits and handles zero users flatly.
Verified directly against the failed rubric lines (not a fresh blind
panel — iteration recheck, noted honestly).

Verdict: edit holds after one fix round; voice win carries. New S1 rubric
line added (voice-match) so future regressions keep scoring it.

## 2026-08-29 — regression: ear layer / spoken modality (pre-edit d806940 vs post-edit)

Edit under test: new references/writing-for-the-ear.md (sentence shape,
information order, reference, numbers, redundancy inversion, homographs,
TTS punctuation, read-aloud test) plus a SKILL.md modality switch (ear
layer stacks on Layers 1–2 and wins conflicts; two named inversions:
redundancy required, precision yields to processability), description and
quality-gate lines extended. New scenario S5 (video voiceover,
underspecified probe: names the medium, no ear technique).

RED first: pre-edit skill ran S5 before drafting. It failed by ear — bare
"This is a JSON log, live" opener (bare-This + the homograph *live*),
`cargo install ttail` and `--filter` kept as typed syntax inside the
spoken text, no spoken/on-screen separation. Gap confirmed, section
drafted against it.

Regression: pre-edit vs post-edit, five scenarios, uniform harness (arms
read the skill files; references loaded only when the loaded SKILL.md
calls for them), blind judge, per-line PASS/FAIL, mechanical dash check
(zero in all ten outputs). n=1 per cell — signal, not proof.

- S1: tie — both arms fail the same voice line once (an honesty
  framing-announcement: "Full honesty:" vs "Being honest about where this
  stands:"); no fabrications either side
- S2: tie — both clean 5/5
- S3: tie — both 7/7; both owned the stat in first person, no laundering
- S4: **post-edit** — pre-edit colon-spliced a third clause past the
  two-sentence cap; post-edit answered in two real sentences. Either way:
  no over-triggering, the ear layer left the negative case alone
- S5: **post-edit, decisive** — 10/10: numbers as spoken ("fifty megabytes
  a second"), CLI moved to separated [ON SCREEN] cues, spoken form ("the
  filter flag"), redundancy applied, no homographs. Pre-edit arm put a raw
  `--filter` and the homograph "live" into the voice's mouth (same two
  failure classes as the RED run, so the gap is stable across runs)

Judge verdict: post-edit 2–0–3 by scenario, 2 vs 3 on total rubric-line
failures. The target scenario separates the arms cleanly; no regression
anywhere else. Edit committed. Obsolescence: no — the pre-edit arm failed
the ear lines twice in two independent S5 runs. **Watch item:** the S1
honesty framing-announcement ("Full honesty:" / "Being honest:") failed in
both arms; if it recurs, add it to the voice guide's banned frames.

## 2026-08-29 — regression: honesty-announcement ban (pre-edit a4169c0 vs post-edit)

Edit under test: the previous run's watch item, confirmed by the author
("honesty is part of my voice, but I edit the announcement out of
content"). Voice-guide addition under mechanic 5: never announce the
honesty — "Full honesty:", "To be honest,", "Being honest about where this
stands:" die; the disclosure itself stays and lands flat. S1 rubric's
voice line extended to name honesty-announcements explicitly.

Targeted regression: S1, S3, S5 only — the scenarios where the voice guide
loads (S2 is neutral reference, S4 is the two-sentence negative; the edit
cannot reach them). Pre-edit arm reuses the previous run's post-edit
outputs verbatim (identical skill state and harness, noted honestly rather
than re-rolled). Blind judge, per-line PASS/FAIL. n=1 per cell — signal,
not proof.

- S1: **post-edit** — the target line is fixed: "Nobody uses this yet."
  lands flat with no preamble, where pre-edit wrote "Full honesty: nobody
  uses this yet." Post-edit's one blemish: "It shipped an hour ago", a
  minor invented timestamp inside the true launch day; judge ranked it
  less severe than the verbatim banned frame
- S3: tie — both clean 7/7, stat owned in first person both sides
- S5: tie — both clean 11/11; post-edit script keeps disclosures flat
  ("Nobody uses this yet. I built it for myself") with CLI in separated
  on-screen notes

Judge verdict: post-edit 1–0–2, one rubric failure per arm with severity
favoring post-edit. Edit holds — committed. **Watch item:** micro-invented
timestamps ("an hour ago") slipping past the biography rule; if it recurs,
extend Core Rule 5 with a clock-and-calendar line.

## 2026-09-16 — regression: voice guide rebuilt from the full notes corpus (pre-edit 8545ac2 vs post-edit)

Trigger: the author was unhappy with the voice. Diagnosis from five real
outputs (two fresh skill runs, a vault note, two published blog posts): the
skill bans words and punctuation, but the surviving tell is cadence — a
sentence of evidence, a three-to-six-word verdict, a paragraph break
("The model did not change. The solver did.", "Cache with an index. Cache
with a curator. The honest names.", "It's the attractor, not the budget.").
Root cause: the 2026-07-19 voice guide read two or three notes, saw "It
was BAD" and "Jitter is unacceptable", and made "compress the verdict"
rule one; the model applied a rare note habit at full density. The guide
was also written in that cadence, so the model imitated the guide's prose
rather than the corpus. The evals could not see it: rubric lines checked
for listed tells and for the mechanics, and an LLM judge shares the
writer's taste.

Corpus: the author's Obsidian vault, all 116 English notes read in full
(~29k words) plus a skim of the Russian ones; the July guide's sample was
two or three notes. Measured on prose paragraphs: connectives ~20-23 per
1000 words (skill drafts: 10-16), "X, not Y" ~1.3/k (skill: 3-7), plain
intensifier verdicts, parentheses ~4-5/k (skill: ~0), exclamation ~2-3/k
(skill: 0). The habits the earlier guide named as the voice (compressed
verdicts, flat opinions) are real but rare; the dominant mode is sequential
explanation with ordinary glue and casual verdicts inside the sentence.

Edit under test: voice-guide.md rewritten around how the author explains
(glue, paragraph shape, parentheses, questions, exclamation, mixed
register, plain-intensifier verdicts sitting with the evidence) with a
named "cadence to avoid" section carrying seven hard limits and the skill's
own failures as negative examples; SKILL.md Layer 2 short version and
quality gate rewritten to match, Layer 2 explicitly overrides Layer 1's
compression, and a "de-slop adds nothing" line; ai-tells.md gains a Cadence
section and the how-to-ai.guide vocabulary; evals/rhythm.py added as a
mechanical meter (thresholds from the corpus numbers, no corpus text in the
repo); S1 rubric gains cadence and texture lines; new S6 (500-word opinion
post, cadence probe).

Arms: pre-edit = committed skill (8545ac2), post-edit = worktree. S1 and S6
pre-edit outputs are the fresh diagnostic runs from earlier in the same
session, identical harness. Blind judge per round, per-line PASS/FAIL,
mechanical dash check zero everywhere. n=1 per cell — signal, not proof.

Round 1 (full guide, first draft): S1 post, S2 tie, S4 tie, S6 post. Meter:
fragment endings 3→1 and 3→0, pronouncements 1→0, x_not_y 1→0 and 2→1.
INVALID for S1/S6 all the same: the guide's before/after examples were
built from the S1 and S6 pre-edit drafts, and the post-edit S6 reproduced
two "after" sentences verbatim ("neither of them is memory. They are both
caches, which I only realized...", "The annoying part is that a stale fact
looks exactly like a fresh one"); S1 and S5 reproduced "Some numbers,
then." from the guide. Answers were in the prompt. Also connectives
overshot to 57/k and 45/k against the author's ~20: a floor with no
ceiling became the next tic.

Fix 1: before/after examples replaced with ones drawn from the blog and
vault drafts (not eval scenarios), explicit "do not reuse any sentence
from this guide" rule, connective ceiling of 30/k added to guide, rubric
and gate.

Round 2 (S1, S5, S6 rerun; S2-S4 carried): meter S1 and S6
connectives 25.6/k and 27.7/k, all cadence limits pass. Judge: S1 post
(pre hits "No X. No Y." template, fails cadence/voice/texture), S2 tie,
S3 **pre** (post invented a motive: "It does nothing else on purpose,
since readable output was the only part I ever needed"), S4 tie, S5
**pre** (post landed the load-bearing point once; ear layer wants twice),
S6 post by a wide margin.

Fix 2: guide gains "glue is not a license to invent reasons" under the
biography rule, and a spoken-scripts note that the ear layer's redundancy
wins.

Round 3 (S3, S5 rerun): S3 **pre** again (post republished the 30% stat as
"I've seen the claim that... (I don't have the source)" and kept the
contrast in paraphrase); S5 **pre** (post put the homograph *live* in the
spoken text). Two losses with different surface failures and one shared
cause each: on a tightening task the guide's "keep the glue and the
explanation" made the rewrite less aggressive, and the guide had grown
from 133 to 300 lines, so S5's four-file load diluted the ear layer.

Fix 3: "On a tightening or de-slop task this guide adds nothing: cut the
tells, keep the brief's facts, connect what remains. No new reasons, no
rescued statistics, no restated contrasts" in both SKILL.md and the guide;
"I've seen the claim that" added to the own-the-stat list; guide trimmed
to 218 lines (examples cut to two per mechanic, structure-habits and old
before/afters dropped, homograph reminder in the spoken-scripts note).

Round 4 (S1, S3, S5, S6 rerun on the trimmed guide): meter S1 connectives
29.2/k, S6 25.9/k, one fragment ending each (neither a verdict), x_not_y 1
each, pronouncements/announcements 0. Judge: S1 **post** (no failed line;
one flagged opinion, "the part I trust least is the filter parser", judged
derivable from the brief), S3 **tie** (both clean on every line; pre keeps
a punchline close outside the rubric), S6 **post** decisively (pre ends on
a verbatim banned close and fails every cadence count), S5 **pre** on a
single hard-fail ruling the judge itself flagged as hinging on strictness:
"so you can actually read it" scored as a homograph gamble, where the
round-3 judge passed "I can read" as unambiguous after a modal. The
rubric's wording ("words whose pronunciation the voice must guess") sides
with the round-3 reading; the S5 line now says so explicitly. Without that
line the judge called post the stronger script (real anchor, real recap).
Not re-rolled: four rounds is enough sampling.

Verdict: edit holds. Target scenarios flip decisively and stay flipped
across four rounds (S1 3-0, S6 3-0 post, with the contaminated round 1
excluded from the count); S2/S4 never over-trigger; S3 lands at a tie
after the de-slop line; S5 is disputed on a rubric ambiguity now resolved
in the rubric. Committed. Obsolescence: no — the pre-edit arm fails the
cadence lines in every round.

**Lessons for future guide edits, all three observed this run:**
1. A rule without a rate becomes a tic. "Compress the verdict" became
   every paragraph; "use connectives" became 57/k. Give the model both a
   floor and a ceiling.
2. The model imitates the guide's prose and reuses its example sentences.
   Write the guide in plain register, never build examples from an eval
   scenario, and say "do not reuse" outright.
3. An LLM judge scoring mechanics rewards the tic. Mechanical meters
   (rhythm.py) and a real-writing comparison are the check, not another
   rubric line.

**Watch items:** the S5 modal-homograph ruling (if a future judge still
fails it, the ear layer needs the clarification too); post-edit S1 drafts
leaning on derivable-but-unstated opinions ("the part I trust least");
"X, not Y" sitting exactly at the cap of one in every post-edit piece
(the cap is being used, not avoided).

## 2026-09-16 — regression: "rather than" joins the contrast cap; closings must state the mechanism (pre-edit 8545ac2 vs post-edit)

Trigger: first real-world run of the rebuilt skill, a voice rewrite of a
published 1,600-word post. Facts, tables, images and links preserved,
meter clean, punchlines gone. Two residues by eye: the model swapped "X,
not Y" for "rather than" four times (the meter did not count it), and the
closing section kept the original's slogans joined with "and" and "so".
The author's own part-2 finding in miniature: a ban relocates the pattern.

Edit under test: "X rather than Y" counted toward the one-contrast cap in
voice-guide.md, ai-tells.md, the S6 rubric, and rhythm.py's CONTRAST
regex (the first-pass rewrite now meters at 5 contrasts, not 1); cadence
limit 7 extended: joining two slogans with "and"/"so" is the same close,
the closing section must state the mechanism.

Arms: pre-edit = 8545ac2 outputs from the earlier run (reused), post-edit
= worktree, S1 and S6 only (the scenarios the edit can reach). Blind
judge, per-line PASS/FAIL, meter on both arms, dashes zero. n=1 per cell.
Note: the first judge run stalled with no output after ten minutes and
was relaunched with a length cap; the retry's verdict is the one logged.

Meter, post-edit: S1 fragments 0, x_not_y 0, connectives 25.4/k; S6
fragments 0, x_not_y 1, connectives 24.9/k. Pre-edit unchanged (S1 3/1/
9.8, S6 3/2/9.6).

- S1: **post**, narrowly. Pre lands "That is the whole pitch." and the
  "No X, no Y" device and fails cadence, voice and texture. Post invents a
  reaction ("I was surprised it held up at that rate!") and a usage
  history ("only been run against the logs I had on hand"); judge ranked
  the verbatim punchline worse but called the fabrications top-severity.
- S6: **post**, clearly. Pre fails seven of nine lines with two banned
  examples verbatim; post fails two soft lines (a padded "Neither one is
  memory... Both are caches" contrast, a self-answered question).

Verdict: edit holds, committed. **Watch item, now seen in three rounds
(r4 "the part I trust least", r5 "I was surprised", "logs I had on
hand"):** the texture push (exclamation at surprise, verdicts with
evidence) invites invented reactions and usage history on S1. If it
recurs, add "reactions are biography too" under the brief's-facts rule
and rerun S1. Second watch item: "Neither one is memory... Both are
caches" is the model's favourite opening for S6 in every round; the
banned-example quote in the rubric may be steering it rather than
deterring it.
