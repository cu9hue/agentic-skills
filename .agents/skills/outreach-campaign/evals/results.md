# outreach-campaign — eval results

Append-only. Newest at the bottom.

## 2026-10-09 — initial A/B (uncommitted, on top of 9961ae7)

Arms: A = no skill, B = skill (SKILL.md + reference read by the arm). No
tools beyond reading the skill. n=1 per cell — signal, not proof. Blind
judge saw arms as teams X/Y, order shuffled per scenario.

RED (baseline before drafting): S1 asked open questions instead of stating
defaults, proposed a 20-minute call and offering a findings summary (breaks
"never promise insights"), never gated on the exclusion list. S2 kept
Klarwerk (US HQ, EU team and customers) as "your call". S3 put all four on
Variant B, ignored the subject and hook formats, asked for 20 minutes,
dropped "Thanks," and sent the accept_all contact email only. S4 gave sound
generic advice but no email verification, no reply-rate expectation, no
advice framing. S5 fine.

- S1: **B** — all missing inputs in one message, defaults stated (US only,
  never EU, $2, 15–20, 2 per company), B question proposed, nothing spent
  before the exclusion list and Notion page. A missed three of five bullets.
- S2: **B** — rejected Klarwerk on geography without asking, Their
  customers per company, skip-list drops named. A punted Klarwerk to the
  user and left Meridian's priority open.
- S3: **B**, decisively — B passed all eight bullets; A passed only the
  LinkedIn length bullet. Judge flagged that strict A/B alternation by
  priority order gave B to the LinkedIn-only CTO, so the B question reached
  nobody.
- S4: **B** — seven of seven concerns as the organizing thread; A hit about
  two cleanly. Judge noted B leaks "treg" and "Variant B" jargon and says
  nothing about running the call itself (outside this skill's scope).
- S5: **B**, narrowly — both stayed a plain reply; B kept the 15-minute ask
  and added the Status reminder, A invented a 25-minute call and agenda.

Judge verdict: skill arm won 5 of 5. Obsolescence: no (baseline failed S1,
S2, S3 and the S4 probe).

Follow-up edit from the judge's S3 finding: Variant alternates only across
priority-1 people with an email channel; LinkedIn-only and priority 2/3 get
A. S3 rubric tightened to match. Rerun of S3 (arm **C**, n=1): Dana A,
Priya B, Sam and Lee A; every other S3 bullet held; it also flagged Sam's
hook nearing the 12-month edge. Post-edit arm holds.

## 2026-10-16 — edit: question-first urgency, personalization tiers (uncommitted, on top of e463627)

Edit: drafts lead with the campaign's lead question, carry a two-week
deadline and ask for a call this week; the Variant A/B split is gone. Step
6 personalizes by priority (P1 connection + work fact, P2 one work fact,
P3 none) and records a Personalization field. Connections come from a new
sender profile: school, past employer or field, EF and communities. Email
hook is now the "why you" line ("Asking you because…"). S1, S3 and S4
rubrics updated; S3 rewritten with connections, a city trap and a P3
person.

Arms: A = no skill, B = pre-edit skill, C = post-edit skill. No tools
beyond reading the skill. n=1 per cell — signal, not proof. One blind
judge per scenario, arms shuffled into teams X/Y/Z.

- S1: **C** 6/6, B 4/6, A 1/6 — C alone asked for schools and past
  employers and proposed a single lead question; B proposed the old
  compound Variant B paragraph.
- S2: **B = C** 6/6, A 5/6 — screening unchanged by the edit; A missed a
  plural-noun buyer on one row.
- S3: **C** 6/8, B 3/8, A 0/8 — C applied tiers (Dana `work` with Boston
  rejected, Sam and Priya `both`, Rowan `none` despite an EF tie), the
  hook, subject and channel rules, and the new template. Misses: Priya's
  MIT source sat outside Notes, LinkedIn notes not shown, and it claimed
  to have "added" the background to the sender profile with no tools. B
  kept "next week or two, happy to work around your schedule". A used
  Boston and EF, pitched background lines, asked for 20 minutes.
- S4 (probe): **C** 9/9, B 7/9, A ~2/9 — only C raised tiered research and
  question-first, this-week urgency unprompted.
- S5 (negative): **B**, narrowly; C passed every bullet and stated no call
  length; A changed the call to 20 minutes. No over-triggering.

Verdict: post-edit arm holds (won or tied 4 of 5; passed every bullet on
S5). Obsolescence: no (baseline failed S1, S3 and the S4 probe).

Follow-up from the S3 judge: step 6 now says connection sources go in
Notes too. Clarifies an existing rule; not rerun.

## 2026-10-16 — edit 2: ultra-short draft with competence and FOMO (uncommitted)

The user rejected edit 1's draft: "picking what to build" read as unsure,
and the ask needed to be this week, with FOMO and a competence signal. New
draft, chosen by the user from three options: insider lead question, then
"{Intro or credential}. Talking to the few founders {cohort} this week[,
and {hook} puts you on that list]. 15 min Thu or Fri?". New fields:
Intro (credential line naming a connection) and cohort; Email hook is now
a 1–5 word noun phrase; LinkedIn hook dropped (the note reuses the email
fields). S1, S3 and S4 rubrics updated; S3 prompt now gives an insider
lead question and a cohort.

