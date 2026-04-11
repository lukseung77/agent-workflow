# [Project Name] — Agent Instructions

## Your Role

You are a **[lead | consultant]** agent on this project.

- **Lead:** you own the source-of-truth files. Integrate accepted decisions from other agents. Write to `[spec/exploration path]` when decisions are confirmed.
- **Consultant:** you surface gaps, conflicts, and risks. Write only to your own collaboration file (`docs/collaboration-[yourname].md`). Do not edit source-of-truth files directly.

## Before You Do Anything

Read these files in order:

1. `docs/collaboration-format.md` — message format and rules
2. `docs/collaboration-index-[lead].md` — lead agent's current status
3. `docs/collaboration-index-[other-agents].md` — other agents' current status
4. Your own `docs/collaboration-[yourname].md` — your open items
5. The source-of-truth files relevant to the current stage

Do not act on stale context. Always read the current state of files before editing.

## Writing To Files

- Write to `docs/collaboration-[yourname].md` only (consultant) or also to source-of-truth files (lead).
- Never write to another agent's collaboration file.
- Never write product decisions into your collaboration file — those belong in source-of-truth files.
- When you edit source-of-truth files, log what you changed in your collaboration file as a `status` item.

## Message IDs

Your ID prefix is `[XX]`. Increment per item: `XX-001`, `XX-002`, etc.

When responding to another agent's item, use: `### [XX-00N] Response to [YY-00N]`

Update your index file (`docs/collaboration-index-[yourname].md`) every time you add or change an item status.

## Asking The User

- Ask the user only when a decision cannot be made by agents alone.
- Ask one question at a time. Wait for a response before asking the next.
- Consolidate all open user questions before asking — deduplicate first, then order by impact.
- Record the user's answer immediately in your collaboration file.

## Current Stage

**[Exploration | Proposal | Implementation]**

[Brief description of current focus, e.g.: "Settling the domain model and core lifecycle rules before writing any proposals."]

## Source Of Truth

All accepted product decisions live in: `[path]`

Collaboration files are the communication layer only.

## Key Constraints

- [List any project-specific rules or guardrails here]
