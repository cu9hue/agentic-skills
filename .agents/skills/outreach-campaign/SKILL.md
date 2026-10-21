---
name: outreach-campaign
description: "Use when the user wants to run or continue a cold-outreach campaign for customer discovery: find companies for an ICP, find and verify people's emails, write hooks and drafts, fill the Notion outreach tracker. Also use when they ask what to get right in cold outreach for discovery calls. Not for replying to a prospect who already answered, or for one-off messages outside a campaign."
origin: "The author's own cold-outreach pipeline, tracker schema and message templates. Tool mechanics from the treg skill in this repo."
---

# Outreach Campaign

Run one batch of the user's cold-outreach pipeline for any ICP: discover
companies, screen them, find people, find and verify emails, personalize by
priority, write tracker rows, report. The goal is discovery calls: 15 minutes of a
prospect's advice. Never a sale.

Schema, formulas, templates and copy rules live in
`references/notion-and-templates.md`. Read it before step 5.

## Hard rules

- **US only. Never EU.** Reject a company whose team, engineering or
  customers sit in the EU, even with a US headquarters. Do not ask the user
  about it; reject it and say why.
- **Search with Exa and treg only.** Never use WebSearch. Never query a
  search engine through curl.
- **Never guess an email address.** Only use an address a provider returned,
  and verify every one.
- **Never use an unverified fact or connection in a hook.** Open the source
  and confirm it on the page.
- **Never pitch, and never promise insights the user does not have.** No
  "I'll share what I learn", no "happy to send a summary". The ask is 15
  minutes of advice.
- **Never create or change the tracker without a yes.** Propose the setup
  in step 0 and build only the parts the user agreed to.
- **Quote the cost before spending; report actual spend after.** The budget
  cap is the user's go-ahead for the batch. Stop and ask before any step that
  would cross it.

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
| Topic sentence per track (below) | draft one from the one-liner and ask the user to confirm |
| Sender: name, background sentence (below), calendar link | none, ask; no calendar link is a valid answer |
| Sender background worth matching for this ICP | none, discuss (below) |
| LinkedIn note | off; build it only if the user asks |

**Topic sentence.** What the sender wants to learn, in the form "I'm
looking to understand how {workflow} {works} now that {change}", at most
30 words: "I'm looking to understand how refunds and credits get approved
considering AI agents are taking over support." It names the workflow and
the change, and it stays true for every prospect in the track, including
those whose setup differs from the hypothesis. Never open with a question
about the prospect's own setup ("what cap did you set on your agent?"): a
prospect it does not fit will not reply. The specific questions belong on
the call.

**Background sentence.** One sentence, at most 25 words, that signals
competence to this ICP: "I spent 6 years in finance building trading and
risk systems, and I've built AI agents in production." Keep it consistent
with the sender's public profile, since prospects check. Leave out any
industry or employer that would put this ICP off, and say why when you
propose the cut.

**Sender background.** Ask for the sender's schools, past employers and
field, and communities. Then name which of them a prospect in this ICP
would care about, and say why. Agree on that short list with the user.
"None" is a valid outcome: then priority 1 skips the connection search and
no row gets a Connection.

**Tracker setup.** Propose it and let the user drop parts:

- **Outreach database**: the core. Dedupe and per-person tracking need it.
- **Calls database** and its relation: skip if they log calls elsewhere.
- **The three views**: skip if they will build their own.
- **Draft formula** (Email draft, plus LinkedIn note if asked for): skip if
  they write the messages themselves. Rows still get Subject, Connection and
  Email hook.

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
   exists, and the draft formula if the user kept it), then the views. If
   the databases exist from an older template (no Topic property), tell
   the user what would change: new Track, Topic, Background, Calendar,
   Connection and Opener properties, Credential, Intro, Lead question and
   Cohort removed, and a new draft formula that rewrites the drafts on
   unsent rows. Change them only after a yes.
3. Query Outreach for every existing Company. Merge them with the exclusion
   list into one **skip list**.

## Step 2 — discover companies

With an existing target list, skip this step and screen the list in step 3.

- Tools: Exa MCP (`mcp__plugin_exa_exa__web_search_exa`,
  `mcp__plugin_exa_exa__web_fetch_exa`) and treg `exa.companies.search`
  (~$0.007/call, semantic).
- Write several descriptive queries per ICP angle. Describe the company, not
  keywords: "US startup whose AI agents resolve card disputes for credit
  unions". Vary the angle: the product, the buyer, the workflow, the named
  customer type.

```bash
treg balance   # record the starting balance
treg --json call exa.companies.search --method POST \
  --data '{"query":"<description>","category":"company","numResults":10}'
```

- Gather about twice the batch size, then screen.

## Step 3 — screen for fit

Drop anything on the skip list first, and name why. Then judge each company
against the fit criteria and assign priority 1, 2 or 3. Reject, with a
one-line reason, anything that is:

- **wrong geography**: outside the US, or an EU team or EU customers
- **wrong side of the market**: a buyer (a bank, a credit union), not a
  vendor that sells to them
- **defunct or pivoted**: acquired, shut down, stale site, now selling
  something else
- **unverifiable team**: no named founders or no profiles you can match
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
   `"pagination":{"size":<n>}` set to what you need. Search CEO/founder
   first; if you need a second person, then CTO, then sales or partnerships.
