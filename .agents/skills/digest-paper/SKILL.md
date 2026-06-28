---
name: digest-paper
description: Use when digesting, summarizing, triaging, or critically reviewing a scientific or research paper from a PDF or an arXiv/DOI/URL link, or when surveying and mapping the literature of a research field. Not for general articles or blog posts.
origin: synthesized from S. Keshav, "How to Read a Paper" (the three-pass method and literature-survey loop), and a community five-question hypothesis-summary framework
---

# Digest Paper

Reading a whole paper at full depth is wasteful before you know it's worth it.
Digest in escalating passes and stop at the depth the task needs. Throughout,
keep what the paper *claims* separate from your own *read* of it.

## When to Use

- summarizing or triaging a paper from a PDF, arXiv ID, DOI, or URL
- deciding whether a paper is worth a full read, and for whom
- pulling out a paper's hypothesis, evidence, and stated caveats
- a critical review of a paper's method and conclusions
- mapping the literature of a field (see Surveying a field, below)

Not for general articles, blog posts, or documentation.

## How it runs

Default to **Pass 1 only**. Run Pass 2 when asked, then Pass 3 when asked, one
after the other. Each pass ends with a decision: go deeper or stop. This mirrors
how an expert reads, spending depth only where it pays off.

Read the PDF with the Read tool; for PDFs over ~10 pages, read in page ranges.
Ground every claim you report in a section or figure, and quote numbers from the
text. Never estimate or invent a figure: the paper is long, so anchor to it.

## Pass 1: Triage (default)

From the title, abstract, introduction, section headings, conclusions, and
references. Produce the five Cs, compressed:

- **Category**: empirical study / theory or methods / survey or review /
  position. This picks the Pass 2 template.
- **Context**: what it builds on; name familiar related work if any.
- **Correctness**: do the core assumptions look reasonable at a glance?
- **Contributions**: the main claims, in the authors' own terms.
- **Clarity**: is it well-structured and well-written?

End with a one-line verdict: what the paper is, whether it is worth a full read,
and for whom. Then stop and ask whether to continue to the brief.

## Pass 2: Brief (on request)

Adapt to the category found in Pass 1.

For an **empirical / hypothesis-driven** paper, the five questions:

1. **Hypothesis**: the question or claim being tested.
2. **Verdict**: does the author conclude it holds? (yes / no / partly / maybe)
3. **Why**: the evidence and method in a line or two (data, sample, what was
   measured).
4. **Author's reservations**: the caveats and doubts the authors state
   themselves, methodological or other.
5. **Beyond the result**: further conclusions or calls (e.g. "quantitative
   methods aren't enough; calls for qualitative follow-up").

**Theory / methods**: the construct, model, or method introduced; what it
improves on or replaces; what is *proven* versus *asserted*; the assumptions it
rests on.

**Survey / review**: the scope and organizing frame or taxonomy; what it
concludes about the state of the field; the gaps or open problems it names.

Always add, whatever the category:

- **Key figures**: name the one to three figures or tables that carry the
  result, and what each shows.
- **Independent read**: your own assessment, labeled as yours and kept separate
  from the author's: limitations the authors did not admit (thin or biased
  sample, confounds, missing baselines, an abstract that overclaims its results).
  If the paper is weak, say so with the specific reason. No inflated praise.

Then stop and ask whether to go deeper.

## Pass 3: Deep dive (on request)

- **Reproduce it**: could you rerun the study or rebuild the system from what is
  written? Name what is missing if not.
- **Reproducibility**: is data or code available? are parameters and settings
  given?
- **Validity**: threats to internal and external validity; do the conclusions
  actually follow from the results?
- **Connections**: how it sits against related work, and what it opens up next.

## Surveying a field (optional)

When the task is mapping a field's literature rather than digesting one paper,
read `literature-survey.md` and follow it. It runs a seed-and-citation loop and
calls this skill on each paper.

## Keep author and reader separate

- Report what the paper says and your own read as distinct things. Never present
  your critique as the authors'.
- Tie each substantive claim to a section or figure reference.
- Quote numbers from the paper; do not estimate or invent them.
- Follow the `writing` skill's anti-slop rules: plain, concrete, no hype.

## Quality Gate

Before delivering, confirm:

- the category is identified and the brief matches it
- the author's claim, the author's reservations, and your independent read are
  all distinguishable
- the key figures are named
- claims are tied to sections or figures, and no number is fabricated
- the triage verdict says who the paper is for
- deeper passes ran only when asked
