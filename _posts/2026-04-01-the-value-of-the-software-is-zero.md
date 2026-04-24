---
title: "The Value of the Software Is Zero"
author: Geoff Scott
date: 2026-04-01
tags:
  - Strategy
  - Practice
  - Technology
excerpt: >
  When an AI agent can migrate your financial data and generate clean statements
  in 48 minutes, what was QuickBooks actually selling you? The answer reshapes
  how we think about every knowledge-work tool.
---

# The Value of the Software Is Zero

Tonight I rage-quit QuickBooks. And in doing so, I accidentally proved something I've been thinking about for months.

## The last straw

I needed to prep my P&L and balance sheet for my accountant. 2025 tax filings. Routine stuff. But I had a discrepancy I couldn't resolve, so I tried QuickBooks' new AI assistant — the beta one they've been promoting.

An hour. I spent over an hour with this thing. It couldn't hold context. It would lose track of where we were mid-conversation, circle back to questions I'd already answered, suggest things we'd already tried. Classic context window mismanagement — the kind of thing you'd catch in the first week of testing if you actually used your own product.

Then I ran out of credits. And it tried to upsell me.

But the AI assistant was just the last straw. This is a product I pay for that intentionally obstructs my ability to use it for what I'm paying for. Persistent advertisements for services I don't need that I can't dismiss — they just keep coming back. The same repetitive abuse of my attention, session after session. And this isn't the product's fault. Products don't make choices. People do.

Someone designed this. Someone decided that abusing their users' attention and energy to extract more money for things they don't need was a good idea. And that person was driven by leadership that encourages a myopic focus on monetary extraction as opposed to value creation. That's not a product decision. It's a culture.

## The thing I'd been building toward

I've been frustrated with QuickBooks for a long time. Not just the product — the posture. The locked-in data. The creeping price increases. The fundamental misalignment between what I need (accurate books, minimal friction) and what they optimize for (recurring revenue, upsells, lock-in).

So I'd been researching an alternative. Beancount — open source, plain-text, double-entry accounting. The kind of thing you can version-control. Human-readable. Five hundred years of accounting principles, implemented in a format that belongs to you.

I'd written a backwards press release announcing for a product called CFOKit before writing a line of code. Forced myself to articulate the problem, the solution, who it's for. Through that process, I'd already mapped out the architecture: beancount for the ledger, Plaid for bank feeds, skills to give my AI agent the ability to do the actual bookkeeping.

I knew I could build it. I had the whole thing sketched out — data migration, bank integrations, reconciliation workflows, financial reporting.

But tonight, I didn't plan to start. I just... started. With the first piece.

## Forty-eight minutes

Here's what happened. The timestamps are real.

**20:48** — Exported my data from QuickBooks. Uploaded it to my agent. Asked it to build a converter and import everything into beancount.

**20:59** — First P&L and balance sheet generated. Eleven minutes from "I'm done with QuickBooks" to financial statements.

**21:18–21:36** — Corrections, trial balance reconciliation, final clean reports. Forty-eight minutes total, start to finish.

One person. One AI agent. Under an hour. From rage-quit to clean financials.

Let me be precise about what happened: I migrated my data out of QuickBooks, imported it into an open ledger, reconciled the trial balance, and generated clean financial statements. That's one feature — data migration and reporting. It's not a complete replacement. QuickBooks also does bank feeds, recurring invoices, payroll integrations, tax calculations, and a dozen other things I didn't touch tonight.

But that one feature was enough to see something clearly.

## The insight

The value of the software is zero.

Not approximately zero. Not "low." *Zero.*

Bookkeeping is a 500-year-old solved problem. Double-entry accounting hasn't changed since Luca Pacioli published his treatise in 1494. The math is the math. Any competent system can do it. And now, any AI agent with the right instructions can replicate the functionality in minutes.

If one person and their AI agent can migrate a company's financial data and produce clean statements in forty-eight minutes — even if that's just the first step — it tells you something important about where the value lives. It's not in the ledger math. It never was.

