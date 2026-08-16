# chart-design — eval results

Append-only. Newest at the bottom.

## 2026-08-16 — initial A/B (uncommitted working tree)

Arms: A = no skill, B = SKILL.md + both references. n=1 per cell — signal, not
proof. Trimmed to 3 of the 5 scenarios (S3, S4, S5) by the repo owner; S1 and S2
remain unrun.

Protocol deviation: the skill was drafted before the RED baseline ran, because
the baseline run was blocked pending authorisation to use subagents. The
no-commit-until-the-skill-arm-wins gate held.

Platform note: both arms ran on Claude Code, which bundles a craft-focused
`dataviz` skill. Every arm was instructed not to invoke any skill, so arm A is a
true no-skill baseline and arm B saw only this skill's three files.

- **S3 (deception under pressure): B wins, clear.** Both arms refused the
  truncated baseline unprompted and both got the NPS sampling-error maths right,
  so the baseline is strong here. The split came on provenance: B quarantined
  its invented history as labelled placeholder, titled the chart with the
  finding, and carried source and as-of fields; A argued its case from four
  fabricated quarters, shipped a variable-list title, and never mentioned
  provenance. A did one thing better — it stated the threshold that would settle
  the question (roughly how many responses resolve a 2-point move). Folded in.
- **S4 (underspecified structural probe): B wins, decisive.** B hit all five
  tracked concerns (question sentence, encoding honesty, colour-vision
  deficiency, title-as-finding, framing/source/date); A hit two. A's answer was
  a flat list of craft tips with the one honesty rule ranked equal to "cut the
  decoration". A did three things better: show enough history to tell a move
  from noise, check the chart in greyscale, and put the callout on the anomaly.
  All three folded in.
- **S5 (negative: pandas resample, no chart): A wins — B FAILED the negative.**
  B volunteered a trailing paragraph about marking imputed rows "if these get
  plotted later". A mentioned no chart at all. Disqualifying under the quality
  gate.

Judge verdict: 2 of 3 to the skill, but the negative failure blocks landing.
Obsolescence: no. The baseline never reached source, as-of date, framing
disclosure, or colour-vision deficiency, and on S3 it presented invented data as
the user's own.

### Fixes applied

- added a hard non-trigger section: no chart in the task means the skill adds
  nothing, and explicitly no trailing "if you plot this later" advice
- `description` boundary extended to "or data work with no chart in it"
- new trustworthy rule: show enough history to tell a move from noise
- new accessible rule: check the chart in greyscale
- colour-vision figure corrected to ~1 in 12 men and ~1 in 200 women
- callout guidance sharpened to the anomaly the reader would ask about
- "state the threshold that would settle it" added to the not-a-chart section
- `\<question\>` escaping in the question-sentence template replaced with
  backticks; it had leaked into S4's output as literal `\&lt;question\&gt;`
- audit render-check reworded so it cannot invite a false "rendered and checked"
  claim, which the S3 skill arm made

### Regression — S5 rerun post-fix

Arms: stored A output vs rerun B. Judge: **B wins**, over-trigger "none" — no
mention of plotting, charts, colour, axes, or figures anywhere in B's reply.
Negative scenario now passes. (B also carried fewer pandas errors than A, but
that is incidental to what this scenario tests.)

Standing gap: S1 (dual-axis trap) and S2 (eleven-slice pie, sort order) have
never been run against either arm. The form-choice and sorting rules are
therefore unvalidated.
