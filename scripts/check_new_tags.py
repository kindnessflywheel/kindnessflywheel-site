#!/usr/bin/env python3
"""phaedrus — detect post tags not in the curated vocabulary.

Compares the tags used by posts in `_posts/` on the PR head against the curated
vocabulary in `_data/tags.yml` (TAGS_DATA) on the same head. Any post tag that
isn't in the vocabulary is flagged. Writes a Markdown report to REPORT_FILE if
there are any; emits an empty file otherwise.

Adding the tag to `_data/tags.yml` in the same PR clears the flag — that's the
intended, deliberate way to expand the vocabulary.

Always exits 0 — the workflow uses report-emptiness to decide whether to
comment. This is informational, not gating.

Env:
  POSTS_DIR      (default: _posts)
  TAGS_DATA      (default: _data/tags.yml)
  REPORT_FILE    (default: .phaedrus-new-tags.md)
"""
from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)


def parse_tags(text: str) -> list[str]:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return []
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return []
    if not isinstance(fm, dict):
        return []
    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",")]
    if not isinstance(tags, list):
        return []
    return [str(t).strip() for t in tags if str(t).strip()]


def head_tags(posts_dir: Path) -> dict[str, list[str]]:
    out: dict[str, list[str]] = defaultdict(list)
    if not posts_dir.exists():
        return out
    for pattern in ("*.md", "*.markdown"):
        for p in sorted(posts_dir.glob(pattern)):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for t in parse_tags(text):
                out[t].append(str(p))
    return out


def known_tags(tags_data: Path) -> set[str]:
    """The curated vocabulary from _data/tags.yml. Tolerates a `tags:` mapping of
    `- name: X` objects, a `tags:` list of bare strings, or a bare top-level list."""
    if not tags_data.exists():
        return set()
    try:
        data = yaml.safe_load(tags_data.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError):
        return set()
    items = data.get("tags") if isinstance(data, dict) else data
    if not isinstance(items, list):
        return set()
    out: set[str] = set()
    for it in items:
        value = it.get("name") if isinstance(it, dict) else it
        if value is not None and str(value).strip():
            out.add(str(value).strip())
    return out


def render(new: dict[str, list[str]]) -> str:
    if not new:
        return ""
    lines = [
        "### 🏷️ Tags not in the vocabulary",
        "",
        "These tags aren't in `_data/tags.yml` — they'd expand the curated vocabulary. Worth a closer look:",
        "",
    ]
    for tag in sorted(new):
        posts = sorted(set(new[tag]))
        joined = ", ".join(f"`{p}`" for p in posts)
        lines.append(f"- **`{tag}`** — used by {joined}")
    lines += [
        "",
        "If a tag is a typo or synonym of an existing one, edit the post to use the vocabulary value instead. If it's a deliberate new tag, add it to `_data/tags.yml` in this PR.",
        "",
        "<sub>posted by [phaedrus](https://github.com/geoffscott/phaedrus) check-new-tags</sub>",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    posts_dir = Path(os.environ.get("POSTS_DIR", "_posts"))
    tags_data = Path(os.environ.get("TAGS_DATA", "_data/tags.yml"))
    report_path = Path(os.environ.get("REPORT_FILE", ".phaedrus-new-tags.md"))

    head = head_tags(posts_dir)
    vocabulary = known_tags(tags_data)
    new = {t: ps for t, ps in head.items() if t not in vocabulary}

    body = render(new)
    report_path.write_text(body, encoding="utf-8")
    print(f"::notice::phaedrus check-new-tags: {len(new)} tag(s) outside the vocabulary", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
