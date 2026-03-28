# Claude Skills

Specialized skills for Claude Code: expert engineering review, plan review, and claim verification.

## Installation

First, register the marketplace:
```
/plugin marketplace add cu9hue/claude-skills
```

Then install the plugin:
```
/plugin install claude-skills@claude-skills
```

## Skills

### expert-review
Dispatches a world-class engineer subagent with a chosen specialization (distributed systems, performance, security, or custom) to poke holes in your code, design, or PR.

### review-plan
Structured interactive review of implementation plans, design docs, or PRs — covers architecture, code quality, tests, and performance with opinionated recommendations.

### verify-claims
Dispatches parallel subagents to verify factual claims in documents (RFCs, design docs, PRs) against the actual codebase. Catches stale assumptions and incorrect references.

### interrogate-plan
Takes an existing implementation plan, spec, or design doc and systematically walks every decision branch until no ambiguity remains. Ensures an implementing agent makes zero implicit decisions.
