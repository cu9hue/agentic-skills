**Seed:** A capable model now runs on a phone or laptop, offline, fast, at close to zero cost per call. That is more true this year than last. *(assumed)*

**And then**
1. Inference costs nothing per call → apps run a model all the time, on every message, call and photo, not only when asked → each device keeps a private log of what its model inferred about you, and nobody ever reads it → that log becomes evidence when a family court asks what kind of parent you are.
2. Models run with no network → they ship inside toys, cars and laptops that never phone home → each device's model is frozen at the factory, so it knows the world only up to the day it was made → used devices get priced by what their model knows and who trained it, like a wine vintage.

**Moves** (drawn: Put to another use, Card: "Treat the error message as the main feature", Substitute, Combine)

- **Put to another use:** I kept the on-device model as it is and gave its output to a different user. A landlord and a tenant walk the flat at move-out. A phone with no network writes the condition report as they talk, both sign on the screen, and the report prints the hash of the model weights so either side can rerun it later. Separately, a parent's phone keeps a log of inferred moods for its owner's own recall, and in a custody hearing the other side's lawyer gets that log as an exhibit.
- **Card, "Treat the error message as the main feature":** I made the frozen model's "I don't know" the product. A child's talking toy prints its knowledge date on the box. When the child asks about anything after that date, the toy says so and sends the child to ask a person, so every error teaches where knowledge comes from. Separately, an offline car model logs only the moments it is unsure. The insurer buys that log and rates drivers by how often their usual routes confuse the car.
- **Substitute:** I replaced one component with something from another category. Replace *you*, in a data broker's eyes, with a decoy: your phone's idle cycles generate a coherent fake life (searches, map trails, browsed purchases), and the broker's profile of a 34-year-old nurse says she is a retired angler in Ohio. Replace a game's save file with a small fine-tune of the characters on your playthrough. A player sells a companion who remembers 200 hours of shared quests, and the buyer meets a stranger who knows them.
- **Combine:** I fused the frozen-vintage world with an estate sale. A retiring electrician sells his laptop with "his" model inside, tuned on 31 years of job notes. Buyers pay for the provenance, not the hardware.

**Cone**

| Idea | Cone | Preferable? |
|---|---|---|
| Move-out witness | Plausible | Yes |
| Inference log as custody evidence | Probable | No |
| Toy with a printed knowledge date | Plausible | Yes |
| Insurer buys the car's "unsure" log | Plausible | No |
| Decoy twin for data brokers | Plausible | Mixed: privacy for you, cover for fraud |
| Save file as a model | Plausible | Yes |
| Estate sale of a tradesperson's model | Possible | Yes, mostly |

**Picked:** the custody log, because it makes the unwanted future concrete and it is the most likely idea here; the estate sale, because it fell out of the vintage chain and nobody is pricing expertise that way yet; the toy, because it surprised me, since the model's limit becomes the lesson. Dropped: the move-out witness (useful but obvious), the car log (same shape as the custody log), the decoy twin (ad-noise tools already gesture at it), the save file (fun, but smaller).

**Artifacts**

*1. A court exhibit, with the failure in the footnote*

```
IN THE FAMILY COURT AT LEEDS                     Case No. LS27F00412
EXHIBIT R-14
On-device inference log, extracted from Respondent's phone
Period: 01 Feb 2027 – 28 Feb 2027 (excerpt, 6 of 2,914 entries)

TIMESTAMP          SOURCE          INFERENCE                         CONF
2027-02-03 07:52   voice call      user tone: rushed                 0.66
2027-02-03 07:53   messages        user tone: irritated, re "school" 0.71
2027-02-11 22:40   photos          user at bar-like venue            0.58
2027-02-11 23:58   typing cadence  user possibly intoxicated         0.62
2027-02-14 16:05   voice call      user tone: affectionate, re "Ava" 0.88
2027-02-19 21:17   messages        user expressed wish to "disappear" 0.74

Extracted by: Halden Forensics Ltd. Model: on-device memory v3.2,
weights hash 9f3a…c21e. Re-run on same inputs reproduces 5 of 6 entries.

¹ Respondent's note on 2027-02-19: the message read "I want to disappear
into this book for a week." The model dropped the second half of the
sentence. Entry 2027-02-11 23:58: Respondent was typing with one hand
while holding a sleeping child.
```

*2. A classified ad*

```
FOR SALE: Retired master electrician's laptop + model
ThinkPad, 2026. Battery fair. Keyboard worn on F and R.

Includes "GERRY-7B", tuned by Gerald Okafor (47 yrs in the trade)
on 31 years of his own job notes, fault photos and quotes.
- Diagnoses old fuse boards from a photo. Very strong on 1960s–80s housing stock.
- Knows nothing after June 2026. Gerry says that's a plus.
- Never been online. Weights hash on the receipt; Gerry will sign it.
- Not a substitute for a qualified electrician. Gerry insists on this line.

£1,400 o.n.o. Laptop alone worth £300. You're paying for Gerry.
Collection only, Huddersfield. No time-wasters, no "AI startups".
```

*3. A toy box panel, then the support ticket*

```
PIP knows everything up to 30 June 2026.
After that, Pip will say:
"That happened after I was made. Who could you ask?"
Pip never connects to the internet. Pip will never learn anything new.
That's the point.
```

```
Ticket #48812 · Opened 22 Dec 2027 · Priority: normal
Subject: Pip told my son a man who died is still alive

Hi. My son (7) asked Pip about his grandad's favourite footballer,
who died in March. Pip said he "plays for City and is doing great."
It didn't say "that happened after I was made" because it doesn't know
anything happened. He cried. Can Pip at least say "I might be out of
date" when it talks about people?

— Reply (Kestrel Toys): Thank you. Pip cannot detect what it does not
know. A firmware update adding the phrase "as of when I was made" to
answers about living people is planned, but Pip has no network, so the
update must be installed by USB. Instructions attached.
```

**Theories**

- I think a family court in the UK or US will admit an on-device model's inference log or memory as evidence by the end of 2027.
  - **Backs it:** a published ruling or news report that names on-device AI memory in discovery, or phone vendors adding legal-hold or memory-export language to their help pages.
  - **Kills it:** OS vendors make on-device memory encrypted and non-exportable by design, and courts accept that it cannot be extracted.
- I think a used-goods marketplace will list a named practitioner's tuned local model as the main item, priced above its hardware, by the end of 2028.
  - **Backs it:** listings on eBay or a dedicated site that quote a weights hash or the tuner's name as provenance.
  - **Kills it:** professional bodies treat a transferred model as unlicensed practice and ban the sale, or no such listings exist by then.
- I think a mainstream children's toy will print a model knowledge date on its packaging by Christmas 2027.
  - **Backs it:** a knowledge date on a toy box at a major retailer.
  - **Kills it:** every major AI toy that season ships cloud-connected.

**Next:** I can turn Gerry's ad into a real listing page, so you can see whether anyone writes to ask about a "model with provenance".

Two questions would change this most:
1. Are you after something to build, or material for a talk or essay?
2. Do you mean phones and laptops, or cheap embedded chips in appliances?
