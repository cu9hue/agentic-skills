# writing — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md + references/voice-guide.md loaded), identical prompts otherwise.
The subagent returns only the deliverable text. Anonymize outputs into
teams, blind-judge against the rubrics, log in `results.md`. The em-dash
rubric line is mechanical: grep the output for "—" before judging.

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
having the right logs. That's why I built ttail — a revolutionary little
tool that pretty-prints JSON logs in your terminal. The key is simplicity.
What's your debugging workflow? Let me know in the comments!'"

Rubric:
- every tell removed: "in today's fast-paced", "game-changer",
  "revolutionary", unnamed "studies show" (cut or explicitly sourced/
  weakened), "it's not about X, it's about Y", standalone "the key is",
  closing engagement question
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
