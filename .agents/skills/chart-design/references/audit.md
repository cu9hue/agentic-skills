# Chart audit

Gate 3. The audit's shape enforces the principle order: trustworthiness is a
hard gate that runs first and is never scored against anything, then the rest is
scored. Cite `file:line`, or the chart title and element, for every finding.

## Step 1 — the trustworthy gate (hard pass/fail)

No score, no trade. A single failure means the chart does not ship in that form.

- [ ] bar and area baselines start at zero
- [ ] a truncated line or scatter axis is labelled as truncated
- [ ] no dual axis (two y-scales in one plot)
- [ ] circles, bubbles, and area marks scale by area, not radius or diameter
- [ ] no 3D on 2D data
- [ ] bin widths uniform; time intervals uniform
- [ ] denominator, aggregation, and normalisation stated on the chart
- [ ] source and as-of date present
- [ ] uncertainty shown, or its absence stated
- [ ] no trendline extended past the data; any smoothing is labelled
- [ ] the framing (time range, population, exclusions) is disclosed, not just
      applied
- [ ] colour scale is not manipulated to exaggerate (no clipped range on a
      choropleth without saying so, no non-linear scale unlabelled)

## Step 2 — scored dimensions

Five dimensions, each 0-4. Total out of 20.

| Score | Meaning |
|---|---|
| 0 | Severe: fails the basics |
| 1 | Major gaps |
| 2 | Acceptable, notable issues |
| 3 | Good, minor gaps |
| 4 | Excellent |

1. **Question and editorial.** The question sentence exists and the chart is
   what it required. Angle is relevant and sufficient. Framing is deliberate.
   Focus is one thing. Nothing on the chart that the question did not ask for.
2. **Form and encoding.** Chart type matches the angle's CHRTS family. The
   comparison the question depends on rides an accurate channel (position or
   length), not area or colour. Caveated types carry a stated reason. Sorting is
   a LATCH choice, not a default.
3. **Readability.** Colour never carries meaning alone. Palette survives
   colour-vision deficiency. Contrast holds for text and marks. Direct labels at
   ≤4 series, legend beyond. Units everywhere. Grid and axes recessive. A table
   or alt text exists. Colour meaning is stable across the set.
4. **Annotation.** Title states a finding, not the variable names. Subtitle
   carries the framing. One callout on the subject. Source and as-of date in the
   footer. The chart stands alone with nobody there to explain it.
5. **Restraint.** Every mark justifiable and every removal justifiable. Grey
   for context, saturation for focus. One emphasis. No chartjunk. Consistent
   across the set.

**Bands:** 18-20 excellent · 14-17 good · 10-13 acceptable · 6-9 poor ·
0-5 critical.

## Severity tags

- **P0:** blocking — any trustworthy-gate failure, or the chart answers no
  stated question
- **P1:** major — colour-alone encoding, CVD failure, contrast failure, missing
  units, title that names variables instead of a finding
- **P2:** minor — default sort order, legend where direct labels would read
  better, missing callout
- **P3:** polish

Fix every P0 and P1 before delivering.

## Report structure

1. Trustworthy gate: pass, or the list of failures. This goes first, always.
2. Score table (five dimensions, total, band).
3. Findings by severity, each with its location and the fix.
4. Systemic patterns — one root cause behind several findings.
5. What is already good.

## The deception catalog

How charts lie, mostly by accident. Each entry is a P0.

| Deception | What the reader sees | Fix |
|---|---|---|
| Truncated bar baseline | A 2% change looks like a doubling | Baseline at zero; plot the delta if the delta is the point |
| Dual axis | A correlation manufactured by scale choice | Two panels, small multiples, or index to a common base |
| Radius-scaled circles | A 2× value drawn 4× | Scale by area |
| 3D perspective | Front segments inflated, back segments shrunk | Remove the third dimension |
| Uneven bins | Peaks and troughs created by binning | Uniform bins; state the width |
| Uneven time intervals | A trend created by spacing | Plot time to scale, with gaps where data is missing |
| Count choropleth | A map of where people live | Map a rate or ratio |
| Cherry-picked window | A trend that reverses outside the frame | Show enough history to be representative; disclose the window |
| Aggregation hiding the case | A flat average over a bimodal population | Show the distribution, or split the population |
| Missing denominator | Absolute counts read as prevalence | State the denominator |
| Clipped colour scale | Extremes flattened into one shade | Full range, or say the scale is clipped |
| Point estimate as hard line | Precision the data does not have | Show the interval, or state that it is not shown |
| Unlabelled smoothing | A clean trend that is partly the filter | Name the window; show the raw series behind it |
| Inverted or reversed axis | The opposite conclusion | Conventional orientation, or an unmissable label |

## Pre-delivery gate (hard pass/fail)

The chart does not ship until all five pass:

- [ ] the trustworthy gate passes with no exception taken
- [ ] the question sentence is written and the chart is what it required
- [ ] palette validated against colour-vision deficiency, and no meaning rides
      colour alone
- [ ] title states a finding; source and as-of date are present
- [ ] the chart was rendered and looked at. If you cannot render it, say that
      plainly. Never claim to have checked a picture you did not see.
