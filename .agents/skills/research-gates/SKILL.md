---
name: research-gates
description: Use when deciding whether a research bet deserves more time or money — a trading strategy, a backtest result, a side project or business idea — or when kill criteria are being set, checked or bent, open ideas need a keep-or-kill review, a first allocation needs sizing, or a dead idea needs a post-mortem. Not for explaining one statistic or method on its own; answer that directly.
origin: the six gates, rules and templates are adapted from the author's own Notion research framework ("Canonical Research Pipeline and Templates", 2026); quant checks in references/quant.md draw on Bailey & López de Prado (2014), Bailey, Borwein, López de Prado & Zhu (2014, 2017), Harvey, Liu & Zhu (2016), Moulinier (2026), and the HangukQuant notes "Quantitative and Qualitative Treatments to Capital Markets" (ch 11, after Masters)
---

# Research Gates

A stage-gate framework for research bets. Each gate costs more than the one
before it, and each one can kill the idea. The kill criteria are fixed before
any evidence is touched.

You already know the statistics. What you do not do unprompted is this: fix
the kill criteria first, refuse to move them after the result, log every
attempt, put a sizing step between a good result and real money, and check
that live results come from the reason given. This skill makes those steps
happen.

## First: does this ask need the gates?

Pick one outcome.

**A method or definition question — answer directly and stop.** "What is the
formula for X", "how do I compute Y", "what does Z mean". Answer it in full.
No gates, no idea card, no kill criteria, and no sentence that names this
framework to say it does not apply. A reader must not be able to tell this
skill was loaded.

**A decision about one bet — run the gates.** Spend more time, spend money,
go live, keep or kill, change a criterion. Find the gate the idea is at and
answer from there (see "Answer shape").

**A question inside one gate — answer that gate.** "How do I backtest this",
"what data do I need". Answer the question in full with that gate's checks.
If an earlier step is missing (usually: no kill criteria yet), say so in one
line and propose them. Never withhold the answer until the user goes back to
Thesis.

**An agenda — use the gates as the spine.** "I'm researching a few ideas,
what should I get right?" Answer with the six gates in order and the rules
below as the organizing thread, not as one bullet among many.

## The six gates

Run them in order. An idea cannot skip a gate. A gate without its output
blocks the next one.

| Gate | Kill question | Entry condition | Output |
| --- | --- | --- | --- |
| 1. Thesis | Who pays, and why? | A one-line bet | Thesis, who pays and why they keep paying, kill criteria written and dated before any evidence |
| 2. Evidence | Can I observe the thing at the resolution I need? | Kill criteria written | Dataset plus a data quality log |
| 3. Test | Does the cheapest honest test pass the pre-written kill criteria? | Data quality log signed off | The test result against the kill criteria, with every real cost included |
| 4. Robustness | Does it survive other samples and placebos? | Test passed | Results on other samples, placebos, a selection adjustment for every attempt logged |
| 5. Sizing | Can I survive being wrong three times in a row? If not, size down. | Robustness passed | Size, caps, loss budget, stop rule |
| 6. Live | Does the result come from the reason I gave? If not, post-mortem. | Sized | Results with attribution to the stated reason |

### Gate notes

- **Thesis.** "Who pays" names a party that gives up money, time or margin
  to you, and a reason they will keep doing it. "The market is
  inefficient" or "people need this" names nobody. If you cannot say who
  pays, kill.
- **Evidence.** Check that the thing can be observed at the resolution the
  thesis needs before you build a test on it. The data quality log records
  the source, the period, the conventions, the gaps and the checks run.
- **Test.** The cheapest honest test is the cheapest one that could kill the
  idea with every real cost included. For a trade, an out-of-sample test net
  of all costs. For a product, a request for money, not for an opinion.
- **Robustness.** A result that passes once can be luck or a fit to one
  sample. Run it on samples it never saw, and run placebos that break the
  claimed mechanism. Adjust for every attempt in the log.
- **Sizing.** Size so that three losses in a row at that size leave you able
  to continue. A small live trial is still capital: it goes through Sizing,
  sized small on purpose, with its own stop rule.
- **Live.** A good result for the wrong reason fails this gate. Compare what
  happened with the reason you gave. If they do not match, write the
  post-mortem, even when the result made money.

## Kill criteria

Write them at Thesis, date them, and never edit them. Each criterion names:

