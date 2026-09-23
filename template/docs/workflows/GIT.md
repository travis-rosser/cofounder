# Git and working folders

Read when setting up Git, choosing a branch, handling unfamiliar changes, running
concurrent writing sessions, or integrating work. The founder never needs to type a
Git command. Use plain-English commit messages and explain consequences briefly.

## Default: one agent, one project folder

Work in the existing folder. A feature branch in that folder is fine; do not create a
worktree merely because the task is a Feature. Respect the project's established branch
and review workflow. Resume an existing task branch rather than switching it blindly.

Inspect status before editing. Dirty files can be unfinished work from this same task,
the founder's edits, or someone else's changes. Use the resume note and diffs to determine
what is yours. Preserve unfamiliar changes; do not reset, stash, commit, or overwrite them
without authorization. Continue independent work when safe; ask only when ownership
ambiguity blocks the requested edit. A clean status is not a lock on the folder.

If Git is absent, initialize it during kickoff. If HEAD is detached, create or switch to
an appropriate task branch before editing. Detect the existing default/integration
branch; do not assume it is named `main`.

Commit coherent verified changes, staging only intended files. An unfinished checkpoint
may be saved when useful, but label it unfinished and record failed or missing checks.
Offer a private remote backup early; local commits alone do not protect against loss of
the computer. Honor existing publishing authorization and branch protections.

## Optional: concurrent writing sessions

Use one worktree (a separate working copy) and branch per concurrent writer, including
Tweaks. Do not share a writing folder. Honor a worktree already supplied by the host.
The primary checkout is reserved for integration while concurrent work is active.

Before launching concurrent writers, in a clean primary checkout:

1. Identify the integration branch and fetch current remote state when available.
2. Enable the optional Claude guard's parallel mode with
   `git config --local cofounder.parallel true`.
3. Create each worktree with a unique name, for example
   `git worktree add .worktrees/<task> -b feature/<task> <integration-branch>`.
4. Give each writer a separate dev-server port and isolated test resources where needed.
   Worktrees isolate files, not databases, accounts, remote services, or ports.

Each concurrent task uses `docs/handoffs/<task>.md` copied from `docs/RESUME.md`.
Record its location and next action there. Avoid having all writers update the same
resume note. The integrating agent reconciles the shared snapshot and resume note.

One integrating agent merges at a time. Wait for other merges; do not start a second
integration session. Check that the primary checkout is clean and on the intended
integration branch. Merge without discarding changes. Resolve conflicts only when
intent is clear, and rerun checks affected by the combined result. When edits are needed
for conflict resolution or shared docs, do them in a dedicated integration worktree
on a temporary branch, then fast-forward the clean primary checkout to that verified
commit. Keep parallel mode enabled while writers are active. Then remove the clean,
finished worktree (`git worktree remove <path>`) before deleting its merged branch
(`git branch -d <branch>`). Do not force cleanup of uncommitted work.

When all concurrent writers have stopped, disable parallel mode with
`git config --local cofounder.parallel false` to resume normal single-folder editing.
Never toggle it merely to bypass a guard while another writer is active.

## What the Claude guard does

The optional hook uses Python 3 and Git. It blocks covered file-edit tools in detached
checkouts, and blocks edits in the primary checkout when `cofounder.parallel` is true.
Normal single-agent feature branches and linked worktrees are allowed.

It is a limited guard, not a session lock or a security boundary. Shell writes and tools
outside the configured matcher are not covered. It cannot establish file ownership,
serialize merges, or detect two sessions sharing a linked worktree. The workflow above
still applies in every tool. Test results for the hook are not proof of live agent behavior.
