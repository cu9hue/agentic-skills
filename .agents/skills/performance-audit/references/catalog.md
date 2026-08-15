# Fix catalog

This file is not a list of things to go do. It is an index from a measured
bucket to the small set of causes that produce it, and from each cause to the
one measurement that separates it from its neighbours.

Rules for entering:

- **You need a bucket first.** Gate 2 names it. Do not open a section you did
  not measure your way into. Reading the source and recognising a pattern here
  is not a finding, and a pattern that matches the source is the single most
  common way an audit goes wrong.
- **Every entry has a confirming measurement, and it is mandatory.** Run it on
  the unmodified baseline build, before you change any code. Its job is to
  distinguish this cause from the others in the same section. The after-the-fix
  benchmark does not replace it — that is gate 1's job and it comes later.
- **If the confirming measurement does not fire, the entry is wrong.** Drop it.
  Do not weaken it to a maybe and keep it in the report.
- **If you cannot run the confirming measurement on this machine**, the entry
  is not available to you. Say so, and rank it below every entry you could
  confirm.
- **One entry at a time.** Fix, re-measure under gate 1, then reconsider. When
  two entries in the same section both confirm, the second one's number is
  invalidated by the first fix — you must take it again.

No entry states a speedup, and none is ranked against another. The size of a
fix depends on the share of slots the bucket owns and the share of events the
cause owns, and both of those are numbers you measure, not numbers this file
can know. `cost-model.md` turns them into a ranking at gate 4. Anything you
would write as "the biggest single win" has to come from that arithmetic, with
the counters printed beside it.

Every entry states its cost in readability or portability, because most of
these trades are real and some of them are bad.

---

## `backend bound` — memory bound

The bucket most audits land in. Name the level first: L1, L2, L3, DRAM, or
store. The entries below split by level, and a fix aimed at the wrong level
does nothing.

### Array-of-structs when the loop touches few fields

**Symptom.** `memory bound` at L2, L3, or DRAM. The hot loop reads two or
three fields out of a large struct, and the bytes the hardware moves are far
more than the bytes the loop uses.

**Cause.** The cache line is the unit of transfer. Every line the loop pulls
in carries fields it never reads, so the effective bandwidth is the useful
fraction of each 64-byte line. A loop touching 24 bytes of a 96-byte struct
gets a quarter of the machine's bandwidth and no way to ask for more.

**Fix.** Struct-of-arrays for the hot fields, or a hot/cold split that keeps
the hot fields contiguous and moves the rest behind a pointer or into a
parallel array. The hot/cold split is the smaller change and usually the right
first move.

**Confirming measurement.** Compute the ratio of bytes moved to bytes used.
Bytes moved is line fills times 64 — `perf stat -e l2_lines_in.all` on Intel,
or `L1-dcache-load-misses` as a floor on any part. Bytes used is
`sizeof(hot fields) × iterations`, which you can count exactly. A ratio near 1
means the layout is not the problem and this entry is out. Cross-check with
`perf mem report`: the loads should show as served by L2 or worse, attributed
to the struct access. Without a PMU, `cachegrind`'s `D1mr` per source line
does the same job with a simulated cache.

**Cost.** SoA is invasive and permanent. It changes every call site, every
function that takes a `Particle&`, every serialization path, and every debugger
session — a single logical object no longer exists in memory. Once public API
depends on the layout you cannot walk it back. Hot/cold splitting is cheaper
but adds an indirection on the cold fields, which turns a cheap rare access
into a likely cache miss.

### Pointer chasing

**Symptom.** `backend bound` with low IPC. The profile concentrates on a load
whose address came from the previous load.

**This entry owns the chase even when level 2 says `core bound`.** The stall is
a dependency, not a bandwidth shortfall, so level 2 will call it `core bound`
as readily as `memory bound`, and a chase that stays resident in L1 or L2 will
call it `core bound` every time. Do not follow that label into the
dependency-chain entry in the core-bound section: that entry's confirming
measurement passes on a load chain and its fix does not apply to one. The test
is what the chain is made of, not which label level 2 printed.

**Cause.** Dependent loads serialize. The core cannot start load *n+1* until
load *n* returns, so out-of-order execution has nothing to overlap, and the
hardware prefetcher cannot predict an address it has not seen computed.

**Fix.** Flatten the structure into an array and traverse by index. Allocate
nodes from an arena so that traversal order matches address order and the
prefetcher can see a stream. Where the structure must stay linked, prefetch the
next-but-`D` node — but read the software-prefetch entry below before you do.

**Confirming measurement.** Break the dependency in a scratch copy of the loop.
Precompute the visit order into an index array, traverse that instead, and do
identical work per node — same nodes, same order, same arithmetic, only the
address dependency removed. If the stall does not move, the chase is not the
cause and this entry is out. This runs on any machine, needs no PMU, and is the
part you must do.

