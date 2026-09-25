# Cofounder

Cofounder is a project harness that turns your AI coding agent into a technical cofounder:
one that remembers what you're building, has opinions about how to build it, and guides you
the way a real technical cofounder would.

It holds everything a project needs to survive being built one session at a time. A
briefing the agent reads before it touches anything. A permanent record of what you
decided and why, so nobody reopens it in six weeks. The rules for how it builds, when it
argues with you, and what it will never do without telling you first.

Copy it into your project, say "let's get started," and the agent interviews you and fills
the whole thing in.

---

## Why "Cofounder"

Have you ever thought you needed a technical cofounder before you could build anything?

They're the hardest hire in software. Rare, expensive, they want equity, and even when you
find one, the two of you working well together is luck. Most builders never get that
person.

Your agent could do that job. Out of the box it doesn't. It builds what you ask, agrees
with almost everything you say, and shows up every morning knowing nothing about what
you're building.

Cofounder changes how it thinks, not just what it knows. It sizes a request before it
starts. It builds for the stage you're actually at instead of the one you're imagining.
And it holds onto the point of the whole thing while it works.

That last one is the part people underestimate. An agent doesn't go off the rails because
it's careless. It goes off because each next step looked reasonable on its own, and so did
the one after that, and six reasonable steps later it's building something you never asked
for. It has nothing to check itself against.

Cofounder is what it checks against. What you're building and why, what you already
decided, what's deliberately out of scope, all written down and read before it starts. So
drift gets caught while it's still one step off, not six.

A cofounder tells you you're heading the wrong way. An agent that only wants to be helpful
gets you there faster.

---

## Who this is for

The product person. The business person. The person who knows an industry inside out and
can see the thing that ought to exist in it.

You don't have to be technical to start building something with an AI agent. You don't
have to be an engineer.

What you need is to know your product, or your idea, or your industry. The agent is going
to bring you real decisions: what this is for, who it's for, what's in and what's out, and
what the smallest version is that proves it. That's the cofounder's half of the deal.
Your half is to decide.

If you're a strong engineer, you'll probably build your own version of this, and you'd be
right to. I built this one for everyone else.

---

## How your agent remembers today

Agents differ in how they retain conversations and personal memory. That does not give
your project a shared, inspectable record that every agent can reliably pick up.

Cofounder puts that record alongside the code. The briefing is `AGENTS.md`; the template
also supplies `CLAUDE.md` and `GEMINI.md` imports. Setup checks that your tool actually
loads the instructions instead of assuming every version behaves the same way.

The trap is putting everything in that first file: decisions, mistakes, conventions,
roadmaps, and months of history. It grows, gets stale, and makes the useful facts harder
to find. So keep the current picture short and link to the details when they matter.

---

## How it works

Cofounder fixes that, and the memory is the smaller half of it.

### The memory half

Instead of one giant file, there are four tiers, ordered by how often the agent reads
them. The one it reads every session is the shortest on purpose.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#ffffff','primaryTextColor':'#18181b','primaryBorderColor':'#3f3f46','secondaryColor':'#fafafa','tertiaryColor':'#ffffff','lineColor':'#52525b','textColor':'#18181b','clusterBkg':'#f4f4f5','clusterBorder':'#a1a1aa','edgeLabelBackground':'#ffffff','nodeBorder':'#3f3f46'},'flowchart':{'padding':14,'nodeSpacing':20,'rankSpacing':26,'diagramPadding':16,'useMaxWidth':true}}}%%
flowchart TB
    subgraph T0["TIER 0 · Read every session"]
        CM["<b>AGENTS.md</b> · the briefing<br/><i>Where are we right now</i>"]
        COF["<b>COFOUNDER.md</b><br/><i>How the agent behaves</i>"]
        RES["<b>RESUME.md</b><br/><i>Where to pick up</i>"]
    end
    subgraph T1["TIER 1 · Permanent reference, read when relevant"]
        SPEC["<b>SPEC.md</b> · <i>what it is</i>"]
        ARCH["<b>ARCHITECTURE.md</b> · <i>how it is built</i>"]
        DEC["<b>DECISIONS.md</b> · <i>why, append-only</i>"]
        INFRA["<b>INFRA.md</b> · <i>what breaks without what</i>"]
        FLOW["<b>docs/workflows/</b> · <i>procedures when needed</i>"]
    end
    subgraph T2["TIER 2 · Running lists, appended and pruned"]
        BACK["<b>BACKLOG.md</b> · <i>decided later</i>"]
        UPD["<b>UPDATES.md</b> · <i>small, real, easy to lose</i>"]
        HELP["<b>HELP-ARTICLES.md</b> · <i>what users will need explained</i>"]
    end
    subgraph T3["TIER 3 · Feature records and indexed history"]
        SPECS["<b>docs/specs/</b> · <i>one design doc per feature</i>"]
        PLANS["<b>docs/plans/</b> · <i>cross-cutting plans</i>"]
        LOGS["<b>docs/logs/</b> · <i>what happened on the big days</i>"]
    end
    T0 ~~~ T1 ~~~ T2 ~~~ T3

    classDef box fill:#ffffff,stroke:#52525b,color:#18181b,stroke-width:1px
    class CM,COF,RES,SPEC,ARCH,DEC,INFRA,FLOW,BACK,UPD,HELP,SPECS,PLANS,LOGS box
    style T0 fill:#f4f4f5,stroke:#a1a1aa,color:#18181b
    style T1 fill:#f4f4f5,stroke:#a1a1aa,color:#18181b
    style T2 fill:#f4f4f5,stroke:#a1a1aa,color:#18181b
    style T3 fill:#f4f4f5,stroke:#a1a1aa,color:#18181b
