---
title: "Contribute to the Kindness Flywheel"
permalink: /contribute/
---

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

Three ways in. Pick whichever fits how you like to work — they all end up in the same place: a pull request we read, maybe ask a question or two about, and publish. You don't need to know Git, and for one of them you don't even need a GitHub account.

### Write it in your browser

This is the simplest way, and there's nothing to install and no code to touch.

Go to [kindnessflywheel.org/admin](https://kindnessflywheel.org/admin/) and sign in with GitHub. (No account? [Making one](https://github.com/signup) takes a minute and costs nothing.) You'll land in a clean editor with a box for your title, a date, your name, a one-line summary, a few tags to choose from, and a wide-open space to write. No files to wrangle, no Markdown to learn, no formatting to get right. Got a photo or two? Drag them in.

When you're done, save. That doesn't put it live — it sends it to us as a draft. We read it, and once it's ready, it's published.

### Talk it through with an AI assistant

If you'd rather think out loud than fill in a form, write your post in a conversation. This works with any AI assistant that speaks MCP; we'll use Claude as the example.

Connect it once:

1. In [claude.ai](https://claude.ai), open **Settings → Connectors**.
2. Click **Add custom connector**.
3. Paste this address: `https://mcp.kindnessflywheel.org/mcp`

That's the whole setup — no password, no key. Now just talk. Tell it what happened, what you learned, what you're still working out. Draft together, shape it, and when you're happy with it, ask it to submit. It knows the format and the tags, and it opens the pull request for you. We take it from there.

### Fork it and open a pull request

If you're comfortable with Git, the usual flow works:

1. Fork this repository.
2. Add your post under `_posts/` — see [Post Format](#post-format) below for the shape.
3. Open a pull request with a sentence or two about what you're sharing and why.

#### Drafting with an AI agent over several sessions

If you're using an AI agent — Claude Code, Claude Code Cloud, OpenClaw, or anything else — to help draft over multiple sessions, we recommend a convention that keeps your private context (voice profile, research, in-progress drafts) in your fork without leaking it into PRs to upstream.

**One-time setup.** From a clone of your fork:

    ./scripts/setup-author.sh

The script will:

- Add `upstream` remote pointing at this repo
- Create a `drafts` branch in your fork off the latest `main`
- Scaffold `_authors/<your-slug>.md` (your public author bio)
- Scaffold `.claude/authors/<your-slug>/voice.md` (your private voice profile)
- Set `drafts` as your fork's default branch (via `gh repo edit`)
- Push everything to your fork

After it runs, edit `voice.md` with your voice rules and reference posts. Drop additional reference documents (rhetorical forms, source materials, structural frameworks) into `.claude/authors/<your-slug>/` as you accumulate them — the CLAUDE.md hook reads every file in that directory automatically.

**Day-to-day authoring.** Stay on `drafts`. Your agent reads your voice profile and references on every session. Iterate freely; commits stay on `drafts` and only ever live in your fork.

**Submitting a post.** Tell Claude Code to publish. It runs `scripts/submit-post.sh _posts/<your-post>.md`, which:

- Branches `post/<slug>` off your fork's `main` (so make sure you've clicked "Sync fork" on `main` in the GitHub UI first, so it mirrors upstream)
- Copies everything that differs between `drafts` and `main`, **except** anything under `.claude/authors/*/` — so your post, any author bio updates, image assets, and incidental tweaks all come along, but your private voice profile and research do not
- Makes one squashed commit (`post: <title>`) so the upstream PR is a single clean diff
- Force-pushes to your fork
- Prints a compare URL

Click the URL. GitHub shows you the one-commit diff. Add a sentence or two of description and click "Create pull request". That's the whole submission.

**Handling editor feedback.** Edit the post on `drafts` as usual, then tell Claude Code to publish again. The script force-pushes the same `post/<slug>` branch and the existing PR updates automatically — no second PR needed.

**Staying current with upstream.** Click "Sync fork" in the GitHub UI on:

- Your `drafts` branch — pulls upstream improvements into your working branch so your new posts start from current state
- Your `main` branch — required before publishing, so `scripts/submit-post.sh` branches off current upstream

Both are one-click operations in the browser. No commands needed.

**Why this works.** `.claude/authors/*/` is gitignored upstream, so per-contributor content is private by default. Files only become tracked on your fork's `drafts` branch (force-added by the setup script). `scripts/submit-post.sh` mechanically excludes that path from the PR branch, so private context cannot leak — even if you forget.


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

**Keep it mostly text.** Posts are built to read cleanly on any screen, so headings, paragraphs, lists, and the occasional block quote are the whole toolkit — complex page layouts aren't supported. Images are welcome, but go light: one or two per post is plenty. Drop them in `assets/images/posts/`, give each one descriptive alt text, and keep the files a reasonable size so pages stay fast for everyone.

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
