# rust-patterns — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. The subagent returns only the
deliverable. Anonymize outputs into teams, blind-judge against the rubrics,
log the verdict in `results.md`.

## S1 — write: sessions module for a library crate

User message: "For a Rust library crate, write a `sessions` module. Sessions
have a session id and a user id (both u64 under the hood) and a state: active
with an expiry timestamp (u64 unix seconds), or revoked with a reason string.
Provide an in-memory `SessionStore` with operations to create a session, look
one up, revoke one, and list the ids of all currently active sessions (given a
`now` timestamp). Looking up a missing session and revoking an already-revoked
session are errors. Just the code."

Rubric:
- errors are a structured typed enum (thiserror-style or hand-implemented),
  NOT anyhow, NOT `Box<dyn Error>`, and no panicking on the two error cases
- zero `unwrap()`/`expect()` outside `#[cfg(test)]` code
- session state is an enum with data-carrying variants (Active { expiry },
  Revoked { reason }), not booleans or parallel Option fields
- session id and user id are wrapped in newtypes, not passed as bare u64
- listing active sessions uses an iterator chain (filter/filter_map + collect),
  not a manual push-loop
- helpers and struct internals are private or `pub(crate)`; only the intended
  API surface is `pub`

## S2 — review: planted violations

User message: "Review this module from our Rust library crate `jobqueue` and
list the problems you find:

```rust
use std::collections::HashMap;
use std::time::Duration;

pub enum JobState {
    Queued,
    Running,
    Done,
    Failed,
}

pub struct JobStore {
    pub jobs: HashMap<u64, JobState>,
}

pub fn describe(state: &JobState) -> &'static str {
    match state {
        JobState::Queued => "queued",
        JobState::Running => "running",
        _ => "finished",
    }
}

pub fn parse_job_id(input: String) -> Result<u64, Box<dyn std::error::Error>> {
    let id = input.trim().parse::<u64>()?;
    Ok(id)
}

pub fn first_running(store: &JobStore) -> u64 {
    let mut ids = Vec::new();
    for (id, state) in &store.jobs {
        if matches!(state, JobState::Running) {
            ids.push(*id);
        }
    }
    *ids.first().unwrap()
}

pub fn count_long_labels(labels: &Vec<String>) -> usize {
    let copy = labels.clone();
    copy.iter().filter(|l| l.len() > 8).count()
}

pub fn peek(bytes: &[u8], idx: usize) -> u8 {
    unsafe { *bytes.get_unchecked(idx) }
}

pub async fn poll_until_done(store: &JobStore, id: u64) {
    loop {
        if matches!(store.jobs.get(&id), Some(JobState::Done)) {
            return;
        }
        std::thread::sleep(Duration::from_millis(500));
    }
}
```"

Planted violations (8): wildcard `_` arm collapsing Done/Failed on a business
enum; `String` parameter where `&str` suffices; `Box<dyn Error>` return in a
library (should be a typed error); manual push-loop instead of an iterator
chain; `unwrap()` on possibly-empty result in production code; needless
`.clone()` of the labels vec (and `&Vec<String>` instead of `&[String]`);
`unsafe get_unchecked` with no SAFETY comment and no bounds proof; blocking
`std::thread::sleep` inside an `async fn`.

Rubric (one line per plant — pass = the review flags it):
- flags the wildcard `_` arm in `describe` as hiding variants of a business
  enum (Done vs Failed collapsed / future variants silently absorbed)
- flags `parse_job_id` taking `String` instead of `&str`
- flags `Box<dyn Error>` as wrong for a library API (recommends a typed /
  thiserror-style error)
- flags the manual accumulation loop in `first_running` as an iterator-chain
  candidate (find/filter)
- flags the `unwrap()` in `first_running` as a panic when no job is running
  (should return Option/Result)
- flags the needless `.clone()` in `count_long_labels` (and/or the
  `&Vec<String>` parameter type)
- flags the `unsafe` block in `peek` as unjustified: missing SAFETY comment
  and/or no bounds guarantee (plain indexing or `get` suffices)
- flags `std::thread::sleep` in `poll_until_done` as blocking the async
  executor (should be `tokio::time::sleep(...).await`)

## S3 — refactor: nested matching and manual loops

User message: "Refactor this Rust code to be more idiomatic. Keep the
behavior identical. Just the refactored code.

```rust
struct Profile { email: Option<String> }
struct User { profile: Option<Profile> }

fn primary_email_domain(user: &User) -> Option<String> {
    match user.profile.as_ref() {
        Some(profile) => match profile.email.as_ref() {
            Some(email) => match email.split('@').nth(1) {
                Some(domain) => Some(domain.to_string()),
                None => None,
            },
            None => None,
        },
        None => None,
    }
}

fn collect_domains(users: &Vec<User>) -> Vec<String> {
    let mut result = Vec::new();
    for user in users {
        let d = primary_email_domain(user);
        if d.is_some() {
            result.push(d.unwrap());
        }
    }
    result
}
```"

Rubric:
- nested triple match replaced with a combinator chain (`as_ref`/`and_then`/
  `map`) or `?` on Options — no nested `match` ladders remain
- the `is_some()` + `unwrap()` pair is eliminated (via `filter_map`,
  `flatten`, or `if let`); zero `unwrap()` in the result
- manual push-loop in `collect_domains` replaced with an iterator chain
  ending in `collect()`
- parameter loosened from `&Vec<User>` to `&[User]`
- behavior preserved: same return types (`Option<String>`, `Vec<String>`),
  domain still the part after '@'

## S4 — negative: should not trigger

User message: "Quick question: should I commit Cargo.lock for a Rust library
crate, or only for binaries? Short answer please."

Rubric:
- answers the question directly and concisely (a few sentences)
- no unsolicited idiom checklist, pattern review, code samples of unrelated
  patterns, or module-structure ceremony — behaves as if the skill were
  absent
