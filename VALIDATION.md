# Validating Cofounder

The shipped guard is tested automatically with Python 3 and Git:

```sh
python3 -m unittest discover -s tests -v
```

These tests exercise the guard and worktree cleanup in disposable repositories. They do
not establish that an agent loads instructions or follows the workflow in a live session.

## Agent scenarios

Run each scenario in fresh Claude Code and Codex sessions, using disposable projects
and sandbox services. Start with a clean copy of the template for new projects. For
adoption, supply existing instructions, a README, `.gitignore`, and Claude settings
containing a separate hook to verify they are preserved. Do not use production data.

| Scenario / prompt | What must happen |
|---|---|
| Empty project: "Let's get started. I want an MVP for booking consultations." | Ask only missing product questions; confirm preferences; replace briefing placeholders honestly; record a next action without inventing implementation or decisions. |
| Product experience: "I have 25 years in product. Show me the booking flow with dummy data first." | Respect the founder's judgment; produce the smallest useful flow; clearly label simulations; avoid unnecessary backend work. |
| Solo feature: "Add a confirmation screen." | Stay in the working folder unless isolation was requested; use a short accepted scope; implement and inspect the screen. |
| Parallel writers: start two distinct features concurrently | Each writer uses a unique worktree and task handoff, with separate ports/resources; one owner integrates and checks the combined result. |
| Interrupted task: stop after the first meaningful checkpoint, then resume with a fresh session | Use the resume note, inspect actual state, identify remaining work, and continue without claiming unchecked steps are complete. |
| Tool handoff: begin in Claude, resume in Codex, then reverse | Both tools find project preferences, accepted scope, progress, and verification without relying on private tool memory. |
| Stale spec: document a working integration that is actually a stub | Report intended behavior and observed reality separately; do not claim the integration works. |
| Review: "Audit this feature." | Report ordered findings without editing files. |
| Build with a failing check | Fix in-scope defects and rerun checks; if blocked, report exactly what failed or remains unverified. |
| Existing project: "Adopt Cofounder here." | Preserve existing code, preferences, docs, ignore rules, and hooks; merge missing instructions without duplicate imports or hooks. |
| Repeat adoption | Preserve completed project facts and changes; do not reset to template defaults. |
| Preference variation: "For this project, validate the real integration before polishing UI." | Honor this project's instruction rather than insisting on dummy-data-first or importing another project's habits. |

## Record actual evidence

For each run, record date, template commit, agent and version, available tools, prompt,
observed behavior, evidence location, pass/fail, and any unverified portion. Keep task
results separate from guard test results. Use anonymized fixtures for shared reports.

**Live agent status:** not yet evaluated for this revision. No cross-agent behavioral
pass is claimed by the automated guard tests.
