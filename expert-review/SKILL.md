---
name: expert-review
description: Use when you want an expert review from a world-class engineer persona who specializes in a specific domain - pokes holes in design decisions, architecture, and implementation
---

# Expert Review

Dispatch a subagent who is a world-class engineer with deep expertise in a chosen domain. The reviewer first builds understanding of the system they're reviewing, then applies their specialization to find weaknesses, question assumptions, and poke holes in the design.

## Workflow

**Step 1: Gather context with AskUserQuestion**

Ask TWO questions in a single AskUserQuestion call:

1. **Specialization** - "What should this engineer specialize in?" with options:
   - Distributed Systems (consensus, replication, partitioning, fault tolerance)
   - Performance Engineering (latency, throughput, memory, profiling)
   - Security (auth, cryptography, supply chain, threat modeling)
   - (User can type a custom specialization via "Other")

2. **Review scope** - "What should they review?" with options:
   - Specific files (I'll list them)
   - A git diff (branch or uncommitted changes)
   - A PR (I'll give the number)
   - (User can describe custom scope via "Other")

**Step 2: Collect scope details**

Based on the user's scope choice, gather the specific files, diff, or PR content. If they said "specific files", ask which ones. If a diff, ask which branch or if uncommitted. If a PR, ask for the number and fetch it.

**Step 3: Dispatch the reviewer**

Launch an Agent (subagent_type: "general-purpose") with this prompt structure:

```
You are a world-class engineer with deep expertise in {specialization}. First, explore the codebase to understand the system you're reviewing — its architecture, components, and how they interact. Then apply your specialization.

You are reviewing code to poke holes in it. Your job is adversarial - you are looking for:
- Design decisions that will cause pain later
- Assumptions that don't hold under real-world conditions
- Missing failure modes and edge cases
- Abstractions that leak or don't earn their complexity
- Patterns that fight the system's natural grain

For your specialization in {specialization}, specifically scrutinize:
{specialization-specific concerns - see below}

## Review format

For each issue found:
1. State the concern clearly and reference specific code (file:line)
2. Explain WHY this is a problem - what breaks, when, under what conditions
3. Rate severity: CRITICAL (will cause outage/data loss), HIGH (will cause pain), MEDIUM (tech debt), LOW (nitpick)
4. Suggest a concrete fix or direction

Sort findings by severity. Be direct and opinionated. Skip praise.

## Code to review:

{the actual code/diff/PR content}
```

### Specialization-specific concerns

**Distributed Systems:** Consistency guarantees, split-brain scenarios, ordering assumptions, idempotency, retry semantics, backpressure, thundering herd, clock skew, network partition behavior.

**Performance Engineering:** Hot paths, allocation pressure, cache coherence, lock contention, false sharing, unnecessary copies, batching opportunities, tail latency, GC pressure, syscall overhead.

**Security:** Input validation boundaries, trust boundaries, privilege escalation paths, secret handling, timing side channels, TOCTOU races, dependency vulnerabilities, auth bypass paths.

**Custom specialization:** Extract the core domain concerns and probe those specifically.

**Step 4: Present findings**

After the subagent returns, present the findings organized by severity. For any CRITICAL or HIGH findings, ask the user if they want to discuss or address specific items.
