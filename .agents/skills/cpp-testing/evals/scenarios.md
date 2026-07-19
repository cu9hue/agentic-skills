# cpp-testing — eval scenarios

How to run: one subagent per arm per scenario (arm A = no skill, arm B =
SKILL.md loaded), identical prompts otherwise. Deliverable-only replies;
anonymize; blind judge; log in `results.md`. Primary question: obsolescence
(execution AND attention).

## S1 — write tests

User message: "Write GoogleTest tests for this function:

```cpp
// Parses an HTTP Retry-After header (delta-seconds form only).
// Returns seconds clamped to max_seconds. Returns 0 for empty/whitespace.
// Throws std::invalid_argument for non-numeric or negative input.
int parse_retry_after(const std::string& header, int max_seconds = 300);
```
Just the tests."

Rubric:
- covers: happy path, clamp at/above max, zero, empty, whitespace,
  negative, non-numeric
- error cases use EXPECT_THROW/ASSERT_THROW with the exact exception type
- repetitive case tables use value-parameterized tests (TEST_P +
  INSTANTIATE_TEST_SUITE_P) or a clearly table-driven loop — not seven
  copy-pasted TESTs
- custom max_seconds argument exercised
- descriptive test names (suite + case name describe behavior)
- tests independent: no shared mutable state, no ordering assumptions

## S2 — review: planted violations

User message: "Review this GoogleTest file and list every problem:

```cpp
#include <gtest/gtest.h>
#include <thread>
#include "orders.h"

std::vector<int> g_created_ids;

TEST(Orders, Create) {
    auto id = orders::create("alice");
    g_created_ids.push_back(id);
}

TEST(Orders, Fetch) {
    // needs Create to have run
    EXPECT_EQ(orders::fetch(g_created_ids[0]).owner, "alice");
}

TEST(Orders, AsyncShip) {
    orders::ship_async(1);
    std::this_thread::sleep_for(std::chrono::seconds(2));
    EXPECT_EQ(orders::status(1), "shipped");
}

TEST(Orders, Discount) {
    try {
        EXPECT_EQ(orders::discount(100, "GOLD"), 90);
    } catch (...) {
    }
}

TEST(Orders, Report) {
    orders::generate_report();
}

class DbFixture : public ::testing::Test {
protected:
    void SetUp() override { conn_ = new Connection("test_db"); }
    Connection* conn_;
};

TEST_F(DbFixture, Query) {
    EXPECT_TRUE(conn_->query("SELECT 1").ok);
}
```"

Planted violations (7), rubric = one line per plant:
- global mutable state + order dependence (Create/Fetch)
- sleep_for as async synchronization — flaky and slow
- try/catch(...) around the assertion swallowing failures (Discount can
  fail only silently; EXPECT inside try still marks, but a thrown failure
  path is eaten — should use EXPECT_THROW or no catch)
- test with no assertions (Report)
- fixture leaks: SetUp news a Connection, no TearDown/delete (and raw
  pointer instead of RAII/unique_ptr)
- tests hit real backend state with no isolation/reset between tests
- Fetch crashes with vector OOB (not an assertion failure) when run alone
  — misuse of cross-test state produces wrong failure mode

## S3 — structural probe: underspecified ask

User message: "Our C++ service (CMake project) has almost no tests and I'm
fixing that starting Monday. What should I get right from the start?"

Rubric (pass = covered unprompted):
- harness + build integration raised (GoogleTest/Catch2 via CTest,
  discovered tests, run in CI on every push)
- sanitizers raised (ASan/UBSan at least; TSan if concurrency) as part of
  the test pipeline
- isolation/fixture strategy raised (no shared state, RAII fixtures,
  seams/fakes for external deps)
- fast-vs-slow split or coverage gating raised as suite-management
  discipline
- testing discipline is the organizing thread, not one bullet

## S4 — negative: should not trigger

User message: "One sentence: in GoogleTest, what's the difference between
EXPECT_EQ and ASSERT_EQ?"

Rubric:
- one-sentence correct answer (EXPECT continues the test on failure,
  ASSERT aborts the current test function); no lecture, no suite advice
