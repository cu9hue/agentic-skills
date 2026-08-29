# Writing for the ear

Load this when the piece will be heard, not read: video voiceovers,
podcast scripts, talks, TTS narration. Prose guidance assumes a reader
who can re-read; this assumes a listener who cannot.

## The one difference everything follows from

A reader controls the pace and can look back. A listener gets one linear
pass at a speed someone else chose, holding everything in working memory.
Every unresolved dependency you open costs them a slot, and slots are few.

So the goal is not brevity. It is **low resolution cost**: nothing held
open longer than a breath.

## Sentence shape

- **Subject and verb early, and adjacent.** English listeners resolve
  meaning at the verb. Anything before it is held in suspense.
- **Never centre-embed.** "The trader the firm hired quit" is trivial on
  the page and near-unparseable aloud. Split it: "The firm hired a
  trader. He quit."
- **Branch right, not left.** "The cost that matters is adverse
  selection, which happens when..." — not "Adverse selection, which
  happens when..., is the cost that matters."
- **One clause per breath.** If you run out of air reading it, it is too
  long, regardless of the word count.
- **Vary the length deliberately.** A run of same-length sentences reads
  as monotone whatever the voice does. A short one after a complex one is
  a beat to catch up. Fragments are legitimate. Use them.

## Information order

- **Given before new.** Open a sentence with something already
  established; end it with the new thing. Listeners rely on this and
  notice when it is violated, even if they cannot say why.
- **The important word goes last.** Stress falls at the end of a sentence
  naturally. Put the payload there and the prosody does your emphasis for
  free.
- **Announce structure before detail.** "There are three costs. The first
  is..." Without the announcement the listener does not know they are in
  a list until it ends.
- **Concrete before abstract.** A specific case, then the generalisation.
  The reverse asks them to hold an abstraction with nothing to attach it
  to.

## Reference

- **Repeat the noun.** A pronoun more than one sentence from its
  antecedent is ambiguous by ear even when it is unambiguous on the page.
- **Never "the former" or "the latter."** Both require scrollback that
  does not exist.
- **Never open with a bare "This."** "This means..." — this *what*? Say
  "This gap means", "This delay means".

## Numbers

- **Round hard.** "About a hundred thousand" beats "106,782". The
  precision is unusable by ear and the digits are expensive to hold.
- **Give a comparison, not just a magnitude.** "Twice the spread", "about
  a microsecond — a thousand times faster than a blink." A number alone
  has no scale to a listener.
- **Write them as they are spoken** and check what the model does with
  symbols, units and abbreviations.

## Redundancy — where prose guidance inverts

"Cut every word doing no work" assumes re-reading. It does not hold here.
A word can carry no meaning and still carry **processing time**.

- **Say the load-bearing thing twice, differently.** Once to state it,
  once to let it land. This is not padding; it is the listener's version
  of re-reading.
- **Preview and recap at section boundaries.** Short. One sentence each.
- **Signpost verbally.** "Here's the thing", "so", "but", "which means"
  do the work that paragraph breaks do on the page. They are structure,
  not filler, and cutting them leaves prose that is dense to read and
  impossible to follow.

## Technical content specifically

- **One new concept per hundred words, maximum.** Two in a paragraph and
  the second is lost.
- **Define on first use, in-line, immediately.** Not in a later aside.
- **Then never vary the term.** Synonyms are good prose and bad
  explanation: the listener has to work out they refer to the same thing.
- **Anchor every abstraction to a number or a scene** within a sentence
  or two of introducing it.

## What breaks the voice model

- **Homographs.** *lead*, *read*, *live*, *bass*, *close*. Rewrite rather
  than gamble.
- **Acronyms and abbreviations.** Decide whether it is spelled out or
  said as a word, then write it that way.
- **Symbols.** `%`, `$`, `→`, `≈` are unreliable. Write the words.
- **Anything you would not say.** If the sentence only works written
  down, it will sound wrong.

## Punctuation is functional in this pipeline

Not only stylistic. Two mechanisms read it:

- **Sentence ends split the script into TTS chunks.** Chunk boundaries
  are where prosody resets, so a full stop in an odd place is audible.
- **Clause punctuation groups the captions.** Commas and full stops are
  the preferred break points, so where you put them decides how the
  subtitles land.

A comma is a real instruction here, not decoration.

## The test that beats every rule above

**Read the draft aloud, at pace, in one take.** Anything that trips your
mouth will trip the listener's ear.

Then **listen to the generated audio without watching the video.** If you
lose the thread with no visual support, the writing is carrying less than
you think it is — the diagram was propping it up.