```

Each file has one job. The agent reads the briefing, working agreement, and resume note
each session, checks the current queues, and loads detailed procedures when relevant.
This limits routine reading; it does not guarantee perfect recall or performance.

Three things make that hold up over months:

- **Everything the agent reads costs attention.** Whatever loads at the start of a session
  competes with the actual work. Give it a novel and it does worse at the job. So one
  short file describes the present, and anything that only ever grows, like decisions and
  session logs, gets an index instead of being read front to back.
- **Stale text is worse than no text.** You'd read an old note and think "that's probably
  not true anymore." The agent won't. It'll build it. So every file says what it's in
  charge of and records when current facts were checked. A date alone does not prove accuracy.
- **Decisions have to defend themselves.** If you don't write down why you chose
  something, a future session will helpfully undo it. And the part that does the real work
  isn't the decision, it's the list of what you rejected and why.

### The bigger half

One file, `COFOUNDER.md`, tells the agent how to *act*. Not what the project is, but how a
technical cofounder behaves. You're the product owner: you decide what gets built and
whether it's any good. It decides whether the build is correct, and runs the work. It
makes the technical calls instead of asking you about plumbing. It explains in
consequences, not technologies. It says what it thinks once and then builds. It sizes
every request before starting. It builds for the stage you're at, not the one you're
dreaming about. It never touches money, login, or user data without telling you. It runs
the tests, keeps the docs honest, and handles git so you never have to.

Day to day, it comes out like this. You sit down, say what you're thinking, and start
riffing with something that already knows the project. Nothing gets re-explained. It's
keeping track of the decisions, the roadmap, the structure, the lessons you learned the
hard way. All the things a normal human would keep track of.


## Why it's a folder of files and not an app

Three reasons.

**It is designed to travel between agents.** The common instructions are plain Markdown.
Tool-specific entry files and optional Claude commands sit around them. Discovery,
imports, and hooks differ by tool, so kickoff verifies what loads. The same project
preferences and resume note stay in the repo regardless of which agent reads them.

**You can read it.** Open `COFOUNDER.md` and you'll see, in plain English, how your
cofounder thinks. No generator, nothing hidden. If you want to know why it just pushed back
on you, the reason is in a file you can open.

**You can change it.** Disagree with a rule? Edit the line. The whole idea is that you're
the authority and the files are input. Software that tells you how your cofounder should
behave would have that backwards.

---

## If someone technical asks what this is

There isn't a settled name for this category yet, which is why we started calling it a
**project harness**. An eval harness wraps a model. A wiring harness wraps a machine. A
project harness wraps a project. It's the layer between your agent and the thing you're
building.

Underneath, it's four things that already exist, combined:

| What it does | What it's called | Where it came from |
|---|---|---|
| Docs live in the project, saved alongside the code | **docs-as-code** | The Write the Docs community |
| One record per decision, never edited, only added to | **ADR** (Architecture Decision Record) | Michael Nygard, 2011 |
| A folder you copy to start a project | **repo template**, **scaffold** | GitHub template repos, `cookiecutter` |
| Deciding what an agent reads before it acts | **context engineering** | Newer, 2024 or so |

So if you need the one-liner: Cofounder is a project harness: docs-as-code and decision
records, arranged as context engineering for a coding agent.

---


## How an idea moves through it

The whole point is that a thought you had in a chat doesn't die in the chat. Here's the
path it takes.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#ffffff','primaryTextColor':'#18181b','primaryBorderColor':'#3f3f46','secondaryColor':'#fafafa','tertiaryColor':'#ffffff','lineColor':'#52525b','textColor':'#18181b','clusterBkg':'#f4f4f5','clusterBorder':'#a1a1aa','edgeLabelBackground':'#ffffff','nodeBorder':'#3f3f46'},'flowchart':{'padding':18,'nodeSpacing':40,'rankSpacing':50,'diagramPadding':20,'curve':'basis','useMaxWidth':true}}}%%
flowchart TB
    IDEA(["A thought<br/>in conversation"])

    IDEA -->|"small"| UPD["UPDATES.md"]
    IDEA -->|"later"| BACK["BACKLOG.md"]
    IDEA -->|"material"| SPECS["docs/specs/<br/>dated design doc"]

    UPD -->|"grows up"| BACK
    BACK -->|"scheduled"| SPECS
    SPECS --> PLAN["matching<br/>-plan.md"]
    PLAN --> BUILD["Build it"]

    BUILD --> SPEC["SPEC.md<br/><i>behavior accepted</i>"]
    BUILD --> ADR["DECISIONS.md<br/><i>if load-bearing</i>"]
    BUILD --> ARCH["ARCHITECTURE.md<br/><i>if the system changed</i>"]
    BUILD --> INFRA["INFRA.md<br/><i>if config changed</i>"]
    BUILD --> LOG["docs/logs/<br/><i>if the day was big</i>"]

    SPEC --> SNAP["The briefing<br/><i>snapshot refreshed</i>"]
    ADR --> SNAP

    classDef box fill:#ffffff,stroke:#52525b,color:#18181b,stroke-width:1px
    class IDEA,UPD,BACK,SPECS,PLAN,BUILD,SPEC,ADR,ARCH,INFRA,LOG,SNAP box
```

