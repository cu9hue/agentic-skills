---
name: second-brain-retrieval
description: Use when the user asks about their prior ideas, projects, research, decisions, technical preferences, or anything their curated notes likely cover — "what did I think about…", "did I note…", "where does my thinking stand on…", "what's new in my second brain". Read-only retrieval from the second-brain HTTP service, with citations. Not for editing or authoring notes — canonical edits happen in the authoring workflow and Git, never through this skill.
---

# Second-Brain Retrieval

The user keeps a curated second brain behind an HTTP service. Search it before
you answer any question its notes may cover. This skill is read-only:
retrieve, cite, and stop.

## Configuration

- Read `SECOND_BRAIN_URL` and `SECOND_BRAIN_READER_TOKEN` from the
  environment. Never hardcode a URL or a token.
- The service runs over Tailscale HTTPS.
- Make every call with `curl --fail-with-body -sS`.
- Use the reader token for every normal call. `SECOND_BRAIN_CAPTURER_TOKEN`
  exists only for deliberate inbox captures (see Writes).

## When to search

Search the second brain when the user asks about their prior ideas, projects,
research, decisions, technical preferences, or material their curated notes
likely cover. "Did I note…", "what did I decide…", "where does my thinking
stand…" are all retrieval questions.

Go through the service, not around it. Do not grep the vault on disk even
when it is local: the index does the ranking, and only the service returns
the chunk IDs you must cite. A filesystem crawl of the vault is not
retrieval, it is a slower search with no citations.

Do not search for tasks that never touch the user's notes (writing a script,
fixing a bug in an unrelated repo). Answer those directly.

## The API

| Endpoint | Use for |
|---|---|
| `GET /health` | Diagnostics only — availability and index state. Never routine context gathering. |
| `POST /search` | Primary retrieval. Body: `query`, `limit`, optional `kinds`, optional `tags`. |
| `GET /notes/{note_path}` | The full canonical note — full context. |
| `GET /chunks/{chunk_id}` | The exact cited passage — evidence. |
| `POST /related` | Expand context around a `note_path` or `chunk_id`. Only when the first result needs more context. |
| `GET /recent` | Recently indexed material. Use for "what's new / recent / newly added" — not broad `/search`. |
| `POST /capture` | Inbox Markdown draft. Forbidden unless the user explicitly asks AND `SECOND_BRAIN_CAPTURER_TOKEN` is set. |

Selection rules:

- Recency question → `/recent`, not repeated broad `/search` calls.
- Evidence for a claim → `/chunks/{chunk_id}`. Full context → `/notes/{note_path}`.
- `/health` only when you diagnose a failure, never as an opening move.
- Never call `/capture` speculatively or as a side effect of retrieval.

## The retrieval loop

1. `POST /search` with the question's key terms, `"limit": 5`.
2. Retrieve the most relevant hit with `GET /chunks/{chunk_id}` or
   `GET /notes/{note_path}` before you rely on it. Never answer from the
   search snippet alone.
3. `POST /related` only when that result needs surrounding context.
4. Answer with citations.

## Citation

Cite the note path, heading, and chunk ID for every note-backed claim:

> Your hub note says the reading is interview-targeted, not linear
> (`Sources/TCP-IP Illustrated Volume 1.md` › "TCP/IP Illustrated, Volume 1",
> chunk `02fbddd9d626c88d30103d59`).

- Keep note-backed claims and your own inference visibly separate. The notes
  are curated context, not unquestionable truth — you may disagree, but say
  which is which.
- When the second brain has no useful evidence, say so plainly and answer
  from what you do have. Do not pad a miss into a vague hit.
- Never read or cite `_sources/`. It is raw reference material, not the
  searchable corpus.

## Writes

None. This skill never writes to the service and never modifies canonical
notes — canonical edits happen in the authoring workflow and Git.

The single exception: `POST /capture` creates an inbox draft, and only when
both hold — the user explicitly asked to capture, and
`SECOND_BRAIN_CAPTURER_TOKEN` is present. An aside in a retrieval question is
not an ask; at most, offer to capture it.

## Failure

If a variable is missing, the service is unreachable, or auth fails: say so
in one line and continue with the other context you have. Never print a token
value — not in output, not in logs, not in an error message you relay.

## Shell examples

```sh
# search
curl --fail-with-body -sS -X POST "$SECOND_BRAIN_URL/search" \
  -H "Authorization: Bearer $SECOND_BRAIN_READER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query":"tcp handshake","limit":5}'

# get_chunk — evidence for a citation
curl --fail-with-body -sS "$SECOND_BRAIN_URL/chunks/51db8e3209827cf3b74c2798" \
  -H "Authorization: Bearer $SECOND_BRAIN_READER_TOKEN"

# get_note — full canonical note; URL-encode the path (it may contain spaces)
enc=$(python3 -c 'import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1]))' "Concepts/TCP.md")
curl --fail-with-body -sS "$SECOND_BRAIN_URL/notes/$enc" \
  -H "Authorization: Bearer $SECOND_BRAIN_READER_TOKEN"

# related — expand around a chunk or a note
curl --fail-with-body -sS -X POST "$SECOND_BRAIN_URL/related" \
  -H "Authorization: Bearer $SECOND_BRAIN_READER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"chunk_id":"51db8e3209827cf3b74c2798"}'   # or {"note_path":"Concepts/TCP.md"}
```
