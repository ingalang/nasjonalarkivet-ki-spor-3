#!/usr/bin/env bash
set -euo pipefail

# Usage: scripts/start-issue.sh <ISSUE> [--autopilot] [--codex|--claude] [--no-start]
#
# Creates (or reuses) the branch <type>/<n>-<title-slug> from origin/main,
# checks it out in its own worktree under .worktrees/, fills in a template
# from scripts/templates/ and starts the agent there. The default is the
# brainstorm template and Codex (--codex); --claude starts Claude Code. <type> comes from the issue's labels:
# bug → fix, otherwise feat.
# --no-start creates the worktree and prints the command instead of starting
# the agent (used by the start-issue skill, which already runs in an agent).

ISSUE="" TEMPLATE="brainstorm" AGENT="codex" START=true
for arg in "$@"; do
  case "$arg" in
    --autopilot) TEMPLATE="autopilot" ;;
    --codex) AGENT="codex" ;;
    --claude) AGENT="claude" ;;
    --no-start) START=false ;;
    -*) echo "Unknown flag: $arg" >&2; exit 2 ;;
    *) ISSUE="${arg#\#}" ;;
  esac
done
[[ "$ISSUE" =~ ^[0-9]+$ ]] || { echo "Usage: $0 <ISSUE> [--autopilot] [--codex|--claude] [--no-start]" >&2; exit 2; }

ROOT="$(git rev-parse --path-format=absolute --git-common-dir)/.."
ROOT="$(cd "$ROOT" && pwd)"
git -C "$ROOT" fetch -q origin

BRANCH="$(git -C "$ROOT" branch -r --format='%(refname:short)' | grep -E "^origin/[^/]+/${ISSUE}-" | head -n1 || true)"
BRANCH="${BRANCH#origin/}"
if [[ -z "$BRANCH" ]]; then
  TITLE="$(gh issue view "$ISSUE" --json title --jq .title)"
  TYPE="feat"
  gh issue view "$ISSUE" --json labels --jq '.labels[].name' | grep -qx bug && TYPE="fix"
  SLUG="$(printf '%s' "$TITLE" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+//' | cut -c1-40 | sed -E 's/-+$//')"
  BRANCH="${TYPE}/${ISSUE}-${SLUG}"
fi

WT="$ROOT/.worktrees/${BRANCH#*/}"
if [[ ! -d "$WT" ]]; then
  if git -C "$ROOT" show-ref -q --verify "refs/heads/$BRANCH"; then
    git -C "$ROOT" worktree add -q "$WT" "$BRANCH"
  elif git -C "$ROOT" show-ref -q --verify "refs/remotes/origin/$BRANCH"; then
    git -C "$ROOT" worktree add -q -b "$BRANCH" "$WT" "origin/$BRANCH"
  else
    git -C "$ROOT" worktree add -q -b "$BRANCH" "$WT" origin/main
  fi
fi

mkdir -p "$WT/.agent"
ISSUE="$ISSUE" BRANCH="$BRANCH" awk '{
  gsub(/\{\{ISSUE\}\}/, ENVIRON["ISSUE"]); gsub(/\{\{BRANCH\}\}/, ENVIRON["BRANCH"]); print
}' "$ROOT/scripts/templates/$TEMPLATE.md" > "$WT/.agent/instructions.md"

PROMPT="Follow the instructions in .agent/instructions.md."
echo "✅ #$ISSUE → $WT ($BRANCH, $TEMPLATE)"
if [[ "$START" == false ]]; then
  printf 'Start the agent in a new terminal window:\n  cd "%s"; %s "%s"\n' "$WT" "$AGENT" "$PROMPT"
  exit 0
fi
cd "$WT"
exec "$AGENT" "$PROMPT"
