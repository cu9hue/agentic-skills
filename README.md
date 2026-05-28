# Agent Skills

Specialized skills for coding agents: structured plan review, and resolving every open design decision before implementation.

## Layout

Skills live in `.agents/skills` — the open `SKILL.md` standard, read natively by
both Claude Code and Codex. `.claude/skills` symlinks to `.agents/skills` for
project-scope use. Shared cross-project, cross-agent instructions live in
`.agents/GLOBAL.md`.

## Global install

Point both agents at this repo as a single source of truth, active in every
project. Run once, with `REPO` set to wherever you cloned this:

```sh
REPO="$HOME/Projects/personal/claude-skills"   # adjust to your clone path

# Codex reads ~/.agents/skills natively at user scope:
ln -s "$REPO/.agents" ~/.agents

# Claude reads ~/.claude/skills — point it at the same canonical skills
# (skip the rm if ~/.claude/skills holds skills you want to keep):
rm -rf ~/.claude/skills
ln -s ~/.agents/skills ~/.claude/skills
```

Codex's built-in skills in `~/.codex/skills` are left untouched (it reads both
locations).

Share global instructions by importing `GLOBAL.md` from each agent's user-level
instruction file — both support `@path` imports. Add an **absolute** path
(e.g. `@/Users/you/.agents/GLOBAL.md`):

```
# ~/.claude/CLAUDE.md   →   @/Users/you/.agents/GLOBAL.md
# ~/.codex/AGENTS.md    →   @/Users/you/.agents/GLOBAL.md
```

**Adding a skill:** drop a folder into `.agents/skills/<name>/` and commit — both
agents pick it up everywhere. Only `SKILL.md` skills port across agents;
subagents (`.md` vs `.toml`) and hooks are agent-specific.

> Note: running Codex *inside this repo* may list each skill twice — Codex sees
> them via both its repo scan and `~/.agents`. This is cosmetic and only happens
> here; in other projects each skill appears once.

## Skills

### Process
- **review-plan** — structured interactive review of implementation plans, design docs, or PRs (architecture, code quality, tests, performance).
- **design-decision-tree** — walks every decision branch in a plan/spec until no ambiguity remains, so an implementing agent makes zero implicit decisions.
- **gateguard** — fact-forcing gate that blocks Edit/Write/Bash until concrete investigation (importers, schemas, intent) is done.
- **safety-guard** — prevents destructive operations on production systems or during autonomous runs.

### Languages
- **rust-patterns** / **rust-testing** — idiomatic Rust (ownership, traits, concurrency) and TDD-style testing (unit, integration, async, property-based).
- **cpp-coding-standards** / **cpp-testing** — C++ Core Guidelines enforcement; GoogleTest/CTest, coverage, sanitizers.
- **python-patterns** / **python-testing** — Pythonic idioms, PEP 8, type hints; pytest, fixtures, mocking, coverage.
- **coding-standards** — language-agnostic baseline conventions (naming, readability, immutability).

### Frontend
- **vite-patterns** — Vite config, plugins, HMR, env/proxy, SSR, library mode, build optimization.
- **frontend-a11y** — accessibility patterns (semantic HTML, ARIA, keyboard nav, focus). Framework-agnostic substance despite a React-flavored description.

### Security
- **security-review** — checklist + patterns for auth, user input, secrets, API endpoints, payments; bundles `cloud-infrastructure-security.md`.

### Ops & growth
- **dashboard-builder** — operator-focused monitoring dashboards for Grafana/SigNoz.
- **seo** — technical SEO, on-page, structured data, Core Web Vitals, content strategy.

> Most extracted skills are adapted from [ECC](https://github.com/affaan-m/ECC) (MIT).
> Skills needing external infra (e.g. AgentShield MCP, Exa MCP for lead-intelligence)
> were left out until those servers are wired up.
