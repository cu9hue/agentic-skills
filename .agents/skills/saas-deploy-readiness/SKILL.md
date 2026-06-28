---
name: saas-deploy-readiness
description: Use when setting up staging/production, configuring deployment secrets, planning or running database migrations, diagnosing failed deploys, planning a rollback, hardening server-action error handling, or checking auth/email/payment webhooks. Tuned for a Next.js + Vercel + Supabase + Stripe + Resend + GitHub Actions + Drizzle stack.
origin: distilled from real deployment incidents on a Next.js/Vercel/Supabase/Stripe/Resend stack; migration and rollback patterns adapted from ECC (github.com/affaan-m/everything-claude-code)
---

# SaaS Deploy Readiness

Make deployment boring: separate environments, explicit secrets, reproducible
deploys, reversible schema changes, safe errors, and smoke tests that exercise
real user flows. This skill assumes one stack: Next.js on Vercel, Supabase
Postgres, Stripe, Resend, GitHub Actions, Drizzle. It is opinionated on purpose.

## Core Rules

- Treat staging as a real environment, not a branch name. It needs its own app
  URL, auth redirect URLs, database/storage boundary, Stripe mode, webhook
  endpoints, email sender behavior, and secrets.
- **Classify every environment variable before deploying**, because where it must
  live depends on the class:
  - **Build-time**: read while compiling or bundling, especially `NEXT_PUBLIC_*`.
    For prebuilt CI deploys these must be in the CI secret store, not only in
    Vercel. Vercel runtime env (especially "sensitive" vars) may be unreadable
    during a CI build.
  - **Runtime**: read by server functions after deploy (DB URL, service keys, API
    secrets, webhook signing secrets, HMAC secrets).
  - **Both**: read during the build and at runtime; put it in both stores.
- A green local build proves nothing about deployed runtime env. Add a CI
  preflight that fails on missing or blank required secrets, and read runtime
  logs after the first deploy.
- Use the Supabase **transaction pooler** URL from serverless, not the direct
  database host. The direct host causes DNS/IPv6/pooling failures on Vercel.
- Keep public URLs consistent across app, auth, Stripe, webhooks, and emails.
  Mismatched domains cause failures that look unrelated.
- Obscure staging names are not access control. Use Stripe test mode, Resend
  test behavior, and Vercel deployment protection for real gating.
- Keep DNS ownership separate from hosting when useful. Cloudflare can stay DNS
  owner with DNS-only records pointing app subdomains at Vercel.

## Deployment Checklist

1. Identify environments: `local`, `staging`, `production`.
2. Decide deployment topology:
   - Vercel Git integration: verify comments/statuses/access are acceptable.
   - CI + CLI/prebuilt deploys: duplicate build-time secrets into CI (see Core
     Rules for the env-var classes).
   - If production is not ready, prevent automatic production deploys.
3. Configure external services with the exact deployed URLs:
   - Supabase auth site URL and redirect URLs.
   - Stripe webhook endpoints and signing secrets (the signing secret is not the
     API secret key).
   - Resend sender domain and from address.
   - Cron auth secret and endpoint URL.
4. Validate before deploy: CI fails early on missing secrets; typecheck and tests
   pass; build logs show the intended environment.
5. Smoke test after deploy: open the app URL, sign up/in, complete onboarding,
   run the core paid workflow in Stripe test mode, trigger or verify webhooks,
   confirm emails, links, redirects, and cron protection.

## Database Migrations (Drizzle + Supabase Postgres)

Schema changes are the highest-risk part of a deploy. Code rolls back in seconds;
a migration does not. Make every migration safe to run while the old code is
still live.

- Generate and commit migrations. Never `drizzle-kit push` against staging or
  production: push has no migration file and no history. Use it only in local dev.
- `drizzle-kit generate` writes the SQL; `drizzle-kit migrate` applies it. Run
  migrate as an explicit CI deploy step, not from app startup.
- Migrations are forward-only in production. To undo, write a new forward
  migration; never edit one that has already run.
- Keep schema (DDL) and data backfill (DML) in separate migrations.
- Follow standard safe-DDL on a populated table: add columns nullable or
  defaulted, build indexes concurrently, backfill in batches. Drizzle needs a
  raw migration for `CREATE INDEX CONCURRENTLY`.

Renaming or dropping a column (expand-contract, never in one step):

1. **Expand:** add the new column; deploy code that writes both old and new.
2. **Migrate:** backfill the old data; deploy code that reads new, still writes
   both.
3. **Contract:** deploy code that uses only new; drop the old column in a later
   migration.

This ordering is also what makes code rollback safe: at every step the previous
deploy still works against the current schema.

## Rollback

Two independent rollbacks. Know both before you ship.

- **Code:** `vercel rollback`, or promote the previous deployment in the
  dashboard, returns to the last good build instantly. This is the default escape
  hatch.
- **Database:** there is no instant DB rollback. Safety comes from
  backward-compatible migrations (expand-contract above), so rolling back code
  never requires touching the schema.
- **Features:** gate risky changes behind a flag so you can disable them without a
  deploy or a rollback.

Before deploying anything risky, confirm:

- the previous Vercel deployment is still available to promote
- the migration in this deploy is backward-compatible with the previous code
- a smoke test exists that tells you fast when a rollback is needed
- you have tested the rollback path in staging, not just the forward path

## Error-Handling Standard

For every user-facing client handler that awaits a server action or network
request:

```ts
setBusy(true);
setError(null);
try {
  const result = await action();
  if (!result.ok) setError(result.error);
} catch {
  setError("We couldn't complete that action right now. Please try again in a few minutes.");
} finally {
  setBusy(false);
}
```

For server actions that touch DB/auth/payments/email/storage:

- Catch expected provider failures and return safe user messages.
- Log structured event names with diagnostic metadata, not secrets.
- Preserve intentional redirects.
- Do not expose raw provider/database errors to users.
- Avoid top-level imports that throw on missing runtime env when a friendly
  action error is possible; import lazily or validate inside the action path.

## Common Failure Patterns

- `NEXT_PUBLIC_*` missing from CI: client bundle lacks auth/captcha/app URL
  values even when Vercel runtime env is set.
- Sensitive Vercel env vars not readable by CI: prebuilt builds fail or receive
  blank values.
- Direct Supabase host used from serverless: DNS/IPv6/pooling failures; switch to
  the transaction pooler.
- Auth/captcha mismatch: form submits but the provider rejects the token; check
  the site key in build env and the secret key in the auth provider.
- Webhook secret confusion: Stripe API secret keys and webhook signing secrets
  are different values.
- Commit attribution gates: Vercel may inspect git author metadata even for CLI
  deploys; ensure the commit email is verified/linked if needed.
- Server action throws in production: the browser sees a generic digest and the
  UI hangs unless the client uses `try/finally`.
- `NOT NULL` column added without a default: migration locks and rewrites the
  whole table on first deploy.

## Deployment Incident Review

After any deploy failure, capture:

- Failing step: dependency install, env pull, build, deploy, runtime request,
  webhook, migration.
- Exact error message and where it came from: CI, Vercel build logs, runtime
  logs, browser console, Supabase/Stripe dashboard.
- Env var class involved: build-time, runtime, or both.
- Fix applied.
- New rule/check to prevent recurrence.

Turn recurring fixes into a CI preflight, a test, or a checklist item above.
