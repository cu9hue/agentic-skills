# python-patterns — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. The subagent returns only the
deliverable (code or review text). Anonymize into teams, blind-judge against
the rubrics, log in `results.md`. Primary question for this skill:
obsolescence — does the no-skill arm already pass every rubric?

## S1 — write

User message: "Write a small Python module with one function:
`load_config(path)` reads a JSON config file and returns a `Config` object
with fields `host: str`, `port: int`, `debug: bool` (default False). Handle
a missing file and invalid JSON sensibly."

Rubric (each line = one skill mandate):
- type hints on the function signature and Config fields
- Config is a dataclass (or equivalent typed container), not a bare dict
- file opened with a context manager
- specific exceptions caught (FileNotFoundError, json.JSONDecodeError) —
  no bare except, no silent None return
- exceptions chained (`raise ... from e`) or original context preserved
- no mutable default arguments anywhere

## S2 — review

User message: "Review this Python code and list the problems:

```python
from os.path import *

def collect(items, seen=[]):
    for i in items:
        if type(i) == str:
            seen.append(i)
    return seen

def read_all(paths):
    out = ""
    f = None
    try:
        for p in paths:
            f = open(p)
            out += f.read()
            f.close()
    except:
        pass
    return out

def find(d, key):
    if key == None:
        return None
    if key in d:
        return d[key]
    return None
```"

Rubric — flags each planted anti-pattern:
- star import
- mutable default argument (`seen=[]`)
- `type(i) == str` instead of isinstance
- string concatenation in a loop (O(n²), should join)
- manual open/close without context manager (and the leak when read fails)
- bare except swallowing errors
- `== None` instead of `is None`

## S3 — refactor

User message: "Make this function Pythonic:

```python
def get_names(users):
    names = []
    for u in users:
        if u.active == True:
            names.append(u.name)
    return names
```"

Rubric:
- list comprehension replaces the manual loop
- `u.active` truth-tested directly, not compared to True
- type hints added to the signature
- no behavior change

## S4 — negative: plain knowledge question

User message: "Explain in two sentences what the GIL is."

Rubric:
- direct two-sentence answer; no code rewrite ceremony, no pattern
  checklist, no unsolicited style advice
