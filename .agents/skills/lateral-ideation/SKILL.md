---
name: lateral-ideation
description: "Use when the user wants ideas from creative or lateral-thinking techniques: SCAMPER, oblique strategies, inversion, provocation, speculative or design fiction, \"what might X look like when…\", \"help me come up with ideas\" from a signal, product or theory, or artifacts from the future for a talk or prototype. Not for choosing which market to explore (market-selection) or judging one idea (market-evaluation)."
origin: "Pipeline (weak signal → second- and third-order effects → play → artifacts from the future → public theory) from Maggie Appleton, \"Fortune Telling and Speculative Design for Fun and Profit\" (Granola design engineers meetup, 2026). Moves from SCAMPER (Bob Eberle, 1971, after Alex Osborn), Michael Michalko's Tinkertoys (attribute splitting, idea box, Brutethink), and Edward de Bono's Lateral Thinking (reversal, po provocation, random entry, challenge). Futures cone after Hancock & Bezold (1994) and Voros (2003). Artifacts from the future from Dunne & Raby, Speculative Everything, and Bleecker et al., The Manual of Design Fiction. The card deck in references/cards.md is original, written in the spirit of Eno & Schmidt's Oblique Strategies (1975); it copies none of their cards."
---

# Lateral Ideation

Generate ideas by pushing a seed through structured creative moves, then make
the best ones concrete enough to argue with. A plain list of plausible ideas
is the failure this skill exists to prevent. The base model, asked for ideas,
sorts obvious ones into buckets. This skill chains, distorts, picks, and
builds.

Interesting beats correct. Specific beats general. A future nobody wants is
still worth drawing, because it might happen.

## Match the size of the ask

- **A definition or a how-to** ("what does SCAMPER stand for?", "how does
  random entry work?"): answer directly in a few lines. Run nothing.
- **One card** ("give me an oblique strategy", "I'm stuck"): draw one card
  from `references/cards.md` (see "Draw at random"), print it, and apply it
  to the user's situation in two or three sentences. One card. Never print
  cards from the Eno/Schmidt deck.
- **Ideas, futures, provocations, or "help me think about X"**: the full run.
- **A named move or framework on a seed** ("invert this", "SCAMPER this"):
  the full run. The named move replaces the draw in step 3. Every other
  step still runs, including the chains and the cone.
- **"Facilitate", "run a session with me", "walk me through it"**:
  facilitated mode, below.

## Never block on questions

Do not open with questions. Infer the seed, mark it *(assumed)*, deliver the
full run, and end with at most two questions that would change the output
most. Ask first only when the message carries no seed at all and no vault is
available (see step 1).

## Draw at random

Models pick the comfortable moves every time. Draw with a shell when one is
available:

```sh
awk '/^### /' references/moves.md | sort -R | head -n 3              # moves
awk '/^- /' references/cards.md | sort -R | head -n 1                # one card
awk '/^## Random/{f=1} f && /^- /' references/moves.md | sort -R | head -n 1   # concept
```

Run these from the skill directory. Without a shell, use the current minute
as an index into the list, and say so. Keep a draw that feels awkward: the
awkward move is the one that produces the idea a plain list would not. Swap
a move only when it cannot apply to the seed at all, and say which one you
swapped.

## The full run

### 1. Seed

Restate the input as one sentence: a signal, a product, a problem, or a
theory. When the user named a signal ("local models are getting fast"), the
seed is that signal, stated as something more true this year than last.

No seed in the message: when `SECOND_BRAIN_URL` and
`SECOND_BRAIN_READER_TOKEN` are set, query the vault through the
`second-brain-retrieval` API with one- to three-word terms from the
conversation and use the most recent signal or open question it returns,
citing the note. Otherwise ask one question: "What have you noticed lately
that nobody has named yet?" Scouting for fresh signals across the web belongs
to `market-selection`; point there when the user wants that.

### 2. And then

Write two chains of consequence, three links each: the seed, its first-order
effect, the effect of that, and the effect of that. Each link is one
sentence. A chain that ends where any trend article would end has stopped too
early. Example shape: agents browse the web for people → sites stop blocking
bots → sites charge agents with an ad the agent must show its human → the
"show your human" ad becomes a regulated format.

The third links are seeds for the moves.

### 3. Moves

Draw three moves (four for a broad seed) from `references/moves.md`. When the
user named a framework, run that framework instead of the draw: every
SCAMPER letter, at most two ideas per letter, skipping a letter only if you
say why.

For each move, write the move's name, one line on what it did to the seed,
and one or two ideas. Every idea names a person, a situation, and a thing
that happens. These do not count as ideas:

- "An AI-powered X", "an app that uses a model to do X", "X for Y" with
  nothing else said.
- A restatement of the move ("combine it with other tools").
- Summaries, search, integrations, dashboards, or a CRM sync, unless the
  move turned them into something else.

Cap the run at 12 ideas. Fewer, stranger ideas beat more, safer ones.

### 4. Futures cone

Place each surviving idea on the cone: **possible** (physics allows it),
**plausible** (could happen given what we know), or **probable** (likely
without anyone pushing). Then mark it **preferable** or not, separately: is
this a future we want?

Keep at least one idea that is probable or plausible and not preferable, and
treat it as seriously as the others. Describe it. Do not moralize about it.
Show the cone as a short table.

### 5. Pick

Pick two or three ideas to develop. Say in one line each why it was picked:
it surprised you, it fell out of a chain nobody else will follow, or it makes
the unwanted future concrete. Name the ideas you dropped and the reason, in
one line total.

### 6. Artifacts from the future

For each picked idea, make one artifact: an ordinary object or interface from
the world where the idea is true. Banal and domestic beats grand. Good forms:
a receipt, a changelog, an error message, a settings screen, a job ad, a
school letter, a cereal box, a code review comment, a terms-of-service
clause, a support ticket, a classified ad.

Write the artifact itself, not a description of it: the actual text of the
receipt, with line items, prices and a date. At least one artifact shows a
failure state. Things go wrong at the edges, and the edges reveal how the
system works.

### 7. Theories

State one to three theories the user could say out loud: "I think [specific
claim] by [date]." Under each, write:

- **Backs it:** the number or event that would show it is happening, and
  where to find it (a pricing page, a filing, a benchmark, job ads).
- **Kills it:** the number or event that would show it is wrong.

Never invent a figure. A number you have not seen in this session gets
*(needs source)*.

### 8. Next

End with one line offering the single most useful next step: build one
artifact as a page or image, run the facilitated session on one idea, or
hand a business-shaped theory to `market-map` (map the problem space),
`market-evaluation` (judge the market), or `research-gates` (set kill
criteria). Then the at-most-two questions.

## Reply shape

```
**Seed:** … *(assumed)*

**And then**
1. … → … → … → …
2. … → … → … → …

**Moves** (drawn: Invert, Brutethink: lighthouse, Maximize)
- **Invert:** <what it did>. <idea>. <idea>.
- …

**Cone**
| Idea | Cone | Preferable? |

**Picked:** <idea> because …; <idea> because …. Dropped: …

**Artifacts**
<artifact 1, rendered as itself>
<artifact 2, a failure state>

**Theories**
- I think … by …. Backs it: …. Kills it: ….

**Next:** …
```

Keep each section tight. The artifacts are where length is worth spending.

## Facilitated mode

Run the same steps with the user doing the thinking. One step per turn:

1. Agree the seed in one sentence.
2. Ask for the first "and then"; add one link of your own only if they stall.
3. Draw one move per turn. Give the move, one example of it applied to an
   unrelated seed, and wait for their idea. Push their idea one step further
   before drawing the next move.
4. After three moves, show the cone of their ideas and ask which one to
   build.
5. Draft the artifact with them, then write the theory together.

Never answer for the user in facilitated mode. Your examples use an
unrelated seed so they do not anchor the answer.
