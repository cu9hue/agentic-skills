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
| Email | email | empty when not found or not usable |
| Email check | select | valid, valid-risky, accept_all, invalid, not found |
| LinkedIn | url | |
| First touch | select | linkedin, email |
| Channel | multi-select | email, linkedin, intro |
| Sender | select | the sender's first name |
| Calendar | url | the sender's booking link; used in the reply, never in a draft |
| Topic | text | the track's confirmed topic sentence |
| Opener | select | question, advice |
| Variant | select | A, B, C: picks the wording of the bridge and the sign-off |
| Personal line | text | one sentence from a confirmed fact |
| Email subject | text | the subject line of the email: the same fact as a 1–5 word noun phrase |
| Question | text | the confirmed question for the person's role group |
| Personalization | select | both, connection, work |
| Status | select | To send, Request sent, Accepted, Sent, Replied, Followed up, Call booked, No reply, Not a fit |
| Sent | date | the day message 1 or the email went out |
| Follow-up due | formula | `dateAdd(prop("Sent"), 4, "days")` |
| Message | formula | below |
| Email draft | formula | below |
| Nudge | formula | below |
| Notes | text | source URL + date for the fact, anything to check |
| Calls | relation | → Calls, two-way, shown there as `Person` |

Status in order: `To send` → `Request sent` (LinkedIn request out) →
`Accepted` (send message 1 now) → `Sent` (message 1 or the email is out) →
`Replied` (they answered; send the nudge) → `Followed up` (nudge or bump
sent) → `Call booked`.

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
| Commitment | text (what was asked for at the end, and the answer) |
| Kill tests touched | multi-select (add options as they come up) |
| What changed in my view | text |
| Next step | text |

### Views on Outreach

- **Send queue**: table, filter Status = To send, sort Priority ascending.
- **Message now**: table, filter Status = Accepted.
- **Follow up**: table, filter Status = Sent, sort Sent ascending.
- **Pipeline**: board grouped by Status.

If the Notion tool cannot create views, give the user these four lines to
add by hand.

### Formulas

Everything campaign-specific lives in row properties, so the formulas are
the same for every campaign, track and sender.

Message (LinkedIn message 1, and the body of the email):

```
"Hi " + prop("First name") + "! " + prop("Personal line") + " " + if(prop("Opener") == "advice", prop("Topic") + " " + if(prop("Variant") == "B", "Would really appreciate 15 mins of your advice", if(prop("Variant") == "C", "Could I get 15 mins of your advice?", "Would love 15 mins of your advice")), if(prop("Variant") == "B", "Quick one for you", if(prop("Variant") == "C", "Curious", "Quick question")) + " - " + prop("Question"))
```

Email draft (the body; the subject line is the Email subject property):
the Message expression, then

```
+ "\n\n" + if(prop("Variant") == "B", "Thank you!", if(prop("Variant") == "C", "Thanks so much!", "Thanks!")) + "\n" + prop("Sender")
```

Nudge (after they answer the question):

```
"Thanks that helps a lot. " + prop("Topic") + " Could I get 15 mins of your advice this week?"
```

A row with no Variant reads as A.

When a formula goes through SQL DDL, write each apostrophe in its text as
`''`.

The Notion API does not return formula output. After the first row is
written, ask the user to open it and check the three drafts. If `\n` shows
as literal text in Email draft, tell the user and fall back to writing the
drafts as plain text into text properties of the same names.

## Message templates

The voice: short, casual, slightly unpolished, the way the sender would
type it by hand. Light punctuation: no colon, no semicolon, no comma, no
em dash (see the copy rules). The sender finishes each one by hand; the
draft is a starting point. The signature block lives in the email client;
never add one to a draft.

The templates use spintax: `{first}` is a field, and `{a|b|c}` is a choice
that the row's Variant picks (A the first, B the second, C the third).

Every message 1 does three jobs in at most three sentences (a short
either/or tail such as "Days or weeks?" does not count):

- **Personal**: the first sentence is about them, from a confirmed fact.
- **Small ask**: one question they can answer in a line, or 15 minutes of
  advice.
- **Nothing else**: no apology, no background sentence, no pitch, no link.

**Message 1, `question` opener** (LinkedIn after they accept; the same
body by email with the hook as subject)

