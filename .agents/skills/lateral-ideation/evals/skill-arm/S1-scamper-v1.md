**Seed:** Granola is a meeting notepad. It listens to your calls through the laptop's audio, with no bot in the room, and turns your rough notes into clean ones. *(assumed)*

**Moves** (SCAMPER, in order)

- **Substitute:** swapped the office call for other rooms and other talkers.
  - A kitchen fitter walks a homeowner through the job. The phone in his pocket listens. Before he leaves, the homeowner signs a scope of work built from what they both said, including "you said the old tiles stay." Notes become the contract for trades.
  - A procurement manager's buying agent negotiates overnight with a supplier's sales agent. At 8am she reads the minutes of a meeting between two bots and initials each concession. The notepad becomes the human sign-off for agent-to-agent deals.
- **Combine:** fused the notes with the invoice.
  - A family lawyer never fills in a timesheet. Each client call becomes its own bill: "14:02–14:09, custody schedule, £58." The client taps a line and hears the seven minutes they paid for.
- **Adapt:** borrowed the flight recorder.
  - A team's meetings go into a sealed box that nobody on the team can read. When a launch slips a quarter, an outside reviewer breaks the seal and writes the post-mortem from what people said, not what they remember. Recording stops feeling like surveillance, because the tape is opened only after a crash.
- **Maximize / Minimize:** stretched the memory to years for one person, then cut it to one day for a company.
  - An adult daughter's father has early dementia. Every call he takes is recorded: the GP, the bank, the man who says his account is compromised. She gets a text when a stranger asks for card details. She can check whether the doctor really changed the dose.
  - A general counsel bans recorders because transcripts are discoverable. This product keeps only the action items, shreds the audio and transcript at 24 hours, and issues a destruction certificate. It sells forgetting.
- **Put to another use:** same transcripts, new user.
  - A Brazilian engineer on a US team misses idioms in standup. Each Friday she gets a ten-minute drill built from phrases her colleagues used that week, with her own replies beside them.
  - A startup winds down. The administrator lists three years of board and product meeting audio as an asset and sells it to a model lab as training data on how companies make decisions.
- **Eliminate:** removed the meeting.
  - Five people each talk to the notepad for four minutes, alone, when it suits them. The app writes the minutes of the meeting that would have happened. It books a live call only for the two points where they disagree.
- **Reverse:** flipped who holds the notes, and when they are written.
  - The buyer, not the seller, runs the notepad on every sales call. Each vendor promise ("SSO by Q3", "no price rise for two years") lands in a ledger. Procurement pastes the ledger into the contract as clauses.
  - The notes come before the meeting. The app drafts what the meeting will decide from the thread so far. The meeting exists only for people to strike lines out.

**Picked:** the sealed flight recorder, because it removes the reason people refuse to be recorded instead of recording more; the dementia guardian, because it moves the product from work to family, where the stakes are money and consent; the corpus sale, because it is the future nobody wants and it is closer than it looks. Dropped: the trades contract, the invoice and the promise ledger are good businesses but stay inside "notes as a record"; the drill, the shredder, the async meeting and the pre-notes read more like modes of a notes app than new directions.

**Artifacts**

*1. Seal-break notice, sealed flight recorder*

```
From:    Blackbox <seal@blackbox.app>
To:      Priya Raman, VP Engineering
Date:    Mon 4 Aug 2028, 09:15
Subject: Seal broken: Project Kestrel (14 Jan – 30 Jun 2028)

The seal on Project Kestrel was broken at 09:14 today.

Trigger:        Launch date missed by more than 30 days
                (rule set by you on 12 Jan 2028)
Opened by:      Tomasz Wilk, external reviewer, Halden Review Ltd
Access window:  21 days. Ends Mon 25 Aug 2028.

What he can read
  212 meetings, 167 hours
  Transcripts and audio
  Who attended, who spoke, and for how long

What he cannot read
  6 meetings marked "personal" by an attendee (titles hidden)
  Anything recorded after 30 Jun 2028

Your team will not see the transcripts. They will see his report.
Every page he opens is logged. Each attendee gets the log on 26 Aug.

A broken seal cannot be resealed.
```

*2. Call log, dementia guardian (failure state)*

```
Lumen · Dad's calls · Thu 14 Nov 2027

10:02  Dr Okafor's surgery        4 min   Notes ready
       "Amlodipine stays at 5 mg. Bloods in two weeks."

10:41  Unknown number            17 min   NOT RECORDED
       Dad said "stop recording" at 10:41:07.
       Recording paused for this call, as his consent setting requires.

10:58  Unknown number            22 min   NOT RECORDED
       Pause still on. Dad has not said "start recording" again.

11:23  Barclays card services     3 min   Notes ready
       "Two payments today to HMRC SETTLEMENTS LTD, £1,900 each.
        Card ending 4471 frozen at customer's request."

⚠  Two calls from new numbers, 39 minutes in total, while recording was off.
   We can't tell you what was said.

   [ Call Dad ]     [ Review consent settings with Dad ]
```

*3. Administrator's asset schedule, corpus sale*

```
SCHEDULE 3: DIGITAL ASSETS
In the matter of Northlight Labs Ltd (in administration)
Sealed bids close 17 March 2029

Lot  Description                                           Reserve
11   Domain names (4), incl. northlight.ai                  £8,000
12   Source code and product repositories, 2022–2028       £40,000
13   Customer list (1,140 accounts), non-exclusive         £15,000
14   Internal meeting corpus, Jan 2023 – Dec 2028         £220,000
       6,812 recorded meetings, 9,400 hours, audio + transcript
       Includes board meetings (61), all-hands (140),
       hiring panels (388), 1:1s (2,950)
       Speaker labels intact. Employee names pseudonymised
       at the buyer's request.
       Licence: perpetual, includes model training.
       Note: employment contracts (cl. 14.2) assign recordings
       made on company devices to the Company.
15   Office furniture, Shoreditch                           £3,500
```

**Theories**

- I think a company's own meeting recordings will appear as a listed asset in an administration, bankruptcy or acquisition filing by end of 2028.
  - **Backs it:** an asset schedule or deal filing that names "recordings", "transcripts" or "meeting data"; a model lab saying publicly that it buys enterprise conversation data.
  - **Kills it:** a court or data-protection regulator rules that employees' recorded speech cannot be sold on without fresh consent.
- I think an enterprise notes product will ship sealed records, captured but unreadable by the team until a set trigger, by end of 2027.
  - **Backs it:** a pricing or security page that offers sealed or escrowed transcripts, or an RFP that asks for them.
  - **Kills it:** legal teams keep banning recorders outright. Watch whether "no AI notetaker" clauses keep spreading in vendor and employee policies.
- I think a meeting-notes or ambient-scribe company will sell a caregiver plan for an older parent's calls by end of 2027.
  - **Backs it:** a "family" or "caregiver" tier on a pricing page; a partnership with a bank's elder-fraud team. The FBI IC3 elder-fraud report gives the size of the pain *(needs source)*.
  - **Kills it:** a two-party-consent lawsuit or a regulator letter against an early entrant.

**Next:** hand the dementia guardian to `market-map` to find out who pays (the daughter, the bank or the insurer) and what consent law allows.

1. Are you building in this space, or looking for a wedge next to it? That decides whether the picks should stay near Granola's users or leave them.
2. Is consumer on the table, or only B2B?