The one rule under all of this: **the docs change in the same commit as the behavior.**
Not after. A doc you'll update later is a doc you'll never update.

---

## Intent and reality

Two files will disagree. Cofounder separates what you want from what currently works.

**Intent:** your latest explicit direction comes first, followed by accepted specs and
non-superseded decisions. Drafts and old research do not silently become requirements.
If accepted specs disagree, the agent reconciles the disputed behavior before building.

**Reality:** the agent inspects code, runs checks, and observes the actual environment.
Architecture and infrastructure docs summarize those facts; they cannot prove a feature
works just by saying it does.

If the spec says billing works but the implementation is incomplete, the agent reports
both facts. A bug does not become a requirement, and a plan does not become a shipped
feature. Your decision resolves the intended behavior, and the docs change with it.

---

## The files, one at a time

### The briefing: `AGENTS.md`

**Root of the repo. The common starting point for a session.**

The one file that answers "where are we right now" in a single read. Keep it short. Letting
it grow is the number one way this whole thing falls apart, and it grows on its own if you
let it.

What's in it:

- **Working relationship.** Who decides what. Be blunt here.
- **Current snapshot.** Dated, with the project's **stage**. What's built, what stack,
  what's running, what you're deliberately not doing.
- **Confirmed project preferences.** How this founder wants this project built.
- **Intent and reality.** What should happen versus what has been verified.
- **File map.** A table of what lives where.
- **House rules.** The handful of conventions that actually get broken. Not all of them.
- **Documentation rules.** When a spec is required, how decisions get superseded, when
  docs have to change alongside behavior.
- **Session protocol.** What to read at the start, what to update at the end.
- **Commands.** How to run, build, test.

What's *not* in it: history, changelogs, reasoning. If you catch yourself explaining *why*
in this file, that's a decision record. Move it.

### `COFOUNDER.md`: how the agent behaves

