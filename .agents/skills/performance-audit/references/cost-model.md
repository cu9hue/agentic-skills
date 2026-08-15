# Cost model

Order-of-magnitude anchors for what a single event costs. Use them to rank
hypotheses before you test them, and to sanity-check whether a counter total
can explain the runtime. Nothing here is a measurement of your machine.

**Stamp: 2026-08, modern x86-64 server class.** Intel Ice Lake-SP through
Granite Rapids and Sierra Forest, AMD Zen 3 through Zen 5, two sockets,
DDR4-3200 through DDR5-6400.
Figures are in cycles first, because cycle counts survive a clock change and
nanoseconds do not. The ns column assumes a sustained 3.0 GHz — one cycle is
0.33 ns. Your machine's sustained clock under load is not its boost clock;
read the real one as `cycles / task-clock` from `perf stat`.

| Event | Cycles | ns @ 3.0 GHz | What moves it |
|---|---|---|---|
| L1d hit, load-to-use | 4–5 | 1.3–1.7 | 4 on Zen 3–5 with the fast-path addressing mode; 5 on Ice Lake-SP and later Intel, and on any part with an indexed addressing mode |
| L2 hit | 12–16 | 4–5 | L2 size. Ice Lake-SP is about 14; Sapphire Rapids, with a 2 MB L2, about 16; Zen 3 about 12. |
| L3 hit, local slice | 45–90 | 15–30 | Core count and interconnect. Mesh server parts run above client ring parts. On Zen, an in-CCX hit sits near the low end; a line found in *another* CCD's L3 is not this row — it costs more, and behaves like the false-sharing round trip below. |
| Local DRAM | 200–350 idle; 500–1000+ loaded | 70–120; 170–330+ | Utilization. The left figure is idle latency. Queueing dominates under load and grows without bound past roughly 80% of peak bandwidth, so the loaded figure has no real ceiling. **Re-derive this row before it enters gate-4 arithmetic** — see below. DDR5 is not lower-latency than DDR4; it is wider. |
| Remote-NUMA DRAM | 350–700 | 120–230 | 1.3–2.2x local, per socket distance and link generation. Read your machine's real matrix; do not assume a factor. |
| Branch mispredict | 15–20 | 5–7 | Pipeline depth. |
| dTLB miss, second-level TLB hit | 7–15 | 2–5 | STLB capacity and page size. Charged once per miss and no walk follows; it is the next row that hurts. |
| dTLB miss + page walk | 20–50 when the page-table entries are cached; 500+ when they are not | 7–17; 170+ | Where the four levels of page-table entries live. Each level is its own load and each can miss to DRAM. |
| Atomic RMW, uncontended | 15–25 | 5–8 | Line already held in L1 in modified state. The cost includes draining the store buffer, so it is a barrier as well as an operation. |
| Atomic RMW, contended | 100–300 same socket; 500+ cross-socket | 35–100; 170+ | Thread count. Throughput collapses faster than linearly as writers are added. |
| False-sharing round trip | 100–200 same socket; 300–600 cross-socket | 35–70; 100–200 | Paid per write, in both directions, for as long as both threads keep writing. |
| Syscall, trivial (`getpid`-class), mitigations fixed in silicon or off | 150–250 | 50–85 | The floor: `syscall`/`sysret`, the entry stub, and the kernel-side work. |
| Same syscall with KPTI active | 900–1800 | 300–600 | Page-table switch on entry and exit. PCID support roughly halves it, so read `/sys/devices/system/cpu/vulnerabilities/*` and check `dmesg` for `pti` before you quote either row. Part of the cost lands *after* the return, as TLB misses charged to your code. |
| `memcpy`, 4 KiB, both buffers L1-hot | 100–200 | 35–70 | 32–64 B/cycle steady state, plus `rep movsb` startup on the ERMS path. |
| `memcpy`, 4 KiB, source cold in DRAM | 600–1000 | 200–350 | Bandwidth-bound, not latency-bound: 64 line fills stream. Single-core streaming bandwidth is 10–20 GB/s. |

These are anchors for ranking hypotheses. They are not evidence and they are
not measurements. No audit finding may cite a row of this table as support for
a claim about the code under audit — not the localization, not the confirming
measurement, not the expected gain. The table tells you which of two
hypotheses is worth testing first. The test is what tells you which one is
true. If a report sentence would still stand with the table deleted, it is a
finding; if it collapses, it was never one.

