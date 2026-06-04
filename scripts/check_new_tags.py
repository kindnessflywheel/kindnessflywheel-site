#!/usr/bin/env python3
"""phaedrus — detect newly-introduced tags in a PR.

Compares the set of tags in `_posts/` on the PR head against the set on the
base branch (BASE_REF). Writes a Markdown report to REPORT_FILE if any tags
are net-new; emits an empty file otherwise.

Always exits 0 — the workflow uses report-emptiness to decide whether to
comment. This is informational, not gating.

Env:
  BASE_REF       (default: origin/main) — git ref for the base branch.
  POSTS_DIR      (default: _posts)
  REPORT_FILE    (default: .phaedrus-new-tags.md)
"""
from __future__ import annotations

import os
import re
import subprocess
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


def base_tags(base_ref: str, posts_dir: str) -> set[str]:
    out: set[str] = set()
    try:
        listing = subprocess.check_output(
            ["git", "ls-tree", "-r", "--name-only", base_ref, "--", f"{posts_dir}/"],
            text=True,
            stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return out
    for path in listing.splitlines():
        if not (path.endswith(".md") or path.endswith(".markdown")):
            continue
        try:
            content = subprocess.check_output(
                ["git", "show", f"{base_ref}:{path}"],
                text=True,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError:
            continue
        for t in parse_tags(content):
            out.add(t)
    return out


def render(new: dict[str, list[str]]) -> str:
    if not new:
        return ""
    lines = [
        "### 🏷️ New tags in this PR",
        "",
        "These tags don't appear on any post on the base branch — they expand the site's taxonomy. Worth a closer look:",
        "",
    ]
    for tag in sorted(new):
        posts = sorted(set(new[tag]))
        joined = ", ".join(f"`{p}`" for p in posts)
        lines.append(f"- **`{tag}`** — introduced by {joined}")
    lines += [
        "",
        "If a new tag is a typo or synonym of an existing one, consider editing the post to use the existing tag instead. If it's intentional, merge with care.",
        "",
        "<sub>posted by [phaedrus](https://github.com/geoffscott/phaedrus) check-new-tags</sub>",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    base = os.environ.get("BASE_REF") or "origin/main"
    posts_dir_str = os.environ.get("POSTS_DIR", "_posts")
    posts_dir = Path(posts_dir_str)
    report_path = Path(os.environ.get("REPORT_FILE", ".phaedrus-new-tags.md"))

    head = head_tags(posts_dir)
    base_set = base_tags(base, posts_dir_str)
    new = {t: ps for t, ps in head.items() if t not in base_set}

    body = render(new)
    report_path.write_text(body, encoding="utf-8")
    print(f"::notice::phaedrus check-new-tags: {len(new)} net-new tag(s)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
