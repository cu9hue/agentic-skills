# concepts-ledger — eval results

Append-only. Newest at the bottom.

## 2026-10-22 — initial A/B (base deb0633)

Arms: A = no skill, B = SKILL.md. n=1 per cell — signal, not proof. One blind
judge per scenario; teams shuffled per scenario so neither arm kept a fixed
name. RED ran before the skill was drafted, and the drafting worked from the
recorded baseline failures.

Platform note: both arms ran on Claude Code. Every arm was told to invoke no
skill of its own, so A is a true baseline. Subagents could not write files, so
each returned the file contents inline.

RED summary: the baseline picks the right concepts and already proposes a
ledger unprompted. It fails on the file itself — order, extra sections,
narrative, length — and on stating the threshold and the review loop.

- S1 (set up the ledger): **B wins, 7/7 vs 4/7.** A chose the same five
  concepts and the same exclusions, then put the excluded names in a
  "not concepts" table inside the file, added a how-to-read block, a flow
  overview, and an open-questions section, and ordered the entries by flow
  instead of name. ~108 lines against a ~40-line ceiling. B wrote 34 lines,
  flat and alphabetical, and put its observations in the reply.
- S2 (update from a branch diff): **tie, 7/7 vs 7/7.** The two ledgers are
  identical except that A's Indexer line also names `rebuild()`. Both
  renamed DocumentStore to Repository without keeping both, dropped
  Fingerprint from the depends-on line, left out IndexStats and retry, and
  kept Pipeline and Stage byte-for-byte. The baseline already does this well.
- S3 (underspecified structural probe): **B wins, 4/4 vs 1/4** on the rerun.
  A answered with a hand-off checklist (tests for invariants, one feature per
  PR, decide what stays thin) with the ledger as one bullet, no entry
  threshold, and review of the PR description rather than the ledger diff.
  A was the only arm on the first run to state the brake ("extend an
  existing concept before adding one"); the first B run scored 3/4 and
  missed exactly that line. Folded a brake paragraph into the skill and reran
  S3: B then passed all four. One fixture fix: the rubric for S2 originally
  demanded Document unchanged, but the branch renames Document's file, so
  its path line must move; the rubric now says so.
- S4 (negative: docstring request): **tie, 2/2 vs 2/2.** Both wrote the
  docstring and stopped. Neither proposed a ledger. No over-trigger.

Judge verdict: the skill arm wins S1 and S3 and ties S2 and S4. Landing.
Obsolescence: no. The baseline failed three of seven lines on S1 and three of
four on the structural probe. S2 shows the baseline already does the update
step well; the skill earns its keep on the shape of the file and on putting
the threshold, the diff-review loop, and the brake on the agenda unprompted.
