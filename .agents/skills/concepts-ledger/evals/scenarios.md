# concepts-ledger — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. Every arm is told to invoke no
skill of its own, so arm A is a true baseline and arm B sees only this skill.
The subagent returns exactly the deliverable — the reply it would send, with
any files inline — and no meta-commentary. Anonymize outputs into teams,
blind-judge against the rubrics, log in `results.md`.

## Shared material — the `ingest` codebase

A small Python project. The subagent gets these files inline.

```python
# ingest/pipeline.py
from .stage import Stage, StageResult
from .store import Document

class Pipeline:
    """Runs an ordered list of stages over one document."""
    def __init__(self, stages: list[Stage]) -> None:
        self.stages = stages

    def run(self, doc: Document) -> StageResult:
        warnings: list[str] = []
        for stage in self.stages:
            result = stage.apply(doc)
            doc = result.doc
            warnings.extend(result.warnings)
        return StageResult(doc=doc, warnings=warnings)
```

```python
# ingest/stage.py
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from .store import Document

@dataclass
class StageResult:
    doc: Document
    warnings: list[str] = field(default_factory=list)

class Stage(ABC):
    """One transformation in a Pipeline. Stateless; apply() must not mutate its input."""
    @abstractmethod
    def apply(self, doc: Document) -> StageResult: ...
```

```python
# ingest/stages/normalize.py
from ..stage import Stage, StageResult
from ..store import Document

class NormalizeStage(Stage):
    def apply(self, doc: Document) -> StageResult:
        text = " ".join(doc.text.split())
        return StageResult(doc=Document(id=doc.id, text=text))
```

```python
# ingest/stages/dedupe.py
from ..stage import Stage, StageResult
from ..store import Document, DocumentStore
from ..fingerprint import Fingerprint

class DedupeStage(Stage):
    def __init__(self, store: DocumentStore) -> None:
        self.store = store

    def apply(self, doc: Document) -> StageResult:
        fp = Fingerprint.of(doc.text)
        if self.store.has_fingerprint(fp):
            return StageResult(doc=doc, warnings=[f"duplicate of {fp}"])
        return StageResult(doc=doc)
```

```python
# ingest/fingerprint.py
import hashlib

class Fingerprint:
    """Content identity for a document. Two documents with equal
    fingerprints are the same document for dedupe purposes, even if
    their ids differ."""
    def __init__(self, digest: str) -> None:
        self.digest = digest

    @classmethod
    def of(cls, text: str) -> "Fingerprint":
        return cls(hashlib.sha256(text.encode()).hexdigest()[:16])

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Fingerprint) and other.digest == self.digest

    def __hash__(self) -> int:
        return hash(self.digest)

    def __str__(self) -> str:
        return self.digest
```

```python
# ingest/store.py
import sqlite3
from dataclasses import dataclass
from .fingerprint import Fingerprint

@dataclass(frozen=True)
class Document:
    id: str
    text: str

class DocumentStore:
    """Owns the sqlite file. The only place that reads or writes documents."""
    def __init__(self, path: str) -> None:
        self.conn = sqlite3.connect(path)

    def put(self, doc: Document) -> None:
        fp = str(Fingerprint.of(doc.text))
        self.conn.execute("INSERT OR REPLACE INTO docs VALUES (?, ?, ?)", (doc.id, doc.text, fp))
        self.conn.commit()

    def get(self, id: str) -> Document | None:
        row = self.conn.execute("SELECT id, text FROM docs WHERE id = ?", (id,)).fetchone()
        return Document(*row) if row else None

    def has_fingerprint(self, fp: Fingerprint) -> bool:
        return self.conn.execute("SELECT 1 FROM docs WHERE fp = ?", (str(fp),)).fetchone() is not None
```

```python
# ingest/settings.py
from dataclasses import dataclass

@dataclass
class Settings:
    db_path: str = "ingest.db"
    batch_size: int = 100
```

```python
# ingest/util.py
from itertools import islice

def chunked(iterable, n):
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch
```

