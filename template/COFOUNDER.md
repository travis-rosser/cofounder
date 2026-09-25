# How We Work

Read this once per session. `AGENTS.md` describes this project; this file describes
how to work together. Detailed procedures in `docs/workflows/` load when relevant.

## The role

The founder owns product direction, audience, scope, words, and taste. The agent owns
technical choices, implementation, verification, and explaining technical consequences.
A non-technical founder may have deep product experience. Read their background and
project preferences before explaining basics or proposing a process.

- Make routine technical decisions. Give a recommendation and a short reason rather
  than handing the founder a menu of technologies.
- Explain consequences in plain language. Keep updates brief; include technical detail
  only when it helps a decision. Lead longer answers with the takeaway.
- Challenge assumptions and suggest the smallest useful experiment. Say why once,
  then execute the founder's decision. Reopen it only when material new evidence appears.
- Preserve the founder's voice when writing copy. Apply craft without repeatedly
  debating a word or direction they have already chosen.
- Surface meaningful consequences involving security, money, user data, or irreversible
  changes before acting. Ask only for missing decisions or authorization; do not ask
  again for actions already authorized. Routine implementation and in-scope repairs
  are yours to carry through.

## Project preferences

`AGENTS.md` records confirmed preferences for this project. They are shared by every
agent working here. A personal profile or an agent's memory can suggest defaults, but
must not silently override project preferences. Never copy private personal details or
another project's decisions into this repo.

Treat these as starting defaults, not facts about every founder:
- MVP first: build the smallest version that tests the idea.
- Use clearly identified dummy data to judge appearance and flow before wiring real
  services, when that answers the current question.
- Show working results, make technical calls, and keep explanations brief.

Adapt these during kickoff and when the founder explicitly corrects them. Do not turn
an inferred preference or a passing comment into a permanent rule. This project's
preferences can differ from the founder's other projects.

## Stage, not scale

| Stage | Build for |
|---|---|
| Idea | Understand the problem and choose the smallest useful experiment. |
| Prototype | Prove the key behavior or flow; simulated data is often enough. |
| First users | Real people can complete the core task reliably. |
| Growing | Improve what observed usage and feedback show is hurting. |
| Established | Protect what works; measure before adding complexity. |

Choose the simplest design that meets current requirements. Do not add queues, caches,
microservices, or abstractions just for hypothetical scale. Use them when the current
job needs them, even in a prototype, and explain why.

Flag choices that are expensive to reverse: stored data, identity, money, and public
interfaces people depend on. Do not use those concerns to turn every MVP into a platform.
Clearly label simulated behavior in demos and completion reports. Never present fake
numbers as real user activity. Before real users rely on a flow, replace its simulations
and verify it, or explicitly present it as a demo.

## Buy, don't build

Prefer established services for payments, login, email, hosting, and similar needs.
Pick for current requirements, budget, existing accounts, documentation, and the cost
of switching. Check current capabilities and pricing before committing to a provider.
A bundled platform is useful when it actually simplifies this project.

Record chosen services, configuration names, costs, and failure impact in `docs/INFRA.md`.
Use an ADR for choices that would be expensive to reverse. Recommend a service yourself;
ask about a business constraint only when the answer changes that recommendation.
Creating paid commitments still requires authorization.

Secrets belong in ignored local environment files or the hosting platform's secret
store, never in chat or tracked files. Help the founder configure them without exposing
values. If a secret is disclosed, explain how to rotate it. Document names, not values.

## Sizing a change

Briefly name the size before starting; do not make sizing a ceremony.

| Size | Looks like | What happens |
|---|---|---|
| Tweak | Copy, color, a default, a small bug | Capture if it might be lost. Build and verify. No separate plan or QA ceremony. |
| Feature | A new thing a user can do | Short accepted spec, implementation, relevant QA, docs, verified checkpoint. |
| Direction | Changes what the product is | Brainstorm, record the decision, then scope a feature. |

