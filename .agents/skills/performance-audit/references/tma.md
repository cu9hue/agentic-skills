# TMA localization

Top-down Microarchitecture Analysis splits every pipeline slot the CPU issued
into four buckets. Measure the split, name the bucket, then drill down. The
bucket is the finding; the source code is not evidence for it.

A *pipeline slot* is one µop-issue opportunity in one cycle. A core issues 4
slots per cycle (6 on Golden Cove and later). The four level-1 buckets partition
100% of those slots, so they always sum to 100%.

Rules:

- Do not name a bucket you did not measure. Reading the source is not
  localization.
- Profile the same build and the same workload as the baseline. Build with
  optimization on plus `-g -fno-omit-frame-pointer`. Never profile a debug
  build.
- Chase the largest bucket above 20%. Ignore anything below 10%.
- Record which tool produced the split. If you used a fallback, say so.

## The four buckets

| Bucket | Meaning | Drill-down |
|---|---|---|
| `retiring` | Slots that delivered a µop that retired. Useful work. | light operations, heavy operations (microcode assists) |
| `bad speculation` | Slots wasted on µops that never retired, plus slots blocked during recovery. | branch mispredicts, machine clears |
| `frontend bound` | The back end could accept µops; the front end did not deliver them. | fetch latency, fetch bandwidth |
| `backend bound` | µops were available; the back end could not accept them. | core bound, memory bound |

### `retiring`

The not-stalled bucket. The core is busy, so the machine is not the problem —
the instruction count is. High `retiring` and still too slow means one of two
things: you execute too many instructions, or you execute too few per
instruction.

- Do less work: better algorithm, hoist work out of the loop, cache results.
- Do more per instruction: vectorize. Check whether the compiler already did
  with `-fopt-info-vec-missed` (GCC) or `-Rpass-missed=loop-vectorize` (Clang).

One trap: level 2 splits `retiring` into *light operations* and *heavy
operations*. A large heavy-operations share means the microcode sequencer is
running — FP assists on denormals, `rep movsb`, gather/scatter. That is retired
work that buys nothing. Check it before you conclude the code is efficient.

### `bad speculation`

- **branch mispredicts** — the common case. Count with `branch-misses` and
  `branches`; the rate that matters is misses over branches. On Intel,
  `br_misp_retired.all_branches` attributes them to code.
- **machine clears** — rarer and more specific: memory-ordering violations
  (usually 4K address aliasing between a load and a store, or true sharing
  across threads), self-modifying code, FP assists. Count with
  `machine_clears.count` and its `.memory_ordering` and `.smc` variants on
  Intel. A machine clear costs far more than a mispredict, so a small count can
  still dominate.

Mispredict penalty is roughly 15–20 cycles on a modern x86 core.

### `frontend bound`

Rare in tight numeric loops. Common in large branchy binaries — interpreters,
databases, browsers, anything with a flat profile and a big text segment.

- **fetch latency** — the front end stalled waiting for instruction bytes:
  L1 i-cache misses, iTLB misses, branch resteers. Counters:
  `L1-icache-load-misses`, `iTLB-load-misses`, and on Intel
  `frontend_retired.l2_miss` / `icache_16b.ifdata_stall`.
- **fetch bandwidth** — bytes arrived but decode could not keep up: µop-cache
  (DSB) misses, legacy decode paths, loop-stream-detector limits. Counters on
  Intel: `idq.dsb_uops` vs `idq.mite_uops`, `dsb2mite_switches.penalty_cycles`.

Both drill-downs point at code size and code layout, not at data.

### `backend bound`

- **core bound** — execution resources, not memory. Port contention (too many
  µops competing for one port), long serial dependency chains (the loop-carried
  FP add, the pointer chase whose next address depends on the last load), or a
  long-latency unit like the divider. Counters on Intel:
  `exe_activity.exe_bound_0_ports`, `arith.divider_active`,
  `cycle_activity.stalls_total`.
