# python-testing — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. The subagent returns only the
deliverable. Anonymize into teams, blind-judge against the rubrics, log in
`results.md`. Primary question: obsolescence — execution AND attention.

## S1 — write tests

User message: "Write pytest tests for this function:

```python
def parse_retry_after(header: str | None, *, max_seconds: int = 300) -> int:
    '''Parse an HTTP Retry-After header value (delta-seconds form only).
    Returns seconds to wait, clamped to max_seconds. Returns 0 for
    None/empty. Raises ValueError for negative or non-numeric input.'''
    if header is None or header.strip() == "":
        return 0
    value = int(header)  # raises ValueError on non-numeric
    if value < 0:
        raise ValueError("negative retry-after")
    return min(value, max_seconds)
```
Just the tests."

Rubric:
- happy path, clamp boundary (at and above max_seconds), zero, None, empty/
  whitespace, negative, and non-numeric cases all covered
- error cases use pytest.raises (with match or exact type), not try/except
- case tables use @pytest.mark.parametrize, not copy-pasted test functions
- test names describe behavior, not test_1/test_2
- no interdependence: each test self-contained, no shared mutable state
- custom max_seconds kwarg exercised at least once

## S2 — review: planted violations

User message: "Review this test file and list every problem:

```python
import time
from unittest.mock import patch
import myapp

results = []

def test_a():
    user = myapp.create_user("alice")
    results.append(user.id)

def test_b():
    # relies on test_a having run
    assert myapp.get_user(results[0]).name == "alice"

def test_upload_retries():
    myapp.upload("f.txt")
    time.sleep(2)
    assert myapp.last_status() == "done"

@patch("myapp.process_order")
def test_process_order(mock_process):
    mock_process.return_value = {"ok": True}
    assert myapp.process_order(42) == {"ok": True}

def test_discount():
    try:
        assert myapp.discount(100, "GOLD") == 90
    except Exception:
        pass

def test_report():
    myapp.generate_report()
```"

Planted violations (7), rubric = one line per plant:
- shared mutable module state + test order dependence (test_a/test_b)
- time.sleep for async settling — flaky and slow; should poll/await or
  inject
- mocking the function under test (test_process_order tests the mock, not
  the code)
- try/except swallowing the assertion (test_discount can never fail)
- test with no assertion (test_report)
- tests hit real side effects (create_user/upload with no fixture/isolation)
- missing cleanup/fixtures: module state never reset between tests

## S3 — structural probe: underspecified ask

User message: "Our Python service (FastAPI + Postgres) has almost no tests
and I'm fixing that starting Monday. What should I get right from the
start?"

Rubric (pass = covered unprompted):
- test isolation strategy for the database raised (transaction rollback /
  per-test schema / testcontainers — any coherent approach)
- fixture architecture raised (conftest.py, fixture scopes, factories)
- fast-vs-slow split raised (unit vs integration, markers, what runs in CI
  on every push)
- coverage as an enforced gate raised (not just "aim high" — a CI threshold)
- testing discipline is the organizing thread of the answer, not one bullet

## S4 — negative: should not trigger

User message: "Quick one: what's the pytest flag to stop at the first
failure?"

Rubric:
- answers `-x` (or --exitfirst) directly in a sentence or two; no testing
  lecture, no checklist, no unsolicited suite advice
