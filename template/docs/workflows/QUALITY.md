# Design, QA, and launch

Read the relevant section when its trigger applies. These are review lenses for the
current agent, not a requirement to spawn additional agents.

## Design

Exists to prevent generic, forgettable interfaces. **Runs on its own whenever a screen a
user will see is built or changed.**

Standards:
- Make deliberate choices: typography, color, spacing, layout. Avoid the defaults every
  AI produces: stock gradients, glass effects, the same three fonts.
- **Shared parts, from the first screen.** A product looks homemade when every screen
  builds its own buttons, fields and cards, each slightly different. So when you build the
  first real screen, build the pieces it actually uses as shared parts in one place.
  Add other components when a screen needs them; do not build a component catalog upfront. Set one small list of text sizes,
  spacing steps, corner roundings and named colors at the same time. This is part of
  building that screen, not a separate phase before it.
- **Every later screen reuses the parts.** Before building a piece, check whether it
  exists. If it is missing, add it to the shared parts, not to the one screen. If a part
  needs to look different somewhere, give the part a new option; do not override it on
  that screen. If the project's tools come with a standard set of parts, build on that
  rather than from scratch.
- **Designs from elsewhere come in as parts.** When the founder brings a design from a
  design tool, a mockup, or another project, take its colors, type, spacing and
  components as the starting shared parts, fitted to this project's folder. Then build the
  screens from those parts. Do not paste the design in screen by screen, and do not keep
  two styles side by side.
- **Placeholder data is fine** for laying out and judging a screen; it is often the only
  way to see how it looks. Replace it with real data before real people rely on the
  screen, and never show made-up numbers to users as if they were real.
- Icons come from a real icon set. Default: **Font Awesome Free**, installed with the
  first screen. If the project already uses another set, stay with it. Never a typed
  symbol or a hand-drawn shape standing in for an icon.
- Design every state: empty, loading, error, partial, success. The empty state is the
  first thing a new user sees.
- Works on a phone. Readable contrast. Keyboard reachable.
- **Look at it yourself before calling it done.** Open the screen in a browser, at normal
  size and at phone size, and fix what is off. Reading the code is not looking. The
  founder should never be the first person to see a broken screen.
- Record the shared parts, where they live, and the lists of sizes and colors in
  `docs/ARCHITECTURE.md` → Design system, so the next session reuses them instead of
  rebuilding.

## QA

Exists to break things before users do. **Runs on its own before any Feature is called
done, and before anything touching money, user data, or authentication ships.** Skipped
for Tweaks; a verify is enough there.

Checks:
- Every state in the spec, including the failure states. Each one reachable and sane.
- Bad input. Empty input. Very long input. Double-submit. Refresh mid-flow.
- On a phone. On a slow connection.
- What else did this change touch? Run whatever tests exist.
- In a standalone Review, report findings without editing. During an authorized Build,
  the implementing agent fixes in-scope defects and reruns the affected checks. Do not
  make the founder approve routine repairs. Escalate changes to product scope or
  actions outside the authorization already given.
- Sort findings by stage: what blocks this stage, what can wait, and the consequence.
  Estimate time only when asked.
- Use isolated test data and sandbox services. Remove only fixtures created for this
  check; never delete real user data as cleanup or send test messages to real users.

## Launch

Exists because going live is where non-technical founders get stuck. **Invoked by "let's
launch", "go live", "deploy", and raised by the cofounder when the stage reaches First
users.**

Checklist:
- Hosting chosen and recorded in `docs/INFRA.md`. Domain pointed. HTTPS on.
- Every variable and secret listed in `docs/INFRA.md` with what breaks without it. No
  secret values anywhere in the repo.
- Errors are visible somewhere, so the founder can tell when something breaks.
- Data is backed up, or the founder has explicitly accepted that it is not.
- A rollback path exists: what to do if the launch is bad.
- A stranger can sign up and do the main thing without help. Try it.

## Optional accelerators

Published skill sets that make the agents sharper. Install what your tool supports; the
standards above apply either way.

| Skill | What it adds | Where |
|---|---|---|
| impeccable | Design direction, audits, polish. Works in Claude Code, Codex, Gemini CLI, Cursor. | https://github.com/pbakaus/impeccable (`npx impeccable install`) |
| frontend-design | Anthropic's guide to distinctive, non-generic UI. | https://github.com/anthropics/skills (`skills/frontend-design`) |
| superpowers | Brainstorming, test-first building, verification before "done", git worktrees. | https://github.com/obra/superpowers |

If a skill is referenced and not installed, offer to install it. Do not block on it.

