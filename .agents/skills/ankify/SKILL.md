---
name: ankify
description: Use when turning a paper, article, book chapter, doc, or notes into Anki flashcards or spaced-repetition cards — triggers like "make Anki cards", "ankify this", "flashcards from this". For retaining conceptual understanding, not rote facts.
origin: synthesized from Michael Nielsen, "Augmenting Long-Term Memory" (augmentingcognition.com/ltm.html); deliberately biased toward conceptual knowledge over the factual recall cards Nielsen also keeps
---

# Ankify

Every card you keep costs review minutes for years. So the bar is high: a card
earns its place only if recalling it changes how you think or what you can do.
This skill drafts candidates from a source; you curate. Writing and editing the
cards is itself the learning, so the final keep / cut / edit is yours.

## When to Use

- turning a paper, article, book chapter, doc, or notes into Anki cards
- "make flashcards", "ankify this", "cards from this paper"
- studying to retain understanding you will reuse, not trivia you can look up

Not for generating a card per fact, or for material you do not yet understand —
ankify understanding, not text.

## How it runs

1. Read the source. For a research paper, run the `digest-paper` skill first if
   you have not — its passes surface what is worth keeping. Otherwise read directly.
2. **Map the spine before you write a single card.** Name the source's central
   claim in one sentence, then list the load-bearing ideas holding it up — the
   ones you could not understand the claim without. Build it from the whole
   source at once, never section by section: a spine assembled a section at a
   time is just the table of contents, and that is exactly how a big idea loses
   to whatever detail happened to be locally vivid.
3. Draft one card per spine node, applying the value bar and the writing rules.
   A candidate card that maps to no node on the spine is a detail — cut it.
4. Present the spine first, then the cards under it, for keep / cut / edit. The
   spine is what lets you see at a glance that an idea got skipped. Open with one
   line on why these cards earn their place. The editing is where the learning
   happens — say so.

## The value bar (apply before writing any card)

Ask of each candidate two things: *will recalling this change how I think or
what I can do?* and *is it worth the review minutes it will cost me for years?*
A card has to earn both. This trade — your future time against the value of the
memory — is the whole filter; everything below serves it.

Keep cards for:

- mechanisms — how something actually works
- causal "why", trade-offs, when to use what
- conceptual distinctions and definitions you will reason with
- transferable principles that outlive this source
- a surprising result *and the reason* it is surprising

Cut lookup-able trivia: dates, author names, benchmark scores, hardware,
hyperparameters, isolated numbers — unless the number *is* the insight (a
constant that anchors an estimate). When in doubt, cut.

There is no target number. The spine is the list of ideas — make **one card per
spine node**. A thin source carries two or three; a rich one carries more. Let the
count fall out of the spine: never pad to fill a deck, never truncate a source
that genuinely holds more. The bloat to fight is carding *detail, examples, and
restatements* as if they were core, and splitting one idea across several cards —
not a high count of real ideas. A long source that argues by worked example is
the trap: several examples demonstrating one idea are **one card**, not one card
each. Card only what you actually understood from your read. **If nothing clears
the bar, make no cards.**

## Writing rules

- **Atomic** — one idea per card. Split compound facts so a lapse points at
  exactly what you forgot. Never bundle a concept with a number "to save a card".
- **No yes/no questions** — reframe into which / why / how / for what.
- **One idea, one card** — never reframe the same point into two or three
  near-duplicate cards. Merge overlapping candidates and keep the sharpest. (Still
  avoid lone facts disconnected from everything you know.)
- **Source-qualify findings** — "What does Vaswani 2017 claim about path length…",
  not a bare fact, when it is a specific result that could be wrong.
- **Understanding over recall** — prefer "why does X help?" to "what is X?".
- **Images** — default to text. Text forces you to reconstruct the idea; an image
  invites recognition without understanding. Add one only when the answer is
  inherently spatial and you must reproduce or label it: a diagram, a memory or
  struct layout, a protocol header layout, a topology, a state machine. For
  those, prefer Anki's Image Occlusion — hide the labels, fields, or states and
  recall them — over a static picture on the back. Never use an image as
  decoration, or to stand in for a mechanistic or causal explanation.
- **Plain language** — phrase every card by the `writing` skill's anti-slop rules:
  concrete, no filler, no hedging, no inflated abstractions. A card you have to
  reread to parse is a card you will dread.
- **Cloze sparingly**; never write a card you will dread reviewing.

## Output format

These cards get retyped into Anki's Add dialog by hand, so the format serves
exactly one goal: select a side, copy it, in a single gesture.

Put the cards in a fenced code block, grouped by topic under plain markdown
headings. One card is **two adjacent lines** — front, then back. No `Q:` / `A:`
prefixes to strip, no indentation to sweep up. A blank line separates cards.

```
Why does TIME_WAIT last 2*MSL?
So late duplicates from the dead connection expire before the same port pair is reused.

What does the TCP checksum's pseudo-header bind a segment to?
The source and destination IP addresses, so a segment cannot land on the right port of the wrong host.
```

**Never hard-wrap a side.** Each front and each back is exactly one line, however
long it runs — let the terminal soft-wrap it. A hard-wrapped side costs a second
selection, which is the whole reason this format exists. And if a side is too long
to sit on one line comfortably, that is a fact about the card, not the format: it
is not atomic, so split it.

Nothing else goes inside a card side — no bullets, no numbered lists, no bold
markers, no table pipes. Every one of them survives the paste and has to be
cleaned out by hand.

Cloze cards need Anki's Cloze note type, so they go in their own labeled block,
one card per line. Use them sparingly, and only when the deletion lands on the
load-bearing idea — never to blank out a stray word:

Cloze:

```
The Transformer drops {{c1::recurrence}} so computation parallelizes across {{c2::positions}}.
```

No import file — you copy the keepers into Anki yourself.

## Quality gate

Before delivering, confirm:

- the spine is stated above the cards, and every card maps to a node on it — no
  orphan details
- no spine node is missing a card unless it explicitly failed the value bar
- every card is worth its lifetime of review minutes — if you would not spend
  them on it, cut it
- each card is one of the source's core ideas — not a detail, example, or restatement
- repeated examples of a single idea are one card, not one card each
- the count matches the spine — nothing padded to a quota, nothing truncated
- no two cards test the same idea — near-duplicates merged
- every card is atomic; zero yes/no questions
- specific findings are source-qualified
- no card side is hard-wrapped; no `Q:` / `A:` prefixes; no bullets, list
  markers, or bold markup inside a card side
- images appear only for spatial answers (layouts, topologies, state machines),
  preferably via Image Occlusion, never as decoration or a substitute for
  reconstruction
- if nothing cleared the bar, you made no cards
- phrasing follows the `writing` skill's anti-slop rules