Supporting evidence where the host allows it: show that the loop is
latency-bound rather than bandwidth-bound by comparing its achieved memory
bandwidth against the machine's streaming peak. Neither number comes from plain
`perf stat` — `cost-model.md` gives the uncore IMC and UMC events for achieved
bandwidth and the STREAM/MLC commands for the peak, and both need `-a` plus
elevated privileges. Far below peak with a high stall count is the signature.
If you cannot run these on this host, say which half of the measurement you
have; the index-array experiment alone still confirms or kills the entry.

**Cost.** An arena changes the ownership and lifetime model of the whole data
structure, which is a design decision, not an optimization. Indices are weaker
than pointers: no type safety, no null, and invalidation on resize is silent
where a dangling pointer would at least be caught by a sanitizer. A flattened
structure resists incremental insert and delete until you add a free list, at
which point the addresses stop being ordered again.

### False sharing

**Symptom.** `memory bound` with an L3 or DRAM signature that the working set
does not explain. It appears only with more than one thread and gets worse as
threads are added; the single-threaded run is clean.

**Cause.** Two threads write different variables that share one cache line.
Each write invalidates the other core's copy, and the line ping-pongs between
cores at the round-trip cost in `cost-model.md`, paid per write, both ways.

**Fix.** Give each thread a private accumulator and combine once at the end —
prefer this. Where the shared object must stay shared, pad or align it to a
cache line.

**Confirming measurement.** `perf c2c record` then `perf c2c report --stdio`.
Read the HITM counts and the per-cache-line offsets: two hot offsets on one
line, touched by different PIDs or TIDs, is false sharing. The *same* offset
from several threads is true sharing — a different problem, and padding will
not touch it. `perf c2c` needs PEBS load-latency on Intel or IBS on AMD; see
`tma.md` section 4 for its privilege requirements.

**Cost.** Padding multiplies footprint. An array of per-thread counters padded
to 64 bytes is many times its useful size and can become a cache problem in
its own right. A hardcoded 64 is not portable: Apple M-series and IBM POWER use
128-byte lines, and Intel's adjacent-line prefetcher effectively pairs lines to
128 bytes, so 64 is sometimes not enough even on x86. Use
`std::hardware_destructive_interference_size` where the toolchain has it,
noting that GCC warns about its ABI stability under `-Winterference-size` and
that baking it into a public struct freezes an ABI to one compiler's guess.
`getconf LEVEL1_DCACHE_LINESIZE` reads the real value at build time.

### Capacity misses on a repeatedly traversed working set

**Symptom.** `memory bound` at L2 or L3. The miss rate jumps as the problem
size crosses a cache capacity, and the loop makes several passes over an array
larger than that cache.

**Cause.** Data is evicted between uses because the reuse distance exceeds the
cache. Nothing about the access pattern is wrong; there is simply too much of
it between the first touch and the second.

**Fix.** Block or tile the loop so each tile's working set fits the target
level. Where the passes are separable, fuse them so each element is touched
once per trip instead of once per pass.

**Confirming measurement.** Sweep the problem size and plot the level's miss
rate against working-set size. The knee must sit at the cache capacity from
`lscpu -C`; if it sits somewhere else, you are looking at conflict misses or a
prefetcher effect, not capacity, and tiling will disappoint. Then compute the
candidate tile's working set by hand and check it fits with room for the rest
of the loop's live data. After tiling, that level's miss counter should fall
while the retired instruction count stays roughly flat — if instructions rose
sharply, the tiling overhead ate the win.

**Cost.** Tiled loops are considerably harder to read than the loops they
replace, and the tile size is a machine-specific constant that goes stale
silently on new hardware. Watch for conflict misses: a tile whose row stride is
a large power of two will alias within a set-associative cache and keep
missing, and the fix for that — padding the row stride — makes the code harder
still to follow.

### TLB pressure on a large working set

**Symptom.** dTLB MPKI above 1 by the ratio in `tma.md` fallback A, and
page-walk cycles a meaningful share of total cycles. The working set is large
and touched with poor page locality.

**Cause.** The working set spans more pages than the TLB covers. With 4 KiB
pages and a second-level TLB of one to two thousand entries, coverage is only a
few MiB, so a larger working set walks the page table constantly. A walk is up
to four dependent loads, each of which can miss.

**Fix.** Huge pages. Transparent huge pages via `madvise(MADV_HUGEPAGE)` on the
specific mapping, or explicit `hugetlbfs` where you need the guarantee. Where
the pattern rather than the size is the problem, improving page locality — so
that a page's worth of data is consumed before moving on — beats huge pages
and costs nothing at deploy time.

**Confirming measurement.**
`perf stat -e dtlb_load_misses.walk_active,dtlb_store_misses.walk_active,cycles`
on Intel, or `ls_tablewalker.*` on AMD. The number is page-walk-active cycles
as a share of total cycles. Under a few percent, huge pages will not pay and
this entry is out. After the change, verify the pages were actually granted —
`AnonHugePages` in `/proc/<pid>/smaps` and `grep thp /proc/vmstat` — because a
`MADV_HUGEPAGE` that silently failed looks exactly like a fix that did not work.

