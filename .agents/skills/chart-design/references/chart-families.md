# CHRTS — angle of analysis to chart type

Kirk's taxonomy. Five families, keyed by the **primary** angle each one answers.
Find the angle you wrote in Gate 2, read down to the chart type.

Some charts sit in two families. A flow map is Relational and Spatial. Classify
by the angle that dominates your question, not by the marks on the page.

Dashboards and small multiples are not chart types. They are composition
techniques over these types, and their hard problems are editorial (which angles
to show) and compositional (how to fit them together).

---

## C — Categorical

Comparison between categories. Every other family also compares categories, but
adds a second dimension of analysis; this family is the one where the category
*is* the analysis.

### Comparisons — "how do these categories compare on one measure?"

| Chart | Use it when |
|---|---|
| **Bar chart** | The default. One measure across categories. Horizontal when labels are long. Baseline at zero, always. |
| **Clustered bar** | A second categorical breakdown, two or three sub-categories at most. Beyond that the clusters stop reading. |
| **Dot plot** | Large values with a narrow range of differences, where bars would be near-identical stubs. |
| **Connected dot plot** (dumbbell) | Two states per category — before/after, actual/target, men/women. The gap is the subject. |
| **Pictogram** | Feeling tone, small counts, subject with an obvious icon. One icon = one unit, never a stretched icon. |
| **Proportional shape / bubble chart** | Feeling tone over precision. Area encoding, so accept that readers will only get big/medium/small. |
| **Radar chart** | Rarely. See caveats. |
| **Polar chart** | Cyclical categories (months, compass points) where the wrap-around matters. |

### Distributions — "how are values spread?"

| Chart | Use it when |
|---|---|
| **Histogram** | One variable's shape. Uniform bin widths; state the bin width. |
| **Range chart** (box plot, violin) | Comparing spread across categories. Say which summary the box shows. |
| **Univariate scatter** (strip, beeswarm) | Small n, where showing every observation beats summarising it. |
| **Word cloud** | Rarely. See caveats. |

### Part-to-whole — "how does the whole divide?"

| Chart | Use it when |
|---|---|
| **Stacked bar** | Parts within categories. Works when the parts are ordinal so the stack order means something. Only the bottom segment and the total are read accurately. |
| **100% stacked bar** | Composition when the totals are irrelevant. Say that the totals are hidden. |
| **Waffle chart** | One breakdown where the reader should be able to count units. 10×10 grid. |
| **Back-to-back bar** | Two mirrored populations — a population pyramid. |
| **Pie chart** | Two or three parts, or one part against its remainder. See caveats. |
| **Treemap** | Many parts spanning orders of magnitude, where the tail must stay visible. Area encoding, so comparison is approximate. |
| **Venn diagram** | Overlapping set membership, two or three sets. |

---

## H — Hierarchical

"What is the structure of this tree, and how do quantities sit in it?"

| Chart | Use it when |
|---|---|
| **Dendrogram / tree diagram** | Structure is the subject: what contains what, at what depth. |
| **Sunburst** | Hierarchy plus magnitude, radially. Outer rings compress; deep trees become unreadable. |
| **Treemap** | Hierarchy plus magnitude, rectangularly. Better than sunburst for reading sizes, worse for reading depth. |

Both sunburst and treemap need interaction (hover, drill) past two levels.

---

## R — Relational

"How do these measures relate?"

### Correlations

| Chart | Use it when |
|---|---|
| **Scatter plot** | Two quantitative measures. The workhorse of this family. |
| **Bubble plot** | A third measure by area. The third measure gets read approximately; put it third in importance. |
| **Parallel coordinates** | Many measures across many records. Needs interaction and an ordering rationale for the axes. |
| **Heat map** | Two categorical dimensions crossed, one measure by colour. Sort both axes deliberately. |

### Connections

| Chart | Use it when |
|---|---|
| **Node–link diagram** | Network structure. Layout is a claim; state the algorithm. |
| **Matrix chart** | Dense networks where a node–link diagram becomes a hairball. |
| **Chord diagram** | Flows between a small, fixed set of entities. |
| **Sankey diagram** | Flow through stages, where the conserved total matters. |

