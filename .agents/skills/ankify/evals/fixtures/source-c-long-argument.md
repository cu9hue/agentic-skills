# Reading notes — Saltzer, Reed & Clark, "End-to-End Arguments in System Design"

ACM Transactions on Computer Systems, vol. 2 no. 4, Nov 1984, pp. 277–288.
Earlier version presented at the 2nd International Conference on Distributed
Computing Systems, Paris, April 1981. Authors were all at MIT's Laboratory for
Computer Science; Saltzer came out of the Multics project.

Read straight through, notes in reading order.

---

## The setup

Paper is about *where* to put a function in a layered system. Layered design
gives you a choice: you can implement a given function at a low level (inside
the communication subsystem), at a high level (in the application), or at both.
The paper argues there is a principled way to choose, and that the intuitive
answer — push it down, make the plumbing reliable — is usually wrong.

They call the argument a "class of system design arguments", not a theorem.
Explicitly framed as a rule of thumb, a guideline for design analysis. They say
it does not decide cases by itself; it tells you which questions to ask.

## The careful file transfer example

The whole first half hangs on one worked example. Host A has a file on disk.
Move it to host B's disk. It must arrive intact.

Enumerate what can go wrong (they list five categories):

1. Disk read error on A, or write error on B.
2. Software bug in the file system or the transfer program — buffering and
   copying is where these bite.
3. Transient error in processor or memory on either host while buffering.
4. The network drops, corrupts, duplicates, or reorders packets.
5. Either host crashes part-way through.

Note the shape of that list: only item 4 lives in the network. Everything else
is above or below it.

So suppose you build a perfectly reliable network. Item 4 goes away. Have you
solved the problem? No. The file can be corrupted in host A's memory *before*
it is handed to the network, or in host B's memory *after* it comes out. A
perfect channel between two corruptible endpoints does not give you a correct
file transfer.

What does solve it: the file transfer application computes a checksum over the
file, sends it along, and B recomputes and compares after writing to disk. On
mismatch, retry. This works regardless of how bad the network is — and it is
the *only* thing that works, because it is the only check that spans the whole
path from A's disk to B's disk.

## The central claim

Stated in the paper roughly as: the function in question can be completely and
correctly implemented only with the knowledge and help of the application
standing at the endpoints of the communication system. Therefore providing that
function as a feature of the communication system itself is not possible.
Sometimes an incomplete version at the low level is useful as a performance
enhancement.

Two consequences the authors draw out:

- The low-level version is **redundant for correctness**. The endpoint check has
  to exist anyway, and once it exists the low-level check adds no correctness.
- Cost of the low-level version is **paid by every client**, including clients
  that do not need it.

## The performance caveat — this is not "never do it low"

They are careful here and I nearly misread it. The argument does *not* say the
network should be unreliable or that hop-by-hop error handling is wasted. It
says the low-level function cannot be justified on **correctness** grounds, and
must instead be justified on **performance** grounds, as an engineering
tradeoff.

The mechanism: if the network loses packets at a high enough rate, an
end-to-end retry means retransmitting the whole file, and the expected time to
complete a large transfer can grow without bound. A hop-by-hop retransmission
scheme keeps the end-to-end retry rate low enough to be affordable. So the low
level is doing *probability management*, not correctness.

The tradeoff has a second edge: too strong a low-level function actively hurts
the clients who did not ask for it. Their example is real-time packet voice.
A voice application would rather receive a packet with a gap or a click than
wait for a retransmission — the retransmission arrives too late to be played
and the delay damages the conversation. A network that guarantees delivery by
retrying imposes unbounded delay on an application whose whole requirement is
bounded delay.

That reframes the design question. Not "how reliable should the network be" but
"how reliable, before the cost to indifferent clients exceeds the benefit to
the ones who want it".

## Identifying the ends

Subtle point that I think is easy to skip. Applying the argument requires you
to know where "the ends" are, and that is not a property of the network — it is
a property of the application.

For file transfer, the ends are the two disks. For a voice conversation between
two people, the ends are the speaker's mouth and the listener's ear, and the
correctness criterion is intelligibility to a human, not bit-exactness. For a
voice *recording* being shipped for later playback, the ends move — now
bit-exactness matters again and delay does not, so the same data type flips its
answer based on the application around it.

Same bits, different ends, opposite design. The argument has no content until
you fix the application.

## The case studies

Second half is a run of applications of the argument. Notes on each:

**Delivery acknowledgement.** The network can tell you it delivered a packet.
That is not what the sender wanted to know. The sender wants to know the
*target application acted on it* — wrote the record, debited the account. A
network-level ack says the bits arrived at the far host, which is compatible
with the far application having crashed before doing anything. Only an
application-level response answers the real question.

**Secure transmission of data.** Link-level encryption protects a wire. It does
not protect against a compromised intermediate node, which sees plaintext at
every hop, and it does not protect against errors or malice inside the hosts
themselves. Also authentication has to be end-to-end: if the network vouches for
the sender, you are trusting the network. If the application encrypts and
authenticates, it need not trust the network at all — and then the link-level
encryption is, again, redundant for correctness.

**Duplicate message suppression.** The network can suppress duplicates it
generated. It cannot suppress a duplicate the *application* generated — when an
application resends after its own timeout, that resend is a brand new message as
far as the network is concerned. So the application needs its own duplicate
detection regardless, and the network's is redundant.

**FIFO message delivery.** The network can order messages within one connection.
An application using several connections, or reconnecting after a failure, gets
no ordering guarantee across them and must sequence for itself.

**Transaction management.** Two-phase commit is offered as the end-to-end case:
the commitment decision belongs to the application that knows what the
transaction means, and cannot be delegated to a lower layer.

Pattern across all five is identical, which I think is the point of running
five of them: the low-level mechanism handles a *subset* of the failure cases,
the application still needs the full check, and the full check subsumes the
subset.

## Closing threads

They note the argument works as a design analysis tool, not a decision
procedure — it identifies what the application must do for itself, and only
then can you argue about what the network should do as an optimization.

They also observe the argument gets rediscovered constantly under other names,
and that layered systems tempt designers toward putting function low because
that is where it looks tidiest and where a single implementation serves
everyone. That temptation is the thing the argument exists to resist.

Passing remark near the end that the same reasoning shows up in RISC-vs-CISC
processor debates — keep the low level simple and fast, push the specialized
function up. Not developed, just noted.
