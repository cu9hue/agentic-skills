**Bar:** bootstrap. A profitable business you can run alone, reached from revenue within 12–18 months. Your income target is unknown, so I sized buyer pools at "a few dozen to a few hundred paying customers" *(assumed)*.
**Geography:** US (stated).
**Edge as capabilities:**
1. Pre-action limit checks: decide in milliseconds whether one actor may take one action, against limits shared across many accounts.
2. Deterministic replay: rebuild every input to a past decision, so an auditor, a counterparty or a regulator gets the exact reason.
3. Market microstructure: you know how auctions, order books and settlement windows get gamed, from the operator's side.
4. Agent failure modes: production harnesses taught you how agents retry, misread tool output, and act outside their brief.
5. Policy as code: you turn a written rule into checks that run deterministically.

Your edge statement is close to the definition your vault uses: an edge is judged against other founders, not colleagues (`Concepts/Edge.md` › What we know, chunk `fe3e7cd38743350dd3ba4a8b`). Few founders hold both (1) and (2) at production scale.

## Shifts

| Shift | Type | Date | Source |
|---|---|---|---|
| Nacha fraud-monitoring rules go live. Phase 1 covers all ODFIs and large originators. Phase 2 removes the volume threshold, so every non-consumer Originator, Third-Party Sender and TPSP must run "risk-based processes and procedures" to identify fraudulent entries and review them at least once a year. RDFIs must monitor incoming credits for the first time. | Rule / deadline | Mar 20, 2026; Jun 22, 2026 | [Nacha news](https://www.nacha.org/news/new-nacha-risk-management-rules-now-effect), [Nacha Phase 2](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2) |
| The GENIUS Act takes effect at the earlier of 18 months after enactment (Jul 18, 2025, so Jan 18, 2027) or 120 days after final rules. The OCC proposed its implementing rule; BSA/AML/OFAC rules come separately. | Rule / deadline | OCC NPRM Feb 25, 2026; effective by Jan 18, 2027 | [OCC Bulletin 2026-3](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-3.html) |
| Treasury proposes Section 3 rules on who may offer stablecoins to people "located in the United States", including location-detection evasion. | Rule | NPRM Aug 18, 2026; comments closed Oct 19, 2026 | [Federal Register](https://www.federalregister.gov/documents/2026/08/18/2026-16796/genius-act-regulations-on-payment-stablecoin-issuance-offer-and-sale) *(not opened)* |
| CFTC Enforcement advisory on insider trading and fraud in Kalshi event contracts. It says the Commission will police DCMs directly. | Scandal / scrutiny | Feb 25, 2026 | [CFTC 9185-26](https://www.cftc.gov/PressRoom/PressReleases/9185-26) |
| CFTC staff advisory 26-08 tells DCMs they must monitor all trading in real time and maintain audit trails for event contracts. | Scrutiny | Mar 12, 2026 | [CFTC Letter 26-08](https://www.cftc.gov/csl/26-08/download) |
| CFTC advance notice of proposed rulemaking on prediction markets. | Rule (pending) | Mar 16, 2026 | [CFTC 2026-05105](https://www.cftc.gov/LawRegulation/FederalRegister/proposedrules/2026-05105.html) |
| Kalshi plus Polymarket monthly volume rose from under $5B to about $24B. Asset-price contracts grow fastest. Nasdaq and Cboe filed to list binary contracts on equity indices. | Behaviour at scale | Sep 2025 → Apr 2026; Mar 2026 | vault: `Concepts/Prediction Market.md` › What we know, chunk `77098d0872b0df86144fb6b0` |
| First documented settlement manipulation on Polymarket's five-minute BTC contract: 821 wallets took $8.2M, and 93% of the losses fell on retail. | Failure / scandal | contract live Feb 12, 2026 | vault: `Concepts/Settlement Manipulation.md` › What we know, chunk `aa1929bd449cee05fb2828b7` |
| Mastercard Agent Pay for Machines launches with "authorization rules and spending limits that are programmatically enforced". More than 30 launch partners, including Stripe, Adyen and Coinbase. | New rail | Jun 10, 2026 | [Mastercard](https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html) |
| Amazon Bedrock AgentCore payments reaches GA. Its controls per payment session are a spend cap and an expiry, plus logs. | New rail | Aug 18, 2026 (preview May) | [AWS blog](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-payments-is-now-generally-available-enabling-agents-to-transact-safely-and-autonomously-at-scale/) (date opened; cap detail from search excerpt) |
| Visa Intelligent Commerce Connect is in pilot with spend controls. Partners include Highnote and Payabli. | New rail | Apr 8, 2026 | [Visa](https://corporate.visa.com/en/sites/visa-perspectives/newsroom/visa-intelligent-commerce-connect-ai-shopping-for-businesses.html) |
| ERCOT RTC+B goes live: ancillary services are co-optimized every five minutes, with state-of-charge duration rules for batteries and penalties for missed obligations. One large merchant storage owner stopped bidding day-ahead ancillary services. | Rule / market design | Dec 5, 2025 | [ERCOT](https://www.ercot.com/news/release/12052025-ercot-goes-live); [Canary Media](https://www.canarymedia.com/articles/batteries/texas-energy-market-redesign-battery-developers) *(not opened)* |

**Themes (undated):** "agents will spend money". This is the theme behind the rail launches above. Only the launches carry dates, so only they count as shifts.

**Lenses from your vault:**
- AP2 leaves "dispute-time retrieval" out of scope in v0.2 (`Concepts/Agent Mandate.md` › Open questions, chunk `204020c4194a25fb34239b91`). Liability is the stated blocker to adoption (`Concepts/Agentic Commerce.md` › What we know, chunk `a42cd8b7126994ed2403ff1e`). Visa TAP carries no mandate at all (`Sources/Visa Trusted Agent Protocol.md` › TL;DR, chunk `70eed31b30b569d325e3934b`). So the rails prove *who* acted, and the evidence of *why* is still unowned.
- Oversight fails on attention: people ignore flags that come often (`Concepts/Oversight Layer.md` › Summary, chunk `4626d184a9be750aea738d2c`). The same note says approval records could price insurance, which points to a buyer who carries the loss.
- Pull means you can name the budget line you replace (`Concepts/Market Pull.md` › Summary, chunk `adb6840c45cdcb2677176edd`). Every test below asks for that line.
- Control point: the layer every payment must pass through (`Concepts/Control Point.md` › Summary, chunk `afcb15e86de5f34b0e3a2729`). An authorization check sits in that path; a dashboard does not.
- None of the vault's open `[!contradiction]` callouts bears on these directions. The one on Edge asks whether personal friction is a valid start. Your directions start from professional capability, so it does not apply.

## Patterns

- **Prove the decision, not only make it.** Each new control comes with a demand for evidence afterwards. Nacha wants documented processes, reviewed every year. CFTC wants DCM audit trails. Mastercard says Verifiable Intent gives disputes a "clear audit trail". AP2 has receipts but no way to retrieve them at dispute time. This need shows up in ACH, event contracts and agent payments, three unrelated places. It is your edge sentence, and it is the strongest output of this run.
- **Settlement got too fast for review after the fact.** Five-minute event contracts. Five-minute ancillary-service reassignment in ERCOT. Machine-speed micropayments under AP4M and AgentCore. When the cycle is minutes or milliseconds, a check has to run before the action, inside the flow. Signals: the settlement-manipulation note, RTC+B, AP4M.
- **Rails ship coarse controls and leave the policy to the deployer.** AgentCore gives one session cap and an expiry. Visa and Mastercard give "spend controls". Nacha leaves "risk-based" undefined. Each platform hands the hard part, an organisation's own policy across accounts and rails, to the buyer.

## Directions (ranked)

### 1. The Nacha rules (live Jun 22, 2026) put a fraud-monitoring duty on every small Third-Party Sender and B2B originator: vertical SaaS that moves ACH for clients, payroll providers, payfacs. A pre-send check that leaves an evidence record of why it decided changes their outcome, because their sponsor bank (ODFI) audits them and can cut them off.
- Why it ranks here: the shift is forced and dated, and money is already moving (Nacha itself says "vendor solutions have emerged"). There are hundreds of small buyers with a compliance budget, which fits the bootstrap bar. It also sits outside your home industries.
- Widen: the sponsor bank carries the loss and must show the rule is met across all of its fintech programs. One ODFI can push the product to dozens of originators. Test both buyers.
- Main risk: edge fit is moderate. The rule does not require monitoring before posting, so many buyers will settle for a cheap rules engine. Funded fraud vendors (Sardine, Unit21, Alloy) sell into the larger end. Go narrow: small originators, credit-push fraud, and a replay pack built for the ODFI audit.
- Belief: I believe small ACH Third-Party Senders will pay $300–1,500/month for a pre-send fraud check with an audit-ready decision record, because Nacha Phase 2 made monitoring mandatory on Jun 22, 2026, and this is true by the first annual audit cycle after the rule.
- Test: 100 messages to heads of payments or risk at vertical-SaaS companies and payfacs that originate ACH through a sponsor bank. Send 15 more to fintech-program risk leads at sponsor banks. Question: "When your sponsor bank asked how you meet the new Nacha fraud-monitoring rule, what did you show them, and what did it cost to put together?" Pass: 3 or more replies that describe a real fraud loss or a named spend, inside 2 weeks.
- Kill result: fewer than 3 replies, or replies say "our processor or bank handles it, at no cost to us". That means the duty is absorbed upstream.

### 2. CFTC scrutiny of event contracts (Feb–Mar 2026) plus fivefold volume growth create a surveillance-and-replay duty for prediction-market DCMs and the brokers that route retail flow to them. Your exchange risk and replay engine is the reason you win: settlement-window pushes and affiliation insider trades are exchange-microstructure problems, not generic AML.
- Why it ranks here: the shift is dated, with a statutory duty behind it (Core Principles 3, 4 and 12; real-time monitoring), and money is moving. Edge fit is the strongest in the list: replaying the order book around a five-minute close is your old job. Bar fit is mixed. The buyer pool is small (a dozen-plus DCMs and applicants, plus the FCMs and brokerages that offer event contracts), but a few contracts would cover a bootstrap income.
- Widen: sports leagues and integrity bodies carry the reputational loss from insider bets. Broker-dealers adding event contracts carry the supervision duty for their customers. Either may buy faster than a DCM.
- Main risk: incumbent surveillance vendors (Nasdaq SMARTS, Eventus, Solidus) already sell to exchanges, and enterprise sales are slow. The CFTC rule is still an advance notice. Go narrow: event-contract detectors (settlement-window pushes, outcome-affiliated traders) plus a case file for referrals, sold as an add-on.
- Belief: I believe new DCMs and brokers offering event contracts will pay for event-specific surveillance with replayable case files, because CFTC told them in March 2026 to monitor all trading in real time, and this is true by the end of the ANPRM-to-rule cycle in 2027.
- Test: 12 conversations with CCOs or market-surveillance leads at DCMs, DCM applicants, and brokerages offering event contracts. Question: "Walk me through your last suspicious-trading inquiry on an event contract: how long did it take to reconstruct, and what tools did you use?" Pass: 4 or more describe an inquiry they handled with manual reconstruction or a tool they want replaced, inside 3 weeks.
- Kill result: most say an incumbent vendor already covers event contracts well, or that inquiries are rare enough to handle by hand.

### 3. Agent payment rails went live in 2026 (Visa Apr 8, Mastercard Jun 10, AWS GA Aug 18) with only coarse controls. Companies whose agents spend company money across rails need one policy and one evidence trail. Real-time limits across many accounts, plus deterministic replay of each agent decision, change the outcome, because disputes and liability are the stated blocker.
- Why it ranks here: money is moving, but adoption is discretionary, not forced. Your edge (capabilities 1, 2 and 4 together) is the product. Without it you ship a dashboard, not a control point. Bar fit is good: the buyers are developers, and the sale can be self-serve.
- Widen: card issuers and program managers who put cards in agents' hands (Highnote is a Visa pilot partner) carry the loss. So do insurers starting to price agent errors. A program manager could buy the check for all its agent cardholders.
- Main risk: the platforms (Stripe, AWS, Visa, Mastercard) keep adding controls, and funded agent-wallet startups crowd the horizontal version. Go narrow: cross-rail policy plus a dispute-evidence pack, the piece AP2 leaves out of scope.
- Belief: I believe B2B teams running agents that pay for APIs, compute or goods will pay for cross-rail spend policy with replayable decision records, because agent rails reached GA in 2026 with only session caps, and this is true by mid-2027.
- Test: 100 messages to engineering leads at companies that publicly ship agents using x402, MPP, AgentCore payments or Stripe Shared Payment Tokens, plus 10 conversations with fintech card-program risk leads. Question: "Has an agent of yours ever spent money it shouldn't have, or been unable to prove a spend was authorized? What happened next?" Pass: 3 or more replies that describe a real incident or a manual control they built, inside 2 weeks.
- Kill result: replies say agents spend too little to matter today, or the platform's built-in caps are enough.

### 4. The GENIUS Act takes effect by Jan 18, 2027 at the latest, and the Treasury Section 3 rule (proposed Aug 2026) makes digital-asset service providers prove they offer only permitted stablecoins to US-located users. Your crypto-exchange risk engine changes the outcome: per-account, per-asset eligibility checks with replay, so a provider can show the regulator each block or allow decision.
- Why it ranks here: the deadline is forced and close. Edge fit is high, but this is your home industry. Bar fit is weak: the final rules are not out, the buyers include banks, and the BSA/AML piece comes in a separate rule.
- Main risk: Chainalysis, TRM and the exchanges' own teams cover nearby ground, and the scope may shift with the final rule.
- Belief: I believe mid-size US crypto platforms and fintechs offering stablecoins will pay for an eligibility-and-evidence layer, because the GENIUS Act binds by Jan 18, 2027.
- Test: 10–15 conversations with compliance leads at mid-size US exchanges, wallets and fintech stablecoin programs. Question: "How will you prove, per transaction, that a stablecoin you offered a US user was permitted on that date?" Pass: at least a third describe a budget line or a build they already started, inside 3 weeks.
- Kill result: most plan to rely on their current blockchain-analytics vendor or a static allowlist.

### 5. ERCOT RTC+B (Dec 5, 2025) reassigns battery capacity every five minutes and penalises missed ancillary-service obligations. Merchant storage owners need a pre-commit check ("may this battery take this AS award at this state of charge?") and a record of why. Your power-auction work changes the outcome.
- Why it ranks here: dated, forced market design and a real penalty. But this is your home industry, and bidding optimizers (Tesla Autobidder, Fluence, Ascend and others) already own the offer workflow.
- Main risk: the check folds into the optimizer the owner already pays for.
- Belief: I believe ERCOT merchant storage owners will pay for an independent SoC-obligation check with replay, because RTC+B changed the penalty risk in Dec 2025.
- Test: 10 conversations with asset managers at ERCOT storage owners and their QSEs. Question: "Since RTC+B, have you paid a penalty or skipped an AS market because of state-of-charge risk? What did it cost?" Pass: 4 or more name a cost, inside 2 weeks.
- Kill result: owners say their optimizer vendor already handles it.

## This week

Start test 1, the Nacha one. It has the strongest forced shift, the most small buyers, and the fastest sale for a solo bootstrapper. The ODFI widening may hand you a channel. Run test 3's 100 messages alongside it if you have the hours, because your edge fits it best. After the first replies, use `market-map` to map the winning direction's workflow.

**To sharpen this:**
1. Your income target and runway. It decides whether a slow DCM sale (direction 2) is affordable.
2. Ideas you already tried or killed, and why.
3. Any buyers or regions you rule out, for example crypto or regulated banks.

---
Run log
- Read skill files: market-selection/SKILL.md, second-brain-retrieval/SKILL.md.
- Vault /search (limit 5): "edge" 5, "why now" 5, "tarpit" 5, "market pull" 5, "control point" 5, "agent" 5, "audit" 5, "margin" 5, "replay" 5, "authorization" 5, "risk" 5, "compliance" 5. Second pass (to get chunk IDs): "agentic commerce" 5, "agent mandate" 5, "oversight layer" 5, "liability" 5, "power" 5, "auction" 2, "stablecoin" 2, "chargeback" 0, "one-person company" 0, "market selection" 5, "authorization" 5, "edge" 5, "agent certification" 5, "identity binding" 5. Third pass: "why now" 5, "control point" 5, "market pull" 5, "settlement manipulation" 5, "prediction market" 5, "settlement manipulation" (limit 8) 8, "kalshi" 2.
- Vault /notes: Concepts/Agentic Commerce, Agent Mandate, Oversight Layer, AI Liability, Edge, Why Now; Sources/AP2 - Agent Payments Protocol, Visa Trusted Agent Protocol; Concepts/Tarpit Market, Control Point, Polymarket, Agent Certification, Settlement Manipulation, Prediction Market. (One batch first returned empty because I read the wrong JSON field; I re-ran it.)
- Exa web_search_exa (5): Nacha 2026 fraud-monitoring rules; 2026 agent payment rail launches; GENIUS Act implementing rules; ERCOT RTC+B; CFTC 2026 prediction-market actions.
- Exa web_fetch_exa (1, batched 9 URLs): Nacha news, AWS AgentCore GA, Mastercard AP4M, OCC Bulletin 2026-3, CFTC 9185-26, CFTC Letter 26-08, CFTC 2026-05105, ERCOT RTC+B release, Visa Intelligent Commerce Connect. Not opened: Treasury FR NPRM, Canary Media, Stripe and Mastercard Verifiable Intent posts (seen only in search results).
