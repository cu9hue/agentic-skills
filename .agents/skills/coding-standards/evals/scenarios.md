# coding-standards — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. The subagent returns only the
deliverable. Anonymize outputs into teams, blind-judge against the rubrics,
log the verdict in `results.md`.

## Shared material

All scenarios are self-contained; code under review is inlined in the
scenario prompts. Language is TypeScript throughout, matching the skill's
examples.

## S1 — write: fetch-and-merge module

User message: "Write a small TypeScript module for a Node service: a
function that, given a userId, fetches the user's profile from
`GET https://api.example.com/users/:id` and their recent orders from
`GET https://api.example.com/users/:id/orders`, retries each failed request
up to 3 times with a 500ms delay between attempts, and returns a merged
summary object `{ user, orders, orderCount }`. Include a short usage
example."

Rubric:
- functions use verb-noun names and variables are descriptive; no
  single-letter or cryptic abbreviated identifiers (`d`, `res2`, `fn1`)
- explicit types on function parameters and return values; `any` appears
  nowhere
- fetch results are checked (`response.ok` or equivalent status check) and
  failures are handled via try/catch or explicit error path — not bare
  `fetch(...).json()`
- the two independent fetches run in parallel (`Promise.all` or
  equivalent), not sequentially awaited one after the other
- the retry count (3) and delay (500) appear as named constants (e.g.
  `MAX_RETRIES`, `RETRY_DELAY_MS`), not inline magic numbers at the point
  of use
- the merged summary is built as a new object; no mutation of fetched
  objects or shared state
- comments, if any, explain why rather than restating what the line does

## S2 — review: planted violations

User message: "Review this TypeScript function and list the code-quality
problems you find. Be specific — point at lines.

```typescript
const results = []

async function proc(id: any) {
  const d = await fetch('https://api.example.com/markets/' + id)
  const j = await d.json()
  const owner = await fetchUser(j.ownerId)
  const stats = await fetchStats(j.id)
  if (j) {
    if (j.status === 'active') {
      if (owner) {
        if (owner.verified) {
          if (stats.volume > 1000) {
            j.featured = true
            results.push(j)
          }
        }
      }
    }
  }
  // return the market object
  return j
}
```"

Planted violations (rubric = review flags each one):
- unclear names: `proc`, `d`, `j` (non-descriptive function/variable
  naming)
- `id: any` (type-safety violation; should be `string` or similar)
- no error handling: no `response.ok` check and no try/catch around the
  fetch/json calls
- sequential awaits: `fetchUser` and `fetchStats` are independent of each
  other and could run in parallel (`Promise.all`)
- deep nesting: 5 nested ifs that should be early returns / guard clauses
- direct mutation: `j.featured = true` and/or `results.push(j)` mutating
  the object / shared module-level array
- magic number: `1000` should be a named constant
- useless comment: `// return the market object` restates the code

## S3 — refactor: naming, immutability, nesting

User message: "Refactor this TypeScript function for readability. It
computes order-line totals: when the flag is set it keeps only lines with a
positive amount and applies 8% tax; otherwise it passes amounts through as
totals. Keep the behavior identical.

```typescript
function calc(data, f) {
  let res = []
  for (let i = 0; i < data.length; i++) {
    let item = data[i]
    if (f) {
      if (item.a > 0) {
        item.t = item.a * 1.08
        res.push(item)
      }
    } else {
      item.t = item.a
      res.push(item)
    }
  }
  return res
}
```"

Rubric:
- `calc`, `f`, `res`, and the loop temp are renamed to descriptive names
  (e.g. `calculateLineTotals`, `applyTax`, `lineTotals`)
- the `a`/`t` property names are surfaced via a typed interface or clearly
  named locals — the refactor adds explicit TypeScript types; no `any`
- input objects are not mutated: each output line is a new object
  (spread/object literal), not `item.t = ...` on the input
- nesting is flattened: filter+map, guard clauses, or a single-level
  structure replaces the nested if-inside-loop
- `1.08` (or `0.08`) is a named constant (e.g. `TAX_RATE`)
- behavior is preserved: tax path filters non-positive amounts; non-tax
  path keeps every line with total = amount

## S4 — negative: should not trigger

User message: "Quick question, two sentences max: in a REST API, when
should I use PATCH instead of PUT?"

Rubric:
- answers the question directly in at most a few sentences; no headers,
  checklist, code sample, or standards lecture beyond the ask (the skill's
  API-conventions section must not turn a quick factual question into a
  review)