There are only a handful of major features between what I built tonight and a full QuickBooks replacement: bank feed integration, recurring transaction handling, multi-entity support, tax-ready exports. Each one is a solved problem. The trajectory is clear, even if the timeline is uncertain.

But the insight isn't about the features remaining. It's about what I noticed when the first one fell so easily. The hard part was never the functionality. The hard part is the accumulated context — the agent that understands *your* business. That remembers where things are. That knows your patterns — which expenses recur, how you categorize things, what your accountant needs and when. That context builds through interaction. Through the agent and the human working together over time.

*That's* where the value lives. Not in the software. In the relationship.

## What I don't know yet

I want to be honest about the limits of what I proved tonight, because I think the honest version makes a stronger argument than the overclaimed one.

**I built this because I could.** I'm a CTO. I run an AI agent platform. I had the architecture already mapped out. Most people can't do this — yet. The gap between "only a technical founder can do this" and "anyone can do this" is closing, but it hasn't closed.

**I migrated one feature, not the whole product.** QuickBooks has network effects that aren't trivial to replace. Accountant integrations. Tax filing workflows. Payroll connections. The bookkeeping math is the easy part; the ecosystem around it is the hard part. I have significant development ahead before I can fully stop paying Intuit.

**I don't know if this is cheaper.** The post might read like I'm saving money. Maybe. But it depends on which LLMs I use and how much they cost per interaction. An agent that reconciles your books daily might cost more in API calls than a QuickBooks subscription. I genuinely don't know yet. I'll find out and report back.

**The skills I built tonight aren't ready for anyone else.** They handle my edge cases, my chart of accounts, my specific QuickBooks export format. I plan to open source them — MIT-licensed, free forever for core functionality. But "planning to open source" and "production-ready for other people" are very different things. Significant development separates the two.

**The trajectory is clear but the timeline is uncertain.** I can see the path to a full replacement. I can't tell you when I'll finish walking it.

## Why the honest version is the stronger one

Here's what I keep coming back to.

If even an incomplete migration of one feature — data export, import, and reporting — proves that the functionality isn't the hard part... what happens when the rest gets built? What happens when bank feeds work, when reconciliation is automated, when tax-ready exports are a single command?

The functionality was never the moat. QuickBooks has been selling a 500-year-old solved problem wrapped in lock-in. And the lock-in is dissolving.

This is the same pattern we're seeing across every knowledge-work tool. In [the inaugural post on this site](/2026/03/28/the-race-to-the-mean), I wrote about convergence — how AI is compressing the execution layer of every knowledge profession. The gap between the best AI models and the rest shrank from 17.5 percentage points to 0.3 in a single year. Feature-level replication now takes hours to days. This isn't just happening to accounting software. It's happening everywhere.

When capability converges to zero cost, what's left?

## What it means

QuickBooks had a choice tonight. When their AI assistant failed me — when their beta product burned an hour of my time accomplishing nothing — they could have said: *We're sorry. Here's a credit. Let us make this right.* That would have cost them almost nothing and might have kept me for another year.

Instead, they upsold me. Because someone in a product meeting decided that when a customer hits a wall, the right response is an upgrade screen. That's not a bug. That's a philosophy. It's extraction — optimizing every touchpoint for revenue, not for the person on the other end.

The alternative is a system that's actually on your side. An agent that knows your business, that gets better the longer you work together, that doesn't have a financial incentive to keep you confused or locked in. Your books in plain text. Your data in a format you own. Your agent running on infrastructure you control.

This is the kindness flywheel in practice. Not kindness as softness — kindness as alignment. Building systems that genuinely serve the people who use them.

In a world where functionality is free, alignment is the only moat left. The question isn't whether software capability gets commoditized — that's already happening. The question is what we build in its place.

I think we build relationships. Real ones. Between people and the systems that serve them. Accumulated context. Genuine alignment. Tools that care about getting it right.

The value of the software is zero. The value of the relationship is everything.

---

*This post is part of [The Kindness Flywheel](https://kindnessflywheel.github.io) — exploring the hypothesis that kindness is the most defensible business strategy in the age of AI.*
