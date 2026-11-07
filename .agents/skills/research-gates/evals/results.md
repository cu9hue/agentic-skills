# research-gates — eval results

Append-only. Newest at the bottom.

## 2026-11-07 — RED baseline, no skill loaded (pre-commit, repo HEAD 7e7e488)

Arms: A = no skill. n=1 per cell — signal, not proof. Subagents on Opus 5.5,
told to use no skills, read no files and search nothing. Scored by the author
against the rubrics before drafting; the blind judge scores A against B in
the GREEN round below.

The base model is strong here. It already knows Deflated Sharpe, fill-model
bounds, markouts and "don't move the line after the data". The skill's job
is the residue it does not apply unprompted. **Rubric lines failed or
partial: 10 of 25.** Failures, which are the skill's job description:

**S1 — overfit backtest, capital ask** (1 pass, 2 partial, 2 fail)

- partial: computes the expected best-of-200 Sharpe from noise and names
  Deflated Sharpe, but sets no bar ("search DSR"); no PBO
- partial: writes kill criteria "now" only as live stop-losses; never says
  the sweep result is exploratory and a confirmatory test needs criteria
  fixed first
- fail: no permutation test, and no rerun of the optimization on shuffled
  data
- fail: no sizing rule; suggests an arbitrary "$2k" live run, no fractional
  Kelly, drawdown budget or stop rule

Passed: demands untouched data, walk-forward, and costs before money.

**S2 — passive backtest without own fills** (3 pass, 1 partial, 1 fail)

- partial: capacity framed only as own market impact ("keep size small");
  no estimate of depth at the touch or of competitors sharing it, and no
  claim that capacity can bind before the signal
- fail: no placebo separating which fills happen from how many

Passed: touch / queue / trade-through fill models as bounds ("if it only
makes money under touch, it doesn't make money"), adverse selection,
markouts at 1s–5min.

**S3 — kill criterion edit, non-trading** (4 pass, 1 partial)

- partial: no explicit lesson or post-mortem on what the 50 demos showed

Passed: refuses the recount, offers a second test with the line written
first, demands fresh evidence (real payment), humane tone.

**S4 — structural probe** (2 pass, 3 partial)

- partial: kill criteria before data and a go/no-go time box are present,
  but as items 2 and 7 of a nine-item list, not as stage gates
- partial: no sizing stage before capital beyond "go small"; no live check
  that P&L comes from the stated reason (factor regression is close)
- partial: no periodic review that forces keep or kill on every open idea

Passed: "who is on the other side, and why do they keep losing" asked
early; counts variants and names Deflated Sharpe.

**S5 — negative, definition** (2 pass)

Clean: formula, inputs, the 0.95 reading, two common input mistakes.

Obsolescence: NO — the no-skill arm missed 10 rubric lines, concentrated in
re-optimizing permutation tests, sizing, placebos, capacity and gate
structure. Expect a narrow margin on S2, S3 and S5.

## 2026-11-07 — GREEN round 1: initial A/B (pre-commit)

Arms: A = no skill (the RED outputs), B = SKILL.md + `references/quant.md`.
n=1 per cell — signal, not proof. All arms on Opus 5.5. One blind judge
subagent; arms anonymized into teams X/Y, order shuffled per scenario
(seeded), mapping kept outside the judge's packet.

Skill arm 21 pass / 1 partial / 0 fail; baseline 9 / 9 / 4.

- S1: **B** 5/5 vs A 1 pass, 3 partial, 1 fail — B rejects the sweep as
  exploratory, proposes pre-registered criteria with DSR ≥ 0.95, a
  permutation rerun of the full 200-combination sweep, and a sizing step
  (three worst in a row, ¼–½ Kelly, stop rule); A handed DSR off ("search
  it") and suggested an unsized "$2k" live run
- S2: **B** 5/5 vs A 2 pass, 2 partial, 1 fail — B pre-registers the decision
  fill model, warns the sign can flip, adds the random-fill placebo and a
  capacity cap; A had no placebo and treated capacity as a data limit
- S3: **B** 4 pass, 1 partial vs A 3 pass, 1 partial, 1 fail — B demands 50
  new people and writes the post-mortem; A's second test reused the 10
  people picked by the result. A had the better tone; B's gate jargon read
  as lecturing (partial)
- S4: **B** 5/5 vs A 2 pass, 2 partial, 1 fail — gates are the spine in B;
  A listed the same ideas as nine scattered bullets
- S5: **B** 2/2 vs A 1 pass, 1 partial — both free of ceremony (no
  over-trigger); A's first sentence misstated DSR as a test against zero

Judge verdict: skill arm wins all five on substance. The judge flagged one
pattern in every winning skill answer: framework vocabulary the user never
introduced ("Gate 3", "entry conditions", "idea card in `Notes/`") and a
prediction-market illustration presented in a market-agnostic question.
Obsolescence: no — baseline failed 4 lines and was partial on 9, and the
structural probe (S4) shows a clear delta.

Fix applied after this round: SKILL.md "Answer shape" now says to speak in
plain words unless the user already uses the gate names, to drop "entry
condition" and rule slogans with users, and to offer an idea card only where
cards live; `quant.md` illustrations now name their setting.

## 2026-11-07 — GREEN round 2: regression for the plain-language edit (pre-commit)

Edit under test: the "Answer shape" plain-language rule, the idea-card
condition and the named settings for illustrations (listed under round 1).
Arms: B = pre-edit skill (round 1 outputs), C = post-edit skill. S1–S4 only;
S5's triage text did not change. n=1 per cell — signal, not proof. Fresh
blind judge, teams shuffled per scenario (seeded), told to penalize
framework jargon, slogans, assumed files and transplanted market examples.

- S1: **C** — both pass all five lines; B wrapped them in "Gate 3", "entry
  conditions" and a `Notes/` card offer, C said the same in plain words and
  added a PBO procedure and the live-sample standard error
- S2: **C** — C passes capacity outright (competitors at the touch, binds
  before the signal) and flags the prediction-market numbers as another
  setting; B repeated gate labels and presented them as "the spread you can
  expect"
- S3: **C**, narrow — both pass every substantive line; B lost the tone line
  on gate framing and the "overfitting with extra steps" quip
- S4: **C**, near tie — both pass all five lines; B asserted a vault
  template file as fact

Judge verdict: post-edit wins 4/4 with no rubric regression and less
ceremony in every scenario. Edit holds.

Judge-found errors, fixed in `quant.md` after this round, without a rerun
(wording fixes; no mandate changed):
- C-S2 inverted the random-fill placebo ("no worse than random" means which
  fills is the problem). The reference line was ambiguous; it now says that
  real fills doing worse than random fills at the same rate means adverse
  selection.
- C-S2 advised "inner joins only" for trades against snapshots, which drops
  most trades. The reference now says to match each trade to the quote in
  force (as-of join with a staleness limit), and to keep only times when
  both sources were live when pairing venues.
- C-S4 attributed the factor-of-two Kelly result to Breiman. The reference
  now says Breiman states the critical fraction, crediting Dubins & Savage,
  and the factor of two is a small-edge approximation.

Open for real use: competitors sharing depth surfaced only after the edit,
so treat capacity as a weak spot. The arms ran with the vault as working
directory, which may explain the idea-card offers; a run from a neutral
directory has not been done.
