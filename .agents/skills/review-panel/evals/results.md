# review-panel — eval results

Append-only. Newest at the bottom.

## 2026-08-28 — initial A/B (base 929b446)

Arms: A = no skill, B = SKILL.md. n=1 per cell — signal, not proof. One blind
judge scored all five scenarios; teams renamed per scenario so neither arm
kept a fixed name. RED ran before the skill was drafted; the draft worked
from the recorded baseline failures (S1 missed the scalability angle, S3
asserted a billing convention, S4 answered with a deploy checklist instead of
review angles).

Platform note: both arms ran on Claude Code, told to invoke no skill of their
own. The repo under review was inlined, not on disk, so arm B's reviewers
could not explore a codebase; on every scenario the diff fit one screen and
arm B took the skill's single-reader path rather than fanning out — the
fan-out clause is exercised by real usage, not by these evals.

- S1 (multi-angle execution): **tie, 8/8 vs 8/8.** Both arms found every
  planted defect, including the cache race tied to threaded workers and the
  dead keyless exchangerate.host endpoint. B additionally surfaced the
  unbounded `.all()` (A passed rubric f on the stale cache alone) and asked
  two domain questions (historical-rate conversion, rounding convention) that
  A folded into assertions. The rubric could not separate them.
- S2 (verification kills the noise): **tie.** Both arms led with the silent
  `None` return, explicitly cleared the import-time registry, and did not
  invent a race. Both caught the bonus wasted sleep. B found a real
  CSV-vs-`resp.json()` bug beyond the plant; A matched with
  retry-on-non-retryable notes.
- S3 (domain adequacy): **B wins.** A asserted "the hardcoded 30 is wrong"
  — answering the exact question the rubric wanted asked — and failed rubric
  d. B asked three numbered questions with labeled defaults and asserted no
  convention. B's soft spot: it classified `int()` truncation as
  "confirmed-safe, cleanup only" instead of a finding (rubric b fail); noted
  as a known weakness, not blocking since the mechanism was still flagged.
- S4 (structural probe): **B wins, 3/3 vs 1/3.** A gave a strong deploy-risk
  checklist (rollback, migrations, kill switch) but covered at most three of
  the seven review angles and never mentioned data races, pattern
  conformance, or external-API currency. B named all ten angles and the
  verification gate, and offered to run the panel.
- S5 (negative): **B wins on restraint, and does not over-trigger.** B
  summarized and stopped. A appended a caveats paragraph enumerating two
  bugs — past the rubric's one-sentence allowance.

Judge verdict: two ties on detection, three B wins on judgment — ask when
it's a convention, review when asked to review, stop when asked to
summarize. Landing.
Obsolescence: no. The baseline failed rubric lines in S3, S4, and S5, and
scored 1/3 on the structural probe — the ten angles are earning their keep
as attention allocation, not as detection ability the base model lacks.
