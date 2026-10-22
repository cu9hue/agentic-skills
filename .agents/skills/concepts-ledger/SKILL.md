---
name: concepts-ledger
description: Use when the user wants a written inventory of the abstractions a codebase is made of — "set up a concepts ledger", "what is this codebase made of", "update the ledger for this branch", or when prepare-pr reaches its ledger gate. Also use when the user asks how to keep understanding a codebase an agent is changing. Not for docstrings, READMEs, architecture diagrams, or explaining one class.
---

# Concepts Ledger

One file, `docs/concepts.md`. One entry per named abstraction the code thinks
in terms of. The user reads it to know what the codebase is made of, and reads
its diff in every PR to see which abstractions the branch added. The ledger is
short and stays short. Anything that is not an entry does not go in it.

The ledger is also a brake. Every new entry in a PR diff is a new abstraction
the user gets to question, so before you add a class to the code, read the
ledger: when an existing entry already does the job, extend that concept
instead. No announcement is needed when you do add one. The diff is the
announcement.

## What earns an entry

A thing earns an entry when it is a named abstraction with its own identity
or behaviour: the code passes it around, extends it, or calls it by name when
describing what happens. The language does not matter. A class, struct, or
enum with its own methods usually qualifies. So does a trait, interface,
protocol, or abstract base the code implements: it and its implementations
are one entry, with the implementations named inside it, unless an
implementation carries behaviour the base does not describe.

A data type with no methods still earns an entry when it is the unit the
other concepts operate on: they take it, return it, store it, and their
entries would name it on a `Depends on` line (`Document` in a pipeline,
`Order` in a shop). This is a rule, not a close call. Apply it and move on;
do not ask the user whether to keep such a type.

No entry for:

- a dataclass, struct, record, tuple, or object type that only bundles
  values to return or pass them between two functions (`StageResult`,
  `IndexStats`, `PopResult`); no other entry would depend on it
- a config or settings holder
- a function, helper, or utility
- a constant, variable, module, or type alias
- a newtype, enum, or error type with no methods of its own

When unsure, leave it out. A missing entry costs one line later. A padded
ledger costs the reader every time.

## The file

```markdown
# Concepts

One entry per named abstraction the code thinks in terms of. Alphabetical.

## <Name>
What: <one sentence — what it is, in the codebase's own terms>
Owns: <what it is responsible for or holds; "nothing" is a valid answer>
Where: `<path>`[, `<path>`]
Depends on: <other entries by name, or —>
```

Rules for the file:

- Entries in one flat list, sorted alphabetically by name. No sections per
  module, layer, or package. No table of contents, no flow overview, no
  "how to read this" block, no "not concepts" list, no open questions.
- Each line of an entry is one line. `What` is one sentence. `Owns` is at
  most two. An entry over five lines is narrating; cut it.
- The entry says what the concept is, not why it exists or how it got here.
  No "introduced to", "replaces", "used to be", "previously".
- Invariants a reader must hold go in `Owns` in a few words (`apply()` must
  not mutate its input). Nothing else explanatory.
- Paths are repo-relative and in backticks.

What you noticed while reading — duplicated logic, a rule the code breaks, a
table nobody creates — goes in the chat reply, in a few lines, and never in
the file.

## Set up

Run when `docs/concepts.md` does not exist.

1. Read the code. Every module, not a sample. List every class, struct,
   enum, trait, interface, and type alias by name.
2. Apply the entry test to each one. Write down what you excluded and the
   rule that excluded it.
3. Write `docs/concepts.md` in the shape above. Nothing else: no README
   section, no CLAUDE.md line, no second file.
4. Reply with the file, the list of names you left out with the rule for
   each, and anything you noticed. Then stop.

## Update

Run when `docs/concepts.md` exists and a branch has changed code.

1. Take the diff against the default branch: `git diff main...HEAD` (three
   dots). Work from the diff, not from memory of the branch.
2. For each class, struct, enum, trait, or interface the diff adds: apply
   the entry test. Add an entry for each that passes, in alphabetical
   position.
3. For each the diff removes: delete its entry. Remove its name from every
   `Depends on` line.
4. For each the diff renames or moves: rewrite the entry under the new name
   at the new path. Never keep both. Fix every `Depends on` and `Where` line
   that named the old name or old path.
5. For each the diff changes in meaning (new responsibility, a dropped
   invariant): rewrite `What` or `Owns`. A method added or a bug fixed is not
   a change in meaning.
6. Leave every other entry byte-for-byte as it was. The PR diff of this file
   is what the user reviews; noise in it hides the one line that matters.
7. Reply with the changed entries, the names you left out with the rule for
   each, and anything you noticed. Then stop.

If the diff adds no abstraction and removes none, say so in one line and
change nothing.

## Not this skill

A request to document one class, write a README, draw the architecture, or
explain how a module works is not a request for the ledger. Do that one thing.
Do not create `docs/concepts.md` on the side, and do not add trailing advice
about tracking concepts.

## Quality gate

- `docs/concepts.md` is the only file written
- every entry has exactly `What`, `Owns`, `Where`, `Depends on`
- entries are alphabetical, in one flat list, with no extra sections
- no entry for a return bundle, config holder, function, or constant
- no entry explains why or tells history
- on update: untouched entries are unchanged in the diff, renamed concepts
  appear once, and no `Depends on` line names a deleted concept
- observations are in the reply, not the file