```python
# ingest/cli.py
import argparse, sys
from .pipeline import Pipeline
from .settings import Settings
from .stages.normalize import NormalizeStage
from .stages.dedupe import DedupeStage
from .store import Document, DocumentStore
from .util import chunked

def parse_args(argv):
    p = argparse.ArgumentParser()
    p.add_argument("files", nargs="+")
    return p.parse_args(argv)

def main(argv=None):
    args = parse_args(argv or sys.argv[1:])
    settings = Settings()
    store = DocumentStore(settings.db_path)
    pipeline = Pipeline([NormalizeStage(), DedupeStage(store)])
    for batch in chunked(args.files, settings.batch_size):
        for path in batch:
            doc = Document(id=path, text=open(path).read())
            result = pipeline.run(doc)
            for w in result.warnings:
                print(w, file=sys.stderr)
            store.put(result.doc)
```

The named abstractions here are `Pipeline`, `Stage` (with `NormalizeStage`
and `DedupeStage` as its implementations), `Document`, `DocumentStore`, and
`Fingerprint`. `StageResult` only bundles a return value. `Settings` only
holds config. `chunked`, `parse_args`, and `main` are functions.

## S1 — set up the ledger on an existing codebase

User message: "Set up a concepts ledger for this codebase so I can see what
it's made of without reading everything."

The subagent gets the shared material and no existing `docs/` folder.

Rubric:
- writes one file at `docs/concepts.md`, and nothing else (no per-module
  files, no extra README section)
- has an entry for each of `Pipeline`, `Stage`, `Document`, `DocumentStore`,
  `Fingerprint`; `NormalizeStage` and `DedupeStage` appear either as their own
  entries or named inside the `Stage` entry
- has no entry for `StageResult`, `Settings`, `chunked`, `parse_args`, or
  `main`
- every entry says what the thing is, what it owns or is responsible for,
  where it lives (a file path), and which other concepts it depends on
- entries are in one flat alphabetical list, with no sections per module or
  layer
- no entry narrates why the concept exists or how it came to be
- the whole file fits on one screen for a codebase this size (roughly 40
  lines or fewer)

## S2 — update the ledger from a branch diff

User message: "Update the concepts ledger for this branch."

The subagent gets the shared material, the ledger below as the current
`docs/concepts.md`, and the diff summary below as `git diff main...HEAD`.

Current `docs/concepts.md`:

```markdown
# Concepts

One entry per named abstraction the code thinks in terms of. Alphabetical.

## Document
What: an immutable id-plus-text record, the unit every stage operates on.
Owns: nothing. Frozen dataclass.
Where: `ingest/store.py`
Depends on: —

## DocumentStore
What: the persistence layer for documents.
Owns: the sqlite connection; the only code that reads or writes the docs table.
Where: `ingest/store.py`
Depends on: Document, Fingerprint

## Fingerprint
What: content identity for a document; equal fingerprints mean the same document for dedupe.
Owns: the hashing rule (sha256, first 16 hex chars).
Where: `ingest/fingerprint.py`
Depends on: —

## Pipeline
What: an ordered list of stages run over one document.
Owns: stage ordering and warning collection.
Where: `ingest/pipeline.py`
Depends on: Stage, Document

## Stage
What: one stateless transformation of a document. Implementations: NormalizeStage, DedupeStage.
Owns: nothing; `apply()` must not mutate its input.
Where: `ingest/stage.py`, `ingest/stages/`
Depends on: Document
```

Branch diff, summarized:

- Adds `ingest/indexer.py` with `class Indexer`: owns the full-text index,
  exposes `add(doc)` and `search(query) -> list[Document]`, holds an open
  `sqlite3` FTS table, and is the only code that writes to it.
- Adds `@dataclass IndexStats(count: int, elapsed_s: float)` in the same
  file, returned by `Indexer.rebuild()`.
- Renames `DocumentStore` to `Repository` everywhere (`ingest/store.py` is
  now `ingest/repository.py`); behaviour unchanged.
- Deletes `ingest/fingerprint.py`. `DedupeStage` and `Repository` now call
  `hashlib.sha256(text.encode()).hexdigest()[:16]` inline.
- Adds `def retry(fn, attempts=3)` to `ingest/util.py`.
- `Pipeline` untouched.

Rubric:
- adds an `Indexer` entry with what, owns, where, depends on
- adds no entry for `IndexStats` or `retry`
- replaces the `DocumentStore` entry with a `Repository` entry at the new
  path, and does not keep both
- removes the `Fingerprint` entry, and drops `Fingerprint` from the
  `Repository` entry's depends-on line
