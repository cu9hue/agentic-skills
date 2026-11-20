The copy and the fields for all five are below. I have no Notion access in this session, so nothing is written to the tracker yet.

## Three things I need from you

1. **Sam's question.** You confirmed the question for founders. Sam is a CTO. I used the same question for him, because a CTO with agents in production can answer it from memory. Confirm, or give me a different one.
2. **Rowan's opener.** The question does not fit Gridmark. Gridmark sells a test harness and runs no agent at a customer, so "let the agent act" assumes a setup Rowan does not have. I gave him the `advice` opener. Confirm, or give me a question that is true for a testing company.
3. **Four LinkedIn URLs.** Your material has Sam's URL only. Paste the URLs for Dana, Priya, Lee and Rowan. I did not make any up.

## Stored text

I dropped the comma from each sentence and changed no word. Messages carry no comma, colon or semicolon.

- **Topic:** I'm trying to understand how credit unions decide to trust AI agents with money and where that decision gets stuck.
- **Question:** do your credit union customers let the agent act on its own today or does someone approve each action?

The question starts in lower case so it reads after the bridge ("Quick question - do your ...").

## Dedupe

The skip list is Northlight Payments, Ardent Ledger (your exclusion list) and Brightwater Ops (already in the tracker). None of the four companies is on it.

## People

| Name | Title | Company | Priority | First touch | Email check | Channel | Opener | Variant | Fact behind the line |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dana Ruiz | CEO | Ledgerline | 1 | linkedin | valid | linkedin, email | question | A | work, level 4 (company news) |
| Sam Okafor | CTO | Ledgerline | 1 | linkedin | not found | linkedin | question | B | connection + work, level 1 (his talk) |
| Priya Shah | CEO | Meridian Recon | 1 | linkedin | accept_all | linkedin | question | C | connection + work, level 4 (company news) |
| Lee Tran | Founder | Tallyhand | 2 | linkedin | invalid | linkedin | question | A | work, level 1 (his post) |
| Rowan Hale | CEO | Gridmark | 3 | linkedin | valid | linkedin, email | advice | B | connection + work, level 4 (company news) |

Only Dana and Rowan get an email. Sam has no address, and I did not build one from Dana's pattern. Priya's address is `accept_all` and Lee's is `invalid`, so neither goes on the email channel.

Dana and Sam have different facts, so Ledgerline gets two rows. They have different Variants, so the two messages do not read the same.

## Tracker rows

### Same value on all five rows

