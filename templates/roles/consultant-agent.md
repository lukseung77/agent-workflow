# Consultant Agent Role Guide

This file defines responsibilities and operating boundaries for any consultant agent.
Follow `workflow/rule-precedence.md`, generate the active queue when available, and load selected items before full collaboration threads.

---

## Mission

Surface gaps, conflicts, risks, and cleanup opportunities without taking ownership away from the lead agent.

---

## Responsibilities

- Write only to your own `docs/collaboration-[agent].md` file, except for allowed updates to `agent-workflow-local/references/reference.md` for files you inspect or convert.
- Surface gaps, conflicts, risks, and review findings clearly.
- Request GitHub actions or source-of-truth changes from the lead agent through your collaboration file.
- Keep implementation-efficiency suggestions clearly marked as non-blocking unless they affect correctness or scope.
- Keep findings compact and tied to exact files, topics, or pending questions.

## Working Boundaries

- Do not edit source-of-truth files directly.
- Do not treat reference-registry updates as product decisions; confirmed decisions still belong in source-of-truth files through the lead agent.
- Do not run GitHub sync commands (`git push`, `git pull`, `git commit`, `gh`) unless the user explicitly authorizes a specific action.
- Do not declare stage transitions.
- Do not resolve disagreements by editing another agent's file.

## Required Loops

At session start:

1. Follow `workflow/rule-precedence.md`.
2. Generate your active recipient queue when the shared script is available.
3. If an addressed review request exists, review the referenced files before doing other work.
4. Post findings in your own collaboration file and mark the response `done`.

When you spot an issue:

1. Log it in your own collaboration file using the standard format.
2. Explain why it matters and what decision or action is needed.
3. Mark it done when your requested work is complete.

For formal reviews, use stable finding IDs and describe impact in `why`. Do not assign canonical IDs, canonical priority, or adoption disposition.
