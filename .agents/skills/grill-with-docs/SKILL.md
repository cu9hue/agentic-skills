---
name: grill-with-docs
description: A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. Hand it a task paragraph or a number ("3 questions") for one capped round instead.
disable-model-invocation: true
origin: "Built on mattpocock/skills (MIT, https://github.com/mattpocock/skills) grill-with-docs at commit bbadaa6, with his grilling and domain-modeling folded in. The capped round comes from this repo's former design-decision-tree skill, itself adapted from Matt's grilling. This repo's eval mandate applies."
---

Pick the mode from the input:

| Input | Mode |
|---|---|
| A task paragraph, a ticket or an idea, even with "grill me"; or a number ("give me 3 questions") | **Capped round**: one message, at most N questions, ranked |
| A plan, spec or design to work through, or a request to go all the way down | **Full grilling**: rounds until the frontier is empty |
| A small change with one obvious reading (add a flag, rename, fix a typo) | **No grilling**: say there is nothing worth a round, state the one assumption you will make, and offer to make the change. Ask one question only if the change cannot be done without its answer |

Judge "small" by what an implementer would have to guess, not by how the
user phrased it: a one-line request can hide a scope decision, and then it
gets a capped round. When the input fits no row, ask which mode the user
wants. Both modes
use **Domain modeling** below: when an answer settles a term or a
hard-to-reverse decision, write it down as that section says.

## Capped round

Task text in. One round of at most N numbered questions out, each carrying the
answer you would pick.

Your job is to remove ambiguity, not to survey it. Under a cap you cannot ask
everything, so every slot goes to the question whose answer removes the most.

N is the user's attention budget. Six unless they name a number; "cap at 3"
means 3. Never exceed it, and never pad to reach it.

### Settle what you can before you ask anything

Finding facts is your job, never the user's. Resolve what the evidence
resolves — the task text, the conversation, and the codebase. Dispatch Agent
(subagent_type: "Explore") calls for the components, schemas, conventions, and
dependencies the task touches.

Every fact kills a question. A question the repo answers is not ambiguity, it
is homework you skipped. A question the user answered two messages ago is
worse.

### Map the tree

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

### Rank by ambiguity removed

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

### Ask only the frontier

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

### Write the round

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

### After the answers

Apply them. The defaults the user let stand are decisions now, not guesses, so
write them down where the work lives.

Then recompute the frontier once. Settled answers push it outward, and a node
that was blocked may now be askable and genuinely uncertain. When such a node
blocks the work, say so in one line and ask for another round. Otherwise stop.
Never manufacture a second round to look thorough.

## Full grilling

Interview the user relentlessly until you reach a shared understanding. Map this as a **design tree**: every decision branches into the decisions that hang off it.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the whole frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Word each question so "yes" accepts your recommended answer.

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Finding _facts_ is your job, never the user's. When a frontier question needs a fact from the environment (filesystem, tools, etc.), dispatch a sub-agent with a fresh context window to find it; don't ask the user for anything you could look up yourself. Don't block on it: a running exploration is an unsettled prerequisite, so only the questions downstream of it wait for the sub-agent to report; ask the rest of the frontier now. The _decisions_ are the user's: put each to them and wait.

The session is done when the frontier is empty: every branch of the design tree visited, nothing left silently assumed. Do not act on it until the user confirms you have reached a shared understanding.

## Domain modeling

Actively build and sharpen the project's domain model as you design. This is the *active* discipline: challenging terms, inventing edge-case scenarios, and writing the glossary and decisions down the moment they crystallise. (Merely *reading* `GLOSSARY.md` for vocabulary is not this skill: that's a one-line habit any skill can do. This skill is for when you're changing the model, not just consuming it.)

### File structure

Most repos have a single context:

```
/
├── GLOSSARY.md
├── docs/
│   └── adr/
│       ├── 0001-event-sourced-orders.md
│       └── 0002-postgres-for-write-model.md
└── src/
```

If a `GLOSSARY-MAP.md` exists at the root, the repo has multiple contexts. The map points to where each one lives:

```
/
├── GLOSSARY-MAP.md
├── docs/
│   └── adr/                          ← system-wide decisions
├── src/
│   ├── ordering/
│   │   ├── GLOSSARY.md
│   │   └── docs/adr/                 ← context-specific decisions
│   └── billing/
│       ├── GLOSSARY.md
│       └── docs/adr/
```

Create files lazily: only when you have something to write. If no `GLOSSARY.md` exists, create one when the first term is resolved. If no `docs/adr/` exists, create it when the first ADR is needed.

### During the session

#### Challenge against the glossary

When the user uses a term that conflicts with the existing language in `GLOSSARY.md`, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"

#### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account': do you mean the Customer or the User? Those are different things."

#### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

#### Cross-reference with code

When the user states how something works, check whether the code agrees. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?"

#### Update GLOSSARY.md inline

When a term is resolved, update `GLOSSARY.md` right there. Don't batch these up: capture them as they happen. Use the format in [GLOSSARY-FORMAT.md](references/GLOSSARY-FORMAT.md).

`GLOSSARY.md` should be totally devoid of implementation details. Do not treat `GLOSSARY.md` as a spec, a scratch pad, or a repository for implementation decisions. It is a glossary and nothing else.

#### Offer ADRs sparingly

Only offer to create an ADR when all three are true:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip the ADR. Use the format in [ADR-FORMAT.md](references/ADR-FORMAT.md).
