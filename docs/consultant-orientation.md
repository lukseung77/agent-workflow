# Consultant Orientation: Canonical Repository Review

## Purpose And Authority

This is the reusable upstream workflow, not a downstream application project.
The human has requested assessment and refactoring to reduce context load and
help agents find and follow all applicable rules. Consultants provide independent
review; Codex is the master-agent and owns repository changes, reconciliation, suggestion
status, and GitHub actions. The human decides suggestion acceptance and stage
transitions under the applicable workflow rules.

`workflow/master-governance.md` governs upstream authority, including this
project's narrow consultant communication exception. Non-Codex agents may create
and update only their own `docs/collaboration-[agent].md`. They must not
create or modify other project files, including another agent's
collaboration file. Reference
registry updates and generated files are not exceptions here.

## File Location And Creation

The collaboration directory is:
`/Volumes/Data/troy/Documents/_lukseung/__Projects/agent-workflow/docs/`
and already exists. Use this project's directory, not a downstream project's
`docs/` directory.

- Claude: `docs/collaboration-claude.md`
- Gemini / `agy`: `docs/collaboration-gemini.md` (use `gemini` in message fields)
- Codex: `docs/collaboration-codex.md` (only Codex may write this file)
- Other invited agents: `docs/collaboration-<agent>.md`, using their own stable
  lowercase kebab-case agent name, never another agent's identity.

If your file is absent, create it with a heading such as
`# Claude Collaboration`, then add messages using
`workflow/collaboration-format.md`. If it exists, preserve its contents and
continue its message ID sequence. Creation of your own file does not require
separate approval or an open review request. Multiple sessions using the same
agent identity share that file and must avoid overwriting each other's work.

## Consultation Channel

1. Read `docs/collaboration-codex.md` for an open `review-request` addressed to
   your agent name or `all`. Use the generated queue if useful.
2. Take scope, lens, and file references from that request. Invitations and
   chat messages are not consultation requests; Codex records requests in its
   collaboration file before consultants act.
3. Post questions, gaps, and findings only in your own
   collaboration file, addressed to `codex` and referencing the request ID.
   Follow `workflow/collaboration-format.md` and `workflow/review-cycle.md`.
4. Mark your completed review response `done`. Do not modify Codex's request;
   Codex handles consolidation and closes it.
5. Receive follow-up requests through the same channel. Chat may acknowledge
   completion with a file/item reference, but must not substitute for the
   consultation record.

If Codex's request file is missing or no addressed open request exists, you may
prepare your own file and post a question to `codex` there, then wait. Do not
create Codex's file or start an unrequested review.

## Focused Reading Order

1. Read `workflow/master-governance.md` for upstream authority.
2. Read `workflow/rule-precedence.md` and `workflow/agent-workflow.md` for startup
   and task routing. Here the workflow root is this repository itself.
3. Read `workflow/role-boundaries.md`, the collaboration format and review cycle,
   then the addressed request and its assigned lens.
4. Inspect `git status --short`, `git diff --stat`, and the relevant diff. Read
   relevant untracked files explicitly: `git diff` does not include them.
5. Follow task-routing links only for the scenario being checked. For template
   consistency, compare the relevant template with its canonical topic file.

Downstream `agent-workflow-local/` and collaboration bootstrap files may be
absent here. Do not create them or mistake their absence for a downstream setup
failure. Do not load legacy history or every rule file by default.

## Current Review Context

The working tree contains changes from several approved requests. Confirm the
actual state with Git; the list below is orientation, not a fixed revision.

- Task-based routing in `workflow/rule-precedence.md` and a shorter operating
  model in `workflow/agent-workflow.md`.
- Placement details moved to `workflow/local-project-files.md`.
- Defined-term rules extracted to `workflow/defined-terms.md`, with pointers
  from collaboration guidance and templates.
- Startup and setup templates adjusted for focused reads and workflow-root paths.
- Capability mapping in `workflow/role-boundaries.md` and optional skill
  opportunity guidance in `docs/skill-recommendations.md`.
- Earlier governance and phase-role checks remain applicable.

Use `docs/change-log.md` for change intent and rollback orientation. Use
`user-agent-suggestions/status.md` only when suggestion history is relevant.
Submitted suggestions are proposals, not rules; this review does not accept,
deny, or change their status. A separate human-triggered evaluation follows
`workflow/master-governance.md`.

## Review Method

Walk representative tasks through their entry points and linked rules. For
each problem, show where an agent would encounter it, what it could do wrong,
and the smallest correction. Assess whether reduced reading retains a reliable
route to required rules. Distinguish measured context reduction from estimates;
word counts alone do not prove agents will remember or obey rules.

Read-only Git inspection and file searches are sufficient for this assignment.
The master-agent owns checks that create caches or generated files. Apart from
your assigned collaboration file, do not alter the working tree; do not reset,
stash, clean, or checkout. Record the
HEAD hash and relevant working-tree state in the report so findings can be
reconciled if files change during review.

If an OpenSpec phase changes during the assignment, re-check your consultant
role and assigned lens before continuing. The master/lead gives the human the
brief role reminder; reviewing does not confer transition authority.

## Response Format

Write a `review` item in your assigned collaboration file, addressed to `codex`,
with the original request ID in `refs`. Begin its body with your assigned lens,
HEAD hash, and files or scenarios reviewed. For `formal: true` requests, use the
canonical finding table in `workflow/collaboration-format.md`.
For each finding, provide:

- Local finding ID, such as `A-01` or `B-01`.
- Exact file and line reference; include both locations for a conflict.
- Observed problem and a concrete trigger or example.
- Impact and whether it blocks the stated refactor objective.
- Suggested minimal correction, with compatibility or maintenance tradeoffs.

Order findings by impact. These are consultant findings; the master-agent
assigns consolidated IDs, final priorities, and dispositions. End with optional
improvements, uncertainties, and checks not performed. Explicitly say when no
findings were found. No minimum finding count is required.

## Reconciliation

The master-agent verifies findings against the current files, consolidates
duplicates, records adoption or rejection with reasons, and applies changes
within the human-authorized scope. Recommendations needing a new human decision
remain proposals until that decision. Consultants do not implement their own
findings in this canonical repository.
