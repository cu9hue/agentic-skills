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
- **cpp-coding-standards** — C++ Core Guidelines enforcement (RAII, immutability, type safety, value semantics). Earns its keep as attention allocation: organizes open-ended C++ advice around the guidelines (see `evals/results.md`).
- **coding-standards** — language-agnostic baseline conventions (naming, readability, immutability).

### Performance
- **performance-audit** — measurement-driven audit for CPU- and memory-bound native code (C, C++, Rust): five ordered gates — baseline, localize with TMA, confirm the cause, a ranked report, then fix on approval one change at a time. No fix ships without a number; anything unmeasured is labeled `hypothesis`, carrying the experiment that would settle it. Refuses in both directions — it declines wrong-layer work (I/O, database, GC latency) and work too small to measure, answering directly instead of opening an audit (see `evals/results.md`). Bundles a TMA localization guide, a dated cost model, and a symptom-to-cause-to-fix catalog. Draws the memory-hierarchy material from Ulrich Drepper's ["What Every Programmer Should Know About Memory"](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf) (2007), microarchitecture and vectorization guidance from [Agner Fog's optimization manuals](https://www.agner.org/optimize/), and the localization backbone from Intel's Top-Down Microarchitecture Analysis, per [Ahmad Yasin's 2014 paper](https://ieeexplore.ieee.org/document/6844459).

### Frontend
- **ui-design** — anti-slop discipline for consumer UIs: establish a `DESIGN.md` from real references and the product's own subject, build within its tokens, audit against a slop rubric spanning type, color, layout, motion, and imagery. Assumes Tailwind + React. Harvested from [ECC](https://github.com/affaan-m/ECC) (MIT), [impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0), two anti-slop posts, and the design skills from [Anthropic](https://github.com/anthropics/skills), [claudekit](https://github.com/claudekit/frontend-design-pro-demo), and [taste-skill](https://github.com/Leonxlnx/taste-skill).
- **frontend-a11y** — accessibility patterns (semantic HTML, ARIA, keyboard nav, focus). Earns its keep as attention allocation: puts a11y on the agenda in open-ended feature work (see `evals/results.md`).

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
- **saas-deploy-readiness** — deploy readiness for a Next.js + Vercel + Supabase + Stripe + Resend + GitHub Actions + Drizzle stack: environment separation, env-var classification, Drizzle migrations (expand-contract), rollback, safe server-action errors, smoke tests. Distilled from real deploy incidents; migration and rollback patterns adapted from ECC.

> Skills needing external infra (e.g. AgentShield MCP, Exa MCP for lead-intelligence)
> were left out until those servers are wired up.
