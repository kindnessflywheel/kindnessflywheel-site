#!/usr/bin/env bash
#
# Submit a post from the `drafts` branch to upstream as a clean PR.
#
# Designed to run inside Claude Code Cloud against the contributor's fork.
# CCC's network sandbox only permits operations against the fork (origin), so
# this script:
#   - Branches off origin/main (which the contributor keeps synced with
#     upstream via the GitHub UI "Sync fork" button)
#   - Copies in the post and any other non-private files from drafts
#   - Makes ONE squashed commit so the upstream PR is clean
#   - Force-pushes to the fork
#   - Opens the PR with a generated description (via gh), falling back to a
#     compare URL only when the PR can't be created (sandbox / no gh auth)
#
# Usage:
#   scripts/submit-post.sh _posts/2026-05-14-my-post.md
#   scripts/submit-post.sh 2026-05-14-my-post.md
#   scripts/submit-post.sh 2026-05-14-my-post

set -euo pipefail

UPSTREAM_REPO="kindnessflywheel/kindnessflywheel-site"

if [ $# -lt 1 ]; then
  echo "Usage: $0 <post-file>" >&2
  echo "Example: $0 _posts/2026-05-14-my-post.md" >&2
  exit 2
fi

POST_ARG="$1"
case "$POST_ARG" in
  _posts/*) POST="$POST_ARG" ;;
  *.md)     POST="_posts/$POST_ARG" ;;
  *)        POST="_posts/${POST_ARG}.md" ;;
esac

git rev-parse --git-dir >/dev/null

CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "drafts" ]; then
  echo "Error: run this from the 'drafts' branch (currently on '$CURRENT_BRANCH')." >&2
  exit 1
fi

if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "Error: working tree has uncommitted changes. Commit them on 'drafts' first." >&2
  exit 1
fi

ORIGIN_URL=$(git remote get-url origin)
FORK_OWNER=$(echo "$ORIGIN_URL" | sed -E 's|.*[:/]([^/]+)/[^/]+(\.git)?$|\1|')
if [ -z "$FORK_OWNER" ] || [ "$FORK_OWNER" = "$ORIGIN_URL" ]; then
  echo "Error: could not parse fork owner from origin URL: $ORIGIN_URL" >&2
  exit 1
fi

git fetch origin main

if ! git cat-file -e "drafts:$POST" 2>/dev/null; then
  echo "Error: post file '$POST' does not exist on the 'drafts' branch." >&2
  exit 1
fi

POST_BASENAME=$(basename "$POST" .md)
SLUG=$(echo "$POST_BASENAME" | sed -E 's/^[0-9]{4}-[0-9]{2}-[0-9]{2}-//')
BRANCH="post/$SLUG"

TITLE=$(git show "drafts:$POST" | awk '
  /^---$/ { n++; next }
  n == 1 && /^title:/ {
    sub(/^title:[[:space:]]*/, "")
    gsub(/^"|"$/, "")
    print
    exit
  }
')

if [ -z "$TITLE" ]; then
  echo "Error: could not extract 'title:' from post frontmatter." >&2
  exit 1
fi

# Build the publish branch off the freshly-fetched origin/main.
git checkout -B "$BRANCH" origin/main

# Files to include: everything that differs between origin/main and drafts,
# EXCEPT anything under .claude/authors/*, AND any other _posts/* files
# besides the one being submitted (so multiple in-flight posts don't leak
# into this PR).
FILES=$(git diff --name-only origin/main..drafts -- . | while IFS= read -r f; do
  case "$f" in
    .claude/authors/*) ;;
    _posts/*)
      [ "$f" = "$POST" ] && printf '%s\n' "$f"
      ;;
    *)
      printf '%s\n' "$f"
      ;;
  esac
done)

if [ -z "$FILES" ]; then
  echo "Error: no eligible files differ between 'drafts' and 'origin/main'." >&2
  echo "Did you sync your fork's main branch from upstream via the GitHub UI?" >&2
  git checkout drafts
  exit 1
fi

# Copy file contents from drafts onto this branch, then stage them.
while IFS= read -r f; do
  if git cat-file -e "drafts:$f" 2>/dev/null; then
    git checkout drafts -- "$f"
    git add -- "$f"
  else
    # File was deleted on drafts relative to main; remove it here too.
    git rm -- "$f" >/dev/null
  fi
done <<< "$FILES"

if git diff --cached --quiet; then
  echo "Error: nothing to commit after staging. Aborting." >&2
  git checkout drafts
  exit 1
fi

git commit -m "post: $TITLE"

git push -f origin "$BRANCH"

PR_TITLE="$TITLE"
PR_BODY=$(printf 'New post: **%s**\n' "$TITLE")

git checkout drafts

# shellcheck source=scripts/lib/open-pr.sh
. "$(dirname "$0")/lib/open-pr.sh"
open_pr
