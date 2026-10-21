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
| Track | select | the campaign's tracks, e.g. Operator, Underwriter |
| Priority | select | 1, 2, 3 |
| Segment | select | the ICP angle the company came from |
| Their customers | text | plural noun that reads in a sentence: "credit unions" |
| Email | email | empty when not found |
| Email check | select | valid, valid-risky, accept_all, invalid, not found |
| LinkedIn | url | |
| Subject | text | "15 min chat?" |
| Sender | select | the sender's first name |
| Background | text | the sender's background sentence |
| Calendar | url | the sender's booking link; may be empty |
| Topic | text | the track's confirmed topic sentence |
| Opener | select | apology, none |
| Connection | text | completes "We're both …"; empty without one |
| Email hook | text | completes "Saw …"; empty without a work fact |
| Personalization | select | both, connection, work, none |
| Channel | multi-select | email, linkedin, intro |
| Status | select | To send, Sent, Followed up, Replied, Call booked, No reply, Not a fit |
| Sent | date | |
| Follow-up due | formula | `dateAdd(prop("Sent"), 4, "days")` |
| Email draft | formula | below |
| Notes | text | hook source URL + date, anything to check |
| Calls | relation | → Calls, two-way, shown there as `Person` |

Add a **LinkedIn note** formula only when the user asks for one.

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

Everything campaign-specific lives in row properties, so the formula is the
same for every campaign, track and sender.

Email draft:

```
"Hi " + prop("First name") + ",\n\n" + if(prop("Opener") == "apology", "sorry for the cold outreach!! no intention of selling, promise.\n\n", "") + "I'm " + prop("Sender") + ". " + prop("Background") + " " + prop("Topic") + if(empty(prop("Connection")), if(empty(prop("Email hook")), "", " Saw " + prop("Email hook") + ", which is why I thought of you."), " We're both " + prop("Connection") + if(empty(prop("Email hook")), "", ", and I saw " + prop("Email hook")) + ", which is why I thought of you.") + "\n\nwould you be down for a 15 min chat this week?" + if(empty(prop("Calendar")), "", " feel free to grab a time here: " + prop("Calendar")) + "\n\nThanks!\n" + prop("Sender")
```

LinkedIn note, only when asked for (under 300 characters):

```
"Hi " + prop("First name") + ", " + if(prop("Opener") == "apology", "sorry for the cold DM!! not selling, promise. ", "") + "I'm " + prop("Sender") + ". " + prop("Topic") + " 15 min this week?"
```

When the formula goes through SQL DDL, write each apostrophe in the text as
`''`.

After the first row is written, open it and check the Email draft. If `\n`
shows as literal text instead of line breaks, tell the user and fall back to
writing the drafts as plain text into the same property. The Notion API does
not return formula output, so ask the user to look if you cannot.

## Message templates

The voice: short, casual, slightly unpolished, lowercase where it reads
natural. No em dashes. The sender's signature block lives in their email
client; never add one to a draft.

Every draft does four jobs:

- **Disarm**: the opener says this is not a sales email.
- **Competence**: one background sentence the ICP would respect.
- **Curiosity**: the topic sentence says what the sender wants to learn,
  broad enough to fit everyone in the track.
- **Easy yes**: 15 minutes this week, with a calendar link when there is
  one.

**Email** (subject "15 min chat?")

```
Hi {first},

sorry for the cold outreach!! no intention of selling, promise.

I'm {sender}. {background} {topic}[ personal line]

would you be down for a 15 min chat this week? feel free to grab a time here: {calendar}

Thanks!
{sender}
```

The personal line is one of:

- connection and work fact: "We're both {connection}, and I saw {hook},
  which is why I thought of you."
- connection only: "We're both {connection}, which is why I thought of
  you."
- work fact only: "Saw {hook}, which is why I thought of you."
- none: nothing.

Example, `work`:

```
Hi Marcus,

sorry for the cold outreach!! no intention of selling, promise.

I'm Polina. I spent 6 years in finance building trading and risk systems, and I've built AI agents in production. I'm looking to understand how community banks review AI agents that move money now that examiners are asking about them. Saw the Harbor Trust rollout, which is why I thought of you.

would you be down for a 15 min chat this week? feel free to grab a time here: https://calendly.com/example/15min

Thanks!
Polina
```

**Follow-up** (~3 business days later, Monday to Thursday; on LinkedIn if
the email went unanswered and the person is there, otherwise in the same
email thread):

```
Hi {first}, bumping this. Wrapping up these calls in the next few days and still want your take. 15 min tomorrow or the day after?
```

## Copy rules

- Ask for 15 minutes of advice. Never promise insights the user does not
  have. Never pitch a product during discovery.
- Topic sentence: at most 30 words, "I'm looking to understand how … now
  that …". It names the workflow and the change. It never asks about the
  prospect's own setup, and it stays true for prospects whose setup
  differs from the hypothesis.
- Background sentence: at most 25 words, true to the sender's public
  profile, nothing that would put this ICP off.
- Subject: "15 min chat?". Never "Chartway x Ledgerline", never a
  partner's or customer's voice, never "Re:".
- Connection: a plural noun phrase of 1–5 words that completes "We're both
  …": "MIT alums", "ex-Halcyon quants", "EF founders".
- Email hook: a noun phrase of 1–5 words that completes "Saw …", no verb,
  no flattery ("impressive", "love", "amazing"), no em dash: "the Chartway
  case study", "your SR 11-7 post".
