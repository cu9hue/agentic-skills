# frontend-a11y — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. The subagent returns only the
deliverable. Anonymize outputs into teams, blind-judge against the rubrics,
log the verdict in `results.md`.

## Shared material

S2 inlines its own JSX. No other setup needed; all scenarios are
self-contained single-shot prompts.

## S1 — build: signup form with validation

User message: "Build a React `SignupForm` component in TypeScript. Fields:
email (required), password (required, min 8 chars), and a free-text 'How did
you hear about us?' textarea (optional). Validate on submit and show
per-field error messages. No UI library, plain JSX."

Rubric:
- every input/textarea has a `<label>` connected via matching `htmlFor`/`id`
  (no placeholder-only or floating labels)
- required fields carry `required` and/or `aria-required="true"`, and any
  visual required marker (e.g. `*`) is hidden from screen readers with
  `aria-hidden`
- error messages are programmatically linked to their input via
  `aria-describedby` pointing at the error element's `id`
- invalid inputs get `aria-invalid` when their error is present
- error text is announced (`role="alert"` or an `aria-live` region)
- submit control is a real `<button type="submit">` inside a `<form>` with
  an `onSubmit` handler (not a click-handled div/span)

## S2 — review: newsletter card with planted violations

User message: "Review this React component and list every problem you find,
each with a one-line fix. Return only the numbered list of problems and
fixes.

```jsx
function NewsletterCard({ onSubscribe, error }) {
  return (
    <div className="card">
      <h1>Stay in the loop</h1>
      <h4>Get our weekly digest, no spam ever</h4>
      <img src="/sparkles.svg" className="deco" />
      <label>Email</label>
      <input type="email" />
      <input type="text" placeholder="First name" />
      {error && <span className="error">Please enter a valid email</span>}
      <div className="btn" onClick={onSubscribe} tabIndex={2}>
        Subscribe
      </div>
      <button className="settings-btn" onClick={() => openPrefs()}>
        <GearIcon />
      </button>
    </div>
  );
}
```
"

Rubric (one line per planted violation — pass = the review flags it):
- flags the heading-level skip (h1 followed by h4)
- flags the decorative `<img>` with no `alt` (fix: `alt=""` and/or
  `aria-hidden="true"`)
- flags the email `<label>` not connected to its input (missing
  `htmlFor`/`id` pairing)
- flags placeholder used as the only label on the first-name input
- flags the error `<span>` not linked to the input (missing
  `aria-describedby`, no `role="alert"`/`aria-live`, no `aria-invalid`)
- flags the click-handled `<div>` Subscribe control (should be a `<button>`,
  or needs role + keyboard handler)
- flags the positive `tabIndex={2}`
- flags the icon-only settings button missing an accessible name
  (`aria-label`)

## S3 — build: confirmation modal

User message: "Build a React `ConfirmDialog` component in TypeScript: props
`isOpen`, `onConfirm`, `onCancel`, `title`, `message`. It overlays the page
when open, with Confirm and Cancel buttons. Plain JSX, no libraries."

Rubric:
- dialog container has `role="dialog"` and `aria-modal="true"`
- dialog has an accessible name tied to the title (`aria-labelledby`
  referencing the title element's `id`, or `aria-label`)
- focus moves into the dialog when it opens (a ref + `.focus()` on open, or
  autofocus of a control inside)
- focus is restored to the previously focused element on close (previous
  `document.activeElement` saved and re-focused)
- Escape key closes/cancels the dialog
- action controls are real `<button>` elements (not click-handled divs)

## S4 — negative: should not trigger

User message: "In React, how do I memoize an expensive `sortBy` over a
10k-row array so it doesn't re-run on every render? Show the hook call."

Rubric:
- answers directly with `useMemo` (or equivalent) and a code snippet; no
  accessibility commentary, checklist, ARIA attributes, or a11y caveats
  bolted onto a pure rendering-performance question