| Field | Value |
| --- | --- |
| Track | Founders and CTOs (one track; I will match the value on Kim Alvarez's row if it differs) |
| Their customers | credit unions |
| Sender | Polina |
| Calendar | https://calendly.com/polina/15min (for the reply after they agree; never in a draft) |
| Topic | I'm trying to understand how credit unions decide to trust AI agents with money and where that decision gets stuck. |
| Status | To send |
| Sent | empty |
| Follow-up due | formula; empty until Sent is set |
| Calls | empty |
| Nudge (formula output) | see "Shared drafts" below |

### Row 1: Dana Ruiz

| Field | Value |
| --- | --- |
| Name | Dana Ruiz |
| First name | Dana |
| Company | Ledgerline |
| Title | CEO |
| Priority | 1 |
| Segment | Disputes |
| Email | dana@ledgerline.ai |
| Email check | valid |
| LinkedIn | not in your material; paste it |
| First touch | linkedin |
| Channel | linkedin, email |
| Opener | question |
| Variant | A |
| Personal line | Saw the Chartway case study on disputes. |
| Email hook | the Chartway case study |
| Question | do your credit union customers let the agent act on its own today or does someone approve each action? |
| Personalization | work |
| Notes | Work fact: Chartway Federal Credit Union disputes case study, ledgerline.ai/customers/chartway, 2026-05-12 (level 4). Not used: $4M seed, TechCrunch, 2024-03-02 (older than 12 months). Not used: "used by 40+ credit unions", aitoolsdirectory.io (listicle, no source). No connection: Stanford 2012, ex-Square. Fit: agents in production at a named credit union. |

Message 1 (LinkedIn, after she accepts):

```
Hi Dana! Saw the Chartway case study on disputes. Quick question - do your credit union customers let the agent act on its own today or does someone approve each action?
```

Email (second touch):

```
Subject: Quick question about Ledgerline

Hi Dana! Saw the Chartway case study on disputes. Quick question - do your credit union customers let the agent act on its own today or does someone approve each action?

Thanks!
Polina
```

Boston is not in her line. A shared city is not on the list we agreed, and it does not count as a connection.

### Row 2: Sam Okafor

| Field | Value |
| --- | --- |
| Name | Sam Okafor |
| First name | Sam |
| Company | Ledgerline |
| Title | CTO |
| Priority | 1 |
| Segment | Disputes |
| Email | empty |
| Email check | not found |
| LinkedIn | linkedin.com/in/samokafor |
| First touch | linkedin |
| Channel | linkedin |
| Opener | question |
| Variant | B |
| Personal line | Fellow ex-Halcyon risk quant here and saw your Money20/20 talk on guardrails for agents that move money. |
| Email hook | your Money20/20 guardrails talk |
| Question | do your credit union customers let the agent act on its own today or does someone approve each action? |
| Personalization | both |
| Notes | Connection: risk quant at Halcyon Capital 2016–2020, linkedin.com/in/samokafor (sender 2017–2021; overlap 2017–2020). Work fact: talk "Guardrails for agents that move money", Money20/20 USA, money2020.com/sessions/guardrails-agents, 2025-10-27 (level 1; about 13 months old). Email find returned nothing; no address built from a pattern. Question confirmed for founders only; Sam is a CTO. |

Message 1 (LinkedIn, after he accepts):

```
Hi Sam! Fellow ex-Halcyon risk quant here and saw your Money20/20 talk on guardrails for agents that move money. Quick one for you - do your credit union customers let the agent act on its own today or does someone approve each action?
```

Email: none. No address was found.

### Row 3: Priya Shah

| Field | Value |
| --- | --- |
| Name | Priya Shah |
| First name | Priya |
| Company | Meridian Recon |
| Title | CEO |
| Priority | 1 |
| Segment | Reconciliation |
| Email | empty |
| Email check | accept_all |
| LinkedIn | not in your material; paste it |
| First touch | linkedin |
| Channel | linkedin |
| Opener | question |
| Variant | C |
| Personal line | Fellow MIT alum here and saw the AutoPost launch. |
| Email hook | the AutoPost launch |
| Question | do your credit union customers let the agent act on its own today or does someone approve each action? |
| Personalization | both |
| Notes | Connection: MIT 2014, meridianrecon.com/team (sender MIT 2016). Work fact: AutoPost launch, meridianrecon.com/blog/autopost, 2026-08-19 (level 4). Also available: Corelink partnership, corelink.com/news/meridian, 2026-06-03. Email find returned priya@meridianrecon.com; verify = accept_all; not usable for email. Do not re-run the find. |

Message 1 (LinkedIn, after she accepts):

```
Hi Priya! Fellow MIT alum here and saw the AutoPost launch. Curious - do your credit union customers let the agent act on its own today or does someone approve each action?
```

Email: none. The verifier could not confirm the mailbox.

### Row 4: Lee Tran

| Field | Value |
| --- | --- |
| Name | Lee Tran |
| First name | Lee |
| Company | Tallyhand |
| Title | Founder |
| Priority | 2 |
| Segment | not in your material; tell me the angle |
| Email | empty |
| Email check | invalid |
| LinkedIn | not in your material; paste it |
| First touch | linkedin |
| Channel | linkedin |
| Opener | question |
| Variant | A |
| Personal line | Saw your post on why examiners want to see the human in the loop. |
| Email hook | your examiners post |
| Question | do your credit union customers let the agent act on its own today or does someone approve each action? |
| Personalization | work |
| Notes | Work fact: Lee's post "Why examiners want to see the human in the loop", tallyhand.com/blog/examiners, 2026-07-14 (level 1). No profile data, so no connection checked. Email find returned lee@tallyhand.com; verify = invalid; do not use. Do not re-run the find. |

Message 1 (LinkedIn, after he accepts):

```
Hi Lee! Saw your post on why examiners want to see the human in the loop. Quick question - do your credit union customers let the agent act on its own today or does someone approve each action?
```

Email: none. The address is invalid.

### Row 5: Rowan Hale

| Field | Value |
| --- | --- |
| Name | Rowan Hale |
| First name | Rowan |
| Company | Gridmark |
| Title | CEO |
| Priority | 3 |
| Segment | Testing |
| Email | rowan@gridmark.io |
| Email check | valid |
| LinkedIn | not in your material; paste it |
| First touch | linkedin |
| Channel | linkedin, email |
| Opener | advice |
| Variant | B |
| Personal line | Fellow EF alum here and saw the model-risk report launch. |
| Email hook | the model-risk report launch |
| Question | empty (no question fits a testing company; the `advice` opener does not use one) |
| Personalization | both |
| Notes | Connection: EF alum per his profile (profile URL not in the material; add it). Work fact: Gridmark model-risk report launch, gridmark.io/blog/mrm, 2026-09-02 (level 4). Opener is advice: Gridmark sells a test harness and runs no agent at a customer. |

Message 1 (LinkedIn, after he accepts):

```
Hi Rowan! Fellow EF alum here and saw the model-risk report launch. I'm trying to understand how credit unions decide to trust AI agents with money and where that decision gets stuck. Would really appreciate 15 mins of your advice
```

Email (second touch):

```
Subject: Could I get your perspective?

Hi Rowan! Fellow EF alum here and saw the model-risk report launch. I'm trying to understand how credit unions decide to trust AI agents with money and where that decision gets stuck. Would really appreciate 15 mins of your advice

Thank you!
Polina
```

## Shared drafts

Nudge, after Dana, Sam, Priya or Lee answers the question:

```
Thanks that helps a lot. I'm trying to understand how credit unions decide to trust AI agents with money and where that decision gets stuck. Could I get 15 mins of your advice this week?
```

Rowan does not need the nudge. His message 1 already asks for the 15 minutes.

Reply when someone agrees, within the hour. This is the only message with the link:

```
Great thank you! I could do {time 1} or {time 2}. Or grab any slot here https://calendly.com/polina/15min
```

Follow-up, once, about 3 business days after message 1 with no answer, in the same thread:

```
Hi {first}! Bumping this in case it got buried. Still curious if you have a minute
```

You gave no finding for this track, so the follow-up is the plain bump. One sourced fact of your own would make it stronger.

## How to send

1. Send each LinkedIn request with no note. Set Status to `Request sent`.
2. Send message 1 within minutes of the acceptance.
3. Email Dana and Rowan about 5 business days after the request if they have not accepted. Sam, Priya and Lee have no second touch.
4. Send the nudge after they answer. Send the reply with the link once they agree.

No draft carries a background sentence. Your LinkedIn profile does that job, so keep it current. EF, Halcyon Capital and MIT must show on it, because three of the five lines lean on them.

## Left out and rejected

- **People left out:** none. All five have a fact.
- **Facts rejected for Dana:** the $4M seed (2024, too old) and the "40+ credit unions" claim (a listicle with no source).

## Spend

$0. I made no treg call. I could not read the balance in this session.

## Check before you send

- **Sources.** I had no web access in this session. The facts, dates and URLs come from your material, and I did not open the pages. Open each source before you send its line.
- **Dana, level 4 fact.** She is priority 1 and has only company news. I could not search for something she said or wrote. A post or talk of hers would make a stronger line.
- **Sam, talk date.** The talk is from 2025-10-27, about 13 months ago. That is at the edge of "recent". The Halcyon line stands without it: "Fellow ex-Halcyon risk quant here."
- **Sam, Halcyon.** I know only that your dates overlap from 2017 to 2020. If you knew him there, rewrite the line by hand.
- **Lee, question fit.** Two risks. Priority 2 covers companies with no named customer yet, and the question says "your credit union customers". Also, his post title suggests the answer is "someone approves each action". Read the post first. If Tallyhand has no credit union customers, I will switch him to the `advice` opener.
- **Lee, Segment.** Your material does not say what Tallyhand's product does.
- **Rowan, EF.** The material says "EF alum" with no URL. Add the page where it shows.
- **Priya, second fact.** The Corelink partnership (2026-06-03) is in Notes if you prefer it to the AutoPost launch.
- **First email.** Before the first email goes out, send the draft to your own Gmail and Outlook accounts and see where it lands.

Answer the three questions and paste the four URLs. Then I will write the rows to the tracker once Notion is connected.
