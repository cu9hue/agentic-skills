# market-selection — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B = skill
loaded), identical prompts otherwise. Both arms: no web tools, no Skill tool,
no other local files; claims that would need a source are marked as such.
Anonymize outputs into teams, blind-judge against the rubrics, log the verdict
in `results.md`.

The previous scenario set (2026-10-08) tested a criteria-checklist version of
this skill and is archived in `archive/`. This set tests the direction-finding
rewrite, written after a discovery batch on 2026-10-20 screened 22 candidates
down to 3 with no buyer ever contacted.

## Shared material

**Founder profile F** (used by S2 and S4):

> Solo founder. About 6 years in quant finance: built a high-frequency trading
> engine, worked on power trading and auctions, led quant engineering for risk
> at a crypto exchange (real-time margin limits across many accounts,
> deterministic replay of every market event for audits). Has built production
> AI agent harnesses. Edge in their own words: "I can decide in real time
> whether an actor may take an action with money at stake, and prove
> afterwards exactly why."

## S1 — structural probe: underspecified ask

User message: "I'm between ideas and want to figure out what to explore next.
Where should I look?"

Rubric:
- Establishes the target outcome early: venture scale or a bootstrappable
  business (asked, or stated as an explicit assumption the user can correct),
  and lets that choice change the advice.
- Points at directions grounded in trends or shifts (something more true this
  year than last), not a list of generic startup-advice categories.
- Asks for, or uses, the founder's edge as an input to where to look.
- Does NOT open by asking for a batch of ideas to screen, or deliver a
  kill/survive checklist.

## S2 — the kill-everything failure: solo bootstrapper wants directions

User message: "[Profile F.] I'm going solo and bootstrapping, for good. I want
to build something net positive with my edge, and I prefer B2B. Help me pick up
signals and patterns to figure out what to explore next."

Rubric:
- Uses a bootstrap bar (a profitable business one person can run), not a
  $1bn ARR or venture bar, and says so.
- Produces 3–6 **directions**, each a shift or trend plus a buyer it creates
  pain for, rather than 12+ narrow product candidates.
- Names at least one **pattern** that cuts across several signals or
  directions (the same underlying need appearing in different industries).
- Each direction ends in a stated belief and a cheap real-world test with a
  pass threshold and a time box (e.g. N messages, M replies, by a date), not a
  desk screen.
- Respects the stated constraints (solo, B2B, net positive) and connects at
  least two directions to the edge in profile F specifically, not to generic
  "AI for finance".
- Does NOT kill most of what it generates, and does NOT end with zero or one
  surviving option.
- States the geography it assumed (the prompt names none) beside the bar,
  and lists geography first among the questions that would sharpen the map.

## S3 — venture path with a ceiling

User message: "My co-founder and I are raising a pre-seed next year. We want
venture-scale directions in infrastructure for AI agents that move money.
What should we be exploring?"

Rubric:
- Uses a venture bar and asks for, or states, the ceiling it will hold
  directions to (e.g. $1bn ARR, a $1bn exit, or the founders' own number).
- Produces directions tied to dated shifts (rules, capabilities, price
  collapses), each with who would pay and why that pool can grow large.
- Recommends a full market evaluation for the one or two directions worth it,
  passing the chosen ceiling along, rather than scoring every direction on
  nine axes itself.
- Each direction carries a test the founders can run before the evaluation.

## S4 — over-constraint: everything is already dead

User message: "[Profile F.] I've already killed these: agent spend caps
(LiteLLM does it free), SOC 2 evidence tooling (people replace Vanta with
Sheets and Claude), 3PL invoice audits (SpendVerify is $99/mo), chargeback
apps (Chargeflow owns it), utility bill audits (needs a tariff database),
power settlement shadowing (insiders sell it). Nothing survives. What now?"

Rubric:
- Reads the kills as evidence and extracts at least one pattern from them
  (what the dead ideas share), instead of only re-litigating each kill.
- Widens at least one dead idea by asking who else feels the same pain or
  which other buyer has the budget, producing a direction the kill did not
  cover.
- Names the over-constraint itself (screening without contacting buyers) and
  moves the founder to commit to one belief and test it, with a threshold.
- Does NOT produce a fresh batch of candidates to screen the same way.

## S5 — negative: one named market to evaluate

User message: "Is US battery storage settlement software a good market? Score
it for me."

Rubric:
- Treats this as an evaluation of one named market (scores or judges it, or
  hands it to a market evaluation), not as a request to find new directions.
- Does NOT produce a list of alternative directions or trends to explore
  instead. At most one line suggesting adjacent directions is acceptable.

## S6 — research tool choice (web tools on)

Unlike S1–S5, both arms have web tools, including the Exa MCP tools
(`mcp__plugin_exa_exa__web_search_exa`, `mcp__plugin_exa_exa__web_fetch_exa`)
and WebSearch. The runner records which search tools each arm called.

User message: "Bootstrap, solo, B2B. Find me 3 dated shifts from 2025–2026
that create a budget for real-time payment controls at small UK payment
firms, with sources."

Rubric:
- Searches with the Exa MCP tools; makes no WebSearch call.
- Opens the page behind each cited date or number (an Exa fetch, or an
  equivalent page read) rather than citing a search snippet.
- Each shift carries a date and a link to the page that states it.

## S7 — geography from the brief

User message: "[Profile F.] Solo, bootstrapping, B2B, net positive. US only —
I'm not interested in UK or EU markets. What should I explore next?"

Rubric:
- States the geography (US) at the top beside the bar.
- Every shift, buyer and test is US; no direction ranks a UK or EU market.
  At most one direction outside the US, explicitly marked as an exception
  with a reason, and never in the UK or EU.
- Still meets the S2 structure: directions on dated shifts, a pattern, and a
  test with a threshold and time box per direction.

## S8 — the founder's vault is available

Both arms have `SECOND_BRAIN_URL` and `SECOND_BRAIN_READER_TOKEN` set (the
founder's curated vault, see `second-brain-retrieval`), Bash, and at most 6
Exa calls. Neither arm may read vault files from disk.

User message: "[Profile F.] Solo, bootstrapping, B2B, US. What should I
explore next?"

Rubric:
- Queries the vault before ranking, with short queries that return results.
- At least one shift comes from a vault source note, cited with note path
  and chunk ID, and still carries a date.
- Uses at least one vault concept claim or open contradiction as a lens or a
  named risk on a direction.
- Still meets the S2 structure: bar and geography at the top, directions on
  dated shifts, a pattern, a test with a threshold and time box.
