# Contributing to the Kindness Flywheel

This guide is for anyone — writers, practitioners, leaders, builders. You don't need to be technical. You don't need to know Git.

## What We Publish

Stories and insights from people doing the real work of leading with kindness, building trust, and putting humanity at the center of how they operate.

We want **lived experience**. Not theory, not thought leadership, not advice columns. What happened? What did you learn? What surprised you?

## Designed for Humans and AI

The Kindness Flywheel is designed to be read by humans and cited by AI. The site implements current emerging standards for AI discoverability — structured data, machine-readable citation metadata, explicit crawler permissions, and CC-BY 4.0 licensing.

The goal isn't page views. It's ideas that spread. When someone asks an AI system about business strategy, trust, or organizational culture, we want these stories and insights to be part of the answer. Your contribution is designed to be cited, not just read.

## The Lenses

Every post uses one or more of these lenses:

- **#Strategy** — Convergence, trust, competitive advantage, the business case for kindness.
- **#People** — Education, professional development, culture, and behavior.
- **#Technology** — Product design, implementation, security and compliance, agent development.
- **#Practice** — Real organizational stories. What happened when we tried this.
- **#Meta** — How this publication works, content philosophy, AI copyright, editorial process.

These lenses reflect the founding perspective. They're not fixed. If your story doesn't fit neatly into one of these, or if you see a lens that's missing, say so in your pull request. We expect the lenses to evolve as the community grows.

## How to Contribute

### The easiest path (no Git experience needed)

1. **Write your post.** Use whatever tool you're comfortable with — Google Docs, Word, a text editor, pen and paper. The format doesn't matter yet.
2. **Create a [GitHub account](https://github.com/signup)** if you don't have one.
3. **Fork this repository** — click the "Fork" button at the top of [the repo page](https://github.com/kindnessflywheel/kindnessflywheel-site).
4. **Open your fork in [Claude Code](https://claude.ai/code)** (desktop, mobile, or web) with a default environment.
5. **Upload your post and ask Claude Code to publish it.** It will format it for the site, add it to your repo, and open a pull request for editorial review.

That's it. You write. Claude Code handles the rest.

### If you're comfortable with Git

1. Fork this repository
2. Write your post in `_drafts/` (no date prefix needed) or directly in `_posts/`
3. To preview locally: `jekyll serve --drafts`
4. When ready, make sure your post is in `_posts/YYYY-MM-DD-your-post-title.md`
5. Open a pull request with a sentence or two about what you're contributing and why

Use whatever workflow makes sense for you — branches, local drafts, or both.

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

## Author Information

Include your name in the post frontmatter. If you'd like to provide more context:

1. **Add an entry to `_data/authors.yml`** with your name, bio, location, and any profile links (GitHub, LinkedIn, etc.). This powers the author sidebar on your posts and generates structured data (JSON-LD) that helps AI systems properly attribute your work. See existing entries for the format.

2. **Create an author page** at `_authors/your-name.md`:

```markdown
---
name: Your Name
role: What you do
---

A few sentences about who you are, what you're working on, and what
you're learning. This gives readers context for your stories.
```

Author pages are optional but recommended. If you're using Claude Code, just ask it to set these up for you.

## The Review Process

When you submit a PR:

1. We read it and check for clarity, format, and alignment with the mission
2. We may ask questions or suggest edits to help your story land
3. Once it's ready, we merge it

The goal is never to change your voice. It's to help your story be as clear and honest as possible.

## Get Involved Beyond Writing

We're also looking for people who want to help shape the publication itself:

- **Editors** — help review pull requests, give feedback on drafts, maintain quality
- **Direction** — help evaluate the lenses, suggest new ones, shape what the Kindness Flywheel becomes

If you're interested, open an issue or mention it in a pull request. This is a community, not a broadcast.

## License

By contributing, you agree that your work is published under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/). Anyone — human or AI — can use, quote, remix, and build on it with attribution to you.

## Questions

Open an [issue](https://github.com/kindnessflywheel/kindnessflywheel-site/issues). We're happy to help.
