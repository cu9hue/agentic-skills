**Bar:** bootstrap. A profitable business within 12–18 months, funded from revenue. A few dozen paying B2B customers is enough. Income target *(assumed)*: replace a senior quant salary.
**Geography:** US
**Edge as capabilities:**
1. A real-time authorization engine: decide allow, hold or deny for each action against limits that span many accounts, in milliseconds.
2. Deterministic replay: rebuild any past decision from the event log, with the exact inputs and rule version, so an auditor or regulator can see why it happened.
3. Surveillance instincts from market microstructure and auctions: you know what spoofing, wash trading, front-running and insider patterns look like in an order stream.
4. Production agent harnesses: you know how LLM agents fail when they are given tools, and money.

Your one-line edge, "decide in real time whether an actor may take an action with money at stake, and prove afterwards exactly why", is not a trading skill. It travels. Below, "actor" means a trader, an ACH originator, a sports bettor, an AI agent and a stablecoin holder.

## Shifts

| Shift | Type | Date | Source |
|---|---|---|---|
| Nacha fraud-monitoring Phase 1. All ODFIs, plus Originators and third parties with more than 6M entries in 2023, must run risk-based processes to catch fraud-induced ACH entries, including credits. | Rule / deadline | 2026-03-20 | [Nacha Phase 1](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-1) *(not opened; dates confirmed on the Phase 2 page)* |
| Nacha Phase 2. The volume threshold is removed, so **every** non-consumer Originator, Third-Party Sender and Third-Party Service Provider must comply and review its procedures each year. | Rule / deadline | 2026-06-22 (effective in practice) | [Nacha Phase 2](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2) |
| Google's AP2 protocol: signed "mandates" that prove what a user authorized an agent to buy, with price limits and a "non-repudiable audit trail". | New rail | 2025-09-16 | [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol) *(not opened)* |
| Mastercard Verifiable Intent: a tamper-resistant record of what the cardholder authorized, so "if a dispute occurs, all parties can rely on a clear audit trail". | New rail | 2026-03-05 | [Mastercard](https://www.mastercard.com/us/en/news-and-trends/stories/2026/verifiable-intent.html) |
| Mastercard Agent Pay for Machines: "authorization rules and spending limits that are programmatically enforced" for machine payments. More than 30 launch partners (Stripe, Adyen, Coinbase, Cloudflare). Early access opened today. | New rail | 2026-06-10; early access 2026-10-20 | [Mastercard](https://www.mastercard.com/us/en/news-and-trends/press/2026/june/mastercard-launches-agent-pay-for-machines.html); [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/mastercard-debuts-tool-to-help-ai-agents-purchase-digital-services/) *(not opened)* |
| FIDO Alliance opens working groups on agent authentication and "trusted delegation for commerce". Chairs come from Google, OpenAI, CVS, Mastercard and Visa. | Standard / platform | 2026-04-28 | [FIDO](https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/) *(not opened)* |
| Money moving: Natural raised $30M for agent wallets and "transaction observability". The x402 Foundation launched with 40 members. Thoughtworks argues that payment rails verify single transactions, but nobody governs what the transactions add up to. | Money moving | Article 2026-10-12 (x402 launch date not stated) | [Thoughtworks](https://thoughtworks.com/insights/blog/generative-ai/why-agentic-payments-require-executable-model-organizational-authority) |
| CFTC Enforcement advisory on prediction markets after Kalshi insider cases. It restates that exchanges "have an independent duty… to maintain audit trails, conduct surveillance, and enforce rules". | Scrutiny / rule | 2026-02-25 | [CFTC](https://www.cftc.gov/PressRoom/PressReleases/9185-26) |
| Scandal: an Army sergeant was indicted for $409K of Polymarket bets on classified Maduro-operation information. The NYT found 80+ suspicious Polymarket accounts. House Oversight asked Kalshi how it detects anomalous trading. | Scandal | Indictment 2026-04-24; letter 2026-05-22 | [House Oversight letter](https://oversight.house.gov/wp-content/uploads/2026/05/Kalshi-Prediction-Markets-Letter.pdf) *(not opened)* |
| CFTC staff advisory on sports event contracts sets "new expectations for compliance, surveillance". It tells FCMs and introducing brokers to check their own surveillance programs. | Rule / guidance | 2026-03 | [Katten summary](https://quickreads.ext.katten.com/post/102mmtf/game-changer-cftc-clarifies-sports-contracts-listing-standards-and-seeks-input-o) *(not opened)* |
| NY Gaming Commission draft responsible-gaming rule. It sets 13 mandatory automated triggers (for example, deposits over $10K in 24h, or three limit increases in 7 days). A licensee that clears a flagged patron must "document the specific reasons" and keep the record 7 years. | Rule (pre-proposal) | 2026-03-25 memo | [NY Gaming Commission](https://gaming.ny.gov/system/files/documents/2026/03/03.25.26.preproposalcommentmemo_responsiblegambling.pdf) *(not opened)*. Related: Colorado Rule 9.6, amended 2026-01-14, requires operators to detail their automated problem-gambling triggers ([CO SBG](https://sbg.colorado.gov/sites/sbg/files/documents/SBRule9011426.pdf) *(not opened)*). |
| Treasury (FinCEN and OFAC) proposed GENIUS Act rule. Stablecoin issuers become BSA financial institutions and must be able to "block, freeze, and reject specific or impermissible transactions". | Rule (proposed) | 2026-04-10; comments closed 2026-06-09 | [Federal Register](https://www.federalregister.gov/documents/2026/04/10/2026-06963/permitted-payment-stablecoin-issuer-anti-money-launderingcountering-the-financing-of-terrorism) |

Theme with no date: "AI agents need guardrails" is everywhere. It belongs in the table only through the dated rails above.

## Patterns

- **Authorization is moving from people to systems, and each new rule asks for proof of why.** The rules don't only say "stop the bad action". They say "show your reasoning later": Nacha's annual review of procedures, the NY draft's 7-year "specific reasons" record, the CFTC's audit-trail duty, the dispute audit trails in AP2 and Verifiable Intent, and GENIUS's block/freeze/reject capability. These are five unrelated regimes (ACH, gaming, derivatives, card networks, stablecoins). Your edge statement describes this pattern almost word for word. It is the strongest output of this run, because it survives the death of any one buyer.
- **The rails ship the primitives. The operator still owns the policy and the evidence.** Mastercard enforces limits that someone else must set. AP2 signs a mandate, but someone must decide whether an action fits it. Thoughtworks names the gap: "ten individually permitted purchases" can still add up to a bad commitment. Lobster.cash says agent ecosystems "historically relied on… developer-defined controls". Signals: AP4M, AP2, Thoughtworks, Lobster.cash.
- **Rules written for large players now reach the long tail.** Nacha Phase 2 drops the volume threshold. The NY draft applies to every mobile licensee. Prediction-market scrutiny now reaches brokers that only route orders. The smaller parties have no quant-risk team, and they are the buyers a bootstrapped founder can reach.

## Directions (ranked)

### 1. Nacha Phase 2 made every business that pushes ACH credits responsible for catching fraud-induced payments, and a real-time hold/release engine that replays its decisions for the sponsor bank wins, because the bank's review asks "show me why you released this".
- **Buyer, widened.** Start with non-consumer Originators and Third-Party Senders that push credits at volume: payroll providers, AP-automation platforms, rent and property-management payout platforms, insurance-claims payout platforms. The party that carries the loss is the ODFI (sponsor bank). A bank is a slow sale, but a bank that tells its 40 Third-Party Senders "use this" is a distribution channel. Sell to the Third-Party Sender first and use the bank as a referral.
- **Why it ranks here.** This is the strongest shift on the list: a forced rule, already in effect, applying to all parties, with an annual review built in. The bar fit is good, with thousands of reachable mid-market buyers. The edge fit is moderate: a basic velocity check satisfies the letter of the rule. The replay evidence is what sets you apart.
- **Main risk.** The rule is risk-based and does not require monitoring before posting. Minimum compliance can be cheap, and fraud vendors (Sardine, Unit21, Alloy and similar) already sell into this space. Go narrow: sell the audit-grade "why we released it" record, not generic fraud scoring.
- **Belief.** I believe heads of risk at Third-Party Senders will pay for per-payment decisions that their sponsor bank accepts as evidence, because Nacha Phase 2 took effect on 2026-06-22 and the first annual reviews and sponsor-bank audits land in 2026–27.
- **Test.** Send 100 targeted messages to heads of risk, compliance or payments ops at US payroll, AP-automation, rent-payout and claims-payout platforms. The question: "Since June 22, what has your sponsor bank asked you to show about how you catch fraud-induced ACH credits, and what did you show them?" Pass: 3 or more replies that describe a sponsor-bank request, a failed review, or a credit-push fraud loss in the last 12 months. Time box: 2 weeks.
- **Kill result.** Fewer than 3 such replies. Or most replies say "our processor's monitoring covered it and the bank accepted it".

### 2. Insider-trading scandals and the CFTC's February advisory put prediction-market exchanges, and the brokers that route to them, on the hook for surveillance and audit trails. An engineer who has built exchange risk and deterministic replay can rebuild "who traded what, when, knowing what" quickly enough to answer a regulator.
- **Buyer, widened.** Chief compliance officers at CFTC-registered exchanges (DCMs) that list event contracts. Then FCMs and introducing brokers that offer event contracts to retail customers: the CFTC staff advisory told them to check their own programs. Then sports leagues and college conferences, which carry the integrity loss.
- **Why it ranks here.** The shift is strong: a live scandal, congressional pressure and an existing legal duty. The edge fit is the best on this list. Without HFT and exchange-risk experience this product is not credible. The bar fit is weaker: the pool is tens of exchanges and brokers, not thousands, though each pays well and many are startups that buy fast.
- **Main risk.** Few buyers, and established trade-surveillance vendors already sell to exchanges. Event-contract patterns, such as an insider on the underlying event or someone trading their own race, are new enough that incumbents may not cover them yet. That gap is the wedge.
- **Belief.** I believe compliance heads at event-contract exchanges and brokers will pay for event-aware surveillance with replayable case files, because the CFTC advisory (2026-02-25) and the House inquiry (2026-05-22) made surveillance gaps a regulatory exposure in 2026.
- **Test.** Hold 10–15 conversations with CCOs or surveillance leads at exchanges listing event contracts and at brokers offering them. The question: "For your last suspected insider case, how long did it take to rebuild who knew what and when, and what did it cost you?" Pass: at least a third describe a cost they already pay (headcount, a vendor, a regulator inquiry). Time box: 3 weeks.
- **Kill result.** Exchanges say their current vendor plus in-house staff covers it at no felt cost, and brokers say surveillance is the exchange's job.

### 3. State responsible-gaming rules now require automated triggers and documented reasons for each decision. A sportsbook needs an engine that flags patrons in real time and can show, years later, exactly why each flagged patron was cleared. *(Outside your industries: the same capability, a new buyer.)*
- **Buyer, widened.** Responsible-gaming leads and compliance at mobile sportsbook licensees in NY, CO and MD. Then B2B sportsbook platform providers, which serve many smaller operators at once and are the faster sale.
- **Why it ranks here.** The shift is forced: Colorado's rule is in force and NY's draft spells out 13 triggers and a 7-year record. The NY rule is still a pre-proposal, so it ranks below #1 and #2. The edge fit is good: the "document the specific reasons" clause is deterministic replay under another name.
- **Main risk.** Gaming vendors often need a state vendor license *(assumed; check per state)*. That costs time and money a bootstrapped founder may not have, and responsible-gaming analytics vendors already exist.
- **Belief.** I believe sportsbook compliance teams will pay for a trigger engine with replayable decision records, because NY's draft (2026-03-25) and Colorado Rule 9.6 (2026-01-14) make automated triggers and documented reasons an exam item in 2027.
- **Test.** Hold 10–15 conversations with RG leads and compliance at licensees and B2B platforms. The question: "If NY's draft triggers became final, how would you produce the reason you cleared a flagged patron, seven years later?" Pass: at least a third say their current system cannot do it and they would build or buy. Time box: 3 weeks.
- **Kill result.** Most say their platform vendor will ship it, or the vendor-license cost and timeline exceed your runway.

### 4. Card networks shipped rails for agent payments in 2026 but left the spend policy and the dispute evidence to whoever deploys the agent. A limit engine across many agents, with deterministic replay of every authorization, decides who wins a chargeback or an internal audit.
- **Buyer, widened.** Agent platforms and AI products whose agents already spend money (procurement, travel, ad-buying and API-buying agents, platforms integrating x402 or AP4M). The party that carries the loss is the agent platform when a user disputes a charge, and later the card issuers and program managers behind agent cards.
- **Why it ranks here.** It ranks 4th only because adoption is discretionary: no rule forces it. The edge fit is the highest on the list. This direction uses all four of your capabilities, including the agent-harness experience. The rails are dated and money is moving (Natural's $30M).
- **Main risk.** Funded players (Natural, Crossmint/Lobster.cash) and the networks themselves are crowding the horizontal layer. Go narrow: one vertical where agents already spend real money, or the dispute-evidence piece alone.
- **Belief.** I believe teams whose agents spend real money will pay for spend policy and replayable proof of authorization, because Agent Pay for Machines (early access 2026-10-20) and AP2 put agent payments into production, and the first disputes arrive by mid-2027.
- **Test.** Send 100 targeted messages to founders and CTOs at companies whose agents make purchases or pay for APIs. The question: "The last time one of your agents spent money it shouldn't have, how did you find out, and how did you prove what it was allowed to do?" Pass: 3 or more replies that describe a real incident or dispute. Time box: 2 weeks.
- **Kill result.** Fewer than 3 incidents, which means agents don't yet move enough real money. Or replies say network and wallet controls are enough.

### 5. GENIUS Act rules will require stablecoin issuers to block, freeze and reject transfers on lawful orders. Real-time enforcement with a replayable record of each block is the evidence an examiner asks for.
- **Buyer, widened.** Issuers applying for GENIUS permits. Also the payment companies that settle in stablecoins (BVNK-type), which carry sanctions exposure without being issuers.
- **Why it ranks here.** The shift is forced but the rules are only proposed. Issuers are few, well funded and slow to buy, which is a poor bootstrap fit. Your crypto-exchange background gives a good edge fit.
- **Main risk.** Long procurement, and blockchain-analytics incumbents already own sanctions screening.
- **Belief.** I believe stablecoin payment companies will pay for auditable freeze-and-block enforcement, because Treasury's proposed rule (2026-04-10) makes it a licensing requirement once final rules land.
- **Test.** Hold 10 conversations with compliance heads at stablecoin issuers and stablecoin-settling payment companies. The question: "On your last freeze or sanctions hit, how long did it take to show exactly which transfers you blocked and why?" Pass: at least a third describe a cost they pay. Time box: 3 weeks.
- **Kill result.** Their current analytics vendor covers it, or every buyer requires SOC 2 and a procurement cycle longer than 6 months.

## This week

Start test #1. Send the 100 Nacha messages to Third-Party Senders now. The rule is in force, the buyers are many and reachable, and a sponsor-bank request is a pain you can hear in one reply. Run test #4's 100 messages in the same two weeks if you have the capacity: it is the same message volume, and it tells you whether your strongest edge has a buyer yet. When replies arrive, I can map the winning direction's workflow with `market-map`.

**To sharpen this**
1. What monthly income and runway do you have? This sets how slow a sale you can afford, and it decides whether #2 (few buyers, large contracts) beats #1.
2. Will you sell into regulated buyers that need SOC 2, a gaming vendor license or bank vendor review? A no drops #3 and #5 down the ranking.
3. Have you already tried or killed any ideas? Their common thread would show where the constraints are too tight.

---

**Run log**
- Read: the skill file `market-selection-pre-vault.md` (the only local file read).
- Vault queries: none. The skill has no vault step, so I made 0 calls to `SECOND_BRAIN_URL`.
- ToolSearch: loaded `web_search_exa` and `web_fetch_exa` (not an Exa call).
- Exa call 1, `web_search_exa`: agent payment authorization (AP2, Mastercard Agent Pay, x402). 8 results.
- Exa call 2, `web_search_exa`: Nacha 2026 fraud-monitoring rules. 5 results.
- Exa call 3, `web_search_exa`: CFTC and prediction-market surveillance and insider trading, 2026. 6 results.
- Exa call 4, `web_search_exa`: GENIUS Act implementing rules from OCC and Treasury. 5 results.
- Exa call 5, `web_fetch_exa`: opened 6 URLs (Nacha Phase 2, Mastercard AP4M, CFTC press release 9185-26, Federal Register GENIUS NPRM 2026-06963, Thoughtworks, Mastercard Verifiable Intent). All 6 returned content.
- Exa call 6, `web_search_exa`: state responsible-gaming rules for sportsbooks, 2026. 6 results.
- Total: 6 of 6 allowed Exa calls. No WebSearch, WebFetch or Skill tool calls.