The short working agreement, read each session. Detailed kickoff, Git, design, QA, and
launch procedures live in `docs/workflows/` and load when needed.

**The role.** You own product decisions. The agent makes technical calls, explains their
consequences, challenges assumptions, and follows through. It can recommend a simpler
experiment without repeatedly arguing after you decide. New evidence can justify a new
conversation.

**MVP first.** Build the smallest useful version. Use clearly identified dummy data to
judge appearance and flow before wiring services when that answers the question. Real
users must not mistake simulated behavior for a working integration.

**Stage, not scale.** Avoid machinery for hypothetical future needs. Use the simplest
option that meets today's requirements. Flag choices that would be expensive to reverse,
without using them as a reason to overbuild the whole product.

**Buy, don't build.** Prefer established services where appropriate. Choose for current
requirements, budget, existing accounts, and switching costs. Check current capabilities
and pricing; record the choice in `INFRA.md`. Secrets never go in tracked files or chat.

**Sizing.** A Tweak gets implemented and verified without a separate planning ceremony.
A Feature gets a short accepted spec and relevant QA. A Direction gets a brainstorm and
recorded decision. Money, data, and login changes always get Feature-level checks.

**Modes.** Brainstorm clarifies and scopes. Build implements and verifies. Review audits
without making changes. Plain phrases work; Claude commands are optional conveniences.

**Quality lenses.** The current agent applies Design standards to visible interfaces,
QA to features and sensitive flows, and Launch checks before going live. These are not
mandatory extra agents. During a build, it repairs ordinary in-scope defects itself;
a standalone review remains read-only. Optional skills can add depth.

**Done means checked.** The agent reports what changed, where you can see it, what it
actually verified, what is simulated or unverified, and any decision still needed.
A commit is not proof of correctness, and a completed change is not necessarily deployed.

**One agent or several.** Both are supported. A single agent can stay in the project
folder, including on a feature branch. Concurrent writers each get a separate worktree
and branch, even for small changes. One agent integrates at a time and verifies the
combined result. Worktrees separate files, not databases or external accounts.

**The optional guard.** In Claude Code, a small hook blocks covered edits on detached
checkouts. Enabling parallel mode also reserves the primary checkout for integration.
It allows normal single-agent branches. It is not a lock: shell writes and shared
resources are outside its coverage. Python 3 is required for this optional hook.

**First session.** Inspect what exists, ask only what is missing, confirm preferences,
and leave a useful briefing and next action. Existing projects keep their docs and
configuration; adoption merges useful rules instead of overwriting them with stubs.

### Preferences belong to this project

Your product experience and working preferences should be available to every agent in
this project. Record confirmed preferences in `AGENTS.md`. The default suggestions are
MVP-first, dummy data when useful, and brief explanations. These are defaults, not
requirements for every founder or every project. One or multiple agents are supported;
the template does not prescribe an agent count.

An optional personal profile can provide a starting point. This project's confirmed
preferences win. Do not transfer unrelated product decisions or private personal details
between projects, and do not turn an agent's guess into a permanent preference.

### `docs/RESUME.md`: where to pick up

A short, mutable checkpoint: accepted scope, branch or worktree, last verified code commit,
what is complete, what remains, actual check results, blockers, and the next action.
Update it at meaningful checkpoints and before pausing. Read and verify it on return.

This is useful even when you stay with the same agent. It is also the handoff when you
switch tools within the same project. Concurrent tasks use separate notes in
`docs/handoffs/` so they do not all rewrite the same checkpoint.

### `docs/workflows/`: details when needed

- `KICKOFF.md`: new-project setup and safe existing-project adoption.
- `GIT.md`: single-folder work, optional concurrent worktrees, integration, and guard limits.
- `QUALITY.md`: design, QA, launch, and optional skills.

Keep the working agreement short; move procedure details here when they are only needed
for a particular kind of work.

### `docs/SPEC.md`: what it is

The source of truth for accepted intent. When observed behavior disagrees, report the
mismatch; verify implementation before claiming the intended behavior works.

Keep it to what someone can do and what happens when they do it. Not how it's built. Once a
project has a lot of features, this file turns into an index and the detail moves to
`docs/specs/`.

### `docs/ARCHITECTURE.md`: how it's built

The running pieces, stack, folder layout, shared design parts, and how data moves.
Link to the backlog and accepted specs for planned work; keep future work separate
from the system that actually exists.