**Cost.** This is a deployment change wearing a code change's clothes. The same
binary behaves differently depending on
`/sys/kernel/mm/transparent_hugepage/enabled`, which means your measurement and
production can disagree. Huge pages raise resident footprint through internal
fragmentation, and THP's defrag path can add allocation-time latency spikes to
a workload that previously had none — a bad trade for a tail-latency-sensitive
service. `hugetlbfs` is Linux-only and needs pages reserved at boot.

### NUMA-remote access

**Symptom.** `memory bound` at the DRAM level, and per-thread performance
depends on which socket the thread landed on. Bare `numastat`, which prints
node-level kernel counters, shows growth in `numa_foreign` and `other_node`
across the run — that is a machine-wide signal and it does not attribute to
your process.

**Cause.** The pages were faulted in on the wrong node. Linux allocates on
first touch, so the node is decided by whichever thread wrote the memory
first — usually a single-threaded initialization loop, not the parallel loop
that later consumes it.

**Fix.** First touch. Have each thread initialize exactly the memory it will
later work on, using the same partitioning as the compute loop, and pin threads
so the mapping holds. `numactl --cpunodebind --membind` places a whole process;
`--interleave` is the right answer for data that every node reads and that is
bandwidth-bound rather than latency-bound.

**Confirming measurement.** The cheap one first: run the unmodified binary
under `numactl --membind=0 --cpunodebind=0` and see whether the time moves. If
it does not, placement is not your problem. Then attribute it: `numastat -p
<pid>` is a *different* report from bare `numastat` — it prints this process's
resident MB per node, so it tells you where your pages ended up, not how many
foreign accesses the machine served. Use the bare form for the access signal
and the `-p` form for the placement, and do not treat one as evidence for the
other. Then `perf mem report`, whose data-source column distinguishes local
from remote DRAM and is the only one of these that attributes remote *accesses*
to your code, and `perf c2c report`'s remote-HITM column for the shared-line
case.

**Cost.** First touch couples the initialization loop's decomposition to the
compute loop's. Change one and you must change the other — with no compiler
error, no test failure, and a performance regression as the only signal. Thread
pinning fights the scheduler and is actively harmful on a shared machine or
under a container CPU quota. `numactl` and `libnuma` are Linux-only, so the
fix does not travel.

### Misaligned and split loads

**Symptom.** `memory bound` at the L1 level with the working set comfortably
resident. Split-load and store-forwarding-block counters are a non-trivial
share of loads. Common in packed structs, unaligned network or file buffers,
and hand-vectorized code using unaligned loads over a non-aligned allocation.

**Cause.** A load that crosses a 64-byte line boundary needs two accesses.
Separately, a load that is not fully contained within a preceding overlapping
store cannot be forwarded from the store buffer and must wait for the store to
commit. (4K aliasing is a third, related case; `tma.md` covers it — it is a
forwarding block, not a machine clear.)

**Fix.** Align the allocation and size the elements so hot vectors do not
straddle lines: `alignas`, `std::aligned_alloc` or `posix_memalign`,
`#[repr(align(N))]` in Rust. Drop `#pragma pack` on hot-path structs. For
forwarding stalls, make the load's size and offset match the store's, or keep
the value in a register instead of round-tripping it through memory.

**Confirming measurement.**
`perf stat -e mem_inst_retired.split_loads,mem_inst_retired.split_stores,ld_blocks.store_forward,ld_blocks.no_sr`
on Intel — check `perf list` first, as these names move between generations.
The number is splits and blocks as a share of total retired loads. Under a few
percent, alignment is not the story and this entry is out.

**Cost.** Alignment inflates struct size and therefore array footprint, which
pushes back on the layout entries above — you can pad your way from a split-load
problem into a capacity problem. Removing `#pragma pack` changes ABI and any
on-disk or on-wire layout that depended on it, which is a correctness change,
not a performance one. `aligned_alloc` has a size-multiple-of-alignment
requirement in C11 that C23 dropped and that implementations honour
inconsistently; check yours rather than assuming.

### Regular strided misses the hardware prefetcher cannot see

**Read the caution that closes this entry before you read the fix.**

**Symptom.** `memory bound` at the DRAM level, latency-bound rather than
bandwidth-bound, on an access pattern that is *regular* but outside what the
prefetcher tracks. The two common shapes: a stride large enough to cross a
4 KiB page boundary every step, which the L2 streamer will not follow, and an
indirect access `a[b[i]]` where `b` streams cleanly and `a` does not.

**Cause.** Hardware prefetchers detect sequential and simple strided streams
and, on Intel, stop at page boundaries. Outside that envelope they see nothing
and every access is a cold miss.

**Fix, in this order.** First change the pattern: sort or bucket the indices so
the indirect access becomes sequential; use huge pages so the streamer's page
limit stops applying; restructure so the far-apart accesses become near. Only
if all of those are measured and rejected, insert
`__builtin_prefetch(&a[b[i + D]], 0, 0)` with a distance `D` tuned by sweep.

