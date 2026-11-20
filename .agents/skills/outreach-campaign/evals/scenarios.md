# outreach-campaign — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, or the
pre-edit skill for a regression; arm B = SKILL.md and
`references/notion-and-templates.md` read by the arm), identical prompts
otherwise. Every arm is told that today is 2026-10-09, to invoke no
skill of its own, and to call **no tools** (no web, no treg, no Notion), so
the pipeline's judgment is under test, not live data. The subagent returns
exactly the deliverable, the next chat message it would send, with no
meta-commentary. Anonymize outputs into teams, blind-judge against the
rubrics, log in `results.md`.

The failures this skill targets: a run that starts spending before it has
the exclusion list and the tracker; screening that lets an EU team or a
buyer-side company through; hooks built on stale or unsourced facts;
subjects that read as if the prospect's customer sent them; guessed email
addresses; drafts that pitch or drift from the user's voice; a first
message that opens with an apology, a background sentence or a request for
time instead of a personal line and one question; a link in a first
message; a generic row for a person with no confirmed fact; a question
that assumes a setup the prospect may not have; and email treated as the
only channel.

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
  per company, LinkedIn first with email as the second touch, the
  `question` opener
- proposes for confirmation a topic sentence that fits every prospect in
  the ICP, and one question for the role group that can be answered in one
  line, asks for a fact, and does not assume the prospect's setup
- asks for the sender's first name and a calendar link ("none" allowed)
  and for the background worth matching, allowing "none"; asks for no
  background sentence for the message; assumes no background from earlier
  campaigns
- asks for a yes before creating the tracker and names the parts the user
  can skip (Calls database, views, draft formulas), with "no tracker"
  allowed
- does not ask for LinkedIn access or data and does not offer to send for
  the user
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

## S3 — personal lines, drafts and tracker fields

User message: "Campaign C. Their customers: credit unions. Topic: 'I'm
trying to understand how credit unions decide to trust AI agents with
money, and where that decision gets stuck.' Question for founders: 'Do
your credit union customers let the agent act on its own today, or does
someone approve each action?' I'm the sender, Polina. Calendar:
https://calendly.com/polina/15min. Background we agreed is worth matching:
EF, ex-risk quant at Halcyon Capital 2017–2021, MIT 2016. I live in Boston.
All five have LinkedIn URLs. Write the copy and the tracker fields for
these five."

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
- every one of the five gets a Personal line: one sentence, at most 20
  words, from a confirmed fact or agreed connection. Dana from the
  Chartway case study (Boston is not a connection); Sam from the Halcyon
  connection, the talk, or both; Priya from MIT, AutoPost or Corelink; Lee
  from the post; Rowan from the report or EF (priority 3 still gets a line)
- no personal line uses the 2024 seed round or the unsourced listicle;
  every source URL and date is in Notes
- Email hook on every row: a noun phrase of 1–5 words, no verb, no
  flattery, no em dash; it is named as the email subject, and no row uses
  "15 min chat?"
- Personalization recorded per row (`both`, `connection` or `work`)
- First touch `linkedin` for all five. Channel: Dana and Rowan linkedin +
  email; Sam, Priya (accept_all) and Lee (invalid) linkedin only; Email
  check recorded per person; no address invented for Sam
- message 1 follows the template: "Hi {first}!", the personal line, then
  "Quick question:" and the confirmed question, in at most three
  sentences; the `advice` opener is also right for Rowan, whose product
  is a test harness and not an agent, if the output says why
- message 1 has no apology, no background sentence, no calendar link and
  no request for a call; the nudge asks for 15 minutes after the answer
  and uses the topic sentence; the calendar link appears only for the
  reply after they agree
- no pitch, no promise of insights, no em dashes

## S4 — structural probe: underspecified ask

User message: "I'm starting cold outreach to founders next week to get
customer discovery calls. What should I get right?"

Rubric:
- the skill's core concerns structure the answer unprompted; pass needs at
  least five of: connect on LinkedIn with no note and message on
  acceptance; open with a personal line from one recent, verifiable,
  specific fact; ask one specific question first and ask for the call
  after the answer; ask for 15 minutes of advice and never pitch; three
  sentences, no link in a first message; verify every email, never guess
  one, and keep unconfirmed addresses off email; batches with one
  follow-up after ~3 business days; change the message after a zero-reply
  batch before burning more prospects; track acceptance apart from replies
  and compare channels; expect ~5–10% replies and size volume to match;
  end each call with a small commitment question
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
Mercer, not me. No calendar link. We talked it through and none of Alex's
background is worth matching for this ICP. Their customers: credit unions.
Topic: 'I'm trying to understand how credit unions decide to trust AI
agents with money, and where that decision gets stuck.' Question for
founders: 'Do your credit union customers let the agent act on its own
today, or does someone approve each action?' Both have LinkedIn URLs.
Write the tracker fields and Dana's messages for these two."

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
- Personalization is `work` for both; no personal line uses a connection,
  even though Sam shares EF and a risk-quant past that a different sender
  might match
- no connection search is proposed or run for these priority-1 people
- Sender is Alex on both rows; the email draft signs "Thanks! Alex";
  nothing says Polina, risk quant or Halcyon
- Dana's message 1 follows the template: "Hi Dana!", a personal line from
  the Chartway case study, "Quick question:" and the question; no
  background sentence, no apology, no calendar clause, no call request
- Dana's email uses the hook as its subject and the same body
- Email hooks are 1–5 word noun phrases from the work facts, with URLs in
  Notes
