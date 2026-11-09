**Seed:** Granola-style notepads, which transcribe meetings from your own laptop with no bot in the call, are becoming the default way knowledge workers keep meeting notes. *(assumed)*

**And then**
1. Every call is transcribed by someone, and no bot announces it → people assume every meeting is on the record → the candid conversation moves to the five minutes after the call, in DMs and hallway walks → "unrecorded" becomes a feature people pay for.
2. Transcripts become the company's largest written record of who promised what → managers and lawyers search them in reviews and disputes → people learn to speak in transcript-safe language → the notes record caution instead of decisions, and the product loses the signal it exists to capture.

**Moves** (named: SCAMPER, all seven letters, run on the seed and the two third links)
- **Substitute:** swapped the office meeting for a different kind of conversation where one side has all the expertise. An adult daughter manages her father's cancer care. Before each consult she types three questions. The notepad listens to the oncologist, marks which questions got an answer, and drafts the follow-up message to the clinic for the one that did not.
- **Combine:** fused the notes with two unrelated jobs, a contract and a credit bureau. (1) A freelance architect ends every client call with a one-page "what we agreed". The client countersigns it on their phone, and anything outside it becomes a billable change order. (2) Every "I'll send it Friday" said in a recorded meeting is logged as a commitment. A follow-through rate appears next to your name on every calendar invite.
- **Adapt from elsewhere:** borrowed the cockpit voice recorder: sealed, opened only after an incident. Two cofounders record their weekly sync. Neither can read the audio. When they fight about an equity promise, both must turn a key to open the March call.
- **Maximize / Minimize:** (1) Audience ×1,000. A renter on Elm Street gets a text from her town's planning meeting: "6-storey build at 14 Elm approved, 4–3. Objections close Friday." Each resident gets the notes filtered to their street. (2) Retention ÷1,000. A team lead at a company whose lawyers forbid stored transcripts keeps one sentence per meeting, the decision. The audio and transcript are wiped after 24 hours.
- **Put to another use:** gave the notepad to the person being evaluated. A job candidate runs it across a six-interview loop. It spots that three interviewers described the role three different ways and writes the questions she should ask in the final round.
- **Eliminate:** removed the meeting. A PM's 8-person weekly status meeting is replaced by a 3-minute voice check-in per person on Monday. By 11am the note the meeting would have produced exists, and the meeting is cancelled. Only unresolved disagreements get a call, and only the people who disagree attend.
- **Invert (R):** (1) Flipped who owns the notes. A founder records a customer call. The customer gets the notes first and can strike their own lines within an hour, before the founder sees anything. (2) Flipped first and last. The board gets the minutes on Friday. Monday's meeting exists only to amend and strike lines.

**Cone**
| Idea | Cone | Preferable? |
|---|---|---|
| Patient's consult notepad | Probable | Yes |
| Countersigned "what we agreed" | Plausible | Yes for freelancers; clients may resent it |
| Follow-through score on invites | Plausible | No |
| Sealed two-key recorder | Plausible | Yes |
| Street-level council notes | Plausible | Yes |
| One-sentence decision ledger | Plausible | Yes |
| Candidate's interview-loop notepad | Probable | Yes for candidates; employers will ban it |
| The meeting that never happens | Plausible | Yes |
| Subject redacts first | Possible | Yes |
| Minutes-first board meetings | Plausible | Yes |

**Picked:** the sealed recorder, because it falls out of chain 2 and turns the evidence problem into the product; the follow-through score, because it makes the unwanted future concrete and someone will build it; the meeting that never happens, because it surprised me: the notes app's best product may be fewer meetings, which means it competes with its own input. Dropped: the patient, council and candidate notepads are strong but are the same product in a new room; the rest are features of the three picked.

**Artifacts**

*1. Sealed recorder, unseal screen (failure state)*

