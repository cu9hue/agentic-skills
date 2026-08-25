# design-decision-tree — eval results

Append-only. Newest at the bottom.

## 2026-08-25 — backfill + regression for the capped-triage path (base afad7b0)

The skill had no `evals/` directory. Scenarios were written first, then the
three arms ran against them. Arms: **A** = no skill (baseline, doubles as the
obsolescence probe), **B** = pre-edit SKILL.md (full walk only), **C** =
post-edit SKILL.md (two paths). n=1 per cell — signal, not proof. One blind
judge per scenario, teams renamed and shuffled per scenario.

Protocol note: this is a backfill, so there was no true RED phase. Arm A ran
alongside every scenario instead, which gives the same information — what the
base model does unaided — but after the fact rather than before.

Environment note: no arm could dispatch subagents. Every arm was told to
assume codebase exploration returned nothing, so the skill's "find facts
yourself" step is untested here. That is a real gap; a future scenario should
put a fact in the repo that ought to kill a candidate question.

- S1 (capped triage, demo-shaped): **C wins, 7/7 vs B 4/7 vs A 3/7.** B has no
  capped path, so it did what it knows — announced 15 decisions and asked one,
  which is the drip the cap exists to prevent. A fired roughly fifteen
  questions across eight headed sections, several with no default at all, and
  ended by opening a new question instead of closing the set. Neither A nor B
  produced a below-the-line block or an answering contract.
- S2 (explicit cap of 3): **C wins, 4/4 vs A 1/4.** A returned three good
  questions and no defaults — "the choice needs to be deliberate", "worth
  deciding now" — and silently dropped every decision it did not ask about.
- S3 (document input, full-walk regression): **tie, 4/4 both.** The new
  routing table does not hijack the document path: C still built the tree,
  presented branch counts, ordered by dependency, and treated the rewrite as
  the endpoint. Observed but not folded in: B listed all 28 nodes with IDs up
  front and cross-referenced the first decision to the specific downstream
  nodes it constrains, where C gave branch counts only. Path B's text is
  identical in both arms, so that is run variance, not the edit — but a
  full-node inventory is a real improvement and belongs in a future scenario.
- S4 (underspecified structural probe): **C wins, 5/5 vs A 1/5.** A wrote a
  flat list of nine imperative best practices with no ranking criterion, fixed
  Redis without saying so, supplied no concrete values, and closed by asking
  the user two facts discoverable from the repo and the public pricing page.
  This is the scenario that most clearly shows the skill earning its keep.
- S5 (negative: two-line CLI change): **tie, 3/3 both, and C does not
  over-trigger.** C made the change, named one flippable choice, and stopped.
  No round, no cap, no ranking, no assumed-defaults block. A was the better
  reply on substance — it caught that `run` and `status` are undefined and that
  a config-load failure prints nothing even with `--verbose` — but that is code
  quality, not skill behavior.

Judge verdict: the post-edit arm wins the three scenarios that exercise the new
path, ties the two that should be unaffected, and does not over-trigger.
Landing.

Obsolescence: no. The baseline scored 3/7, 1/4, and 1/5. Left alone it answers
a design question with unranked advice and no defaults, and drops every
decision it chose not to raise.

### Fold-ins from the losing arms, and the reruns that verified them

Three rules came out of what the losing arms did better, or out of what the
judges caught in the winner. Each changed what the capped path mandates, so S1
and S2 were rerun.

1. **Correctness of a judgment output is tier 1.** The S1 judge noted that arm
   A made an eval set a real pre-code step while C buried "you eyeball the top
   ten" below the line. Added to the ranking tiers.
2. **A default resting on unconfirmed infrastructure must say so.** The S2
   judge noted that C's default assumed a request-scoped actor id without
   flagging that the plumbing may not exist. Added to the default rules.
3. **Defaults compose.** Found by the S1 rerun judge outside the rubric: two
   defensible defaults had independently walked the project from "a tool that
   watches our Slack channel" to "a script that reads a committed JSON file",
   and no question put that combined retreat to the user. Added as a check
   before the round is sent.

Rubric lines 8, 9, and 10 were added to S1 and line 5 to S2 to cover them.

- S2 rerun after fold-ins 1–2: **5/5.** The reply now says "This assumes
  Postgres" and "I have not confirmed that list against your schema". The judge
  was asked separately whether pushing the same-transaction decision below the
  line was a mistake and ruled it correct — the Q1 default already determines
  it, so it is a consequence of a settled question, which is the frontier rule
  working as intended.
