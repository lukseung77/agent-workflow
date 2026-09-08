# Agent Collaboration Workflow

A generic, file-based workflow for multiple AI agents working with one human decision-maker.

The workflow keeps durable decisions in project files, collaboration in per-agent threads, and reusable operating rules in focused canonical files.

## Start Here

For normal agent startup, follow:

1. `workflow/rule-precedence.md`
2. `workflow/agent-workflow.md`
3. project-local files under `agent-workflow-local/`
4. the selected collaboration item and its focused source files

Load topic files only when the current task needs them.

## Canonical Rule Map

| Need | File |
|------|------|
| Startup order, rule ownership, conflict precedence | `workflow/rule-precedence.md` |
| Shared operating model | `workflow/agent-workflow.md` |
| Canonical upstream maintenance and suggestions | `workflow/master-governance.md` |
| Local project file placement | `workflow/local-project-files.md` |
| Lead, consultant, user, and master-agent authority | `workflow/role-boundaries.md` |
| Collaboration message schema and queues | `workflow/collaboration-format.md` |
| User questions and decision queues | `workflow/question-model.md` |
| Decision classification and escalation | `workflow/decision-protocol.md` |
| Stage gates | `workflow/stages.md` |
| Reviews and finding consolidation | `workflow/review-cycle.md` |
| Context, restart state, handoff, archives | `workflow/context-management.md` |
| External document conversion | `workflow/markitdown.md` |
| Diagram defaults | `workflow/diagrams.md` |
| Explanatory overview | `workflow/ai-coworking-guide.md` |
| Canonical update history | `docs/change-log.md` |

## Roles

- `master-agent`: maintains this canonical upstream `agent-workflow` repository and evaluates downstream suggestions under `workflow/master-governance.md`.
- `lead agent`: owns project source-of-truth updates, GitHub sync by default, stage readiness, and consultant reconciliation.
- `consultant agent`: reviews, critiques, and suggests through its own collaboration file unless explicitly assigned a narrower downstream action.
- `human user`: resolves product, scope, risk-acceptance, and stage-transition decisions that agents cannot decide from files.

## Project Layout

Downstream projects use one workflow root plus project-local state:

```text
project-root/
├── agent-workflow/                 # optional vendored workflow root
├── agent-workflow-local/           # project facts, rules, overrides, current state
├── docs/                           # collaboration files
└── source-of-truth files           # specs, explorations, proposals, code docs
```

The workflow root may also be a sibling checkout:

```text
shared-workspace/
├── agent-workflow/
└── project-root/
```

Use `<workflow-root>` in commands and templates to mean whichever copy is active, usually `../agent-workflow` or `./agent-workflow`.

## Collaboration

Each agent writes to its own `docs/collaboration-[agent].md`.

Generate active work from collaboration files:

```sh
python3 <workflow-root>/scripts/collab_queue.py <agent>
python3 <workflow-root>/scripts/collab_queue.py <agent> --id ITEM-ID
```

Persistent collaboration indexes are compatibility fallbacks only.

## Upstream Suggestions

User-agents from downstream projects may submit upstream improvement suggestions only when the human user explicitly asks them to.

- Template: `user-agent-suggestions/suggestion-form.md`
- Submission directory: `user-agent-suggestions/submitted/`
- Status ledger: `user-agent-suggestions/status.md`
- Governance: `workflow/master-governance.md`
- Legacy history: `docs/legacy/external-lead-suggestions.md`
- Canonical change log: `docs/change-log.md`

Suggestion files are proposals, not active rules.

## Setup

When creating a new project, start with:

- `templates/project-init.md` for the guided setup flow
- `templates/new-project-setup.md` for the file checklist
- `templates/agent-common.md` plus the relevant `templates/CODEX.md`, `templates/CLAUDE.md`, or `templates/GEMINI.md`

## Tools

- `scripts/collab_queue.py`: compact active queue and item detail
- `scripts/collab_lint.py`: collaboration schema and restart-state validation
- `scripts/collab_archive.py`: threshold-based resolved-item archives

Run validation from a project root:

```sh
python3 <workflow-root>/scripts/collab_lint.py --root . --strict-state
```

## Anti-Patterns

- Duplicating canonical rules in local project files.
- Maintaining manual active indexes when generated queues work.
- Leaving accepted decisions only in collaboration notes.
- Asking the user to decide items agents can classify or resolve from existing files.
- Loading full history before generated queues and focused source files.
