# market-selection — eval results

Append-only. Newest last.

---

## 2026-09-03 — RED baseline, before drafting. Verdict: do not build the skill.

**Sample size: n=1 per cell.** Five scenarios, baseline arm only (no skill, which
does not yet exist). All baseline agents ran inside the second-brain repo, so they
had `CLAUDE.md` and the `Concepts/` graph available.

| Scenario | Rubric outcome |
|---|---|
| S1 hidden fatal criterion | **pass** 4/4 |
| S2 graveyard discriminator | **pass** 4/4 |
| S3 underspecified probe | **pass** 3/4, one partial |
| S4 generate from edge | **pass** 4/5, one partial |
| S5 negative, landing copy | **partial** — wrote the copy, but over-interrogated position |

**Verdict: the skill is unnecessary. Stopping per the authoring mandate.**

The baseline arm reconstructed every discriminator the skill was going to encode,
by reading the concept pages. S1 named buyer concentration as potentially fatal and
did the bottom-up ceiling arithmetic. S2 produced the three-way graveyard
discriminator unprompted. S3 raised five criteria against a prompt that named no
axis. S4 generated four candidate directions from a stated edge, filtered them
afterwards rather than before, and applied the control-point test to choose.

The knowledge is already operational in the repo. A skill would restate the concept
pages to an agent that can read them.

**Where the partials fell.**

- S3 treated bottom-up distribution for developer tools as given rather than as a
  hypothesis. Minor, and defensible for that category.
- S4 was thin on who currently pays what. It named the gaps well and the buyers
  weakly, which is the market-pull half of the framework underperforming.
- S5 is the one real weakness, and it runs the opposite way from a missing skill.
  The base model already interrogates positioning on a copy request. Adding a
  market-selection skill would amplify an over-trigger that is present without it.

**Consequence for any future version.** Build this only if the criteria need to
travel outside this repo, where the concept pages are absent. That is a packaging
job with a tightly scoped `description` and an explicit "not for" covering copy,
positioning and messaging. It is not a behavior-change job here, and the obsolescence
probe (S3, the underspecified structural scenario) shows no delta to recover.

**Unexpected finding.** The exercise was worth running for a reason unrelated to
skills: S4's generation run produced four candidate directions and a through-line
thesis, sourced entirely from gaps documented in `Concepts/`. Recorded separately.

## 2026-10-20 — rewrite as a direction-finding skill (branch market-selection-directions, base b6e3d21)

Why: a discovery batch on 2026-10-20 (synced startup-idea-discovery) screened 22 candidates to 3 at a desk with no buyer contacted, and venture-bet-discovery kills on the first failed step by design. The user asked for a skill that maps directions and trends, asks venture vs bootstrap first, and retires venture-ideation and venture-bet-discovery. New scenario set in `scenarios.md`; the 2026-10-08 set is archived.

