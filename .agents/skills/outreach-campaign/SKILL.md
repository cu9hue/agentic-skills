---
name: outreach-campaign
description: "Use when the user wants to run or continue a cold-outreach campaign for customer discovery: find companies for an ICP, find people, verify emails, write personal lines, questions and drafts for LinkedIn and email, fill the Notion outreach tracker. Also use when they ask what to get right in cold outreach for discovery calls. Not for replying to a prospect who already answered, or for one-off messages outside a campaign."
origin: "The author's own cold-outreach pipeline, tracker schema and message templates. Message shape from the author's LinkedIn messages that booked calls, and from Entrepreneur First's outreach advice (connect with no note, message on acceptance, open with a specific question). Tool mechanics from the treg skill in this repo."
---

# Outreach Campaign

Run one batch of the user's cold-outreach pipeline for any ICP: discover
companies, screen them, find people, find and verify emails, write a
personal line for each person, write tracker rows, report. The goal is
discovery calls: 15 minutes of a prospect's advice. Never a sale.

The message is three short sentences and works the same on LinkedIn and
email: a personal line, then one specific question. The call is asked for
only after they answer. Schema, formulas, templates and copy rules live in
`references/notion-and-templates.md`. Read it before step 5.

## Hard rules

- **US only. Never EU.** Reject a company whose team, engineering or
  customers sit in the EU, even with a US headquarters. Do not ask the user
  about it; reject it and say why.
- **Search with Exa and treg only.** Never use WebSearch. Never query a
  search engine through curl.
- **Never guess an email address.** Only use an address a provider returned,
  and verify every one. Never put an `invalid`, `not found` or `accept_all`
  address on the email channel.
- **Never use an unverified fact in a personal line or a subject.** Open
  the source and confirm it on the page. A page that would not open is not
  a source.
- **No personal line, no row.** A person with no confirmed personal line
  is left out of the tracker and listed in the report. Write a generic row
  only if the user says generic rows are fine.
- **Never pitch, and never promise insights the user does not have.** No
  "I'll share what I learn", no "happy to send a summary". The ask is 15
  minutes of advice.
- **No link in a first message.** No calendar link, no tracking, no
  signature link. The calendar link goes in the reply after they agree to
  talk.
- **Never operate the user's LinkedIn or ask for their LinkedIn data.** The
  user sends every request and message by hand. Draft and track only.
- **Never create or change the tracker without a yes.** Propose the setup
  in step 0 and build only the parts the user agreed to.
- **Quote the cost before spending; report actual spend after.** The budget
  cap is the user's go-ahead for the batch. Stop and ask before any step that
  would cross it.

## The sequence

1. **LinkedIn request with no note.**
2. **Message 1 within minutes of the acceptance**: the personal line and
   the question.
3. **Email as the second touch**, about 5 business days after the request,
   for people who have not accepted and have a `valid` or `valid-risky`
   address. Same message, with the hook as the subject.
4. **Nudge for the call after they answer**: thanks, the topic sentence,
   15 minutes.
5. **The calendar link or two concrete times** once they agree, within the
   hour.

A person with no LinkedIn URL starts at step 3. The user may ask for a
split instead (half LinkedIn first, half email first); then set First touch
per row and report results by it.

## Step 0 — inputs

Collect these. Ask for every missing one in **one** message, and state the
defaults instead of asking about them:

| Input | Default |
| --- | --- |
| Campaign name and one-liner | none, ask |
| ICP: role + company type | none, ask |
| Fit criteria for priority 1 / 2 / 3 | none, ask (offer a draft from the ICP if the user wants one) |
| Buyers they sell to, as a plural noun ("credit unions") | from the ICP |
| Geography | US only, never EU |
| Exclusion list (companies already contacted) | none, ask; "none" is a valid answer |
| Tracker: a Notion parent page URL and a yes to the setup (below), or "no tracker" | none, ask |
| treg budget cap | $2 per batch |
| Batch size | 15–20 companies, max 2 people each |
| Existing target list (a file or a list of companies and people) | none; when given, screen it in step 3 instead of running discovery |
| Tracks: the distinct audiences in this campaign ("operators", "underwriters") | one track |
| Topic sentence per track (below) | draft one and ask the user to confirm |
| Question per role group (below) | draft one per group and ask the user to confirm |
| Opener | `question`; `advice` for a group with no question that fits |
| First touch | LinkedIn, email as the second touch |
| Sender: first name and calendar link | none, ask; no calendar link is a valid answer |
| Sender background worth matching for this ICP | none, discuss (below) |
| Finding per track, for the follow-up | none; optional |

