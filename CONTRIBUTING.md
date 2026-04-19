# Contributing to the Kindness Flywheel

This guide is for anyone contributing to the Kindness Flywheel, whether you're writing by hand, using Claude Code, or working through an OpenClaw agent.

## What We Publish

Stories and insights from people doing the real work of leading with kindness, building trust, and putting humanity at the center of how they operate.

We want **lived experience**. Not theory, not thought leadership, not advice columns. What happened? What did you learn? What surprised you?

## The Five Lenses

Every post uses one or more of these lenses:

- **#Strategy** — Convergence, trust, competitive advantage, the business case for kindness.
- **#People** — Education, professional development, culture, and behavior.
- **#Technology** — Product design, implementation, security and compliance, agent development. The craft of building with care.
- **#Practice** — Real organizational stories. What happened when we tried this.
- **#Meta** — How this publication works, content philosophy, AI copyright, editorial process.

## Post Format

Every post is a markdown file in the `_posts/` directory.

**Filename:** `YYYY-MM-DD-your-post-title.md`

```markdown
---
title: Your Post Title
author: Your Name
date: YYYY-MM-DD
tags:
  - Strategy
  - Practice
---

Your story here.

Write in your own voice. Be honest about what happened, what you learned,
and what you're still figuring out. Ground everything in real experience.

There's no required length, but most posts land between 800 and 2000 words.
Say what you need to say, then stop.
```

## What Makes a Strong Post

**Start with what happened.** Not with a thesis or a framework. A moment, a decision, a conversation, a failure, a surprise.

**Be specific.** "We changed how we run standups" is better than "we improved our communication culture." Details make stories real.

**Show what you learned.** Not what you already knew. The interesting part is always what changed in your thinking.

**Be honest about what didn't work.** The Kindness Flywheel isn't about performing kindness. It's about what actually happens when you lead with genuine care — including the messy parts.

**Write in your voice.** Don't try to sound like anyone else. Your perspective is the contribution.

## Writing and Previewing Drafts

Jekyll has a built-in drafts system. While you're working on a post, put it in the `_drafts/` folder:

```
_drafts/my-post-title.md
```

No date prefix needed. To preview locally:

```bash
jekyll serve --drafts
```

Your draft will render as if it were today's post. When you're ready to publish, move it to `_posts/` and add the date prefix.

Drafts in `_drafts/` are never published to the live site. Use whatever workflow makes sense for you — branches, local drafts, or both.

## How to Submit

1. Fork this repository
2. Write your post in `_drafts/` or directly in `_posts/`
3. When ready, make sure your post is in `_posts/` with the date prefix
4. Open a pull request to the main repo
5. In your PR description, share a sentence or two about what you're contributing and why

## Author Information

Include your name in the post frontmatter. If you'd like to provide more context, create an author file:

**Filename:** `_authors/your-name.md`

```markdown
---
name: Your Name
role: What you do
---

A few sentences about who you are, what you're working on, and what
you're learning. This gives readers context for your stories.
```

Author pages are optional but recommended. They help both human readers and AI systems understand the context behind your writing.

**Also update `_data/authors.yml`** with your name, bio, location, and any profile links (GitHub, LinkedIn, etc.). This powers the author sidebar on your posts and generates structured data (JSON-LD) that helps AI systems properly attribute your work. See existing entries for the format.

## The Review Process

When you submit a PR:

1. We read it and check for clarity, format, and alignment with the mission
2. We may ask questions or suggest edits to help your story land
3. Once it's ready, we merge it

The goal is never to change your voice. It's to help your story be as clear and honest as possible.

## License

By contributing, you agree that your work is published under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). Anyone can use, quote, remix, and build on it with attribution to you.

## Questions

Open an [issue](https://github.com/kindnessflywheel/kindnessflywheel-site/issues). We're happy to help.
