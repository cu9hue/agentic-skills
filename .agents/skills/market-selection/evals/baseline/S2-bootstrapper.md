# S2 baseline (no skill), 2026-10-20

Your edge has two parts, rarer together: (1) stateful real-time limits — "may this actor do this, given everything they and related actors already did?" (stateless checks are solved by OPA, Cedar, Oso); (2) deterministic replay. Look for places where money moves fast, limits depend on accumulated state, and someone later explains a decision to an auditor, regulator, insurer or court.

Signals to hunt for: "we can't let it do X yet" (human approves every agent action); spreadsheet risk; a post-mortem that couldn't answer why; a rule that demands proof (SEC market access rule, REMIT, MiCA, EU AI Act logging; needs source); small firms needing a big-firm function; auditors or insurers asking new questions (needs source).

Spaces, ranked by transfer: 1. small power market participants (position limits, bid validation, replayable record; 10–30 customers sustain a solo business); 2. pre-trade risk for small venues and brokers (ethically mixed buyers); 3. spend controls for AI agents in one vertical, e.g. refund authority for AI support agents ("prove why the bot refunded $400"); 4. claims and benefits decisions (slow sales, later move).

Filters for solo bootstrapped: existing budget; sales cycle under ~3 months; narrow niche; edge is the product; net positive by design.

Next two weeks: pick two spaces (power aggregators, agent refund authority); 10 conversations per space with the person who carries the loss; ask about the last automated action that cost money, who approves today, how long to answer a regulator. Score each on real incident / human bottleneck / outside party asks for proof; keep a space where most conversations hit all three.

Sharpen: geography, runway, stance on crypto and trading customers.