**Confirming measurement.** Establish the precondition, which is that the
hardware prefetcher is not already covering this loop:
`perf stat -e l2_rqsts.all_pf,l2_rqsts.pf_miss` on Intel shows whether the
prefetcher is issuing for it at all. Where the host lets you measure achieved
bandwidth, add the latency-versus-bandwidth check from the pointer-chasing
entry — it is supporting evidence there and it is supporting evidence here, so
its absence does not block you. Then, if you insert a
prefetch, it is not confirmed by one run: sweep at least three distances,
re-measure each under the full gate-1 protocol with spread, and keep the change
only if the win exceeds the run-to-run spread at every distance around the
best one. A win at exactly one distance and nowhere near it is noise.

**Cost.** Readability: a `__builtin_prefetch` with a bare distance constant is
opaque at the call site. Nothing in the source says which microarchitecture the
constant was tuned on, and no reader can tell by inspection whether it still
earns its place. Portability: the builtin is GCC and Clang only — MSVC spells
it `_mm_prefetch`, Rust reaches it through `core::arch::x86_64::_mm_prefetch`
or the unstable `core::intrinsics::prefetch_read_data` — and the locality hint
argument, the useful distance, and the underlying instruction all differ across
x86, Arm, and generations within each. Maintenance: the constant is tuned once
against one part, one line size, and one memory configuration; no test
exercises it; when the machine changes it silently stops helping and keeps
costing. And it is a *permanent* tax for a *conditional* benefit — the prefetch
occupies an issue slot and a load port on every iteration whether or not it
helped that iteration.

**Caution — Drepper's, and it is the point of this entry.** In *What Every
Programmer Should Know About Memory*, §6.3, Drepper's conclusion about software
prefetching is that it is difficult to use correctly and frequently makes
things slower. The mechanisms hold today. A prefetch that lands too early
evicts a line that was still live. A prefetch that runs `D` elements past the
end of an array — the ordinary consequence of a fixed distance — reads a valid
but unrelated page, so it walks the page table and fills a line for data
nobody wants; that is the common waste, not the exotic one. (A genuinely
invalid address is the harmless case: the walk aborts, the prefetch is dropped,
and no fault is raised.) On some parts a stream of software prefetches
disrupts the hardware prefetcher's own stream tracking, so you lose prefetching
you already had. Treat this as the entry you reach last, after the layout
entries above have been tried and measured, and expect it to lose.

---

## `backend bound` — core bound

Execution resources, not memory. Level 2 has to say `core bound` before you
open this section; low IPC alone does not.

Two carve-outs to the gate, because two problems present outside it:

- **A dependency chain made of loads is not in this section.** If the serial
  chain is a load whose *address* came from the previous load, that is the
  pointer-chasing entry under memory bound, whatever level 2 called it — a
  chase that hits in L1 or L2 reads as `core bound` because it is a latency
  chain, and the dependency-chain entry below will appear to confirm on it and
  then fix nothing. See the exclusion in that entry.
- **Denormals present as `retiring` and as `bad speculation`, never as
  `core bound`.** The entry lives here because the fix is arithmetic, but you
  will arrive from one of those two buckets. `retiring` and `bad speculation`
  both point at it.

### Long loop-carried dependency chain

**Symptom.** `core bound` with low IPC and execution ports *not* saturated —
the machine is idle, waiting. The hot loop has a serial chain: one FP
accumulator summed across iterations, or any `x = f(x)` where `f` is an
arithmetic operation.

**Not this entry if the chain is made of loads.** `p = p->next`,
`x = a[x]`, or anything else where the next *address* depends on the last
load, is the pointer-chasing entry under memory bound. It matches this
symptom — a chase resident in L1 or L2 has cycles per iteration equal to the
load latency, so the confirming measurement below *passes* — and the fix here
does not apply to it, because splitting a serial address dependency into
independent accumulators is not a thing you can do. Check what the chain is
made of before you go further. If it is loads, go back.

**Cause.** Throughput is set by the chain's latency, not the machine's
throughput. An FP add is 3–4 cycles of latency and two can issue per cycle, so
a single accumulator leaves roughly seven eighths of the add capacity idle, and
adding cores or widening vectors changes nothing. That ratio is what the fix
recovers *inside the chain*; it is not the speedup. The gain you can actually
report is still capped by the `core bound` slot share and by Amdahl on the
region — `cost-model.md` does that arithmetic.

**Fix.** Split into N independent accumulators and combine at the end. N is the
chain latency divided by the reciprocal throughput in cycles per op —
equivalently, latency times the number of units that can execute it. FP add at
4 cycles latency on two ports gives N = 8; FMA at 4–5 cycles on two FMA units
gives N = 8 to 10. Read both numbers off an instruction table for your part;
they are not the same across microarchitectures.

**Confirming measurement.** Compute cycles per iteration from
`perf stat -e cycles` divided by the trip count, and compare against the chain
latency per iteration from an instruction-latency table. Equality is the
confirmation — *after* you have ruled out the load-chain case above, which
produces the same equality for a different reason. Cross-check with
`llvm-mca -mcpu=native -timeline` on the loop
body, which reports both the critical-path length and per-resource pressure;
if resource pressure rather than the chain is binding, this is the wrong entry
and the port-saturation entry below is the right one. `llvm-mca` is a static
model that assumes every load hits L1 and every branch predicts — it is
evidence about the chain, not about the loop's real behaviour.

