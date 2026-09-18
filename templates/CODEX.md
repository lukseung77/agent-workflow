# [Project Name] — Codex Instructions

Follow the canonical startup order in `<workflow-root>/workflow/rule-precedence.md`, where `<workflow-root>` is usually `../agent-workflow` or `./agent-workflow`.

This file covers only what is specific to Codex.

---

## Assignment

- Role: **[lead | consultant]**
- Collaboration file: `docs/collaboration-codex.md`
- Queue command: `python3 <workflow-root>/scripts/collab_queue.py codex`
- Source-of-truth inventory: `agent-workflow-local/project-facts.md`

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

All accepted product decisions live in the files listed in `agent-workflow-local/project-facts.md`.

## Key Constraints

- [List any project-specific rules or guardrails here]

## Tool Adapters

Read `<workflow-root>/workflow/agent-tooling.md` when exploring repository structure, implementing code, validating changes, or running verbose commands. Host-specific Graphify, Ponytail, and RTK adapters are optional and must not override OpenSpec or project requirements.