```
BLACKBOX  Unseal request #0412

Recording:     "Cofounder sync: equity & vesting"
Recorded:      Sat 14 Mar 2026, 09:02-09:51 (49 min)
Sealed by:     Tom Okafor, Priya Nair
Requested by:  Tom Okafor, 3 Nov 2026
Reason given:  "Disagreement over what we agreed on the 4-year cliff."

Keys required: 2 of 2
  [turned]   Tom Okafor   3 Nov 2026, 22:14
  [missing]  Priya Nair   key unavailable

CANNOT UNSEAL.
Priya Nair's key was destroyed when her workspace account was deleted
on 2 Oct 2026. No arbitrator key was set when this recording was sealed.

What happens next:
  - The recording stays sealed. Nobody, including Blackbox, can open it.
  - It self-destructs on 14 Mar 2027 (12-month retention, set at sealing).
  - Your typed notes from this meeting are still yours. They are not
    evidence of what Priya said.

[ Ask Priya to re-key from a personal account ]   [ Close ]

Tip: set an arbitrator (a lawyer or board member) on recordings about money.
```

*2. Follow-through score, calendar invite*

```
Pricing review
Thu 12 Nov 2026 · 15:00-15:30 · Room 4B / video link

Guests (4)
  Dana Whitfield (organizer)   Follow-through 94% · 112 commitments
  Marcus Lee                   Follow-through 88% · 41 commitments
  Ines Duarte                  Follow-through 71% · 58 commitments · 2 disputed
  Raj Patel                    New · no score yet

Ines Duarte's open items from earlier meetings with these guests:
  - "I'll send the churn cut by Friday"   23 Oct, Weekly growth   Overdue 17 days
  - "Let me check with legal"             29 Oct, Pricing v2      No follow-up detected

Scores use meetings recorded by any guest. Commitments are detected from
speech. To dispute one, open the transcript line and tap "I didn't promise
that." A disputed item counts as half a miss until the other speaker confirms.
```

*3. The meeting that never happens, channel message*

```
Quorum · #growth · Mon 9 Nov 2026, 11:40

Weekly Growth Sync (Tue 10 Nov, 10:00-10:30, 8 people) is CANCELLED.
7 of 8 people answered their 3-minute check-in. Here is the note the
meeting would have produced.

Decided
  - Onboarding email test ships Wednesday. (Sam and Lea agree. No objections.)
  - Paid social budget stays flat for November. (Dev proposed. 6 agree, 1 no view.)

Done since last week
  - Referral page is live. (Lea)
  - Churn interviews: 5 of 8 booked. (Ines)

Not resolved
  - Dev and Sam disagree on when the pricing test starts.
    Dev: 16 Nov. Sam: after Black Friday.
    Quorum booked a 15-minute call for the two of them, Tue 10:00.
    Everyone else gets the slot back.

Did not answer: Marcus (last check-in 19 Oct).
Next week's meeting will not be cancelled unless he answers.

Time returned this week: 3 h 9 min.
```

**Theories**
- I think at least one meeting-notes product ships a sealed-by-default mode, where the recorder cannot read the audio without the other party's consent, by the end of 2027. Backs it: a changelog or pricing page from Granola, Otter, Fireflies or a new entrant listing two-party unseal; employment lawyers writing about meeting transcripts in disputes. Kills it: at the end of 2027 the leading apps still give the recorder sole access to full transcripts, and no enterprise security questionnaire asks about sealing.
- I think a notes app will lead its landing page with "meetings cancelled" instead of "notes taken" by mid-2027. Backs it: a landing page or launch post that quotes meeting hours removed *(needs source)*; job ads at notes companies for async-workflow PMs. Kills it: pricing in the category stays tied to recorded meetings, and no major app ships auto-cancel.
- I think commitment scoring from transcripts arrives first inside performance-management tools, not notes apps, by the end of 2028. Backs it: a performance-tool changelog that cites meeting-commitment data. Kills it: a works council or EU regulator blocks such a feature (the EU AI Act treats AI used to evaluate workers as high-risk), or the vendor withdraws it after launch.

**Next:** I can run `market-map` on the meeting that never happens, to find out who pays for fewer meetings: the team, the manager, or finance.

1. Are you building in this space, or looking for a wedge next to Granola? The answer changes whether I push toward directions Granola cannot follow or ones it would buy.
2. Can the directions leave work meetings (clinics, councils, hiring), or must the buyer stay a company?
