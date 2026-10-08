# market-selection — eval results

Append-only. Newest last.

---

## 2026-09-03 — RED baseline, before drafting. Verdict: do not build the skill.

**Sample size: n=1 per cell.** Five scenarios, baseline arm only (no skill, which
does not yet exist). All baseline agents ran inside the second-brain repo, so they
had `CLAUDE.md` and the `Concepts/` graph available.

| Scenario | Rubric outcome |
|---|---|
| S1 hidden fatal criterion | **pass** 4/4 |
| S2 graveyard discriminator | **pass** 4/4 |
| S3 underspecified probe | **pass** 3/4, one partial |
| S4 generate from edge | **pass** 4/5, one partial |
| S5 negative, landing copy | **partial** — wrote the copy, but over-interrogated position |

**Verdict: the skill is unnecessary. Stopping per the authoring mandate.**

The baseline arm reconstructed every discriminator the skill was going to encode,
by reading the concept pages. S1 named buyer concentration as potentially fatal and
did the bottom-up ceiling arithmetic. S2 produced the three-way graveyard
discriminator unprompted. S3 raised five criteria against a prompt that named no
axis. S4 generated four candidate directions from a stated edge, filtered them
afterwards rather than before, and applied the control-point test to choose.

The knowledge is already operational in the repo. A skill would restate the concept
pages to an agent that can read them.

**Where the partials fell.**

- S3 treated bottom-up distribution for developer tools as given rather than as a
  hypothesis. Minor, and defensible for that category.
- S4 was thin on who currently pays what. It named the gaps well and the buyers
  weakly, which is the market-pull half of the framework underperforming.
- S5 is the one real weakness, and it runs the opposite way from a missing skill.
  The base model already interrogates positioning on a copy request. Adding a
  market-selection skill would amplify an over-trigger that is present without it.

**Consequence for any future version.** Build this only if the criteria need to
travel outside this repo, where the concept pages are absent. That is a packaging
job with a tightly scoped `description` and an explicit "not for" covering copy,
positioning and messaging. It is not a behavior-change job here, and the obsolescence
probe (S3, the underspecified structural scenario) shows no delta to recover.

**Unexpected finding.** The exercise was worth running for a reason unrelated to
skills: S4's generation run produced four candidate directions and a through-line
thesis, sourced entirely from gaps documented in `Concepts/`. Recorded separately.
