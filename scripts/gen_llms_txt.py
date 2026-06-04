#!/usr/bin/env python3
"""phaedrus llms.txt generator — site-agnostic.

Walks a Jekyll site's _posts/ (and optionally collections declared in _config.yml),
emits a Markdown block listing every published post between the markers:

    <!-- phaedrus:llms-autogen:start -->
    ...generated...
    <!-- phaedrus:llms-autogen:end -->

The rest of llms.txt is hand-edited and preserved. The site must contain the
markers; `install-site-assets` reminds the operator to add them on first install.
"""
from __future__ import annotations

import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Iterable

import yaml

ROOT = Path(__file__).resolve().parents[1]
LLMS_TXT = ROOT / "llms.txt"
CONFIG_YML = ROOT / "_config.yml"

START = "<!-- phaedrus:llms-autogen:start -->"
END = "<!-- phaedrus:llms-autogen:end -->"

FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)", re.DOTALL)


def load_config() -> dict:
    if not CONFIG_YML.exists():
        return {}
    with CONFIG_YML.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def parse_front_matter(text: str) -> tuple[dict, str]:
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}, text
    fm = yaml.safe_load(m.group(1)) or {}
    if not isinstance(fm, dict):
        fm = {}
    return fm, m.group(2)


def permalink_for(config: dict, fm: dict, default_date: date, slug: str) -> str:
    """Apply Jekyll's permalink template using a minimal substitution set."""
    pattern: str = fm.get("permalink") or config.get("permalink") or "/:categories/:year/:month/:day/:title:output_ext"
    d = fm.get("date")
    if isinstance(d, str):
        try:
            d = datetime.fromisoformat(d.replace("Z", "+00:00"))
        except ValueError:
            d = default_date
    if isinstance(d, datetime):
        d = d.date()
    if not isinstance(d, date):
        d = default_date
    categories = fm.get("categories") or []
    if isinstance(categories, str):
        categories = [categories]
    subs = {
        ":year": f"{d.year:04d}",
        ":month": f"{d.month:02d}",
        ":day": f"{d.day:02d}",
        ":i_month": str(d.month),
        ":i_day": str(d.day),
        ":title": slug,
        ":slug": slug,
        ":categories": "/".join(categories),
        ":output_ext": ".html",
    }
    out = pattern
    for k, v in subs.items():
        out = out.replace(k, v)
    out = re.sub(r"/+", "/", out)
    if not out.startswith("/"):
        out = "/" + out
    return out


def slug_from_filename(name: str) -> tuple[date, str]:
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.(md|markdown|html)$", name)
    if not m:
        return date.today(), name.rsplit(".", 1)[0]
    return date(int(m.group(1)), int(m.group(2)), int(m.group(3))), m.group(4)


def iter_post_dirs(config: dict) -> Iterable[Path]:
    yield ROOT / "_posts"
    collections = config.get("collections") or {}
    if isinstance(collections, dict):
        for name, meta in collections.items():
            if not isinstance(meta, dict):
                continue
            if meta.get("output") is False:
                continue
            yield ROOT / f"_{name}"


def collect_posts(config: dict) -> list[dict]:
    site_url = (config.get("url") or "").rstrip("/")
    baseurl = (config.get("baseurl") or "").rstrip("/")
    posts: list[dict] = []
    for d in iter_post_dirs(config):
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")) + sorted(d.glob("*.markdown")):
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                continue
            fm, _body = parse_front_matter(text)
            if fm.get("published") is False:
                continue
            file_date, slug = slug_from_filename(path.name)
            title = fm.get("title") or slug.replace("-", " ").title()
            # Mirror jekyll-seo-tag: prefer an explicit SEO `description` override,
            # otherwise fall back to the post's `excerpt` (the canonical hook).
            description = fm.get("description") or fm.get("excerpt") or ""
            link = permalink_for(config, fm, file_date, slug)
            posts.append({
                "title": str(title),
                "description": str(description),
                "url": f"{site_url}{baseurl}{link}",
                "date": fm.get("date") or file_date.isoformat(),
            })
    posts.sort(key=lambda p: str(p["date"]), reverse=True)
    return posts


def render_block(posts: list[dict]) -> str:
    lines = [START, "", "## Posts", ""]
    for p in posts:
        bullet = f"- [{p['title']}]({p['url']})"
        if p["description"]:
            bullet += f": {p['description']}"
        lines.append(bullet)
    lines.extend(["", END])
    return "\n".join(lines)


def splice(existing: str, block: str) -> str:
    if START in existing and END in existing:
        return re.sub(
            re.escape(START) + r".*?" + re.escape(END),
            block,
            existing,
            count=1,
            flags=re.DOTALL,
        )
    return (existing.rstrip() + "\n\n" + block + "\n") if existing.strip() else block + "\n"


def main() -> int:
    config = load_config()
    posts = collect_posts(config)
    block = render_block(posts)
    if not LLMS_TXT.exists():
        print(f"warning: {LLMS_TXT} does not exist — creating with autogen block only.", file=sys.stderr)
        existing = ""
    else:
        existing = LLMS_TXT.read_text(encoding="utf-8")
    updated = splice(existing, block)
    if updated != existing:
        LLMS_TXT.write_text(updated, encoding="utf-8")
        print(f"wrote {LLMS_TXT} ({len(posts)} posts)")
    else:
        print(f"{LLMS_TXT} unchanged ({len(posts)} posts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
