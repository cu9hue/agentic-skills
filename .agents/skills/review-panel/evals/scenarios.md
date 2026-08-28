# review-panel — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. Every arm is told to invoke no
skill of its own, so arm A is a true baseline and arm B sees only this skill.
The repo under review does not exist on disk: each scenario inlines the diff
and states the repo facts, and the arm is told to work from those alone — no
reading files, no git. Arm B may dispatch subagents; they get the same inlined
material. The arm returns exactly the deliverable — the review report or reply
it would send — and no meta-commentary. Anonymize outputs into teams,
blind-judge against the rubrics, log in `results.md`.

## Shared material — the export-report diff (S1, S5)

Repo facts stated to the arm: a Flask app served by gunicorn with threaded
workers. The codebase already has `app/http.py:fetch_json(url, timeout=5,
retries=2)` for outbound HTTP and `app/observability.py:log_error(exc,
**context)` for error reporting; both are used everywhere else. Accounts can
have zero usage events. The diff is the whole change on the branch.

```diff
diff --git a/app/export.py b/app/export.py
new file mode 100644
--- /dev/null
+++ b/app/export.py
@@ -0,0 +1,38 @@
+import requests
+from datetime import datetime
+
+from app.db import get_session
+from app.models import UsageEvent
+
+RATES_URL = "https://api.exchangerate.host/latest?base=USD"
+
+_rates_cache = {}
+
+
+def _get_rates():
+    if "rates" not in _rates_cache:
+        resp = requests.get(RATES_URL)
+        _rates_cache["rates"] = resp.json()["rates"]
+    return _rates_cache["rates"]
+
+
+def build_report(account_id, currency):
+    session = get_session()
+    events = session.query(UsageEvent).filter_by(account_id=account_id).all()
+    rates = _get_rates()
+    rows = []
+    for e in events:
+        rows.append({
+            "sku": e.sku,
+            "amount": round(e.amount_usd * rates[currency], 2),
+            "day": e.created_at.strftime("%Y-%m-%d"),
+        })
+    total = sum(r["amount"] for r in rows)
+    avg = total / len(rows)
+    return {
+        "generated_at": datetime.utcnow().isoformat(),
+        "rows": rows,
+        "total": total,
+        "avg_per_event": avg,
+    }
diff --git a/app/routes.py b/app/routes.py
--- a/app/routes.py
+++ b/app/routes.py
@@ -41,6 +41,15 @@
+@app.route("/accounts/<account_id>/report")
+def report(account_id):
+    currency = request.args.get("currency", "USD")
+    try:
+        data = build_report(account_id, currency)
+    except Exception:
+        return jsonify({"error": "internal error"}), 500
+    return jsonify(data)
```

Planted issues, by angle (for the judge, never shown to arms):

1. Data race: check-then-act on `_rates_cache` under threaded workers.
2. Edge case: `total / len(rows)` raises ZeroDivisionError for an account
   with zero events; `rates[currency]` raises KeyError on unknown
   user-supplied currency.
3. Production readiness: `requests.get` has no timeout and no
   `raise_for_status`; the route swallows every exception with no logging.
4. Patterns: ignores the existing `fetch_json` and `log_error` helpers.
5. External API: exchangerate.host's free keyless endpoint was discontinued
   (requires an access key since mid-2023); `datetime.utcnow()` is
   deprecated since Python 3.12.
6. Scalability: `.all()` loads every event into memory and the response is
   unbounded; the rates cache never refreshes (stale forever).
7. Domain: per-row `round(..., 2)` then summing accumulates rounding drift
   against the true total — currency-conversion convention worth a question.

## S1 — multi-angle execution

User message: "Review this change before I open the PR." followed by the
shared repo facts and diff.

Rubric:
- finds the `_rates_cache` check-then-act race and ties it to the threaded
  workers, not generic "consider thread safety" hedging
- finds the ZeroDivisionError on zero events and the KeyError on an unknown
  `currency` value
- flags the missing timeout AND the silently-swallowed exception with no
  logging
- flags the unused `fetch_json` / `log_error` helpers as a pattern violation
- questions the external API itself (keyless exchangerate.host endpoint dead
  or unverified) rather than only how it is called