- S1 rerun after fold-ins 1–2: **9/9.**
- S1 rerun after fold-in 3: **9/10, failed line 9.** The reply now names the
  drift explicitly ("my defaults quietly turn 'a tool that watches our Slack
  channel' into 'a script that prints an HTML report'"), so line 10 passes. It
  lost line 9 on one question out of six: the ranking default assumes the
  channel carries per-customer identity and its cost line never says so. The
  rule is in the skill and fired on three other questions in the same reply, so
  this reads as application variance at n=1, not a missing directive. Not
  patched further — logged as the thing to watch in real use.

## 2026-08-25 — reframe: rank by ambiguity removed, and a wording pass (base afad7b0)

Two changes, one substantive and one editorial, driven by a single request:
make the wording read like the `grilling` skill it borrows from, and make the
capped path pick the questions that reduce ambiguity most.

**The substantive change.** "Blast radius" measured consequence and nothing
else, and consequence alone ranks wrong: a decision can matter enormously and
still have a completely predictable answer, which makes it a default nobody
wrote down rather than a question. The criterion is now **span × uncertainty**
— span being how much stays undetermined until the node is answered, counting
what it unblocks, and uncertainty being how far apart the plausible answers are
and how well you can predict which one this user takes. Both terms, always.

**The editorial change.** Step 1–6 scaffolding became verb-first headings, the
four-tier grid became a prose ladder, and every hedge came out — "almost
never" → "never", "rarely earns a slot" → "never spend a slot on", "if there is
one" cut. `grep` for hedging words in the prose returns nothing.

Arms: single-arm scoring against the persisted rubrics, since the pre-edit
baseline is already on the record above. n=1 per cell. Rubric lines grew across
rounds as new rules landed, so raw scores are not comparable between rounds —
read the failed line numbers, not the fraction.

### Round 1 — after the reframe and wording pass

- S1: **11/12**, failed the frontier line — two slots' defaults collapsed if a
  neighbouring question was answered differently.
- S2: **6/6.**
- S4: **5/7**, failed two. It ran the six questions in build order with no
  stated ranking basis, and marked its fifth question "the one I would push on"
  while leaving it fifth. It also spent a slot on the 429 header contract,
  whose answer is fully predictable from ordinary practice, justifying the slot
  on cost of reversal.
- S5 (negative): still does not fire. Sharpening the directives did not make it
  interrogate a two-line CLI change.

Four wording gaps, all in rules that were already present but too loose to
bind:

1. **Tiebreakers were being read as ranking terms.** "Expensive to reverse
   beats one you can change on Friday" licensed the 429-contract slot. Now
   gated: tiebreakers only break ties between nodes that already clear both
   terms, and irreversibility never buys a slot for a predictable answer.
2. **The frontier rule covered questions but not defaults.** A reply passed the
   rule with six independent questions, then wrote a default reading
   "classifying against the Q3 taxonomy". The rule now binds defaults too.
3. **"Defaults compose" only checked fidelity to the user's framing.** Two
   judges independently found the other failure: one reply declared "no
   persistence between runs" then cached to SQLite; another paired a
   debugging-grade audit log with a failure mode that takes down billing. The
   set now has to be one somebody would pick on purpose.
4. **The ranking was computed but never shown.** Order strictly, and open with
   one line naming what you ranked on.

### Round 2 — after those four

- S1: **13/14**, failed the frontier line again — a default naming "the
  accuracy number from Q2".
- S2: **9/9.**
- S4: **9/9.** The 429 contract moved below the line on its own, annotated
  "this is the question people ask first and it matters least, since it sits
  behind an interface you can swap".

Both judges landed on the same residue: defaults leaning on a neighbouring
slot, and one default that branched. "Every default stands on its own" was too
terse to bind, so it was made concrete — never reference another question by
number, name the assumption inside the default instead, and a default that
branches is not a default (pick one side, put the condition in the cost line).

### Round 3 — final

- S1: **15/15.**
- S4: **10/10.**
- S2: **9/9**, scored on the round-2 output. Its round-3 run was not
  re-scored; the last patch targets a failure S2 was already passing.

Protocol error, corrected: the first S2 judge in round 2 was pointed at the
round-1 file and returned 6/9, failing two lines whose rules did not exist when
that text was generated. Rescored against the right file: 9/9. The 6/9 is not
evidence about the skill.

Known residue, not patched: at n=1 the model still occasionally couples its top
two nodes — S4's final reply put "what is the limiter for" and "where do the
counters live" in slots 1 and 2 when the first answer changes the store. The
frontier rule covers this and fired everywhere else in the same reply. Logged
as the thing to watch in real use rather than met with more text.

Obsolescence: unchanged, no. Nothing in this round re-ran the no-skill arm; the
baseline scores above stand.
