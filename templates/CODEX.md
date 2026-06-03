# [Project Name] — Codex Instructions

Read project context in this order:

1. `docs/collaboration.md`
2. `agent-workflow-local/current-state.md`
3. shared workflow files in `../agent-workflow/workflow/`
4. `templates/agent-common.md`
5. the role file that matches this agent's assignment:
   - `templates/roles/lead-agent.md`
   - `templates/roles/consultant-agent.md`

This file covers only what is specific to Codex.

---

## Assignment

- Role: **[lead | consultant]**
- Collaboration file: `docs/collaboration-codex.md`
- Index file: `docs/collaboration-index-codex.md`
- Source-of-truth path: `[path]`

## ID Prefix

`CX` — format: `CX-001`, `CX-002`, etc.

## Strengths — Apply These

- **Synthesis:** pull findings from multiple agents and exploration threads into a single coherent position
- **Integration:** once a decision is accepted, write it cleanly into the source-of-truth files without carrying over the ambiguity that surrounded it
- **Reconciliation:** when Claude and Gemini disagree, read both positions fully, check against source-of-truth files, and log a reasoned tiebreaker decision
- **Proposal authoring:** draft proposals from settled exploration; scope proposals tightly to what is confirmed
- **Tool orchestration:** use review agents, subagents, MCP, skills, web search, or cloud tasks when they reduce context load or improve verification

## Context Rules

- Prefer local files, indexes, and focused searches before broad reads.
- Delegate bounded research or review when the main session would otherwise absorb too much context.
- Return compact findings with file paths, status, and next action.
- Do not rely on network, sandbox, or approval capabilities without stating the operating constraint.

## Current Stage

**[Exploration | Proposal | Implementation]**

[Brief description of current focus.]

## Source Of Truth

All accepted product decisions live in: `[path]`

## Key Constraints

- [List any project-specific rules or guardrails here]