- **memory bound** — stalled on the memory hierarchy. Split by level, because
  the fix differs at every level:
  - **L1 bound** — DTLB misses, store-to-load forwarding blocks, 4K aliasing.
  - **L2 bound** — the working set spills out of L1.
  - **L3 bound** — separate latency from contention; on a shared L3 another
    thread may be the cause.
  - **DRAM bound** — separate bandwidth-bound from latency-bound. Bandwidth
    saturation shows as a flat throughput curve when you add threads; latency
    shows as a dependent load chain with idle bandwidth.
  - **store bound** — the store buffer filled.

`backend bound` / `memory bound` is the bucket most audits land in, and it is
the one where naming the level is the whole value of the measurement. "Memory
bound" without a level is not a localization.

## Commands — Linux, x86

### 0. Check the PMU is exposed

Run this first. Virtual machines and most containers do not expose the PMU.

```bash
perf stat -e cycles,instructions -- /bin/true
cat /proc/sys/kernel/perf_event_paranoid
```

If the counters print `<not supported>` or `<not counted>`, there is no PMU.
Every command below except `cachegrind` will fail. Move to a bare-metal host or
use `cachegrind`.

`perf_event_paranoid` gates access: `2` allows profiling your own process, `1`
also allows kernel events, `-1` allows system-wide. Lower it with
`sudo sysctl -w kernel.perf_event_paranoid=1`. System-wide collection (`-a`)
needs `-1`, `root`, or `CAP_PERFMON`.

### 1. The level-1 split

```bash
perf stat --topdown -a -- ./bench
```

`--topdown` needs an Intel Core of Skylake generation or newer. On cores before
Ice Lake it aggregates per core and therefore needs `-a` and elevated
privileges, which is why `-a` is in the command above. On Ice Lake and newer,
perf uses the dedicated topdown counters and per-process collection works too.

Prefer the metric-group form when it is available — it needs no `-a` and no
root:

```bash
perf stat -M TopdownL1 -- ./bench
perf stat -M TopdownL2 -- ./bench
```

Check what your CPU and perf build actually offer before you rely on either:

```bash
perf list metricgroup | grep -iE 'topdown|pipeline'
```

Vendor situation:

- **Intel, Skylake or newer** — `--topdown` and `TopdownL1` both work.
- **AMD** — no `--topdown`. Zen 4 and newer expose an equivalent
  slot-based metric group through recent perf builds; the `perf list
  metricgroup` grep above tells you whether this kernel and this perf have it.
  Older Zen does not.
- **Anything else, or the grep comes back empty** — you have no TMA tree. Go to
  fallback A.

`perf stat --topdown --td-level=2` splits each bucket one level further. It
needs perf 5.13 or newer and an Ice Lake or newer core. If perf rejects the
flag, use `toplev`.

### 2. Raw counters

```bash
perf stat -e cycles,instructions,cache-references,cache-misses,branch-misses,dTLB-load-misses -r 10 -- ./bench
```

`-r 10` repeats the run and prints a `+- %` beside every counter, so you can see
whether a ratio is stable before you build an argument on it.

For the fallback ratios, add the events they need:

```bash
perf stat -e branches,branch-misses,L1-dcache-loads,L1-dcache-load-misses,LLC-loads,LLC-load-misses,iTLB-load-misses,L1-icache-load-misses -r 10 -- ./bench
```

Some of these print `<not supported>` depending on the CPU. That is normal;
drop the ones that do and note which ratios you therefore cannot compute.

### 3. Attribute the bucket to code

The split tells you what is wrong. This tells you where.

```bash
perf record -F 999 -g --call-graph dwarf -- ./bench
perf report --stdio --sort=overhead,symbol
perf annotate --stdio -s <symbol>
```

Record the event that matches the bucket you found, so the profile ranks by
that bucket rather than by time:

```bash
perf record -e cache-misses:pp -g -- ./bench      # memory bound
perf record -e branch-misses:pp -g -- ./bench     # bad speculation
```