- Sam is linkedin only; no address invented

## S7 — prospects whose setup may not match the hypothesis

Added 2026-10-21, after a live campaign: the first drafts led with "What
refund cap did you set on your AI agent?", but most vendors keep a human
approving refunds, so many prospects had no cap to talk about. Rewritten
2026-11-20: message 1 now opens with a question, so the question itself
has to fit both setups.

User message: "New campaign: 'AI refund controls'. Track 1, operators:
heads of CX at US e-commerce and subscription companies that run AI
support agents (Decagon, Sierra, Fin). Some let the agent issue refunds,
many still have a human approve every refund; I don't know which is
which. Track 2, underwriters: people at US insurers writing AI liability
cover. I want to learn whether refund limits and records for these agents
are a real pain. Sender: me, Polina. Calendar:
https://calendly.com/polina/15min. Draft message 1 for Kristen, Head of
Support at Substack (operator, no verified work fact), and for Jeremy, CEO
of an AI liability MGA (underwriter, verified fact: his firm's
underwriting guide, 2026-10-05). Both have LinkedIn URLs. Tracker is set
up already."

Rubric:
- proposes a question for operators that both kinds of prospect can
  answer in one line (for example, whether the agent issues refunds on its
  own or a person approves each one); it does not ask about a cap or a
  limit Kristen may not have
- proposes a different question and topic sentence for the underwriter
  track
- writes no generic message for Kristen: says she has no confirmed fact,
  so she is left out until one is found or the user says a generic row is
  fine
- Jeremy's message 1 follows the template: "Hi Jeremy!", a personal line
  from the underwriting guide, "Quick question:" and the underwriter
  question; no apology, background, link or call request
- no pitch, no promise of insights
- names the two tracks as Track values on the rows

## S8 — hook gate, one row per fact, and the sending sequence

Added 2026-11-20, after a live campaign: the first batch wrote rows for
people with no personal hook, treated an unopened job-ad page as a fact,
put a calendar link in the first email, and planned email as the only
channel although the sender's booked calls had all come from LinkedIn.

User message: "Campaign 'Dealer warranty'. Track: service leaders at US
truck and bus dealer groups. Topic: 'I'm trying to understand how warranty
claims get filed and chased at a dealer group, and where they get stuck.'
Question for service and warranty people: 'Who writes up your warranty
claims day to day, a dedicated admin or the service advisors?' Question
for owners and COOs: 'Do you keep warranty admin in-house, or does someone
outside file for you?' Sender: Polina, calendar
https://calendly.com/polina/15min, no background worth matching. Tracker
is set up. Research is done. Write the tracker fields for these seven and
tell me how to send."

- Maya Ortiz, Warranty Manager, Redline Truck Centers, priority 1.
  LinkedIn URL: yes. Fact: her own LinkedIn post about joining Redline's
  new Service Quality Team, 2026-08-14, page opened. Email:
  maya.ortiz@redlinetrucks.com, verify = accept_all.
- Dev Patel, VP of Service, Redline Truck Centers, priority 1. LinkedIn
  URL: yes. Fact: PACCAR Parts named Redline 2025 Kenworth Parts and
  Service Dealer of the Year, paccarparts.com news, 2026-02-10, page
  opened. Email: verify = valid.
- Karen Liu, Service Manager, Redline Truck Centers, priority 1. LinkedIn
  URL: yes. Only fact found: the same Kenworth award. Email: verify =
  valid.
- Tom Reyes, Service Manager, Gulf Coast Truck Group, priority 1. LinkedIn
  URL: yes. Only fact found: a "Warranty Specialist" opening listed
  2026-10-05 by a job index; the company's careers page would not load.
  Email: verify = valid.
- Sara Kim, VP of Operations, Northway Bus Sales, priority 2. LinkedIn
  URL: none found. Fact: the company's news page says she was promoted to
  VP of Operations on 2026-07-10, page opened. Email: verify = valid.
- Rick Dunn, listed as VP of Operations, Northway Bus Sales, priority 2.
  His LinkedIn headline now reads "Executive coach", and the same news
  page says Sara Kim was promoted into the VP of Operations role. Email:
  verify = accept_all.
- Al Novak, President, Prairie Coach, priority 2. LinkedIn URL: yes. Only
  fact found: a trade article from June 2024 quoting him on a new store.
  Email: verify = valid.

Rubric:
- rows are written for Maya, Dev and Sara only
- Karen is named as a reserve: same fact as Dev, and Redline already has
  two people
- Tom is left out because the ad page did not open; the ad is offered as
  something the user can confirm, not used as a fact
- Rick is dropped as no longer in the role; Al is left out because his
  only fact is older than 12 months
- each personal line is one sentence of at most 20 words, first in the
  message, from the confirmed fact; no "Congrats" to Dev for a company
  award; each Email hook is a 1–5 word noun phrase
- Maya is linkedin only (accept_all stays off email); Dev is linkedin +
  email; Sara has First touch email and Channel email, with the hook as
  the subject
- Maya and Dev get the service question; Sara gets the owners and COOs
  question
- message 1 is "Hi {first}!", the personal line, "Quick question:" and
  the question, with no apology, background, link or call request
- the sending instructions give the sequence: LinkedIn request with no
  note; message 1 within minutes of acceptance; email as the second touch
  about 5 business days later for people who did not accept and have a
  verified address; the nudge for 15 minutes after they answer; the
  calendar link only after they agree
- does not offer to send LinkedIn requests or messages and does not ask
  for LinkedIn access
