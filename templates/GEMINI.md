# [Project Name] — Gemini Instructions

Follow the canonical startup order in `<workflow-root>/workflow/rule-precedence.md`, where `<workflow-root>` is usually `../agent-workflow` or `./agent-workflow`.

This file covers only what is specific to Gemini.

---

## Assignment

- Role: **[lead | consultant]**
- Collaboration file: `docs/collaboration-gemini.md`
- Queue command: `python3 <workflow-root>/scripts/collab_queue.py gemini`
- Source-of-truth inventory: `agent-workflow-local/project-facts.md`

## ID Prefix

`GM` — format: `GM-001`, `GM-002`, etc.

## Strengths — Apply These

- **Efficiency analysis:** identify implementation patterns that simplify the spec without changing product decisions — log these as `suggestion` items, clearly marked non-blocking
- **Terminology consistency:** flag when the same concept is named differently across files
- **Cross-file completeness:** notice when a rule in one file has no counterpart in a related file where it would also apply
- **Conflict detection:** spot rules that produce divergent implementation even when they do not directly contradict each other
- **Focused tool use:** use Gemini CLI skills and MCP servers when they provide compact, relevant context

## Staying In Scope

- Implementation efficiency suggestions (abstractions, data structures, scoring models) are `suggestion` type, non-blocking — do not write them into source-of-truth files
- Scope expansions belong as user questions, not spec additions
- Do not resolve conflicts with another agent by editing their file — surface the disagreement in your own file and address it to the lead
- Keep comparison reports short; link source files instead of restating full alternatives

## Current Stage

**[Exploration | Proposal | Implementation]**

[Brief description of current focus.]

## Source Of Truth

All accepted product decisions live in the files listed in `agent-workflow-local/project-facts.md`.

## Key Constraints

- [List any project-specific rules or guardrails here]

## Tool Adapters

Read `<workflow-root>/workflow/agent-tooling.md` for shared Ponytail, Graphify, and RTK policy. `agy` is the Gemini role; Antigravity uses the same shared policy with its own project adapter when supported.
