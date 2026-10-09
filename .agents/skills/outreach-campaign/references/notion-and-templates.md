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
| Email hook | text | |
| LinkedIn hook | text | |
| Variant | select | A, B |
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

Replace `<ONE-LINER>` with the campaign one-liner, lowercase start, no
trailing period. Replace `<B-QUESTION>` with the confirmed Variant B
paragraph, with every "{their customers}" written as
`" + prop("Their customers") + "`.

Email draft:

```
if(prop("Variant") == "B",
  "Hi " + prop("First name") + ",\n\n" + prop("Email hook") + " and thought you might have some good insight into what I am working on\n\n<B-QUESTION>\n\nWould you be open to a quick call in the next week or two? Happy to work around your schedule\n\nThanks,\nPolina",
  "Hi " + prop("First name") + ",\n\n" + prop("Email hook") + " and thought you might have some good insight into what I am working on\n\nI'm <ONE-LINER>. You've clearly been through this with real " + prop("Their customers") + ", and I'd really value 15 minutes of your advice on how those conversations go\n\nWould you be open to a quick call in the next week or two? Happy to work around your schedule\n\nThanks,\nPolina"
)
```

LinkedIn note:

```
"Hi " + prop("First name") + ", " + prop("LinkedIn hook") + ". I'm <ONE-LINER> and would love 15 minutes of your advice on how you work with " + prop("Their customers") + "."
```

After the first row is written, read its Email draft back. If `\n` shows
as literal text instead of line breaks, tell the user and fall back to
writing the drafts as plain text into the same properties.

## Message templates

The user's voice: short, casual, slightly unpolished. No em dashes. The
signature (EF · Risk quant & AI engineer · LinkedIn) lives in the email
client; never add it to a draft.

**Email A (advice ask)**

```
Hi {first},

{email hook} and thought you might have some good insight into what I am working on

I'm {one-liner, lowercase start}. You've clearly been through this with real {their customers}, and I'd really value 15 minutes of your advice on how those conversations go

Would you be open to a quick call in the next week or two? Happy to work around your schedule

Thanks,
Polina
```

**Email B (pain as a question)**: Email A with the middle paragraph
replaced by one curious question about the suspected pain, e.g. "I'm
curious how you get {their customers} comfortable letting your agents act
on their own and whether that part ever slows a deal down".

**LinkedIn note** (under 300 characters; no background line, since they
see the profile):

```
Hi {first}, {LinkedIn hook}. I'm {one-liner} and would love 15 minutes of your advice on how you work with {their customers}.
```

**Follow-up** (~4 days later, on the other channel; if both channels are
already used, reply in the same email thread):

```
Hi {first}, following up on my note from {day}. Totally get it if now's busy. Would 15 minutes sometime next week work?
```

## Copy rules

- Ask for 15 minutes of advice. Never promise insights the user does not
  have. Never pitch a product during discovery.
- Subject: "question about your {launch / customer / post / talk}". It reads
  as an outsider asking. Never "Chartway x Ledgerline", never a partner's or
  customer's voice, never "Re:".
- Email hook: one sentence, starts "Saw …" or "Congrats on …", at most 22
  words, plain, no flattery ("impressive", "love", "amazing"), no em dash,
  no trailing period.
- LinkedIn hook: 3–8 words, lowercase start, e.g. "saw the Chartway
  disputes case study".
