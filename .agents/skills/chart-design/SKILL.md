---
name: chart-design
description: Use when building or reviewing any chart, plot, graph, or figure — plotting code (matplotlib, plotly, d3, Recharts, ggplot), inline SVG, a figure in an artifact, a slide. Also for auditing an existing chart, or deciding whether the data needs a chart at all. Not for dashboard platform mechanics (see dashboard-builder), page-level type and colour systems (see ui-design), or data work with no chart in it.
origin: spine adapted from Andy Kirk, "Data Visualisation: A Handbook for Data Driven Design" (SAGE, 2016) — the trustworthy/accessible/elegant principles, the purpose map, angle/framing/focus, and the CHRTS families; editorial layer cross-checked against Ben Jones, "On Visualizing Data Well" (dataremixed.com, 2015), which maps Zinsser's On Writing Well onto visualisation; LATCH sorting from Richard Saul Wurman; encoding accuracy from Cleveland–McGill via Mackinlay (1986)
---

# Chart Design

A chart is an argument made out of geometry. It can be false, it can be
unreadable, and it can be ugly. Those three failures are not equal, and knowing
which one outranks which is most of the craft.

## The order that settles every argument

**Trustworthy → Accessible → Elegant.**

> "Any choices you make towards achieving 'elegance' must not undermine the
> accomplishment of trustworthiness and accessibility in your design."
> — Andy Kirk

When two choices conflict, the earlier principle wins. Every time, no exceptions
taken. A chart that misleads has failed no matter how it looks. A chart that is
hard to read has failed no matter how it looks. Elegance is what remains once
the first two hold, and it usually arrives on its own once they do.

Three gates enforce that order. Gates 1 and 2 happen before you write a line of
chart code.

## When this skill does not apply

If the task has no chart in it, this skill adds nothing. Data wrangling, a
resample, an aggregation, a query, a model, a table: answer what was asked and
stop. Do not run the gates. Do not volunteer chart advice. Do not append a note
about how the result could be plotted later. Data is not a chart, and a task
that only touches data is not this skill's business.

## Gate 1 — the question

Write this sentence, in your reply or as a comment above the code:

> This chart answers `[question]` for `[who]`, who will do `[what]`
> differently depending on the answer.

If you cannot write it, there is no chart. Say so, and offer a sentence, a
number, or a table instead. Kirk's test: *"Why present data on a map if there is
nothing spatially relevant about the regional patterns?"* Ask that of every mark
you are about to draw.

Then place the work on the **purpose map** and state the cell in two words.

| Axis | Positions |
|---|---|
| **Experience** | *explanatory* — you surface the insight for the reader · *exhibitory* — you present the data and the reader does the interpreting · *exploratory* — the reader drives and finds their own |
| **Tone** | *reading* — precise magnitude estimation · *feeling* — gist, at a glance |

Default to explanatory + reading tone. Most work belongs there. Any other cell
needs a reason you can say out loud. Feeling tone buys emotional weight and pays
for it in precision, so spend it only when the subject earns it.

## Gate 2 — editorial thinking

A chart is a photograph of data. You cannot photograph 360°, so you pick a
standpoint. Write all three down before choosing a chart type.

- **Angle** — what is measured, broken down by which dimension(s). "Revenue by
  region over time" is an angle. "The data" is not. Check it twice: is the angle
  *relevant* to the question, and is it *sufficient* to answer it?
- **Framing** — what is in and what is out: time range, population, filters,
  exclusions, denominators. Framing decides what the reader concludes, so it
  goes on the chart, in the subtitle. Not in your head.
- **Focus** — what gets emphasis. Pick one thing. If everything is emphasised,
  nothing is.

Only now pick the form: angle → CHRTS family → chart type. The families are
Categorical, Hierarchical, Relational, Temporal, Spatial; the lookup and the
caveated chart types are in `references/chart-families.md`.

Form choice is governed by how accurately each channel encodes a quantity:

**position > length > angle/slope > area > colour intensity > volume**

Spend the accurate channels on the comparison the question depends on, and the
weak ones on context. A quantity the reader must estimate goes on position or
length. A quantity the reader only needs to sense goes on area or colour.

## Gate 3 — the audit

Run the three principles in order. A failure at a higher principle is not
tradeable against a win at a lower one. Scored form: `references/audit.md`.

### Trustworthy — never traded

- Bar and area baselines start at zero. Always. A bar must represent the whole
  quantity, nothing more and nothing less.
- Line and scatter axes may be truncated, because they encode by position and
  not by size. Label the truncation when you use it.
- **No dual axis.** Two measures on two y-scales is the most common way to
  manufacture a correlation. Use two panels, small multiples, or index both
  series to a common base.
- Circles, bubbles, and any area mark scale by **area**, never by radius or
  diameter. Doubling the radius quadruples the mark.
- No 3D on 2D data. The isometric tilt inflates the front and shrinks the back.
- Uniform bin widths and uniform time intervals. An irregular bin is a claim.
- State the denominator, the aggregation, and any normalisation on the chart.
  "Rate per 100k" and "count" are different arguments.
- Source and as-of date are present. If you do not have them, say the slot is
  empty rather than shipping without one.
- Show uncertainty, or say plainly that it is not shown. A point estimate drawn
  as a hard line is a claim about precision.
- Do not extend a trendline past the data, and do not smooth a series without
  labelling the smoothing.
- Show enough history to tell a move from noise. Two periods give you a
  difference; several give you a trend. If two is all you have, say so on the
  chart rather than letting the reader infer a direction.

