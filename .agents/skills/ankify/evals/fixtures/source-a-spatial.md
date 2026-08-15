# Notes: TCP wire format and connection lifecycle

## Header layout

A TCP segment starts with a 20-byte fixed header, laid out in 32-bit words.
Word 0 holds the source port (bits 0-15) and destination port (bits 16-31).
Word 1 is the sequence number. Word 2 is the acknowledgement number. Word 3
packs the data offset (4 bits), a reserved field (4 bits), the eight flag bits
(CWR, ECE, URG, ACK, PSH, RST, SYN, FIN), and the receive window (16 bits).
Word 4 holds the checksum and the urgent pointer. Options, if any, follow, and
the data offset field says where the payload actually begins — which is why the
field exists at all: options make the header variable-length.

## Connection lifecycle

A connection walks a state machine. The passive side sits in LISTEN. On
receiving a SYN it sends SYN+ACK and moves to SYN_RECEIVED. The active side
leaves CLOSED by sending SYN into SYN_SENT, and on SYN+ACK it replies ACK and
reaches ESTABLISHED. Teardown is asymmetric: the side that closes first sends
FIN and passes FIN_WAIT_1 -> FIN_WAIT_2 -> TIME_WAIT; the peer passes
CLOSE_WAIT -> LAST_ACK -> CLOSED.

TIME_WAIT lasts 2*MSL. The reason is not politeness: a delayed duplicate
segment from the old connection could otherwise arrive during a new connection
that reuses the same four-tuple and be accepted as valid data. Waiting twice
the maximum segment lifetime guarantees every straggler has died.

## Why the checksum covers a pseudo-header

The TCP checksum is computed over a pseudo-header containing the source and
destination IP addresses and the protocol number, plus the real header and the
payload. This deliberately breaks layering. It exists so a segment misdelivered
to the wrong host, or handed up under the wrong protocol number, fails the
checksum instead of being accepted.
