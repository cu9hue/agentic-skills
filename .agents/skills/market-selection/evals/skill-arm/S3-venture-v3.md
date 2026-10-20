# S3 skill arm v3 (post proven-niche edit), 2026-10-20

**Bar:** venture, with a ceiling of $1bn ARR in under 10 years *(assumed: a pre-seed raise implies venture, but you named no ceiling)*
**Geography:** US first, with global rails *(assumed)*
**Edge as capabilities:** *(assumed, because you didn't describe your backgrounds)* security-critical low-latency backend systems; modelling risk and loss; selling to risk, compliance or payments teams.

No vault or web in this run; every shift is from memory and marked *(needs source)*.

## Shifts
| Shift | Type | Date | Source |
|---|---|---|---|
| Visa Intelligent Commerce: agent tokens and spend controls | New rail | Apr 2025 | *(needs source)* |
| Mastercard Agent Pay | New rail | Apr 2025 | *(needs source)* |
| Coinbase x402 | New rail | May 2025 | *(needs source)* |
| US GENIUS Act | Rule | Jul 2025 | *(needs source)* |
| Google AP2 signed mandates | New rail | Sep 2025 | *(needs source)* |
| OpenAI + Stripe Agentic Commerce Protocol, Instant Checkout | Behaviour at scale | Sep 2025 | *(needs source)* |
| Stripe Tempo after Bridge | Incumbent move | Sep 2025 | *(needs source)* |
| Visa Trusted Agent Protocol | New rail | Oct 2025 | *(needs source)* |
| Cloudflare Web Bot Auth / signed agents | Capability | 2025 | *(needs source)* |
| EU AI Act high-risk obligations, possibly delayed | Rule | Aug 2026 | *(needs source)* |

Themes: Reg E / chargeback liability for agent purchases unsettled; agent fraud not yet counted.

## Patterns
- Every protocol proves intent, but nobody checks the proof (AP2, Visa/Mastercard tokens, TAP, Cloudflare).
- The loss lands on parties who didn't build the agent (issuers, merchants, sponsor banks, x402 sellers).
- Cards vs stablecoins race; a rail-neutral control layer is worth more.

## Directions (ranked)
1. Agent-checkout disputes: evidence layer that replays what the user authorised. Category: new; buyer widened to issuers and sponsor banks; ceiling depends on agent purchase volume growing. Test: 12 dispute/fraud-ops conversations, pass at 4+ real cases, 3 weeks.
2. Fleet-level real-time spend authorisation for agent platforms. Category: new, next to proven card issuing (Marqeta, Lithic, Ramp; check prices); niche = AP automation, procurement and travel-agent vendors whose workflow is fleets, not employees; ceiling = vendors × platform fee + bps *(needs source)*. Test: 100 messages to CTOs, pass at 3+ incidents or in-house builds, 2 weeks.
3. Agent-traffic risk scoring for merchants. Category: proven (Cloudflare, Sift, Forter; check prices); niche = merchants with high agent traffic blocking good agents. No ceiling stated; no statement on whether the shift grows the niche. Test: 10 heads of fraud, pass at 4+.
4. x402 / GENIUS stablecoin metering for API sellers. Thin volume risk. Test: 100 messages, pass at 3+.
5. *(outside your geography)* EU AI Act replay audit for EU lenders.

## This week
Run direction 1's 12 conversations and direction 2's 100 messages in parallel; take the winner to `market-evaluation` against $1bn ARR.

(Condensed from the full reply; structure, categories and tests kept.)