### Accessible — yields only to trustworthy

- Never colour alone. Pair colour with a label, a shape, a position, or a
  texture. Red–green colour blindness affects roughly 1 in 12 men and 1 in 200
  women, so the traffic-light palette fails a real share of any audience.
- Check the chart in greyscale. Print is one reason; the faster reason is that
  greyscale is the quickest test of whether meaning rides colour alone.
- Palettes survive colour-vision deficiency. On Claude Code, run the bundled
  `dataviz` skill's `scripts/validate_palette.js` rather than eyeballing it;
  elsewhere, use a ramp built for the purpose (Viridis, Cividis, ColorBrewer)
  and check a deuteranopia simulation.
- Contrast holds for text and for marks against the surface.
- Direct-label the series at four or fewer; use a legend beyond that. Never put
  a number on every point.
- **Sort deliberately.** LATCH gives the five options: Location, Alphabet, Time,
  Category, Hierarchy. Alphabetical is a lookup order, not a default — pick it
  only when the reader will scan for a known name. Otherwise sort by quantity or
  by an inherent order the subject already has.
- Grid and axes stay recessive. They are apparatus, not content.
- Units on every axis and every quoted value.
- A table or alt text exists for anyone who cannot use the picture.
- Keep a colour's meaning fixed across a set of charts. Reassigning it costs the
  reader everything they learned.

### Elegant — yields to both

- **Eliminate the arbitrary.** Every mark must be justifiable, and so must every
  mark you removed. Kirk: *"Every single design decision you make — every dot,
  every pixel — should be justifiable."*
- Grey is the workhorse. Reserve saturation for the focus. If everything is
  shouting, nothing is heard.
- One emphasis per chart.
- Consistency across a set beats local optimisation in any single chart.
- Make the last cut. Remove the least necessary flourish and check whether the
  chart got worse. Usually it did not.

## The annotation layer

This is where the writing happens, and where most charts are thrown away
half-finished.

- **The title states the finding.** "Revenue grew 40% while signups flattened"
  beats "Revenue and Signups". A title that names the variables makes the reader
  do work you already did.
- **The subtitle carries the framing.** Population, time range, exclusions.
- **One callout**, on the thing the chart is about. Usually that is the anomaly
  the reader would ask about anyway: the spike, the price change, the outage,
  the week the methodology changed. Answer it on the chart instead of in the
  meeting. Not a callout per point.
- **Source and as-of date**, in the footer, always.
- **Cut every mark doing no work.** This is Zinsser's clutter chapter with
  different nouns: examine every gridline, every tick, every border, every
  legend entry, and delete the ones carrying nothing.
- **Say what you found.** Ben Jones's reading of Zinsser's transaction: the
  reader connects with a person who has a view. A chart with no point of view is
  a table that spent extra ink.

## Colour has three jobs

Do them in this order, and stop when the job is done.

1. **Data legibility** — colour encoding the data itself. Nominal wants equal
   contrast with no implied order. Ordinal and quantitative want one hue running
   light to dark. Diverging wants two hues around a neutral midpoint, and the
   midpoint must be meaningful.
2. **Editorial salience** — colour directing the eye to the focus. Grey the
   context, colour the subject. This is the only place emphasis belongs.
3. **Functional harmony** — everything else that must have a colour to be
   visible: background, grid, apparatus, labels. Judge these as a set, not one
   at a time.

Check connotation before shipping: red means falling in the West and rising in
China; do not use cheerful palettes for grim subjects; skip blue-for-boys and
pink-for-girls, which cost the reader nothing to relearn.

## When the answer is not a chart

Say so, in one sentence, and give the better thing:

- Two or three numbers → a sentence, or a stat line.
- Precise values the reader will look up → a table.
- No pattern in the dimension you were about to plot → drop the chart, keep the
  finding.
- A request to make a small difference look large → give the honest alternative
  (plot the delta, widen the time range, add a benchmark) and name what is
  missing that would settle whether the difference matters at all. Where you
  can, state the threshold: the sample size, effect size, or historical
  variation that would make the difference real. A number the team can go get
  beats an objection they cannot act on.

Give the alternative and move on. Do not lecture.

## Quality gate

Before delivering, confirm:

- the question sentence is written, and the chart is what it required
- the purpose-map cell is stated
- angle, framing, and focus were written before the chart type was chosen
- every trustworthy rule holds, with no exception taken
- every accessible rule holds, or a violation is named with its reason
- elegance changed nothing that trustworthy or accessible established
- the title states a finding; framing is in the subtitle; source and as-of date
  are present
- nothing was added that the question did not require

## References and related skills

- `references/chart-families.md` — CHRTS lookup: angle of analysis → family →
  chart type, with the caveated types and what to use instead.
- `references/audit.md` — the three-principle audit as a scored checklist, plus
  the deception catalog.
- `dashboard-builder` — Grafana and SigNoz mechanics: panel JSON, thresholds,
  variables, panel sets. This skill supplies the thinking; that one supplies the
  platform.
- `ui-design` — owns typography, the page colour system, and layout when the
  chart lives inside a UI. This skill owns the encoding inside the frame.
- `frontend-a11y` — keyboard and screen-reader behaviour for interactive charts.
- On Claude Code only, a bundled `dataviz` skill carries a runnable palette
  validator, mark specs, and interaction rules. Use it for those mechanics. Do
  not depend on it: it does not exist in Codex.
