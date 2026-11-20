Five rows and their drafts are below. I have no Notion access in this session, so nothing is written to the tracker yet. I also opened no source page, so every fact comes from your material (see Check 1).

None of the four companies is on the skip list (Northlight Payments, Ardent Ledger, Brightwater Ops).

## Stored text

Messages carry no comma, so I dropped one comma from each. No word changed.

- **Topic:** I'm trying to understand how credit unions decide to trust AI agents with money and where that decision gets stuck.
- **Question (founders):** do your credit union customers let the agent act on its own today or does someone approve each action?

The question starts in lower case because it follows the bridge ("Quick question -").

## Fields that are the same on all five rows

| Field | Value |
| --- | --- |
| Track | Vendor (my name for the single track; tell me if the Brightwater Ops row uses another) |
| Their customers | credit unions |
| Topic | I'm trying to understand how credit unions decide to trust AI agents with money and where that decision gets stuck. |
| Sender | Polina |
| Calendar | https://calendly.com/polina/15min (on the row only, never in a first message) |
| First touch | linkedin |
| Status | To send |
| Sent | empty |
| Follow-up due | formula, empty until Sent is set |
| Calls | empty |

## Fields per person

| Name | First name | Company | Title | Priority | Segment | Variant | Opener | Personalization | Fact level | Channel | Email | Email check | LinkedIn |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Dana Ruiz | Dana | Ledgerline | CEO | 1 | Disputes | A | question | work | 4 (company news) | linkedin, email | dana@ledgerline.ai | valid | need the URL |
| Sam Okafor | Sam | Ledgerline | CTO | 1 | Disputes | B | question | both | 1 (his own talk) + connection | linkedin | empty | not found | linkedin.com/in/samokafor |
| Priya Shah | Priya | Meridian Recon | CEO | 1 | Reconciliation | C | question | both | 4 (company news) + connection | linkedin | empty | accept_all | need the URL |
| Lee Tran | Lee | Tallyhand | Founder | 2 | not set (see Check 4) | A | question | work | 1 (his own post) | linkedin | empty | invalid | need the URL |
| Rowan Hale | Rowan | Gridmark | CEO | 3 | FI AI tooling | B | advice | both | 4 (company news) + connection | linkedin, email | rowan@gridmark.io | valid | need the URL |

Dana and Sam are at one company, so they get different Variants (A and B) and different facts.

## Copy per person

### Dana Ruiz (Ledgerline)

- **Personal line:** Saw the Chartway Federal Credit Union case study on disputes. (10 words)
- **Email hook:** the Chartway case study (4 words)
- **Question:** do your credit union customers let the agent act on its own today or does someone approve each action?
- **Notes:** Fact: Chartway Federal Credit Union case study on disputes, 2026-05-12, ledgerline.ai/customers/chartway. Not used: $4M seed (TechCrunch, 2024-03-02, older than 12 months); "used by 40+ credit unions" (aitoolsdirectory.io, a listicle with no source). Profile: Stanford 2012, ex-Square. No match with the sender background.

Message 1 (LinkedIn, right after she accepts):

```
Hi Dana! Saw the Chartway Federal Credit Union case study on disputes. Quick question - do your credit union customers let the agent act on its own today or does someone approve each action?
```

Email (second touch, about 5 business days after the request if she has not accepted):

```
Subject: the Chartway case study

Hi Dana! Saw the Chartway Federal Credit Union case study on disputes. Quick question - do your credit union customers let the agent act on its own today or does someone approve each action?

Thanks!
Polina
```

I did not use Boston. It is not on the list we agreed, and a shared city is not a connection.

### Sam Okafor (Ledgerline)

- **Personal line:** Fellow ex-Halcyon risk quant here and saw your Money20/20 talk on guardrails for agents that move money. (17 words)
- **Email hook:** your Money20/20 guardrails talk (4 words)
- **Question:** do your credit union customers let the agent act on its own today or does someone approve each action?
- **Notes:** Fact: talk "Guardrails for agents that move money", Money20/20 USA, 2025-10-27, money2020.com/sessions/guardrails-agents. Connection: risk quant at Halcyon Capital 2016–2020, linkedin.com/in/samokafor; sender was there 2017–2021. Email find: not found.

Message 1 (LinkedIn, right after he accepts):

```
Hi Sam! Fellow ex-Halcyon risk quant here and saw your Money20/20 talk on guardrails for agents that move money. Quick one for you - do your credit union customers let the agent act on its own today or does someone approve each action?
```

No email. The find returned no address and I will not build one from Dana's pattern.

### Priya Shah (Meridian Recon)

- **Personal line:** Fellow MIT alum here and saw the AutoPost launch. (9 words)
- **Email hook:** the AutoPost launch (3 words)
- **Question:** do your credit union customers let the agent act on its own today or does someone approve each action?
- **Notes:** Fact: AutoPost launch, 2026-08-19, meridianrecon.com/blog/autopost. Connection: MIT 2014, meridianrecon.com/team; sender MIT 2016. Spare fact: Corelink partnership, Corelink press release, 2026-06-03, corelink.com/news/meridian. Email find returned priya@meridianrecon.com, verify = accept_all, not usable. Do not re-run the find.