It describes the system that *actually exists*. Ideas live in a spec or a decision record
until they're real.

### `docs/DECISIONS.md`: why

The most valuable file, and the one everybody skips. Every real decision gets a numbered
record:

```markdown
## ADR-007: Short imperative title

**Date:** YYYY-MM-DD
**Status:** Accepted | Proposed | Superseded by ADR-NNN

### Context
What was true that forced a choice.

### Decision
What we chose. Present tense, unambiguous.

### Alternatives rejected
What else was on the table and why it lost. This is the part that stops
the same debate happening again in four months.

### Consequences
What we now accept, including the bad parts.
```

**You only add to this file.** To change a decision, write a new record that supersedes the
old one and mark the old one superseded. You never edit history.

Which means it only grows, so it opens with an index: number, title, status. That's what
keeps it usable at forty decisions. You read the index, see which are still live, and open
the one record you need instead of the whole file. Superseding is three edits: the new
record, a mark on the old one, and both index rows.

A decision belongs here if reversing it would be expensive, or would surprise somebody.

### `docs/INFRA.md`: what breaks without what

Every setting, environment variable, secret name, outside service, domain, and scheduled
job. Plus **what breaks if it goes missing.** That last column is the whole point.

Write it for the version of you at 11pm, when something's down and you can't remember what
`CONNECTION_KEY_SECRET` does or where it lives.

Never put secret *values* here. Just the name, where it's set, what uses it, and what
happens when it's gone. This is also where the operational gotchas live: "this needs a
server restart," "this port collides with that other project."

### `docs/BACKLOG.md`: decided later

Work you've deliberately put off, sorted by horizon: Now, Next, Later, Parked. It exists so
that a real decision to wait doesn't look identical to forgetting.

### `docs/UPDATES.md`: small and real

Things you noticed while using the product. Too small for a spec, too real to lose. Two
sections, Open and Shipped, with dates. If something in here grows up into real behavior,
promote it.

### `docs/HELP-ARTICLES.md`: what users will need explained

While you're building, you keep noticing things a real user will trip over. You have no
help centre yet, so there's nowhere to put that thought and it evaporates. This is where
it goes.

It's the same logic as `UPDATES.md`: the moment you can see the confusion is the moment
you're deep in the work, and that moment doesn't come back. By the time you're actually
writing support docs, the list is already there.

Optional. Delete it if the project will never face users who need explaining to.

### `docs/specs/`: one design doc per feature

`YYYY-MM-DD-short-description.md`, with a matching `-plan.md` when the build needed one.
This is the spec, plan, code sequence made permanent, so the reasoning behind a feature
outlives the session that built it.

A spec has: the problem and desired outcome, scope, flow, failure states, data changes,
open questions, and acceptance criteria. Identify simulated behavior and, when useful,
the assumption being tested and the evidence that would change your mind.
The template ships `SPEC-TEMPLATE.md` and `PLAN-TEMPLATE.md` in this folder. Copy them,
don't edit them.

Mark a spec `Draft` until its scope is accepted. An explicit request to implement a
clear scope can accept it; merely writing a draft does not authorize a build.

### `docs/plans/`: plans that cross features

Migrations, refactors, anything that touches more than one feature. A plan for a single
feature goes next to its spec instead. Optional. Delete it if you never use it.

### `docs/logs/`: the big days

Not a transcript. A handoff, written so a session that wasn't there can pick the work up.
Write one when a day materially changes direction, architecture, or what's shipped, or when
you learned something the hard way. Skip it for a normal day. Most days need nothing.

`YYYY-MM-DD-short-description.md`, same as a spec. **Its line goes in the folder's index in
the same change that writes it.** That index is the whole point: at thirty logs it's how
you find the one day that matters without opening thirty files. A log nobody can find is a
log nobody reads.

A good one has: what the session set out to do, what changed, what got decided and where
it's recorded, **the corrections and surprises**, where things stand now, and the next
action.

The corrections section is the one people cut. Don't. That's where the expensive lessons
are.

Logs are never edited afterward and never deleted. If one turns out to be wrong, that's a
new log or a new decision record, not a rewrite of the old one.

---

## The rules

1. **Separate snapshot, progress, and history.** The briefing describes the project;
   the resume note tracks unfinished work; logs preserve significant history.
