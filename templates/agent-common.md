# Agent Common Rules

This file applies to every agent on the project, regardless of role or tool.
Each agent-specific file references this as the shared foundation.

---

## Core Operating Rules

These rules apply to every agent, on every task:

1. Do not assume. Do not hide confusion. Surface uncertainties and tradeoffs clearly.
2. Write the minimum code that solves the problem. Do not add speculative work.
3. Touch only what is necessary. Clean up only the changes you introduced.
4. Define success criteria before acting. Continue until the result is verified.
5. If information is missing or you would need to make an assumption, verify with the user before proceeding.

---

## How To Read These Templates

Follow `workflow/rule-precedence.md` for the canonical startup order and conflict resolution. Apply this file together with the matching agent-specific and role files; load topic rules only when relevant.

---

## Session Start Checklist

Run this every time you start a session, before doing anything else:

1. Follow the canonical startup order in `workflow/rule-precedence.md`.
2. Generate your active recipient queue when `scripts/collab_queue.py` is available.
3. Select one active item and load its details.
4. Read only the source-of-truth files referenced by that item or needed for the next action.

Do not act on stale context. Always read the current state of files before writing anything.

---

## Writing Rules

- Follow `workflow/role-boundaries.md` for who may write collaboration files, source-of-truth files, reference-registry rows, and GitHub state.
- Follow `workflow/collaboration-format.md` for message schema, lifecycle status, generated queues, and archival behavior.
- Follow `workflow/local-project-files.md` for what belongs in local facts, local rules, current state, and source-of-truth files.

## Message Format

Use `docs/collaboration-format.md` for the project-local roster and `workflow/collaboration-format.md` for the canonical schema.

---

## Asking The User

Use `workflow/question-model.md` for user-facing questions and `workflow/decision-protocol.md` for deciding what must be escalated to the user.

## Context Budget

Use `workflow/context-management.md` for startup context and restart discipline. Use `workflow/markitdown.md` for bulky external references.

---

## Resolving Items

Use `workflow/collaboration-format.md` for item resolution rules and `workflow/review-cycle.md` for review consolidation.

---

## GitHub Sync

Use `workflow/role-boundaries.md` for GitHub ownership and `workflow/stages.md` for stage transitions.

---

## Stage Awareness

Always know the active stage from `agent-workflow-local/current-state.md`; use `workflow/stages.md` for stage gates and stage-specific authority.