- the metric and the line it must clear
- the sample it will be judged on (period, population, what counts)
- the cost and assumptions the test must include
- the attempt budget: how many variants you will try at most
- the date by which the gate decides

Add "what would change my mind": the observation that kills the idea from
here, and the one that would make you back it harder.

**Editing kill criteria is overfitting with extra steps.** If the criteria
were wrong, reframe: the old idea is killed with a post-mortem, and a new
idea opens with new criteria written before any new evidence. Evidence the
user has already seen cannot confirm criteria written after it. The reframe
needs fresh evidence.

## Rules

- **Kill criteria are written at Thesis and never edited.** Changing them
  means a new idea.
- **Each gate has an entry condition, an output and a kill question.** Name
  all three when you work a gate.
- **Exploratory work cannot pass a gate.** Anything done before the kill
  criteria were fixed is exploratory. It can suggest an idea. It cannot
  confirm one. Say so when a user brings a result from a search they ran
  before writing criteria.
- **Log every attempt.** Record each variant tried, with its result. The
  best of many attempts looks good by chance; the count is what lets you
  correct for it.
- **An idea left undecided for two weeks is killed.** A periodic review
  (weekly by default) gives every open idea keep, kill or reframe, with a
  dated line in its decision log.
- **Do not commit capital before Sizing.**
- **Every number traces to a dataset or a cited source.** An untraced number
  is a guess and is labeled as one.
- **Grade the process, not the outcome.** A profitable bad decision is still
  a bad decision. Grade the process before you look at the result.

## Status and post-mortem

An idea has one of three statuses:

- `open`: moving through the gates
- `kept`: passed Live and still running; reviews continue
- `killed`: stopped, with a post-mortem

A reframe kills the old idea and opens a new one.

The post-mortem is the idea's last dividend, not a failure state. It records:
what the thesis said, what happened (with numbers), what killed it, which
gate should have caught it, the process grade, and the lesson in one
sentence. Write one for every killed idea, at every gate.

## Where idea cards live

- **In the user's Obsidian vault** (`/Users/palg/Projects/personal/second-brain`):
  an idea is a page in `Notes/` filled from `_templates/idea.md`. Its
  frontmatter holds `type: idea`, `status`, `gate` and `last-review`. Its
  sections are the bet, who pays, kill criteria, what would change my mind,
  the gates table, the evidence log, the decision log and the post-mortem.
  Update `gate` when the idea advances and `last-review` at each review.
  Append to the evidence and decision logs. Never edit the kill criteria
  section.
- **Elsewhere:** put the card wherever the project keeps research notes, with
  the same sections.

## Domain references

- **Quantitative trading:** read `references/quant.md` before you answer at
  any gate for a trading idea. It holds the checks for each gate, the
  default thresholds (all user-tunable), and short templates for a research
  note, a data quality log and a post-mortem.
- **Business ideas:** the general gates apply. No reference file exists yet;
  add `references/business.md` when one is needed.

## Answer shape

Speak the user's language, not the framework's. Unless the user already
works with these gates, say what the step is in plain words ("before any
money goes in, size it so three losses in a row are survivable") rather than
"you are at Gate 5". Do not use "entry condition" or "gate output" with
them, and do not quote the rule slogans at them; give the reason in a plain
sentence. Offer an idea card only when the user keeps research notes where
cards live, or asks to track the idea.

For a decision about a bet:

1. Say which step the idea is at and the question that step must answer.
2. Compare the evidence with the kill criteria. If no criteria exist, say
   the evidence so far is exploratory and propose criteria, labeled as a
   proposal for the user to fix.
3. Give the next cheapest honest test, and what happens if it fails.
4. If the idea dies here, give the post-mortem lines.

Keep it direct. Say what the rule is and why in a sentence. Do not lecture,
and do not moralise about a user who wants to bend a criterion: the pull to
bend it is normal, and the rule exists because of it.

## Quality gate

- the triage ran; on a method or definition question no gate, card or
  criterion appears
- the answer works the right gate and asks its kill question, in plain words
  unless the user already uses the gate names
- kill criteria exist before evidence, or the answer says the evidence is
  exploratory and proposes criteria
- no criterion was edited after a result; a change became a reframe that
  needs fresh evidence
- every attempt is counted, and the result is adjusted for the count
- no capital before Sizing, including small live trials
- every number traces to a dataset or a cited source
- for a trading idea, the gate's checks in `references/quant.md` were applied
