# Market evaluation: compliance software for US data centres under the new large-load interconnection rules

**Assumptions:** The customer is the owner or operator of a US data centre that connects at transmission voltage: hyperscalers, colocation firms, neoclouds and crypto miners. The buyer is that company's head of energy or power, or its compliance lead. The users are its electrical and compliance engineers. The geography is the US. The product is SaaS that runs NERC registration, CLO-001/002/003 compliance evidence, modeling-data submissions, and readiness for the new RTO large-load application rules. The ceiling is **$100M ARR in under 10 years**, as the request states. "The new rules" means two things here. The first is FERC's June 2026 show-cause orders to the six RTOs. The second is NERC's new Computational Load Owner/Operator registration and its standards. Utilities are a possible second buyer, but this run does not score them as the core market.

**Verdict:** Under the $100M bar, **Scale fails** (1, -4). The market is real, mandatory and urgent, but too small: about 400 sites in scope, at a plausible $50k–$100k per site per year, is about $30M of total spend at 100% share. The generational ($1bn) reading is -5, and the venture-outcome reading is -5. **Truth passes** (lowest: 4. Market dynamics, -2). **Speed passes** (lowest: 9. Learning speed, -2). The weakest axis overall is 1. The forward reading does not clear $100M either, so this market is small, not early. It suits a profitable niche software-plus-services firm with a $20–40M revenue ceiling, or a wedge into a larger data-centre power platform (flexible-load operations, interconnection, energy procurement). It is not a stand-alone $100M ARR market.

| Test | Axis | Score | Confidence |
|---|---|---|---|
| Scale | 1. $100M ARR path | $100M ceiling -4 · generational -5 · venture outcome -5 | medium |
| Scale | 2. US first | +3 | high |
| Scale | 3. Adjacencies | +1 | low |
| Truth | 4. Market dynamics | -2 | medium |
| Truth | 5. Problem size | -2 | medium |
| Truth | 6. Pain depth | +2 | medium |
| Truth | 7. Repeatability | +1 | medium |
| Truth | 8. Tailwinds | +3 | medium |
| Speed | 9. Learning speed | -2 | low |

Scale: FAIL at $100M (1, -4) · FAIL generational (1, -5) · FAIL venture outcome (1, -5) · Truth: PASS (lowest: 4. Market dynamics and 5. Problem size, -2) · Speed: PASS (lowest: 9. Learning speed, -2)

## Scale

### 1. $100M ARR path — $100M ceiling -4 · generational -5 · venture outcome -5 (medium)

