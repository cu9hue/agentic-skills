# outreach-campaign — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md and `references/notion-and-templates.md` read by the arm), identical
prompts otherwise. Every arm is told that today is 2026-10-09, to invoke no
skill of its own, and to call **no tools** (no web, no treg, no Notion), so
the pipeline's judgment is under test, not live data. The subagent returns
exactly the deliverable, the next chat message it would send, with no
meta-commentary. Anonymize outputs into teams, blind-judge against the
rubrics, log in `results.md`.

The failures this skill targets: a run that starts spending before it has
the exclusion list and the tracker; screening that lets an EU team or a
buyer-side company through; hooks built on stale or unsourced facts;
subjects that read as if the prospect's customer sent them; guessed email
addresses; and drafts that pitch or drift from the user's voice.

## Shared material: campaign C

- Campaign: "Exploring trust and control for AI in finance". One-liner:
  "exploring trust and control for AI in finance".
- ICP: founders and CTOs of startups that sell AI agents acting on money
  (disputes, reconciliation, payment exceptions) to credit unions and
  community banks. Priority 1: agents act in production at one or more
  named financial-institution customers. Priority 2: AI copilots for
  FI operations where a human approves each action, or agents with no named
  customer yet. Priority 3: adjacent tooling for FI AI (testing,
  monitoring). Geography: US.
- Exclusion list: Northlight Payments, Ardent Ledger.
- Existing tracker rows: Brightwater Ops (Kim Alvarez, CEO).

## S1 — kickoff with missing inputs

User message: "Run an outreach campaign called 'Exploring trust and control
for AI in finance'. Target founders of US startups that sell AI agents to
credit unions and community banks."

Rubric:
- asks for every missing input in one message: priority 1/2/3 criteria,
  exclusion list, Notion parent page URL
- states the defaults instead of asking open questions about them: US only
  and never EU, $2 treg cap per batch, 15–20 companies, at most 2 people
  per company
- asks for, or proposes for confirmation, the Variant B pain question
- makes no paid call and writes nothing before the exclusion list and the
  Notion page are known (it may say what runs next)
- short: the user can answer on one pass

## S2 — screen a discovery batch

User message: "Campaign C (shared material). Discovery returned these.
Screen them and give me the list."

1. Ledgerline (Austin, TX): AI agents resolve card disputes end to end for
   credit unions. Case study with Chartway Federal Credit Union, May 2026.
2. Klarwerk (HQ New York; engineering and all customers in Germany): AI
   reconciliation agents for German Sparkassen.
3. Pinecrest FCU (Ohio): a credit union piloting AI agents for member
   service.
4. Tallyhand (New York): AI copilot that drafts BSA/AML case narratives for
   community banks; an analyst approves each one. No named customers. Team
   page lists two founders with LinkedIn profiles.
5. Fernwood AI (Denver): site last updated 2023; LinkedIn says "Fernwood
   is now part of Q2".
6. Sablepoint (US): "AI agents for finance teams". No team page, no named
   people, domain registered August 2026.
7. Northlight Payments (US): AI agent for payment exceptions at banks.
8. Covey Labs (US): AI that writes marketing emails for credit union
   marketing teams.
9. Brightwater Ops (Charlotte, NC): agents auto-resolve ACH returns for
   banks.
10. Quillrate (San Francisco): pivoted from lending AI to HR software in
    2025.
11. Meridian Recon (Chicago): AI agent auto-posts reconciliation entries
    for credit unions. Named customer: Lakeside Credit Union. Launched
    AutoPost in August 2026.

Rubric:
- keeps Ledgerline and Meridian Recon at priority 1 and Tallyhand at
  priority 2, each with why it fits and its buyers as a plural noun
- rejects Klarwerk for geography (EU team and market), even with a US HQ
- rejects Pinecrest as the wrong side of the market (a buyer)
- rejects Fernwood (acquired), Quillrate (pivoted), Sablepoint
  (unverifiable team), Covey (weak fit: does not act on money)
- drops Northlight (exclusion list) and Brightwater (already in the
  tracker), naming the reason for each
- every reject carries a one-line reason

## S3 — hooks, drafts and tracker fields

User message: "Campaign C. Their customers: credit unions. Variant B
question: 'I'm curious how you get credit unions comfortable letting your
agents act on their own and whether that part ever slows a deal down'.
Write the copy and the tracker fields for these four."

- Dana Ruiz, CEO, Ledgerline, priority 1. Facts: (a) case study with
  Chartway Federal Credit Union on disputes, published 2026-05-12,
  ledgerline.ai/customers/chartway; (b) $4M seed, TechCrunch, 2024-03-02;
  (c) a listicle on aitoolsdirectory.io says "used by 40+ credit unions",
  no source. Email: dana@ledgerline.ai, verify = valid.
- Sam Okafor, CTO, Ledgerline, priority 1. Fact: talk "Guardrails for
  agents that move money" at Money20/20 USA, 2025-10-27,
  money2020.com/sessions/guardrails-agents. Email: not found.
- Priya Shah, CEO, Meridian Recon, priority 1. Facts: AutoPost launch,
  meridianrecon.com/blog/autopost, 2026-08-19; partnership with Corelink
  announced in Corelink's press release, 2026-06-03,
  corelink.com/news/meridian. Email: priya@meridianrecon.com, verify =
  accept_all.
- Lee Tran, founder, Tallyhand, priority 2. Fact: Lee's post "Why
  examiners want to see the human in the loop", tallyhand.com/blog/examiners,
  2026-07-14. Email: lee@tallyhand.com, verify = invalid.

Rubric:
- every subject reads "question about your …" and reads as an outsider
  asking (no "Chartway x Ledgerline", nothing that sounds like the customer
  or partner wrote it)
- every email hook starts "Saw" or "Congrats on", is at most 22 words,
  has no em dash and no trailing period, and no flattery
- every hook uses a fact from the last 12 months with its URL in Notes;
  never the 2024 seed round or the unsourced listicle
- LinkedIn hooks are 3–8 words with a lowercase start
- Variant alternates A/B across the priority-1 people who get an email
  (Dana, Priya), so both variants go out; Sam and Lee get A (rubric
  tightened after the first run, see `results.md`)
- Channel: Dana and Priya email + linkedin; Sam and Lee linkedin only;
  Email check recorded per person; no address invented for Sam
- drafts follow the templates: "Hi {first}," opener, the hook then "and
  thought you might have some good insight…", 15 minutes of advice, signed
  "Thanks, Polina" with no signature block, no pitch, no em dashes
- LinkedIn notes are under 300 characters with no background line

## S4 — structural probe: underspecified ask

User message: "I'm starting cold outreach to founders next week to get
customer discovery calls. What should I get right?"

Rubric:
- the skill's core concerns structure the answer unprompted; pass needs at
  least four of: ask for 15 minutes of advice and never pitch; one recent,
  verifiable, specific hook per person; verify every email and never guess
  one (accept_all also goes to LinkedIn); batches of ~10–20 with a
  follow-up after ~3 business days on the other channel; change the
  message after a zero-reply batch before burning more prospects; no open
  tracking, replies tracked by hand; expect ~5–10% replies and size volume
  to match
- the concerns are an organizing thread, not one bullet

## S5 — negative: should not trigger

User message: "Dana from Ledgerline replied: 'Sure, happy to chat. Send me
a few times.' Draft my reply."

Rubric:
- returns a short reply offering concrete times; no pipeline ceremony
- asks for no campaign inputs, plans no discovery or spend
- a one-line reminder to set Status to "Replied" or "Call booked" is fine
