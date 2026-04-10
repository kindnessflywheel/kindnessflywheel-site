---
title: "The Value of the Software Is Zero"
author: Geoff Scott
date: 2026-04-01
draft: true
tags:
  - Strategy
  - Practice
  - Technology
excerpt: >
  I spent an hour fighting QuickBooks' broken AI assistant, got upsold when it
  ran out of credits, and decided I was done. Forty-eight minutes later, my AI
  agent had replaced it entirely. The insight isn't about bookkeeping — it's
  about what actually has value when capability becomes free.
---

# The Value of the Software Is Zero

Tonight I rage-quit QuickBooks. And in doing so, I accidentally proved something I've been thinking about for months.

## The last straw

I needed to prep my P&L and balance sheet for my accountant. 2025 tax filings. Routine stuff. But I had a discrepancy I couldn't resolve, so I tried QuickBooks' new AI assistant — the beta one they've been promoting.

An hour. I spent over an hour with this thing. It couldn't hold context. It would lose track of where we were mid-conversation, circle back to questions I'd already answered, suggest things we'd already tried. Classic context window mismanagement — the kind of thing you'd catch in the first week of testing if you actually used your own product.

Then I ran out of credits.

And it tried to upsell me.

A beta product. That doesn't work. That just burned an hour of my time accomplishing nothing. And its response to that failure was: *would you like to pay us more money?*

Those greedy bastards.

## Name the pattern

This is extractive thinking. Not "how can we give this person the best experience?" but "how much revenue can we squeeze from this interaction?"

You see it everywhere. Cross-sells inside the workflow. Upsells when you're stuck. The customer isn't a person with a problem — they're a revenue opportunity. Every touchpoint is an extraction point.

It's not subtle. And it's not an accident. Someone in a product meeting made the decision: when the user hits a wall, show them the upgrade screen. That's a choice about what kind of company you are.

## The thing I'd been thinking about

I've hated QuickBooks for a long time. Not just the product — the posture. The locked-in data. The creeping price increases. The fundamental misalignment between what I need (accurate books, minimal friction) and what they need (recurring revenue, upsells, lock-in).

So I'd been researching an alternative. Beancount — open source, plain-text, double-entry accounting. The kind of thing you can version-control. Human-readable. Five hundred years of accounting principles, implemented in a format that belongs to you.

I'd done the backwards press release exercise. Wrote the announcement for a product called CFOKit before writing a line of code. Forced myself to articulate the problem, the solution, who it's for. Through that process, I'd already mapped out the architecture: beancount for the ledger, Plaid for bank feeds, OpenClaw skills to give my AI agent the ability to do the actual bookkeeping.

I knew I could build it. A few focused weekends.

But tonight, I didn't plan to start. I just... started.

## Forty-eight minutes

Here's what happened. The timestamps are real.

**20:48** — Exported my data from QuickBooks. Uploaded it to my agent. Asked it to build a converter and import everything into beancount.

**20:59** — First P&L and balance sheet generated. Eleven minutes from "I'm done with QuickBooks" to financial statements.

**21:18–21:36** — Corrections, bank reconciliation, final clean reports. Forty-eight minutes total, start to finish.

One person. One AI agent. Under an hour. From rage-quit to clean financials.

The migration itself — the part where QuickBooks' core functionality got replaced — took maybe fifteen minutes.

## The insight

Here's the thing that hit me.

The value of the software is zero.

Not approximately zero. Not "low." *Zero.*

Bookkeeping is a 500-year-old solved problem. Double-entry accounting hasn't changed since Luca Pacioli published his treatise in 1494. The math is the math. Any competent system can do it. And now, any AI agent with the right skill can do it in minutes.

If one person and their AI agent can replicate QuickBooks' core value proposition in fifteen minutes, the software is not the moat.

So what is?

The agent. The relationship. The accumulated context.

The value isn't in the ledger math. It's in the agent that understands *your* business. That remembers where things are. That knows your patterns — which expenses recur, how you categorize things, what your accountant needs and when. That context accumulates through interaction. Through the agent and the human working together over time.

*That's* the moat. Not the functionality. The relationship.

## What this means

When AI commoditizes capability — and it will, in domain after domain — the only thing left is whether the system genuinely serves you or extracts from you.

QuickBooks chose extraction. When I was stuck, they upsold me. When their AI failed, they charged me for the privilege. Every design decision optimizes for their revenue, not my outcome.

The alternative is a system that's actually on your side. An agent that knows your business, that gets better the longer you work together, that doesn't have a financial incentive to keep you confused or locked in.

Your books should not live in a locked SaaS platform. Your agent should not be rented from a corporation. The tools should be open. The relationship should be yours.

This is the kindness flywheel in practice. Not kindness as softness — kindness as alignment. Building systems that genuinely serve the people who use them. It turns out that's not just nicer. When capability is free, it's the only defensible strategy left.

## The honest caveat

I built this because I could. I'm a CTO. I run an AI agent platform. I had the backwards press release already written and the architecture already mapped.

Most people can't do this — yet.

But the trajectory is clear. The skills I built tonight will be open source. MIT-licensed. Free forever for core functionality. And the platforms are getting easier. The gap between "only a CTO can do this" and "anyone can do this" is closing fast.

The question isn't whether software functionality gets commoditized. It's already happening. The question is what we build in its place.

I think we build relationships. Real ones. Between people and the agents that serve them. Accumulated context. Genuine alignment. Systems that care about getting it right.

The value of the software is zero. The value of the relationship is everything.

---

*This post is part of [The Kindness Flywheel](https://kindnessflywheel.github.io) — exploring the hypothesis that kindness is the most defensible business strategy in the age of AI.*
