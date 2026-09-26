# venture-bet-discovery — eval results

Append-only. Newest at the bottom.

## 2026-09-26 — regression for aligning with market-evaluation (base f85b095)

The skill was imported from a claude.ai-synced copy with no evals, so the
scenarios were backfilled before the edit. Arms: **B** = pre-edit (the
imported copy), **C** = post-edit. n=1 per cell — signal, not proof. Arms
read the skill from a neutral path, had no web access, and invoked no other
skill. One blind judge scored anonymized outputs (labels shuffled per
scenario, key held back until scoring was done).

- S1: **C** — B screened against $100M with 15/25/40% tiers, ran no US-first
  or learning-speed check, and killed K1 at step 6 without a scale verdict; C
  used the $1bn bar and killed K1 on heroic share, K2 on US first, and K4 on
  both ceiling and learning speed. C named a Janz shape for only two of four
  candidates and used a "Figma-like 6.3×" multiple as a best case with no
  comparable.
- S2: **C** — B sent the survivor straight to the stress test; C routed it
  to market-evaluation first, carrying the ceiling, shape, adjacency and a
  learning-cycle estimate.
- S3: **C** — B described the old $100M screen with no handoff; C laid out
  the $1bn bar, US first, year-3 asset and learning speed, and ended with
  market-evaluation before the stress test. C did not name a revenue shape.
- S4: **tie** — both treated the $10k/month ask as a bootstrap search and
  gave a usable answer; neither leaked the venture bar.

Judge verdict: C won all three venture scenarios; the negative case was a
tie. Both arms' S3/S4 answers showed auto-memory context (the founder's
spikes) leaking into the arms — equal across arms, noted as noise.

Follow-up edit from the judge's findings: the shape is now required "for
every candidate, killed or not", and a retention comparable must sell to the
same kind of buyer (Snowflake and Figma show the method, not a default).
Rerun of S1 on the follow-up (arm **C'**, n=1): named a shape for all four
candidates, kept 1.0× where no comparable existed, and used a borrowed
multiple only to confirm a kill, flagging that it came from a different
buyer. US-first and learning-speed kills held. Post-edit arm holds.

## 2026-09-26 — regression for removing the startup-idea-discovery references (base 1bd55ab)

The skill no longer names `startup-idea-discovery`: the comparison section
became "What this screen does not kill", the description's boundary reads
"a side business meant to pay the founder", and an island niche is logged
instead of handed off. Only S4 exercises the changed boundary, so only S4
was rerun (arm **D** = post-edit, n=1), compared against C's S4.

- S4: **holds** — D applied no venture screen and no $1bn bar, used
  bootstrap criteria (who pays today, reachable buyers, deposits before
  building), and gave a usable answer, matching C.

## 2026-09-26 — regression for the single-formula ceiling (base c38ef98)

The ceiling is now `market-evaluation`'s axis 1: N × revenue per customer at
today's sourced price, on the one pricing basis the product would charge
(seat, usage, or a take rate on the customer's flow). The `max()` of two
ceilings, the expansion multiple, and the "do not kill on 1.0×" rule are
gone; growth past today's price counts only as a named adjacency. S1's rubric
gained a bullet for this rule. Arms: **C** = previous post-edit outputs (S1
from the C' rerun, S2 from the first run), **E** = this edit. n=1 per cell;
blind judge, labels shuffled per scenario.

- S1: **E** — C treated every ceiling as a floor "at a 1.0x expansion
  multiple", refused scale kills for K1–K3, and borrowed Figma's retention to
  test K4; E killed all four on scale at today's price and reopened K1/K3
  only through a sourced wider N, a sourced take rate, or the FALSIFY check.
- S2: **E** — C rescued K3 with a recalled, unverified ServiceTitan NRR
  multiple; E held the ceiling at today's price and gave a conditional
  step-2 kill with sourced rescue paths.

Judge verdict: E won both. Post-edit arm holds.

## 2026-09-26 — regression for the ideation split and the stress-test removal (base 2fdcd3e)

Generation moved to `venture-ideation`: this skill now screens a batch,
checks the batch against the ideation quotas (screening a narrow batch
anyway, with a warning), and ends at `market-evaluation` followed by
customer conversations — no stress test. S3's rubric now expects generation
via `venture-ideation` first. Arm **F** = post-edit, n=1, checked against
the rubrics; the S3 arm had both skills available.

- S2: **holds** — routed K3 to market-evaluation then customer
  conversations; carried ceiling, shape, share and learning speed; no
  advocacy; no stress test.
- S3: **holds** — batch of 12–15 from eight origins with the quotas, then
  the ten-step screen at $1bn, then market-evaluation and customer calls.
  It did not name the revenue shape in the scale step.

## 2026-09-26 — regression for the flagged outcome (base efdccaa)

A step-2 shortfall now ends in **kill** (robust: sourced inputs or a kill
that holds across plausible values, and nothing moving) or **flag** (a dated
growth signal, a pivotal unsourced input, or a breaking assumption). A flag
names the input to verify and the value that clears the line, never projects
growth into a bigger ceiling, continues through steps 3–10, and reaches
market-evaluation only after verification. New scenario S5 (kill vs flag).
Arms: **F** = pre-edit, **G** = post-edit; n=1; blind judge on S5.

- S5: **G** — F killed P1 at step 2 ("neither kill is close") and passed P3
  conditionally without a flag; G flagged P1 (growth: clears at ~$171bn a
  month of volume at 0.25%, ~8.5× January 2026) and P3 (pivotal price),
  killed P2 as robust (~$28M per venue needed), and carried both flags
  through later steps, where they died at steps 9 and 5. Neither arm
  projected growth or sent a flag to market-evaluation. G's headline said
  "nothing is flagged" while its body recorded two flags; the handoff now
  says a flag killed later belongs in the kill log with its flag noted.
- S1 (G only, regression): **holds** — all four kills robust; K3 explicitly
  not flagged because its inputs are sourced and no growth signal exists.

Post-edit arm holds.