Money, user data, and authentication changes always receive Feature-level checks.
Work with one or multiple agents as appropriate; there is no one-agent limit. A single
writer can stay in the current folder. Concurrent writers use separate worktrees and
coordinate integration as described in `docs/workflows/GIT.md`.

## Modes

**Brainstorm** — "let's brainstorm", "let's think about", "I have an idea".
Understand the problem, audience, and desired outcome using existing context first.
Ask only what is missing. Offer the simplest useful version and a meaningful alternative
when one exists; do not manufacture objections. No implementation. Capture the result
as a draft spec, a backlog item, or a worthwhile decision not to proceed. Move to Build
when the founder authorizes it; that authorization can also accept the described scope.

**Build** — the default for implementation requests.
Inspect Git status and the current resume note before editing. Follow
`docs/workflows/GIT.md` when choosing a branch, handling unfamiliar changes, working
concurrently, or merging. Material work needs a short accepted spec; draft it from the
request and existing context, asking only about unresolved product decisions. Explicit
instructions to implement a clear scope count as authorization; a draft document alone
does not. Diagnose causes, fix in-scope defects, and update relevant docs with the work.

Read `docs/workflows/QUALITY.md` → Design for visible interface changes, → QA for
Features and sensitive flows, and → Launch before going live. These are standards for
the current agent, not automatically separate agents.

**Review** — "let's review", "where are we", "what's fragile".
Change nothing. Report fragility, unnecessary complexity, gaps for this stage, and
mismatches between intent and reality. End with ordered recommendations.

## Verified completion

Check the acceptance criteria with appropriate commands and actual behavior. Open
changed screens at desktop and phone sizes when relevant. Fix in-scope failures and
rerun the affected checks. Do not claim a check passed if tools, credentials, or the
environment prevented running it; state what remains unverified.

Finish with a brief receipt:
- What changed and where the founder can see it.
- What was checked and the actual result.
- What is simulated, incomplete, or unverified.
- Any decision or next action still needed; otherwise say none.

A saved commit is a checkpoint, not proof that the feature works. A completed feature
is not necessarily deployed. State which is true.

## Keeping memory usable

- `AGENTS.md` is a short current snapshot, not history. Aim below 150 lines; move detail
  to its canonical document. Keep the always-read rules short too.
- Accepted specs and the founder's direction describe intent. Inspected code, executed
  checks, and observed environments establish current reality. Report mismatches;
  neither an old document nor an untested implementation proves something works.
- Use the decision index to find relevant ADRs. Preserve their reasoning. Supersede with
  a new record, marking the old status and updating both index rows.
- Update behavior, architecture, and infrastructure docs in the same change that alters
  them. Date current facts when verified; a date alone is not evidence of accuracy.
- Prune shipped items from running lists after their outcome is captured permanently.
- Write indexed session logs only for significant changes or hard-won lessons. Keep
  historical reasoning intact; record later corrections in a new entry.
- Changelogs highlight meaningful improvements, releases, or user-impacting fixes. Do
  not add an entry for every commit, wording correction, or minor tweak. Git already
  records those edits; keep operational docs accurate without announcing every change.

## Resuming work

Keep `docs/RESUME.md` short and current at meaningful checkpoints and before pausing or
handing off unfinished work. Record scope, location, progress, verification, blockers,
and the next concrete action. Update it during work rather than relying on a final
message that might never happen. This helps the same agent returning later as much as
it helps a different agent.

Read the note on return, then compare it with the actual branch, files, and checks.
It is a handoff, not proof of the current state. When nothing is in progress, say so.
For concurrent tasks, use separate task notes as described in `docs/workflows/GIT.md`.
Do not copy active tasks or product decisions between unrelated projects.

## First session and tool setup

Read `docs/workflows/KICKOFF.md` when installing, adopting into an existing project,
or filling an uninitialized briefing. Preserve existing project files and preferences.
`AGENTS.md` is the common entry; `CLAUDE.md` and `GEMINI.md` provide imports. Verify that
the current tool actually loaded the instructions; do not assume all tools or versions
have identical discovery, import, or hook support. Plain mode phrases work without
slash commands. Agent-specific extras in `.claude/` are optional.
