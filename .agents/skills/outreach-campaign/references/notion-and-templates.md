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
| Company | text | the everyday name, no legal suffix; used for dedupe and in the email subject |
| Title | text | job title |
| Track | select | the campaign's tracks, e.g. Operator, Underwriter |
| Priority | select | 1, 2, 3 |
| Segment | select | the ICP angle the company came from |
| Their customers | text | plural noun that reads in a sentence: "credit unions" |
| Email | email | empty when not found or not usable |
| Email check | select | valid, valid-risky, accept_all, invalid, not found |
| LinkedIn | url | |
| First touch | select | linkedin, email: where this person starts (the mix rule in SKILL.md) |
| Channel | multi-select | email, linkedin, intro |
| Sender | select | the sender's first name |
| Calendar | url | the sender's booking link; used in the reply, never in a draft |
| Topic | text | the track's confirmed topic sentence |
| Opener | select | question, advice |
| Variant | select | A, B, C: picks the wording of the bridge, the email lead, the hook sentence and the sign-off |
| Personal line | text | one sentence from a confirmed fact |
| Email lead | text | the email's first two lines: the segment's lead in the row's Variant wording |
| Email hook | text | the same fact as a 1–5 word noun phrase that completes "Saw …"; closes the email, never the subject |
| Question | text | the confirmed question for the person's role group |
| Personalization | select | both, connection, work |
| Status | select | To send, Request sent, Accepted, Sent, Replied, Followed up, Call booked, No reply, Not a fit |
| Sent | date | the day message 1 or the email went out |
| Follow-up due | formula | `dateAdd(prop("Sent"), 4, "days")` |
| Message | formula | below |
| Email subject | formula | below |
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
  It shows Email subject next to Email draft.
- **Message now**: table, filter Status = Accepted.
- **Follow up**: table, filter Status = Sent, sort Sent ascending.
- **Pipeline**: board grouped by Status.

If the Notion tool cannot create views, give the user these four lines to
add by hand.

### Formulas

Everything campaign-specific lives in row properties, so the formulas are
the same for every campaign, track and sender.

Message (LinkedIn message 1):

```
"Hi " + prop("First name") + "! " + prop("Personal line") + " " + if(prop("Opener") == "advice", prop("Topic") + " " + if(prop("Variant") == "B", "Would really appreciate 15 mins of your advice", if(prop("Variant") == "C", "Could I get 15 mins of your advice?", "Would love 15 mins of your advice")), if(prop("Variant") == "B", "Quick one for you", if(prop("Variant") == "C", "Curious", "Quick question")) + " - " + prop("Question"))
```

Email subject:

```
if(prop("Opener") == "advice", "Could I get your perspective?", "Quick question about " + prop("Company"))
```

Email draft (the body of the email; its own order, never the Message
again):

```
"Hi " + prop("First name") + "! " + if(empty(prop("Email lead")), if(prop("Opener") == "advice", "", if(prop("Variant") == "B", "Quick one for you", if(prop("Variant") == "C", "Curious", "Quick question")) + " - " + prop("Question") + "\n\n"), prop("Email lead") + "\n\n") + prop("Topic") + if(empty(prop("Email hook")), "", " Saw " + prop("Email hook") + if(prop("Variant") == "B", " so I thought you would know.", if(prop("Variant") == "C", " and figured you would be a good person to ask.", " which is why I thought of you."))) + if(prop("Opener") == "advice", " " + if(prop("Variant") == "B", "Would really appreciate 15 mins of your advice", if(prop("Variant") == "C", "Could I get 15 mins of your advice?", "Would love 15 mins of your advice")), "") + "\n\n" + if(prop("Variant") == "B", "Thank you!", if(prop("Variant") == "C", "Thanks so much!", "Thanks!")) + "\n" + prop("Sender")
```

A row with no Email lead opens with the bridge and the question (an
`advice` row opens with the topic). A row with no Email hook gets no hook
sentence.

Nudge (after they answer the question):

```
"Thanks that helps a lot. " + prop("Topic") + " Could I get 15 mins of your advice this week?"
```

A row with no Variant reads as A.

When a formula goes through SQL DDL, write each apostrophe in its text as
`''`.

The Notion API does not return formula output. After the first row is
written, ask the user to open it and check the subject and the three
drafts. If `\n` shows as literal text in Email draft, tell the user and
fall back to writing the drafts as plain text into text properties of the
same names.

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

**Message 1, `question` opener** (LinkedIn, after they accept)

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

**Email** (the first touch for the email-first people in the mix and for
anyone with no LinkedIn URL; the second touch for the rest)

```
Subject: Quick question about {company}

Hi {first}! {email lead}

{topic} Saw {email hook} {which is why I thought of you|so I thought you would know|and figured you would be a good person to ask}.

{Thanks!|Thank you!|Thanks so much!}
{sender}
```

The email lead, written per row in the Variant's wording:

```
{One {kind of source} says|A {kind of source} claims|One {firm or vendor} in this space claims} {claim}. {Does that match what you see or is it a sales pitch?|Is that real or just a sales pitch?|Does that sound right to you or is it marketing?}
```

Example (Variant B):

```
Subject: Quick question about Allegiance Truck Centers

Hi Tonya! A warranty vendor claims dealers recover 15 to 30% more warranty money once it handles their claims. Is that real or just a sales pitch?

I'm trying to understand how warranty claims get filed and chased at a dealer group and where they get stuck. Saw your Service Improvement Team post so I thought you would know.

Thank you!
Polina
```

An `advice` email adds the advice ask after the hook sentence.

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
  changes the bridge, the wording around the email lead's claim, the hook
  sentence and the sign-off. Never vary the question's words, the claim's
  numbers or the fact in the personal line. When the user asks which
  wording works, report replies by Variant.
- **LinkedIn and email are different.** LinkedIn message 1 opens with the
  personal line: they have accepted the request and can see the profile.
  The email goes to a cold inbox, where the subject and the first two
  lines decide whether it is read. Its order is the lead, then the topic,
  then the hook. Never reuse message 1 as the email body.
- Email lead: at most two sentences and 40 words. A claim from a page you
  opened, attributed to a kind of source ("one warranty vendor"), with its
  numbers exact, then a doubt they can settle in one line. Or a finding
  the user owns, then "Does that match what you see?". Never the sender's
  own belief, never a pitch, never a fact about the reader.
- Personal line: one sentence, at most 20 words, first in message 1,
  built from one confirmed fact. "Saw …" for something they made or said.
  "Congrats on …" only for something that happened to the person or that
  they led: a promotion, an acquisition they ran. A company award sent to
  an employee gets "Saw that …". No flattery words ("impressive", "love",
  "amazing"), nothing the source does not say. A person with a connection
  and a work fact gets both, joined by "and" with no comma: "Fellow MIT
  alum here and saw the AutoPost launch."
- Email hook: the same fact as a noun phrase of 1–5 words, no verb: "your
  Service Improvement Team post", "the Chartway case study". It completes
  "Saw …" and closes the email. A hook is not a subject: it never goes
  in the subject line.
- Email subject: plain, and true to the body. "Quick question about
  {Company}" for the `question` opener and "Could I get your perspective?"
  for the `advice` opener. Never "Re:", never urgency or clickbait, never
  a partner's or customer's voice, never a claim the body does not make.
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
