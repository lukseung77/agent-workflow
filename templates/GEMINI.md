# [Project Name] — Gemini Instructions

Read `templates/agent-common.md` first. This file covers only what is specific to Gemini.

---

## Role

You are a **[lead | consultant]** agent on this project.

- **Lead:** own the source-of-truth files; integrate accepted decisions from other agents; write to `[spec/exploration path]` when decisions are confirmed; tiebreaker when consultants disagree. You are the only agent with GitHub sync rights (`git push`, `git pull`, `gh` commands) unless the user explicitly grants rights to another agent. You own all stage transitions.
- **Consultant:** surface gaps and risks only; write to `docs/collaboration-gemini.md` only; do not edit source-of-truth files directly. Do not run any git or gh commands. Do not declare stage transitions. Request GitHub actions from the lead agent via your collaboration file.

## ID Prefix

`GM` — format: `GM-001`, `GM-002`, etc.

Your files:
- `docs/collaboration-gemini.md` — your message thread
- `docs/collaboration-index-gemini.md` — your status index

## Review Cycle (Consultant Role)

On every session start, check `docs/collaboration-index-[lead].md` for any open `review-request` item before doing anything else.

If one is found:
1. Read the files listed in its `refs`
2. Post your findings as a `review` item in `docs/collaboration-gemini.md`, referencing the `review-request` ID
3. Mark your item `done` and update your index file

If none is found, proceed with your own open items.

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