**Cost.** This changes floating-point results. Summation order changes, so the
answer changes, and that is why no compiler will do it for you without
`-ffast-math` or `-fassociative-math`. If the code has a reproducibility
requirement, a bit-exact regression test, or a numerical-stability argument
that depends on the accumulation order, this fix breaks it and you must say so
before you propose it. The readability cost is small by comparison.

### Division or `sqrt` in a hot loop

**Symptom.** `core bound` with the divider busy for a large share of cycles.

**Cause.** The divider is not fully pipelined. Scalar `divsd` is roughly 13–20
cycles of latency with a throughput of one per 4–8 cycles, and `sqrt` is
similar, against one-per-cycle or better for nearly everything else. A handful
of divides in a loop body can dominate it.

**Fix.** Hoist a loop-invariant divisor and multiply by its reciprocal. Where a
divisor is reused across iterations, compute `1/y` once. Where the precision
budget allows, use `rsqrtps` or `vrsqrt14ps` plus a Newton–Raphson step. For
integer division by a constant, check the generated assembly first — compilers
already strength-reduce this when the constant is visible, and hand-rolling it
adds unreadable code for nothing.

**Confirming measurement.** `perf stat -e arith.divider_active,cycles` on
Intel; the number is divider-active cycles over total cycles. On Zen, use
`ex_div_busy` against `cycles`, with `ex_div_count` for the operation count —
but note these are *integer* divider counters, so they confirm the
integer-division-by-constant case and say nothing about scalar FP divide. For
FP divide on AMD, and for any part with neither counter, use
`llvm-mca -mcpu=native` on the loop body and read the divider port's pressure.
Under about 5% of cycles, this is not the cause and the entry is out.

**Cost.** Reciprocal multiplication is not the same operation as division.
`x * (1/y)` differs from `x / y` in the low bits, and it differs a great deal
more when `1/y` overflows, underflows, or flushes to zero for a `y` that
`x / y` would have handled. The fast reciprocal-square-root instructions give
about 12 bits (SSE `rsqrtps`) or 14 bits (`vrsqrt14ps`); one Newton–Raphson
step roughly doubles that, which reaches `float` precision and does not reach
`double`'s 53 bits without a second step. State the precision you are trading
before you trade it. `-ffast-math` makes the compiler do all of this globally,
which is a far larger and less reviewable change than doing it at one site.

### Port saturation

**Symptom.** `core bound` with *high* IPC. Not a stall — a throughput ceiling.
One execution port is pegged while others idle. The classic shapes are too many
shuffles for the single shuffle port, too many stores for the store-data port
on pre-Ice-Lake parts, and more loads than the load ports can serve — two on
Skylake-era parts, three on Golden Cove and later, which is itself a reason to
check the port map for your part rather than reusing a remembered one.

**Cause.** The loop's µop mix concentrates on one port, and the core cannot
issue past it no matter how much parallelism is available.

**Fix.** Change the mix, not the amount of work. Replace a shuffle with a blend
(different port), a variable shift with a multiply, a pair of loads with a load
plus a broadcast. Often the real answer is a data layout that needs no shuffle
at all, which puts you back in the memory section.

**Confirming measurement.** On Intel, per-port dispatch counters —
`uops_executed_port.port_*` on Haswell through Skylake, `uops_dispatched.port_*`
on Ice Lake and newer. Run `perf list | grep -i port` first; these names move
between generations exactly like the i-cache counters in `tma.md`. Portable
alternative: `llvm-mca -mcpu=native -timeline` prints per-port pressure and
names the binding resource. Same caveat as above — static model, perfect cache,
perfect prediction.

The number that decides it: µops dispatched to the busiest port, divided by
total cycles. One port at or above about 0.9 dispatches per cycle while the
others sit well below is saturation. Below about 0.7 on every port, nothing is
pegged and this entry is out — the loop is limited by something else and you
should be in the dependency-chain entry or back at level 2.

**Cost.** This is the least portable work in the catalog. The port map is
per-microarchitecture, so a mix tuned for Skylake can be neutral or worse on
Golden Cove and on Zen 4, and there is no warning when it goes stale. If the
binary ships to hardware you do not control, this entry is almost never worth
its maintenance cost. If you own the fleet and the fleet is homogeneous, it can
be.

### Denormals

**You arrive here from `retiring` or from `bad speculation`, not from
`core bound`.** The entry sits in this section because the fix is arithmetic.
The symptom is not.

**Symptom.** Performance collapses on specific inputs — decaying signals,
values converging toward zero, an audio tail — while the instruction count is
unchanged. In the TMA tree it shows as `retiring` with a large
heavy-operations share and as `bad speculation` / machine clears at the same
time; `tma.md` explains why both are correct.

