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

### review-plan
Structured interactive review of implementation plans, design docs, or PRs — covers architecture, code quality, tests, and performance with opinionated recommendations.

### design-decision-tree
Takes an existing implementation plan, spec, or design doc and systematically walks every decision branch until no ambiguity remains. Ensures an implementing agent makes zero implicit decisions.
