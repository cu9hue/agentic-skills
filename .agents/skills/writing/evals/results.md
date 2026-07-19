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
