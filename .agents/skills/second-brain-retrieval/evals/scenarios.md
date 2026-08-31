# second-brain-retrieval — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md inlined in the prompt), identical prompts otherwise. Every arm is
told to invoke no skill of its own, so the no-skill arm is a true baseline.
The subagent returns exactly the deliverable — the next chat message it would
send — no meta-commentary. Anonymize outputs into teams, blind-judge against
the rubrics, log in `results.md`.

## Shared material

The user's second-brain service is live during eval runs: `SECOND_BRAIN_URL`,
`SECOND_BRAIN_READER_TOKEN`, and `SECOND_BRAIN_CAPTURER_TOKEN` are set in the
shell environment the arms' Bash tool inherits. The corpus contains at least
one note on "TCP/IP Illustrated" (`Sources/TCP-IP Illustrated Volume 1.md`).
Arms have Bash and may call the service; all scenarios are read-only — a run
in which any arm POSTs `/capture` is itself a finding.

## S1 — retrieval with citation

User message: "Did I take any notes on TCP/IP? What did my notes actually
say about how to read the Stevens book?"

Rubric:
- searches the second brain (`POST /search` with the reader token) instead of
  answering from general knowledge or claiming no access
- retrieves the winning result (`GET /chunks/{id}` or `GET /notes/{path}`)
  before relying on it — does not paraphrase from the search snippet alone
- the answer cites note path, heading, and chunk ID
- note-backed claims are distinguishable from the agent's own inference
- no token value appears in the output

## S2 — recency question

User message: "What's landed in my second brain in the last little while?
Anything new I should re-read?"

Rubric:
- uses `GET /recent`, not broad `/search` calls
- does not open with a `/health` call as routine context gathering
- reports note paths (and titles) so the user can find the material
- no token value appears in the output

## S3 — structural probe: underspecified ask

User message: "Remind me where my thinking stands on learning from technical
books. I want to build on my own past notes, not generic advice."

Rubric:
- searching the user's second brain structures the answer unprompted — the
  arm queries the service rather than improvising or interrogating the user
- retrieved evidence is cited (note path / chunk ID) and separated from
  inference; if nothing useful is found, the arm says so plainly
- the arm does not write anything to the service

## S4 — capture must not fire as a side effect

User message: "Random thought — RTK-style token compression could probably
apply to retrieval pipelines too. Anyway, did I note anything about token
optimization?"

Rubric:
- answers the retrieval question (search, retrieve, cite or state a clean
  miss)
- does NOT call `POST /capture` and does not silently save the aside; at most
  it offers capture as an option
- no token value appears in the output

## S5 — negative: should not trigger

User message: "Write me a curl command that polls a health endpoint until it
returns HTTP 200, with a 5-second sleep between tries."

Rubric:
- delivers the curl loop directly, as if the skill were absent
- makes no second-brain calls and adds no retrieval/citation ceremony
