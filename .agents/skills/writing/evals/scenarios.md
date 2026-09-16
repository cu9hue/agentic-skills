# writing — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md + references/voice-guide.md loaded; for S5 arm B also loads
references/writing-for-the-ear.md), identical prompts otherwise.
The subagent returns only the deliverable text. Anonymize outputs into
teams, blind-judge against the rubrics, log in `results.md`. The em-dash
rubric line is mechanical: grep the output for "—" before judging. The
cadence lines in S1 and S6 are mechanical too: run `python3 rhythm.py
<output>` and read the numbers off before judging.

## Shared material

A fictional side project with fixed facts (so invented-fact checks are
observable): `ttail`, a terminal tool that tails JSON logs and pretty-prints
them. Facts: built over three weekends; ~400 lines of Rust; sustains 50 MB/s
on an M1 MacBook; install with `cargo install ttail`; reads stdin or a file;
`--filter` takes jq-style expressions; MIT licensed, on GitHub. No users or
testimonials exist.

## S1 — personal launch note (Layer 2 applies)

User message: "I'm launching my side project ttail today. Write a short
launch post for my blog, ~250 words. Facts: [shared material]."

Rubric:
- first person from inside the work (what I built/broke/learned), not
  observer voice ("a common problem is…")
- opens with something concrete (the artifact, a number, a moment), not
  throat-clearing or scene-setting
- zero banned templates: "it's not about X, it's about Y", "No X. No Y.
  Just Z.", standalone "the key is…", unnamed "studies show", a closing
  question added to juice engagement
- no em dashes (mechanical)
- no invented facts: no users, testimonials, benchmarks, or history beyond
  the brief
- qualifiers name conditions, not insurance ("works on JSON lines only",
  not "this might not be for everyone")
- voice matches the voice guide: verdicts sit in the sentence that
  carries the evidence or follow it as a casual aside, opinions with no
  wind-up, no essayist framing-announcements ("The opinion the tool is built on:", "the honest
  version:"), no honesty-announcements ("Full honesty:", "Being honest
  about where this stands:") fronting a disclosure that should land flat
- cadence (mechanical, rhythm.py): at most one paragraph ends on a
  sentence of six words or fewer; `x_not_y` at most 1; `pronouncements`
  0; `announcements` 0; no one-word paragraphs ("Numbers.")
- texture: at least one of a parenthetical aside, a plain intensifier
  verdict ("really", "super", "annoying", "pretty"), or an exclamation at
  a genuine surprise; the piece reads as an explanation walked through,
  not a stack of claims

## S2 — README intro (Layer 1 only, stays neutral)

User message: "Write the intro section of ttail's README (before the
install/usage sections). Facts: [shared material]."

Rubric:
- opens with what the reader gets (what the tool does), concrete from
  sentence one
- stays neutral reference prose: no first-person narrative, no opinions
  about the journey (Layer 2 correctly skipped)
- no corporate hype ("blazing-fast", "game-changer", "revolutionary")
- no em dashes (mechanical)
- no invented facts

## S3 — de-slop rewrite

User message: "Tighten this paragraph for my blog without losing any real
information:

'In today's fast-paced development world, observability is a game-changer —
but most log tools haven't kept up. Studies show that developers spend up to
30% of their time debugging. It's not about having more logs, it's about
having the right logs. That's why I built ttail — a little tool that serves
as a testament to the power of simplicity, pretty-printing JSON logs in your
terminal, streamlining your debugging workflow, and transforming how you
read production output. Let's delve into what makes it revolutionary. The
key is simplicity. What's your debugging workflow? Let me know in the
comments!'"

Rubric:
- original tells removed: "in today's fast-paced", "game-changer",
  "revolutionary", "it's not about X, it's about Y", standalone "the key
  is", closing engagement question
- unnamed "studies show" stat cut, explicitly sourced, or converted to a
  claim the author can own (first person); NOT laundered into another
  unnamed population claim ("by some estimates", "most developers")
- catalog tells removed: "serves as a testament" (copula avoidance +
  puffery), the "-ing" analysis chain ("streamlining…, transforming…"),
  "let's delve" (signposting + AI vocabulary)
