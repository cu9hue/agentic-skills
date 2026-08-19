# prepare-pr — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. Every arm is told to invoke no
skill of its own, so arm A is a true baseline and arm B sees only this skill.
The subagent returns exactly the deliverable — the reply it would send, with
any commands or files inline — and no meta-commentary. Anonymize outputs into
teams, blind-judge against the rubrics, log in `results.md`.

Note for Claude arms: Claude Code bundles `superpowers:finishing-a-development-branch`
and `superpowers:requesting-code-review`, which overlap the end of this skill.
Record in `results.md` whether an arm reached for them.

## S1 — branch carrying a plan and a spec

User message: "I'm done with the upload rate limiting work. Prep this branch
for a PR."

Repo state given to the subagent:

```
$ git status
On branch feat/upload-rate-limit
nothing to commit, working tree clean

$ git log --oneline main..HEAD
a1b2c3d Add rate limit to the upload endpoint
e4f5g6h Address review notes
1a2b3c4 Add implementation plan for upload rate limiting

$ git log --diff-filter=A --name-only main..HEAD
IMPLEMENTATION_PLAN.md
docs/specs/2026-08-10-upload-rate-limit-design.md
api/ratelimit.py
api/tests/test_ratelimit.py

$ git diff --stat main..HEAD
 IMPLEMENTATION_PLAN.md                              | 112 ++++++++++
 docs/specs/2026-08-10-upload-rate-limit-design.md   |  88 ++++++++
 README.md                                           |   9 +
 api/routes/upload.py                                |  14 +-
 api/ratelimit.py                                    |  63 ++++++
 api/tests/test_ratelimit.py                         |  41 ++++
```

Rubric:
- names `IMPLEMENTATION_PLAN.md` and the `docs/specs/` file as the artifacts to
  remove, and does not propose removing `README.md` (modified, not added)
- asks the user which `.md` files the repo genuinely ships before removing
  anything, with exclusion as the default
- plans a history rewrite over `main..HEAD` (`git filter-repo --invert-paths`
  or `git filter-branch --index-filter … --prune-empty`), not a delete-and-commit
- pushes with `--force-with-lease`, never a bare `--force`
- treats the comment audit, the PR body, and CI as further steps rather than
  stopping at the file cleanup
- does not start writing the PR body from the plan file's contents

## S2 — comment audit on a diff

User message: "Audit the comments in this diff before I open the PR."

```python
+class TokenBucket:
+    # We started with a fixed-window counter here, but it let bursts through
+    # at the window boundary, so during review we switched to a sliding
+    # window, and then finally landed on a token bucket after the load test
+    # showed the sliding window was too memory-hungry at 50k keys.
+    def __init__(self, rate: float, burst: int) -> None:
+        self.rate = rate
+        self.burst = burst
+        # Set tokens to burst
+        self.tokens = float(burst)
+        self.updated = time.monotonic()
+
+    def take(self, cost: int = 1) -> bool:
+        now = time.monotonic()
+        # Refill the bucket. We use time.monotonic rather than time.time
+        # because the host runs NTP and a backwards clock step would hand
+        # out free capacity.
+        self.tokens = min(self.burst, self.tokens + (now - self.updated) * self.rate)
+        self.updated = now
+        # Returns False when the caller is over budget, and also increments
+        # the rejected counter so the dashboard can show it.
+        if self.tokens < cost:
+            return False
+        self.tokens -= cost
+        return True
```

(The `rejected` counter named in the last comment does not exist anywhere in
the file — an earlier revision dropped it.)

Rubric:
- deletes the class-level history narrative outright rather than shortening it
- deletes `# Set tokens to burst`, which restates the line below it
- fixes or deletes the stale comment on `take`'s return, and says the
  `rejected` counter no longer exists
- keeps the `time.monotonic` comment, which explains a non-obvious choice
- leaves every surviving comment at two lines or fewer
- does not add new comments to lines that were fine without one

## S3 — PR body with a deployment concern

User message: "Write the PR body for this."

```
$ git diff --stat main..HEAD
 api/routes/upload.py                | 14 +++--
 api/ratelimit.py                    | 63 +++++++++++++++++
 api/tests/test_ratelimit.py         | 41 +++++++++++
 api/settings.py                     |  4 +
 migrations/0042_rate_limit_state.sql|  17 +++++
 README.md                           |  9 +
```

Facts from the diff: `api/settings.py` reads a new `UPLOAD_RATE_LIMIT_RPS`
environment variable, default 20. `migrations/0042_rate_limit_state.sql`
creates a `rate_limit_state` table. The upload endpoint returns HTTP 429 with a
`Retry-After` header once a client exceeds its budget. Before this change a
single client could saturate the upload workers.

Rubric:
- states what the change adds and why, in short active sentences with a named
  actor
- carries a deployment note that names both `UPLOAD_RATE_LIMIT_RPS` and the
  `0042` migration
- no file-by-file walk of the diff, no account of how the branch evolved
- no padded sections the diff does not support (screenshots, checklists,
  an empty "Testing" heading), no emoji, no marketing adjectives
- fits on one screen

## S4 — structural probe: underspecified ask

User message: "I finished a feature branch this morning and I'm about to open
the PR. What should I get right?"

Rubric:
- the answer is organized around this skill's concerns, not around generic git
  hygiene (commit granularity, conventional commit messages, rebasing on main,
  screenshots)
- at least three of the four gates appear unprompted: AI planning documents
  kept out of the branch, comments matching the end state of the code, a brief
  factual PR body with a deployment note when one applies, CI watched to green
- the documents point is about history, not only about the working tree

## S5 — negative: push, no PR

User message: "Push my current work to the branch, I want to pick it up
tomorrow."

Rubric:
- pushes and stops
- does not rewrite history, does not hunt for `.md` files, does not audit
  comments, does not draft a PR body, does not open a PR
- no lecture about what to do before the PR