**Cause.** On Intel, an operation producing or consuming a denormal takes a
microcode assist costing on the order of a hundred cycles or more. AMD handles
most denormal cases in hardware without an assist, which is why identical code
can be fast on one vendor and catastrophic on the other.

**Fix.** Prefer fixing the algorithm so denormals never arise: rescale, clamp,
or add a floor. Otherwise set flush-to-zero and denormals-are-zero in MXCSR —
`_MM_SET_FLUSH_ZERO_MODE(_MM_FLUSH_ZERO_ON)` and
`_MM_SET_DENORMALS_ZERO_MODE(_MM_DENORMALS_ZERO_ON)`.

**Confirming measurement.** `perf stat -e fp_assist.any` over the workload, on
Intel through Skylake; on Ice Lake and newer the event is `assists.fp`, so run
`perf list | grep -iE 'assist'` first. Large and correlated with the slow
region is the confirmation; zero
rules the entry out completely. Cross-check by running the *unmodified* binary
with FTZ and DAZ set at startup and re-measuring — if the time does not move,
denormals were not the cause whatever the counter said.

**Cost.** FTZ and DAZ change results and are not IEEE 754 conformant. They are
a per-thread CPU mode, so they apply to every piece of code running on that
thread, including library code that never asked for them and may depend on
gradual underflow. `-ffast-math` sets the mode process-wide through a static
initializer in `crtfastmath.o`, which is why building a shared library with it
is considered hostile — it changes the arithmetic of the program that loaded
you. If the code has an accuracy contract near zero, this fix violates it.

---

## `bad speculation`

Two entries here, and one elsewhere. If level 2 puts the weight on *machine
clears* rather than branch mispredicts, the two entries below do not apply —
machine clears are memory-ordering violations, self-modifying code, and FP
assists. For the FP-assist case go to the **Denormals** entry in the core-bound
section above; it presents from here and from `retiring`, never from
`core bound`. For memory-ordering clears from cross-thread sharing, go to
**False sharing** under memory bound. `tma.md` covers the split.

### Unpredictable data-dependent branch

**Symptom.** `bad speculation` above 20% of slots, branch miss rate above 5%,
and `perf record -e branch-misses:pp` concentrating on one branch whose
condition depends on data with no learnable pattern.

**Cause.** The predictor cannot learn a random condition, and each miss costs
15–20 cycles of pipeline refill.

**Fix, in this order.** Sort or partition the data so the branch becomes
predictable. This is frequently the largest and the least invasive change, and
it is the one people skip. Only then consider making it branchless: a ternary
that the compiler lowers to `cmov`, `std::min`/`std::max`, or a masked SIMD
operation. Note that you cannot reliably *force* `cmov` — GCC and Clang decide,
and `__builtin_expect_with_probability` and `-fno-if-conversion` only nudge, so
read the assembly and confirm you got what you asked for.

**Confirming measurement.** `perf stat -e branches,branch-misses` for the rate,
then `perf record -e branch-misses:pp -g` to attribute misses to the specific
branch. On AMD `:pp` resolves only for `cycles:pp`, so use `perf mem`/IBS or
fall back to `valgrind --tool=cachegrind --branch-sim=yes` and read `Bcm` per
source line. The number that decides it: misses attributable to *this* branch,
times 15–20 cycles, as a share of total cycles. Small product, no fix.

**Cost.** Branchless is *slower* when the branch is in fact predictable. It
executes both sides unconditionally, and a `cmov` converts a control dependency
the predictor could speculate past into a data dependency it cannot — which
lengthens the critical path and can drop you into the dependency-chain entry
above. Sorting costs its own time, which must be counted against the win, and
it may change an output order that callers silently depend on. Masked SIMD
code is harder to read and harder to test than the branch it replaced, because
both paths now always run and errors on the not-taken side stop being latent.

### Indirect call in a hot loop

**Symptom.** `bad speculation` with the misses on an indirect branch
(`br_misp_retired.indirect` on Intel, `Bim` in cachegrind), often alongside
`frontend bound` / fetch latency from the resteer. Virtual dispatch, a function
pointer, or a tag switch inside the loop.

**Cause.** The indirect target predictor holds a bounded set of targets per
site. A site that alternates among many callees mispredicts, and it costs
twice: the mispredict itself, and the fact that an opaque call blocks inlining,
so the callee's work stays invisible to the optimizer.

**Fix.** Try the compiler first: LTO plus PGO lets it speculatively devirtualize
the dominant target with a guarded direct call, which costs you no design
change at all. Then design changes, cheapest first: `final` on the class or
method so the compiler can prove the target; hoisting the dispatch out of the
loop by grouping objects by type and running a monomorphic loop per group; a
tagged variant with a switch.