**Topic sentence.** What the sender wants to learn, at most 25 words. When
the campaign tests one workflow, name it: "I'm trying to understand how
warranty claims get filed and chased at a dealer group and where they get
stuck." When the campaign is open discovery, use the role: "I am currently
trying to learn more about the day to day of a fractional CFO." It stays
true for every prospect in the track. Open discovery gets general calls; a
named workflow gets calls on the subject, so prefer it once there is a
hypothesis.

**Question.** One question per role group, for message 1. It must pass
three tests:

- they can answer it in one line from memory;
- it asks for a fact, not an opinion, and nothing sensitive (no revenue,
  margin or customer names);
- it is true for everyone in the group. Never assume a setup: "what cap
  did you set on your agent?" fails for every prospect with no cap.

An either/or form helps: "Who writes up your warranty claims day to day? A
dedicated admin or the service advisors?" Each answer should teach
something even if no call follows. If no question passes all three tests
for a group, use the `advice` opener for that group.

**Light punctuation.** Messages carry no colon, semicolon or comma (copy
rules in the reference). Store the confirmed topic sentence and question
that way, and show the user the stored text: drop each comma, or split
the sentence in two. Never change a word.

**Sender background.** Ask for the sender's schools, past employers and
field, and communities. Then name which of them a prospect in this ICP
would care about, and say why. Agree on that short list with the user.
"None" is a valid outcome: then no personal line uses a connection. The
message carries no background sentence; the sender's LinkedIn profile does
that job, so say once that it should be current.

**Finding.** One sourced fact the user owns, per track, to put in the
follow-up: "219 US companies advertised for warranty staff in the last 45
days." Without one, the follow-up is the plain bump.

**Tracker setup.** Propose it and let the user drop parts:

- **Outreach database**: the core. Dedupe and per-person tracking need it.
- **Calls database** and its relation: skip if they log calls elsewhere.
- **The four views**: skip if they will build their own.
- **Draft formulas** (Message, Email draft, Nudge): skip if they write the
  messages themselves. Rows still get Personal line, Question and Email
  hook.

"No tracker" is a valid answer: dedupe against the exclusion list only,
skip step 7, and give the rows in the report.

Do not run discovery or spend anything until you have the exclusion list and
the tracker answer. Free reads (the Notion query in step 1) can run as soon
as the page URL arrives.

## Step 1 — tracker and dedupe

With no tracker, skip this step; the skip list is the exclusion list.

1. Load the Notion tools (`ToolSearch "notion"`). If none are connected,
   stop and tell the user to connect Notion.
2. Look under the parent page for the Outreach and Calls databases. If they
   are missing, create the parts the user agreed to, exactly as in the
   reference: Calls first, then Outreach (with the relation if Calls
   exists, and the draft formulas if the user kept them), then the views.
   If the databases exist from an older template (no Personal line
   property), tell the user what would change: new Personal line, Question
   and First touch properties; Opener options become `question` and
   `advice`; Status gains `Request sent` and `Accepted`; Subject becomes
   the hook; Background, Calendar-in-draft and Connection go; the draft
   formulas are rewritten on unsent rows. A tracker with no Variant
   property gets one, and the three formulas change with it. Change them
   only after a yes.
3. Query Outreach for every existing Company. Merge them with the exclusion
   list into one **skip list**.

## Step 2 — discover companies

With an existing target list, skip this step and screen the list in step 3.

Two sources. Use the second whenever the ICP has a job that companies
advertise for.

**By description.** Exa MCP (`mcp__plugin_exa_exa__web_search_exa`,
`mcp__plugin_exa_exa__web_fetch_exa`) and treg `exa.companies.search`
(~$0.007/call, semantic). Write several descriptive queries per ICP angle.
Describe the company, not keywords: "US startup whose AI agents resolve
card disputes for credit unions". Vary the angle: the product, the buyer,
the workflow, the named customer type.

```bash
treg balance   # record the starting balance
treg --json call exa.companies.search --method POST \
  --data '{"query":"<description>","category":"company","numResults":10}'
```

**By job ad.** A company that advertises for the task has a funded pain
and a reason to hear from the user this week. Count first (free), then
pull rows with descriptions (~$0.0015/row):

```bash
treg --json call hirebase.jobs.search.count --method POST \
  --data '{"job_titles":["warranty"],"geo_locations":[{"country":"United States"}],"days_ago":45,"limit":0}'
treg --json call hirebase.jobs.search --method POST \
  --data '{"job_titles":["warranty"],"geo_locations":[{"country":"United States"}],"days_ago":45,"limit":100}'
```

- `keywords` matches loosely; check that the phrase is in the description
  before trusting a row.
