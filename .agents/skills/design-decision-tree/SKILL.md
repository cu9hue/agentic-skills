---
name: design-decision-tree
description: Use when a plan, spec, design doc, or a paragraph describing a task needs its open decisions surfaced before anyone builds — triggers like "what am I not deciding?", "grill me on this", "what should I get right here?". Either a capped round of the questions that remove the most ambiguity, or an exhaustive walk until nothing is left silently assumed. Not a quality review of the plan (that is review-plan).
origin: capped triage adapted from Matt Pocock's `grilling` skill (github.com/mattpocock/skills, skills/productivity/grilling) — relentless ambiguity reduction, the design-tree and frontier framing, one round of numbered questions each carrying a recommended answer, and "finding facts is your job, never the user's"
---

# Design Decision Tree

Drive the ambiguity out relentlessly. Map the work as a design tree — every
decision branches into the decisions hanging off it — and keep working the tree
until nothing is left silently assumed.

This is not a quality review. `review-plan` judges whether the plan is good;
this skill only asks whether it is *decided*. It hunts every place the text
says "use a queue" without saying which one, or assumes a data model without
writing it down.

## Two paths

| Input | Path | Output |
|---|---|---|
| A document — spec, plan, design doc, file path | Full walk | Every decision resolved, document rewritten |
| Task text — a paragraph, a ticket, an idea, "I want to build X" | Capped triage | At most 6 questions, ranked by ambiguity removed, each with a default |