**Confirming measurement.** `perf stat -e br_misp_retired.indirect` against
`br_inst_retired.indirect` on Intel for the indirect miss rate. These are Ice
Lake and later; on Skylake-era parts they are *absent*, not renamed, so
`perf list | grep -i indirect` coming back empty means you have no indirect
breakdown on this host and must use the fallback. Then
`perf record -e branch-misses:pp -g` to confirm the site. Portable fallback:
`valgrind --tool=cachegrind --branch-sim=yes` and read `Bim` per call site,
which simulates an indirect predictor and works everywhere. If the site turns out to be
effectively monomorphic on this workload, the predictor is already handling it
and your cost is lost inlining, not misprediction — a different problem needing
`final` or LTO, not a redesign.

**Cost.** `final` closes the type to extension; that is an API decision made
for a performance reason, and it will outlive the reason. Sorting objects by
type changes their memory order and can cost you locality that another loop
depended on. Type-grouped loops duplicate the body per type and grow the text
segment, which pushes directly against the `frontend bound` section below. LTO
and PGO change the build, the build time, and the CI story, and PGO needs a
representative profile that somebody has to keep current.

---

## `frontend bound`

Rare in tight numeric loops. Expect it in large branchy binaries with flat
profiles — interpreters, databases, browsers. All three entries here are about
code size and code layout, never about data.

### Over-inlining blowing the i-cache

**Symptom.** `frontend bound` / fetch latency with i-cache MPKI meaningful by
the `tma.md` fallback-A ratio. Large text segment, flat profile. Often
correlates with an inlining-threshold change or a header full of templates
instantiated everywhere.

**Cause.** Inlining duplicates code. Once the hot working set of *instructions*
exceeds the L1i, every call fetches from L2 or further, and the front end
starves a back end that has nothing wrong with it. L1i is 32 KiB on Skylake,
Golden Cove, and all Zen, 48 KiB on Ice Lake-SP, and 64 KiB on Granite Rapids —
read yours from `lscpu -C` rather than assuming, because the whole calculation
is a comparison against that one number.

**Fix.** PGO is the principled version — it inlines by measured hotness instead
of by heuristic. Failing that, inline discipline by hand:
`__attribute__((noinline))` on cold helpers, `[[gnu::cold]]` on error paths, a
lower `-finline-limit` or `inline-unit-growth` on GCC or `-mllvm
-inline-threshold` on Clang, and moving template bodies out of headers.

**Confirming measurement.** `perf stat -e L1-icache-load-misses,instructions`
for the MPKI, the Intel i-cache stall counter named in `tma.md`, and `size -A`
plus `perf report --sort=dso,symbol` for how much text is actually hot. Then
the direct test: rebuild with only the inlining knob changed and re-measure
under gate 1. If i-cache MPKI is under about 1, this is not the entry.

**Cost.** `noinline` is honoured as a command, and it blocks every downstream
optimization that inlining would have enabled — constant propagation, dead
branch elimination, escape analysis. A global inline-threshold change is a
blunt instrument applied to every function in the translation unit, most of
which you did not measure. Both go stale as the code moves and nobody
re-measures them, so they become superstition in the codebase.

### µop-cache misses from huge unrolled bodies

**Symptom.** `frontend bound` / fetch bandwidth. `idq.dsb_uops` low relative to
`idq.mite_uops`, `dsb2mite_switches.penalty_cycles` meaningful. Those counter
names are Intel-only, but the problem is not: Zen 3 and later have an op cache
with the same failure mode, measured with `de_src_op_disp.op_cache` against
`de_src_op_disp.x86_decoder` — the direct analogue of the DSB-versus-MITE
ratio. The allocation rules and therefore the useful unroll factor differ
between the two vendors, so re-sweep rather than porting a tuned constant.

**Cause.** The µop cache holds a bounded number of µops per 32-byte code region
under strict allocation rules. A loop body unrolled past that falls out to
legacy decode, which is narrower, so the front end delivers fewer µops per
cycle than the back end could accept.

**Fix.** Unroll less. Where the compiler did it, cap it: `#pragma GCC unroll N`,
Clang's `#pragma clang loop unroll_count(N)`, or `-fno-unroll-loops` on the
specific unit. Sweep N and measure each value.

**Confirming measurement.**
`perf stat -e idq.dsb_uops,idq.mite_uops,dsb2mite_switches.penalty_cycles` on
Intel, or `perf stat -e de_src_op_disp.op_cache,de_src_op_disp.x86_decoder` on
Zen 3 and later — run `perf list` first, the names move between generations.
The number is µops delivered from the µop cache as a share of total delivered
µops; a high share rules the entry out.
`llvm-mca` cannot help here: it models the scheduler and the ports and assumes
a perfect front end, so it does not see the DSB at all.

**Cost.** Unrolling less re-exposes the dependency chain the unroll was hiding,
so this entry and the accumulator-splitting entry pull in opposite directions.
That is precisely why you cannot tune both at once — change one, re-measure,
then reconsider the other. The pragmas are compiler-specific and the other
compiler ignores them without a word.

### Cold-path code inline with the hot path

**Symptom.** `frontend bound` / fetch latency, and `perf annotate` shows the
hot loop's bytes interleaved with error handling, logging, or assertion code
that never executes. The fetched lines are mostly dead bytes.

