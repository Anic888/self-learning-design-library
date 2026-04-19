#!/usr/bin/env bash
#
# monthly-research.sh — trigger the periodic-research subagent manually.
#
# Normally this runs automatically on the 1st of each month via a Claude Code
# scheduled task. Use this script to trigger it off-cycle (e.g. right after
# setup, or if you missed a cycle).
#
# Usage:
#   scripts/monthly-research.sh           # runs and commits+pushes
#   scripts/monthly-research.sh --dry-run # runs research but skips commit
#
# Prereqs:
#   - Claude Code installed (https://claude.com/claude-code)
#   - design-library repo at ~/Documents/design-library
#   - git configured with push access to origin

set -euo pipefail

DRY_RUN=false
if [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
fi

REPO_DIR="$HOME/Documents/design-library"

if [[ ! -d "$REPO_DIR" ]]; then
    echo "Error: design-library not found at $REPO_DIR" >&2
    exit 1
fi

cd "$REPO_DIR"

# Check git state is clean before starting
if [[ -n "$(git status --porcelain)" ]]; then
    echo "Error: repo has uncommitted changes. Commit or stash first." >&2
    echo "Running 'git status' to show you what's pending:" >&2
    git status
    exit 1
fi

# Build the prompt for Claude Code
DATE_STAMP=$(date +"%Y-%m")

if $DRY_RUN; then
    PROMPT="Invoke the periodic-research subagent with skip_commit:true. Date stamp: $DATE_STAMP. Return a summary of what would be refreshed without committing."
else
    PROMPT="Invoke the periodic-research subagent. Date stamp: $DATE_STAMP. Refresh all research sources, write snapshot files, update synthesis, commit and push."
fi

echo "Triggering periodic-research for $DATE_STAMP..."
if $DRY_RUN; then
    echo "(dry-run — no commit)"
fi

# Invoke Claude Code non-interactively
# Requires `claude` CLI installed and authenticated
if ! command -v claude >/dev/null 2>&1; then
    echo "Error: 'claude' CLI not found in PATH." >&2
    echo "Install from: https://claude.com/claude-code" >&2
    exit 1
fi

claude --prompt "$PROMPT" --no-input

echo "Done. Check $REPO_DIR/sources/research/ for new files."
