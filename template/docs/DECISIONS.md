# <Project> Architecture Decision Records

Append-only. A decision in here is load-bearing: to change it, add a new ADR that
supersedes the old one. Never quietly rewrite history. The point of this file is to stop a
future session from "fixing" something that was a deliberate choice.

**Read the index first.** This file only grows. The index is what keeps it usable at forty
decisions: it tells you which ones are still live, so you open one record instead of
reading the whole file.

**Superseding a decision is two edits.** Write the new ADR, mark the old record
`Superseded by ADR-NNN`, and update both rows in the index. A superseded record stays
exactly where it is, unchanged.

## Index

| ADR | Decision | Status |
|---|---|---|
| 001 | <Short imperative title> | Accepted |

---

## ADR-001: <Short imperative title>

**Date:** <YYYY-MM-DD>
**Status:** Accepted

### Context
<What was true that forced a choice.>

### Decision
<What we chose. Present tense, unambiguous.>

### Alternatives rejected
<What else was on the table and why it lost. This is what stops the same
debate happening again in four months.>

### Consequences
<What we now accept, including the bad parts.>

---

## ADR template

### ADR-NNN: Title

**Date:** YYYY-MM-DD
**Status:** Proposed | Accepted | Superseded by ADR-NNN

#### Context
#### Decision
#### Alternatives rejected
#### Consequences
