---
name: review-plan
description: Use when reviewing an implementation plan, design document, or PR before making code changes - performs structured interactive review of architecture, code quality, tests, and performance
---

# Review Plan

Review a plan or code change thoroughly before making any code changes. For every issue or recommendation, explain the concrete tradeoffs, give an opinionated recommendation, and ask for user input before assuming a direction.

## Engineering Preferences

Use these to guide recommendations:

- **DRY is important** - flag repetition aggressively.
- **Well-tested code is non-negotiable** - rather have too many tests than too few.
- **"Engineered enough"** - not under-engineered (fragile, hacky) and not over-engineered (premature abstraction, unnecessary complexity). Err on the side of handling more edge cases, not fewer; thoughtfulness > speed.
- **Bias toward explicit over clever.**

## Review Sections

### 1. Architecture Review

Evaluate:
- Overall system design and component boundaries.
- Dependency graph and coupling concerns.
- Data flow patterns and potential bottlenecks.
- Scaling characteristics and single points of failure.
- Security architecture (auth, data access, API boundaries).

### 2. Code Quality Review

Evaluate:
- Code organization and module structure.
- DRY violations - be aggressive here.
- Error handling patterns and missing edge cases (call these out explicitly).
- Technical debt hotspots.
- Areas that are over-engineered or under-engineered relative to preferences above.

### 3. Test Review

Evaluate:
- Test coverage gaps (unit, integration, e2e).
- Test quality and assertion strength.
- Missing edge case coverage - be thorough.
- Untested failure modes and error paths.

### 4. Performance Review

Evaluate:
- N+1 queries and database access patterns.
- Memory-usage concerns.
- Caching opportunities.
- Slow or high-complexity code paths.

## For Each Issue Found

For every specific issue (bug, smell, design concern, or risk):

1. Describe the problem concretely, with file and line references.
2. Present 2-3 options, including "do nothing" where that's reasonable.
3. For each option, specify: implementation effort, risk, impact on other code, and maintenance burden.
4. Give your recommended option and why, mapped to the engineering preferences above.
5. Then explicitly ask whether the user agrees or wants to choose a different direction before proceeding.

## Workflow

- Do not assume priorities on timeline or scale.
- After each section, pause and ask for feedback before moving on.

**BEFORE YOU START:** Ask if the user wants one of two options using AskUserQuestion:

1. **BIG CHANGE**: Work through this interactively, one section at a time (Architecture -> Code Quality -> Tests -> Performance) with at most 4 top issues in each section.
2. **SMALL CHANGE**: Work through interactively ONE question per review section.

**FOR EACH STAGE OF REVIEW:** Output the explanation and pros/cons of each stage's questions AND your opinionated recommendation and why, then use AskUserQuestion. NUMBER issues and give LETTERS for options. When using AskUserQuestion make sure each option clearly labels the issue NUMBER and option LETTER so the user doesn't get confused. Make the recommended option always the 1st option.
