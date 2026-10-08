# S2 baseline (no skill) — the graveyard discriminator

**Prompt:** "Loads of startups have tried consumer AI note-taking and none of them
got big. I still think there's something there. Am I walking into a tarpit?"

**Rubric outcome: PASS on all four criteria.**

- Three-way discriminator: **pass**. "Two innocent readings of a pile of failures:
  a wall moved recently, or the pioneers fumbled a winnable position — Friendster,
  not a broken market."
- Demands a named mechanism: **pass**. Asks which specific wall killed Evernote,
  Roam, Mem and Rewind, and whether it fell in the last two or three years. Quotes
  the "'AI is hot' is not a why-now" line.
- Names structural properties: **pass**. Willingness to pay, churn, network
  effects, free competition from platforms, plus the pull test for B2C.
- Avoids an unconditioned yes/no: **pass**. Leans yes, then states what would move
  the verdict.

**Why it passed, and what it means for the skill.**

The baseline arm had the vault. It read `Concepts/Tarpit Market.md`, `Why Now`,
`Market Pull`, `Moat`, `Non-Consensus Thesis`, `Edge` and
`Notes/What the Agent Shift Displaces`, and reconstructed the discriminator from
the pages themselves. The knowledge is already operational in the repo without a
skill loading it.

It also went beyond the rubric in two ways a skill would have to match rather than
add: it applied the user's own note on whether a domain produces a cheap
trustworthy failure signal, and it surfaced the open question on
`Distribution Asymmetry` about consumer exceptions, which is the strongest
counter-argument to its own verdict.

**Provisional conclusion, pending S1, S3 and S4:** the obsolescence risk is real and
runs the opposite way from usual. The vault may already be the skill. If S3, the
underspecified probe, also passes at baseline, the honest verdict is that no skill
should be written for use inside this repo, and the criteria only need packaging if
they are to travel to other projects where the concept pages are absent.
