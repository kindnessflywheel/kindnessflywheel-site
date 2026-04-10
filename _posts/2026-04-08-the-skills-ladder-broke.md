---
title: "The Skills Ladder Broke"
author: Geoff Scott
date: 2026-04-08
draft: true
tags:
  - Strategy
  - Education
excerpt: >
  The traditional software engineering career ladder — intern to distinguished
  engineer — was built for a world where technical depth was the differentiator.
  AI just collapsed the bottom half. What does the ladder look like now?
---

The software engineering skills ladder has looked roughly the same for thirty years. Intern, junior, mid, senior, staff, principal, distinguished. Each rung defined by increasing technical depth, broader system understanding, and the ability to solve harder problems with less guidance.

AI just collapsed the bottom half of that ladder.

## The Traditional Ladder

Here's the simplified version most companies run:

| Level | Core Expectation |
|-------|-----------------|
| **Intern** | Learn the codebase. Ship small tasks with heavy mentorship. |
| **Junior** | Deliver features with guidance. Write tests. Follow patterns. |
| **Mid** | Own components. Make design decisions within constraints. Debug complex issues. |
| **Senior** | Own systems. Set technical direction for a team. Mentor others. Make tradeoffs. |
| **Staff** | Own architecture across teams. Influence org-wide technical strategy. |
| **Principal** | Shape the company's technical trajectory. Solve the hardest cross-cutting problems. |
| **Distinguished** | Industry-level impact. Define practices that extend beyond the organization. |

At each rung, the differentiator was technical depth. Could you write better algorithms? Debug harder problems? Design more elegant systems? Understand more of the stack?

That was the game. And it made sense — because technical execution was hard, slow, and scarce.

## What AI Normalizes

Here's what's already converging:

**Code generation.** A junior engineer with Cursor or Claude Code ships features at the speed a mid-level engineer did two years ago. The gap between "can write code" and "can write good code" is compressing fast. Not gone — but the floor has risen dramatically.

**Pattern application.** Knowing which design pattern to apply, how to structure a service, how to write idiomatic code in a given language — AI handles this well. The encyclopedic knowledge that separated a 2-year developer from a 10-year developer is increasingly available on demand.

**Debugging and troubleshooting.** AI is already good at reading stack traces, identifying common failure patterns, and suggesting fixes. The "I've seen this before" intuition that took years to develop is being compressed into seconds.

**Documentation and communication artifacts.** Technical writing, API docs, architecture decision records, PR descriptions — AI produces competent versions of all of these. The person who was valued because they could write clearly about technical topics finds that skill less scarce.

**Testing.** Writing unit tests, integration tests, identifying edge cases — AI does this well. Test coverage as a differentiator is fading.

These are the skills that defined the bottom half of the ladder. Intern through mid-level was largely about acquiring them. Senior was about having mastered them.

If AI normalizes these skills, what's left?

## What Still Differentiates

Some things don't compress:

**Judgment under ambiguity.** Knowing what to build, not just how to build it. Understanding which tradeoffs matter for this business, this team, this moment. AI can generate options; it can't tell you which one is right for your specific context with incomplete information.

**Organizational influence.** Getting alignment across teams. Navigating politics without creating enemies. Convincing a skeptical VP that a technical investment is worth the cost. This is human work — and it gets more important as AI handles more of the execution.

**System thinking at scale.** Not "how does this service work" but "how do these 40 services interact under load when the third-party payment provider is degraded and we're mid-migration." AI can model parts of this. The holistic judgment is still human.

**Taste.** What should the developer experience feel like? What's the right level of abstraction? When is a system too clever? Taste is pattern recognition plus values, and it's hard to automate because it's hard to articulate.

**Mentorship and team development.** Growing other engineers. Knowing when someone needs a stretch assignment versus support. Reading the room in a code review. This is fundamentally relational.

## What Emerges as New

Here's where it gets interesting. The AI-native ladder needs skills that didn't exist on the old one:

**Agent orchestration.** Understanding how to decompose work across AI agents, when to trust agent output, how to design effective agent workflows. This is a new engineering discipline — not prompt engineering (that's already commoditizing), but system design where some of your components are non-deterministic.

**Verification and judgment at speed.** The bottleneck shifts from "can you produce this?" to "can you evaluate whether this is correct, safe, and appropriate — fast?" An engineer who can review AI-generated code, catch subtle bugs, and make quality judgments at the speed of generation is enormously valuable.

**Context curation.** AI is only as good as the context it operates in. Engineers who can maintain clean, well-structured project context — architecture docs, decision records, constraints files — so that AI agents produce better output are creating leverage for the whole team.

**Human-AI collaboration design.** Where should a human be in the loop? Where is full automation safe? Where does AI augmentation help versus create false confidence? Designing these workflows is a new skill.

**Cross-domain fluency.** When AI handles the execution layer, the person who understands the business domain deeply AND can guide technical implementation becomes the most valuable person in the room. The "full-stack" concept expands from "frontend and backend" to "business context and technical implementation."

## The New Ladder

What might this look like?

| Level | Traditional Core | AI-Native Core |
|-------|-----------------|----------------|
| **Junior** | Write code with guidance | Orchestrate AI output with guidance. Verify, test, and evaluate generated work. |
| **Mid** | Own components, make design decisions | Own agent workflows. Curate context. Make judgment calls on AI output quality. |
| **Senior** | Own systems, mentor, make tradeoffs | Design human-AI collaboration patterns. Develop team capability with AI tools. Set quality standards for AI-augmented work. |
| **Staff** | Cross-team architecture | Cross-team AI strategy. Define where automation is safe and where humans must remain in the loop. |
| **Principal** | Company-wide technical trajectory | Company-wide AI integration philosophy. Define how the organization learns and adapts with AI. |

Notice what happened to the bottom rungs. Intern and junior used to be about acquiring technical skills through repetition. Now they're about developing judgment — learning to evaluate, not just produce. That's a fundamentally different onboarding challenge.

And notice what happened at the top. Distinguished engineers used to be defined by deep technical expertise. In an AI-native world, they're defined by wisdom — judgment, influence, taste, and the ability to see around corners that AI can't.

## The Uncomfortable Part

This raises hard questions:

**How do juniors develop judgment without the reps?** If AI handles the code, how does a new engineer build the intuition that comes from writing bad code, debugging it, and learning? We might be optimizing away the training ground.

**What happens to the mid-level majority?** Most engineers live in the mid-to-senior range. If AI normalizes those skills, that's a lot of people whose differentiator just evaporated. The answer isn't "learn to prompt" — it's develop the human skills that are now the differentiator.

**Who gets left behind?** The engineer who defined themselves by technical depth — by knowing the language spec, by writing the fastest algorithm, by having memorized the framework internals — finds that knowledge commoditized. The transition isn't easy.

## The Kindness Flywheel Connection

Here's what I keep coming back to: the skills that survive and emerge on the AI-native ladder are all human skills. Judgment. Influence. Mentorship. Taste. Collaboration. Cross-domain empathy.

The organizations that invest in developing these skills — that treat people as whole humans capable of growth, not as "resources" to be utilized — will have the engineers who thrive in this transition. The ones that double down on extraction — stack ranking, utilization metrics, "do more with less" — will optimize away the very capabilities they need most.

The skills ladder didn't just change shape. It changed substance. And the substance it changed to is human.

---

*This is a working draft. The traditional ladder varies by company, and the AI-native version is evolving in real time. If your organization is rethinking its engineering ladder, I'd love to hear what you're seeing.*