- leaves the `Pipeline` and `Stage` entries byte-for-byte unchanged, and
  changes only the path line of `Document` (its file was renamed)
- keeps the file one flat alphabetical list; `Indexer` lands between
  `Document` and `Pipeline`
- adds no narrative about why Fingerprint was removed or why Indexer was
  added

## S3 — structural probe: underspecified ask

User message: "I'm about to hand this codebase to a coding agent for a few
weeks of feature work. I want to still understand what's in it at the end.
What should I get right?"

The subagent gets the shared material.

Rubric:
- proposes a single short written inventory of the codebase's named
  abstractions as the central answer, not a list of generic agent-hygiene
  tips (good prompts, tests, small PRs, code review)
- states a threshold for what gets an entry — abstractions with their own
  identity or behaviour, not every class or data holder
- says the inventory gets updated as part of each change and that its diff
  is what the user reviews in the PR
- says the inventory is a brake on new abstractions: an entry added is an
  abstraction the user gets to question

## S4 — negative: a nearby documentation request

User message: "Add a docstring to `DedupeStage` that explains what it does."

The subagent gets the shared material.

Rubric:
- writes the docstring and stops
- creates no `docs/concepts.md`, proposes no ledger, and adds no trailing
  advice about tracking concepts

## S5 — set up the ledger on a Rust crate

User message: "Set up a concepts ledger for this crate."

The subagent gets the `jobq` crate below and no existing `docs/` folder.

```rust
// src/lib.rs
pub mod backend;
pub mod job;
pub mod scheduler;
pub mod state;
pub mod util;

pub type Result<T> = std::result::Result<T, backend::BackendError>;
```

```rust
// src/job.rs
#[derive(Clone, Copy, Debug, PartialEq, Eq, Hash)]
pub struct JobId(pub u64);

/// One unit of work. Owns its retry count; the scheduler never edits it directly.
#[derive(Clone, Debug)]
pub struct Job {
    pub id: JobId,
    pub payload: Vec<u8>,
    attempts: u32,
}

impl Job {
    pub fn new(id: JobId, payload: Vec<u8>) -> Self {
        Self { id, payload, attempts: 0 }
    }
    pub fn attempts(&self) -> u32 {
        self.attempts
    }
    /// Returns a copy with one more attempt recorded. The original is unchanged.
    pub fn retried(&self) -> Self {
        Self { attempts: self.attempts + 1, ..self.clone() }
    }
}
```

```rust
// src/state.rs
use std::time::Instant;

#[derive(Clone, Debug)]
pub enum Event {
    Start,
    Succeed,
    Fail(String),
}

/// Lifecycle of one job. Only `transition` may move between variants.
#[derive(Clone, Debug)]
pub enum JobState {
    Queued,
    Running { since: Instant },
    Done,
    Failed { reason: String },
}

#[derive(Debug)]
pub struct TransitionError(pub &'static str);

impl JobState {
    pub fn is_terminal(&self) -> bool {
        matches!(self, JobState::Done | JobState::Failed { .. })
    }

    pub fn transition(self, event: Event) -> std::result::Result<JobState, TransitionError> {
        use JobState::*;
        match (self, event) {
            (Queued, Event::Start) => Ok(Running { since: Instant::now() }),
            (Running { .. }, Event::Succeed) => Ok(Done),
            (Running { .. }, Event::Fail(reason)) => Ok(Failed { reason }),
            (s, _) if s.is_terminal() => Err(TransitionError("job already finished")),
            _ => Err(TransitionError("event not valid in this state")),
        }
    }
}
```

