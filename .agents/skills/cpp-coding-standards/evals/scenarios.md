# cpp-coding-standards — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. The subagent returns only the
deliverable. Anonymize into teams, blind-judge against the rubrics, log in
`results.md`. Primary question: obsolescence — execution AND attention.

## S1 — write: a resource-owning class

User message: "Write a C++20 class `TempFile` for a Linux service: on
construction it creates a temporary file (mkstemp), exposes `write(bytes)`
and `path()`, and the file must be unlinked and the descriptor closed when
the object goes away. It will be stored in containers and sometimes handed
off between owners. Just the code."

Rubric:
- RAII: cleanup in the destructor, no manual close/unlink required by users
- copy operations deleted; move constructor/assignment provided (or
  explicitly defaulted where valid) — container/handoff requirement met
  without double-close
- no naked new/delete; any dynamic resource behind RAII
- error path on construction/write uses exceptions or an explicit error
  type, not silent ignore or errno-checked-by-caller
- const-correctness: `path()` (and any observer) is const
- destructor is noexcept-safe (no throwing operations unguarded)

## S2 — review: planted violations

User message: "Review this C++ code from our service and list every problem
you find:

```cpp
#include <string>
#include <vector>

int g_retry_count = 3;

enum Status { OK, TIMEOUT, ERROR };

class Buffer {
public:
    Buffer(size_t n) { data_ = new char[n]; size_ = n; }
    ~Buffer() { delete[] data_; }
    char* data_;
    size_t size_;
};

Status fetch(std::string url, double* elapsed_ms, Buffer* out);

char* make_greeting(const std::string& name) {
    char* buf = new char[name.size() + 16];
    sprintf(buf, "Hello, %s!", name.c_str());
    return buf;
}

double average(std::vector<double> samples) {
    double sum = 0;
    for (int i = 0; i < samples.size(); i++) sum += samples[i];
    return sum / (int)samples.size();
}
```"

Planted violations (8), rubric = one line per plant:
- non-const global `g_retry_count` (I.2)
- plain `enum` instead of `enum class` (unscoped, converts to int)
- `Buffer`: owning raw new[] with destructor but no copy control —
  rule-of-three/five violation, double-delete on copy (also public members)
- `fetch` out-parameters (`double*`, `Buffer*`) instead of return
  value/struct; `std::string url` by value where const& (or view) fits
- `make_greeting` transfers ownership by raw pointer (I.11) and leaks on
  caller error; should return std::string
- `sprintf` into a hand-sized buffer (unsafe, off-by-one risk)
- `average` takes vector by value (needless copy) — const& or span
- signed/unsigned loop mixing plus C-style cast `(int)` instead of
  static_cast / ranged-for / std::reduce

## S3 — structural probe: underspecified ask

User message: "I'm starting the first real C++ module of our new backend
service next week (it talks to a message queue and keeps an in-memory
index). What should I get right from the start?"

Rubric (pass = the answer covers it unprompted):
- RAII / ownership discipline raised (smart pointers, no owning raws)
- const/immutability-by-default raised
- type-safety defaults raised (enum class, strong types, no C casts)
- error-handling strategy raised as a decision to make (exceptions vs
  expected, noexcept boundaries)
- the guidelines mindset is an organizing thread of the answer, not one
  bullet

## S4 — negative: should not trigger

User message: "Two sentences max: what does `std::move` actually do?"

Rubric:
- direct, correct, ≤2 sentences (it's a cast, doesn't move anything); no
  guidelines lecture, no code review ceremony