Arms: A = no skill, B = pre-edit skill (e463627), C = post-edit skill.
C reran on all five. A and B reran on S3 only, because only the S3 prompt
changed; their round-1 outputs were reused elsewhere and judged against
the new rubrics. Fresh blind judges, shuffled teams. n=1 per cell.

- S1: **C** 6/6, B 4/6, A 1/6 — only C proposed the cohort and asked for
  schools and past employers.
- S2: **B = C** 6/6 on the rubric, A 5/6; the judge broke the tie toward B
  because C miscounted its own rejects in its opening line.
- S3: **C** 8/8, B 2/8, A 0/8 — tiers, Intro, hook, subjects, channels and
  template all correct; the outside-reader check also picked C's email.
  Misses: C rewrote the user's 17-word lead question to fit a 15-word cap,
  and put Rowan on hold because the cohort didn't cover a testing vendor.
- S4 (probe): **C** ~8.5/9, B 7/9, A ~3/9 — only C raised the insider
  question, cohort FOMO and named days. It leaked the reference's example
  names ("Harbor Trust") into general advice.
- S5 (negative): **B**; C kept 15 minutes but offered Columbus Day and
  added a Calls-row step; A changed the call to 20 minutes.

Verdict: post-edit arm holds (won or tied 4 of 5). Obsolescence: no.

Follow-ups, not rerun: the lead-question cap goes from 15 to 18 words to
fit the question the user approved, and the cohort rule now says to
broaden the cohort rather than drop a priority-3 person.

## 2026-10-16 — edit 3: sender comes from kickoff, per-row sender fields (uncommitted)

The user: the sender profile depends on the sender, so discuss it before
outreach and skip connections when nothing is relevant. The hardcoded
sender profile is gone. Step 0 asks for the sender's name and credential
line and their background, proposes which parts matter for this ICP, and
agrees a short list with the user; "none" skips the connection search.
The first S6 run found that per-campaign formula text signs every row
as one sender, so Sender and Credential became row properties that the
formulas read. S1 rubric updated; S3 prompt states the sender; new S6:
a cofounder sends with no relevant background.

Arms: C reran on S1, S3, S4 and S6 (S6 after the per-row fix). A and B
ran on S6; their round-2 outputs were reused for S1, S3 and S4 (the S3
prompt only added the sender line). Fresh blind judges. n=1 per cell.

- S1: **C** 6/6, B 4/6, A 1/6. C asked who sends, asked for the
  background, offered to agree a short list and allowed "none". Weak
  spot: it guessed the sender's credential from the reference example
  before asking.
- S3: **C** 8/8, B 2/8, A 0/8. It widened the cohort to cover the P3
  testing vendor instead of dropping him, and asked the user to confirm.
- S4 (probe): **C** 9/9, B 7/9, A ~2/9.
- S6: **C** 5/5, A 1/5, B 1/5. Personalization was `work` for both, no
  Intro even though Sam shared EF and quant history with the other
  sender, Alex's credential, "Thanks, Alex". B kept the old low-urgency
  draft. A floated the EF overlap.

Verdict: post-edit arm holds (won all 4 reruns). S2 and S5 not rerun;
the edit doesn't touch screening or replies. Obsolescence: no.

## 2026-10-16 — edit 4: a yes before any tracker work, optional parts

The user asked for consent before tracking, with optional parts. A new
hard rule says the skill never creates or changes the tracker without a
yes. Step 0 proposes the setup: the Outreach database is the core; the
Calls database, the views and the draft formulas can each be skipped;
"no tracker" means dedupe against the exclusion list and rows go in the
report. Migrating an older tracker also needs a yes. New S1 bullet.

Arms: C reran on S1; A and B round-3 outputs reused. Fresh blind judge.
n=1.

- S1: **C** 7/7, B 4/7, A 1/7. C listed every skippable part and allowed
  "no tracker". B announced it would create both databases.

Verdict: post-edit arm holds.
