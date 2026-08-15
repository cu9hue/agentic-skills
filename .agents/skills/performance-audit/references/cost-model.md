# Cost model

Order-of-magnitude anchors for what a single event costs. Use them to rank
hypotheses before you test them, and to sanity-check whether a counter total
can explain the runtime. Nothing here is a measurement of your machine.

**Stamp: 2026-08, modern x86-64 server class.** Intel Ice Lake-SP through
Emerald Rapids, AMD Zen 3 through Zen 5, two sockets, DDR4-3200 or DDR5-4800.
Figures are in cycles first, because cycle counts survive a clock change and
nanoseconds do not. The ns column assumes a sustained 3.0 GHz — one cycle is
0.33 ns. Your machine's sustained clock under load is not its boost clock;
read the real one as `cycles / task-clock` from `perf stat`.

| Event | Cycles | ns @ 3.0 GHz | What moves it |
|---|---|---|---|
| L1d hit, load-to-use | 4–5 | 1.3–1.7 | 4 on Skylake and Zen 3/4 fast path; 5 on Ice Lake, Golden Cove, and with an indexed addressing mode |
| L2 hit | 12–16 | 4–5 | Server parts sit at the high end. Skylake-SP is 14. |
| L3 hit | 35–70 | 12–23 | Core count and interconnect. Ring parts are low, mesh server parts high. On Zen, an in-CCX hit is far cheaper than a cross-CCX one. |
| Local DRAM | 200–350 | 70–120 | Idle latency. Queueing under load pushes it past 200 ns. DDR5 is not lower-latency than DDR4; it is wider. |
| Remote-NUMA DRAM | 350–700 | 120–230 | 1.3–2.2x local, per socket distance and link generation. Read your machine's real matrix; do not assume a factor. |
| Branch mispredict | 15–20 | 5–7 | Pipeline depth. |
| dTLB miss, second-level TLB hit | 7–15 | 2–5 | — |
| dTLB miss + page walk | 20–50 when the page-table entries are cached; 500+ when they are not | 7–17; 170+ | Where the four levels of page-table entries live. Each level is its own load and each can miss to DRAM. |
| Atomic RMW, uncontended | 15–25 | 5–8 | Line already held in L1 in modified state. The cost includes draining the store buffer, so it is a barrier as well as an operation. |
| Atomic RMW, contended | 100–300 same socket; 500+ cross-socket | 35–100; 170+ | Thread count. Throughput collapses faster than linearly as writers are added. |
| False-sharing round trip | 100–200 same socket; 300–600 cross-socket | 35–70; 100–200 | Paid per write, in both directions, for as long as both threads keep writing. |
| Syscall, trivial (`getpid`-class) | 300–700 on a hardware-mitigated part; 1500–5000 with KPTI active | 100–230; 500–1700 | Mitigation state. Read `/sys/devices/system/cpu/vulnerabilities/*` before you quote either figure. |
| `memcpy`, 4 KiB, both buffers L1-hot | 100–200 | 35–70 | 32–64 B/cycle steady state, plus `rep movsb` startup on the ERMS path. |
| `memcpy`, 4 KiB, source cold in DRAM | 600–1000 | 200–350 | Bandwidth-bound, not latency-bound: 64 line fills stream. Single-core streaming bandwidth is 10–20 GB/s. |

These are anchors for ranking hypotheses. They are not evidence and they are
not measurements. No audit finding may cite a row of this table as support for
a claim about the code under audit — not the localization, not the confirming
measurement, not the expected gain. The table tells you which of two
hypotheses is worth testing first. The test is what tells you which one is
true. If a report sentence would still stand with the table deleted, it is a
finding; if it collapses, it was never one. Every range here also spans a
factor of two or more, and the ranges overlap, so two hypotheses whose anchors
are within a factor of two are not ordered by this table at all — measure both
or say you could not.

Re-derive the rows that matter to your audit on the target machine, and quote
the derived numbers instead. `lmbench` covers memory latency, syscall, and
context switch. `perf bench mem` covers `memcpy` and `memset` at the sizes you
care about. A pointer-chase loop with a stride sweep finds the cache-level
boundaries on this specific part, which is the one thing the vendor
documentation will not tell you about your populated configuration. Run each
under the same repeat-and-spread protocol as gate 1 — a cost model derived
from one run is no better than the table above.

```bash
# Machine shape first. Everything below is meaningless without it.
lscpu -C                      # cache sizes and line size per level
getconf LEVEL1_DCACHE_LINESIZE
numactl --hardware            # node count and the distance matrix
cat /sys/devices/system/cpu/vulnerabilities/*
cat /sys/kernel/mm/transparent_hugepage/enabled

# Memory latency vs working-set size. The knees are your cache boundaries.
lat_mem_rd -P 1 512m 64       # lmbench: 512 MiB range, 64-byte stride
lat_syscall -P 1 null
lat_ctx -P 1 -s 0 2

# memcpy and memset across sizes, on the routine glibc actually selects.
perf bench mem memcpy -s 4KB -l 100
perf bench mem memcpy -s 64MB -l 10
perf bench mem memset -s 4KB -l 100
perf bench sched pipe         # round-trip through the kernel

# NUMA latency and bandwidth matrix, if Intel MLC is available.
mlc --latency_matrix
mlc --bandwidth_matrix
```

For the cache-level boundaries, a pointer chase is more trustworthy than any
tool, because you control the stride and can defeat the prefetcher. Build a
cyclic permutation of indices over a buffer of size `S`, walk it `N` times, and
report cycles per step. Sweep `S` from below L1 to well past L3, doubling each
time; the plateaus are the levels and the steps between them are the latencies
in the table above. Sweep the stride separately: a stride below 64 bytes
measures line reuse rather than latency, a stride at exactly a power of two
large enough to alias will report conflict misses as capacity misses, and a
stride above 4 KiB defeats the L2 streamer, which is the point when you want
raw latency. Randomize the permutation rather than using a fixed stride once
you have the boundaries, or the hardware prefetcher will hide the number you
are trying to read.

## Ranking with this file — gate 4

Rank a hypothesis by the cycles it would remove, not by how large the fix is:

```
expected cycles removed  ≈  (events you would eliminate) × (cycles per event)
expected share           ≈  expected cycles removed / total cycles
```

Take the event count from your own counters, never from this file. Take the
per-event cost from this file only until you have re-derived it. Then bound
the result three ways before it goes in the report:

- **The bucket caps it.** A fix inside `backend bound` cannot recover more
  than the slot share gate 2 measured for `backend bound`. A fix inside a
  level-2 node cannot exceed that node's share.
- **Out-of-order execution caps it again.** The core overlaps much of this
  latency, so the product above is an upper bound and it usually overshoots.
  That is what makes it useful for ruling hypotheses *out*: a cost that cannot
  reach a few percent of cycles even at full penalty is not your problem.
- **Amdahl caps the whole thing.** The ceiling is the fraction of wall time
  the affected region owns, which is a gate-1 number.

Report the result as an order of magnitude and as a bound — "at most a few
percent", "the same order as the runtime". Never as a predicted number, and
never as a ranked list of wins. The ranking orders what you test next. It does
not tell the reader what they will get.