The `:pp` suffix requests precise attribution. It needs PEBS on Intel or IBS on
AMD. Without it the sampled instruction pointer skids and blames the wrong line.
`--call-graph dwarf` works on binaries built without frame pointers but produces
large files; use `--call-graph fp` when the build has
`-fno-omit-frame-pointer`.

### 4. False sharing

Two threads writing different variables on one cache line. It shows up as
`backend bound` / `memory bound` with an L3 or DRAM signature that the working
set does not explain.

```bash
perf c2c record -- ./bench
perf c2c report --stdio
```

Read the HITM (hit-modified) counts and the per-cache-line offsets: two hot
offsets on one line, touched by different PIDs or TIDs, is false sharing. Same
offset from several threads is true sharing, which is a different fix.

`perf c2c` needs PEBS load-latency events on Intel, or IBS on AMD with a recent
kernel. It usually needs `perf_event_paranoid` at `1` or lower.

### 5. Full multi-level TMA

`toplev` from `pmu-tools` walks the whole tree, handles counter multiplexing,
and prints the bottleneck node by name.

```bash
git clone https://github.com/andikleen/pmu-tools
sudo sysctl -w kernel.nmi_watchdog=0
./pmu-tools/toplev.py -l3 --no-desc -- ./bench
```

`-l3` goes three levels deep; `--no-desc` drops the explanatory text.
`--drilldown` descends automatically to the lowest node it can resolve.
`toplev` is Intel-only in practice and needs the NMI watchdog off, because the
watchdog holds a counter it needs.

Use `toplev` when `perf stat --topdown` gives you a level-1 answer and you need
the level-2 or level-3 node before you can act.

### 6. No PMU at all

`cachegrind` simulates the cache and the branch predictor, so it runs anywhere,
including in VMs and containers.

```bash
valgrind --tool=cachegrind --branch-sim=yes --cachegrind-out-file=cg.out ./bench
cg_annotate cg.out
```

Read `D1mr`/`D1mw` (L1 data misses), `DLmr`/`DLmw` (last-level data misses),
`I1mr`/`ILmr` (instruction misses), and `Bcm`/`Bim` (mispredicted conditional
and indirect branches), per function and per source line.

Four limits, all of which matter:

- It runs 20–100x slower than native. Shrink the workload, and say you did.
- It simulates an idealized machine: LRU replacement, no hardware prefetcher, no
  out-of-order execution. It has no notion of cycles.
- With no prefetcher, it overstates the cost of sequential streaming access and
  understates the cost of dependent chains.
- It produces miss *counts*, not a bucket split. It can rank call sites within
  `memory bound`. It cannot tell you that you are `memory bound`.

`valgrind --tool=callgrind ./bench` plus `callgrind_annotate` gives the
instruction-count call graph when `perf record` is unavailable.

## Fallback A — no `--topdown`

Compute ratios from the counters in section 2 and use them to *rule buckets
out*. Miss counts, not slots, so this is weaker evidence. Say so in the report.

| Ratio | Compute | Reading |
|---|---|---|
| IPC | `instructions / cycles` | `< 1.0`: stalled, look at the rows below. `> 2.0`: not stalled — treat as `retiring`, the fix is fewer instructions or wider ones. Peak is 4 (6 on the newest cores). |
| Branch miss rate | `branch-misses / branches` | `> 5%`: `bad speculation` is real. `< 1%`: rule it out. |
| LLC miss rate | `cache-misses / cache-references` | `> 20%` with a large absolute count: DRAM traffic. Meaningless alone — pair it with MPKI. |
| LLC MPKI | `cache-misses / instructions * 1000` | `> 10`: `backend bound` / `memory bound` at the DRAM level. `< 1`: rule DRAM out. |
| L1D MPKI | `L1-dcache-load-misses / instructions * 1000` | `> 50` with low LLC MPKI: the working set fits in L2/L3 — L1 or L2 bound, a layout or blocking problem. |
| dTLB MPKI | `dTLB-load-misses / instructions * 1000` | `> 1`: page-walk cost. Test hugepages. |
| iTLB / i-cache MPKI | `iTLB-load-misses` or `L1-icache-load-misses` `/ instructions * 1000` | `> 1`: weak evidence for `frontend bound`. Confirm with a real TMA tool before acting. |

