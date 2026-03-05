---
name: verify-claims
description: Use when a document, RFC, design doc, or PR contains factual claims about the codebase that need verification - dispatches parallel subagents to check each claim against actual code
---

# Verify Claims

Dispatch subagents to verify factual claims in a document against the actual codebase. Catches stale assumptions, incorrect references, and claims that don't match reality.

## Workflow

1. **Read the document** — identify all verifiable claims (see claim types below)
2. **Group claims** — batch related claims that can be checked together
3. **Dispatch subagents in parallel** — one Agent (subagent_type: "Explore") per claim group
4. **Collect results** — present findings as VERIFIED, INCORRECT, or UNVERIFIABLE

## What Counts as a Verifiable Claim

- "Component X communicates with Y via Z" — check actual call sites
- "This is handled by the FooService" — check if FooService exists and does that
- "The current behavior is..." — check if that's actually what the code does
- "This field is stored in table/struct X" — check the schema/type definition
- "Performance is bounded by..." — check if the bound is plausible given the code
- "There is no existing mechanism for..." — search to confirm absence

## Subagent Prompt Template

For each claim group, dispatch with:

```
Verify these claims against the codebase. For each claim:
1. State the claim
2. Search for the relevant code
3. Verdict: VERIFIED (with evidence), INCORRECT (with what's actually true), or UNVERIFIABLE (explain why)

Claims to verify:
{list of claims with document line references}
```

## Presenting Results

```
| # | Claim | Verdict | Evidence |
|---|-------|---------|----------|
| 1 | "X talks to Y via gRPC" | INCORRECT | X uses HTTP — see file:line |
| 2 | "FooService handles auth" | VERIFIED | FooService.authenticate() at file:line |
```

Flag INCORRECT claims prominently. Ask the user how they want to handle each one.
