# Change Log

The master-agent records canonical `agent-workflow` updates here when they are not already fully tracked in `user-agent-suggestions/status.md`.

Keep entries compact. Use this file for rollback orientation and downstream update notes, not detailed design discussion.

## 2026-09-08 - Master Governance And Context Refactor

- `request`: human-requested canonical governance update and context-efficiency cleanup
- `summary`: added master-agent governance, one-file-per-suggestion intake, compact suggestion status ledger, downstream vendored workflow-root support, and lower-context startup orientation
- `backup`: `/private/tmp/agent-workflow-backup-20260908-135043.tgz`
- `changed`: `workflow/master-governance.md`, `workflow/rule-precedence.md`, `workflow/role-boundaries.md`, `workflow/context-management.md`, `workflow/collaboration-format.md`, `README.md`, `skills/multi-agent-coworking/SKILL.md`, setup templates, `user-agent-suggestions/`, `docs/external-lead-suggestions.md`, `docs/legacy/external-lead-suggestions.md`
- `downstream note`: downstream agents may customize local `agent-workflow/` copies but submit reusable upstream changes only through `user-agent-suggestions/submitted/` when explicitly asked by the human user
- `rollback`: restore from the backup archive or revert the commit that includes this entry
