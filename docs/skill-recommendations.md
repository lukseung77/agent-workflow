# Skill Recommendations

This advisory channel identifies areas where a specialized skill, local workflow, or repeatable capability would be beneficial.

It does not require projects to install any skill. User-agents should not edit this file directly; submit upstream suggestions through `user-agent-suggestions/submitted/` when the human user explicitly asks.

## Use

- Record reusable skill opportunity areas.
- Prefer functional capability labels over concrete tool names.
- Keep concrete skills, commands, and project-local workflows in downstream project files unless they are broadly reusable.
- Treat this as planning input, not an active workflow rule.

## Recommended Skill Areas

| Area | Useful capability |
|------|-------------------|
| Suggestion evaluation | Evaluate proposed workflow changes for improvement, conflicts, security, generality, migration, maintenance, and rollback. |
| Workflow consistency audit | Find duplicated rules, stale paths, conflicting authority rules, over-burdening procedures, and misplaced canonical content. |
| OpenSpec phase transition review | Check role assignments, review lenses, source-of-truth files, and stage gates before phase transitions. |
| Acceptance criteria audit | Review proposals for testable Given-When-Then criteria, missing edge cases, undefined states, and unverifiable requirements. |
| Source-of-truth reconciliation | Convert collaboration findings into clean source-of-truth updates without carrying over unresolved discussion. |
| Context efficiency refactor | Identify oversized startup files, repeated policy text, stale history, and candidates for legacy/archive/reference movement. |
| Browser or app verification | Run or guide real app/browser checks for visible UI or interaction changes, complementing automated tests. |
| Security and permission review | Check workflow changes for unsafe command execution, excessive write authority, GitHub authority leaks, prompt-injection risks, and external dependency assumptions. |
| Downstream migration review | Check whether upstream changes affect `../agent-workflow`, `./agent-workflow`, local overrides, templates, or legacy paths. |
| Rollback and change-log review | Verify canonical updates have enough record to explain, revert, or communicate downstream impact. |

## Candidate Backlog

Add candidate skills here after evaluation and human approval.
