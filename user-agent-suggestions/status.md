# User-Agent Suggestion Status

The master-agent owns this ledger. User-agents may read this file to check the status of submitted suggestions, but must not edit it.

See `workflow/master-governance.md` for submission, evaluation, approval, implementation, and rollback rules.

## Status Values

- `proposed`
- `under-review`
- `pending`
- `accepted`
- `partially-accepted`
- `denied`
- `implemented`
- `reverted`
- `superseded`

## Ledger

| suggestion_file | status | decision_date | summary | refs |
|-----------------|--------|---------------|---------|------|
| `user-agent-suggestions/submitted/2026-09-08-1418-rideroute-phase-consultant-roles-001.md` | implemented | 2026-09-08 | Accepted in generalized form as optional phase-specific consultant review lenses. | `workflow/role-boundaries.md`; `templates/project-facts.md`; `templates/roles/consultant-agent.md`; `templates/roles/lead-agent.md`; `templates/new-project-setup.md` |
| `user-agent-suggestions/submitted/2026-09-08-1828-rideroute-openspec-phase-skills-002.md` | pending | 2026-09-08 | Evaluation complete; deferred by human decision. Portable capability guidance may be useful but should wait. | evaluated against `workflow/role-boundaries.md`, `workflow/stages.md`, `workflow/review-cycle.md` |
| `user-agent-suggestions/submitted/2026-09-08-1940-rideroute-openspec-phase-skills-clarification-004.md` | implemented | 2026-09-08 | Accepted as a compact capability-first mapping rule; concrete skills, local workflows, and optional packages are examples unless project-local files require them. | `workflow/role-boundaries.md`; `templates/project-facts.md`; `templates/roles/consultant-agent.md` |

Use `refs` for changed files, commit hashes, backup paths, rollback notes, or follow-up detail when needed. Keep rows compact; add a short detail block below the table only when a row would otherwise become hard to scan.

### Intake Awaiting Evaluation

| suggestion_file | status | decision_date | summary | refs |
|-----------------|--------|---------------|---------|------|
| `user-agent-suggestions/submitted/2026-09-08-1831-rideroute-openspec-phase-skills-addendum-003.md` | proposed | none | Registered during consultant reconciliation; no acceptance or supersession decision recorded. Await human-triggered evaluation. | `docs/collaboration-codex.md` CX-003; related suggestion 004 |
