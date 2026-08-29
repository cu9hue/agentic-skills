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
