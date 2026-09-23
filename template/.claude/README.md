# Claude Code extras (optional)

Modes: `/kickoff`, `/brainstorm`, `/build`, `/review`. Quality lenses: `/design`, `/qa`,
`/launch`. They load the same procedures as plain phrases. They do not spawn agents.

The optional guard requires Python 3 and Git. It covers the edit tools listed in
`settings.json`, blocking detached checkouts. Normal single-agent feature branches are
allowed. Enable `git config --local cofounder.parallel true` only when starting concurrent
writers: then primary-checkout edits are also blocked, while linked worktrees are allowed.
See `docs/workflows/GIT.md` for setup, integration, and when to turn parallel mode off.

This is not a session lock. It does not cover shell writes, protect shared databases,
or prevent two sessions from sharing one worktree. A dirty folder alone does not establish
who owns the changes. Every agent still follows the documented workflow.

When adopting into an existing project, merge these optional settings and commands;
never overwrite existing configuration. If Python 3 is unavailable, skip this hook and
explain the reduced coverage. Other coding tools can keep this folder for future Claude
sessions; they follow the plain-language rules without this hook.