---

## T — Temporal

"How has this changed over time?"

### Trends

| Chart | Use it when |
|---|---|
| **Line chart** | The default. Change and trend between points. Axis may be truncated; label it if you do. |
| **Bar chart over time** | Individual values matter more than the trend between them. |
| **Slope graph** | Exactly two time points across many categories. Ranking change is the subject. |
| **Bump chart** | Rank over time. Plots rank, not value — say so, because rank hides magnitude. |
| **Area chart** | One series against zero, where the accumulated quantity is meaningful. Baseline at zero. |
| **Stacked area** | Composition over time. Only the bottom band is readable; order the bands deliberately. |
| **Stream graph** | Feeling tone over many series. No shared baseline, so no accurate reading. |
| **Connected scatter** | Two measures whose *joint* path over time is the subject. Label the start, the end, and the turns. |
| **Horizon chart** | Many series in little vertical space. Requires a reading key; do not use it for a general audience. |

### Activities

| Chart | Use it when |
|---|---|
| **Gantt chart** | Durations with start and end, across a schedule. |
| **Connected timeline** | Events in sequence, where the gaps between them matter. |
| **Instance chart** | Point events over time across categories. |

---

## S — Spatial

"Where is this?" Use a spatial family only when location is part of the answer,
not because the data happens to have place names in it.

### Overlays — real geography

| Chart | Use it when |
|---|---|
| **Choropleth** | A **rate or ratio** by region. Never a raw count: the eye reads area, so a choropleth of counts is a population map. |
| **Proportional symbol map** | Counts by location. Scale symbols by area. |
| **Dot map** | Individual occurrences, or one dot per fixed unit. Say which. |
| **Isarithmic map** (contour, heat surface) | A continuous surface — temperature, elevation, density. |
| **Flow map** | Movement between places. Relational and Spatial both. |
| **Prism map** | Rarely. Extruded 3D regions occlude each other. |

### Distortions — geography reshaped by the data

| Chart | Use it when |
|---|---|
| **Area cartogram** | The measure should dominate the geography and readers know the map well enough to survive the distortion. |
| **Grid map** (tile grid) | Equal weight per region regardless of physical size — the usual fix for a choropleth where small dense regions vanish. |

---

## Caveats — types that need a reason

Not banned. Each has a narrow job and fails outside it.

- **Pie chart.** Angle is a weak channel. Works for two or three parts, or one
  part against its remainder. At five or more, use a sorted bar chart. Never
  explode it, never tilt it, never nest two of them.
- **Radar chart.** Area depends on the arbitrary order of the axes, and the
  shape rewards whichever variables you happened to put next to each other. Use
  it only for a small fixed set of axes readers see repeatedly, in the same
  order every time. A dot plot or a small-multiple bar usually beats it.
- **Word cloud.** Encodes frequency by an area-ish attribute of glyphs of
  unequal width, so it reads the frequency of *long words*. Feeling tone only.
  A sorted bar chart of term counts is the honest version.
- **Stacked area and stacked bar.** Only the bottom band sits on a common
  baseline, so only it is readable. Fine for composition, wrong for comparing
  the middle bands. If a middle band is the subject, break it out.
- **Treemap and sunburst.** Area and angle encoding. Good for "this dominates",
  bad for "this is 12% larger than that".
- **Dual axis.** Not a caveat. See the hard rules in SKILL.md.
- **3D on 2D data.** Not a caveat. See the hard rules in SKILL.md.

## Sorting — LATCH

Every categorical axis is sorted somehow, including by accident. Pick one of
Wurman's five on purpose:

**L**ocation · **A**lphabet · **T**ime · **C**ategory · **H**ierarchy (by
quantity, ascending or descending).

Hierarchy is the usual right answer for a bar chart: sort by the measure so the
ranking is visible. Category is right when the subject has an inherent order
(ordinal scales, seniority, positions on a team). Alphabet is a lookup order —
choose it only when the reader arrives knowing which label they want.
