# last30days — eval results

Append-only. Newest at the bottom.

## 2026-11-26 — initial A/B (branch outreach-campaign-email-order, base 9a4eea4)

Arms: A = no skill, B = skill. n=1 per cell: a signal, not proof.

Setup: both arms ran live in this environment with the `social` MCP, Exa,
WebSearch, Bash, `curl` and the `treg` CLI. The skill arm read SKILL.md and
`references/sources.md` first. Outputs are in `baseline/` and `skill-arm/`.
The S3 prompts in both arms add "read-only, keep treg spend under $0.10",
because the permission classifier refused the first S3 baseline launch
without it. One blind judge, team labels shuffled per scenario. The judge
decoded every cited X status id and fetched every cited HN item. Reddit
links could not be fetched by any method, so they counted neither way.

RED (baseline, before drafting): no arm used treg, so Reddit came only
through digests and third-party tallies after `social` Reddit search
failed (patchright has no Chrome), and YouTube and TikTok were never read.
S1 partial: strong facts, but a changelog-and-press structure, quotes not
tied to handles, an Oct 20 launch under "what shipped". S2 fail on
sourcing: product strengths from listicles and tallies, quotes unlinked.
S3 partial: built from aggregator newsletters, no hot-list sweep, no
content angles, single-source items unmarked. S4 partial: ran research
but no fixed window, articles and digests instead of community links,
gaps in one footnote. S5 pass.

GREEN, round 1 (skill v1):

- S1: **B** (6/1/0 vs 2/3/2) — r/cursor, X, HN and YouTube lead the stories, quotes verbatim and linked, every gap named, $0.013 spent. Partial: two stories led with facts before the community.
- S2: **B** (5/0/0 vs 1/2/2) — every product point cites a dated Reddit, HN or X post and thin evidence is flagged. Baseline rested on MetaWhisp and GTM Ranked tallies and misattributed one X post.
- S3: **B** (4/1/0 vs 1/3/1) — swept top-of-month Reddit, about 85 HN stories and X first; each topic has 2+ sources and two hooks. Partial: one topic rested on one person's experiment.
- S4: **B** (5/0/0 vs 0/3/2) — fixed window, community sources picked by engagement, six linked quotes, Coverage and Gaps lines. Baseline gave talk advice built from articles.
- S5: **tie** (2/0/0 each) — both answered directly; the skill arm routed to "not this skill" and spent nothing.

Fixes from the round-1 runs (reference): the Reddit comments call moved
from `crawl4ai.reddit.post.comments` (0 rows on every thread) to
`scrapecreators.x.v1-reddit-post-comments`; the captions parameter is
`video`; X thread reads are filtered by `inReplyTo`; the start balance
greps the `Balance` line; spend is the run's charge-log sum, because the
team balance is shared.

Fixes from the verdict (skill v2): the first sentence after each headline
is what people said; one person's experiment is junk in trending; sweep
phrases must not collide ("ai agents", never bare "agent").

GREEN, round 2 (skill v2, S1 and S3 only; fresh judge, labels reshuffled;
round-1 outputs kept as `skill-arm/S1-round1.md` and `S3-round1.md`):

- S1: **B** (6/1/0 vs 1/5/1) — 4 of 6 stories now open with what people said; two open with an engagement ranking ("most-liked Cursor post"), still partial. 13 X and HN links decoded, all in window, quotes verbatim.
- S3: **B** (4/1/0 vs 0/4/1) — sweep by engagement across HN, Reddit and X; the one-person claim is marked single-source and the topic stands on other sources. Partial: headings are claims, not proper nouns first.

Spend per skill-arm run: $0.013–0.024 on treg, all under the $0.10 cap.

Judge verdict: the skill arm wins S1–S4 in both rounds and ties the
negative (S5) with no over-trigger. Obsolescence: no. The baseline fails
the structural probe (S4) at 0/3/2: it never read a community source
directly, and without treg it could not reach Reddit, YouTube or TikTok.
Open: topic headings in trending mode still drift toward themes.

## 2026-11-27 — regression: treg X fallback, "10 cents" fix (uncommitted, base 9a4eea4)

Edit: SKILL.md falls back to treg X search when the `social` MCP is down
and writes the cap as "10 cents" (the skill loader replaced `$0` with the
first argument, so "$0.10" rendered as "AI.10"). sources.md adds the treg X
call, the YouTube comments call (`video_id`) and an RTK note. S1 gained a
rubric bullet for the fallback.

Arms: pre = skill v2, post = this edit. S1 only, n=1, run while the
`social` MCP was not connected. One blind judge, labels shuffled. Outputs
in `regression-2026-11-27/pre/` and `post/`.

- S1: **pre** (7/1/0 vs 6/2/0). Both pass the new fallback bullet: the pre
  arm found treg X search in the catalog by itself (two extra lookups) and
  also read replies with `conversation_id:`. The only difference is bullet
  2: the post arm linked two pre-window sources (x.ai Oct 12, TechCrunch
  Aug 15), each stated as dated background, which SKILL.md allows but the
  rubric does not. Both 12 X ids and all HN items checked are in the
  window. Spend: pre $0.021, post $0.020.

Found during the run: `conversation_id:<id>` on treg X search returns
replies (tested on the routed call); sources.md now says so instead of
"cannot read replies".

Verdict: the edit does not change the outcome on its target, since the
base model found the fallback anyway; it saves the catalog search. The
post arm lost by one partial on a bullet the edit did not touch. Open: the
rubric and SKILL.md disagree on linked background facts.

## 2026-11-27 — made user-invoked

`disable-model-invocation: true` (Codex: `allow_implicit_invocation: false`). The skill now runs only when the user types its command, to cut always-loaded context. Its instructions are unchanged, so nothing was rerun. Scenarios that relied on the skill firing on its own, such as the structural probe, now assume the user typed the command.