2. **Decisions only get added to.** Supersede, never rewrite.
3. **Docs change in the same commit as behavior.**
4. **Don't duplicate.** Link to the one place a fact lives. Duplicated facts drift apart,
   and then the agent picks the wrong one.
5. **Verify current facts.** A dated header helps locate stale information; checking
   the actual system establishes whether it is still true.
6. **Anything that only grows gets an index.** Decisions and session logs are never read
   front to back. The index line is written in the same change as the thing it indexes.
7. **You are the authority.** Documents inform. They don't overrule.
8. **Write for the reader who wasn't there.** No "as discussed." No pointing at a
   conversation. No "it" without saying what "it" is.

---

## When it goes wrong

| What you'll notice | What actually happened | Fix |
|---|---|---|
| The briefing is hundreds of lines long | History leaked into the snapshot | Move it to a session log or a decision record. Past ~150 lines, do that before anything else. |
| Nobody can find the session log about the thing that broke | Logs were written but never indexed | One line in `docs/logs/README.md`, written in the same change as the log. |
| The agent reads forty decisions to check one | `DECISIONS.md` has no index | Add the index table. Read it first, open one record. |
| The agent enforces a rule you never agreed to | Someone's passing observation in a notes file turned into a law | Add the precedence list. State that documents are input. |
| You're having the same debate twice | The decision was never recorded, or recorded without what you rejected | Write the record, including what lost. |
| A deliberate choice gets "fixed" | No decision record, or one without consequences | Decision records with a Consequences section. |
| The docs describe a system that doesn't exist | Ideas got written into `ARCHITECTURE.md` | Ideas live in specs and decision records until they're real. |
| Small requests keep disappearing | No `UPDATES.md`, so they only ever existed in chat | Write them down the moment they're said. |

---

## Get started

```
your-project/
├── AGENTS.md                    ← the briefing and project preferences
├── CLAUDE.md, GEMINI.md         ← pointers that load AGENTS.md + COFOUNDER.md
├── COFOUNDER.md                 ← how the agent behaves
├── README.md                    ← for humans showing up cold
├── .gitignore
├── .claude/                     ← optional: Claude Code slash commands + guard hook
└── docs/
    ├── RESUME.md                ← where to pick up unfinished work
    ├── workflows/               ← kickoff, Git, and quality procedures
    ├── SPEC.md
    ├── ARCHITECTURE.md
    ├── DECISIONS.md
    ├── INFRA.md
    ├── BACKLOG.md
    ├── UPDATES.md
    ├── HELP-ARTICLES.md
    ├── specs/                   ← SPEC-TEMPLATE.md, PLAN-TEMPLATE.md, and an index
    ├── plans/                   ← a README explaining when to use it
    └── logs/                    ← the session-log template, and an index
```

You don't fill any of this in by hand. Don't even open the files. Make a new folder, open
your coding agent in it, and say one sentence.

If the folder is empty:

> Get the Cofounder template from this repo, copy it in here, and let's get started.

If you already dropped the template in:

> Let's get started.

That's the whole onboarding. The agent sees the unfilled briefing, knows it's the first
session, and runs the kickoff. It asks you a few questions at a time, fills in the
briefing, writes the first decision record, and reads the whole thing back to you in plain
English so you can tell it what's wrong.

The first session leaves a shared briefing, confirmed preferences, and a next step.
Your agent can then say, "We can test this with less. Here is how. Your call."

Then go bring your idea to life.

Do this on day one if you can. You can add it to a project that's already running and it
will clean things up, but the context that's already lost is lost. Nobody remembers why
that decision got made in week three, and the agent certainly doesn't.

For an existing project, say:

> Adopt Cofounder in this project. Preserve my existing files and settings, merge the
> useful instructions, and confirm this project's working preferences.

**If you're an agent reading this:** follow `template/docs/workflows/KICKOFF.md`.
Copy the template into an empty root, including hidden files. For an existing project,
merge deliberately; never overwrite current docs or settings with template stubs.

---

## Making it yours

Not every project needs all of it.

- **Small or short-lived:** keep the working agreement, briefing, resume note, and
  decision record. Leave other docs as stubs until needed.
- **No infrastructure:** keep `INFRA.md` and say so. "No infrastructure, on purpose" is a
  useful thing for an agent to read.
