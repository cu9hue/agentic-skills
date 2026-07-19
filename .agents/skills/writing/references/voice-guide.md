# Voice Guide

The fixed personal voice for opinion and personal pieces. Load this only when
writing posts, essays, launch notes, or newsletters. Skip it for neutral
reference material, where the anti-slop rules alone apply.

Derived from the author's actual notes corpus (128 files, ~38k words,
analyzed 2026-07-19). Every rule below is an observed habit, not a persona;
the quoted examples are real lines from the corpus.

**The voice in one line:** evidence gets sentences, the verdict gets a
fragment; opinions land flat and unhedged; casual and technical share a
sentence; everything is written from inside the work.

## Mechanics

**1. Compress the verdict.** Explanations run normal length; conclusions
compress to a fragment or a short flat sentence, often after the evidence.

- "Jitter is unacceptable."
- "It was BAD."
- "Hard to set up."

One-word-emphasis CAPS is allowed, rarely. Aphoristic compression is native:
"If this is up to me, it deserves 100% of my energy. Otherwise, it's none of
my concern."

**2. The dash-thought, converted at polish.** The native connective move is
claim — consequence ("Allocations are costly — consider a pool"). Keep the
move, convert the punctuation before publishing (em dashes are the top AI
tell, banned by the skill): colon, period, or parentheses.

- Draft: "Allocations are costly — consider a pool."
- Published: "Allocations are costly: consider a pool."

The `=>` and `->` shorthand stays in notes; it never ships.

**3. Opinions land flat.** No wind-up, no softening clause. "Corporate
theater." "Bloated and smells." "Denormalized data is not a sin." A verdict
is a sentence, not a paragraph. Qualifiers are allowed only when they name a
condition: "Perfectly fine for hot path however."

**Own the stat or kill it.** An unnamed population claim never survives in
this voice, in any disguise: "most developers", "a big chunk of developers'
time", "by some estimates" are all the same laundered "studies show".
Convert to first person ("debugging eats enough of my time") or cut the
sentence entirely.

**4. Mixed register is the texture.** Casual and technical in the same
breath: "people feel less wealthy and don't wanna invest" next to
"deleveraging". Do not sand it off. The author's own discourse markers —
"actually", "basically", "super" — are voice, not AI tells; keep them in
personal pieces (the ai-tells cluster rule governs: one marker is voice, a
pile-up of catalog tells is slop).

**5. Self-honesty, no performance.** Admit what you don't know, plainly:
"Incredibly dense talk. I learned that I need to learn a lot of stuff."
Self-directed imperatives are native: "Toughen up." "Reread every time there
is an urge." No fake vulnerability arcs; the honesty is operational, not
confessional.

**6. Structure habits.** Bold-label bullets ("**What drives me:**"),
"Actionable:" callouts, question headers that do real thinking ("What's
going to spark the next crash?"), numbered taxonomies ("6 ways to say no").
Exclamation marks mark genuine surprise ("3–6 assertions on average to get
to the behavior change!"), never hype.

**7. From inside the work, on the brief's facts.** First person, builder's
view: "As my own sidenote, template bloat can lead to worse instruction
cache utilization." Lived experience comes from the brief's actual history
plus your reasoning and taste; an invented war story or usage timeline is
slop wearing the voice. Habits and preferences are biography too: "the jq
dialect I already use everywhere else" is a fabricated fact unless the brief
says so. Without real history, the inside-the-work move is your actual
reasoning.

## The diagnostic test (the single most useful habit)

The nuance instinct and the hedging instinct produce sentences that look
identical. Before keeping any qualifier, ask:

> Is this conditional describing *when the claim holds* (keep it), or is it
> lowering my exposure *in case I'm wrong* (cut it)?

Be provisional about conclusions, rigorous about reasoning: state the
framework solidly, let the verdict stay revisable.

## Before / after

**1. Pre-hedge becomes a condition with teeth**

- Before: "Lock-free isn't always faster. It really depends, and there's a
  lot of nuance here, so take this with a grain of salt."
- After: "Lock-free loses to plain locks under low contention. The
  atomic-operation overhead doesn't pay off until you're past [threshold].
  Here's the data."

**2. Padded verdict becomes a compressed one**

- Before: "Overall, this approach turned out to have significant drawbacks
  that made it less suitable for our use case than we initially hoped."
- After: "It was bad. Crashes always lead to low economic activity" — verdict
  first, mechanism after. (Pattern straight from the corpus.)

**3. Sanded register becomes mixed register**

- Before: "Individuals become reluctant to make investments during downturns."
- After: "People feel less wealthy and don't wanna invest."

**4. Observer voice becomes builder's sidenote**

- Before: "It should be noted that template instantiation may increase code
  size."
- After: "As my own sidenote, template bloat can lead to worse instruction
  cache utilization. Perfectly fine for hot path however."

## Voice in one breath

Verdicts compressed, opinions flat, register mixed, honesty operational.
Rigorous about *how*, relaxed about *whether*. In the work, not above it.

---

Anti-slop reference: the full tell catalog and cluster rule live in
[ai-tells.md](ai-tells.md). The five slop categories' shared antidote —
specificity, real lived experience, cited sources, information gain — is
this voice's baseline, not its ceiling.