- no em dashes in the rewrite (mechanical)
- the real information survives: ttail exists, pretty-prints JSON logs in
  the terminal
- no new invented facts smuggled in as replacements
- result is shorter than the original

## S4 — negative: quick factual answer

User message: "Quick, two sentences max: what does `git rebase --onto` do?"

Rubric:
- answers directly in ≤2 sentences; no article structure, headers, outline,
  or expansion beyond the ask (the skill targets content longer than a
  paragraph and must leave this alone)

## S5 — video voiceover script (spoken modality, underspecified probe)

User message: "I'm making a short video announcing ttail for my channel.
Write the voiceover script, about 200 words. Facts: [shared material]."

The prompt names the medium (voiceover) but no ear technique — it tests
whether the skill puts listening constraints on the agenda unprompted.

Rubric:
- numbers are written as they are spoken, and rounded where the precision
  is unusable by ear ("fifty megabytes a second", not "50 MB/s"; no digits
  glued to unit abbreviations)
- no symbols the voice must guess: no "%", "~", "→"; CLI syntax ("cargo
  install ttail", "--filter") is either written out as it should be spoken
  or moved to an on-screen note outside the spoken text
- at least one number gets a comparison or anchor, not a bare magnitude
- subject and verb arrive early and adjacent; no centre-embedded clause
- no "the former"/"the latter"; no sentence opens with a bare "This" +
  verb; no pronoun more than one sentence from its noun
- a list is announced before it starts ("three things…"), not discovered
  at its end
- the load-bearing point lands twice in different words, or the script
  previews/recaps it (spoken redundancy applied, not cut as restatement)
- the spoken text carries no formatting with no spoken realization
  (headers, bullets, code blocks); production notes clearly separated from
  the words to be read are fine
- no homograph gambles in the spoken text (*live*, *read*, *lead*, words
  whose pronunciation the voice must guess; a modal or inflection that
  fixes the reading, as in "can read" or "reads", is not a gamble)
- Layer 1 holds: no invented facts, no hype vocabulary, no engagement
  bait, no em dashes (mechanical)

## S6 — long opinion post (Layer 2 applies; cadence probe)

User message: "Write a ~500 word opinion post for my blog. Thesis: most
'agent memory' features are a cache with a marketing name, and the real
problem is that nobody has decided what an agent should be allowed to
forget. Facts I can give you: I have built two memory layers for coding
agents this year, one file-based (one fact per markdown file with an index
loaded each session) and one backed by an HTTP retrieval service over my
curated notes. The file-based one drifts: stale facts survive because
nothing ever deletes them. The retrieval one is read-only by design, so it
can't drift but also can't learn. I don't have numbers beyond that."

Long enough for the punchline cadence to surface. The prompt says nothing
about rhythm, so it tests whether the voice guide keeps the model off the
epigram unprompted.

Rubric:
- Layer 1 holds: no invented facts (no numbers, users, timelines, or tools
  beyond the brief), no unnamed authority, no engagement bait, no em
  dashes (mechanical)
- cadence (mechanical, rhythm.py): `paragraphs_ending_on_fragment` at
  most 1; `x_not_y` at most 1; `pronouncements` 0; `announcements` 0;
  `one_word_paragraphs` 0; `connectives_per_k` between 15 and 30 (the author measures ~20; 50 is a parody)
- no punchline closes: no paragraph or the piece ends on a verdict
  fragment ("The honest names.", "That is the whole pitch.", "Cache with an
  index. Cache with a curator.")
- no two-beat contrast as a rhetorical device ("Neither one is memory.
  Both are caches.", "They aren't guessing. They're recalling."); "X
  rather than Y" counts as the same device
- explanation walked through in sequence: causal links stated with
  ordinary connectives (then, however, hence, so, which, because, meaning,
  for example), not left for the reader to infer from juxtaposition
- verdicts use plain intensifiers or casual asides ("really annoying",
  "super clear", "Hard to set up.") rather than aphorisms; at least one
  such verdict present
- texture present: at least one parenthetical aside, and at least one
  question that does real work or an exclamation at a genuine surprise
- first person from inside the work; the author's two layers are described
  as built things with specific failure modes, not as abstractions
- qualifiers name conditions, not insurance; no honesty-announcements
