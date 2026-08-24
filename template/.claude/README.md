# Claude Code extras (optional)

**Slash commands.** Modes: `/kickoff`, `/brainstorm`, `/build`, `/review`. Agents:
`/design`, `/qa`, `/launch`. Each one just enters the matching section of
`COFOUNDER.md`. Plain phrases ("let's brainstorm", "QA this") work identically.

**Guard hook.** `hooks/cofounder-guard.sh` runs before every file edit and enforces the
rule in `COFOUNDER.md` → Git and parallel sessions: the main folder stays on `main`;
feature work happens in a worktree. If the folder is on another session's branch, the
edit is refused and the agent is told to make its own worktree. This is what turns the
rule into muscle memory instead of advice.

Using a different agent? Delete this folder. The rules in `COFOUNDER.md` still apply;
they are just not enforced by a hook.
