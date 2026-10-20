# Market evaluation: compliance software for US data centres under the new large-load interconnection rules

**Assumptions:** The customer and buyer is the owner or operator of a US data centre site that falls under the new rules. The user is that company's grid, energy or compliance engineer. The geography is the US: NERC also covers Canada, but FERC and RTO rules are US only. The product is SaaS, with expert-assisted workflows, covering four things: NERC registration as a Computational Load Owner or Operator, evidence for the three new CLO standards (modelling data, operational communications, disturbance monitoring), RTO/utility large-load tariff obligations, and interconnection study data. The ceiling is the user's: **$100M ARR in under 10 years**.

**Verdict:** Under the $100M ceiling, **Scale fails** (axis 1, -4), **Truth passes** (lowest: 4. Market dynamics and 5. Problem size, both -2), and **Speed fails** (9. Learning speed, -3). The generational bar ($1bn) and the venture-outcome bar ($1bn exit) both fail Scale at -5. The weakest axis is 1. The regulation is real, mandatory and well timed. But it covers roughly 280–850 sites owned by a few dozen companies, so the bottom-up ceiling today is about $8M–$64M, below $100M even at 100% share. The forward reading does not clear $100M either, except under an upper bound that stacks every favourable assumption. So the market is small, not early. It suits a capital-efficient compliance business or a feature for a broader grid-compliance platform. It does not suit a standalone venture bet.

| Test | Axis | Score | Confidence |
|---|---|---|---|
| Scale | 1. $100M ARR path | custom ($100M) -4 · generational -5 · venture outcome -5 | medium |
| Scale | 2. US first | +4 | high |
| Scale | 3. Adjacencies | +1 | medium |
| Truth | 4. Market dynamics | -2 | medium |
| Truth | 5. Problem size | -2 | medium |
| Truth | 6. Pain depth | +2 | medium |
| Truth | 7. Repeatability | +1 | medium |
| Truth | 8. Tailwinds | +3 | high |
| Speed | 9. Learning speed | -3 | medium |

Scale: FAIL $100M (1, -4) · FAIL generational (1, -5) · FAIL venture outcome (1, -5) · Truth: PASS (lowest: 4 and 5, -2) · Speed: FAIL (9. Learning speed, -3)

