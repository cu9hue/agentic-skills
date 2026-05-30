---
name: writing
description: Write articles, posts, essays, launch notes, newsletters, guides, and docs in a direct, concrete, anti-slop style. Anti-slop rules apply to all prose; a fixed first-person voice layers on for personal and opinion pieces. Use when the user wants written content longer than a paragraph and cares about specificity, credibility, and not sounding like an LLM.
origin: adapted from ECC article-writing
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
4. Never invent facts, credibility, or customer evidence.

## Banned Patterns

Delete and rewrite any of these.

**Sentence templates:**
- "It's not about X, it's about Y"
- "No X. No Y. Just Z."
- "In today's fast-paced world" / "In today's rapidly evolving landscape"
- "The key is..." as a standalone insight
- "Studies show..." or "research suggests..." without naming the source
- "here's why this matters" as a standalone bridge
- a closing question added only to juice engagement

**Texture:**
- em dashes
- literary flourish, vague profundity, motivational language
- corporate filler and hype ("game-changer", "cutting-edge", "revolutionary")
- generic AI throat-clearing that delays the point
- fake vulnerability arcs
- biography padding that does not move the argument

**The five slop categories** (from <https://slopdetector.org/slop-taxonomy>),
with their tells:
1. **Generic** ("In today's fast-paced world..."): templated, no concrete detail.
2. **Pseudo-insight** ("The key is to find balance..."): sounds deep, says nothing.
3. **Fake authority** ("Studies have shown..."): authoritative tone, zero sources.
4. **Wikipedia rehash** ("X is defined as..."): basic definitions sold as analysis.
5. **Wellness** ("Self-care isn't selfish..."): universal advice that helps no one.

The antidote to all five is the same: specificity, lived experience, cited
sources, real information gain.

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

- every factual claim is backed by a provided source, or stated as an assumption
- every paragraph adds new information
- no banned patterns survive (run the slop-category tells)
- no em dashes
- short sentences, concrete nouns, plain verbs
- for personal pieces: voice matches the voice guide, and every qualifier passes
  the diagnostic test (naming a condition, not buying insurance)
- formatting matches the intended medium