```
Hi {first}! {personal line} {Quick question|Quick one for you|Curious} - {question}
```

Examples:

```
Hi Tonya! Saw your post about being part of the Service Improvement Team. Quick question - who writes up your warranty claims day to day? A dedicated admin or the service advisors?
```

```
Hi Josh! Congrats on the Hudson Bus Sales acquisition. Quick one for you - do you keep warranty admin in-house or does someone outside file for you?
```

**Message 1, `advice` opener** (for a group with no question that fits
everyone, and for open discovery)

```
Hi {first}! {personal line} {topic} {Would love 15 mins of your advice|Would really appreciate 15 mins of your advice|Could I get 15 mins of your advice?}
```

Example:

```
Hi Scott! Congrats on starting your own practice. I am currently trying to learn more about the day to day of a fractional CFO. Would love 15 mins of your advice
```

**Email** (second touch, or first touch for a person with no LinkedIn URL)

```
Subject: {email subject}

Hi {first}! {personal line} {Quick question|Quick one for you|Curious} - {question}

{Thanks!|Thank you!|Thanks so much!}
{sender}
```

**Nudge** (after they answer the question)

```
Thanks that helps a lot. {topic} Could I get 15 mins of your advice this week?
```

**When they agree** (within the hour; this is where the link goes)

```
Great thank you! I could do {time 1} or {time 2}. Or grab any slot here {calendar}
```

**Follow-up** (once, ~3 business days after message 1 with no answer, in
the same thread)

With the track's finding:

```
Hi {first}! One thing I found while looking into this - {finding}. Still curious about my question if you have a minute
```

Without one:

```
Hi {first}! Bumping this in case it got buried. Still curious if you have a minute
```

## Copy rules

- Ask for a one-line answer or for 15 minutes of advice. Never promise
  insights the user does not have. Never pitch a product during discovery.
- **Light punctuation.** A message reads as typed by hand, and a person
  typing a LinkedIn message does not punctuate like a document. In every
  message (message 1, the email, the nudge, the reply, the follow-up):
  - no colon, no semicolon, no comma, no em dash;
  - where a comma sat, drop it. If the sentence does not read without it,
    split it in two: "who writes up your warranty claims day to day? A
    dedicated admin or the service advisors?";
  - the bridge joins the question with a spaced hyphen: "Quick question -
    do you …";
  - keep full stops, question marks, apostrophes and the "!" after the
    name. A comma inside a proper name stays ("Trucks, Parts, Service");
  - the last sentence may end with no full stop;
  - never add a spelling or grammar mistake. Missing punctuation reads as
    human; typos read as careless.

  Apply this to the user's own topic sentence and question as well, and
  show them the stored text. It changes punctuation only, never a word.
- **Variants.** Give each row a Variant: A, B, C in rotation down the
  rows, and never the same one for two people at one company. The Variant
  changes the bridge and the sign-off only. Never vary the question's
  words or the fact in the personal line. When the user asks which
  wording works, report replies by Variant.
- Personal line: one sentence, at most 20 words, first in the message,
  built from one confirmed fact. "Saw …" for something they made or said.
  "Congrats on …" only for something that happened to the person or that
  they led: a promotion, an acquisition they ran. A company award sent to
  an employee gets "Saw that …". No flattery words ("impressive", "love",
  "amazing"), nothing the source does not say. A person with a connection
  and a work fact gets both, joined by "and" with no comma: "Fellow MIT
  alum here and saw the AutoPost launch."
- Email subject: the same fact as a noun phrase of 1–5 words, no verb: "your
  Service Improvement Team post", "the Chartway case study". It is the
  subject line of the email. Never "Re:", never a partner's or customer's voice, never
  a question the body does not ask.
- Question: at most 25 words. A fact they know from memory, nothing
  sensitive, true for everyone in the role group, either/or where
  possible. It never assumes a setup the prospect may not have. Store it
  starting in lower case, so it reads after the bridge.
- Topic sentence: at most 25 words, starts "I'm trying to understand how …"
  or "I am currently trying to learn more about …". It names the workflow
  under test, or the role for open discovery, and stays true for every
  prospect in the track.
- No link, no calendar, no tracking pixel in message 1 or the email. The
  calendar link appears only in the reply after they agree.
- No background sentence. The LinkedIn profile carries it.