- **No users yet:** drop `HELP-ARTICLES.md` until there's a help surface.
- **Solo and moving fast:** stay in one folder; use a short feature spec and a plan only
  when it helps.
- **Several agents at once:** follow `docs/workflows/GIT.md` for separate worktrees,
  task handoffs, and one integration owner.

What you should never drop: the **briefing**, **`COFOUNDER.md`**, the **decision record**,
the **resume note**, and the **intent-versus-reality distinction**.

It all comes down to one thing: you're giving your agent what a cofounder actually brings.
A memory, a structure to keep it in, and opinions about how to build.

---

## Checking the harness

The optional Git guard has automated tests. From this repository's root:

```sh
python3 -m unittest discover -s tests -v
```

[VALIDATION.md](VALIDATION.md) defines realistic scenarios for fresh Claude Code and
Codex sessions, including single-agent work, concurrent agents, interrupted work, and
existing-project adoption. Hook tests do not prove those agent behaviors; record live
results separately. [CHANGELOG.md](CHANGELOG.md) highlights meaningful improvements in
plain language. Small corrections stay in Git history; they do not each need an entry.

---

## Why I made this

Every new project starts the same way. An empty folder.

You open your agent in it and there's nothing there. No plan. No idea what you're
building, who it's for, or what you already know about it. You start from zero and so does
it, and the first hour goes into explaining a thing that only exists in your head.

Then, once you're moving, it forgets. One session it knows exactly what we're building and
why. Close the window, open a new one, and it doesn't remember why we rejected the obvious
approach, what broke last time, or which decisions I'd rather die than reopen. So it
"fixes" things that weren't broken and re-argues things we settled weeks ago.

Worse than forgetting, it fills the gap. It'll confidently describe a decision we never
made, or a reason I never gave, and build on top of it.

And even when it remembers, it builds the wrong thing. Not broken. Wrong. It doesn't ask
what this is for, or who it's for, or whether the feature I just asked for is worth
building at all. It builds for a million users when I have four. It hands me a technical
decision I'm not equipped to make, I pick one, and a couple of weeks later I find out what
that pick cost. A very capable, very agreeable agent will help you drive straight off a
cliff.

A cofounder doesn't do that. A cofounder says "I think this is a mistake."

None of that cost me much money. It cost me time and sanity. Weeks of building the wrong
thing well, and the frustration of finding out late.

So I started telling it to keep track. Write this down. Remember that we decided this.
And slowly, without either of us planning it, it built its own little system. Four months
into one project I looked up and realized the structure was actually good, and that the
project was still sharp, months in, while my others had gone foggy.

Then I started something new, and hit the empty folder again. So I asked it: how did you
do this on the other one? And it drew me the diagram. Here are the files. Here's what each
one holds. Here's what I read before I touch anything.

So I said: package that up.

That's this template.

I made it for myself first, so I'd never cold-start again. Then I kept sharpening it,
because remembering wasn't enough. I wanted it opinionated. Ask the right questions before
building. Push back when I'm wrong. Make the technical calls so I don't have to. Don't
build for scale I haven't earned yet. I might still be proving the thing is worth
building at all.

So that all I have to do is focus on the product. What I'm building, and who it's for.

There's nothing about me or my projects in it. Copy it, fill it in, and it's yours.

---

## About the creator

I'm not an engineer. I've spent twenty-five years in software as a designer, a UX person, a
product lead, and a founder. The guy who can see the whole thing in his head and can't
build a line of it.

I co-founded Kajabi. It started as three of us with an idea and some mockups, no investors
and no Silicon Valley money. It became a $2 billion company, and the creators on it have earned
over $10 billion selling what they know.

I didn't write any of that code.

That's the thing about being the product person. You need a technical partner,
and they're rare, they're expensive, they want equity, and even when you find one, the two
of you working well together is luck. I've spent my whole career dependent on that search.

Then agents got good enough that I could build things myself, for about a week, until the
agent forgot everything, agreed with everything I said, and started asking me to make the
technical decisions I'd spent a career not having to make.

Cofounder is how I closed that gap. It's the partner I always wished for: knows the
project, has opinions, tells me when I'm wrong, and never needs the story re-explained.

Twenty-five years of needing someone else to build it. Now I just describe what I want and
watch it get made. I've stopped pretending that isn't a little bit magic.
