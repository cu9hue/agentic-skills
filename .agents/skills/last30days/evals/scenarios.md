# last30days — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
skill loaded), identical prompts otherwise. Both arms run live in this
user's environment: the `social` MCP (X, Reddit, LinkedIn), Exa, WebSearch,
Bash with `curl` and the `treg` CLI. The skill arm reads SKILL.md and its
references first. Each subagent writes exactly its reply to the user into
`evals/<arm>/S<n>.md` and returns a short log of the calls it made and what
it spent. Anonymize outputs into teams, blind-judge against the rubrics, log
the verdict in `results.md`.

Results are live, so the two arms see slightly different data. Judge the
method and the honesty of the report, not which arm found the bigger story.

The window is the 30 days before the run date. A judge spot-checks dates by
opening at least three cited links per output.

## S1 — named topic with a collision-prone name

User message: "last30days Cursor"

Rubric:
- Every cited item is about Cursor the AI code editor. No item about mouse
  cursors, database cursors or pagination.
- Every cited item spot-checked is dated inside the window.
- Evidence comes from at least four distinct sources, and at least three of
  them are community sources (X, Reddit, Hacker News, YouTube, TikTok),
  not articles.
- Each story leads with what people said, cited to a handle, subreddit or
  thread, with web articles used only for facts the community sources lack.
- At least two community quotes are verbatim, attributed and linked.
- Sources that failed or were skipped are named as gaps. The report never
  calls a failed source quiet.
- Paid calls, if any, are reported with the amount spent.
- If the `social` MCP is unavailable during the run, X evidence still
  appears through a fallback, and Coverage names the route. (Added
  2026-11-27; applies only to runs where the MCP is down.)

## S2 — comparison

User message: "Granola vs Otter vs Fireflies — what are people saying this
month?"

Rubric:
- Each of the three products gets its own sentiment, strengths and
  weaknesses, each point cited to a dated community source.
- A head-to-head view compares the three on the same dimensions.
- A "choose X if" line per product, grounded in cited evidence.
- No strength or weakness comes from prior knowledge without a source in
  the window. Where a product has thin evidence, the report says so.
- Every cited item spot-checked is dated inside the window.

## S3 — trending in a domain

User message: "What's trending in AI agents right now?"

Rubric:
- The run sweeps what is hot first (HN front page or top stories, top X
  posts, top Reddit posts in the window) instead of searching one keyword
  and reporting whatever comes back.
- Topics are named specifically (proper nouns first), not as themes like
  "agent frameworks are evolving".
- Each reported topic carries evidence from at least two sources, or is
  marked single-source.
- Help-me posts, promo and personal musings are dropped.
- Each topic has a content angle: why it matters or a hook for a post.

## S4 — structural probe: underspecified ask

User message: "I'm giving a talk on vibe coding next week and want to know
what the vibe actually is out there right now. What should I get right?"

Rubric:
- Puts a fixed recency window on the agenda, with dates checked rather
  than assumed.
- Puts community sources (X, Reddit, HN, YouTube or TikTok) ahead of
  articles, and names engagement as the way to pick evidence.
- Puts verbatim, linked quotes and cross-source confirmation on the agenda.
- Puts coverage gaps on the agenda: say which sources failed instead of
  calling them quiet.
- These concerns organize the answer, or the answer runs the research and
  shows them. They are not one bullet among many.

## S5 — negative: research with no recency angle

User message: "Give me a short explainer on where the Unix philosophy came
from."

Rubric:
- Answers directly: a short, accurate explainer.
- No social-media sweep, no treg spend, no 30-day framing, no
  last30days report structure.
