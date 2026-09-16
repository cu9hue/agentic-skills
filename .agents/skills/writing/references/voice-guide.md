# Voice Guide

The fixed personal voice for opinion and personal pieces. Load this only when
writing posts, essays, launch notes, or newsletters. Skip it for neutral
reference material, where the anti-slop rules alone apply.

Derived from the author's own notes: 116 English files, about 29,000 words,
read in full on 2026-09-16. An earlier version of this guide was built from
two or three notes and got the voice wrong (see "The cadence to avoid").
The quoted lines are real lines from the notes. The rates are measured.

## What the voice is

The author explains things in order, in ordinary sentences, and says what
she thinks of them in ordinary words. A note reads like a smart colleague
walking you through a mechanism: this happens, then this, which causes
that. An opinion arrives as a plain adjective, a short aside, or an
exclamation mark, and then the explanation carries on. Casual and technical
share a sentence. This guide is about how she explains, more than how she
concludes; the conclusions take care of themselves once the explanation is
in her mode.

## How the author explains

**1. Sentences connect with ordinary glue.** Causal links are stated, not
left for the reader to infer from two sentences placed side by side.
Openers on nearly every page: Then, However, Hence, Additionally, Note
that, Meaning, For example, Simply put, In a nutshell, That's where X
comes in, Enter X.

- "There was also a mild recession in 1927 which led to more unemployment
  and a drop in production. In response, the government raised interest
  rates and further dampened economic activity."
- "Okay, so hardware models are hard and there is a lot of them. We need
  some kind of contract, so that reasoning about correctness on weak
  models like ARM would be possible. That's where DRF-SC comes in."

Measured rate: about twenty connectives per thousand words. Drafts at ten
read as machine-written; drafts at fifty read as a parody, with "however"
and "hence" bolted onto every sentence. Fifteen is the floor, thirty the
ceiling. Most sentences still start with their subject.

**2. Paragraphs are two to four medium sentences and end on the
consequence**, the next step in the chain or the effect of the mechanism,
never a verdict. "...This causes the loaner to do a 'fire sale' at a loss
and drives the further price fall." "...Even if newer kernels have NUMA
balancing and try to migrate pages to follow the compute, it's reactive
and has overhead."

**3. Parentheses carry the clarification.** "(read: largest alignment)",
"(intentional redundancy)", "(not just a C++ self-inflicted wound)", "this
(wrong) belief". About five per thousand words; zero is a missing habit.

**4. Questions do work**, opening a section or paragraph with the answer
right after. "Can the program print 0? Depends on the hardware, and depends
on the compiler." "Is software engineering dead? No way, but we have new
tools now."

**5. "We" and "you" are the working subjects.** "We track running max and
running denominator per row." "You can only add so much CPU to a server."
Definitions use "is": "A cache is a temporary storage area."

**6. Exclamation marks mark genuine emphasis or surprise**, about one every
three to five hundred words. "Each thread has its own stack!" "This is a
design flaw!" Never for hype.

**7. Register is mixed and stays mixed.** "people feel less wealthy and
don't wanna invest" sits next to "deleveraging". The discourse markers are
voice, not tells: basically, actually, super, pretty, kinda, e.g., btw.
About twice per thousand words. Zero is wrong, ten is a caricature.

## How the author judges

**Verdicts use plain intensifiers**: amazing, horrible, really, super,
pretty, crazy, insane, annoying, weak.

- "0-1 was an amazing book, i'll give Paul that."
- "Also, the speaker is exceptionally annoying. I stopped watching once I
  got the general idea."
- "Figma Make seems to be providing weak ass prototypes."
- "Super clear and compact. However, informal in places."

Layer 1's hype ban stands (revolutionary, game-changer, cutting-edge sell
the thing). These words rate the thing, and in personal pieces they stay.
Strip them and the model has no way left to signal a verdict except the
epigram, which is the failure this guide exists to prevent.

**The verdict sits with the evidence**: an adjective inside the explaining
sentence, or a short casual aside right after it. Not a standalone
paragraph, not a closing line. "Copy-paste: bloated and smells."
"Placement-new can be a bit inefficient (does a null ptr check)." "It was
BAD. Crashes always lead to low economic activity as people feel less
wealthy..." (verdict first, mechanism at once after, same paragraph).

**Hedges are short, casual, and about the evidence.** "Obviously, Garry is
a bit biased towards AI as a VC investor. Take this with a grain of salt!"
"Didn't really explain in detail, but seems reasonable." The diagnostic
test still applies to every qualifier: keep it if it names when the claim
holds, cut it if it lowers the writer's exposure in case she is wrong.

**Own the stat or kill it.** An unnamed population claim never survives:
"most developers", "by some estimates", and "I've seen the claim that..."
are all "studies show" with the source stripped. Convert to first person
("debugging eats enough of my time") or cut the sentence.

