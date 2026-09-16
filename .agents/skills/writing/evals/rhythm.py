#!/usr/bin/env python3
"""Mechanical rhythm meter for the writing skill's voice evals.

Usage: python3 rhythm.py FILE [FILE...]

Counts the cadence tells that a rubric judge scores inconsistently. Only
prose paragraphs count (bullets, headers, code, tables and quotes are
skipped). Reference values come from the author's own notes, measured
2026-09-16 over ~29k words of English prose:

  connectives   ~20 per 1000 words
  X-not-Y       ~1  per 1000 words
  exclamation   ~3.5 per 1000 words
  parentheses   ~4  per 1000 words
  end-fragment  ~19% of paragraphs (casual asides, not verdicts)

The skill's pre-fix drafts sat at 10-15 connectives, 3-7 X-not-Y, 0
exclamation. The thresholds in scenarios.md are derived from these numbers.
"""
import re
import statistics
import sys

CONNECTIVES = re.compile(
    r"\b(however|also|additionally|hence|meaning|note that|e\.g\.|i\.e\.|"
    r"which|so|because|since|though|although|basically|actually|super|"
    r"pretty|kinda|a bit|a lot|generally|usually|for example|in a nutshell|"
    r"simply put|first off|second off|eventually|then|another|that's where|"
    r"enter)\b",
    re.I,
)
CONTRAST = re.compile(
    r"(,\s*not\s+\w"                                  # "X, not Y"
    r"|\bnot\s+[\w' ]{1,25}\.\s+[A-Z]"                 # "not X. Y."
    r"|\b(is|are|was|were|isn't|aren't|wasn't|weren't)\s+(not\s+)?"
    r"[\w' ]{1,20}\.\s+(It's|It is|They're|They are|That's|That is)\b"
    r"|\b(isn't|aren't|wasn't|weren't|doesn't|don't|never)\s+[\w' ]{1,20}"
    r"\.\s+(It|They|That|He|She|We)\s+(is|are|was|were|does|do|did)\b)"
)
PRONOUNCEMENT = re.compile(
    r"^(That is (the|what|where|why|how)|That's (the|what|where|why|how)|"
    r"The honest \w+|Which is the whole|Nothing more\b|That's the whole)",
    re.I,
)
ANNOUNCEMENT = re.compile(r"^(So|Side by side|In short|Put simply|Numbers|The point|Result)\s*:")


def prose_paragraphs(text):
    text = re.sub(r"^---.*?---", " ", text, flags=re.S)
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"!\[.*?\]\(.*?\)", " ", text)
    text = re.sub(r"\[\[([^\]|]*)(\|[^\]]*)?\]\]", r"\1", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\*\*", "", text)
    paras = []
    for block in re.split(r"\n\s*\n", text):
        lines = [l for l in block.split("\n") if l.strip()]
        if not lines:
            continue
        if any(re.match(r"\s*([-*>]|\d+\.|#|\||\[)", l) for l in lines):
            continue
        joined = " ".join(l.strip() for l in lines)
        sents = [s for s in re.split(r"(?<=[.!?])\s+", joined) if s.split()]
        if sents:
            paras.append(sents)
    return paras


def measure(text):
    paras = prose_paragraphs(text)
    sents = [s for p in paras for s in p]
    words = sum(len(s.split()) for s in sents)
    if not words:
        return None
    joined = " ".join(sents)
    lens = [len(s.split()) for s in sents]
    per_k = lambda n: 1000.0 * n / words
    end_frag = [p[-1] for p in paras if len(p[-1].split()) <= 6]
    return {
        "words": words,
        "paragraphs": len(paras),
        "sentence_len_mean": statistics.mean(lens),
        "sentence_len_sd": statistics.pstdev(lens),
        "one_word_paragraphs": sum(1 for p in paras if len(p) == 1 and len(p[0].split()) <= 2),
        "paragraphs_ending_on_fragment": len(end_frag),
        "end_fragments": end_frag,
        "x_not_y": len(CONTRAST.findall(joined)),
        "pronouncements": sum(1 for p in paras for s in p if PRONOUNCEMENT.match(s.strip())),
        "announcements": sum(1 for p in paras if ANNOUNCEMENT.match(p[0].strip())),
        "connectives_per_k": per_k(len(CONNECTIVES.findall(joined))),
        "exclamation_per_k": per_k(joined.count("!")),
        "parentheses_per_k": per_k(joined.count("(")),
        "em_dashes": text.count("—") + text.count("–"),
    }


def main(paths):
    for path in paths:
        m = measure(open(path, encoding="utf-8", errors="ignore").read())
        print(f"== {path}")
        if not m:
            print("   no prose paragraphs found")
            continue
        for k, v in m.items():
            if k == "end_fragments":
                for frag in v:
                    print(f"   end-fragment: {frag!r}")
                continue
            print(f"   {k:32}{v:8.1f}" if isinstance(v, float) else f"   {k:32}{v:8d}")


if __name__ == "__main__":
    main(sys.argv[1:])
