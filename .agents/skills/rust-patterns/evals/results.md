# rust-patterns — eval results

Append-only. Newest at the bottom.

## 2026-07-19 — backfill A/B, obsolescence check (skill as of fcb4361)

Arms: A = no skill, B = skill. n=1 per cell — signal, not proof.

- S1 (sessions module): **tie, 6/6 both** — both arms produced newtypes,
  data-carrying state enum, typed error (hand-impl vs thiserror), zero
  unwrap, iterator chain, private internals
- S2 (review, 8 planted violations): **tie, 8/8 both** — both also caught
  the unsound-safe-API framing of the unsafe block and the logically-dead
  poll loop, beyond the rubric
- S3 (refactor): **tie — the two arms produced byte-identical code**
  (?-chain, filter_map, &[User])
- S4 (negative, Cargo.lock): **B, narrowly** — baseline's answer ended on a
  self-contradicting hedge; both correct on substance and ceremony-free

Judge verdict: 21/21 rubric lines both arms; zero failures anywhere.
Obsolescence: YES — the no-skill arm passed everything; S3's identical
output shows the scenarios can no longer discriminate. Retired.
