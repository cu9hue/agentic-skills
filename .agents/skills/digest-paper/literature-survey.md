# Literature Survey

Use when mapping an unfamiliar field rather than digesting a single paper. This
builds a reading list and a sense of the landscape using the same staged reading
as the main skill: run `digest-paper`'s passes on individual papers as you go.

Requires web access or a search index (Google Scholar, Semantic Scholar, arXiv).
Say so if that is unavailable.

## The loop

1. **Seeds**: find three to five recent, on-topic papers with well-chosen
   keywords. Run `digest-paper` Pass 1 on each to confirm relevance and category.
2. **Shared references**: read the related-work sections of the seeds and scan
   their bibliographies. Papers the seeds cite *in common* are the field's
   foundational works; read those next.
3. **Forward citations**: find recent papers that cite your seeds. These show
   where the field is now.
4. **Iterate**: repeat steps 2 and 3 with the new papers until searches keep
   surfacing names you already have (convergence).
5. **Digest the core**: run `digest-paper` Pass 2 on the handful of works that
   turn out to be central.

## Output

A short landscape:

- the foundational works the field rests on
- the current frontier (most recent significant work)
- the main camps, methods, or schools of thought
- the open gaps and disagreements
- a one-line note on each key paper, taken from its triage

## Notes

- Stop when new searches stop surfacing new papers, not at a fixed count.
- A highly cited paper is not automatically correct. Apply the same independent
  read as in `digest-paper`.
- Distinguish foundational works (old, heavily cited) from frontier works (recent,
  not yet cited much). A good survey covers both.
