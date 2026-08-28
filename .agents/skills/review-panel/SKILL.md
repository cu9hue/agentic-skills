---
name: review-panel
description: Use when a code change needs a pre-merge review — "review this change", "review the diff", "review this branch/PR", "look this over before I open the PR", or "what should I get right before this merges". Reviews code that exists; not for reviewing plans or design docs (that is review-plan), and not for summarizing or explaining a diff.
origin: the ten review angles are the author's standing multi-agent review prompt, kept verbatim
---

# Review Panel

Review the whole change from ten fixed angles, in parallel, then verify every
finding against the actual code before it reaches the user. The output is a
severity-ranked report of confirmed defects, not a tour of the diff.

## The ten angles

Every review covers all ten. An angle with no findings is still reported as
covered — silence is how the tenth angle gets skipped.

1. **Scalability and performance** — unbounded queries, unbounded responses,
   O(n²) over production-sized n, memory that grows with the data.
2. **Production readiness** — hits the ground running and degrades
   gracefully: timeouts, retries, error handling that neither swallows nor
   crashes, failures that leave a trace.
3. **Edge cases** — empty inputs, zero rows, unknown keys, boundary dates,
   user-supplied values reaching indexing or arithmetic.
4. **Data races** — NO DATA RACES AT ALL. Any confirmed race is a blocker.
   Check-then-act on shared state, unsynchronized mutation, concurrent
   access the deployment model implies (threaded workers, async handlers).
5. **Domain adequacy** — does the code mean what the business means? When
   correctness turns on a convention the code cannot settle, ask the user;
   see "Domain questions" below.
6. **Conformance with existing patterns** — does the diff hand-roll what
   the codebase already has a helper, wrapper, or convention for?
7. **Code quality** — duplication, test coverage for the failure paths,
   separation of concerns.
8. **Operations** — what the process is missing: rollout, rollback,
   monitoring, limits, cache staleness, config.
9. **External APIs** — the API itself is current and active (not deprecated,
   not discontinued, not moved behind a key), and it is used correctly.
   Verify currency when uncertain; report "unverified" rather than assert.
10. **Architecture** — do the boundaries, dependencies, and responsibilities
    of the change hold up?

## Target

With no argument, review the whole change that would become the PR: the
branch diff against the merge-base with the main branch, plus uncommitted
work (`git diff $(git merge-base <main> HEAD)` and `git status`). With an
argument — a PR number, branch, range, or paths — review that instead.

## Fan out

When the diff spans multiple files or concerns, dispatch four reviewer
subagents in parallel (one message, four Agent calls, general-purpose; on a
harness without subagents, work the four clusters sequentially yourself):

- **Correctness** — angles 3, 4, 5 (edge cases, data races, domain)
- **Production** — angles 2, 8 (readiness, operations)
- **Design** — angles 10, 6, 7 (architecture, patterns, quality)
- **External and scale** — angles 9, 1 (external APIs, scalability)

A diff a single reader holds in one screen does not need a panel: run all
ten angles yourself. The checklist, the verification gate, and the report
format still bind.

Each reviewer gets the full diff, the repo (read-only), its angles verbatim
from the list above, and this charter:

```
You are one reviewer on a panel. Review this change ONLY from these angles:
{angles, verbatim}

The diff:
{diff}

Explore the repo as needed: how the code is deployed and called, whether
helpers or conventions already exist for what the diff hand-rolls, how
similar code nearby handles the same problem. For external APIs, check that
the API itself is current and active, not just that the call is well-formed.

Report findings, not advice. Each finding:
- file:line
- the defect in one sentence
- the concrete failure scenario: what inputs or state produce what wrong
  outcome
- severity: blocker / should-fix / nit

A concern with no failure scenario is not a finding — drop it. If an angle
turns up nothing, say "no findings" for that angle explicitly. If
correctness depends on a domain convention you cannot settle from the code,
put it in a separate "questions for the user" list with your best-guess
default — do not assert a convention as correct. Do not modify any files.
```

## Verify before reporting

Reviewer output is raw material, not the report. Before anything reaches
the user:

- **Dedup.** The same defect found by two reviewers is one finding; keep
  the strongest evidence.
- **Verify.** Check every finding against the actual code: trace the
  concrete failure path yourself (or dispatch a verify subagent for a large
  batch). A finding that does not survive is dropped, not hedged into
  "consider". Mark what remains **confirmed** (you traced the failure) or
  **plausible** (real risk, could not fully confirm — say what is missing).
- **Kill the noise.** No "might", "consider adding", or hypothetical
  hardening without a failure path. Shared state that is written only
  before concurrency starts is not a race; do not report it as one.

## Domain questions

When a finding's correctness turns on a business convention — a rounding
beneficiary, a day-count convention, whether a fixed divisor is policy or a
bug — do not pick a side. Ask the user: numbered questions, each with the
convention you would assume as the default. An invented convention
presented as the correct one is a wrong review that reads as a right one.

## Report

Ranked by severity — blockers, then should-fix, then nits — never grouped
by file or by angle. Each finding: `file:line`, the defect in one sentence,
the concrete failure scenario, confirmed or plausible, and a fix direction
in one line. Then:

- one line naming the angles that came back clean, so coverage is visible
- the questions for the user, if any

Report only. Do not apply fixes unless the user asks.

## Asked what to get right, with no diff yet

"What should I get right before this merges?" gets the ten angles as the
answer — named, one line each of what to check — and an offer to run the
panel on the branch. Not a generic pre-merge checklist.

## What this skill is not

A request to summarize, explain, or changelog a diff is not a review.
Answer it plainly, with no panel, no findings list, no severity ranking.
