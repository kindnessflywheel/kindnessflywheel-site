#!/usr/bin/env bash
#
# Shared helper for submit-post.sh and submit-changes.sh.
#
# Opens (or reuses) the pull request for $BRANCH with a generated, editable
# description. Falls back to printing a compare URL only when the PR can't be
# created — e.g. a sandboxed environment (Claude Code Cloud can't reach the
# upstream API) or `gh` isn't installed/authenticated.
#
# The caller must set these variables before calling open_pr:
#   UPSTREAM_REPO  e.g. "kindnessflywheel/kindnessflywheel-site"
#   FORK_OWNER     owner of the repo the branch was pushed to (origin)
#   BRANCH         the pushed branch name
#   PR_TITLE       PR title
#   PR_BODY        PR description body

open_pr() {
  local compare_url pr_url=""
  compare_url="https://github.com/${UPSTREAM_REPO}/compare/main...${FORK_OWNER}:${BRANCH}?expand=1"

  if command -v gh >/dev/null 2>&1; then
    # Reuse an existing open PR for this branch if there is one — the
    # force-push already refreshed its diff.
    pr_url=$(gh pr list --repo "$UPSTREAM_REPO" --head "$BRANCH" --state open \
               --json url --jq '.[0].url' 2>/dev/null) || pr_url=""
    if [ -z "$pr_url" ] || [ "$pr_url" = "null" ]; then
      pr_url=$(gh pr create --repo "$UPSTREAM_REPO" --base main \
                 --head "${FORK_OWNER}:${BRANCH}" \
                 --title "$PR_TITLE" --body "$PR_BODY" 2>/dev/null) || pr_url=""
    fi
  fi

  if [ -n "$pr_url" ] && [ "$pr_url" != "null" ]; then
    cat <<EOF

Branch pushed: $BRANCH (one squashed commit)

Pull request ready — description already filled in:

  $pr_url

If it already existed, the force-push updated it. Tweak the description there if you like.
EOF
  else
    cat <<EOF

Branch pushed: $BRANCH (one squashed commit)

Couldn't open the PR automatically (sandboxed environment, or gh not authenticated).
Open it in your browser:

  $compare_url

You'll see one clean commit. Add a sentence or two of description, then click
"Create pull request". If a PR for this branch already exists, the force-push
already updated it; no further action needed.
EOF
  fi
}
