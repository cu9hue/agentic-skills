# Audit rubric

Phase 3. Score the interface, then run the hard gate. Cite `file:line` for every
finding so fixes are unambiguous.

## Scored dimensions

Five dimensions, each 0-4. Total out of 20.

| Score | Meaning |
|---|---|
| 0 | Severe: fails the basics |
| 1 | Major gaps |
| 2 | Acceptable, notable issues |
| 3 | Good, minor gaps |
| 4 | Excellent |

1. **Accessibility:** contrast (4.5:1 body, 3:1 large/UI), `:focus-visible`
   rings, keyboard reachability, semantic HTML, labels wired with
   `aria-describedby`, alt text. Checklist folded in: focus present on every
   interactive element.
2. **Performance:** animates `transform`/`opacity` only, no layout thrash,
   `will-change` used sparingly, lazy loading, no bundle bloat, 60fps on mobile.
3. **Responsive:** no fixed widths that overflow, 44x44px touch targets, text
   scales to 200% without breakage, breakpoint coverage.
4. **Theming / token adherence:** values come from `DESIGN.md` tokens, not
   hard-coded; dark mode complete; tokens consistent. Checklist folded in: type
   hierarchy reads (h1 > h2 > body > caption), spacing rhythm follows the 4pt
   scale, parallel components are visually consistent.
5. **Anti-patterns (critical):** count Slop Catalog tells. 0 = slop gallery (5+
   tells), 4 = no AI tells, distinctive and intentional. Checklist folded in:
   hover/focus/active/disabled/loading/error/empty/success states all present;
   empty and loading states designed, not improvised.

**Bands:** 18-20 excellent · 14-17 good · 10-13 acceptable · 6-9 poor ·
0-5 critical.

## Severity tags

Tag each finding so triage is obvious:

- **P0:** blocking (broken layout, WCAG A failure, text overflow)
- **P1:** major (WCAG AA violation, missing focus/error state)
- **P2:** minor annoyance
- **P3:** polish only

Fix every P0 and P1 before handoff.

## Report structure

1. Anti-patterns verdict (dimension 5) first: the slop tells found, by domain.
2. Health score table (five dimensions, total, band).
3. Findings by severity (P0 down), each with `file:line` and the fix.
4. Systemic patterns (one root cause behind many findings).
5. What is already good.

## 15-minute pre-handoff gate (hard pass/fail)

The interface does not ship until all five pass:

- [ ] at least 8 of 10 sampled components map cleanly to `DESIGN.md` tokens (no
      stray hex, no ad-hoc spacing)
- [ ] no more than 3 shadow recipes across core surfaces
- [ ] WCAG contrast passes on 5 representative text styles
- [ ] focus and disabled states present on every interactive element
- [ ] component naming is non-duplicative (no `Card2`, `ButtonNew`)
