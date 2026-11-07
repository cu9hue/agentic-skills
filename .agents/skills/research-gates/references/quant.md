# Quantitative trading: what each gate checks

Read this for any trading idea, at any gate. It does not assume a market,
venue or asset class. Numbers from specific studies appear as cited
illustrations of how large an effect can be. They are not rules. When you
pass one to a user, name the setting it came from (for example "resting bids
in a prediction market") and use it only to show size; never present it as
if it described the user's market. Every
threshold below is a default the user can change at Thesis, before evidence.
After Thesis, a threshold is a kill criterion and does not move.

## Default thresholds (user-tunable)

| Check | Default | Note |
| --- | --- | --- |
| Test: net Sharpe, out of sample | kill below 1.0 on personal capital, below 0.7 at client scale | Heuristic from the original framework, not a truth. Set your own at Thesis. |
| Robustness: Deflated Sharpe | pass at 0.95 or higher | A probability. 0.5 is a coin flip against the selection-adjusted benchmark, so it is not a pass mark. |
| Robustness: probability of backtest overfitting | no default from the sources; fix one at Thesis | A value near 0.5 means picking the best in-sample variant does no better than chance out of sample. |
| Robustness: t-statistic for a new signal | above 3 | Rough hurdle for a field that has tried many signals (Harvey, Liu & Zhu 2016). |
| Robustness: permutation p-value | at or below 0.05, with m large enough that p can reach it | With m shuffles the smallest possible p is 1/(m+1). |
| Sizing: Kelly fraction | one quarter to one half of full Kelly | Shrink further when the edge comes from a model rather than from a price. |
| Sizing: three losses in a row | the three worst outcomes in a row stay inside the loss budget | If not, size down until they do. |

## 1. Thesis: who loses money to this trade, and why will they keep doing it?

- Name the counterparty and the reason they pay: they demand immediacy,
  they buy insurance, a mandate or rule forces them, a bias moves them, or
  they learn the information later than you. "The market is inefficient"
  names nobody. Kill.
- Say how long until they stop: competition, a rule change, learning. An
  edge with no reason to persist is a sample artifact until shown otherwise.
- Name the edge type: risk premium, information, liquidity provision, or a
  structural constraint. Each type fails in its own way at Live, and the
  attribution there must look for that failure.
- **Plan the attempt budget from theory, not from compute.** Bailey &
  López de Prado (2014) say trials should be planned from "investment
  theory, not computational power". Illustration: to keep the best of N
  skill-less variants from showing an annualized Sharpe of 1, five years of
  data allow about 45 independent variants and two years about 7 (Bailey,
  Borwein, López de Prado & Zhu 2014, minimum backtest length). k binary
  parameters give 2^k variants.
- **Sketch capacity now** for liquidity-providing or small-market
  strategies: depth at the touch times turnover, divided by the number of
  competitors who share it. If the profit at the capacity you can reach is
  not worth the time, kill before Evidence.
- Write the kill criteria (SKILL.md lists the fields). For a trade, include
  the cost model, the fill model if the strategy rests orders, the
  out-of-sample period, the attempt budget, the robustness tests that must
  pass, and the loss that would stop it live.

## 2. Evidence: does the data exist at the frequency needed?

- Match the data to the mechanism. A strategy that depends on queue position
  needs order-book events, not one-minute bars. A strategy that rests orders
  needs either its own fills or the inputs a fill model needs (trades and
  the book on the same clock).
- **Write the data quality log** (template below). Gate 2 cannot close
  without it.
- Check the conventions that silently change results: whether a bar is
  stamped at its open or its close, exchange time against receipt time, the
  timezone, funding and settlement times, the fee schedule in force on each
  date, tick-size changes, contract rolls, delistings and renames.
- Illustration of silent traps: in one study a resolution field held
  terminal prices such as 0.9995 instead of 0/1 flags, and requiring exact
  flags shrank the panel 284 times; a legacy fee field gave a 25-times fee
  error (Moulinier 2026).
- Price at the executable side, never at the mid. Do not forward-fill a
  quote across a period when its source was silent. Match each trade to the
  quote in force at its time (an as-of join with a staleness limit). When
  you pair two venues or sources, keep only the times when both were live.
- **Capacity check.** Measure depth available at the touch, how often it
  refreshes, and how many other participants quote there. For a
  liquidity-providing or small-market strategy, capacity can bind before the
  signal does. Record the capacity estimate; Sizing uses it as a cap.

## 3. Test: does an out-of-sample test, net of every cost, pass the kill criteria?

### Exploratory against confirmatory

- Work done before the kill criteria were fixed is exploratory. A parameter
  sweep on the full sample is exploratory. It cannot pass this gate.
- **Pre-register the confirmatory run.** Before it, write a dated document
  that fixes the universe, signal, execution model, cost model, fill model,
  parameter grid and kill criteria. Freeze the configuration and record its
  hash. A deviation needs a new dated document, not an edit (Moulinier 2026,
  which records a SHA-256 and rechecks it before and after every run).
- Touch the holdout once. A holdout reused many times is a search on the
  holdout: applied 20 times at 95% confidence, it is expected to pass one
  false strategy (Bailey & López de Prado 2014).
- An internal split of data you already had is the weakest form of
  out-of-sample test. Label it as such wherever it stands in for fresh data
  (Moulinier 2026). Data that arrives after the pre-registration is the
  strongest.

### Costs

Include fees at the schedule in force, the spread paid at the executable
side, slippage, funding or borrow, latency, and outages (venue downtime,
missed windows, failed orders). Rerun with costs doubled: an edge that
dies at twice the cost estimate is fragile.

### Fill model first, for passive strategies

- For resting orders, fix the fill model before the first backtest run. The
  fill model can set the sign of the result. Illustration: the same resting
  bids on prediction-market favourites gave +1.39¢, −3.89¢ and −7.08¢ gross
  per contract under three fill models ordered by adversity (Moulinier
  2026).
- Report at least three fill models: a lenient one (fill on touch), a
  middle one (fill after the visible queue ahead is consumed), and a strict
  one (fill only on a trade through the price). Pre-register which one is
  the decision model; the others are bounds. A strategy that makes money
  only under the lenient model does not make money.
- Know each model's bias. A touch model counts fills you would not get. A
  model that counts a fill only when the price moves against you misses the
  benign fills. Only real fills settle the question.
- **Fills arrive when they are losing.** A resting order fills when the
  other side wants to trade into it, often because that side knows more.
  This is adverse selection. Illustration: on prediction-market favourites a
  week or more from resolution, the favourite won 95.5% of the time
  unconditionally but 86.9% when the offer fell to a resting bid (Moulinier
  2026).
- **Measure markouts at several horizons:** the price at t + Δ minus the
  fill price, for horizons from seconds out to the holding period or exit.
  The adverse-selection clock can run in days, not milliseconds, on
  long-dated instruments (Moulinier 2026). Edge = spread captured minus
  markout loss.

### Trial log

Record every configuration tried for the idea: parameters, data range,
metric, date, and whether it was exploratory or confirmatory. Include the
informal runs that never got written up. The number of trials is "the most
important piece of information missing from virtually all backtests"
(Bailey & López de Prado 2014). Deflated Sharpe needs the count and the
variance of the Sharpes across trials. The probability of backtest
overfitting needs the full matrix of returns per trial.

### Sample size

The variance of an annualized Sharpe estimate is about (1 + SR²/(2q))/y over
y years with q returns a year. When the true Sharpe is zero, sampling more
often within a year does not shrink it; only more years do (Bailey, Borwein,
López de Prado & Zhu 2014). Three years of hourly bars are three years, not
26,000 observations of independent evidence.

## 4. Robustness: does it survive other samples and placebos?

### Selection adjustment

- **Deflated Sharpe as a probability.** DSR is the probability that the true
  Sharpe exceeds the best Sharpe expected from N skill-less trials, given
  the sample length, skewness and kurtosis. Compare it with a high bar such
  as 0.95. A DSR of 0.5 is a coin flip against the selection-adjusted
  benchmark; the original framework's "kill below 0.5" sets the bar too low.
  Inputs: the number of independent trials (for M correlated trials with
  average correlation ρ, about ρ + (1 − ρ)M), the variance of Sharpes across
  trials, T, skewness, kurtosis. Illustration: an annualized Sharpe of 2.5
  on five years of daily data, picked from 100 trials with skewness −3 and
  kurtosis 10, gives DSR ≈ 0.90 and fails at 0.95 (Bailey & López de Prado
  2014).
- **Probability of backtest overfitting (PBO)**, by combinatorially
  symmetric cross-validation, when many configurations were tried. Split the
  T × N matrix of trial returns into S equal time blocks. For every way of
  choosing S/2 blocks as in-sample, find the best in-sample trial and its
  rank out of sample on the other blocks. PBO is the share of splits where
  that trial ranks below the out-of-sample median (Bailey, Borwein, López de
  Prado & Zhu 2017). It needs no normality, but it needs the full trial log.
- **Multiple testing.** Use t > 3 as a rough hurdle for a new signal
  (Harvey, Liu & Zhu 2016). For a family of k tests, Bonferroni tests each
  at α/k; Holm's stepdown keeps the same familywise level with more power.
  Romano & Wolf's stepdown compares the best candidate with the maxima from
  resampled or shuffled data, removes it if rejected, and repeats.
  Regression-based corrections fit strategies that are a regression;
  thresholds, sizing and stops can be overfit outside any regression
  (Bailey, Borwein, López de Prado & Zhu 2014). The permutation form below
  works for any criterion, but its sources give no proof of power.

### Permutation tests

- **Two families.** A decision shuffle permutes the strategy's decisions
  against the returns: cheap, and needs neither the strategy nor its
  optimizer. It is valid when at least one series in each pair is serially
  uncorrelated; positions on rolling windows are not. A data shuffle
  permutes the market data, keeping its drift and distribution, and reruns
  the whole strategy.
- **Three p-values** (HangukQuant notes, ch 11, after Masters):
  - timer's p-value: shuffle the returns across time with the weights
    fixed; tests timing
  - picker's p-value: shuffle which asset each return belongs to with the
    time order fixed; tests selection
  - trader's p-value: shuffle the market data and rerun the strategy; tests
    both, relative to market drift
- **p = (k + 1)/(m + 1)**, for k of m shuffled runs that score at least as
  well as the real one.
- **Detect in-sample overfitting:** rerun the full optimization on each
  shuffled dataset. If the optimizer finds results as good on data that
  cannot be predicted, the real in-sample result is mostly fit to noise.
  This needs a repeatable optimizer, which the trial log makes possible.
- **Shuffle only the pattern under test.** Apply one shuffle index to all
  instruments to keep their correlations. Permute within periods when the
  same instruments were alive. Permute intraday bars day by day. In a
  walk-forward test, shuffle the first training fold separately so training
  data never moves into the test period.
- **Passive strategies:** shuffling positions breaks the fill mechanism.
  Shuffle which markets or times fill, at the observed fill rate, instead.
- **Instruments that converge to a terminal value** (binaries, bonds near
  maturity, expiring options) do not have returns exchangeable through time.
  Shuffle across instruments at matched time to expiry.

### Bootstrap

The bootstrap tests whether a return series differs from zero, not whether
the decisions carry skill. It does poorly on ratio statistics such as the
Sharpe ratio and the profit factor, where a permutation test stays accurate
(HangukQuant notes, ch 11). Resampling single observations destroys serial
dependence, so drawdown and other order-based statistics are invalid under
it. Use a block bootstrap (blocks of about a month of daily data, for
example) when order matters.

### Placebos that report their own teeth

A placebo breaks the claimed mechanism and keeps everything else. Report how
many rows it moved and whether the permuted variable's distribution drifted.
Illustration: a label shuffle that changed 9.2% of labels cannot carry a
verdict; a shuffle that moved 50.3% of rows at zero drift can (Moulinier
2026). Useful placebos:

- random fills at the observed fill rate: if real fills do worse than random
  fills at the same rate, the loss comes from which fills arrive (adverse
  selection), not from how many (win given fill 0.806 real against 0.943
  shuffled on prediction-market favourites, Moulinier 2026)
- a lag sweep for any edge between two sources: shift one source against
  the other. If the edge is not largest at zero lag, the edge is timing, not
  price (Moulinier 2026)
- random entry times, flipped signals, fake sample boundaries

### Other samples

- Walk-forward results, stitched from test windows only.
- Regime split: the gate must pass in each part, not on the pooled sample.
  Illustration: read through 52 cells, five passed in one half and none in
  both (Moulinier 2026).
- Instruments the strategy never saw.
- Parameter neighbourhood: a plateau of good values, not a lone spike.
- Exposure check: regress returns on the obvious exposures (market, momentum,
  carry, volatility). The edge must survive them.

## 5. Sizing: can I survive being wrong three times in a row?

- **Fractional Kelly under parameter uncertainty.** Kelly assumes the edge
  estimate is true. At full Kelly, an edge overestimated by a factor of two
  leaves zero growth, and more than that leads to ruin. Breiman (1961)
  states the critical fraction, crediting Dubins & Savage; the factor of
  two is the small-edge approximation. Overestimating costs ruin;
  underestimating only slows growth. Shrink the edge estimate before you
  size: Kelly on an edge shrunk by k is k times full Kelly. Shrink more when
  the edge comes from a model than when it comes from an observed price.
- **Three losses in a row:** take the three worst outcomes at the proposed
  size, in a row. If they break the loss budget, size down until they do
  not.
- **Venue and instrument caps:** a maximum exposure per venue or
  counterparty (failure, withdrawal halts) and per instrument. Size at or
  below the capacity estimate from Evidence.
- **Drawdown budget:** the loss at which the idea stops, set now.
- **Stop rule:** the drawdown limit, a slippage or fill-rate gap against the
  backtest, a thesis break, and a time stop. Fix the live sample size and
  threshold now, so Live neither kills on noise nor keeps a loser.
- Write down what you expect attribution to show at Live, and what you will
  do if it shows something else.

## 6. Live: does P&L attribution match the thesis?

- **Attribute the P&L:** thesis edge, market drift or beta, volatility
  exposure, funding or carry, fees and rebates, luck. A strategy sold as
  spread capture whose P&L is inventory drift fails this gate, even in
  profit.
- Compare live with backtest: fill rate, markouts, slippage, costs. The gap
  is the most honest number the idea has.
- Grade the process before you look at the P&L.
- If attribution does not match the thesis, write the post-mortem.

## Templates

### Research note

Use for any idea at Test or later.

```markdown
# [Title]
Bottom line: [one sentence: the finding and the number]
Idea: [link]  Gate: [name]  Date: [ ]

## Thesis
Who loses money to this trade, why, and how long until they stop.

## Data
Source, venue, period, frequency, timestamp convention, known gaps.
Data quality log: [link]

## Method
The test in plain words, then the maths. Parameters and why.
Pre-registration: [link, date, config hash]  Trials logged: [N]

## Result
Headline table, net of fees, funding, slippage. Fill models if passive.

## Robustness
Deflated Sharpe, PBO, permutation p-values, placebos with their teeth,
walk-forward, regime split, parameter neighbourhood.

## What would change my mind
The observation that kills it from here.

## Decision
Keep, kill or reframe. Next action with a date.
```

### Data quality log

One per dataset. Evidence cannot close without it.

```markdown
# [dataset name]
Source and endpoint:
Period covered:            Frequency:
Timestamp convention:      Timezone:
Venue specifics: funding times, settlement, fee schedule by date, tick size,
contract specs
Known gaps and outages (dates):
Survivorship: delistings, renames, rolls, migrations handled how
Checks run: duplicates, monotonic time, outliers, cross-source sanity
Signed off by:             Date:
```

### Post-mortem

```markdown
# [Idea or trade]
What the thesis said:
What happened (numbers):
Attribution: thesis / beta / volatility / funding / fees / luck
What killed it:
Which gate let the error through, or should have caught it:
Decision quality (process only): good / acceptable / bad, and why
Lesson in one sentence:
```

## Sources

- Bailey, D. H., & López de Prado, M. (2014). The deflated Sharpe ratio:
  Correcting for selection bias, backtest overfitting and non-normality.
  *Journal of Portfolio Management*, 40(5).
- Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2014).
  Pseudo-mathematics and financial charlatanism: The effects of backtest
  overfitting on out-of-sample performance. *Notices of the AMS*, 61(5).
- Bailey, D. H., Borwein, J. M., López de Prado, M., & Zhu, Q. J. (2017). The
  probability of backtest overfitting. *Journal of Computational Finance*,
  20(4).
- Harvey, C. R., Liu, Y., & Zhu, H. (2016). … and the cross-section of
  expected returns. *Review of Financial Studies*, 29(1).
- Moulinier, G. (2026). Mistiming is not arbitrage: A pre-registered
  falsification of cross-platform prediction-market arbitrage, and the
  two-sided cancellation of the favourite–longshot premium. SSRN 7170178.
- HangukQuant, *Quantitative and Qualitative Treatments to Capital Markets*
  (lecture notes), ch 11, on permutation tests and the bootstrap, after
  Timothy Masters.
- Breiman, L. (1961). Optimal gambling systems for favorable games.
  *Proceedings of the Fourth Berkeley Symposium on Mathematical Statistics
  and Probability*, 1. The factor-of-two reading is the author's own
  small-edge algebra, from the vault page "Kelly Criterion".
