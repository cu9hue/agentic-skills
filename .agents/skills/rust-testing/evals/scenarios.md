# rust-testing — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. Deliverable-only replies;
anonymize; blind judge; log in `results.md`. Primary question: obsolescence
(execution AND attention).

## S1 — write tests

User message: "Write tests for this Rust function:

```rust
/// Parses an HTTP Retry-After header (delta-seconds form only).
/// Returns seconds clamped to `max_seconds`. Returns 0 for None/empty.
/// Errors on negative or non-numeric input.
pub fn parse_retry_after(header: Option<&str>, max_seconds: u32) -> Result<u32, ParseError> { ... }

#[derive(Debug, PartialEq)]
pub enum ParseError { Negative, NotANumber }
```
Just the tests."

Rubric:
- covers: happy path, clamp at/above max, zero, None, empty/whitespace,
  negative, non-numeric
- error cases assert the exact ParseError variant (assert_eq on Err or
  matches!) — not just is_err(), not #[should_panic]
- tests live in #[cfg(test)] mod tests (or are clearly marked as such)
- repetitive cases handled table-driven or as well-named separate tests —
  no copy-paste blur
- descriptive behavior names; tests independent, no shared mutable state

## S2 — review: planted violations

User message: "Review this Rust test code and list every problem:

```rust
use std::thread;
use std::time::Duration;

static mut CREATED_ID: u64 = 0;

#[test]
fn test_a() {
    let user = myapp::create_user("alice");
    unsafe { CREATED_ID = user.id; }
}

#[test]
fn test_b() {
    let id = unsafe { CREATED_ID };
    assert_eq!(myapp::get_user(id).name, "alice");
}

#[test]
fn test_upload() {
    myapp::upload("f.txt");
    thread::sleep(Duration::from_secs(2));
    assert_eq!(myapp::last_status(), "done");
}

#[test]
#[should_panic]
fn test_invalid_input() {
    myapp::parse("garbage").unwrap();
}

#[test]
fn test_report() {
    myapp::generate_report();
}

#[test]
#[ignore]
fn test_flaky_totals() {
    assert_eq!(myapp::total(), 100);
}
```"

Planted violations (7), rubric = one line per plant:
- static mut shared state + order dependence (test_a/test_b) — also UB
  risk, and Rust tests run in parallel by default so this races
- thread::sleep as async settling — flaky, slow
- #[should_panic] without expected = "..." — any panic passes, including
  the wrong one; better: assert the Err variant
- test with no assertion (test_report)
- #[ignore] with no reason/comment — permanently parked flaky test hiding
  a real bug
- tests hit real side effects (create_user/upload) with no
  isolation/fakes
- parallel-execution hazard called out explicitly (default multi-threaded
  test runner makes the shared state race, not just order-fragile)

## S3 — structural probe: underspecified ask

User message: "Our Rust service crate has almost no tests and I'm fixing
that starting Monday. What should I get right from the start?"

Rubric (pass = covered unprompted):
- unit vs integration split raised (#[cfg(test)] mods vs tests/ dir, what
  belongs where)
- isolation strategy for external deps raised (trait seams/fakes,
  wiremock/testcontainers — any coherent approach)
- CI discipline raised (cargo test + clippy/fmt gates on every push)
- edge-case rigor raised (error-path testing, property-based/proptest OR
  coverage tooling like llvm-cov as an enforced check)
- testing discipline is the organizing thread, not one bullet

## S4 — negative: should not trigger

User message: "Quick: how do I run just one test by name with cargo?"

Rubric:
- direct answer (`cargo test name_substring`, optionally -- --exact) in a
  sentence or two; no testing lecture or suite advice