```rust
// src/backend.rs
use crate::job::Job;
use std::collections::VecDeque;

#[derive(Debug)]
pub enum BackendError {
    Full,
    Io(String),
}

/// Where jobs wait. Implementations own durability; the scheduler owns ordering.
pub trait Backend {
    fn push(&mut self, job: Job) -> crate::Result<()>;
    fn pop(&mut self) -> Option<Job>;
    fn len(&self) -> usize;
}

#[derive(Default)]
pub struct MemoryBackend {
    queue: VecDeque<Job>,
}

impl Backend for MemoryBackend {
    fn push(&mut self, job: Job) -> crate::Result<()> {
        self.queue.push_back(job);
        Ok(())
    }
    fn pop(&mut self) -> Option<Job> {
        self.queue.pop_front()
    }
    fn len(&self) -> usize {
        self.queue.len()
    }
}

pub struct SqliteBackend {
    conn: rusqlite::Connection,
}

impl SqliteBackend {
    pub fn open(path: &str) -> crate::Result<Self> {
        let conn = rusqlite::Connection::open(path).map_err(|e| BackendError::Io(e.to_string()))?;
        Ok(Self { conn })
    }
}

impl Backend for SqliteBackend {
    fn push(&mut self, job: Job) -> crate::Result<()> {
        self.conn
            .execute("INSERT INTO jobs (id, payload) VALUES (?1, ?2)", (job.id.0, &job.payload))
            .map(|_| ())
            .map_err(|e| BackendError::Io(e.to_string()))
    }
    fn pop(&mut self) -> Option<Job> {
        let row: Option<(u64, Vec<u8>)> = self
            .conn
            .query_row("SELECT id, payload FROM jobs ORDER BY id LIMIT 1", [], |r| Ok((r.get(0)?, r.get(1)?)))
            .ok();
        let (id, payload) = row?;
        self.conn.execute("DELETE FROM jobs WHERE id = ?1", [id]).ok()?;
        Some(Job::new(crate::job::JobId(id), payload))
    }
    fn len(&self) -> usize {
        self.conn.query_row("SELECT COUNT(*) FROM jobs", [], |r| r.get(0)).unwrap_or(0)
    }
}
```

```rust
// src/scheduler.rs
use crate::backend::Backend;
use crate::job::Job;
use crate::state::{Event, JobState};

#[derive(Clone, Copy, Debug)]
pub struct RetryPolicy {
    pub max_attempts: u32,
    pub backoff_ms: u64,
}

pub struct PopResult {
    pub job: Option<Job>,
    pub remaining: usize,
}

/// Drives jobs through their lifecycle against one backend.
pub struct Scheduler<B: Backend> {
    backend: B,
    policy: RetryPolicy,
}

impl<B: Backend> Scheduler<B> {
    pub fn new(backend: B, policy: RetryPolicy) -> Self {
        Self { backend, policy }
    }

    pub fn pop(&mut self) -> PopResult {
        let job = self.backend.pop();
        PopResult { job, remaining: self.backend.len() }
    }

    pub fn run_once(&mut self, run: impl Fn(&Job) -> std::result::Result<(), String>) -> crate::Result<Option<JobState>> {
        let Some(job) = self.backend.pop() else { return Ok(None) };
        let state = JobState::Queued.transition(Event::Start).expect("queued -> running");
        match run(&job) {
            Ok(()) => Ok(Some(state.transition(Event::Succeed).expect("running -> done"))),
            Err(reason) => {
                if job.attempts() + 1 < self.policy.max_attempts {
                    self.backend.push(job.retried())?;
                }
                Ok(Some(state.transition(Event::Fail(reason)).expect("running -> failed")))
            }
        }
    }
}
```

```rust
// src/util.rs
pub fn now_ms() -> u64 {
    std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .map(|d| d.as_millis() as u64)
        .unwrap_or(0)
}
```

The named abstractions here are `Backend` (with `MemoryBackend` and
`SqliteBackend` as its implementations), `Job`, `JobState`, and `Scheduler`.
`JobId` is a newtype with no methods. `Event` is a plain enum. `RetryPolicy`
is a config holder. `PopResult` bundles a return value. `BackendError` and
`TransitionError` are plain error types. `Result` is a type alias. `now_ms`
is a function.

Rubric:
- writes one file at `docs/concepts.md`, and nothing else
- has an entry for each of `Backend`, `Job`, `JobState`, `Scheduler`;
  `MemoryBackend` and `SqliteBackend` appear either as their own entries or
  named inside the `Backend` entry
- has no entry for `JobId`, `Event`, `RetryPolicy`, `PopResult`,
  `BackendError`, `TransitionError`, `Result`, or `now_ms`
- every entry has exactly the four lines What, Owns, Where, Depends on, with
  `src/…` paths
- entries are in one flat alphabetical list, with no sections per module
- no entry narrates why the concept exists or how it came to be
- the whole file is roughly 35 lines or fewer
