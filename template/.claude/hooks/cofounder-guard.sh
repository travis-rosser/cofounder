#!/bin/sh
# Cofounder guard. Runs before every file edit in Claude Code.
# Rule: the main project folder stays on `main`. Feature work happens in a worktree.
# If this folder is checked out on another branch, another session owns it: refuse.

input=$(cat)
file=$(printf '%s' "$input" | sed -n 's/.*"file_path" *: *"\([^"]*\)".*/\1/p')
dir=$(dirname "$file" 2>/dev/null)
[ -d "$dir" ] || dir=$(pwd)

root=$(git -C "$dir" rev-parse --show-toplevel 2>/dev/null) || exit 0

# In a linked worktree, git-dir and git-common-dir are different directories; in a normal
# checkout they are the same one. Git may report either as relative or absolute depending
# on where it was invoked, so resolve both to real paths before comparing. Comparing the
# raw strings silently treats every subdirectory as a worktree and lets the edit through.
gitdir_raw=$(git -C "$dir" rev-parse --git-dir 2>/dev/null)
common_raw=$(git -C "$dir" rev-parse --git-common-dir 2>/dev/null)
gitdir=$(cd "$dir" 2>/dev/null && cd "$gitdir_raw" 2>/dev/null && pwd)
common=$(cd "$dir" 2>/dev/null && cd "$common_raw" 2>/dev/null && pwd)
if [ -n "$gitdir" ] && [ -n "$common" ] && [ "$gitdir" != "$common" ]; then
  exit 0  # linked worktree, always allowed
fi

branch=$(git -C "$root" branch --show-current 2>/dev/null)
case "$branch" in
  main|master|"") exit 0 ;;
esac

cat >&2 <<MSG
Cofounder guard: this folder is checked out on '$branch', which belongs to another
session. Do not edit here. Either create your own worktree and work in it:

  git worktree add .worktrees/<short-name> -b feature/<short-name>

or tell the founder that another session is active on '$branch' and ask whether to wait.
MSG
exit 2