**Cause.** Instruction fetch works in 64-byte lines, exactly like data. Cold
bytes sitting on a hot line waste i-cache capacity and fetch bandwidth in the
same way an unread struct field wastes a data line — this is the AoS entry,
applied to code.

**Fix.** Move cold paths out of line: `[[unlikely]]`, `__builtin_expect`, or
`[[gnu::cold]]` on the slow branch; put the slow path in its own `noinline`
function; let `-freorder-blocks-and-partition` put cold blocks in
`.text.unlikely`, which GCC does at `-O2` when it has profile data. PGO does
this correctly and without guessing.

**Confirming measurement.** `perf annotate --stdio -s <symbol>` and read the
layout — hot basic blocks should be contiguous, and if they already are, this
entry is out. After the change, `size -A` should show a non-empty
`.text.unlikely`, and i-cache MPKI should fall. Same floor as the entry above:
under about 1 MPKI, do not do this.

**Cost.** `[[unlikely]]` writes a claim about runtime behaviour into the
source. When the claim is wrong, the compiler pessimizes the path that is
actually hot, and nothing anywhere tells you — it is a silent performance bug
that reads as an optimization. Hand annotation is guessing at what PGO would
have measured, so prefer PGO wherever the build system can carry a profile.

---

## `retiring`

There is no fix list here, and that is the finding.

High `retiring` means nothing is stalled. The core is executing at close to
its issue width and the microarchitecture is not the problem — the instruction
count is. You are not going to find a stall to remove, because there isn't one.

**Check this first.** Level 2 splits `retiring` into light and heavy
operations. A large heavy-operations share means the microcode sequencer is
running — denormal assists, `rep movsb`, gather and scatter — and those are
retired µops that buy nothing. That is deletable work masquerading as useful
work, and it is the only thing in this bucket that behaves like a conventional
fix. `tma.md` covers it; the denormal entry above is the common case.

Otherwise there are three roads, and they are not interchangeable:

1. **A better algorithm.** Complexity beats constants, and this is the only
   one of the three whose gain is not capped by the hardware.
2. **Do less work.** Not a menu — pick the one your profile points at, and each
   has its own discriminating measurement, because retired instruction count
   alone cannot tell these apart:
   - *Loop-invariant computation.* Read `perf annotate` on the loop body and
     find the instruction that recomputes a value nothing in the loop changed.
     If the compiler already hoisted it, it is not in the loop body and there
     is nothing to do.
   - *Redundant copies.* Count them directly rather than inferring: a
     `perf record` on the allocator and `memcpy`/`memmove` symbols, or
     `ltrace`/a `malloc` counter, gives copies and allocations per iteration.
     The target is that number falling, not the cycle count.
   - *Recomputation across calls.* Instrument a hit/miss counter on the value
     you propose to cache. A cache with a low hit rate is a slowdown; measure
     the rate before you build it.
   - *A redundant pass.* Count passes over the data and multiply by the working
     set. Fusing two passes should roughly halve the line fills at whichever
     cache level the working set exceeds — check `L1-dcache-load-misses` or the
     level's counter, not `instructions`.
3. **Do more per instruction.** Vectorize — but check whether the compiler
   already did before you write anything: `-fopt-info-vec-missed` on GCC,
   `-Rpass-missed=loop-vectorize` on Clang. Read *why* it declined. The usual
   answers are possible aliasing (which `restrict` / `__restrict__` may
   resolve), a loop-carried dependency, an unknown trip count, or a layout that
   would need gathers — and the last of those sends you back to the AoS entry.

**Confirming measurement.** For road 1, stop counting cycles and count
operations. Instrument the algorithm's own unit of work — comparisons, node
visits, bytes hashed, tuples examined — and compare the count against the
theoretical minimum for the problem. If the constant factor is already close to
that bound, the algorithm is not the problem and roads 2 and 3 are all that is
left. Road 2's four cases each carry their own measurement above, because
retired instruction count cannot discriminate among them.

For road 3, `instructions` falling is necessary but not sufficient — you also
have to show the work moved into vector lanes. On Intel, count it with
`fp_arith_inst_retired.*`, whose unit masks are per width and per type
(`.256b_packed_double`, `.512b_packed_single`, and so on): the packed masks
should rise and the scalar ones fall. There is no equivalent counter for
integer SIMD, so for that case count statically instead —
`objdump -d ./bench | grep -cE '%[xyz]mm'` over the hot symbol, before and
after. If neither number moved the way you predicted, the change did not do
what you claimed regardless of what the wall clock says.

**Cost.** Intrinsics are the least portable and least readable code most
codebases contain, and they must be maintained per ISA with a scalar fallback
that will silently rot because nothing exercises it. Reach for them in this
order: restructure the data so the compiler auto-vectorizes; then a portable
wrapper (`std::experimental::simd`, `std::simd` where available, Highway;
`std::arch` behind `is_x86_feature_detected!` in Rust); then intrinsics.
Algorithm changes cost review time and carry real correctness risk, but per
unit of gain they are usually the cheapest thing on this page.
