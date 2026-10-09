---
name: outreach-campaign
description: "Use when the user wants to run or continue a cold-outreach campaign for customer discovery: find companies for an ICP, find and verify people's emails, write hooks and drafts, fill the Notion outreach tracker. Also use when they ask what to get right in cold outreach for discovery calls. Not for replying to a prospect who already answered, or for one-off messages outside a campaign."
origin: "The author's own cold-outreach pipeline, tracker schema and message templates. Tool mechanics from the treg skill in this repo."
---

# Outreach Campaign

Run one batch of the user's cold-outreach pipeline for any ICP: discover
companies, screen them, find people, find and verify emails, write hooks,
write tracker rows, report. The goal is discovery calls: 15 minutes of a
founder's advice. Never a sale.

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
- **Never use an unverified fact in a hook.** Open the source and confirm the
  fact on the page.
- **Never pitch, and never promise insights the user does not have.** No
  "I'll share what I learn", no "happy to send a summary". The ask is 15
  minutes of advice.
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
| Notion parent page URL | none, ask |
| treg budget cap | $2 per batch |
| Batch size | 15–20 companies, max 2 people each |
| Variant B question (the suspected pain, as a curious question) | draft one from the one-liner and ask the user to confirm |

Do not run discovery or spend anything until you have the exclusion list and
the Notion page. Free reads (the Notion query in step 1) can run as soon as
the page URL arrives.

## Step 1 — tracker and dedupe

1. Load the Notion tools (`ToolSearch "notion"`). If none are connected,
   stop and tell the user to connect Notion.
2. Look under the parent page for the Outreach and Calls databases. If they
   are missing, create them exactly as in the reference: Calls first, then
   Outreach with the relation, the formulas filled in with this campaign's
   one-liner and B question, then the three views.
3. Query Outreach for every existing Company. Merge them with the exclusion
   list into one **skip list**.

## Step 2 — discover companies

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
3. Keep at most 2 people per company. Drop any profile whose current company
   or title does not match.

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

## Step 6 — write hooks

For each person, find **one** fact with Exa that is:

- **recent**: published in the last ~12 months
- **verifiable**: you opened the page and the fact is on it. Primary
  sources: the company's site, the customer's or partner's site, a news
  outlet, the person's own post or talk. Never a directory, listicle or
  aggregator.
- **specific**: a named customer, a launch, funding, a partnership, a
  certification, or the person's own post or talk. Prefer the person's own
  post or talk; otherwise use the company fact.

Put the source URL and its date in Notes. If no fact passes, write no row
for that person and list them under "Check" in the report.

Then write, per the copy rules in the reference:

- **Subject**: "question about your {launch / customer / post / talk}".
- **Email hook**: one sentence, "Saw …" or "Congrats on …", ≤22 words, no
  flattery, no em dash, no trailing period.
- **LinkedIn hook**: 3–8 words, lowercase start.

Check each one before writing the row: count the hook's words, search it for
"—", confirm the last character is not a period, and confirm the LinkedIn
note (built from the template) is under 300 characters.

## Step 7 — write rows to Notion

One row per person:

- Status: `To send`
- Variant: alternate A, B, A, B across priority-1 people who have an email
  channel. The variant changes only the email, so LinkedIn-only people and
  priority 2 and 3 get A.
- Channel: `email` + `linkedin` if Email check is `valid`, `valid-risky` or
  `accept_all`; otherwise `linkedin` only.
- Fill every other field from steps 3–6. Email draft and LinkedIn note are
  formulas; they fill themselves.

After the first row, read its Email draft back and check the line breaks
(see the reference).

## Step 8 — report

Run `treg balance` again. Then report, in this order:

1. **Companies added**: priority, why they fit, who they sell to.
2. **People**: name, title, company, email status, channel.
3. **Rejected**: company and one-line reason, grouped by reason.
4. **Spend**: balance before and after, and the difference.
5. **Check**: anything the user should look at before sending. For example,
   a hook fact you could only half confirm, a profile that might be stale,
   an `accept_all` address, or a person left out for lack of a hook.

## Operating advice

Give this the first time the user runs a campaign, and whenever they ask
what to get right in cold outreach:

- Send in batches of ~10–20. Follow up after ~3 business days on the other
  channel. If a batch gets zero replies, change the message before you
  spend more good prospects.
- Don't use open tracking. Track replies by hand in Notion.
- `accept_all` means the domain accepts any address, so delivery is
  unconfirmed: send the LinkedIn note too. Mark a bounce `invalid` and
  switch that person to LinkedIn.
- Expect ~5–10% replies on well-targeted cold outreach. Plan volume to
  match: 5 calls takes roughly 50–100 sends.
- Ask for 15 minutes of advice. Never pitch, and never promise insights you
  don't have.
