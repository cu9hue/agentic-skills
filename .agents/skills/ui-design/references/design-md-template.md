# DESIGN.md template

Copy this into the project as `DESIGN.md` and replace every placeholder with an
explicit value. A description ("warm neutrals") is not a value; a token
(`--neutral-50: oklch(0.98 0.008 80)`) is. Leave nothing blank: a blank reverts
to the generic default.

Tokens are shown twice: as CSS custom properties (the source of truth) and as
their Tailwind theme mapping. Keep both in sync.

---

## Personality

- Adjectives (3-5), each with an anti-example: `warm, not childish` · `precise,
  not clinical` · `...`
- One sentence on the feeling a first-time user should get.

## Reference set

| Reference | What we take | What we leave |
|---|---|---|
| <name / url> | <e.g. its restrained type scale> | <e.g. its cool palette> |

Anti-references (looks to avoid): <...>

## Type

Families and weights:

Pick a display face with personality (Fontshare's Clash Display or Satoshi, a
characterful serif, a grotesk with real width), never Inter/Geist/Roboto.

```css
:root {
  --font-display: "<Display Face>", serif;   /* headings */
  --font-body: "<Body Face>", sans-serif;     /* body */
  --font-mono: "<Mono Face>", monospace;      /* optional */
}
```

5-size modular scale (pick a ratio: 1.25 / 1.333 / 1.5):

```css
:root {
  --text-xs: 0.75rem;    /* captions, legal */
  --text-sm: 0.875rem;   /* metadata */
  --text-base: 1rem;     /* body (never below 16px) */
  --text-lg: 1.5rem;     /* subheads, lead */
  --text-xl: 2.5rem;     /* headlines (clamp for marketing, cap ~6rem) */
}
```

Rules: line length 45-75ch · line-height 1.5-1.7 body, 1.1-1.2 headings ·
weights used: `<400 / 500 / 600 / 700>` · `text-wrap: balance` on h1-h3.

Tailwind:

```js
theme: {
  fontFamily: { display: ['<Display Face>', 'serif'], sans: ['<Body Face>', 'sans-serif'], mono: ['<Mono Face>', 'monospace'] },
  fontSize: { xs: '0.75rem', sm: '0.875rem', base: '1rem', lg: '1.5rem', xl: '2.5rem' },
}
```

## Color

OKLCH, tinted neutrals (chroma 0.005-0.015 toward the brand hue). 60-30-10:
neutral dominates, accent is 10%.

```css
:root {
  /* neutrals (tinted, not pure gray) */
  --neutral-50:  oklch(<L C H>);
  --neutral-100: oklch(<L C H>);
  --neutral-500: oklch(<L C H>);
  --neutral-900: oklch(<L C H>);
  /* accent (10% usage: CTAs, focus, highlights) */
  --accent:      oklch(<L C H>);
  --accent-hover: oklch(<L C H>);
  /* semantic */
  --success: oklch(<L C H>);
  --error:   oklch(<L C H>);
  --warning: oklch(<L C H>);
  --info:    oklch(<L C H>);
  /* surfaces */
  --bg:      var(--neutral-50);
  --surface: var(--neutral-100);
  --text:    var(--neutral-900);
  --text-muted: oklch(<L C H>);  /* not gray-on-color: a darker hue of its bg */
}
```

Dark mode: shift surface lightness for depth (not heavier shadows), desaturate
accents slightly, reduce light-text weight. Contrast floors: 4.5:1 body, 3:1
large text and UI.

Tailwind: map each var into `theme.colors` (`neutral`, `accent`, `success`, ...).

## Spacing

4pt base scale (8pt is too coarse). Use `gap`, not margins, for sibling spacing.

```css
:root {
  --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
  --space-6: 24px; --space-8: 32px; --space-12: 48px; --space-16: 64px; --space-24: 96px;
}
```

Rhythm: 8-12px within a group, 48-96px between sections. Tailwind: extend
`theme.spacing` to match.

## Radius

```css
:root { --radius-sm: 4px; --radius-md: 8px; --radius-lg: 12px; } /* cap at 12-16px */
```

## Elevation

At most 3 named shadow recipes. Pick border or shadow per element, never both.

```css
:root {
  --shadow-low:  <0 1px 2px ...>;
  --shadow-mid:  <0 4px 12px ...>;
  --shadow-high: <0 12px 32px ...>;
}
```

## Motion

```css
:root {
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
  --dur-fast: 120ms;   /* feedback */
  --dur-base: 250ms;   /* state change */
  --dur-slow: 400ms;   /* layout */
}
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

Animate `transform` and `opacity` only. No bounce or elastic. No scroll-triggered
motion on every section.

## Imagery

Pull from the product's own world before any stock. Define one treatment for the
whole set so images read as intentional, not scavenged.

- Sources: `<the product's own photography, or a named licensable source>`; no
  invented URLs, no placeholders shipped as final.
- Treatment (one, applied to every image): `<e.g. duotone --neutral-900 +
  --accent · 12% grain · -8% saturation grade>`
- Aspect ratios in use: `<e.g. 16:9 hero, 4:5 cards>`
- Format and delivery: WebP/AVIF · `width`/`height` always set · responsive
  `srcset` · lazy-load below the fold.
- Alt text: states content or function, never "image".

## Explicit negatives

This project's specific "do not" list (beyond the global Slop Catalog). Examples:

- no gradient text, no glassmorphism
- no card nested inside a card
- accent appears on at most one element per viewport
- <project-specific bans>
