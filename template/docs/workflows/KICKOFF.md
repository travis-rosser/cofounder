# First session and existing-project adoption

Use when installing the template or initializing the briefing. The founder should not
need to edit placeholders or operate Git.

## Preserve what already exists

Inspect the root, README, instructions, Git status, and existing docs before writing.
If adopting into an existing project, merge the template's useful rules into the current
structure. Do not replace an existing README, AGENTS.md, CLAUDE.md, GEMINI.md, docs, or
configuration with template stubs. Preserve founder preferences and project conventions.
Explain real conflicts and ask only when the answer cannot be inferred safely.

For new projects, copy template contents including hidden files into the root, without
nesting them in a `template/` folder. For existing projects, add missing files and merge
intentionally: combine missing `.gitignore` entries; add imports without replacing
existing entry-file instructions; merge optional `.claude/settings.json` hooks without
removing existing settings. Skip the optional hook if Python 3 is unavailable and say so.
Do not automatically install optional skills or delete another tool's configuration.

Reinstalling or upgrading must preserve completed docs and preferences. Review the diff,
check JSON configuration, avoid duplicate imports/hooks, and record the template commit
adopted in the project README. Do not infer that old decisions happened at installation.

## Establish the project

1. Verify the current tool reads the common briefing and working agreement. If automatic
   discovery is unavailable, explicitly load them and explain the limitation. Slash
   commands and hooks are optional and are not portable promises.
2. Follow `GIT.md`. Initialize Git if absent; preserve current work if it exists.
3. Use existing context first. Ask a few plain questions about the product, audience,
   what exists, what the smallest useful result is, and the founder's background and
   preferred working style. Non-technical does not mean inexperienced in product.
4. Confirm project preferences. Offer MVP-first, clearly identified dummy data for
   judging flow, brief explanations, and one-agent operation as adaptable defaults.
   Carry in personal preferences only when supplied or confirmed for this project.
5. Set the stage from evidence. Default to Idea only when nothing indicates otherwise.
   Fill the briefing and relevant spec/architecture facts; mark unknowns honestly.
   Record an ADR only for an actual decision with known reasoning.
6. Initialize `docs/RESUME.md` with the next concrete action. Keep other files as clearly
   marked stubs until needed. Remove briefing placeholders; commands with no implementation
   should say "not configured yet" rather than pretending code exists.
7. Read the short snapshot back to the founder and invite corrections. If a correction
   is necessary to continue, wait for it; otherwise continue already authorized work.
8. Remove the first-session marker and commit only the intended changes. Give the founder
   a clear next step. For existing projects, explain what was adopted and preserved.