The rows are not equally soft. The wide ones: contended atomic RMW spans 3x
inside one socket, and the page-walk row is bimodal — 20–50 cycles with the
page-table entries cached against 500 or more without, a 25x split inside a
single row.

The rule for using two rows together is one you apply, not one you look up:
**any two rows whose cycle ranges intersect rank nothing against each other.**
Read the two ranges and check. Intersections are common enough that listing
them would run longer than the table, and they include some you would not
guess — a branch mispredict (15–20) sits entirely inside an uncontended atomic
RMW (15–25); a same-socket false-sharing round trip is the same 100–200 as a
4 KiB L1-hot `memcpy`; the syscall floor (150–250) reaches idle local DRAM, a
same-socket contended atomic, and that same false-sharing round trip; a
cold-source `memcpy` (600–1000) reaches remote DRAM, loaded local DRAM, an
uncached page walk, and a cross-socket atomic; even an L3 hit (45–90) reaches a
cached page walk (20–50). Those are examples, not an inventory: do not read a
pair's absence from this paragraph as permission to rank it. Where the ranges
intersect, measure both or say you could not.

Where they do not intersect, the *direction* holds and the *size* does not. An
L3 hit and an idle local DRAM access are 2.2x apart at their closest (90
against 200) and 7.8x apart at their widest (45 against 350), because each row
is its own band and a ratio between two bands compounds both. Across every part
this stamp covers, DRAM is the more expensive of the two — that ordering is
safe. By how much is a 3.5x question, which is why you must not put the size in
a report without deriving it. That is what the next paragraph is for.

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
mlc --loaded_latency          # the DRAM row under load — see below
mlc --max_bandwidth           # socket streaming peak, all cores

# Streaming peak without MLC. STREAM is the portable answer; the perf bench
# line above gives the single-core figure and prints GB/s directly.
stream_c.exe                  # build with -O3 -fopenmp, array >> L3
```

**Streaming peak, and the achieved bandwidth to compare it against.** Two
different numbers, and the catalog's latency-versus-bandwidth tests need both.
The peak comes from `mlc --max_bandwidth`, STREAM Triad, or
`perf bench mem memcpy -s 64MB` for the single-core figure. The *achieved*
bandwidth of your workload is not something plain `perf stat` reports — it
needs uncore memory-controller counters:

```bash
# Intel server: the uncore memory controllers. Modern perf builds ship the
# Intel uncore JSON, which attaches a ScaleUnit to these events, so perf
# already prints MiB — read that number and divide by elapsed time. Do NOT
# multiply it by 64; the scaling is applied for you and you would overstate
# bandwidth by orders of magnitude.
perf stat -a -e uncore_imc/cas_count_read/,uncore_imc/cas_count_write/ -- ./bench

# Only if perf prints a bare unscaled count — a number with no unit beside
# it — do you convert by hand: bytes = (reads + writes) * 64, one CAS per
# 64-byte line. Check which you got before you divide.

# AMD Zen 4 and later expose the UMC PMU. Check what this kernel has:
perf list | grep -iE 'umc|uncore_imc|amd_df'

# Some perf builds carry a ready-made metric group. Prefer it if present:
perf list metricgroup | grep -iE 'memory.*bandwidth|DRAM'
```

Both need `-a` and therefore `perf_event_paranoid` at 0 or root, and neither
exists inside most VMs. If you cannot get an achieved-bandwidth number on this
host, say so — the catalog entries that use it name a fallback that does not.

**The DRAM row specifically.** Idle latency is the wrong input to gate-4
arithmetic on a busy machine. Derive the loaded figure with
`mlc --loaded_latency`, which sweeps injection rate and reports latency at each
level of achieved bandwidth; read off the point matching your workload's
achieved bandwidth from the counters above. Without MLC, run the pointer chase
below on one core while the other cores run a bandwidth hog, and take the
difference. Quote the loaded number, not the idle one.

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
per-event cost from this file only until you have re-derived it.

One row needs the re-derivation before you use it at all: **local DRAM**. Its
table figure is idle latency, and a typically loaded server runs two to three
times higher — that is the number to plan with. Past roughly 80% of peak
bandwidth queueing takes over and there is no ceiling at all, which is the
tail the row's "+" refers to; two to three times is the working case, not a
bound. Feed the idle number into the arithmetic above and every DRAM
hypothesis is systematically under-ranked — which is the bucket most audits
land in, so the bias is not random, it points one way. Either use a loaded
figure derived on the target machine, or state that your DRAM estimate is a
lower bound and rank accordingly.

Then bound the result three ways before it goes in the report:

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
