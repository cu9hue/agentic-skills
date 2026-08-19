---
name: prepare-pr
description: Use when a finished branch is ready to become a pull request — clearing AI plans and specs out of the branch history, auditing the comments the change leaves behind, writing the PR body, and watching CI to green. Not for deciding whether the work is done or how to merge it.
origin: PR body rules follow ASD-STE100 (Simplified Technical English) and William Zinsser, "On Writing Well"
---

# Prepare a Pull Request

Four gates, in order. Each gate blocks the next.

Two conventions for every command below: `main` stands for the repo's default
branch, and the working tree is clean before gate 1 starts. Check it with
`git status --porcelain`. Commit or stash anything it prints — a history
rewrite on a dirty tree fails halfway through.

Run the test suite once before gate 1 and keep the output. A failure after the
rewrite then points at the rewrite, not at the code.

## Gate 1 — no AI documents in the branch history

Specs, implementation plans, and task notes drive the work. They do not ship
with it. Deleting them from the working tree is not enough: the blobs stay in
the branch's commits and land in the PR diff.

List every Markdown file the branch adds, across all its commits:

```sh
git log --diff-filter=A --name-only --pretty=format: main..HEAD -- '*.md' | sort -u
```

Added files only. A modified `README.md` or `CHANGELOG.md` is the branch
documenting itself. Leave it alone.

**Ask before you remove.** Show the user the whole list in one message and ask
which files the repo genuinely ships. Exclusion is the default. Do not rule on
this yourself: a dated design document under `docs/` looks like a deliverable
and usually is not, and the one file that belongs is rarely the one you would
guess.

Save the current shape of the change, so you can prove the rewrite touched
nothing else:

```sh
git diff --stat main..HEAD > /tmp/pr-prep-before.txt
```

Rewrite the branch. Use `git filter-repo` when it is installed:

```sh
git filter-repo --force --invert-paths \
  --path IMPLEMENTATION_PLAN.md --path docs/specs/2026-08-10-design.md \
  --refs main..HEAD
```

Otherwise fall back to `filter-branch`:

```sh
FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch --force --prune-empty \
  --index-filter 'git rm --cached --ignore-unmatch -- IMPLEMENTATION_PLAN.md docs/specs/2026-08-10-design.md' \
  main..HEAD
```

`--prune-empty` drops the commits that only ever touched those files.

Do not reach for `git reset --soft` and one big commit instead. It removes the
files, but it also flattens a commit structure the user did not ask you to
touch.

Verify, then push:

```sh
git log --diff-filter=A --name-only --pretty=format: main..HEAD -- '*.md' | sort -u
git diff --stat main..HEAD | diff /tmp/pr-prep-before.txt - 
git push --force-with-lease -u origin HEAD
```

The first command prints only the files the user kept. The second prints only
the removed files. `--force-with-lease` always, `--force` never. A rejected
push means someone else moved the branch: stop and tell the user.

If the path will come back on the next branch, offer a `.gitignore` line for
it. Offer — the user decides.

## Gate 2 — comments match the end state

Dispatch one subagent with `git diff main...HEAD` (three dots) and the rules
below. It edits the files directly and reports each change in one line. On a
platform with no subagent, do the audit as one dedicated pass with the diff in
front of you and nothing else in scope.

The rules, given to the subagent verbatim:

- A comment is at most two lines. Longer means it is narrating the code
  instead of explaining it. Cut it down or cut it out.
- A comment states why, not what. Delete any comment that restates the line
  under it.
- A comment describes the end state. Delete every trace of how the code got
  there: "previously", "we switched to", "after review", "used to be",
  "turned out to be".
- A comment is factual and current. One that names a counter, flag, variable,
  or function the code no longer has is wrong. Delete it and report it — it
  often marks a feature dropped by accident, not just a stale sentence.
- Keep the comments that carry something a reader cannot infer: why this API
  and not the obvious one, which invariant the caller must hold, which bug the
  odd-looking branch handles.
- Add no comments. Lines that are fine without one stay untouched.

When the subagent reports, read its edits in the diff and run the test suite or
build. Report what changed and what the tests printed.

## Gate 3 — the PR body

Every fact comes from the final diff. Not from this conversation, and not from
the plan file you removed in gate 1: a plan says what someone intended, the
diff says what shipped.

Title: one imperative line naming the change.

Body, in this order, and nothing else:

1. **What** the change adds or fixes. Two to four sentences.
2. **Why.** What the old behaviour cost, in one or two sentences.
3. **Deployment note**, only when the diff carries one.

Write it in Simplified Technical English:

- One idea per sentence.
- Active voice with a named actor. "The endpoint returns 429", not "a 429 is
  returned".
- One word, one meaning. Pick a term for the thing and reuse it.
- Keep the articles and connectives.
- Ordinary English everywhere except code identifiers and domain terms.

A deployment note exists when the diff adds or changes an environment variable
or secret, a database migration, an external service or dependency, an
infrastructure or config default, a feature flag, or a data backfill. Name the
variable, the migration file, the flag. State the order when order matters:
"Run migration 0042 before the code ships." State the consequence when a
default changes behaviour for existing traffic. No such change in the diff, no
section in the body.

Do not write:

- a file-by-file walk of the diff — the reviewer already has the diff
- the branch's story: what you tried, what review changed, what you rejected
- headings the diff cannot support — Screenshots, Checklist, an empty Testing
  section
- emoji, or adjectives that sell the change

## Gate 4 — CI to green

```sh
gh pr create --base main --title "<title>" --body-file <body.md>
gh pr checks --watch
```

Green: report the PR URL and stop.

Red: stop the gate and hand the failure over.

```sh
gh run view <run-id> --log-failed
```

Report the failing job, the first real error line, and which part of the diff
it points at. Do not push a fix — the user decides what happens next.

Claim green only from the output of `gh pr checks` itself.

## Not this skill

A request to commit, push, or amend is not a request to prepare a pull
request. Do that one thing and stop. No gates, no scan for `.md` files, no
comment audit, and no trailing advice about what to do before the PR.

## Quality gate

- every `.md` file the branch added is gone, except the ones the user named
- `git log --diff-filter=A --name-only main..HEAD` proves it
- every push used `--force-with-lease`
- the comment audit ran, and its edits are visible in the diff
- the PR body has no file list, and no deployment section the diff cannot
  justify
- `gh pr checks` printed green, or the failure is in the user's hands
