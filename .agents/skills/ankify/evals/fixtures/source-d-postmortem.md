# Reading notes — "How a 250ms timeout took down checkout for 43 minutes"

Postmortem write-up from the Plaid engineering blog, March 2024. Read because
it keeps getting cited in retry-storm discussions.

---

## The incident

At 14:07 UTC a routine deploy shipped a config change to the `ledger` service:
its downstream call timeout dropped from 2s to 250ms. The value was copied from
a template meant for the in-memory cache tier. `ledger` sits under `checkout`,
which sits under the public API gateway.

At 14:09 p99 latency on `ledger`'s database crossed 250ms — normal for that
hour's traffic. Calls started timing out. Each timeout triggered a retry.

## The mechanism — why it spread

The retry policy was 3 attempts at every layer: gateway retried `checkout`,
`checkout` retried `ledger`, `ledger` retried its database client. Three
layers of 3 attempts multiply: one user request could become 27 database
queries. The authors measured 21x amplification at peak — some requests
succeeded partway and stopped retrying.

This is the general shape of a retry storm: retries add load exactly when the
system has lost capacity. The database was slow because it was overloaded; the
retries made it more overloaded; more calls hit the timeout; more retries. The
feedback loop closed in about 90 seconds. By 14:11 the database was doing 19x
its normal query volume and `checkout` availability was 4%.

A dashboard existed that graphed retry rate per service, but nobody was paged
on it — the alert had been marked flaky and silenced in November 2023
(ticket INFRA-4102).

## Why it lasted 43 minutes

Rolling back the deploy at 14:23 did not fix it. The overload was
self-sustaining by then: every client that had timed out was retrying, and the
queue of retries alone was enough to keep the database saturated even with the
2s timeout restored. The system had two stable states — healthy and
retry-saturated — and removing the trigger did not move it out of the bad one.
The on-call had to shed load (drop 50% of gateway traffic for 6 minutes) to
let the queues drain. Full recovery at 14:50.

That is the second general lesson the authors draw: past a threshold, a retry
storm is self-sustaining, so recovery needs active load shedding, not just
reverting the cause. They call the two-stable-states framing "metastable
failure" and cite the Bronson et al. HotOS '21 paper that named it.

## What they changed

The fix is not "never retry". Retries at one layer are how you ride out
transient blips. The policy they landed on:

- Exactly one layer owns retries for a given call path — they chose the
  gateway, the outermost layer, because it can see end-to-end success. Inner
  layers get 1 attempt, no retries.
- A retry budget instead of a per-request count: retries may be at most 10% of
  a service's request volume. Under 10%, behavior is unchanged; past it,
  retries stop entirely rather than compounding the overload.
- Jitter on every retry so synchronized clients do not stampede in lockstep.

Remediation items shipped over Q2: the retry budget in the shared client
library (INFRA-4188), un-silencing the retry-rate alert with a saner
threshold (INFRA-4190), and a config linter that flags timeout values below
the target's p99 (INFRA-4201).

## Aside

The write-up ends with a plug for their chaos-testing setup, which injects
latency into staging weekly. Fine, but nothing new there.
