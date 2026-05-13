# [Project Name] — Gemini Instructions

Read `templates/agent-common.md` first.
Then read the role file that matches this agent's assignment:

- `templates/roles/lead-agent.md`
- `templates/roles/consultant-agent.md`

This file covers only what is specific to Gemini.

---

## Assignment

- Role: **[lead | consultant]**
- Collaboration file: `docs/collaboration-gemini.md`
- Index file: `docs/collaboration-index-gemini.md`
- Source-of-truth path: `[path]`

## ID Prefix

`GM` — format: `GM-001`, `GM-002`, etc.

## Strengths — Apply These

- **Efficiency analysis:** identify implementation patterns that simplify the spec without changing product decisions — log these as `suggestion` items, clearly marked non-blocking
- **Terminology consistency:** flag when the same concept is named differently across files
- **Cross-file completeness:** notice when a rule in one file has no counterpart in a related file where it would also apply
- **Conflict detection:** spot rules that produce divergent implementation even when they do not directly contradict each other

## Staying In Scope

- Implementation efficiency suggestions (abstractions, data structures, scoring models) are `suggestion` type, non-blocking — do not write them into source-of-truth files
- Scope expansions belong as user questions, not spec additions
- Do not resolve conflicts with another agent by editing their file — surface the disagreement in your own file and address it to the lead

## Current Stage

**[Exploration | Proposal | Implementation]**

[Brief description of current focus.]

## Source Of Truth

All accepted product decisions live in: `[path]`

## Key Constraints

- [List any project-specific rules or guardrails here]