- flags unbounded memory (`.all()` / unbounded response) or the
  never-refreshed cache
- findings are ranked by severity, not grouped file-by-file
- no fabricated findings (nothing claimed about code not in the diff)

## S2 — verification kills the noise

User message: "Review this retry helper and parser registry before I merge."
Repo facts stated to the arm: the module is imported once at startup, before
the thread pool starts; callers of `fetch_with_retry` treat its result as a
parsed JSON dict.

```diff
diff --git a/app/ingest.py b/app/ingest.py
new file mode 100644
--- /dev/null
+++ b/app/ingest.py
@@ -0,0 +1,30 @@
+import time
+import requests
+from concurrent.futures import ThreadPoolExecutor
+
+from app.parsers import CsvParser, JsonParser
+
+_PARSERS = {}
+
+
+def _register(name, cls):
+    _PARSERS[name] = cls
+
+
+_register("csv", CsvParser)
+_register("json", JsonParser)
+
+
+def fetch_with_retry(url, attempts=3):
+    for i in range(attempts):
+        try:
+            resp = requests.get(url, timeout=5)
+            resp.raise_for_status()
+            return resp.json()
+        except requests.RequestException:
+            time.sleep(2 ** i)
+
+
+def ingest_all(urls, kind):
+    parser = _PARSERS[kind]()
+    with ThreadPoolExecutor(max_workers=8) as pool:
+        payloads = list(pool.map(fetch_with_retry, urls))
+    return [parser.parse(p) for p in payloads]
```

Planted (for the judge): the real bug is `fetch_with_retry` falling off the
loop after the last failed attempt and returning `None`, which callers index
into. Two traps for a noisy reviewer: `_PARSERS` is written only at import
time before any thread exists (not a race), and `pool.map` collects results
in the calling thread (no shared mutable state, not a race).

Rubric:
- reports the silent `None` return after exhausted retries as the top finding
- does not report `_PARSERS` as a data race; a pass mentions it only to say
  it is safe
- does not report the `ThreadPoolExecutor` usage as a data race
- every reported finding cites the specific lines that make it real; no
  finding rests on "might" or "consider" without a concrete failure path
- the sleep after the final attempt (wasted delay before returning None) is
  bonus credit, not required

## S3 — domain adequacy asks instead of assuming

User message: "Review this proration helper." Repo facts stated to the arm:
this computes the charge when a customer upgrades mid-cycle; billing runs
monthly.

```diff
diff --git a/billing/prorate.py b/billing/prorate.py
new file mode 100644
--- /dev/null
+++ b/billing/prorate.py
@@ -0,0 +1,6 @@
+def prorate(monthly_price_cents, start_date, end_date):
+    days = (end_date - start_date).days
+    return int(monthly_price_cents * days / 30)
+
```

Rubric:
- asks the user at least one genuine domain question instead of silently
  assuming a convention — e.g. fixed 30-day month vs. actual month length,
  whether `end_date` is inclusive, who is the rounding beneficiary
- flags `int()` truncation of money as a finding, not a question
- flags that `end_date < start_date` produces a negative charge
- does not invent a billing convention and present it as the correct one

## S4 — structural probe: underspecified ask

User message: "I've got a big backend change landing this week. What should I
get right before it merges?"

Rubric:
- the answer is organized as a multi-angle review, not a generic pre-merge
  checklist (commit hygiene, changelog, reviewer etiquette)
- at least four of these appear unprompted: data races / concurrency, error
  handling and graceful degradation, edge cases, conformance with existing
  codebase patterns, external API currency and correct usage, operational
  gaps (rollout, monitoring, limits), scalability
- verification appears: the answer says findings should be checked against
  the code, or distinguishes confirmed problems from hypotheses

## S5 — negative: summarize, don't review

User message: "Summarize what this diff changes so I can write the changelog
entry." followed by the shared export-report diff (no repo facts).

Rubric:
- returns a short factual summary of what changed
- does not review: no findings list, no severity ranking, no subagents, no
  angle-by-angle analysis
- does not lecture about problems in the code beyond, at most, one passing
  sentence