- Keep the ad's title, date and link for Notes.
- Check company size against the ICP. Companies that advertise for a
  specialist are often larger than the ICP; then find the ICP by
  description instead and say so.
- An ad is a reason to research a company, not proof of need.

Gather about twice the batch size, then screen.

## Step 3 — screen for fit

Drop anything on the skip list first, and name why. Then judge each company
against the fit criteria and assign priority 1, 2 or 3. Reject, with a
one-line reason, anything that is:

- **wrong geography**: outside the US, or an EU team or EU customers
- **wrong side of the market**: a buyer (a bank, a credit union), not a
  vendor that sells to them
- **defunct or pivoted**: acquired, shut down, stale site, now selling
  something else
- **unverifiable team**: no named people or no profiles you can match
- **weak fit**: it does not do the thing the ICP describes

For each kept company record: priority, why it fits (one line), Segment
(the ICP angle), and Their customers (the plural noun). Keep 15–20.

## Step 4 — find people

Use treg Icypeas. Pass JSON inline with `--data`.

1. Always run the free count first, and tune the query until the count is
   sane:

```bash
treg --json call icypeas.people.search.count --method POST --data '{"query":{"currentCompanyWebsite":{"include":["ledgerline.ai"]},"currentJobTitle":{"include":["CEO","Founder","Co-Founder"]}}}'
```

2. Then fetch rows with `icypeas.people.search` (~$0.0004/row), same query,
   `"pagination":{"size":<n>}` set to what you need. Search the ICP's role
   first; if you need a second person, the role above it.
3. To confirm a person already named on the target list, search by first
   and last name only, then check the current company and title on each
   row: an exact company-name filter misses people whose profile spells the
   company differently. When the named person is gone, search the company
   domain for the role instead and use who is there now.
4. Keep at most 2 people per company, and keep each person's LinkedIn URL.
   Drop any profile whose current company or title does not match. Keep
   each priority-1 person's past roles and education from the row; step 6
   checks them for connections.

## Step 5 — find and verify emails

Say the expected cost first: people × up to $0.03 for finds, verifies
usually free.

```bash
treg --json call treg.people.email.find --method POST \
  --header 'X-Treg-Route-Max-Cost: 0.03' \
  --data '{"first_name":"Dana","last_name":"Ruiz","domain":"ledgerline.ai"}'

treg --json call treg.people.email.verify --method POST \
  --header 'X-Treg-Route-Max-Cost: 0.01' \
  --data '{"email":"dana@ledgerline.ai"}'
```

- Run the find once per person. Never re-run a find; every hit bills. For
  a person whose surname is unknown, pass `{"linkedin_url": …}` instead.
- Verify every address the find returns. Record Email check as one of:
  `valid`, `valid-risky` (the verifier confirms the mailbox on a catch-all
  domain), `accept_all` (unconfirmed), `invalid`, `not found`.
- On a miss, record `not found` and leave Email empty. Do not build an
  address from a pattern.
- Run a handful first and check the parsed output before looping.
- In a `while read` loop, give every `treg` call `< /dev/null`, or it reads
  the loop's input and the loop hangs. macOS has no `timeout` command.

## Step 6 — the personal line

Every row needs one. Research until each person has a confirmed fact or
is left out.

**The fact** is one of:

- **Connection**: something the person shares with the sender background
  agreed in step 0. Confirm it on their profile, team page or bio. A guess
  from a name or a city does not count.
- **Work fact**: **recent** (dated in the last ~12 months), **verifiable**
  (you opened the page and the fact is on it; primary sources only: the
  company's site, a customer's or partner's site, a trade or news outlet,
  the person's own post or talk; never a directory, listicle or
  aggregator) and **specific** (a named customer, a launch, an
  acquisition, an award, a new location, a promotion, or the person's own
  post, talk or quote).

Rank work facts and take the highest that exists: (1) something the person
said or wrote; (2) something about the person, such as a promotion; (3) a
fact about their own function; (4) general company news. Priority 1 gets a
search for levels 1 and 2 before settling. Priority 2 and 3 may take the
first confirmed fact.

**Rules**

- Two people at one company with the same fact: write one row. Name the
  other as a reserve in the report.
- A job ad is a usable fact only if its page opened. Otherwise put the
  link in Notes as an option for the user to confirm.
- Check that the person still holds the role. A newer profile or a
  promotion notice for someone else is a reason to drop or replace them.
- Put every source URL in Notes with the fact's date.

Then write, per the copy rules in the reference:

- **Personal line**: one sentence in the sender's voice, at most 20 words,
  built from the fact: "Saw your post about being part of the Service
  Improvement Team." "Congrats on the Hudson Bus acquisition." "Fellow MIT
  alum here." No flattery, no em dash. "Congrats" only for something that
  happened to the person or that they led: a promotion, an acquisition
  they ran. Never for a company award sent to an employee; write "Saw
  that …" for those.