**What the rules are (as of 20 Oct 2026).** "The new large-load interconnection rules" is three layers:
- **NERC registration and standards.** NERC is creating two new registered entity types, Computational Load Owner and Computational Load Operator. They apply to sites of ≥50 MW connected at ≥100 kV. The NERC Board approved the criteria on 8 Oct 2026 ([NERC Q3 2026 update](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/llap-quarterly-update-q3-2026.pdf)). Three standards come with them: CLO-001-1 (interconnection, studies and modelling data), CLO-002-1 (operational data and communications) and CLO-003-1 (protection coordination and disturbance monitoring). They go to FERC in Q4 2026 under a FERC deadline of 31 Dec 2026 ([NERC Large Loads FAQ, Aug 2026](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/large-loads-faqs.pdf); [Q3 update](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/llap-quarterly-update-q3-2026.pdf)).
- **FERC show-cause orders.** On 18 June 2026, FERC ordered all six RTOs/ISOs to justify or reform their large-load tariffs ([FERC](https://ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration)). Those orders "do not … impose immediate obligations on individual customers" ([Foley, June 2026](https://www.foley.com/insights/publications/2026/06/ferc-issues-six-tailored-show-cause-orders-to-accelerate-large-load-interconnection/)).
- **RTO and utility tariffs.** These are already being approved. Examples are PJM's Large Load definition and Large Load Registry (50 MW, effective 12 Oct 2026) ([FERC order ER26-3515](https://www.pjm.com/pjmfiles/directory/etariff/FercOrders/9207/20261009-er26-3515-000.pdf)) and Duke's large-load NITSA provisions ([Utility Dive, Oct 2026](https://www.utilitydive.com/news/ferc-duke-energy-large-load-tariff-nitsa/832847/)).

The NERC layer is the only one that puts a direct, enforceable compliance obligation on the data centre itself. So the evaluation treats it as the core of the market.

**Vault:** The vault has no notes on data centres, FERC, NERC or grid interconnection. Searches for "data center interconnection", "interconnection queue", "grid compliance", "FERC", "electricity grid", "regulatory tailwind" and "AI capex" returned 0 relevant hits. The vault claims below come from the framework notes (concept pages built on [[How to Think About Market Selection]]).

## Scale

### 1. $100M ARR path — custom ($100M) -4 · generational -5 · venture outcome -5 (medium)

**Customers.** NERC estimates that the 50 MW / 100 kV threshold covers **~68,288 MW** of computational load by end-2027. That is 86% of 79,502 MW: 41,827 MW active as of June 2026 plus 37,675 MW under construction ([NERC technical reasoning, Aug 2026](https://www.nerc.com/globalassets/who-we-are/rules-of-procedure/proposed/august-posting-technical-reasoning.pdf)). NERC gives megawatts, not a site count. To turn megawatts into sites:
- The average new US facility in 2025 was ~80 MW, per FERC's 2025 State of the Markets, as summarised by [ITK Research (May 2026)](https://itkservices3.com/background/data_centres_usa). This is secondary; I did not check FERC's own page.
- Sightline's ≥50 MW pipeline is 190 GW across 777 projects, an average of ~245 MW, per [MMCG (Sept 2026)](https://www.mmcginvest.com/post/u-s-data-center-industry-report-2026-two-industries-under-one-name).

68,288 MW ÷ 245 MW ≈ **280 sites**, and 68,288 MW ÷ 80 MW ≈ **850 sites** *(inference)*. The 80 MW average includes sub-50 MW sites, so 850 is generous.

**Buyers are fewer than sites.** [Data Center Index](https://datacenterindex.ai/operators) tracks 65 operators across 519 campuses. Hyperscale is 81.6% of pipeline megawatts ([MMCG census, June 2026](https://www.mmcginvest.com/post/the-u-s-data-center-census-2026)).

**Price per site.** I found no published price for data-centre NERC compliance software, so the price is an *(assumption)* anchored on shadow labour:
- FERC's burden estimates use a loaded engineer and clerk rate of $66.72/hour (BLS 2023) ([FERC, Federal Register, Apr 2024](https://www.govinfo.gov/content/pkg/FR-2024-04-30/pdf/2024-09288.pdf)).
- Assume a site needs 0.5 FTE of ongoing compliance work: 1,040 h × $66.72 ≈ **$69k/year of shadow spend** *(assumption × sourced rate)*.
- A subscription that captures roughly half to all of that is **$30k–$75k per site per year** *(assumption)*.

**Ceiling today** *(inference)*:
- Low: 280 sites × $30k = **$8.4M**
- Mid: 500 × $50k = **$25M**
- High: 850 × $75k = **$64M**

**Shape.** Elephants by buyer, deer by site. Under the $100M ceiling the shapes table divides by 10, so the bar is 1,000 customers at $100k or 10,000 at $10k. This market has 280–850 sites, and far fewer buying companies.

**Bull.** The obligation is mandatory and covers almost all of the load: 86% of data-centre megawatts ([NERC](https://www.nerc.com/globalassets/who-we-are/rules-of-procedure/proposed/august-posting-technical-reasoning.pdf)). More standards are already queued: disturbance performance/ride-through, event reporting and model validation SARs are in progress for 2027 ([NERC Q3 update](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/llap-quarterly-update-q3-2026.pdf)). So the price per site could rise as the requirement list grows. Penalties can exceed $1M per day per violation ([Energize Capital, 2025](https://energizecap.com/insights/why-we-invested-in-gridstrong); an investor blog, weak).

**Bear.** Even the high case ($64M) is below $100M at 100% share. NERC raised the threshold from 20 MW / 60 kV to 50 MW / 100 kV after 44 commenters, including Google, Microsoft, Oracle and Crusoe, pushed back ([NERC technical reasoning](https://www.nerc.com/globalassets/who-we-are/rules-of-procedure/proposed/august-posting-technical-reasoning.pdf); [response to comments](https://www.nerc.com/globalassets/who-we-are/rules-of-procedure/proposed/response-to-comments-document-for-august-posting.pdf)). That lobbying shrank the covered population. The buyer base is concentrated in hyperscalers, the companies most able to build compliance in-house. The vault flags a "structurally capped number of buyers" as a fatal criterion, and treats concentrated buyers as acceptable only when their budgets and decision speed make up for it (`Concepts/Control Point.md` › "Open questions / contradictions", chunk `6bd70c4ee8393e59f2b1851f`; `Concepts/Venture Scale.md` › "Related", chunk `6f856f08eb85772ea860c3d7`).

**Venture outcome.** Realistic ARR = ceiling × 30% *(inference)*: $2.5M (low), $7.5M (mid), $19M (high). Use 30% at most, not less. The market is not low-switching-cost, but GridStrong and others already compete (axis 4).

The multiple comes from public energy and utilities software comparables on [Multiples.vc](https://multiples.vc/energy-utilities-software-valuation-multiples) (sector page updated Sept 2026):
- **PSI Software: 2.5× EV/LTM revenue.** Grid and energy operations software with a thin EBITDA margin (46× EV/EBITDA implies low profitability).
- **Energy One: 6.0×.** Energy trading SaaS with higher recurring revenue and margin.

The two disagree, so I use the lower: 2.5×. The high case gives $19M × 2.5 ≈ **$48M exit** *(inference)*. Even at 6.0×, the exit is ~$114M.

The closest deal is [Mirion's 2025 purchase of Certrec](https://www.mirion.com/news/mirion-acquires-certrec), a NERC/NRC compliance software-and-services firm serving 80+ NERC entities, for $81M at 16.9× EBITDA. That price reflects strategic fit (nuclear) and recurring revenue. Revenue was not disclosed, so it gives no EV/revenue figure. But it shows the size of exits in compliance. Fails $1bn by more than an order of magnitude.

**Forward reading** *(forward)*. NERC's Level 2 Alert data reports load "may increase by 300 GW between 2028 and 2030", mostly data centres ([NERC technical reasoning](https://www.nerc.com/globalassets/who-we-are/rules-of-procedure/proposed/august-posting-technical-reasoning.pdf)). This figure is self-reported by transmission owners. I found **no sourced conversion rate** from that forecast to built load. The 89–92% pre-committed share ([ITK, citing C&W and JLL](https://itkservices3.com/background/data_centres_usa)) applies only to capacity already under construction, which the 2027 figure already counts. Attrition is real: Stargate Abilene's planned 600 MW expansion was cancelled in March 2026 after grid delivery delays ([ITK](https://itkservices3.com/background/data_centres_usa)).

Even at 100% conversion, with 86% registrable, the arithmetic is:
- 300,000 MW × 0.86 ÷ 245 MW ≈ 1,050 more sites, so ~1,330 total × $50k ≈ $67M ceiling, and ~$20M at 30% share.
- The extreme upper bound is 80 MW sites at $75k: ~4,075 sites ≈ $306M ceiling, and ~$92M at 30% share.

That upper bound stacks full conversion, the smallest sites, the top price and the maximum share, and it still lands just under $100M by 2030. The forward reading does not clear the ceiling on any realistic input.

**Score.**
- **Custom $100M: -4.** The bottom-up ceiling is below $100M before any share is applied. The bull case rests on an unpriced, assumed per-site price rising several-fold.
- **Generational: -5.** The ceiling is 1–6% of $1bn.
- **Venture outcome: -5.** ~$48M on the lower sourced multiple, and ~$114M on the higher.

### 2. US first — +4 (high)

**Bull.** The obligation is created in the US: FERC directed NERC under FPA §215(d)(5) ([NERC Q3 update](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/llap-quarterly-update-q3-2026.pdf)). The US also has the load: NERC counts 41.8 GW of active data-centre load ([NERC technical reasoning](https://www.nerc.com/globalassets/who-we-are/rules-of-procedure/proposed/august-posting-technical-reasoning.pdf)), and ITK puts the US at 55% of global hyperscale capacity, per Synergy ([ITK](https://itkservices3.com/background/data_centres_usa)).

**Bear.** The US is a patchwork. There are six RTO tariffs from the show-cause orders. Non-RTO utilities such as Duke file their own rules ([Utility Dive](https://www.utilitydive.com/news/ferc-duke-energy-large-load-tariff-nitsa/832847/)). And each Planning Coordinator defines "Qualified Change" for itself ([NERC Project 2026-02 FAQ](https://www.nerc.com/globalassets/standards/projects/2026-02/formal-posting-1/formal-posting-1/project-2026-02-faq---august-19-2026.pdf)).

**Score.** The US is the only sensible launch market. The patchwork is a cost, not a reason to start elsewhere.

### 3. Adjacencies — +1 (medium)

**Year-3 asset.** Per-site dynamic load models, plus disturbance-monitoring data (SER/FR/DDR) for each site, under a documented chain of custody. CLO-003-1 requires this monitoring data ([NERC FAQ](https://www.nerc.com/globalassets/standards/projects/2026-02/formal-posting-1/formal-posting-1/project-2026-02-faq---august-19-2026.pdf)).

**Next products.**
1. **Flexible-load qualification.** DOE's ANOPR asks whether curtailable loads get faster studies, possibly within 60 days ([FERC RM26-4](https://ferc.gov/rm26-4)). FERC's orders also call for "new transmission services for flexible large loads" ([FERC](https://ferc.gov/news-events/news/ferc-launches-aggressive-targeted-action-speed-large-load-integration)). Verified telemetry and curtailment evidence is the same data asset.
2. **Utility-side study tooling.** Transmission owners and planning coordinators must study these loads: 324 TOs and 62 PCs were registered as of Feb 2024 ([FERC](https://www.govinfo.gov/content/pkg/FR-2024-04-30/pdf/2024-09288.pdf)).

**Bull.** The model and event data lead straight to "prove you are flexible, connect faster", which is speed-to-power money, not compliance money.

**Bear.** Flexibility orchestration already has a well-funded owner: Emerald AI, with $68M from NVIDIA, Eaton and GE Vernova, per a competitor's page ([Veriprajna](https://veriprajna.com/solutions/data-center-grid-interaction); a vendor source, weak). On the utility side, GridStrong already sells model management to generators and transmission owners ([GridStrong](https://www.gridstrong.ai/)).

**Score.** The asset transfers, but both named adjacencies have a funded incumbent.

## Truth

### 4. Market dynamics — -2 (medium)

**Classification: both.** No one had to serve data centres as NERC registrants before, and the reason the gap exists is a regulation that changed in 2026 ([NERC FAQ](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/large-loads-faqs.pdf)). That is a valid why-now. Your vault lists regulatory change as one of five why-now mechanisms, and asks "would this have plausibly failed two years ago?" (`Concepts/Why Now.md` › "Summary", chunk `ff42ec2de4806f1076fa6a69`). Here it would have: no obligation existed.

The space is already crowded on day one:
- **[GridStrong](https://www.gridstrong.ai/customers/data-centers)** has a dedicated data-centre offering. It raised a $10M seed in 2025, its co-founder is NERC's former Director of Engineering, and it serves half of the top-25 renewable owners ([PR Newswire, Sept 2025](https://www.prnewswire.com/news-releases/gridstrong-secures-10m-in-seed-funding-to-automate-grid-compliance-and-reliability-302558254.html)).
- **Point and adjacent tools:** [data phleet](https://www.dataphleet.com/news/f/introducing-automated-nerc-prc-019-2-compliance-check/), [ARCSUSA](https://arcsusa.com/) and [EnergyAtIt](https://energyatit.com/solutions/data-center-grid-connectivity).
- **Services firms:** [Veriprajna](https://veriprajna.com/solutions/data-center-grid-interaction), and Certrec, now part of Mirion ([Mirion](https://www.mirion.com/news/mirion-acquires-certrec)).

**Wedge.** Build on the data-centre side of the meter. Integrate with DCIM, BMS and UPS systems to produce CLO-003 monitoring evidence and validated load models. Generator-focused tools start from SCADA and plant models instead.

**Year-3 asset a funded competitor cannot copy.** A cross-site library of measured disturbance responses, tied to specific UPS and power-supply configurations.

**Bear.** GridStrong has the same standards expertise, an earlier start and a data-centre page. Hyperscalers, who dominate the buyer pool, can staff this in-house. Your vault names "better execution" as the answer that does not count when others are already in the space (`Concepts/Tarpit Market.md` › "What we know", chunk `d3974be09ebeaf718dee25b8`).

**Score.** The why-now is real. But the wedge is thin against a better-credentialed first mover, and the largest buyers can build it themselves.

### 5. Problem size — -2 (medium)

**Bull.** The underlying problem, speed to power, is enormous: 79.5 GW expected by 2027 ([NERC](https://www.nerc.com/globalassets/who-we-are/rules-of-procedure/proposed/august-posting-technical-reasoning.pdf)), and projects are being cancelled over grid delivery ([ITK](https://itkservices3.com/background/data_centres_usa)). FERC has levied ~$900M in penalties since 2007, including $46M in 2024 ([Energize Capital](https://energizecap.com/insights/why-we-invested-in-gridstrong); an investor blog, weak).

**Bear.** The compliance problem this product solves is small. ~500 sites × ~$69k of shadow labour ≈ **$35M/year** across the market *(inference from the axis-1 inputs)*. Big-4 strategy engagements reportedly run $500k–$2M ([Veriprajna](https://veriprajna.com/solutions/data-center-grid-interaction); a vendor source, weak). That cost is per project, not recurring per site.

**Score.** Compliance is a thin slice of a large speed-to-power problem, and the slice itself is tens of millions of dollars.

### 6. Pain depth — +2 (medium)

**Bull.** The pain is mandatory and dated. A newly registered entity "should be audit-ready on the day it is registered", and building a compliance programme takes 6–12 months ([WECC new-entity package, 2023](https://www.wecc.org/sites/default/files/documents/program/2024/Generator%20Welcome%20Package.pdf); written for generators, the closest analogue). The line item exists: regulatory or energy compliance headcount, or consultants. Your vault's pull test, "name the budget line or the shadow spend you replace", passes (`Concepts/Market Pull.md` › "Summary", chunk `adb6840c45cdcb2677176edd`).

**Bear.** For a hyperscaler, compliance cost is a rounding error next to campus capex. Enforceable dates are not set yet: FERC approval is pending ([NERC Q3 update](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/llap-quarterly-update-q3-2026.pdf)). And mandated spend can be "real and unreachable" when the buyer prefers in-house staff or incumbents. That is an open question in the vault (`Concepts/Market Pull.md` › "Open questions / contradictions", chunk `8de1106e1125c8390cddf8e7`).

**Score.** There is a legal mandate and a budget line, but the pain is small compared with the buyer's other costs.

### 7. Repeatability — +1 (medium)

**Bull.** The same three CLO standards apply to every registered site continent-wide ([NERC FAQ](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/large-loads-faqs.pdf)). Winning one hyperscaler opens many sites, so land-and-expand works.

**Bear.**
- Planning Coordinators define their own "Qualified Change" ([NERC FAQ](https://www.nerc.com/globalassets/standards/projects/2026-02/formal-posting-1/formal-posting-1/project-2026-02-faq---august-19-2026.pdf)).
- Thresholds differ by region: PJM 50 MW, SPP 50 MW, Tri-State 45 MW ([FERC ER26-3515 order](https://www.pjm.com/pjmfiles/directory/etariff/FercOrders/9207/20261009-er26-3515-000.pdf)), and Duke's shortfall payments apply at 100 MW ([Utility Dive](https://www.utilitydive.com/news/ferc-duke-energy-large-load-tariff-nitsa/832847/)).
- Site hardware is heterogeneous (UPS, power supplies, DCIM). Multi-tenant colocation sites add per-tenant complexity ([Veriprajna](https://veriprajna.com/solutions/data-center-grid-interaction); weak).

**Score.** The standards core repeats from site to site. The regional and hardware layer does not.

### 8. Tailwinds — +3 (high)

**Bull.** Three forces help:
1. **Regulation keeps stacking.** FERC directed NERC on 16 July 2026, and further SARs (ride-through, event reporting, model validation) are queued for 2027 ([NERC Q3 update](https://www.nerc.com/globalassets/initiatives/large-loads-action-plan/llap-quarterly-update-q3-2026.pdf)).
2. **Load roughly doubles by 2027,** from 41.8 GW to 79.5 GW ([NERC](https://www.nerc.com/globalassets/who-we-are/rules-of-procedure/proposed/august-posting-technical-reasoning.pdf)).
3. **Reliability incidents keep the regulators pressing.** NERC cites Virginia and Texas grid events where data-centre load amplified instability ([NERC letter to FERC, Mar 2026](https://www.nerc.com/globalassets/who-we-are/legal--regulatory/filings--orders/nerc-filings-to-ferc/2026/nerc_accelerated-ll-action-plan_rm26-4_signed.pdf)).

**Bear.** Industry lobbying already shrank the scope once, when the threshold rose from 20 MW to 50 MW. The tailwinds help GridStrong and in-house teams as much as an entrant.

**Score.** The forces are strong and sourced, but they are not exclusive to an entrant.

## Speed

### 9. Learning speed — -3 (medium)

**Buyer.** The VP or director of energy, power or grid interconnection at a hyperscaler, colocation provider or developer. Procurement and legal review gate the deal.

**User.** Electrical and compliance engineers.

**Sales cycle.**
- Enterprise deals typically take 6–12 months ([ZoomInfo, citing a 2026 benchmark](https://pipeline.zoominfo.com/sales/enterprise-sales-cycle)).
- Data-centre deals often take 6–24 months ([Percepture, 2026](https://percepture.com/data-centers-insights/data-center-marketing-guide/)).
- Both are vendor and marketing sources, so the evidence is weak.

**Feedback loop.** The value shows up at registration, audit and interconnection milestones, which are quarters away. The regulator sets the clock: the filing is due Q4 2026, then FERC approval, then implementation plans. That allows **about 1–2 learning cycles in 18 months**.

Your vault holds an open contradiction that bears on this market: "trust/compliance posture" is listed as a moat, while compliance-heavy markets are the slow-feedback ones. "The moat and the slow loop arrive together", and the guide leaves the trade to the founder (`Concepts/Moat.md` › "Open questions / contradictions", chunk `d8248a0d20aa42f8f6d5d2c8`).

**Bull.** Smaller buyers such as neo-clouds, crypto miners and independent colocation providers may buy faster. The crypto miners' "Computational Load Site" definition explicitly covers cryptocurrency mining ([NERC](https://www.nerc.com/globalassets/who-we-are/rules-of-procedure/proposed/computational-load-owner-or-operator-summary-of-changes-august-2026-posting.pdf)). A founder with a NERC or utility network would shorten the cycle. GridStrong's co-founder shows what that looks like. I do not assume the user has that network.

**Score.** The loop is slow, and the regulator, not the company, sets its pace. Without a named network, nothing mitigates that.

## What would move the score

- **Axis 1 ($100M path, -4).** The two unknowns are the true site count and the price per site.
  - Site count: when NERC's Section 1600 data request runs, it will name the CLO/CLOP candidates. Until then, use Aterio's dataset, which NERC licenses, to count ≥50 MW / ≥100 kV sites.
  - Price: the cheapest test this week is five calls with data-centre energy leads. Ask what they budget for NERC registration and CLO compliance, and whether they would pay $50k, $150k or $400k per site per year.
  - To clear $100M at 30% share with ~850 sites, the price must be ~$390k per site *(inference)*. If nobody says yes near that, the ceiling stands.
- **Axis 9 (learning speed, -3).** Test whether non-hyperscaler buyers (crypto miners in ERCOT, neo-clouds, independent colocation providers) will sign a paid pilot in under 90 days. Three such pilots would lift this to -1 or 0.
- **Axis 4 (dynamics, -2).** Ask two hyperscaler grid teams whether they plan to build CLO compliance in-house, buy GridStrong, or use consultants. One "in-house" answer from the top four confirms the bear case.

I can re-run this on a different reading of the market, for example: grid-compliance software for all bulk-power-system-connected assets (generators, IBRs, transmission owners and large loads), or flexibility verification for faster interconnection. Both likely have a larger ceiling.

---

## Run log

**Second-brain vault** (`POST /search`, limit 5; count = results returned):
- Domain queries:
  - "data center interconnection": 0
  - "large load": 5 (none relevant: CPU caches, Redis, ML)
  - "interconnection queue": 0
  - "grid compliance": 0
  - "FERC": 0
  - "data centre": 2 (none relevant)
  - "electricity grid": 0
  - "compliance software": 5 (framework notes only)
  - "regulatory tailwind": 0
  - "AI capex": 0
- Axis-lens queries: "market pull" 5, "control point" 5, "distribution asymmetry" 5, "speed of iteration" 5, "market depth" 5, "non-consensus" 5, "why now" 5, "tarpit" 5 (run twice), "venture scale" 5, "compliance moat" 5, "kingmaker buyers" 1.
- Re-ran "tarpit", "why now", "market pull", "speed of iteration" and "control point" (5 each) to read the full chunk text.
- `GET /chunks/{id}` on the 7 cited chunks: `6f856f08…`, `6bd70c4e…`, `d8248a0d…`, `ff42ec2d…`, `d3974be0…`, `adb6840c…`, `afcb15e8…`. All resolved. `_sources/` was not read.

**Exa (10 calls):**
1. web_search: FERC large-load interconnection rule 2026 (6 results)
2. web_search: NERC registration of large loads / Computational Load entities (6)
3. web_fetch: NERC Large Loads Action Plan Q3 2026 update PDF
4. web_search: number of sites / entities under NERC computational load registration (8)
5. web_search: competitors offering NERC compliance for data centres (8)
6. web_search: NERC compliance cost per newly registered entity / IBR analogue (6)
7. web_search: count of US data centre campuses >50 MW and hyperscaler share (8)
8. web_search: energy compliance software acquisitions and EV/revenue multiples (8)
9. web_search: GridStrong data-centre offering, funding and customers (6)
10. web_search: enterprise sales cycle for selling to data-centre operators (6)