Setup: both arms ran with no web tools, no Skill tool and no other local files; the skill arm read SKILL.md first. Both arms inherited the second-brain vault as working directory (visible in S1 baseline, which mined the vault's git status). The orchestrator condensed some outputs to rubric-relevant records before judging; both arms were condensed the same way, and the judge was told so. One blind judge, labels shuffled with a fixed seed. n=1 per cell: a signal, not proof.

RED (baseline, before drafting): S1 fail 1/4 (no bar, generic categories, no edge); S2 partial 3/6 (no dated shifts, no cross-signal pattern, vague threshold); S3 partial 1/4 (no ceiling, undated shifts, no evaluation handoff, one generic test); S4 mostly pass 3/4 (no widening, no threshold); S5 pass.

Draft v1 failed its own run: S3 and S4 replied with questions only (Step 1 "ask in one message" blocked whenever a profile or domain was given). Fixed in v2 with a "never block on questions" rule and an explicit hand-off for one named market. All five scenarios rerun on v2.

GREEN (v2 vs baseline, blind):
- S1: **skill** — set the bar and asked for the edge; baseline split into "read or build?" with generic advice.
- S2: **skill** — explicit bootstrap bar, five directions on dated shifts, three patterns, thresholds and time boxes; baseline's tests were partial and its threshold vague.
- S3: **skill** — assumed ceiling stated, eleven dated shifts, per-direction tests, handoff to market-evaluation with the ceiling; baseline had none of the last three.
- S4: **skill, narrowly** — sharper pattern from the kills and explicit widening (spend caps resold to whoever eats the chargeback); judge flagged 12 shifts plus 5 directions as close to a new batch.
- S5: **tie** — both evaluated the named market; neither over-triggered.

Follow-up: v3 caps directions at 3 when the founder arrives with killed ideas and leads with the one test. S4 rerun below.
- S4 rerun on v3: **skill** — commits to one direction with a 100-message test, a pass at 3+ incidents in 2 weeks and a named kill signal; baseline diagnoses the kill rule well but hands back three unranked directions with no keep threshold. Judge still marks both partial on "fresh batch" (v3 gives three directions plus six shifts).
- S1–S3 and S5 were not rerun on v3: the v3 change only applies when the founder brings killed ideas, which none of them do.

Verdict: skill arm wins 4 of 5 (S1, S2, S3, S4) and ties the negative (S5, no over-trigger). Obsolescence probe (S1, underspecified): clear delta — baseline never raised the bar or the edge. Post-edit arm holds. n=1 per cell.

Observed in S4 v3, outside the rubric: the top direction was UK gambling compliance. The profile stated no values, so this is not a failure here, but a founder with a "net positive" constraint should see it checked; Step 5's constraint drop covers that case when the value is stated.

## 2026-10-20 — search with Exa (S6, web tools on)

Change: name the Exa MCP tools as the only search route (no WebSearch, no curl), treg only for data Exa cannot reach with the price quoted first; then a second edit after the first post run: a search result is a lead, open the page with `web_fetch_exa` (batched) before a shift enters the table, fetch before more searches when calls are limited, mark unopened links *(not opened)*. Both arms capped at 8 tool calls. Tool use read from each arm's own call list. n=1.

- Pre-edit arm: 5× WebSearch, no Exa, no fetch; cited search results. Fails tool choice and page-opening.
- Post-edit arm, Exa rule only: 4× `web_search_exa`, no WebSearch, no fetch. Passes tool choice; fails page-opening.
- Post-edit arm, Exa + fetch rule: 4× `web_search_exa`, 1× batched `web_fetch_exa` over the three load-bearing pages, two secondary links marked *(not opened)*. Passes all three items.

Verdict: post-edit arm holds on S6.

## 2026-10-20 — geography travels with the bar (S7 new; S2 rubric item added)

Change: take geography from the brief; when absent, infer it, label it *(assumed)* beside the bar and ask it first under "To sharpen this"; keep shifts, buyers and tests inside it, at most one marked exception, never in a region the founder ruled out. Output header gains a Geography line. No web tools. n=1.

- S7 (brief says "US only, not UK or EU"): **tie**. Pre-edit stated "US only" in its constraints line and kept every direction US (Nacha 2026 ACH fraud monitoring, agent spend authority, post-Synapse reconciliation, FERC 2222 aggregators). Post-edit gave an explicit Geography line and kept every direction US (Nacha, agent refund authority, ERCOT RTC+B, event-contract surveillance flagged against net positive, CMS prior authorization marked outside the founder's industry). When the brief states geography, the old skill already respects it.
- The rule targets the unstated case: S2 v2 (pre-geography) ranked EU and UK directions without ever stating a geography. S2 rerun on the current skill below.
- S2 rerun after the inference wording (geography inferred from profile): stated "EU + UK (assumed, from power trading and a crypto exchange; correct me first)" — rubric item met, but the profile names no region, so the inference was invented. Wording changed: infer only when the profile names a region, otherwise assume US, or global for a product sold online with no local rule (consistent with market-evaluation's US-first axis; the user's own preference is US or global).
- S2 rerun on that wording: **pass** — "Geography: US first, product sold online globally (assumed)", geography first under "To sharpen this", every direction US or global (agent refund authority, FERC 2222 aggregators, instant-payout fraud, agent insurers), sports betting and prediction markets dropped on net positive (assumed). Post-edit arm holds.

## 2026-10-20 — query the founder's vault (S8)

Edit: when `SECOND_BRAIN_URL` and `SECOND_BRAIN_READER_TOKEN` are set, the
skill queries the vault through the `second-brain-retrieval` API with
one-to-three-word queries, and cites vault claims by note path and chunk ID.
New scenario S8; pre-edit vs post-edit arm, n=1 each, Exa calls capped equally.
Blind judge verified chunk IDs against the service and opened two web links
per output.

- S8: **post**. Pre never queried the vault; post cited vault chunks and put
  open vault contradictions into risks / bear cases. Web citations held in
  both arms.
- Gaps in the post arm, not yet fixed: a vault-backed shift cited the concept
  page instead of the source note behind it; some vault citations were
  decorative (heading-only chunk, framing that moved no score).
- Confound: the service index is a snapshot from about 2026-09-26 (170 of 509
  notes missing, including the FERC/ERCOT/PJM, OCC and DFAH-Bench sources),
  so domain queries returned little. The test measures the behaviour, not the
  value of a fresh index.

## 2026-10-20 — proven category, underserved niche (S9 new; S3 regression)

Edit: under the bootstrap bar, at least one direction is a proven category
(leaders and prices named) with a niche defined by a buyer segment whose
workflow differs, preferably one the shift is growing. Every niche direction
states its ceiling as niche buyers × price; under 3× the income target is a
named risk. Under the venture bar, a niche in a led category needs the shift
to grow it, or the ceiling is the main risk. New anti-pattern: the feature
niche. Output gains a Category line. Source: Starter Story's bootstrapper
advice. No web tools, no vault. Pre-edit vs post-edit arm, n=1 each, blind
judge.

- S9: **post**. Judge, post vs pre: proven category with leaders pass vs
  partial; buyer-segment niche pass vs partial; ceiling as buyers × price
  pass vs fail; niche growth pass vs fail. Pre never sized a direction
  against the $1M target and ranked second a direction whose own belief
  (5 × $100k) is half the bar. Post sized four directions ($12M, $3M, $7M,
  $6M, all assumed numbers) and flagged the $3M one as a named risk.
- Structure item: partial in both arms, because the judge saw condensed
  outputs from which I dropped the tests of directions 4–5. Both full
  replies carried a test per direction. Runner error, not an arm difference.
- Judge flags on post: direction 1 borrows proof of spend from fraud tools
  while calling itself a new layer, and its main risk (platforms ship
  refund caps) admits it may be a feature; growth claims are bare
  assertions; "12–18 months" and "US first" were added to a brief that said
  "US or global".
- S3 regression (post only, against S3-venture-v2): **holds**. Venture bar
  with ceiling assumed, dated shifts, patterns, tests, hand-off to
  `market-evaluation`. Category lines appeared on every direction. Gap: the
  one proven-category direction (agent-traffic risk scoring) gave no ceiling
  and no statement on niche growth, so the venture clause was half followed.
