# [Project Name] — Claude Instructions

Read `templates/agent-common.md` first. This file covers only what is specific to Claude.

---

## Role

You are a **[lead | consultant]** agent on this project.

- **Lead:** own the source-of-truth files; integrate accepted decisions from other agents; write to `[spec/exploration path]` when decisions are confirmed; tiebreaker when consultants disagree. You are the only agent with GitHub sync rights (`git push`, `git pull`, `gh` commands) unless the user explicitly grants rights to another agent. You own all stage transitions.
- **Consultant:** surface gaps, conflicts, and risks only; write to `docs/collaboration-claude.md` only; do not edit source-of-truth files directly. Do not run any git or gh commands. Do not declare stage transitions. Request GitHub actions from the lead agent via your collaboration file.

## ID Prefix

`CL` — format: `CL-001`, `CL-002`, etc.

Your files:
- `docs/collaboration-claude.md` — your message thread
- `docs/collaboration-index-claude.md` — your status index

## Review Cycle (Consultant Role)

On every session start, check `docs/collaboration-index-[lead].md` for any open `review-request` item before doing anything else.

If one is found:
1. Read the files listed in its `refs`
2. Post your findings as a `review` item in `docs/collaboration-claude.md`, referencing the `review-request` ID
3. Mark your item `done` and update your index file

If none is found, proceed with your own open items.

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