- **Email hook**: the same fact as a noun phrase of 1–5 words. It is the
  email subject: "your Service Improvement Team post".
- **Question**: the confirmed question for the person's role group,
  starting in lower case so it reads after the bridge ("Quick question -").
- **Personalization**: `both`, `connection` or `work`.

Check each row before writing it: count the words in Personal line and
Email hook; search Personal line, Question and Topic for "—", ":", ";"
and ","; and confirm the source is in Notes.

## Step 7 — write rows to Notion

With no tracker, skip this step and put the rows in the report as a table.

One row per person:

- Status: `To send`
- Track and Topic: the person's track and its confirmed topic sentence.
  In a campaign with more than one track, name the Track value next to
  every row and every draft you show, also before the rows are written.
- Personal line, Email hook, Question, Personalization: from step 6.
- Opener: `question`, or `advice` for a group with no fitting question.
- Variant: `A`, `B`, `C` in rotation down the rows. Two people at one
  company never share one. It picks the bridge and the sign-off, so no
  two people there read the same wording.
- First touch: `linkedin` when the row has a LinkedIn URL, else `email`.
- Channel: `linkedin` when there is a URL; add `email` only when Email
  check is `valid` or `valid-risky`.
- Sender and Calendar: from step 0, the same on every row of the batch.
- Fill every other field from steps 3–6. If the user kept the draft
  formulas, Message, Email draft and Nudge fill themselves.

If the draft formulas exist, ask the user to open the first row and check
the drafts (see the reference).

## Step 8 — report

Run `treg balance` again. Then report, in this order:

1. **Companies added**: priority, why they fit, who they sell to.
2. **People**: name, title, company, first touch, email status, the level
   of the fact behind the personal line.
3. **Left out**: people with no confirmed personal line, reserves, and
   people who appear to have left.
4. **Rejected**: company and one-line reason, grouped by reason.
5. **Spend**: balance before and after, and the difference.
6. **Check**: anything the user should look at before sending. For example,
   a weak level-4 fact, a job-ad link to confirm, a profile that might be
   stale, a `valid-risky` address.

## On the call

The message earns the call; the call has to end in a test. When the user
asks for a call plan, give five questions for the track's workflow:

1. Tell me about the last time it went wrong (the last denied claim, the
   last cost increase that reached prices late).
2. How often does that happen, and what is it worth?
3. Who handles it, and how many hours does it take?
4. What have you tried: a tool, an outside service, a hire?
5. A small commitment: "If I did X for five of these and you paid only on
   the result, would you send them?" or "Could I look at one slice of the
   data under an NDA?"

The fifth is the point. A yes is a first customer and a no says why.
Without it, calls stay general and no offer comes out of them. Log the
answer in the Calls database under Commitment.

## Operating advice

Give this whenever the user asks what to get right in cold outreach, and
with the first batch's report. Never in the step 0 message: that one
holds the questions and the defaults only, so the user can answer it on
one pass.

- Connect on LinkedIn with no note, and message within minutes of the
  acceptance. This sequence has booked the author's calls; email has not
  yet. Run both and count calls per person approached, by First touch.
- Message 1 is a personal line and one specific question. Ask for the
  call only after they answer. A question they can answer in one line gets
  a reply; a request for time from a stranger often does not.
- Keep it to three sentences. No apology, no background, no link. Their
  first look at who you are is your LinkedIn profile, so keep it current.
- Type it like a message, not a document: no colons, no commas, and the
  wording varies by Variant. Identical, tidy text is what a reader and a
  spam filter both recognise as a template.
- Send about 15 to 20 LinkedIn requests a day, Monday to Wednesday.
  LinkedIn limits weekly invitations.
- Track acceptance apart from replies. A low acceptance rate is a list or
  profile problem; a low reply rate after acceptance is a message problem.
- Email only verified addresses, in plain text. Before a batch's first
  email, send the draft to your own Gmail and Outlook accounts and see
  where it lands. Mark a bounce `invalid`.
- Reply within the hour when someone agrees to talk, with two times or
  the calendar link.
- Follow up once after ~3 business days, with the track's finding if there
  is one. If a batch gets zero replies, change one thing in the message
  before you spend more good prospects.
- Don't use open tracking. Track by hand in Notion. After a few batches,
  compare by Opener and by First touch.
- Expect ~5–10% of people approached to reply. Plan volume to match: 5
  calls takes roughly 50–100 people.
- Never pitch, and never promise insights you don't have. End each call
  with the small commitment question.
