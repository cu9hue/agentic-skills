---
name: design-decision-tree
description: Use when a user has an existing implementation plan, spec, or design doc and wants to ensure every decision is explicit before implementation begins — eliminates implicit decisions by systematically walking every ambiguity, assumption, and unstated default in the document.
---

# Design Decision Tree

Take an existing implementation plan, spec, or design doc and relentlessly walk every decision branch until no ambiguity remains. The goal: an implementing agent reading the resulting document makes zero implicit decisions.

This is NOT a quality review (that's `review-plan`). This is about completeness — finding every place where the plan says "use a queue" without saying which one, or assumes a data model without specifying it.

## Workflow

### Phase 1: Analysis & Decision Tree Construction

**Step 1: Get the document**

If invoked with an argument (e.g., the user provides a file path), use it. Otherwise, ask:

```
AskUserQuestion: "Which document should I interrogate? Provide the file path."
```

Read the full document into context.

**Step 2: Dispatch parallel subagents for analysis**

Split the document by top-level headings (or logical topic breaks if headings are absent). Dispatch these subagents in parallel:

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

### Phase 2: Walking the Tree

Process decisions in dependency order — decisions that block others come first.

**For each auto-resolvable decision:**

Present the codebase evidence and proposed resolution:

```
**[{progress}/{ total} resolved] Auto-resolved: {decision}**

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

### Phase 3: Document Rewrite

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
