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
2. Read `agent-workflow-local/current-state.md` as a restart snapshot, not as a task queue.
3. Generate your active recipient queue when `scripts/collab_queue.py` is available.
4. Select one active item and load its details.
5. If the selected item involves external references, check `agent-workflow-local/references/reference.md`.
6. Read only the source-of-truth files referenced by that item or needed for the next action.

Do not act on stale context. Always read the current state of files before writing anything.

---

## Writing Rules

- Write to your own `docs/collaboration-[yourname].md` only, unless you are the lead agent.
- Lead agent additionally writes to source-of-truth files when a decision is confirmed.
- Never write to another agent's collaboration file.
- Never write product decisions into a collaboration file — those belong in source-of-truth files.
- When you edit a source-of-truth file, log the change in your own collaboration file as a `status` item.
- Collaboration files are authoritative. Do not maintain a persistent index when generated queues are enabled.
- `agent-workflow-local/references/reference.md` is operational reference metadata. Any agent may update the row for a reference file it just inspected or converted; the lead agent owns cleanup and conflict resolution.

## Defined Terms

Any term formally defined in the project's domain model is a **defined term**.

Format every reference to a defined term — in any project file — as:

```
<span style="color: #0066cc">**TERM NAME**</span>
```

Rules:
- Always use all capital letters
- Apply the format on every use, not just the first
- Do not invent defined terms — only use this format for terms confirmed in the domain model
- When a new term is confirmed during exploration, add it to the domain model and begin using the format immediately

> **GitHub note:** GitHub strips inline styles so the color will not render there. The all-caps bold convention still visually distinguishes defined terms in plain markdown.

---

## Message Format

Every item in your collaboration file needs:

- A unique ID using your assigned prefix (e.g. `CL-001`, `CX-001`, `GM-001`)
- `type`: `status` | `question` | `gap` | `review` | `suggestion` | `response`
- `status`: `open` | `active` | `done` | `superseded`
- `to`: the target agent name, `all`, or `user`
- A short `why` and `request` (or `decision` and `action` for responses)

See `docs/collaboration-format.md` for the full format.

---

## Asking The User

- Ask the user only when a decision cannot be made by agents alone.
- Ask **one question at a time**. Wait for a response before asking the next.
- Before asking, consolidate all open user questions across all agent files — deduplicate first, then order by impact (highest-blocking first).
- Record the user's answer immediately in your collaboration file with the exact wording of the decision.
- After recording, the lead agent writes the decision into source-of-truth files.

## Context Budget

- Prefer summaries, indexes, and focused files over full historical threads.
- If an external document is large or non-Markdown, check the reference registry first. Use an existing current Markdown conversion when one exists.
- If no current conversion exists and local conversion is appropriate, use MarkItDown and record the source and Markdown hashes in `agent-workflow-local/references/reference.md`.
- Do not paste full converted documents into collaboration files.
- Link source paths so another agent can reopen the material when needed.
- Do not rely on filenames alone for external references; use registry paths and hashes. If a user's file request has multiple plausible matches, list the candidates and ask which file they meant.
- Treat files in `_OLD` as obsolete unless the user explicitly asks for old material. Track them in the registry when practical, but do not read or convert them during normal lookup.
- If context is getting crowded, update `current-state.md` before continuing.

---

## Resolving Items

- When an item is resolved, mark it `done` in your collaboration file.
- Leave history in the authoritative collaboration file until size-based archival.
- If a decision has been written into a source-of-truth file, do not restate it in the collaboration file — link to it.

---

## Review Cycle

The review cycle automates the draft -> review -> consolidate loop.
See `workflow/review-cycle.md` for the full protocol.
Role-specific review duties live in:

- `templates/roles/lead-agent.md`
- `templates/roles/consultant-agent.md`

---

## GitHub Sync

GitHub operations (`git push`, `git pull`, `git commit`, `gh` commands) are the lead agent's default responsibility.

| Role | GitHub rights |
|------|--------------|
| Lead agent | Full — push, pull, commit, create repos, manage branches |
| Consultant agent | None — do not run any git or gh commands |

If you are a consultant agent and something needs to be pushed or a file needs to be committed:

1. Log a request in your collaboration file addressed `to: [lead agent]`
2. Describe exactly what needs to be pushed and why
3. The lead agent decides whether and when to act on it

The only exception is if the user explicitly grants a consultant agent GitHub access for a specific action. That grant must come from the user, not from the lead agent.

---

## Stage Ownership

The lead agent owns the current stage and all transitions between stages.

| Action | Who may do it |
|--------|--------------|
| Declare stage transition (e.g. Exploration → Proposal) | Lead agent only |
| Write to source-of-truth files | Lead agent only |
| Post gate-readiness assessment | Any agent (in own collaboration file) |
| Approve a transition | User (confirms after lead declares readiness) |

Consultant agents may post a readiness assessment in their own collaboration file, but they do not trigger the transition. The lead agent reads all assessments, makes the call, and posts the transition declaration.

---

## Stage Awareness

Always know which stage the project is in:

| Stage | Source of truth | Your job |
|-------|----------------|----------|
| Exploration | Exploration files | Surface gaps, conflicts, open questions |
| Proposal | Spec/proposal files | Review drafts, flag out-of-scope items |
| Implementation | Spec files | Track blockers, flag spec ambiguity |

Do not jump ahead. Do not write proposals during Exploration. Do not change spec scope during Implementation without a mini-proposal cycle.

---

## Anti-Patterns

- Writing to another agent's file
- Consultant agent running git or gh commands
- Resolving a conflict unilaterally without logging it
- Asking the user multiple questions at once
- Writing product decisions into collaboration files instead of source-of-truth
- A consultant agent declaring a stage transition
- Moving to the next stage without explicit lead declaration and user confirmation
- Treating a persistent index as authoritative when generated queues are enabled
- Pasting large raw documents or terminal logs instead of summarizing and linking focused source material