Ambiguous input? Ask which the user wants. An explicit cap ("give me 3
questions") always means capped triage.

---

# Path A — capped triage

Task text in. One round of at most N numbered questions out, each carrying the
answer you would pick.

Your job is to remove ambiguity, not to survey it. Under a cap you cannot ask
everything, so every slot goes to the question whose answer removes the most.

N is the user's attention budget. Six unless they name a number; "cap at 3"
means 3. Never exceed it, and never pad to reach it.

## Settle what you can before you ask anything

Finding facts is your job, never the user's. Resolve what the evidence
resolves — the task text, the conversation, and the codebase. Dispatch Agent
(subagent_type: "Explore") calls for the components, schemas, conventions, and
dependencies the task touches.

Every fact kills a question. A question the repo answers is not ambiguity, it
is homework you skipped. A question the user answered two messages ago is
worse.

## Map the tree

Wide first, no cap yet. Every decision branches into the decisions hanging off
it, so list every point where an implementer would guess:

- Ambiguous requirements — "use a cache": which one, where, what eviction?
- Unstated assumptions — "the API returns JSON": does it? is that documented?
- Implicit defaults — "handle errors": retry, fail fast, or log and continue?
- Missing details — "store it in the database": which table, what schema?
- Unresolved trade-offs — "optimize for speed": at what cost?
- Dependency gaps — "after the auth check": which one, returning what?
- Scope edges — what is explicitly out, and does the user know it is out?

Then mark which nodes hang off which. You rank on the edges, so draw them.

## Rank by ambiguity removed

Ambiguity removed is span times uncertainty. Score both, every time.

**Span** is how much stays undetermined until the node is answered, counting
the nodes downstream that cannot be asked until it is. Widest: whether a thing
gets built at all — scope, what the demo shows. Wide: the structure — data
model, boundaries, sync or async, where state lives, what is the source of
truth. Narrow: a contract — API shape, schema fields, event names. Narrowest:
one implementation behind an interface — library, algorithm, naming.

**Uncertainty** is how far apart the plausible answers are, and how well you
can predict which one this user takes. Two answers that build the same system
carry none. A question you can answer from the task text, the repo, or what
you already know of this user carries none either.

Score both terms or you fill the round with questions nobody needed asked. A
widest-span node with a predictable answer is not a question. It is a default
you have not written down yet — put it below the line and spend the slot on
something you cannot call.

Break ties only between nodes that already clear both terms: a node that
unblocks other nodes beats a leaf, and a decision that is expensive to reverse
beats one you can change on Friday. Irreversibility never buys a slot for a
predictable answer — a contract you will write the standard way is a default,
however permanent it is.

Never spend a slot on a narrowest-span node. A library pick in your top six
means you stopped mapping too early.

Treat "how will you know the output is right" as widest span whenever the thing
being built produces a judgment — a ranking, a clustering, a classification, a
summary. It decides what you build to check it, and it is the one people file
as a testing detail.

When the deliverable is a demo, span gains two axes: what the audience sees,
and whether the thing is finished in time.

## Ask only the frontier

The frontier is every node whose prerequisites are settled — the questions you
can ask now without guessing at answers you have not heard. A question that
depends on another question in this same round is not ready. Drop it, promote
the next candidate, and let the dependent one wait.

This binds the defaults too. When a default has to name another question in the
round to make sense, either the two nodes are one node or the wrong one is
above the line.

Every default stands on its own. Never reference another question by number,
and never let a default rest on a neighbour's answer — name the assumption
inside the default instead, so overriding the neighbour does not silently
invalidate it. A default that branches is not a default: pick one side and put
the condition in the cost line.

## Write the round

Give every question a default. A question without one is a question you have
not finished thinking about, so think, then write it.

A default is the concrete thing you will do if the user says nothing: "Postgres
table `events`, one row per event, no partitioning", not "pick a suitable
store". Restating the question as a preference is not a default.

Say so in the cost line when a default assumes a stack, a service, or a
capability you have not confirmed the repo has — Postgres, Redis, a
request-scoped actor id, a job runner. A default resting on infrastructure that
may not exist is a guess wearing a decision's clothes.

Defaults compose. Read them together before you send, and ask whether the
combination still describes the thing the user said they were building. Two
defensible defaults can relocate the project — a batch job over an exported
file is not a tool that watches a channel. When they do, that drift is itself a
decision. Give it a slot.

Read the set for coherence too. It has to be one somebody would pick on
purpose: a debugging-grade audit log that can fail a billing write is two
defaults nobody chooses together. Fix the set before you send it.

Ask all N at once. Never drip them one per turn. Order them strictly, most
ambiguity removed first, and open with one line naming what you ranked on.
Build order is not rank; if you catch yourself calling a later question the
one that really matters, it belongs at the top.

```
❓ **Q1 — {short title}**

{The choice, in a sentence or two. Name the alternatives when the choice is
between named options.}

➡️ **Default:** {the concrete thing you will do} — {what it costs if this is
the wrong call}

---

❓ **Q2 — {short title}**

...
```

Then every node that did not get a slot, in one block:

```
Below the line, assumed: {decision} → {default}. {decision} → {default}.
```

Drop nothing silently. A cap that hides decisions rebuilds the implicit
defaults this skill exists to remove: the cap limits what you ask, never what
you decide.

Close with the answering contract, verbatim:

```
Answer any subset. Anything you skip, I take the default. "go" = all defaults.
```

## After the answers

Apply them. The defaults the user let stand are decisions now, not guesses, so
write them down where the work lives.

Then recompute the frontier once. Settled answers push it outward, and a node
that was blocked may now be askable and genuinely uncertain. When such a node
blocks the work, say so in one line and ask for another round. Otherwise stop.
Never manufacture a second round to look thorough.

---

# Path B — full walk

## Phase 1: Analysis & decision tree construction

**Step 1: Get the document**

If invoked with an argument (e.g., the user provides a file path), use it.
Otherwise, ask:

```
AskUserQuestion: "Which document should I interrogate? Provide the file path."
```

Read the full document into context.

**Step 2: Dispatch parallel subagents for analysis**

Split the document by top-level headings (or logical topic breaks if headings
are absent). Dispatch these subagents in parallel:

**Section analysis agents** — one per section, Agent (subagent_type: "general-purpose"):

```
You are analyzing a section of an implementation plan to find every implicit decision.

Your job: identify every place where an implementing agent would have to guess, assume, or make a judgment call. This includes:

- Ambiguous requirements ("use a cache" — what kind? where? what eviction policy?)
- Unstated assumptions ("the API returns JSON" — does it? is that documented?)
- Implicit defaults ("handle errors" — how? retry? fail fast? log and continue?)
- Missing details ("store in the database" — which table? what schema? what indexes?)
- Unresolved trade-offs ("optimize for speed" — at what cost? memory? complexity?)
- Dependency gaps ("after the auth check" — which auth check? what does it return?)

For each decision point found, output:
1. **What**: The specific ambiguity or implicit decision
2. **Where**: Quote the relevant text from the plan
3. **Depends on**: List any other decisions that must be resolved first (use the "What" text to reference them). If none, say "independent"
4. **Codebase might answer**: Yes/No — whether exploring the existing codebase could resolve this

## Section to analyze:

{section_content}
```

**Codebase exploration agents** — dispatch Agent (subagent_type: "Explore") calls to investigate areas of the codebase referenced or implied by the plan:

```
Explore the codebase to find evidence relevant to this implementation plan. Look for:

1. Existing implementations of things the plan describes building
2. Patterns, conventions, or frameworks already in use that constrain choices
3. Configuration, schemas, or infrastructure that the plan references or assumes
4. Anything that answers questions the plan leaves open

Focus areas from the plan:
{list of technologies, components, and systems mentioned in the plan}

For each finding, report:
- What you found (with file:line references)
- What decision or ambiguity in the plan it relates to
- Whether it definitively answers the question or just constrains the options
```

**Step 3: Build the decision tree**

Collect results from all subagents. Build a unified decision tree:
- **Nodes** are open decisions
- **Edges** are dependencies (decision B requires decision A first)
- Decisions the codebase clearly answers are marked **auto-resolvable**

**Step 4: Present the tree summary**

Show the user the scope before diving in:

```
Found {N} open decisions across {M} branches:
- {Branch name} ({X} decisions, {Y} auto-resolvable)
- {Branch name} ({X} decisions, {Y} auto-resolvable)
- ...

Starting with: {first branch} (blocks {dependent branches})
```

## Phase 2: Walking the tree

Process decisions in dependency order — decisions that block others come first.

**For each auto-resolvable decision:**

Present the codebase evidence and proposed resolution:

```
**[{progress}/{total} resolved] Auto-resolved: {decision}**

The codebase answers this: {evidence with file:line references}

Proposed resolution: {what the plan should say}

Confirm or override?
```

Wait for user confirmation. If overridden, record the user's choice instead.

**For each open decision:**

First, dispatch an Agent (subagent_type: "Explore") to check if the codebase has relevant evidence that could inform the decision. Then present:

```
**[{progress}/{total} resolved] Decision: {decision}**

From the plan:
> {relevant excerpt}

This needs to be decided because: {why it's ambiguous — what could go wrong if an implementer guesses}

{If codebase evidence was found: "Codebase context: {findings}"}

Options:
(a) {option} — {trade-off}
(b) {option} — {trade-off}
(c) {option} — {trade-off}

Recommended: ({letter}) — {reasoning}
```

Wait for the user's choice.

**After each resolution:**

1. Record the decision.
2. **Contradiction check**: Compare against all prior decisions. If a new answer contradicts a prior decision or something stated in the plan, STOP. Present the contradiction clearly:
   ```
   Contradiction detected:
   - Decision {X}: {what was decided}
   - Decision {Y}: {what was just decided}
   - These conflict because: {explanation}

   How do you want to resolve this?
   ```
   Do not continue until the contradiction is resolved.
3. **Tree expansion**: Check whether the resolution reveals new sub-decisions that weren't visible before. If so, add them to the tree and inform the user:
   ```
   Choosing {option} opened {N} new decisions about {topic}. Updated scope: {new total} decisions remaining.
   ```

## Phase 3: Document rewrite

Once every node in the decision tree is resolved:

**Step 1: Dispatch the rewriter**

Launch an Agent (subagent_type: "general-purpose"):

```
You are rewriting an implementation plan to incorporate all decisions that were made during an interrogation process.

## Original plan:

{full original document}

## Resolved decisions:

{numbered list of every decision: what was decided, why, and any codebase evidence}

## Your task:

Rewrite this plan so that an implementing agent can execute it without making a single implicit decision. Guidelines:

1. **Restructure freely** — organize around the resolved decisions. Do not preserve the original structure if a better organization exists.
2. **Be explicit everywhere** — every technology choice, every schema detail, every error handling strategy, every trade-off resolution must be stated.
3. **Include the reasoning** — for non-obvious decisions, briefly note why this choice was made (one sentence).
4. **Preserve intent** — the author's goals and voice should survive, but clarity always wins over style.
5. **No ambiguity** — if you find yourself writing "as appropriate" or "as needed", replace it with the specific decision that was made.

Output the complete rewritten document.
```

**Step 2: Present for review**

Show the rewritten document to the user. Do NOT write it to disk yet.

```
Here is the rewritten plan with all {N} decisions resolved. Review it and let me know if you want any changes.

{rewritten document}
```

**Step 3: Revise if needed**

If the user requests changes, revise and re-present. Repeat until approved.

**Step 4: Write to disk**

Once approved, overwrite the original file with the rewritten document. Do NOT commit to git.