**What the rules require.**
- **FERC.** On 18 June 2026, FERC ordered all six RTO/ISOs to justify or reform their large-load tariffs within 60 days ([FERC, 2026](https://ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration)). The orders preliminarily define a large load as ≥50 MW at >69 kV. They contemplate readiness requirements, real-time telemetry, load management plans, and periodic reporting of actual versus projected load ([Vinson & Elkins, 2026](https://www.velaw.com/insights/ferc-institutes-six-simultaneous-section-206-proceedings-targeting-large-load-interconnection-across-all-rto-iso-markets/)).
- **NERC.** NERC's draft registry criteria make the owner and the operator of a Computational Load Site of ≥50 MW at ≥100 kV registered entities ([NERC webinar, July 2026](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/20260713_registration_cle-registration-update-webinar.pdf)). Registration is expected to begin in early 2027 ([Certrec, 2026](https://www.certrec.com/nerc-compliance/computational-load-standards/)). Under CLO-001-1, these entities must submit modeling data on a schedule of at least once every 13 months ([NERC CLO-001-1 redline, 2026](https://www.nerc.com/globalassets/standards/projects/2026-02/final-ballots/project-2026-02-computational-loads-clo-001-1-final-redline.pdf)).

**Bottom-up arithmetic (today).**
- *Customers.* One tracker counts 221 operational and 200 under-construction campuses, 421 in all ([Data Center Index, 2026](https://datacenterindex.ai/pipeline)). This is a weak aggregator source, and its list includes a few non-US campuses. A floor is the roughly 90 operational US campuses of ≥100 MW ([Bisnow citing The Kobeissi Letter, Sep 2026](https://www.bisnow.com/news/national/data-center-development/large-scale-us-data-centers-projected-triple-by-2030)). This is also a weak source. I assume **~400 US sites in scope by 2028** *(inference)*. Ownership is concentrated: trackers list 377–468 operating companies across all US sites ([Aterio, Oct 2026](https://www.aterio.io/insights/us-data-centers); [FieldProspects, Oct 2026](https://fieldprospects.com/data/data-centers/)).
- *Price per site.* Here are the comparables:
  - AssurX NERC compliance software cost a municipal utility $138,975 for the first year and $17,000 a year after that ([City of Columbia council memo](https://www.como.gov/Council/Commissions/downloadfile.php?id=20419); undated, likely more than 3 years old).
  - Compliance-tracking tools cost from "$30,000 to well into six figures" ([POWER, 2016](https://www.powermag.com/automated-compliance-tracking-solution-right/); more than 3 years old).
  - A smaller NERC CIP entity spends $100k–$250k a year all-in, staff included ([AuditXYZ](https://www.auditxyz.com/frameworks/industry-specific/nerc-cip); weak vendor source).

  I assume **$50k–$100k per site per year** for software that also covers modeling-data and telemetry evidence *(assumption)*.
- *Compliance spend at 100% share.* 400 × $75k = **$30M a year** *(inference)*.
- *Interconnection-application module.* ERCOT received 198 new large-load requests in Q1 2026 ([ERCOT, Apr 2026](https://www.ercot.com/files/docs/2026/04/13/9-Interconnection-and-Grid-Analysis-Update.pdf)). That is about 800 a year in ERCOT *(inference: Q1 × 4)*. Doubled for the rest of the US *(assumption)* and priced at $25k per application *(assumption)*, the module adds up to ~$40M. FERC's readiness requirements and deposits are designed to filter out speculative requests, so this pool should shrink.
- *Total.* About $70M of spend at 100% share. At a ~30% share (fragmented buyers, low switching costs before audits), realistic ARR is **~$20M** *(inference)*.

**Revenue shape.** Elephants, with Janz's table divided by 10: $100M needs 1,000 customers at $100k. This market has about 400 sites and fewer than 500 owning companies. A handful of hyperscalers dominate, and they can build the capability in-house.

**Bull.** Compliance is mandatory and enforceable, and the registration clock starts in 2027. The per-site price can climb as Phase 2 standards arrive. Ride-through requirements are next on NERC's roadmap ([NERC FAQ, Aug 2026](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/large-loads-faqs.pdf)).

**Bear.** $100M ARR would need ~$330M of annual spend at 30% share. That is about 3,300 sites at $100k, eight times the sites in scope. Even 100% of today's spend (~$70M) falls short. The FERC orders "do not ... impose immediate obligations on individual customers, or apply to areas of the country not governed by those RTOs/ISOs" ([Foley, Jun 2026](https://www.foley.com/insights/publications/2026/06/ferc-issues-six-tailored-show-cause-orders-to-accelerate-large-load-interconnection/)). The FERC half of the rules therefore lands mostly on RTOs and utilities, not on data centres.

**Generational reading.** $1bn needs 10,000 customers at $100k. The market holds about 4% of that customer count. It misses by about two orders of magnitude.

**Venture outcome.** Realistic ARR is ~$20M (above).
- I found no same-buyer comparable with an EV/revenue multiple. The closest same-buyer exit is Certrec: NERC compliance for power generators, acquired by Mirion for $81M at 16.9x EV/'25E EBITDA ([Mirion, Jul 2025](https://www.mirion.com/news/mirion-acquires-certrec)). No revenue multiple was disclosed. The reading is **unpriced** on same-buyer comparables.
- As a cross-buyer bound, two regulatory-compliance software deals give revenue multiples:
  - Conversia: €121.6M for €36.6M revenue, 3.3x ([Wilmington RNS, Aug 2025](https://www.investormeetcompany.com/companies/wilmington-plc/rns/4293226/view)) *(inference: price ÷ revenue)*. Subscription GRC for SMEs, ~25% EBITDA margin.
  - Wolters Kluwer FRR: €450M for €123M revenue, 3.7x ([NKP, 2025](https://www.mainsights.io/articles/grc-saas-platforms-transaction-multiples-and-consolidation-trends)). Bought by a strategic acquirer.
- At the lower 3.3x, the exit is ~$66M. At NKP's 7–10x GRC range, the exit is ~$200M. Both are far below $1bn.

**Forward reading** *(forward)*. The horizon is 2032.
- *Pipeline math.* Data Center Index tracks 739 campuses in all stages ([2026](https://datacenterindex.ai/pipeline)). Bisnow projects 280 campuses of ≥100 MW by 2030 ([Sep 2026](https://www.bisnow.com/news/national/data-center-development/large-scale-us-data-centers-projected-triple-by-2030)). That gives 280–740 sites × $75k = $21–55M at 100% share, or $6–17M at 30%.
- *Shadow-spend conversion.* A compliance tool saves up to 2.5 FTE per entity ([POWER, 2016](https://www.powermag.com/automated-compliance-tracking-solution-right/); old vendor-adjacent claim). At $150k per loaded FTE *(assumption)*, that is $375k per site. 740 × $375k × 30% = **~$83M**. This is an upper bound: it needs every tracked campus built and the full 2.5 FTE replaced.
- Neither method clears $100M. The market is small, not early.

**Score.** $100M ceiling: -4. The bear case clearly outweighs, because even 100% of plausible spend sits below the ceiling. The score is not -5, because Phase 2 standards and shadow-spend conversion could close part of the gap. Generational: -5, short by about two orders of magnitude. Venture outcome: -5, an exit of about $66–200M on the available comparables.

### 2. US first — +3 (high)

**Bull.** The rules are US-native: FERC under the Federal Power Act, and NERC under FERC authority ([NERC webinar, 2026](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/20260713_registration_cle-registration-update-webinar.pdf)). The US holds the bulk of the world's data-centre buildout. ERCOT alone tracks ~474 GW of large-load requests, ~90% of them data centres ([Seyfarth, Jul 2026](https://www.seyfarth.com/dir_docs/documents/presentation-slides/260729-Energy-Webinar-CLE-Material-Around-the-Grid-Texas-Data-Centers-Power-Policy.pdf)).

**Bear.** The same fact cuts the other way. Rule-specific software does not transfer abroad without a rebuild. Canada and parts of Mexico come under NERC, but they add few sites.

**Score.** +3. The US is the right and only launch market. The non-transferability is the named limit.

### 3. Adjacencies — +1 (low)

**Bull.** By year 3, the company would hold each site's verified steady-state, dynamic and short-circuit models. It would also hold its disturbance-monitoring data, and a map of every transmission owner's and planning coordinator's requirements. CLO-001 requires those models and per-entity interconnection requirements ([NERC CLO-001-1](https://www.nerc.com/globalassets/standards/projects/2026-02/final-ballots/project-2026-02-computational-loads-clo-001-1-final-redline.pdf)). Two products follow:
- **Flexible-load operations.** FERC's orders create "new transmission services for flexible large loads" ([FERC, 2026](https://ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration)). Responding to operating instructions is already part of CLO-002 ([NERC FAQ](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/large-loads-faqs.pdf)).
- **Utility-side tooling.** Transmission owners must document their own CLO interconnection requirements (R1).

**Bear.** Flexibility and siting already have funded players. GridCARE raised a $64M Series A in May 2026 ([mgrid, 2026](https://mgrid.org/2026/05/14/gridcare-raises-64-million-to-cut-ai-data-center-grid-connection-waits-from-years-to-months/)). Utility interconnection software has GridUnity, backed by a $49.5M DOE grant ([GridUnity, 2024](https://www.gridunity.com/resources/power-grid-international-renewable-energy-world-gridunity-selected-to-receive-nearly-50m-in-federal-funds-for-its-solution-to-speed-up-interconnection)). Whether the compliance data asset transfers into real-time control is unproven *(inference)*.

**Score.** +1. The asset leads to a plausible next product, but incumbents in that adjacency are funded, and the link is not sourced.

## Truth

### 4. Market dynamics — -2 (medium)

**Classification: both.** It is untapped among data centres, because no data centre has ever been NERC-registered. The reason the gap exists is sourced: the registry category and the CLO standards are new, and are due by end-2026 ([NERC FAQ, Aug 2026](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/large-loads-faqs.pdf)). It is crowded among vendors, who saw the rule coming.
- **Certrec** (Mirion) already markets a computational-load compliance offer. It runs NERC programs for 130+ registered entities ([Certrec, 2026](https://www.certrec.com/nerc-compliance/computational-load-standards/)).
- **GridStrong** raised a $10M seed in Sep 2025. Its co-founder is NERC's former engineering director, it already serves "load" owners, and it has more than half of the top 25 renewable owners as customers ([PR Newswire, 2025](https://www.prnewswire.com/news-releases/gridstrong-secures-10m-in-seed-funding-to-automate-grid-compliance-and-reliability-302558254.html)).
- **Vela Energy** (YC W26, $1.3M pre-seed) builds agents for large-load interconnection studies ([YesPress, Jul 2026](https://yespress.io/vela-yc-w26)).
- **ArcusAI** sells interconnection-application software for data centres ([PR Newswire, 2025](https://finance.yahoo.com/news/arcusai-ai-powered-platform-speeds-132000622.html)).
- **Consultancies** already sell CLO readiness: Elevate ([Elevate, Aug 2026](https://www.elevate.energy/post/what-data-center-developers-need-to-know-about-nerc-s-new-computational-load-standards)) and Van Gheem ([VGC](https://vangheemconsulting.com/large-loads-computational-loads/)).

**Wedge.** A data-centre-native product for colocation firms and neoclouds that have no utility-grade compliance staff. It would pair model verification against as-built equipment with CLO-002 operating-instruction evidence.

**Year-3 asset.** A requirements library across every TO, DP, PC and TP that serves data centres, with verified per-site models *(inference)*.

**Bear.** GridStrong and Certrec already hold the NERC compliance workflow and the trust. A well-funded competitor could copy the requirements library within about a year. Hyperscalers may hire the capability in-house.

**Score.** -2. The gap is real and dated, but two credible incumbents moved first, and the year-3 asset is copyable.

### 5. Problem size — -2 (medium)

**Bull.** The surrounding problem is huge. Interconnection waits "routinely run three to seven years" in congested regions ([mgrid on GridCARE, 2026](https://mgrid.org/2026/05/14/gridcare-raises-64-million-to-cut-ai-data-center-grid-connection-waits-from-years-to-months/); vendor-adjacent). NERC penalties can reach $1M per day per violation ([City of Columbia memo](https://www.como.gov/Council/Commissions/downloadfile.php?id=20419); undated).

**Bear.** The compliance problem itself is small. About 400 sites × $100k–$250k all-in spend is $40–100M a year across the market *(inference from the [AuditXYZ](https://www.auditxyz.com/frameworks/industry-specific/nerc-cip) range; weak source)*. The expensive problem, speed to power, is solved by physics, siting and capital, not compliance software.

**Score.** -2. The spend this product would address is too small for a $100M company, although the adjacent problem is large.

### 6. Pain depth — +2 (medium)

**Bull.** The obligations are mandatory and enforceable, with a deadline: FERC directed NERC to file standards and registry criteria by 31 December 2026 ([Certrec, 2026](https://www.certrec.com/nerc-compliance/computational-load-standards/)). Data-centre owners face recurring obligations: modeling data at least every 13 months, disturbance monitoring, and operator training ([Elevate, 2026](https://www.elevate.energy/post/what-data-center-developers-need-to-know-about-nerc-s-new-computational-load-standards)). The budget line already exists at generators as NERC compliance spend: consultants, software and staff ([Utility Services](https://www.utilitysvcs.com/services/nerc-compliance-program-development/)).

**Bear.** In year 1, buyers will likely buy consultants, not software. Registration only begins in 2027, and the first audits come later. Software is easier to defer than a consultant who signs the registration *(inference)*.

**Score.** +2. The pain is mandated and recurring. Consultants will absorb the first wave of the budget.

### 7. Repeatability — +1 (medium)

**Bull.** Every customer faces the same three standards (CLO-001/002/003), the same 50 MW/100 kV threshold, and the same buyer type ([NERC webinar, 2026](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/20260713_registration_cle-registration-update-webinar.pdf)).

**Bear.** Interconnection requirements "differ for each entity" (TO, DP, GO) ([Elevate, 2026](https://www.elevate.energy/post/what-data-center-developers-need-to-know-about-nerc-s-new-computational-load-standards)). Each planning coordinator defines "qualified change" ([NERC FAQ, Oct 2026](https://www.nerc.com/globalassets/standards/projects/2026-02/final-ballots/project-2026-02-faq---october-2026.pdf)). FERC leaves each RTO room to define large loads ([Foley, 2026](https://www.foley.com/insights/publications/2026/06/ferc-issues-six-tailored-show-cause-orders-to-accelerate-large-load-interconnection/)). Each new utility territory therefore needs new configuration.

**Score.** +1. The core workflow repeats. The per-territory requirements add integration cost to every deal.

### 8. Tailwinds — +3 (medium)

**Bull.**
- *Regulation.* NERC's Phase 2 standards begin in 2027, and ride-through requirements are a high priority ([NERC FAQ, Aug 2026](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/large-loads-faqs.pdf)).
- *Buildout.* Large campuses are projected to triple by 2030 ([Bisnow, 2026](https://www.bisnow.com/news/national/data-center-development/large-scale-us-data-centers-projected-triple-by-2030)).
- *Queues.* ERCOT's queue grew by 178 GW in one quarter ([ERCOT, Apr 2026](https://www.ercot.com/files/docs/2026/04/13/9-Interconnection-and-Grid-Analysis-Update.pdf)).

**Bear.** Queue growth is not buildout. "A queue request is not a forecast ... or a construction commitment" ([Seyfarth, 2026](https://www.seyfarth.com/dir_docs/documents/presentation-slides/260729-Energy-Webinar-CLE-Material-Around-the-Grid-Texas-Data-Centers-Power-Policy.pdf)). Community opposition has derailed dozens of projects ([Bisnow, 2026](https://www.bisnow.com/news/national/data-center-development/large-scale-us-data-centers-projected-triple-by-2030)). The regulatory tailwind helps incumbent NERC vendors as much as entrants.

**Score.** +3. Regulation is ratcheting in one direction. An AI capex pullback is the visible headwind.

## Speed

### 9. Learning speed — -2 (low)

**Buyer and user.** The buyer is the VP of energy or power, or the compliance lead, at a data-centre owner or operator. The users are compliance and electrical engineers.

**Bull.** The 2027 registration deadline forces decisions. Colocation firms and neoclouds without in-house NERC staff could become design partners quickly *(inference)*.

**Bear.**
- This is a slow loop. The buyer is not the user, and the value shows at audits, quarters or years after purchase.
- The customer count is small (~400 sites, concentrated owners), so each lost deal is expensive.
- I found no sourced sales cycle for this buyer. An enterprise cycle of 3–9 months would allow about **2–4 learning cycles in 18 months** *(assumption)*.

**Network.** A founder with ex-NERC or utility-compliance credentials, or an existing data-centre operator relationship, would move this to about 0. GridStrong's founding team shows that this credential is the norm in the category.

**Score.** -2. The deadline urgency is a named mitigation, but the loop is procurement-gated and the value is slow to prove.

## What would move the score

- **Axis 1 ($100M path).** The score improves if the realistic price per site exceeds ~$250k a year (software plus managed modeling), or if utilities buy too. To test this, quote three colocation or neocloud compliance leads a $150k-per-site managed CLO program this week. Ask them what Certrec or Elevate quoted them. One sourced count of sites meeting the 50 MW/100 kV test would also replace the tracker estimate. Ask one RTO, or look in NERC's registration materials when published.
- **Axis 4 (dynamics).** Find out whether GridStrong and Certrec already have data-centre customers. To test this, ask two data-centre energy leads who they are talking to for CLO readiness.
- **Axis 9 (speed).** A sourced sales cycle would firm up the score. Ask three prospects: "If registration opened in January, when would you sign, and who must approve it?"

---

## Run log

- Vault queries: none. The followed skill (pre-vault version) gives no vault instruction, so I did not query the second-brain service. 0 queries, 0 results.
- Exa 1, web_search: FERC large-load interconnection rule (RM26-4, June 2026 show-cause orders). 6 results.
- Exa 2, web_search: large-load interconnection request counts and queues (ERCOT, LPPC, Watt Street). 6 results.
- Exa 3, web_search: startups and incumbents in data-centre interconnection and compliance software (GridStrong, Vela, ArcusAI, GridCARE, GridUnity). 8 results.
- Exa 4, web_search: NERC large-load registration and CLO standards. 6 results.
- Exa 5, web_fetch: NERC registration webinar (July 2026) and NERC Large Loads FAQ (Aug 2026). 2 pages.
- Exa 6, web_search: count of US data centres ≥50 MW (Data Center Index, Bisnow, Aterio, FieldProspects, dcmap). 6 results.
- Exa 7, web_search: NERC compliance program costs (AssurX memo, AuditXYZ, POWER 2016). 6 results.
- Exa 8, web_search: energy and utility compliance software acquisitions and multiples (Certrec/Mirion, Hansen/powercloud). 6 results.
- Exa 9, web_search: regulatory compliance software EV/revenue multiples (NKP GRC, Conversia, Admincontrol, NAVEX). 6 results.
- Exa 10, web_search: consultancies and vendors offering data-centre NERC readiness (Certrec, Elevate, Van Gheem). 7 results.
- Total Exa calls: 10 of 10.
