---
name: ui-design
description: "Design and build consumer web interfaces that show care instead of converging on generic AI aesthetics. Runs three phases: establish a DESIGN.md from real references, build within its tokens, then audit against a slop rubric. Use when starting, building, or reviewing any UI where visual quality matters. Assumes Tailwind + React."
origin: harvested from ECC design-system (MIT), impeccable (Apache-2.0), and posts by mindstudio.ai and managed-code.com
---

# UI Design

Build interfaces that look like someone with taste made a decision, not like the
average of every screenshot in the training set.

## The Principle

Under vague direction, the model falls back to the highest-frequency patterns it
has seen: Inter type, indigo accents, gradient hero, glassmorphism, over-rounded
cards, uniform padding. This is statistical gravity, not a style choice.

**Silence in the spec = defaults = slop.** Every decision you leave unstated
reverts to the generic mean. The skill's whole job is to force explicit decisions
in (Phase 1), build only from them (Phase 2), and catch the drift (Phase 3).

## When to Activate

- starting a new consumer UI, page, or component
- building any interactive element (buttons, forms, cards, navigation)
- auditing an existing interface for AI-slop tells
- reviewing a design before handoff or merge

## The Three Phases

### Phase 1: Establish the system (reference-first)

You cannot specify taste from nothing, and a non-designer interviewed in the
abstract still produces generic answers. Start from concrete references.

1. **Get references.** Ask for 1-3 real screens or sites the user admires, and
   1-2 anti-references they dislike. If they have none, ask for three adjectives
   and two products in the same space, propose candidate references, and confirm
   before proceeding. Never skip this step.
2. **Reverse-engineer the tokens.** For each reference, name the concrete moves:
   typefaces and weights, the accent hue and neutral temperature, spacing
   density, corner radius, elevation character, motion feel. Write down what you
   are taking from each and what you are leaving.
3. **Fill the brief.** Five fields, all required:
   - the user's job, in one sentence
   - the screen and component inventory
   - 3-5 personality adjectives, each with an anti-example ("warm, not
     childish")
   - the required interaction states per component
   - the reference set from step 1
4. **Emit `DESIGN.md`.** Fill `references/design-md-template.md`. Every token is
   an explicit value (a hex, a rem, a cubic-bezier), never a description. "Modern
   and clean" is not a token. Commit `DESIGN.md` to the project before building.

> Future hook: once the user has built taste across projects, curated presets can
> seed step 1. Not yet. Reference-first until then.

### Phase 2: Build within bounds

1. **Pull every value from DESIGN.md tokens.** No arbitrary hex, no one-off
   shadow, no ad-hoc spacing. If you need a value the system lacks, add it to
   `DESIGN.md` first, then use it. Never inline a one-off.
2. **Verify components in isolation before composing pages.** A button that is
   wrong in isolation is wrong on every page.
3. **Lock the layout before styling.** Grid, max-width, and padding rhythm come
   before color and ornament.
4. **Ship all eight interactive states up front:** default, hover, focus
   (`:focus-visible`), active, disabled, loading, error, success. Hover without
   focus fails keyboard users. States are not a follow-up task.

### Phase 3: Audit before handoff

1. Run `references/audit-rubric.md`: score each dimension 0-4, cite `file:line`,
   tag findings P0-P3.
2. Run the 15-minute pre-handoff gate (hard pass/fail) in that file.
3. Run the Slop Catalog below as a detection pass.
4. Fix every P0 and P1 before shipping. Do not ship around them.

## The Slop Catalog

The banned visual patterns, by domain, each with its antidote. This is the visual
analog of a banned-phrase list. When you catch one, rewrite to the antidote.

### Type
**Tells:** Inter / Geist / Roboto / Arial / system default as the brand face;
more than 3 families; body text under 16px; `px` font sizes (breaks zoom);
two near-identical sans paired together.
**Antidote:** one typeface with personality; a 5-size modular scale (ratio
≥ 1.25: major third, perfect fourth, or fifth); 3-4 weights, loaded only as
used; `rem` units; line length 45-75ch; line-height 1.5-1.7 body, 1.1-1.2
headings; pair on contrasting axes (serif + sans, geometric + humanist) or use
one family in multiple weights.

### Color
**Tells:** indigo / purple defaults and blue-purple gradient glows; pure black
and pure gray neutrals; gray text on a colored background; gradient text
(`background-clip: text`); color as the only signal.
**Antidote:** OKLCH for perceptually even steps; tinted neutrals (add chroma
0.005-0.015 toward the brand hue, not generic warm/cool); 60-30-10 split (60%
neutral, 30% secondary, 10% accent); semantic roles (success/error/warning/info);
WCAG 4.5:1 body and 3:1 large text and UI; pair color with icon or label; gray
text on color becomes a darker shade of the background hue.

### Shape and elevation
**Tells:** over-rounded cards (radius 24-40px); more than 3 shadow recipes;
`border: 1px` and a wide `box-shadow` on the same element; side-stripe accent
borders (`border-left > 1px`); glassmorphism as a default; cards nested in cards.
**Antidote:** cap radius at 12-16px; a named elevation system with at most 3
shadow recipes; choose border or shadow, not both; vary spacing for separation
instead of stripes and nesting.

### Layout
**Tells:** gradient hero + centered headline + subhead + CTA; identical card
grids repeated forever; uniform ~50px padding everywhere; tiny uppercase eyebrows
over every section; 01 / 02 / 03 numbered markers by default; shadcn-template
icon-and-label sidebar.
**Antidote:** a 4pt spacing scale (4, 8, 12, 16, 24, 32, 48, 64, 96); tight
grouping (8-12px) for related items, generous separation (48-96px) between
sections; vary spacing for rhythm; Flexbox for 1D, Grid for 2D, `repeat(auto-fit,
minmax(280px, 1fr))` for responsive grids; pass the squint test (blur your eyes,
hierarchy still reads).

### Motion
**Tells:** bounce or elastic easing; scroll-triggered animation on every section;
animating `width` / `height` / `top` / `left`.
**Antidote:** the 100/300/500 timing rule (100-150ms feedback, 200-300ms state
change, 300-500ms layout, 500-800ms entrance; exit at ~75% of entrance); ease-out
curves (`cubic-bezier(0.16, 1, 0.3, 1)` and kin); animate `transform` and
`opacity` only; `prefers-reduced-motion` is not optional; reveal animations must
enhance an already-visible default.

### States and copy
**Tells:** missing focus / disabled / error / empty / loading states;
placeholders used as labels; em dashes; buzzwords (seamless, leverage, transform,
unleash, cutting-edge); "click here" link text.
**Antidote:** all eight interactive states; visible `<label>` elements, validate
on blur, errors below the field wired with `aria-describedby`; verb + object
button labels ("Save changes", not "OK"); link text that means something out of
context ("View pricing", not "click here"); 44x44px minimum touch targets; undo
toast over confirmation dialog for destructive actions.

## Quality Gate

Before delivering, confirm:

- `DESIGN.md` exists and every value used traces to a token in it
- no Slop Catalog tell survives the detection pass
- all eight interactive states present on interactive elements
- the pre-handoff gate in `references/audit-rubric.md` passes
- no em dashes, no buzzwords in UI copy

## References

- `references/design-md-template.md`: the fill-in `DESIGN.md` artifact (Phase 1)
- `references/audit-rubric.md`: scoring dimensions and the pre-handoff gate (Phase 3)
