# socratic — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
skill + question-bank loaded), identical prompts otherwise. Anonymize both
arms' outputs into teams, hand a blind judge the rubrics, log the verdict in
`results.md`. Each subagent replies with the exact next chat message only.

## Shared material

A condensed version of Sutton's "The Bitter Lesson" (2019), core ideas:

1. Moore's-law driver — exponentially cheaper compute is the ultimate reason
   general methods win; researchers plan as if compute were constant.
2. Human-knowledge methods gain short-term then plateau; search/learning win
   late but completely (chess, Go, speech, vision).
3. Build meta-methods that discover complexity, not the contents of minds.

Reconstruct the ~250-word condensation from these ideas (include the "over
any horizon longer than a typical project" phrasing and the "personally
satisfying / feels like real understanding" bitter part) and give it to the
subagents as a file.

## S1 — opening move

User message: "I just read this article. Run a socratic session with me to
make sure I deeply understand it."

Rubric:
- exactly one question this turn (question dumps fail)
- question requires reasoning, not recall/recitation
- no answer leakage: does not hand the user a claim they have not yet
  produced (quoting the source's key claim in the framing fails)
- sets expectations (pacing, steering) without lecturing about the article

## S2 — first wrong answer

Transcript: tutor asked what Sutton identifies as the underlying driver of
the plateau-vs-win pattern. User's FIRST wrong answer on this point:
"Because human knowledge is basically wrong — experts don't actually
understand how they do what they do, so encoding their knowledge encodes
their mistakes." (Actual driver: exponentially cheaper compute.)

Rubric:
- stays Socratic: no explanation of the correct answer on a first miss
- hint narrows the search space without containing the answer — naming the
  answer's category ("an economic fact") counts as a reveal
- exactly one question posed
- engages the user's specific error, not a generic redirect

## S3 — wrap-up with one revealed gap

Setup: session covered ideas 2 and 3 solidly; the user never articulated
idea 1 even after two probes and the tutor had to reveal it. User: "ok let's
wrap up here."

Rubric:
- per-idea report, solid vs gap clearly attributed
- names what specifically tripped the user up on the gap
- points to what to reread / how to repair
- retention: produces spaced-repetition cards covering BOTH solid and gapped
  ideas, gap card targeting the exact miss

## S4 — negative: should not trigger

User message (no socratic request anywhere): "Summarize this article for me
in three bullets."

Rubric:
- responds with a summary; does NOT start a questioning session or withhold
  the summary to make the user reason it out
