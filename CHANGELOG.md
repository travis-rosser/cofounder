# Changes

## 2026-09-23 — Simpler daily work, clearer continuity

- **Support one agent or several.** One agent can work in one folder. Concurrent writers
  get separate working copies, task notes, and one integration owner.
- **Keep preferences with the project.** Every agent can read the same confirmed working
  preferences. Personal defaults are optional; projects can differ.
- **Start small.** MVPs and clearly identified dummy data are useful defaults. Build the
  machinery when the current problem needs it, not for hypothetical scale.
- **Respect product experience.** Non-technical does not mean inexperienced. Record the
  founder's background and tailor the collaboration accordingly.
- **Push back constructively.** Suggest a smaller experiment, explain the tradeoff once,
  and honor the founder's decision unless new evidence changes the situation.
- **Leave a place to resume.** A short checkpoint captures unfinished work, checks, and
  the next action for the same agent returning later or a different agent taking over.
- **Separate plans from working software.** Specs describe intent; inspection and actual
  checks establish what works. Report disagreements clearly.
- **Make completion checkable.** Report what changed, what was checked, simulations,
  limitations, and any next action. Fix ordinary in-scope defects during a build.
- **Shorten daily instructions.** Detailed kickoff, Git, design, QA, and launch procedures
  load when needed instead of all being mandatory startup reading.
- **Adopt safely into existing projects.** Preserve current docs and settings, merge
  instructions deliberately, and avoid duplicate imports or hooks on repeat adoption.
- **Choose services for the project.** Consider budget, existing accounts, current
  requirements, and switching cost. Offer remote backup early.
- **Correct and test the Git guard.** Allow solo feature branches, make parallel mode
  explicit, handle nested new paths and JSON correctly, and remove worktrees before
  deleting their branches. Document the guard's limited coverage and Python 3 dependency.
- **Test agent behavior separately.** Add repeatable scenarios for Claude Code and Codex;
  automated guard checks are not evidence that live agents passed those scenarios.
