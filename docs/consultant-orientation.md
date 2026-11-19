# Consultant Orientation

This is the canonical upstream repository. Codex maintains project files under
`workflow/master-governance.md`; consultants write only their own collaboration
file. All paths below are relative to this repository, not a downstream project.

## Start And Select Work

1. Read `workflow/master-governance.md`, then the normal startup and task routing
   in `workflow/rule-precedence.md`. Skip absent downstream bootstrap/local files.
2. Find an addressed request with `python3 scripts/collab_queue.py <agent>` and
   read it with `--id ITEM-ID`. Scope, lens, and reviewed content come from that
   request, not from an old refactor description or this onboarding document.
3. An explicit human assessment request is also valid. Record its origin, date,
   scope, and exact user direction in your own file, then return findings there.
   Without either request, prepare your file if needed, ask Codex, and wait.
4. Read the collaboration schema and review cycle, then only the topic rules and
   source files the selected scope needs.

Use your own stable lowercase agent name in `docs/collaboration-<agent>.md`.
Agent-file mappings and the upstream write exception are defined in master
governance. Create the file if absent, preserve existing content, and continue
its ID sequence. Do not edit Codex's request or another consultant's file.

## Review And Respond

Identify HEAD and the actual reviewed working-tree content, including relevant
untracked files; a commit hash alone does not identify uncommitted changes.
Read-only Git inspection and focused searches are normally sufficient. Follow
the assigned scope for checks; report any checks not performed. Do not generate
project files outside your own collaboration file or install dependencies.

Use the format in `workflow/review-cycle.md` and reference the request ID. For a
human-origin request, quote that instruction and identify it as the origin.
Provide exact locations, concrete triggers, evidence and uncertainty, impact,
and the smallest supported correction. Distinguish defects from optional
improvements; no minimum finding count is required. Review independently before
reading other consultants' conclusions when the request calls for independence.

Mark the completed response `done`. Codex reconciles findings, records
implementation and deferred decisions, and closes its own request. Discussion,
reviewer agreement, or elapsed time grants no additional write or stage authority.