**Never announce the honesty.** "Full honesty:", "To be honest," appear in
the notes and get edited out of anything published. The disclosure stays
and lands plainly: "Nobody uses this yet."

## From inside the work, on the brief's facts

First person, builder's view: "As my own sidenote, template bloat can lead
to worse instruction cache utilization. Perfectly fine for hot path
however." Lived experience comes from the brief plus the author's reasoning
and taste. An invented war story, usage timeline, or habit is slop wearing
the voice.

Glue is not a license to invent reasons. "Because", "since", "so", and "on
purpose" must connect two things the brief actually gives. A motive the
brief does not state ("it does nothing else on purpose, since readable
output was the only part I ever needed") is fabricated biography dressed as
explanation. When the reason is unknown, say what happened without a
because.

On a tightening or de-slop task this guide adds nothing. Cut the tells,
keep the brief's facts, connect what remains. No new reasons, no rescued
statistics, no restated contrasts.

## The dash-thought, converted at polish

The author's native connective is the dash: "Allocations are costly —
consider a pool". Em dashes are banned in published prose, so the move
survives and the punctuation changes at polish: "Allocations are costly,
so consider a pool." The `=>` and `->` shorthand stays in notes.

## The cadence to avoid

Earlier drafts written to this skill had a recognizable rhythm: a sentence
of evidence, then a verdict of three to six words, then a paragraph break.
The first version of this guide saw "It was BAD" and "Jitter is
unacceptable" in a couple of notes and made "compress the verdict" the
first rule. In the notes those lines are rare; the model made them the
default, and the result is the most identifiable LLM tell of the moment.
Lines from those drafts:

- "The model did not change. The solver did. That is the finding worth
  building on."
- "Cache with an index. Cache with a curator. The honest names."
- "It's the attractor, not the budget."
- "Everything got quieter. Nothing got resolved."
- "Numbers." (as an entire paragraph)

The moves, each now a hard limit in personal pieces:

1. A paragraph ending on a fragment of six words or fewer: at most one per
   piece, and only as a casual aside ("Hard to set up."), never a verdict.
2. The two-beat contrast, "X. Y." or "X, not Y", as a rhetorical device:
   at most one per piece. The author writes "Bitcoin is pseudonymous, not
   anonymous", so the construction is hers, but once.
3. "That is the..." / "That's what..." / "The honest X" pronouncements:
   none.
4. One-word or two-word paragraphs: none.
5. Colon-fronted announcements ("So:", "Side by side:"): none. Fold the
   announcement into the sentence that carries the content.
6. Rule-of-three fragment lists ("Tests that fail. Code that throws. A
   transaction that will not reconcile."): none.
7. A closing line that restates the thesis as an epigram: none. End on the
   last consequence, the open question, or what the author would do next.

Why the model does this: Layer 1 strips the intensifiers and cuts every
word that does no work, so the only way left to signal a verdict is to
compress it into an aphorism. In personal pieces Layer 2 overrides that
compression. Sentence length varies. The glue, the adjectives, and the
aside in parentheses stay. A sentence with "which" and "so" and "e.g." in
it is the voice, not padding.

## Before / after

These illustrate moves. They are not stock phrases: do not reuse any
sentence from this guide in a draft.

- Before: "The model did not change. The solver did. That is the finding
  worth building on."
  After: "So the weights didn't change at all, only the configuration
  around them did, which is the part of the result I'd actually build on."
- Before: "Everything got quieter. Nothing got resolved."
  After: "Everything got quieter, however nothing actually got resolved:
  under the same ban the dev tool page still carries twice the colour of
  the back-office one."
- Before: "It's the attractor, not the budget."
  After: "Hence, the thinking budget isn't the reason. With 33x the
  reasoning the model just builds a more thorough version of the same white
  page (84% more elements, same palette)."
- Before: "That artifact is what goes."
  After: "The thing that goes away is that pre-written decision layer,
  which is a narrower claim than the paper's title makes, but it's the one
  the measurements support."

## Spoken scripts

When the piece will be heard, the ear layer stacks on this guide and wins
every conflict: say the load-bearing point twice, preview a list before it
starts, recap at the end, and keep homographs (live, read, lead) out of
the spoken text.

## Checking a draft

Run `evals/rhythm.py` on the draft before delivering a personal piece.
Connectives between fifteen and thirty per thousand words, `x_not_y` at
most one, `pronouncements` and `announcements` zero, at most one paragraph
ending on a fragment. Then read it once asking: does this walk the reader
through something, or does it stack claims? If a paragraph could be
reordered without losing anything, it is stacking.

---

Anti-slop reference: the full tell catalog and cluster rule live in
[ai-tells.md](ai-tells.md).
