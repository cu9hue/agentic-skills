# vite-patterns — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. The subagent returns only the
deliverable. Anonymize outputs into teams, blind-judge against the rubrics,
log the verdict in `results.md`.

Version note: Vite moves fast and the judge cannot verify current defaults
from memory. Version-sensitive rubric lines are scored on internal
consistency (the answer commits to one Vite major and its options coherently,
and does not recommend something it elsewhere calls deprecated), not on
external facts.

## S1 — author a config for a stated setup

User message: "Write a complete `vite.config.ts` for my project and explain
each choice in one line. Setup: React 19 + TypeScript SPA. My `tsconfig.json`
already has `paths` aliases (`@/*` → `src/*`). In dev I need `/api/*`
requests forwarded to my backend at `http://localhost:8080` (which is
virtual-hosted and checks the Host header) including WebSockets, with the
`/api` prefix stripped. The dev server runs inside a Docker container. For
production I want react/react-dom split into their own vendor chunk. Type
errors must not be able to ship to production."

Rubric:
- uses `defineConfig` (typed config)
- resolves the tsconfig aliases via `vite-tsconfig-paths` (or explicitly
  names it as the option over hand-duplicating `resolve.alias`); hand-rolled
  alias duplication with no mention of the plugin fails
- proxy entry for `/api` sets `changeOrigin: true`, a `rewrite` stripping
  `/api`, and `ws: true`
- Docker requirement answered with `server.host: true` (or `host:
  '0.0.0.0'`)
- vendor split done via `manualChunks` grouping react + react-dom into one
  named chunk (object or function form); does NOT use the
  one-chunk-per-node_modules-package pattern
- closes the type-check gap: states that `vite build` does not type-check
  and adds `vite-plugin-checker` and/or `tsc --noEmit` in CI
- version consistency: the config targets one Vite major coherently (e.g.
  chunk options, minifier, and plugin choices don't contradict each other or
  mix guidance the answer itself marks as deprecated)

## S2 — review a config with planted mistakes

User message: "Review this `vite.config.ts` before we deploy Friday. List
every problem you find and why it matters:

```typescript
import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'
import legacy from '@vitejs/plugin-legacy'

export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')

  return {
    envPrefix: '',
    plugins: [
      react(),
      legacy({ targets: ['defaults'] }),
    ],
    define: {
      __DATABASE_URL__: JSON.stringify(env.DATABASE_URL),
    },
    build: {
      minify: 'esbuild',
      sourcemap: true,
      rollupOptions: {
        output: {
          manualChunks(id) {
            if (id.includes('node_modules')) {
              return id.split('node_modules/')[1].split('/')[0]
            }
          },
        },
      },
    },
  }
})
```"

Planted mistakes (7): (1) `loadEnv(…, '')` loads ALL env vars; (2)
`envPrefix: ''` exposes all env vars to client code; (3) `define` inlines
`DATABASE_URL` — a server secret — into the client bundle; (4) `sourcemap:
true` ships original source to production; (5) one-chunk-per-package
`manualChunks` creates hundreds of tiny chunks; (6) `minify: 'esbuild'` is a
deprecated/legacy minifier choice; (7) `@vitejs/plugin-legacy` shipped by
default without evidence it's needed (~40% bundle bloat).

Rubric (one line per plant — pass = the problem is flagged with a correct
reason):
- flags `loadEnv` third arg `''` as loading all env vars including secrets
- flags `envPrefix: ''` as exposing every env var to the client
- flags the `define` of `DATABASE_URL` as baking a secret into the shipped
  bundle
- flags production `sourcemap: true` as leaking source (or requires the
  upload-then-delete error-tracker workflow)
- flags the per-package `manualChunks` heuristic as chunk explosion
- flags `minify: 'esbuild'` as deprecated/superseded (any coherent
  alternative accepted)
- flags default `plugin-legacy` as bloat to gate on real browser analytics
- no false positives: does not invent problems with `defineConfig`, the
  functional config form, or `react()` itself

## S3 — library mode + a secret in a VITE_ var

User message: "I'm publishing my TypeScript React hooks package to npm using
Vite. Give me the build config. Two more things: (a) consumers keep hitting
'two copies of React' errors with my current build, and (b) I want to put my
private analytics write key in `.env` as `VITE_ANALYTICS_SECRET` so the
built package can phone home — fine, right?"

Rubric:
- uses `build.lib` with an entry and explicit `formats`
- fixes (a) by externalizing react, react-dom, AND `react/jsx-runtime` in
  the bundler options, and connects that to the duplicate-React error
- states that library mode does not emit `.d.ts` types and prescribes
  `vite-plugin-dts` or a separate `tsc --emitDeclarationOnly`
- answers (b) with a clear NO: `VITE_`-prefixed vars are statically inlined
  into the shipped JS and extractable; minification/no-sourcemaps do not
  hide them
- prescribes the correct home for the secret: server-side (API/serverless),
  or drops the phone-home; any answer that keeps the secret in a `VITE_`
  var fails
- version consistency: bundler-options key (`rollupOptions` /
  `rolldownOptions`) matches the Vite major the answer commits to, used
  coherently throughout

## S4 — negative: should not trigger

User message: "My Vite + React app is running fine. Write me a
`useDebounce(value, delay)` hook in TypeScript with a short usage example."

Rubric:
- delivers the hook + usage example directly
- does not touch or recommend changes to `vite.config.ts`, plugins, env
  vars, or build settings (the word Vite appearing in prose is fine;
  unsolicited config work fails)
- no ceremony: no audit of the project's Vite setup, no checklist, no
  "while we're here" additions
