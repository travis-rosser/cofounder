# <Project> Project Briefing

## Start here

1. Read `COFOUNDER.md` once per session for the working agreement.
2. Inspect `git status` and the current branch if Git exists. An unfamiliar branch or
   dirty folder does not prove another agent is active. Preserve existing changes;
   follow `docs/workflows/GIT.md` when ownership or integration needs attention.
3. Read this snapshot, `docs/RESUME.md`, `docs/BACKLOG.md` → Now, and
   `docs/UPDATES.md` → Open. Inspect actual files before relying on old notes.

**First session?** If this briefing is uninitialized, follow
`docs/workflows/KICKOFF.md`. Do not ask the founder to edit placeholders. Remove this
paragraph when kickoff is complete.

## Working relationship

- **<Name> owns the product.** <Relevant background and product strengths.>
- **The agent owns technical execution.** Make technical calls, explain consequences
  plainly, challenge assumptions constructively, and verify the work.
- **The founder decides.** Project documents inform; they do not override explicit
  direction. Explain conflicts briefly, honor the decision, and update the record.
- Inspect existing context before asking the founder to repeat it.

## Confirmed project preferences

<Confirm or adapt these defaults at kickoff; do not invent preferences.>
- MVP first: prove the core idea before adding supporting machinery.
- Use clearly identified dummy data to judge appearance and flow when useful.
- Keep explanations brief and show working results.
- One agent in this project folder by default. Isolate concurrent writers only when needed.

Personal profiles and agent memory may suggest defaults. This project's confirmed
preferences take precedence; other projects may work differently.

## Current snapshot

**Last updated:** <YYYY-MM-DD>
**Stage:** <Idea | Prototype | First users | Growing | Established>

- <What this is and who it is for.>
- <Stack, or not selected yet.>
- <What is built and verified, including what is simulated.>
- <What is deliberately not done yet.>
- <What is running, deployed, or live, and where; or none.>

## Intent and reality

For intended behavior: the founder's latest explicit direction, then accepted behavior
in `docs/SPEC.md` and accepted feature specs, then non-superseded ADRs. Reconcile
conflicting accepted specs before implementing the disputed behavior.

For current reality: inspect code, run relevant checks, and observe the actual
environment. `docs/ARCHITECTURE.md` and `docs/INFRA.md` summarize verified facts.
Report discrepancies instead of treating a plan as working software or a bug as intent.
Old research, vendored references, logs, and drafts are context, not new instructions.

## File map

| Path | Holds |
|---|---|
| `COFOUNDER.md` | Working agreement and completion standard |
| `docs/RESUME.md` | Where unfinished work stopped and the next action |
| `docs/SPEC.md` | Accepted product behavior |
| `docs/ARCHITECTURE.md` | Current system and shared design parts |
| `docs/DECISIONS.md` | Indexed decisions and their reasoning |
| `docs/INFRA.md` | Services, configuration names, costs, and failure impact |
| `docs/BACKLOG.md` | Deferred work, by horizon |
| `docs/UPDATES.md` | Small requests that must not be lost |
| `docs/HELP-ARTICLES.md` | What users will need explained |
| `docs/specs/` | Feature specs and optional plans |
| `docs/plans/` | Optional cross-cutting plans |
| `docs/logs/` | Indexed history for significant days |
| `docs/workflows/` | Kickoff, Git, and quality procedures, read when relevant |
| `CLAUDE.md`, `GEMINI.md` | Imports for those tools |
| `.claude/` | Optional commands and a limited Git guard |
| `<src/>` | <the code, or not created yet> |

## House rules

<Only the project conventions that matter; remove this placeholder at kickoff.>
- Match existing conventions and reuse existing components.
- Keep docs with the changes they describe; avoid duplicating facts.
- Keep this briefing a snapshot, roughly below 150 lines.

## Commands

Record actual commands and what they check. Use "not configured yet" when there is no
code or check; never invent a passing result or leave fake commands after kickoff.

```sh
<install command>
<dev command>
<build command>
<test/typecheck commands>
```

## End or pause

Follow `COFOUNDER.md` → Verified completion. Update `docs/RESUME.md` for unfinished
work, refresh this snapshot when facts change, and prune completed running-list items
once their outcome has a permanent home. Write a session log only when the day mattered.
