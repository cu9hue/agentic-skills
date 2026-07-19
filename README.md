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

`GLOBAL.md` holds always-on coding directives, kept lean since both agents load
it every turn. Keep it agent-agnostic; agent-specific guidance (Claude hooks, the
RTK proxy) lives in the separately-imported `RTK.md`. Some rules adapt
[Karpathy's LLM-coding observations](https://x.com/karpathy/status/2015883857489522876).

**Adding a skill:** drop a folder into `.agents/skills/<name>/` and commit — both
agents pick it up everywhere. Only `SKILL.md` skills port across agents;
subagents (`.md` vs `.toml`) and hooks are agent-specific.

> Note: running Codex *inside this repo* may list each skill twice — Codex sees
> them via both its repo scan and `~/.agents`. This is cosmetic and only happens
> here; in other projects each skill appears once.

## Skills

### Process
- **skill-authoring** — the binding process for skill work in this repo: every new skill ships with persisted evals (`<skill>/evals/scenarios.md` + append-only `results.md`), the no-skill baseline runs before drafting, edits rerun persisted evals as regression (backfilling legacy skills first), and a blind subagent judge decides — plus lean-authoring rules (500-line cap, triggers-only descriptions, `references/` for heavy material). Eval methodology adapted from [Phil Schmid's "Testing Agent Skills"](https://www.philschmid.de/testing-skills); on Claude it complements `superpowers:writing-skills`, on Codex it stands alone.
- **review-plan** — structured interactive review of implementation plans, design docs, or PRs (architecture, code quality, tests, performance).
- **design-decision-tree** — walks every decision branch in a plan/spec until no ambiguity remains, so an implementing agent makes zero implicit decisions.
- **gateguard** — fact-forcing gate that blocks Edit/Write/Bash until concrete investigation (importers, schemas, intent) is done.
- **safety-guard** — prevents destructive operations on production systems or during autonomous runs.
- **goal-loop** — write `/goal` contracts for long-running autonomous runs (the "Ralph loop") in Claude Code and Codex: a 5-part contract (objective, constraints, validation command, stop condition, docs), the meta-prompting trick, drift handling, and per-agent mechanics kept separate. Harvested from [davidondrej/skills](https://github.com/davidondrej/skills) (MIT); Claude Code mechanics corrected against the [official `/goal` docs](https://code.claude.com/docs/en/goal).

### Languages
- **rust-patterns** / **rust-testing** — idiomatic Rust (ownership, traits, concurrency) and TDD-style testing (unit, integration, async, property-based).
- **cpp-coding-standards** / **cpp-testing** — C++ Core Guidelines enforcement; GoogleTest/CTest, coverage, sanitizers.
- **python-testing** — pytest, fixtures, mocking, coverage. (python-patterns retired 2026-07-19: evals showed baseline passes 17/18 of its mandates unaided — see git history for the eval record.)
- **coding-standards** — language-agnostic baseline conventions (naming, readability, immutability).

### Frontend
- **ui-design** — anti-slop discipline for consumer UIs: establish a `DESIGN.md` from real references and the product's own subject, build within its tokens, audit against a slop rubric spanning type, color, layout, motion, and imagery. Assumes Tailwind + React. Harvested from ECC, [impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0), two anti-slop posts, and the design skills from [Anthropic](https://github.com/anthropics/skills), [claudekit](https://github.com/claudekit/frontend-design-pro-demo), and [taste-skill](https://github.com/Leonxlnx/taste-skill).
- **vite-patterns** — Vite config, plugins, HMR, env/proxy, SSR, library mode, build optimization.
- *(frontend-a11y retired 2026-07-19: baseline passed all 21 eval rubric lines unaided — see git history for the eval record.)*

### Writing
- **writing** — direct, concrete, anti-slop prose. Anti-slop rules apply to all writing; a fixed first-person voice (`references/voice-guide.md`) layers on for personal and opinion pieces. Adapted from ECC article-writing.

### Research
- **digest-paper** — digest a scientific paper from a PDF/arXiv/DOI in escalating passes (triage by default; brief and deep-dive on request), with the author's claims kept separate from an independent critical read; bundles `literature-survey.md` for mapping a field. Synthesized from Keshav's "How to Read a Paper" (three-pass method) and a five-question hypothesis-summary framework.
- **ankify** — turn a paper/article/doc/notes into Anki flashcards biased toward conceptual understanding over rote recall: drafts candidates against a value bar (keep only what changes how you think), you curate. Synthesized from Michael Nielsen's "Augmenting Long-Term Memory"; pairs with **digest-paper**.
- **socratic** — a Socratic questioning session over material you've read: extracts the core ideas as a private coverage checklist, interrogates one idea at a time (one question per turn, probe-then-reveal on misses), closes with a per-idea gap report and hands everything to **ankify**. Question taxonomy from [UConn CETL's "Socratic Questions"](https://cetl.uconn.edu/resources/teaching-your-course/leading-effective-discussions/socratic-questions/); pairs with **digest-paper**.

### Security
- **security-review** — checklist + patterns for auth, user input, secrets, API endpoints, payments; bundles `cloud-infrastructure-security.md`.

### Ops & growth
- **dashboard-builder** — operator-focused monitoring dashboards for Grafana/SigNoz.
- **seo** — technical SEO, on-page, structured data, Core Web Vitals, content strategy.
- **landing-copy** — landing-page copy and product positioning that sells the desire, not the feature: pin the position, write the page, audit against a conversion-killer catalog. Distilled from Marc Lou's "31 Principles of a Viral Product" and Julian Shapiro's landing-page guide; pairs with **ui-design** (visuals) and **seo** (discovery).
- **gtm-strategy** — go-to-market strategy for a bootstrapped founder-led SaaS as falsifiable bets: stage diagnosis, evidence interrogation (evidence vs assumption tagging), Dunford-style positioning, exactly one channel bet from a fit table, and a 90-day plan with numeric kill criteria. Synthesized from April Dunford's *Obviously Awesome*, the Bullseye framework (*Traction*), and *The Mom Test*; hands off to **landing-copy** and **seo** for execution.
- **growth-metrics** — closes **gtm-strategy**'s measurement loop: one value-delivery activation event, a tracking plan capped at ten events (each carrying the decision it informs), PostHog instrumentation through a typed event catalog on the Next.js/Vercel/Supabase/Stripe stack, and a weekly scorecard read against the strategy doc's kill criteria — falsified bets called falsified, with the named fallback. Ops metrics stay with **dashboard-builder**.
- **saas-deploy-readiness** — deploy readiness for a Next.js + Vercel + Supabase + Stripe + Resend + GitHub Actions + Drizzle stack: environment separation, env-var classification, Drizzle migrations (expand-contract), rollback, safe server-action errors, smoke tests. Distilled from real deploy incidents; migration and rollback patterns adapted from ECC.

> Most extracted skills are adapted from [ECC](https://github.com/affaan-m/ECC) (MIT).
> Skills needing external infra (e.g. AgentShield MCP, Exa MCP for lead-intelligence)
> were left out until those servers are wired up.
