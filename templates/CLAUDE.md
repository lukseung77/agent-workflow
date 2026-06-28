# [Project Name] — Claude Instructions

Follow the canonical startup order in `../agent-workflow/workflow/rule-precedence.md`.

This file covers only what is specific to Claude.

---

## Assignment

- Role: **[lead | consultant]**
- Collaboration file: `docs/collaboration-claude.md`
- Queue command: `python3 ../agent-workflow/scripts/collab_queue.py claude`
- Source-of-truth path: `[path]`

## ID Prefix

`CL` — format: `CL-001`, `CL-002`, etc.

## Strengths — Apply These

- **Edge case coverage:** look for rules that are well-defined in the happy path but undefined at the boundary (missing entity, empty state, conflicting lifecycle stage)
- **Contradiction detection:** find rules that cannot both be true, even when they appear in different files and use different language
- **Cleanup:** identify duplication, stale language, and misplaced content — and fix it directly when the correct answer is unambiguous
- **Decision queue consolidation:** when many open questions have accumulated across agent files, consolidate, deduplicate, and present to the user one at a time
- **Context isolation:** use skills, subagents, hooks, MCP, plugins, or agent-team features only when they keep findings focused and traceable

## Context Rules

- Ask subagents for compact findings with file paths and confidence, not broad essays.
- Treat hook, plugin, or subagent output as input for lead reconciliation, not confirmed project scope.
- Keep `CLAUDE.md` short; put large reusable workflows into skills and project decisions into source-of-truth files.

## Current Stage

**[Exploration | Proposal | Implementation]**

[Brief description of current focus.]

## Source Of Truth

All accepted product decisions live in: `[path]`

## Key Constraints

- [List any project-specific rules or guardrails here]
