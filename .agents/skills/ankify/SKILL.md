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
2. Draft cards that clear the value bar (below), following the writing rules.
3. Present them as markdown for keep / cut / edit. Open with one line on why
   these cards earn their place. The editing is where the learning happens — say so.

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

There is no target number. Extract the source's **core ideas** — the load-bearing
concepts it is actually built on, the ones you would fail to understand it
without — and make **one card per idea**. A thin source carries two or three; a
rich one carries more. Let the count fall out of the ideas: never pad to fill a
deck, never truncate a source that genuinely holds more. The bloat to fight is
carding *detail, examples, and restatements* as if they were core, and splitting
one idea across several cards — not a high count of real ideas. Card only what you
actually understood from your read. **If nothing clears the bar, make no cards.**

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
- **Plain language** — phrase every card by the `writing` skill's anti-slop rules:
  concrete, no filler, no hedging, no inflated abstractions. A card you have to
  reread to parse is a card you will dread.
- **Cloze sparingly**; never write a card you will dread reviewing.

## Output format

Markdown, grouped by topic. Most cards are Q / A:

```
Q: ...
A: ...
```

Use cloze sparingly, and only when the deletion lands on the load-bearing
idea — not to blank out a stray word:

```
Cloze: The Transformer drops {{c1::recurrence}} so computation parallelizes across {{c2::positions}}.
```

No import file — copy the keepers into Anki yourself.

## Quality gate

Before delivering, confirm:

- every card is worth its lifetime of review minutes — if you would not spend
  them on it, cut it
- each card is one of the source's core ideas — not a detail, example, or restatement
- the count matches the ideas — nothing padded to a quota, nothing truncated
- no two cards test the same idea — near-duplicates merged
- every card is atomic; zero yes/no questions
- specific findings are source-qualified
- if nothing cleared the bar, you made no cards
- phrasing follows the `writing` skill's anti-slop rules
