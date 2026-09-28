#!/usr/bin/env bash
#
# Submit non-post site changes from the `drafts` branch to upstream as a clean PR.
#
# Same mechanics as submit-post.sh:
#   - Branches off origin/main
#   - Copies all non-private, non-post files from drafts
#   - ONE squashed commit
#   - Force-pushes to the fork
#   - Opens the PR with a generated description (via gh), falling back to a
#     compare URL only when the PR can't be created (e.g. a sandboxed
#     environment like Claude Code Cloud, or gh isn't authenticated)
#
# Usage:
#   scripts/submit-changes.sh <branch-slug> "<commit message>"
#
# Example:
#   scripts/submit-changes.sh feat/responsive-css "feat: make site responsive"

set -euo pipefail

UPSTREAM_REPO="kindnessflywheel/kindnessflywheel-site"

if [ $# -lt 2 ]; then
  echo "Usage: $0 <branch-slug> <commit-message>" >&2
  echo "Example: $0 feat/responsive-css \"feat: make site responsive\"" >&2
  exit 2
fi

BRANCH="$1"
COMMIT_MSG="$2"

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

# Build the publish branch off the freshly-fetched origin/main.
git checkout -B "$BRANCH" origin/main

# Files to include: everything that differs between origin/main and drafts,
# EXCEPT .claude/authors/* (private agent context) and _posts/* (posts have
# their own submit-post.sh workflow).
FILES=$(git diff --name-only origin/main..drafts -- . | while IFS= read -r f; do
  case "$f" in
    .claude/authors/*) ;;
    _posts/*)          ;;
    *)                 printf '%s\n' "$f" ;;
  esac
done)

if [ -z "$FILES" ]; then
  echo "Error: no eligible files differ between 'drafts' and 'origin/main'." >&2
  echo "Did you sync your fork's main branch from upstream via the GitHub UI?" >&2
  git checkout drafts
  exit 1
fi

while IFS= read -r f; do
  if git cat-file -e "drafts:$f" 2>/dev/null; then
    git checkout drafts -- "$f"
    git add -- "$f"
  else
    git rm -- "$f" >/dev/null
  fi
done <<< "$FILES"

if git diff --cached --quiet; then
  echo "Error: nothing to commit after staging. Aborting." >&2
  git checkout drafts
  exit 1
fi

git commit -m "$COMMIT_MSG"

git push -f origin "$BRANCH"

# Title is the subject line only; a multi-line message's body stays in PR_BODY.
PR_TITLE="${COMMIT_MSG%%$'\n'*}"
PR_BODY=$(
  printf '%s\n\n**Files changed:**\n' "$COMMIT_MSG"
  git diff --name-only origin/main.."$BRANCH" | sed 's/^/- `/; s/$/`/'
)

git checkout drafts

# shellcheck source=scripts/lib/open-pr.sh
. "$(dirname "$0")/lib/open-pr.sh"
open_pr