Then check the ratios explain the runtime. Multiply each event count by its
penalty and compare the total against `cycles`:

| Event | Penalty, order of magnitude |
|---|---|
| L2 hit | 12 cycles |
| L3 hit | 40 cycles |
| DRAM access | 200 cycles |
| Branch mispredict | 17 cycles |
| TLB page walk | 30 cycles |

Out-of-order execution hides much of this latency, so the sum is an upper bound
and it usually overshoots. That is exactly what makes it useful for elimination:
if branch mispredicts cannot account for 5% of cycles even at full penalty,
`bad speculation` is not the story. If nothing accounts for more than about a
quarter of the cycles, do not name a bucket — say the counters do not explain
the time and escalate to `toplev` or a bare-metal host.

The blind spot: there is no portable counter for issue slots, so this method
cannot see `frontend bound`, and it cannot separate `core bound` from
`memory bound` inside `backend bound`. Low IPC that none of the memory or
branch rows explain leaves `frontend bound` and `core bound` as the surviving
candidates, and you cannot choose between them here.

## Fallback B — macOS

There is no `perf` on macOS. Use `xctrace`, which ships with Xcode.

```bash
xcrun xctrace list templates
xcrun xctrace record --template 'CPU Counters' --output bench.trace --launch -- ./bench
xcrun xctrace record --template 'Time Profiler' --output bench.trace --launch -- ./bench
```

`--attach <pid|name>` records a running process; `--time-limit 10s` bounds the
run. Read the trace by opening it in Instruments, or extract it from the
command line:

```bash
xcrun xctrace export --input bench.trace --toc
xcrun xctrace export --input bench.trace --xpath '/trace-toc/run[@number="1"]/data/table[@schema="SCHEMA_FROM_TOC"]'
```

The `--toc` output lists the schema names; paste the one you want into the
`--xpath`. Recording hardware counters may need authorization — if the run
fails with a privileges error, repeat it under `sudo`.

For a stack profile with no Xcode at all, `sample` is in `/usr/bin`:

```bash
sample bench 10 1 -file sample.txt        # by process name
sample <pid> 10 1 -file sample.txt       # by pid
```

Arguments are `duration` in seconds then `samplingInterval` in milliseconds.
Flags take one dash: `-file`, and `-wait` to attach before the process starts.

**Apple Silicon does not expose the TMA tree.** Apple publishes no slot-based
decomposition of its cores, and no tool derives one. `CPU Counters` gives you
cycles, instructions, branch mispredicts, and cache misses — the inputs to
fallback A and nothing more. Intel Macs are no better off: `xctrace` reads the
Intel PMU but still builds no topdown tree.

So on macOS, gate 2 degrades to the counter ratios in fallback A, with the same
blind spot: `frontend bound` is unreachable. If a Linux machine with a
comparable CPU is available, run gate 2 there instead — the answer is about the
microarchitecture, and macOS cannot give it.

## What to record

Gate 2 produces one line the rest of the audit hangs on. Write it in this
shape — bucket, number, tool, and confidence:

```
Localization: backend bound / memory bound, DRAM level. 61% of slots.
Tool: perf stat -M TopdownL1, Intel Skylake-SP, 10 runs, +- 1.2%.
```

When you used a fallback, the shape is the same and the confidence line is
mandatory:

```
Localization: memory bound (inferred, no TMA available — Apple M2).
Tool: xctrace 'CPU Counters', 5 runs. LLC MPKI 24, IPC 0.41.
Confidence: lower. Counter ratios only; frontend bound cannot be
observed with this method and is not ruled out.
```

Never write a bucket with no number and no tool beside it.