Message 1 (LinkedIn, right after she accepts):

```
Hi Priya! Fellow MIT alum here and saw the AutoPost launch. Curious - do your credit union customers let the agent act on its own today or does someone approve each action?
```

No email. An `accept_all` address is unconfirmed, so it stays off the email channel and out of the Email field.

### Lee Tran (Tallyhand)

- **Personal line:** Saw your post on why examiners want to see the human in the loop. (14 words)
- **Email hook:** your examiners post (3 words)
- **Question:** do your credit union customers let the agent act on its own today or does someone approve each action?
- **Notes:** Fact: Lee's post "Why examiners want to see the human in the loop", 2026-07-14, tallyhand.com/blog/examiners. Email find returned lee@tallyhand.com, verify = invalid, not usable. Do not re-run the find.

Message 1 (LinkedIn, right after he accepts):

```
Hi Lee! Saw your post on why examiners want to see the human in the loop. Quick question - do your credit union customers let the agent act on its own today or does someone approve each action?
```

No email. The address is invalid.

### Rowan Hale (Gridmark)

- **Personal line:** Fellow EF alum here and saw the Gridmark model-risk report. (10 words)
- **Email hook:** the model-risk report (3 words)
- **Question:** empty
- **Notes:** Fact: Gridmark model-risk report, 2026-09-02, gridmark.io/blog/mrm. Connection: EF alum, per profile. Opener is advice: the founders' question assumes an agent, and Gridmark sells a test harness.

The founders' question does not fit Rowan. It asks about "the agent", and Gridmark has none. So Rowan gets the `advice` opener: the personal line, the topic, then the ask.

Message 1 (LinkedIn, right after acceptance):

```
Hi Rowan! Fellow EF alum here and saw the Gridmark model-risk report. I'm trying to understand how credit unions decide to trust AI agents with money and where that decision gets stuck. Would really appreciate 15 mins of your advice
```

Email (second touch, about 5 business days after the request if there is no acceptance):

```
Subject: the model-risk report

Hi Rowan! Fellow EF alum here and saw the Gridmark model-risk report. I'm trying to understand how credit unions decide to trust AI agents with money and where that decision gets stuck. Would really appreciate 15 mins of your advice

Thank you!
Polina
```

## Drafts shared by all rows

Nudge, after Dana, Sam, Priya or Lee answers the question (the Nudge formula gives the same text on every row):

```
Thanks that helps a lot. I'm trying to understand how credit unions decide to trust AI agents with money and where that decision gets stuck. Could I get 15 mins of your advice this week?
```

Rowan's message 1 already asks for the call, so skip the nudge there.

Reply when someone agrees, within the hour. This is the only place the calendar link goes. You fill in the two times.

```
Great thank you! I could do {time 1} or {time 2}. Or grab any slot here https://calendly.com/polina/15min
```

Follow-up, once, about 3 business days after message 1 with no answer, in the same thread. You gave no finding, so it is the plain bump.

```
Hi {first}! Bumping this in case it got buried. Still curious if you have a minute
```

## Report

- **Left out:** nobody. No reserves.
- **Rejected:** no company.
- **Spend:** $0. I ran no treg calls.

## Check before you send

1. **Sources.** I opened no page in this session. Open each URL in Notes and confirm the fact is on it. If a page does not open or does not say it, tell me and I will drop that row.
2. **Sam, the connection.** You and Sam were both risk quants at Halcyon from 2017 to 2020. If you know him, write the line by hand. "Fellow" reads oddly to a former colleague.
3. **Sam, the talk.** It is dated 2025-10-27, almost 13 months ago, at the edge of the 12-month window. I kept it because it is his own talk on your topic. If you want to drop it, the line becomes "Fellow ex-Halcyon risk quant here." and Personalization becomes `connection`.
4. **Sam, the question.** You confirmed it for founders. I used it for Sam, a CTO, because it holds for Ledgerline. Say so if you want a separate CTO question.
5. **Lee.** The question assumes Tallyhand has credit union customers. Priority 2 also covers agents with no named customer yet. If that is Tallyhand, the question fails and Lee should move to the `advice` opener. Your material also does not say what Tallyhand sells, so I left Segment unset.
6. **Rowan.** If you would rather open with a question, here is a draft for tooling founders to confirm: "who buys from you today? The credit unions themselves or the vendors that sell AI to them?"
7. **Dana and Priya.** Both are priority 1 on a level-4 fact (company news). The search for something they said or wrote did not run here. One search each is worth it before you send.
8. **LinkedIn URLs.** Your material holds only Sam's. I need the other four to fill the field.
9. **Segment for Meridian Recon.** I inferred "Reconciliation" from the company name. Correct it if it is wrong.
10. **Your profile.** Three lines lean on it showing Halcyon, MIT and EF. Check that it does.
11. **Formulas.** Once the rows are in Notion, open Dana's row and check Message, Email draft and Nudge against the text above. If `\n` shows as literal text in Email draft, tell me.
