# lateral-ideation — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
skill loaded), identical prompts otherwise. Both arms: no web tools, no Skill
tool, no other local files; the skill arm reads SKILL.md and its references
first. Each subagent returns exactly its reply to the user. Anonymize outputs
into teams, blind-judge against the rubrics, log the verdict in `results.md`.

## S1 — named framework on a product seed

User message: "Run SCAMPER on a meeting-notes app like Granola. I want new
product directions, not feature tweaks."

Rubric:
- Every idea names a concrete behaviour, user or situation. No idea only
  restates the SCAMPER letter ("combine it with other tools").
- At least two ideas are non-obvious: not AI summaries, integrations, search,
  action items or a CRM sync.
- At least one idea is followed past the first step to a second- or
  third-order effect ("and then…").
- The reply converges: it picks 2–3 ideas and develops them, instead of
  ending on seven equal one-liners.
- At least one developed idea is made tangible: a specific object, screen,
  message or failure state from the world where it exists.

## S2 — structural probe: underspecified ask

User message: "Local models are getting really fast and cheap. Help me come
up with ideas."

Rubric:
- Extrapolates second- and third-order effects of the signal before, or as
  the source of, the ideas.
- Uses at least two distinct, named creative moves (for example inversion,
  splitting into parts, maximize/minimize, random metaphor, provocation) and
  the moves visibly produce ideas the plain list would not.
- Judges ideas on more than likelihood: separates probable from preferable,
  and keeps at least one future nobody would want.
- Makes at least one idea tangible as an artifact from that future (an
  ordinary object, interface, ad, or error state).
- Ends with at least one stated theory ("I think X by Y") and the evidence
  that would back or kill it.
- Is NOT a flat list of 8+ "app that uses a local model to do X" ideas.

## S3 — speculative design for a talk

User message: "What might family life look like when every household has an
always-on agent? I'm giving a talk and want something provocative, not a
trend report."

Rubric:
- Produces at least two artifacts from the future: ordinary, specific
  objects or interfaces (a receipt, a fridge note, a school letter, a
  settings screen), not abstract scenarios.
- At least one artifact shows a failure or edge case, not a happy path.
- Explores at least one undesirable future seriously, without moralizing.
- Provocations are specific (named situations, numbers, roles), not
  abstractions like "privacy concerns" or "changing family dynamics".
- Gives the speaker a theory they can state on stage and the data they would
  need to back it.

## S4 — negative: definition question

User message: "What does SCAMPER stand for?"

Rubric:
- Answers directly: the seven words, at most a line each.
- Runs no ideation, asks no questions, offers at most one line of follow-up.

## S5 — negative: one card

User message: "I'm stuck on my essay intro. Give me an oblique strategy."

Rubric:
- Gives one card (at most three), short.
- Does not run a framework, a pipeline, or a list of techniques.
- Does not reproduce a long run of verbatim cards from the Eno/Schmidt deck.
