---
name: diagram
description: >-
  Generate an interactive architecture atlas for a named system or subsystem in
  a codebase — a self-contained HTML page with a clickable Map (nodes + edges
  with detail panes), plus Pipeline, Messages, State machines, and Facts &
  rationale tabs. Use when the user wants to map, document, visualize, diagram,
  or produce an architecture overview of a system.
argument-hint: "[system]"
---

# Diagram

Turn any system in a codebase into an interactive overview: a clickable
node/edge map with detail panes, plus Pipeline, Messages, State machines, and
Facts & rationale tabs.

You produce one `model.json`; `render.mjs` injects it into `template.html` and
writes a standalone HTML page.

Throughout this skill, `<skill-dir>` means this skill's base directory (it is
announced when the skill is invoked).

## Inputs
- **system** (required): the thing to map — a service, package family, or flow.
- **out-dir** (optional): where `model.json` and the artifact land. Defaults to
  the model file's own directory.

## Files in this skill
- `schema.md` — the exact `model.json` contract. **Read it before authoring.**
- `template.html` — the renderer/engine. Do not edit per-run; it is data-driven.
- `render.mjs` — inject + write. `node <skill-dir>/render.mjs --model <f> [--out-dir <d>]`.
- `examples/nsq.model.json` — a real atlas of the NSQ messaging platform, built from
  the actual source. **Read it before authoring** to calibrate depth: every `desc`
  cites real code, and the gotchas are footguns found by reading it, not guesses.

## Procedure

### 1. Resolve the system
Find the directories and packages that make it up, and map the user's word to
concrete paths. If the mapping is ambiguous, ask rather than guessing.

### 2. Explore (parallelize)
Fan out reads across the resolved paths. Extract:
- **Components** (nodes): every meaningful process, store, external boundary,
  and control-plane piece. For each: what it does, the `file:line` it lives in,
  data in/out, message types it handles, and its real failure modes / gotchas.
- **Wires** (edges + edgeMessages): who talks to whom, over what transport
  (Kafka / Redis / WS / HTTP / gRPC / in-process / DB), and the exact payloads
  on each wire.
- **Scenarios**: 2–5 end-to-end flows worth highlighting (a happy path, a
  control path, a failure/backpressure path). Give each an ordered edge `path`.
- **State machines**: the small lifecycles (connection, subscription, consume
  loop, retry/backoff). List states + transitions with triggers.
- **Pipeline**: the ordered stages one unit of work flows through.
- **Messages**: the wire/message catalog (protocols, topics, enums, payloads).
- **Facts / rationale / gotchas**: the headline takeaways, why each layer
  exists, and the sharp edges.

Cite `file:line` everywhere. Concrete over generic. Match the depth of
`examples/nsq.model.json`.

### 3. Author `model.json`
Write it following `schema.md` exactly. 12–24 nodes is the sweet spot; push
control/infra pieces to `region:"side"`.

Before rendering, verify your own citations — open a sample of the `file:line`
references and confirm they point at the code you claimed. A citation that
looks plausible but lands on the wrong line is worse than no citation.

### 4. Render
```
node <skill-dir>/render.mjs --model <out-dir>/model.json
```
It writes `<system>.html` (open in a browser) and `<system>.fragment.html`.

### 5. Report
Give the user the path to `<system>.html`. If they want it hosted/clickable,
publish `<system>.fragment.html` via the Artifact tool — it carries no doctype
or `<body>` wrapper and is fully inline, with no external assets to trip CSP.
Summarize what the map covers.

## Design

The engine ships with its own visual language. Keep it; do not restyle per-run
and do not import an external brand's tokens.

**The core rule: hue belongs to the data, not the chrome.** Connection types
own the palette (Kafka red, Redis amber, WebSocket blue, in-process green, …),
and those colors carry real meaning on the map. So the interface itself is
achromatic — surfaces, borders, and text are neutral grays, and interactive
state reads as *luminance and weight* rather than another competing color. A
tinted UI accent would collide with the wire colors and make the map ambiguous.

Tokens live in one `:root` block at the top of `template.html`:

- **Surfaces** — `--bg` ground, `--panel` rails/cards, `--panel2` raised
  controls. Borders: `--line` hairline, `--line2` hover/active.
- **Text** — `--ink` primary, `--ink2` secondary, `--ink3` meta/labels.
- **State** — `--state` / `--stateHi` are white-alpha tints for active and
  hover surfaces. Selection uses `--sel` (pure white) for strokes.
- **Semantic only** — `--good` / `--warn` / `--bad` mean positive / caution /
  negative. Never decorative.
- **Focus** — `--focus` drives a visible `:focus-visible` ring. Keep it; the
  map is keyboard-navigable.

Because active states carry no hue, they need a non-color affordance: the
active tab gets an inset underline bar, the active scenario gets an inset left
bar, and a selected node gets a white stroke plus a lifted fill. Preserve
these if you touch the CSS — without them the UI loses its "you are here."

**What NOT to flatten.** This is a dense interactive explorer, not a figure.
Its per-type edge colors, 2px strokes, curved edges, and canvas depth cue all
carry information. Do not apply generic "flat diagram" rules (strokeless
nodes, uniform surfaces, thin neutral edges) — that has been tried and it
makes the map materially harder to read.

## Map controls (built into the artifact)
- Click a **box** or **line** for its detail pane; the label of the selected/current
  edge is the only one drawn, so the map stays legible.
- Pick a **flow scenario** (left) to highlight + auto-play a path.
- **▶** plays the active flow on a continuous **loop** (toggles to ⏸); each loop
  wipes the lit trail and pulses the source node so the restart is obvious.
- **← / →** step through the flow one edge at a time (pauses the loop); the status
  bar shows `step k/n` and the current wire.
- Layer band labels sit in a left swimlane gutter; node positions are auto-computed
  (no hand-placed coordinates), never overlap, and spread to fill the window.

## Extra node affordances
- `links: [["Runbook", url], …]` on a node renders as external link pills.
- `meta.repo` (strictly `owner/name`) turns every `file:line` citation into a
  GitHub deep link; `meta.branch` overrides the default `main` ref. Put
  worktree/branch provenance in `meta.source` (display-only) — never append it
  to `repo`.

## Quality bar
- Every `desc` cites at least one `file:line`; no hand-waving.
- Gotchas are real footguns found in the code (races, silent drops, ordering
  hazards), not boilerplate caveats.
- The map reads top→bottom along the dominant data flow.
