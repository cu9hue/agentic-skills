# market-evaluation — eval results

Append-only. Newest at the bottom.

## 2026-09-24 — initial A/B (base 94f0360)

Arms: **A** = no skill (baseline, RED ran before the skill was drafted),
**B** = SKILL.md read by the arm. n=1 per cell — signal, not proof. Arms had
web search and fetch. One blind judge scored anonymized, per-scenario-shuffled
outputs and fetched two load-bearing citations per output in S1–S4.

RED failures the draft targeted: A invented its own axes (S1) or used none
(S2–S4); no arm asked US-first, year-3 adjacencies, repeatability, or
learning speed; every arm sized toward $100M or "venture scale", not $1bn;
no scores unless asked, and S1 summed them ("+6 of ±45"); S3 ended in
clarifying questions instead of a verdict. A already sourced well, labeled
assumptions, and resisted the S4 pressure.

- S1: **B** — A used its own axes, bare scores, and an overall total; B hit
  every bullet with a Census × tiered-price bottom-up and a per-test gate.
- S2: **B** — A had no US-first axis, no cycle count, no scores; B named
  Basis as the US equivalent and scored it bearish, counted 12–18 cycles.
- S3: **B** — A ended in three clarifying questions; B stated assumptions,
  scored all nine axes, and failed Truth on market dynamics (-3).
- S4: **B** — both refused to inflate; only B split the district slow loop
  (1–2 cycles) from the parent channel and tied the close to the weakest
  axis.
- S5: **tie** — both gave ~$530M with a source; B did not over-trigger.

Judge verdict: the structured nine-axis outputs won 4 of 5, S5 a tie.
Obsolescence: no — the no-skill arm failed the structural probe (S3) and
never asked the deck's questions. Citation integrity: no fabrications, but
B's S2 cited a page for "6.7% of revenue on IT" that does not contain it,
and that figure carries the answer's IT-pool math; A's S2 linked a true
claim to the wrong DATEV release. Fixed next by requiring the linked page
to state the number.

## 2026-09-24 — regression for the "link the page that states the number" rule (base 94f0360)

Arms: **B** = pre-edit (outputs from the initial run), **C** = post-edit.
n=1 per cell — signal, not proof. Blind judge, labels shuffled per
scenario; it fetched four load-bearing citations per output in S1–S4 (16 per
arm) and grepped primary PDFs and text files where pages blocked fetching.

- S1: **C** — rubric tied; B's $1bn enterprise tier rested on a pricing page
  that states a different figure, C's four checked links all held.
- S2: **C** — rubric tied; B's 6.7% IT-spend figure is not on its linked
  page, C's links all held (BStBK, DATEV, Destatis).
- S3: **tie** — both clean, both failed Truth on market dynamics (-3).
- S4: **B**, narrowly — C read the buyer as districts and handled the parent
  channel only in the re-run offer; B scored the parent loop and contrasted
  the district loop. Both refused to inflate. Reading choice, not a rule
  failure: n=1 cannot separate this from sampling variance.
- S5: **tie** — both one number with a source, no ceremony; C also said it
  could not open the cited page and asked the user to check it.

Citation integrity across S1–S4: B 2 load-bearing mismatches + 3 minor; C 0
load-bearing + 0 minor. No fabrications in either arm. Post-edit arm holds.

## 2026-09-28 — regression for the target-outcome setting (base 9930648, uncommitted branch skills/target-outcome-bar)

Change: axis 1 scored under two bars (generational $1bn revenue, always the official score; venture outcome = ceiling × ≤30% share × the lower of ≥2 linked comparable exit multiples, or "unpriced"); Scale gated under both; verdict leads with the bar the user names. New scenario S6. Arms: pre-edit vs post-edit, web on; n=1 per cell (S2 post re-run once after adding a line requiring the link check on every venture-reading input); blind judges, labels shuffled; judges fetched two load-bearing citations per output in S1–S4 and S6.

- S1: **tie** — both clean on rubric and citations; post added the venture reading unasked (neutral).
- S2: **pre**, twice — post run 1 cited a 6.7% IT-cost share its linked page does not state and built its venture +1 on it; post run 2 (after the link-check line) misread 8,569 Syndikus Steuerberater as practices, understating the ceiling ~16%, and cited competitor evidence via news-search links. Verdict unchanged by the error, but citation integrity lost both times.
- S3: **tie** — both clean.
- S4: **pre**, narrowly — separated the school and parent channels; buyer-reading choice, as in the 2026-09-24 run.
- S5: **tie** — both one number, no ceremony.
- S6: **post** — scored and gated both bars, lower of two linked multiples (Kneat 9.1×, Veeva 11.0×); pre replaced the generational bar with the user's and priced the exit off one comparable.

Post-edit arm does NOT yet hold: it wins the new behaviour (S6) but loses S2 on citation integrity in both runs. Hypothesis: computing the venture reading on every run adds research load that crowds out the link check. Not committed.

## 2026-10-20 — ask the ceiling before research

Edit: the skill now asks the ceiling once before research (default $1bn ARR
in under 10 years, a $1bn exit, or a custom ARR number) unless the request
states it. A custom ceiling rescales axis 1 and adds a one-line generational
reading. Axes 2–9, the venture-outcome reading and the forward reading are
unchanged.

No regression run: the user judged the change minor and chose to skip it.
S1–S4 name no ceiling, so under this edit they now pause for the question;
rerun them as two-turn scenarios (scripted reply "$1bn ARR") at the next
behavior change.

## 2026-10-20 — query the founder's vault (S7)

Edit: when `SECOND_BRAIN_URL` and `SECOND_BRAIN_READER_TOKEN` are set, the
skill queries the vault through the `second-brain-retrieval` API with
one-to-three-word queries, and cites vault claims by note path and chunk ID.
New scenario S7; pre-edit vs post-edit arm, n=1 each, Exa calls capped equally.
Blind judge verified chunk IDs against the service and opened two web links
per output.

- S7: **post**. Pre never queried the vault; post cited vault chunks and put
  open vault contradictions into risks / bear cases. Web citations held in
  both arms.
- Gaps in the post arm, not yet fixed: a vault-backed shift cited the concept
  page instead of the source note behind it; some vault citations were
  decorative (heading-only chunk, framing that moved no score).
- Confound: the service index is a snapshot from about 2026-09-26 (170 of 509
  notes missing, including the FERC/ERCOT/PJM, OCC and DFAH-Bench sources),
  so domain queries returned little. The test measures the behaviour, not the
  value of a fresh index.
