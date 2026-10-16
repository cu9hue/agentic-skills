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
addresses; drafts that pitch or drift from the user's voice; drafts with no
urgency ("next week or two", "happy to work around your schedule") or
no competence and FOMO signal; and
the same research depth for every prospect regardless of priority.

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
- asks for, or proposes for confirmation, the lead question (an insider
  question that names a real mechanism) and the cohort ("the few founders
  …")
- asks who the sender is (name and credential line) and for their
  background, says it will agree with the user which parts matter to this
  ICP, and allows "none"; assumes no background from earlier campaigns
- asks for a yes before creating the tracker and names the parts the user
  can skip (Calls database, views, draft formulas), with "no tracker"
  allowed
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

## S3 — personalization tiers, drafts and tracker fields

User message: "Campaign C. Their customers: credit unions. Lead question:
'When a credit union's model risk team reviews your agent, what do they
actually ask to see?' Cohort: 'working on AI that credit unions trust with
money'. I'm the sender. Credential line: 'Ex-risk quant, now at EF'.
Background we agreed is worth matching: EF, ex-risk quant at Halcyon
Capital 2017–2021, MIT 2016. I live in Boston. Write the copy and the tracker fields for these
five."

- Dana Ruiz, CEO, Ledgerline, priority 1. Facts: (a) case study with
  Chartway Federal Credit Union on disputes, published 2026-05-12,
  ledgerline.ai/customers/chartway; (b) $4M seed, TechCrunch, 2024-03-02;
  (c) a listicle on aitoolsdirectory.io says "used by 40+ credit unions",
  no source. Profile: Stanford 2012, ex-Square; location Boston. Email:
  dana@ledgerline.ai, verify = valid.
- Sam Okafor, CTO, Ledgerline, priority 1. Fact: talk "Guardrails for
  agents that move money" at Money20/20 USA, 2025-10-27,
  money2020.com/sessions/guardrails-agents. Profile
  (linkedin.com/in/samokafor): risk quant at Halcyon Capital 2016–2020.
  Email: not found.
- Priya Shah, CEO, Meridian Recon, priority 1. Facts: AutoPost launch,
  meridianrecon.com/blog/autopost, 2026-08-19; partnership with Corelink
  announced in Corelink's press release, 2026-06-03,
  corelink.com/news/meridian. Profile (meridianrecon.com/team): MIT 2014.
  Email: priya@meridianrecon.com, verify = accept_all.
- Lee Tran, founder, Tallyhand, priority 2. Fact: Lee's post "Why
  examiners want to see the human in the loop", tallyhand.com/blog/examiners,
  2026-07-14. Email: lee@tallyhand.com, verify = invalid.
- Rowan Hale, CEO, Gridmark (test harness for credit-union AI), priority 3.
  Fact: Gridmark launched a model-risk report, gridmark.io/blog/mrm,
  2026-09-02. Profile: EF alum. Email: rowan@gridmark.io, verify = valid.

Rubric:
- Personalization follows priority: Dana `work` (Boston is not a
  connection type); Sam `both` (Halcyon + the talk); Priya `both` (MIT +
  AutoPost or Corelink); Lee `work`; Rowan `none` with empty hooks, even
  though a fact and an EF connection were offered
- Intro only for Sam and Priya: at most 10 words, names the connection
  (Halcyon, MIT), keeps "risk quant" and "EF"; empty for the rest
- Email hook only with a work fact (Dana, Sam, Priya, Lee): a noun phrase
  of 1–5 words, no verb, no flattery, no em dash; empty for Rowan
- subjects follow the tier: "question about your …" with a work fact,
  "quick question about …" for Rowan; every subject reads as an outsider
  asking (no "Chartway x Ledgerline")
- every work fact is from the last 12 months with its URL in Notes; never
  the 2024 seed round or the unsourced listicle; connection sources in
  Notes too
- Channel: Dana, Priya and Rowan email + linkedin; Sam and Lee linkedin
  only; Email check recorded per person; no address invented for Sam
- drafts follow the template: "Hi {first}," then the lead question first,
  then the Intro or the credential ("Ex-risk quant, now at EF"), "Talking
  to the few founders … this week", the hook clause "… puts you on that
  list" (none for Rowan), "15 min Thu or Fri?", signed "Thanks, Polina"
  with no signature block; no "picking what to build", no "next week or
  two", no "work around your schedule", no pitch, no em dashes
- LinkedIn notes are under 300 characters, built from the same fields

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
  to match; scale personalization to the prospect's value (not every
  prospect needs research); lead with an insider question, signal
  competence and peer-cohort FOMO, and ask for a call on named days this
  week
- the concerns are an organizing thread, not one bullet

## S5 — negative: should not trigger

User message: "Dana from Ledgerline replied: 'Sure, happy to chat. Send me
a few times.' Draft my reply."

Rubric:
- returns a short reply offering concrete times; no pipeline ceremony
- asks for no campaign inputs, plans no discovery or spend
- a one-line reminder to set Status to "Replied" or "Call booked" is fine

## S6 — different sender, no relevant background

User message: "Campaign C. This batch goes out from my cofounder Alex
Mercer, not me. Credential line: 'Ex-Stripe payments engineer, now at EF'.
We talked it through and none of Alex's background is worth matching for
this ICP. Their customers: credit unions. Lead question: 'When a credit
union's model risk team reviews your agent, what do they actually ask to
see?' Cohort: 'with agents live at credit unions'. Write the tracker
fields and Dana's email for these two."

- Dana Ruiz, CEO, Ledgerline, priority 1. Fact: case study with Chartway
  Federal Credit Union on disputes, published 2026-05-12,
  ledgerline.ai/customers/chartway. Profile: Stanford 2012, ex-Square.
  Email: dana@ledgerline.ai, verify = valid.
- Sam Okafor, CTO, Ledgerline, priority 1. Fact: talk "Guardrails for
  agents that move money" at Money20/20 USA, 2025-10-27,
  money2020.com/sessions/guardrails-agents. Profile
  (linkedin.com/in/samokafor): risk quant at Halcyon Capital 2016–2020;
  EF alum. Email: not found.

Rubric:
- Personalization is `work` for both; no Intro for either, even though
  Sam shares EF and a risk-quant past that a different sender might match
- no connection search is proposed or run for these priority-1 people
- drafts use Alex's credential line and sign "Thanks, Alex"; nothing says
  Polina, risk quant (as the sender's credential) or Halcyon
- Dana's email follows the template: lead question first, credential,
  "Talking to the few founders with agents live at credit unions this
  week, and … puts you on that list", "15 min Thu or Fri?"
- Email hooks are 1–5 word noun phrases from the work facts, with URLs in
  Notes
