---
name: writing
description: Write articles, posts, essays, launch notes, newsletters, guides, and docs in a direct, concrete, anti-slop style. Anti-slop rules apply to all prose; a fixed first-person voice layers on for personal and opinion pieces. Use when the user wants written content longer than a paragraph and cares about specificity, credibility, and not sounding like an LLM.
origin: adapted from ECC article-writing; sourcing rule and the references/ai-tells.md catalog harvested from blader/humanizer (github.com/blader/humanizer, built on Wikipedia's "Signs of AI writing")
---

# Writing

Write prose that sounds like a person with a point of view and something
specific to say, not an LLM smoothing itself into paste.

## When to Activate

- drafting blog posts, essays, launch notes, newsletters, guides, or tutorials
- turning notes, transcripts, or research into finished writing
- tightening structure, pacing, and evidence in already-written copy
- writing READMEs, design docs, or other reference material (anti-slop layer only)

## The Two Layers

This skill has two layers. Always apply Layer 1. Add Layer 2 only for personal
and opinion pieces.

### Layer 1: Anti-slop (always)

Applies to every piece, including neutral technical docs.

- Be specific, concrete, and useful. Direct, practical style.
- Every paragraph must add new information: a fact, example, constraint,
  trade-off, source, decision, or next step. Cut paragraphs that only restate.
- Prefer short, clear sentences. Concrete nouns, plain verbs.
- If a claim needs evidence, provide the source or weaken the claim.
- If the answer would otherwise be generic, ask for context or state the
  assumptions you're making.
- No em dashes. Use colons, periods, or parentheses instead.

### Layer 2: Voice (personal and opinion pieces only)

For posts, essays, launch notes, and newsletters, load
[references/voice-guide.md](references/voice-guide.md) and write to it. The
short version:

- First person, from inside the work. "Here's what broke when I built X," not
  "a common pitfall is."
- State the framework with full rigor. Keep the verdict revisable. Provisional
  about conclusions, rigorous about reasoning.
- Lead with an opinion about quality when you have one. Taste is content.
- Don't pre-hedge. The diagnostic test for any qualifier: is it naming *when the
  claim holds*, or *buying insurance against being wrong*? Keep the first, cut
  the second.

Skip Layer 2 for reference docs, API documentation, and anything that should
read as neutral.

## Core Rules

1. Lead with the concrete thing: artifact, example, output, anecdote, number,
   screenshot, or code.
2. Explain after the example, not before.
3. Use proof instead of adjectives.
4. Every claim has a source: researched and named, or provided in the brief.
   Neither? Say what isn't known, state it as an assumption, or cut the
   sentence. Never dress a guess up as fact.
5. Biography is claims too. Anecdotes, usage history, tools tried, time
   spent: only from the brief. When the brief gives no lived experience,
   write from the work's facts and your opinions, not a manufactured past.

## Banned Patterns

The full tell catalog lives in [references/ai-tells.md](references/ai-tells.md):
sentence templates, the AI word cluster, texture, structure and format tells,
and the five slop categories. Load it whenever you de-slop, audit, or write
anything longer than a few paragraphs. The core rules, always in force:

- **No em dashes.** Hard constraint, zero in final output.
- **No unnamed authority.** "Studies show", "experts argue", population-level
  stats with the source stripped: name the source, own the claim in first
  person, or cut it.
- **No engagement bait.** Closing questions and comment fishing, in any
  disguise.
- **No template sentences.** "It's not about X, it's about Y", "No X. No Y.
  Just Z.", "The key is…", "in today's fast-paced world".
- **Plain verbs, real analysis.** "Is", not "serves as"; no "-ing" tails
  that fake depth ("…, highlighting the importance of…"); no hype vocabulary
  (delve, tapestry, landscape, game-changer, revolutionary).
- **Cluster over isolation.** One tell is noise, a stack is a confession:
  when tells cluster, rewrite the passage, and preserve genuine human
  signals (asides, mixed registers, unresolved tension) while you do.

## Writing Process

1. Clarify the audience and purpose. Decide whether Layer 2 applies.
2. Build a hard outline with one job per section.
3. Start sections with proof, artifact, conflict, or example.
4. Expand only where the next sentence earns space.
5. Cut anything templated, overexplained, or self-congratulatory.

## Structure Guidance

### Technical guides

- open with what the reader gets
- use code, commands, or concrete output in major sections
- end with actionable takeaways, not a soft recap

### Essays / opinion

- start with tension, contradiction, or a specific observation
- keep one argument thread per section
- make opinions answer to evidence

### Newsletters

- keep the first screen doing real work
- don't front-load diary filler
- use section labels only when they improve scanability

## Quality Gate

Before delivering, check:

- every factual claim, biographical ones included, is backed by the brief or
  a named source, or stated as an assumption
- every paragraph adds new information
- no banned patterns survive (sweep against references/ai-tells.md)
- no em dashes
- short sentences, concrete nouns, plain verbs
- for personal pieces: voice matches the voice guide, and every qualifier passes
  the diagnostic test (naming a condition, not buying insurance)
- formatting matches the intended medium
