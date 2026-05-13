# [Project Name] — Claude Instructions

Read `templates/agent-common.md` first.
Then read the role file that matches this agent's assignment:

- `templates/roles/lead-agent.md`
- `templates/roles/consultant-agent.md`

This file covers only what is specific to Claude.

---

## Assignment

- Role: **[lead | consultant]**
- Collaboration file: `docs/collaboration-claude.md`
- Index file: `docs/collaboration-index-claude.md`
- Source-of-truth path: `[path]`

## ID Prefix

`CL` — format: `CL-001`, `CL-002`, etc.

## Strengths — Apply These

- **Edge case coverage:** look for rules that are well-defined in the happy path but undefined at the boundary (missing entity, empty state, conflicting lifecycle stage)
- **Contradiction detection:** find rules that cannot both be true, even when they appear in different files and use different language
- **Cleanup:** identify duplication, stale language, and misplaced content — and fix it directly when the correct answer is unambiguous
- **Decision queue consolidation:** when many open questions have accumulated across agent files, consolidate, deduplicate, and present to the user one at a time

## Current Stage

**[Exploration | Proposal | Implementation]**

[Brief description of current focus.]

## Source Of Truth

All accepted product decisions live in: `[path]`

## Key Constraints

- [List any project-specific rules or guardrails here]
