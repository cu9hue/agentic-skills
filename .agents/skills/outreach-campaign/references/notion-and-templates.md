# Notion tracker and message templates

## Tracker layout

One tracker per campaign, under the campaign's Notion parent page: an
**Outreach** database and a **Calls** database, joined by a two-way relation
(Outreach `Calls` ↔ Calls `Person`). Create Calls first, then Outreach with
the relation.

### Outreach database

| Property | Type | Values / notes |
| --- | --- | --- |
| Name | title | full name |
| First name | text | |
| Company | text | used for dedupe |
| Title | text | job title |
| Priority | select | 1, 2, 3 |
| Segment | select | the ICP angle the company came from |
| Their customers | text | plural noun that reads in a sentence: "credit unions" |
| Email | email | empty when not found |
| Email check | select | valid, valid-risky, accept_all, invalid, not found |
| LinkedIn | url | |
| Subject | text | |
| Sender | select | the sender's first name |
| Credential | text | the sender's credential line, e.g. "Ex-risk quant, now at EF" |
| Intro | text | credential line naming a connection; empty without one |
| Email hook | text | what "puts you on that list"; empty without a work fact |
| Personalization | select | both, connection, work, none |
| Channel | multi-select | email, linkedin, intro |
| Status | select | To send, Sent, Followed up, Replied, Call booked, No reply, Not a fit |
| Sent | date | |
| Follow-up due | formula | `dateAdd(prop("Sent"), 4, "days")` |
| Email draft | formula | below |
| LinkedIn note | formula | below |
| Notes | text | hook source URL + date, anything to check |
| Calls | relation | → Calls, two-way, shown there as `Person` |

### Calls database

| Property | Type |
| --- | --- |
| Call | title |
| Date | date |
| Person | relation (← Outreach `Calls`) |
| Type | select: Discovery, Follow-up |
| Last case in numbers | text |
| Pain | text |
| Frequency | text |
| $ per occurrence | number (dollar) |
| Hours per occurrence | number |
| Who pays | text |
| Workaround and its cost | text |
| What they pay today | text |
| Kill tests touched | multi-select (add options as they come up) |
| What changed in my view | text |
| Next step | text |

### Views on Outreach

- **Send queue**: table, filter Status = To send, sort Priority ascending.
- **Follow up**: table, filter Status = Sent, sort Sent ascending.
- **Pipeline**: board grouped by Status.

If the Notion tool cannot create views, give the user these three lines to
add by hand.

### Formulas

Fill these per campaign:

- `<LEAD-QUESTION>`: the confirmed lead question, capital start.
  `<LI-QUESTION>`: the same, lowercase start.
- `<COHORT>`: the confirmed cohort, e.g. "with agents live at credit
  unions".

In each, write any "{their customers}" as `" + prop("Their customers") + "`.

Email draft:

```
"Hi " + prop("First name") + ",\n\n<LEAD-QUESTION>\n\n" + if(empty(prop("Intro")), if(empty(prop("Credential")), "", prop("Credential") + ". "), prop("Intro") + ". ") + "Talking to the few founders <COHORT> this week" + if(empty(prop("Email hook")), "", ", and " + prop("Email hook") + " puts you on that list") + ". 15 min Thu or Fri?\n\nThanks,\n" + prop("Sender")
```

LinkedIn note:

```
"Hi " + prop("First name") + ", <LI-QUESTION> " + if(empty(prop("Intro")), if(empty(prop("Credential")), "", prop("Credential") + ". "), prop("Intro") + ". ") + "Talking to the few founders <COHORT> this week" + if(empty(prop("Email hook")), "", ", and " + prop("Email hook") + " puts you on that list") + ". 15 min Thu or Fri?"
```

Sender and credential are row properties, not formula text, so one
tracker can carry batches from different senders.

After the first row is written, read its Email draft back. If `\n` shows
as literal text instead of line breaks, tell the user and fall back to
writing the drafts as plain text into the same properties.

## Message templates

The voice: short, casual, slightly unpolished. No em dashes. The sender's
signature block lives in their email client; never add one to a draft.

Every draft does three jobs in three lines:

- **Competence**: an insider question that names a real mechanism, then a
  credential line. The question shows the sender knows the domain before
  saying so.
- **FOMO**: the sender is talking to the few founders in the cohort this week,
  and their work puts them on that list.
- **This week**: "15 min Thu or Fri?" Never "next week or two", never
  "happy to work around your schedule", never "picking what to build".

**Email**

```
Hi {first},

{lead question}

{intro, or credential}. Talking to the few founders {cohort} this week[, and {email hook} puts you on that list]. 15 min Thu or Fri?

Thanks,
{sender}
```

Example, `work`:

```
Hi Marcus,

When a community bank's examiner reviews your wire agent, what do they actually ask to see?

Ex-risk quant, now at EF. Talking to the few founders with agents live at community banks this week, and the Harbor Trust rollout puts you on that list. 15 min Thu or Fri?

Thanks,
Polina
```

**LinkedIn note** (under 300 characters): the email body on one line,
"Hi {first}, {lead question, lowercase start} …", same fields.

**Follow-up** (~3 business days later, Monday to Thursday, on the other
channel; if both channels are already used, reply in the same email
thread):

```
Hi {first}, bumping this. Wrapping up these calls in the next few days and still want your take. 15 min tomorrow or the day after?
```

## Copy rules

- Ask for 15 minutes of advice. Never promise insights the user does not
  have. Never pitch a product during discovery.
- Lead question: at most 18 words, about their world, not the user's
  product. Name a real mechanism (a model risk review, an examiner, a
  sign-off) so it reads as from an insider.
- Cohort: a group the reader is proud to be in, and true of everyone the
  batch emails, priority 3 adjacent tooling included. If someone falls
  outside it, broaden the cohort; never drop the person to fit it.
- Subject: with a work fact, "question about your {launch / customer / post
  / talk}"; with only a connection, "question from a fellow {connection}";
  with none, "quick question about {topic}". It reads as an outsider
  asking. Never "Chartway x Ledgerline", never a partner's or customer's
  voice, never "Re:".
- Intro: at most 10 words, names the connection plainly and keeps the
  credential: "Fellow ex-Kestrel quant, now at EF", "Ex-risk quant and
  fellow EF founder", "Fellow Columbia alum, ex-risk quant, now at EF".
- Email hook: a noun phrase of 1–5 words, no verb, no flattery
  ("impressive", "love", "amazing"), no em dash: "Harbor Trust", "the Clearline
  launch", "your SR 11-7 post".
