# S2 skill arm v1 (first draft), 2026-10-20

**Bar:** bootstrap, profitable solo within 12–18 months from revenue; a few dozen to a few hundred paying B2B customers (assumed income target).
**Edge as capabilities:** pre-action authorization against shared limits; deterministic replay; auction and bidding mechanics; production agent harnesses; low-latency correct-under-load systems.

## Shifts
| Shift | Type | Date | Source |
|---|---|---|---|
| Agent payment rails: Visa Intelligent Commerce, Mastercard Agent Pay, Google AP2, Stripe/OpenAI ACP, Coinbase x402 | New rail | Apr–Sep 2025 | (needs source) |
| UK mandatory APP fraud reimbursement, up to £85k/claim, 50/50 sending/receiving PSP | Rule | 7 Oct 2024 | (needs source) |
| EU Instant Payments Regulation: VoP and instant euro sends mandatory | Rule | 9 Oct 2025 | (needs source) |
| EU AI Act high-risk logging (Art. 12) and oversight (Art. 14); delay proposed | Rule | Aug 2026, may slip | (needs source) |
| Colorado AI Act consequential-decision duties | Rule | 30 Jun 2026 | (needs source) |
| NAIC model bulletin on insurers' AI use | Rule | Dec 2023 on | (needs source) |
| Synapse collapse; FDIC custodial recordkeeping proposal | Failure | Apr 2024; Sep 2024 | (needs source) |
| Public agent incidents (coding agent deleting a production DB) | Failure | Jul 2025 | (needs source) |
| Insurers sell AI-error cover (Lloyd's-backed) | Money moving | 2025 | (needs source) |
| EU day-ahead power market moves to 15-minute products | Rule/platform | 1 Oct 2025 | (needs source) |
| Spend platforms issue cards/limits for agents | Behaviour | 2025–26 | (needs source) |

Theme, not a shift: "AI agents are taking off."

## Patterns
- Authority to move money passes from people to software, and whoever carries the loss can't see why the action happened (agent rails, irrevocable instant payments, APP reimbursement, AI liability insurance, agent incidents). Strongest output.
- Records that can't be rebuilt after the fact become a liability (Synapse, FDIC proposal, AI Act Art. 12, Colorado, NAIC).
- Rules shift losses onto intermediaries without pre-trade-style controls (receiving PSPs, sponsor banks, insurers and MGAs, merchants accepting agent payments).

## Directions (ranked)
1. **Agent-spend limits with replayable proof for software companies whose agents spend customer money.** Best edge fit, short sale. Risk: rails or spend platforms build basic limits; go narrower (cross-account limits plus dispute replay). Widen: companies deploying procurement/travel/ad agents, insurers underwriting them, card issuers handling agent chargebacks. Belief: true by Q2 2027. Test: 100 messages to founders/CTOs whose agents purchase, book or buy ads; "last time an agent spent money it shouldn't have, or you couldn't explain a charge?"; pass 3+ incident or home-built-control replies; 2 weeks. Kill: <3 incidents, "we just cap the card".
2. **Real-time hold-or-release with dispute-grade replay for small UK/EU PSPs and EMIs under APP reimbursement and IPR.** Strongest shift (forced, dated, money paid out); slower regulated sale. Go narrow: receiving side, mule accounts at EMIs and crypto on-ramps. Test: 10–15 conversations with heads of fraud; pass a third name a cost; 3 weeks.
3. **Per-decision audit replay for MGAs and claims TPAs under NAIC/Colorado/AI Act.** Out-of-industry direction. Test: 10–15 heads of claims/compliance; pass a third describe staff or legal cost; 3 weeks.
4. **Independent bid auditing for small EU battery and flexibility owners after 15-minute day-ahead products.** Home industry, net positive. Test: 100 messages to sub-50MW asset managers; pass 3+ disputes or suspected shortfalls; 2 weeks.
5. **Point-in-time ledger replay for BaaS fintechs after Synapse.** Weak bar fit (banks slow). Test: 10–15 finance/compliance leads; pass a third describe weeks of work or a consent-order demand; 3 weeks.

## This week
Start test 1. It also tests pattern 1, which survives if this buyer group dies; weak replies point to direction 2's buyers. Offer market-map after 3+ incidents. To sharpen: income target, UK/EU/US base, ideas already killed.
