# S5 baseline (no skill) — negative scenario, landing copy

**Prompt:** "Write the hero section copy for my API monitoring product. The
audience is backend engineers at mid-size SaaS companies."

**Rubric outcome:** partial pass, with a pre-existing over-trigger tendency.

- Wrote the copy: **yes**, two hero variants built on two different positioning guesses.
- Did not interrogate the market: **no**. Opened with "describes a category, not a
  position," then five numbered questions, three of which are market questions
  (what breaks that incumbents miss, who feels the pain first, the top objection).
- "At most one short line of market-adjacent observation": **failed**. The
  interrogation is the first half of the response, and it closes by asking the
  founder to answer question one before it writes real headlines.

**What this tells the skill.** The boundary between market evaluation and
positioning is thin, and the base model already leans toward interrogating
position on a copy request. A market-selection skill that triggers on anything
business-adjacent will amplify this into a full criteria walkthrough. The
`description` must be scoped to evaluating or generating *market directions*, with
an explicit "not for" covering copy, positioning and messaging, which belong to
`landing-copy`.

---

## Baseline output, verbatim

Before I write this, one honest flag: "API monitoring for backend engineers" describes a category, not a position. Datadog, Checkly, Better Stack, Sentry and Grafana all fit that sentence. Any hero I write from it alone is copy a competitor could paste onto their own site, which is the main way this fails.

Five things decide the copy. The first one decides most of it.

1. **What breaks that you catch and the incumbent misses?** Uptime pings, p99 latency per route, schema and contract drift, error budgets, or the third-party APIs you depend on? Pick one.
2. **Who feels the pain first?** The on-call engineer at 2am, or the lead who reads the angry customer email at 9am? They want different things.
3. **The top objection.** My guess is "we already pay for Datadog" or "nobody looks at the dashboard we have." Ask three churned trials what almost stopped them.
4. **The name.**
5. **Any real numbers.** Setup time, median time to detect, customer count, one testimonial.

Here are two heroes built on two different guesses at #1, so you can see how much the answer swings the copy. Both are placeholders until you replace my guess with yours.

**A. Wedge: your customers find the outage before you do**

> **Find the broken endpoint before the support ticket does.**
>
> [Name] watches every route you ship and pages you with the failing endpoint, the payload, and the deploy that caused it. One line in your gateway, no agent to install.
>
> [ Monitor my first endpoint ]

**B. Wedge: the failure is in someone else's API, not yours**

> **Half your outages start in an API you don't own.**
>
> [Name] tracks Stripe, Twilio, and every other service your app calls, then tells you which one broke. Stop debugging code that works.
>
> [ Check my dependencies ]

Two notes on the surrounding screen. Put proof directly under the hero, a logo row or one named testimonial from an engineer with a title, since "trust my alerts" is a high-trust purchase and an unproven page won't get it. And answer the "we already have Datadog" objection out loud in the first feature block, not on a comparison page nobody reaches.

One assumption I did not apply: the pricing defaults I'd normally reach for (premium tier, hard paywall, no free plan) are wrong for most self-serve dev tools, which grow product-led through a free tier. Tell me if you're selling top-down instead and I'll revisit.

Answer question 1 and I'll write five headlines against a real position rather than two against a guess.