3. To confirm a person already named on the target list, search by first
   and last name only, then check the current company and title on each
   row: an exact company-name filter misses people whose profile spells the
   company differently. When the named person is gone, search the company
   domain for the role instead and use who is there now.
4. Keep at most 2 people per company. Drop any profile whose current company
   or title does not match. Keep each priority-1 person's past roles and
   education from the row; step 6 checks them for connections.

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

- Run the find once per person. Never re-run a find; every hit bills.
- Verify every address the find returns. Record Email check as one of:
  `valid`, `valid-risky`, `accept_all`, `invalid`, `not found`.
- On a miss, record `not found` and leave Email empty. Do not build an
  address from a pattern.
- Run a handful first and check the parsed output before looping.
- In a `while read` loop, give every `treg` call `< /dev/null`, or it reads
  the loop's input and the loop hangs. macOS has no `timeout` command.

## Step 6 — personalize by priority

The depth of research follows priority. Spend it where a reply is worth the
most.

| Priority | Research | Personalization |
| --- | --- | --- |
| 1 | a connection **and** one work fact; work fact only if the sender background is "none" | `both`, `connection` or `work` |
| 2 | one work fact, a quick pass | `work`, or `none` if nothing passes |
| 3 | none | `none` |

- **Connection**: something the person shares with the sender background
  agreed in step 0: a school, a past employer or field, or a community.
  Nothing outside that list counts. Confirm it on their profile, team page or bio. A guess from a
  name or a city does not count.
- **Work fact**: one fact that is **recent** (published in the last ~12
  months), **verifiable** (you opened the page and the fact is on it;
  primary sources only: the company's site, a customer's or partner's site,
  a news outlet, the person's own post or talk; never a directory,
  listicle or aggregator) and **specific** (a named customer, a launch,
  funding, a partnership, a certification, or the person's own post or
  talk). Prefer the person's own post or talk.

A priority-1 person with neither gets `none` and goes under "Check" in the
report. Put every source URL in Notes, for connections as well as facts,
with the fact's date.

Then write, per the copy rules in the reference:

- **Subject**: "15 min chat?" on every row.
- **Connection**: only with a connection. A plural noun phrase of 1–5 words
  that completes "We're both …": "MIT alums", "ex-Halcyon quants", "EF
  founders". Empty otherwise.
- **Email hook**: only with a work fact. A noun phrase of 1–5 words that
  completes "Saw …": "the Chartway case study", "your SR 11-7 post", "the
  AutoPost launch". No verb, no flattery, no em dash. Empty otherwise.

The formula turns these into one closing sentence after the topic: "We're
both {connection}, and I saw {hook}, which is why I thought of you", or
the half that exists, or nothing.

Check each row before writing it: count the words in Connection and Email
hook, and search both for "—". If the user asked for the LinkedIn note,
confirm it is under 300 characters; if it is over, shorten the hook.

## Step 7 — write rows to Notion

With no tracker, skip this step and put the rows in the report as a table.

One row per person:

- Status: `To send`
- Personalization: `both`, `connection`, `work` or `none`, from step 6.
- Track and Topic: the person's track and its confirmed topic sentence.
- Sender, Background and Calendar: from step 0, the same on every row of
  the batch.
- Opener: `apology` unless the user dropped it.
- Channel: `email` if Email check is `valid`, `valid-risky` or
  `accept_all`, plus `linkedin` when the address is `accept_all`; otherwise
  `linkedin` only, and the user writes that note by hand unless the
  LinkedIn note is on.
- Fill every other field from steps 3–6. If the user kept the draft
  formula, Email draft fills itself.

If the draft formulas exist, read the first row's Email draft back and
check the line breaks (see the reference).

## Step 8 — report

Run `treg balance` again. Then report, in this order:

1. **Companies added**: priority, why they fit, who they sell to.
2. **People**: name, title, company, email status, channel, personalization.
3. **Rejected**: company and one-line reason, grouped by reason.
4. **Spend**: balance before and after, and the difference.
5. **Check**: anything the user should look at before sending. For example,
   a hook fact you could only half confirm, a profile that might be stale,
   an `accept_all` address, or a person left out for lack of a hook.

## Operating advice

Give this the first time the user runs a campaign, and whenever they ask
what to get right in cold outreach:

- Lead with what you want to learn, not with a question about their setup.
  A broad topic fits everyone in the track; the sharp questions go on the
  call.
- Send in batches of ~10–20, Monday to Wednesday, so "this week" in the
  draft has days left. Follow up after ~3 business days. If a batch gets
  zero replies, change the message before you spend more good prospects.
- Don't use open tracking. Track replies by hand in Notion. After a few
  batches, compare reply rates by Personalization: if `none` replies as
  well as `work`, stop researching priority 2.
- `accept_all` means the domain accepts any address, so delivery is
  unconfirmed: send a LinkedIn message too. Mark a bounce `invalid` and
  switch that person to LinkedIn.
- Expect ~5–10% replies on well-targeted cold outreach. Plan volume to
  match: 5 calls takes roughly 50–100 sends.
- Ask for 15 minutes of advice. Never pitch, and never promise insights you
  don't have.
