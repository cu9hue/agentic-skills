# grill-with-docs — eval results

Append-only. Newest at the bottom. History of the capped round, from the
former design-decision-tree skill, is in `design-decision-tree-results.md`.

## 2026-11-27 — regression: capped round folded in from design-decision-tree (base d47b75c)

Edit under test: grill-with-docs gains a mode table. Task text or a named
cap gets design-decision-tree's capped round (ranked by span times
uncertainty, concrete defaults with costs, below-the-line block, answering
contract); a plan or spec gets Matt's full grilling; both write the
glossary and ADRs. design-decision-tree is deleted. With the edit the
skill's instructions differ from upstream, so the third-party exemption
ends and these evals start. Arms: pre = grill-with-docs as copied from
mattpocock/skills, post = this edit. All five scenarios, one blind judge,
labels shuffled per scenario. n=1 per cell.

Round 1:
- S1 capped round: **post** (8/1/0 vs 4/1/4). Pre had no "how will you
  know the list is right" slot, no below-the-line block, no answering
  contract and no ranking line.
- S2 cap of 3: **post** (3/0/0 vs 1/1/1). Pre dropped the cut candidates
  and never asked where the log lives or whether it shares the write's
  transaction.
- S3 spec: tie (5/0/0 each). Full grilling held in both: one numbered
  frontier round, fuzzy terms challenged, GLOSSARY.md offered.
- S4 probe: **post** (4/0/0 vs 2/1/1). Pre ordered by dependency, never
  asked enforce vs observe, and left store-down without a default.
- S5 trivial change: both fail (post asked 3 questions, pre asked 6).

Fix: a third mode row, "No grilling", for a small change with one obvious
reading: say so, state one assumption, offer to make the change; judged by
what an implementer would have to guess, not by the phrasing.

Round 2 (post only, scored against the rubric by the orchestrator, not
blind, since each was a single arm):
- S5: pass both lines. "Too small for a round of questions", one stated
  assumption (stderr, both commands), an offer to make the change.
- S4 recheck: still a ranked capped round of 5 with a below-the-line block
  and the answering contract, so the new row did not swallow a short ask
  that needs grilling.

Verdict: post wins S1, S2 and S4, ties S3, and passes S5 after the fix.
Edit holds. Obsolescence: not measured (no no-skill arm this run); the
design-decision-tree history shows the no-skill baseline failing the
capped scenarios.
