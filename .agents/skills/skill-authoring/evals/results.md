# skill-authoring — eval results

Append-only. Newest at the bottom.

## 2026-07-18 — initial A/B (pre-commit)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof. Scenarios
judged as ordered plans, not executions.

- S1: **B**, 5/6 rubric lines vs 1/6 — baseline drafted then tested, kept
  evals in scratchpad, had no negative scenario and no stop-if-baseline-
  passes condition
- S2: **B**, 4/4 vs 1/4 — baseline invented a throwaway test instead of
  backfilling ankify/evals/, produced no results log, ran no obsolescence
  probe
- S3: **tie** — both arms made a surgical README edit with no ceremony; the
  skill arm correctly cited the cosmetic exemption (no over-triggering)

Judge verdict: skill arm decisive on both positive scenarios, clean on the
negative. Obsolescence: no — baseline failed most of S1/S2.

## 2026-07-19 — regression: line-norm edit (pre-edit ef58fe7 vs post-edit)

Edit under test: authoring rule "repo norm is ~100 lines" replaced with
"200–500 is the healthy range for a substantive skill (per Schmid); size to
the directives that bind; never pad toward the range". Arms: pre-edit vs
post-edit skill, all three scenarios as ordered plans, blind judge. n=1 per
cell — signal, not proof.

- S1: **post-edit**, by a hair — both fully process-compliant; judge flagged
  pre-edit's "~100 lines" target as a padding attractor while post-edit's
  "sized to what binds" read coherently
- S2: **post-edit**, narrowly — on an incidental mechanic (post-edit arm
  preserved pre-edit text via git show; pre-edit arm's plan couldn't run as
  written), unrelated to the norm change
- S3: tie — cosmetic exemption held in both arms, no ceremony

Judge verdict: post-edit wins narrowly, zero rubric-level regressions in
either direction. Edit holds — committed. Note: the sizing rubric line was
added to S1 for this run.

## 2026-07-19 — regression: structural-probe mandate (pre-edit 7f30aec vs post-edit)

Edit under test: scenario sets must include an underspecified structural
probe (vague no-axis ask testing attention allocation); retirement verdicts
must cite the probe's result; eval-template gains the probe skeleton; S1
rubric line added. Motivated by the frontend-a11y retirement reversal: its
21/21 baseline pass measured component-writing while the skill's value was
attention allocation, detectable only by a vague probe. Arms: pre-edit vs
post-edit, all three scenarios as ordered plans, blind judge. n=1 per cell.

- S1: **post-edit** — authors a structural-probe scenario and checks it in
  the quality gate; pre-edit's scenario set is all axis-named execution
  cases
- S2: **post-edit** — backfill includes the probe and the obsolescence read
  explicitly cites it; pre-edit's obsolescence flag "cannot cite a probe
  that was never authored" (judge)
- S3: tie — cosmetic exemption held in both arms, no ceremony

Judge verdict: post-edit wins, pre-edit fails three rubric lines (all the
new mandate), zero regressions elsewhere. Edit holds — committed.

## 2026-11-27 — regression: plain directives, harness enforcement, model-change trigger, plugin-eval runner (uncommitted, base 9a4eea4)

Edit under test: directives stated once with no emphasis markers (and the
skill's own "NOT"/"BEFORE" caps removed); only what the RED baseline shows
the model gets wrong goes in a skill; rules that cannot be taken back go in
a hook or deny rule (hooks exit 2); a new default model triggers no-skill
reruns; `claude plugin eval` named as the offline runner; the
`superpowers:writing-skills` pointer removed. S4 (model change) and S5
(irreversible rule) added. Arms: pre-edit vs post-edit, all five scenarios
as ordered plans, blind judge, labels shuffled per scenario. n=1 per cell.

- S1: **pre**, narrowly (6/1/0 vs 5/2/0): the post arm sized the skill to
  its directives but never named the 500-line cap. Both missed
  `references/`. Unrelated to the edit.
- S2: tie (3/1/0 each). Both reran ankify's existing evals; the rubric's
  backfill path no longer applied, so S2 now targets landing-copy.
- S3: tie: cosmetic exemption held in both arms.
- S4: tie on rubric (4/0/0 each); judge leaned post for spotting a skill
  with no structural probe. The pre arm already reran no-skill arms on a
  model change, so the new trigger paragraph shows no measured delta.
- S5: **post** (4/0/0 vs 2/2/0): post built the hook and deny rules first,
  named the hook in the skill and planned plain wording; pre planned no
  skill wording and never linked its skill to the hook.

Judge verdict: post-edit 17/3/0 vs pre-edit 16/4/0. The edit wins on its
main target (S5), ties S2–S4 and loses S1 by one partial on a line it did
not touch. Edit holds. Open: by the skill's own no-op rule, the
model-change paragraph is unproven (S4 showed no delta).

## 2026-11-27 — regression: third-party exemption (uncommitted, base 9a4eea4)

Edit under test: credited third-party copies (upstream repo and commit in
`origin:`, license file in the folder) are exempt from the eval mandate;
folding in called skills, moving material to `references/` or changing
invocation keeps the exemption; changing what it tells the agent to do
ends it. S6 added. Arms: pre-edit (the version logged above) vs post-edit,
S6 only, since the edit changes no other scenario's path. Blind judge.
n=1.

- S6: **post** (3/0/0 vs 1/2/0). Both credited source and license. The pre
  arm wrote no evals by default but laid out an optional full A/B for an
  unchanged copy, and only implied the boundary by quoting the README. The
  post arm refused evals for the copy and stated when the mandate returns.

Caveat: the README's new third-party section already described the
exemption, and the pre arm read it, so the pre arm was not a clean
no-exemption baseline. Edit holds.
