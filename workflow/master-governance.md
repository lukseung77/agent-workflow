# Master Governance

This file defines how the canonical `agent-workflow` project is maintained and how downstream agents may suggest reusable improvements.

## Canonical Startup

Here `<workflow-root>` is this repository. Read this authority file before acting,
then follow `workflow/rule-precedence.md`; skip absent downstream bootstrap and
local files. Consultants also read `docs/consultant-orientation.md` and the
selected request. Find requests with the queue, or retrieve one item by ID.

## Roles

- `master-agent`: the only agent role authorized to update this canonical `agent-workflow` project, including workflow rules, templates, scripts, docs, GitHub state, and suggestion status.
- `user-agent`: an agent working in another project that uses `agent-workflow` as a dependency, local copy, or customized local workflow.
- `human user`: the person operating this single-user PC and making approval decisions for canonical workflow changes.

Project lead agents and consultant agents are project-local roles. They do not become `master-agent` for this canonical repository unless the human user explicitly starts them in that role for this repository.

## Trust Model

This workflow is operated on a trusted single-user PC. The governance rules rely on agents following documented authority boundaries.

The rules are still written as explicit boundaries so every agent can determine what it should and should not touch. If practical enforcement is needed later, use repository permissions, branch protection, or separate checkouts; do not depend on prompt instructions as a technical access-control system.

## Canonical Repository Authority

This repository is the upstream source for reusable `agent-workflow` rules, templates, scripts, and skills.

Only the `master-agent` may:

- edit canonical files in this repository
- change workflow rules, templates, scripts, skills, or README files
- update suggestion statuses or decision records
- update `docs/change-log.md`
- manage GitHub sync for this repository
- accept, deny, implement, revert, or supersede user-agent suggestions

Agents other than the master-agent must not directly modify this repository,
except for the narrow consultant-channel and downstream suggestion-submission
exceptions below.

## Canonical Project Consultant Channel

For this canonical project, Codex is the designated master-agent. Invited
non-Codex consultants receive consultation requests through
`docs/collaboration-codex.md` or an explicit human request and return findings through their
own `docs/collaboration-[agent].md`. Each invited consultant may create that
file if absent and update it thereafter. Paths are relative to this repository:
Claude uses `docs/collaboration-claude.md`; Gemini uses
`docs/collaboration-gemini.md`. Other invited agents use their own stable
lowercase kebab-case agent name, never another agent's identity.

Creating and updating that own collaboration file is the sole project-write exception
for invited consultants. They may not create or edit other files, implement
findings, change suggestion status, or manage GitHub. Codex consolidates reviews
and maintains project files. An explicit human request for consultant assessment
is valid: record its origin, scope, and date in the consultant's own file before
reviewing; return findings there for Codex to reconcile. An invitation or generic
chat alone is not a review request. Without an addressed request or an explicit
human assessment request, prepare your own file, post a question to Codex, and wait.

The generic reference-registry write exception in `workflow/role-boundaries.md`
and `workflow/collaboration-format.md` does not apply in this canonical
repository. This section governs upstream consultant writes; reference-registry
updates and generated files remain master-agent responsibilities.

This project-specific communication exception does not grant upstream write
authority to downstream user-agents. The separately human-triggered downstream
suggestion submission exception below remains applicable to downstream intake;
invited consultants use collaboration files for this project's consultation.

## Downstream Use

A user-agent may use `agent-workflow` in its own project by copying, cloning, or vendoring it into the project, commonly as:

```text
project-root/
├── agent-workflow/
└── agent-workflow-local/
```

The downstream `agent-workflow/` copy is local to that project. User-agents may customize their local copy and `agent-workflow-local/` files for project-specific needs.

Local downstream customization is not an upstream change. Reusable improvements discovered downstream should be submitted as suggestions instead of applied directly to this canonical repository.

## Downstream Suggestions

Submission permissions, statuses, evaluation criteria, approval, and ledger
records live in `workflow/suggestion-intake.md`. Read it only for suggestion
intake work; downstream agents have no other canonical write exception.

## Maintenance Records

For direct human-requested canonical changes, use `docs/change-log.md` for the
summary, changed files, downstream impact, and rollback reference. Detailed
finding dispositions belong in one linked consolidation record; other records
link to it instead of repeating the decisions. Preserve historical records and
OpenSpec requirements, design, and tasks where they serve distinct purposes.
