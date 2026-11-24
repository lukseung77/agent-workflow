# Core and Project Templates Handover

The structural update is implemented and locally validated. Both independent
reviews have now been consolidated in CX-026; CX-023 is closed. Continue from
`docs/evaluations/core-project-templates-review-2026-11-24.md` and open follow-up
CX-027. Lifecycle corrections remain unapplied. The changes are uncommitted and
unpublished; the implementation inventory and original validation below remain
the handover baseline.

## Session and Ownership

- Date: 2026-11-24
- Session: `codex-2026-11-24-project-templates`
- Branch: `codex/template-guidance-refactor`
- Base HEAD: `80428a9b940f1896e88ab3e8898b43def8c5fdc5`
- Current stage: Implementation; no stage transition was performed.
- Lead: Codex; owns integration and source-of-truth updates.
- Consultants: Claude checks authority/rule consistency; Gemini checks
  architecture, context efficiency, and feasibility.
- Product source: `agent-workflow-foundation/`.
- Accepted requirements: `openspec/specs/foundation-consumers/spec.md`.
- Local authority and inventory: `agent-workflow-local/project-facts.md`,
  `rules.md`, and `maintainer-governance.md`.

## Confirmed Design

The user requested evaluation and clarification before implementation. Decisions
are recorded verbatim in CX-021 in `docs/collaboration-codex.md` and reflected in
accepted requirements. Do not reopen these decisions without new evidence:

1. The core handles communication between agents and the user, including questions,
   decisions, reviews, queues, and handoffs. Grill-Me is a core capability, including
   its separately installed grilling dependency.
2. Project types may contain one or more templates. Setup asks for the type and
   then the template, reusing explicit user answers.
3. Templates own processes, stages, review gates, and integration requirements.
   The core imposes no universal software-development lifecycle.
4. The initial SW Development template uses OpenSpec as the overall development
   process and GitHub for the repository. Additional capabilities depend on the
   actual project.
5. The initial Proposal PT Making template covers RFP analysis through final deck
   review. MarkItDown reads the RFP and supporting data. ChatGPT handles analysis,
   TOC, and per-slide planning; Claude's PowerPoint plugin produces the slides.
6. Proposal PT handoffs between ChatGPT and Claude are manual. Slide plans include
   titles, key messages, contents, and drawing/layout prompts.
7. Setup guides installation. Template selection records requirements and does
   not itself install, authenticate, configure host plugins, or publish anything.

## Implementation Map

| Concern | Main files under the foundation |
|---|---|
| Core/template boundary | `workflow/project-templates.md`, `workflow/agent-workflow.md` |
| Type/template catalog | `templates/project-types.json` |
| Selection resolution | `scripts/project_profiles.py` |
| Installer and template listing | `scripts/foundation.py` |
| Guided setup | `templates/new-project-setup.md` |
| Stage routing and compatibility | `workflow/stages.md`, `workflow/legacy-stages.md` |
| SW workflow and gates | `templates/project-types/sw-development/openspec-github.md`, `stages.md` in that directory |
| Proposal workflow and handoff | `templates/project-types/proposal-pt-making/chatgpt-claude-manual.md`, `slide-handoff.md` in that directory |
| Stage validation and tooling reviews | `scripts/collab_lint.py`, `scripts/tooling_review.py` |

Fresh CLI initialization requires `--project-type` and `--template`; invalid or
missing pairs fail before writes. `foundation.py templates` lists choices.
Defaults are `openspec/` for SW and `proposal/` for Proposal PT, with deliberate
`--source-root` overrides supported. Initialization creates a local
`agent-workflow-local/project-template.json` with the process, stages, requirements,
and handoff mode. Selection and actual capability verification remain separate.

This repository applied the ordinary conflict-free scaffold update. Its existing
source root, stage, consultant lenses, rules, and history were preserved. It is
explicitly `legacy-unselected`; do not silently assign it the new SW template.
Existing consumers retain their prior stage gates through the compatibility
route. SW and existing consumers retain stage-triggered tooling reviews; the
initial Proposal PT template uses explicit manual requests only.

## Validation Already Completed

`python3 -B scripts/validate.py --require-openspec` passed:

- 78 unit tests, including seven additional behavioral tests for this update.
- All three accepted specifications.
- Collaboration lint with zero errors and zero warnings.
- Foundation distribution boundary and self-consumer checks, covering 61 product files.

Both templates also passed an exported-package smoke check: initialization with
a custom foundation directory, strict-state lint, and a no-op update. The final
`git diff --check` and collaboration lint passed after operational records changed.
These are prior-session results; rerun affected checks after substantive edits.

## Next Actions and Open Questions

1. Follow startup through `workflow/rule-precedence.md`, then inspect CX-023:

   ```sh
   python3 -B agent-workflow-foundation/scripts/collab_queue.py codex --startup
   python3 -B agent-workflow-foundation/scripts/collab_queue.py codex --id CX-023
   python3 -B agent-workflow-foundation/scripts/collab_queue.py codex --refs CX-023
   ```

2. Claude CL-012 and Gemini GM-005 are complete. Their findings are dispositioned
   in CX-026 and the linked consolidation. Address CX-027's lifecycle corrections
   before broad rule-file refactoring; settle dependent product choices first.
   Closing the review does not mean those corrections are implemented.
3. The exact Claude PowerPoint plugin remains unidentified and unverified. Keep
   this as a guided project-setup prerequisite before slide production; planning
   can proceed independently. Do not invent a plugin name or claim a live test.
4. If product files change, review/apply the self-consumer lifecycle update before
   final validation, then run the relevant checks:

   ```sh
   python3 -B agent-workflow-foundation/scripts/foundation.py update --project . --source agent-workflow-foundation
   python3 -B agent-workflow-foundation/scripts/foundation.py update --project . --source agent-workflow-foundation --apply
   python3 -B scripts/validate.py --require-openspec
   git diff --check
   ```

5. Preserve the working tree. This update has no commit or remote publication;
   do not treat the earlier publication task's authority as an instruction to
   publish this new update. Use the current user direction for publication scope.

The startup queue also contains older Claude CL-010/CL-011 items. Their lead
reconciliation is already recorded in CX-019; do not confuse them with new CX-023
responses or reopen their resolved design merely because author-owned items remain open.

## Evidence and Review Snapshot

- Evaluation and rollback guidance: `docs/evaluations/core-project-templates-2026-11-24.md`.
- Change record: `docs/change-log.md`, entry dated 2026-11-24.
- Decisions: CX-021; implementation evidence: CX-022; pending review: CX-023.
- Review snapshot SHA-256:
  `6c6f7b8f7d9d3aa9e403192845a7fffdbf37fb299384c95bcb65ae241aa14d85`.
  CX-023 specifies component-wise Python Path sorting. Lexical string sorting of
  the same content gives `489e7d7f63d3e7ceea392d987bc1534204a42c1aa14a05d610875cf13b476d6f`.
  CX-026 independently reproduced both hashes; no source drift was demonstrated.

## Files Changed in the Structural Update

Paths below capture the complete modified/untracked file inventory at handover
preparation, excluding this new note. Read the working tree rather than HEAD.

- `README.md`
- `agent-workflow-foundation/README.md`
- `agent-workflow-foundation/guides/tooling-operations.md`
- `agent-workflow-foundation/scripts/agent_workflow_env.py`
- `agent-workflow-foundation/scripts/collab_lint.py`
- `agent-workflow-foundation/scripts/foundation.py`
- `agent-workflow-foundation/scripts/tooling_review.py`
- `agent-workflow-foundation/templates/agent-workflow-local/project-facts.md`
- `agent-workflow-foundation/templates/new-project-setup.md`
- `agent-workflow-foundation/third-party/origins.json`
- `agent-workflow-foundation/workflow/agent-workflow.md`
- `agent-workflow-foundation/workflow/foundation-lifecycle.md`
- `agent-workflow-foundation/workflow/grill-me.md`
- `agent-workflow-foundation/workflow/local-project-files.md`
- `agent-workflow-foundation/workflow/question-model.md`
- `agent-workflow-foundation/workflow/review-cycle.md`
- `agent-workflow-foundation/workflow/role-boundaries.md`
- `agent-workflow-foundation/workflow/rule-precedence.md`
- `agent-workflow-foundation/workflow/stages.md`
- `agent-workflow-foundation/workflow/tooling-review.md`
- `agent-workflow-foundation/workflow/tooling.md`
- `agent-workflow-local/current-state.md`
- `agent-workflow-local/foundation-state.json`
- `agent-workflow-local/project-facts.md`
- `docs/change-log.md`
- `docs/collaboration-codex.md`
- `openspec/specs/foundation-consumers/spec.md`
- `tests/test_foundation.py`
- `tests/test_tooling_review.py`
- `agent-workflow-foundation/scripts/project_profiles.py`
- `agent-workflow-foundation/templates/project-types.json`
- `agent-workflow-foundation/templates/project-types/proposal-pt-making/chatgpt-claude-manual.md`
- `agent-workflow-foundation/templates/project-types/proposal-pt-making/slide-handoff.md`
- `agent-workflow-foundation/templates/project-types/sw-development/openspec-github.md`
- `agent-workflow-foundation/templates/project-types/sw-development/stages.md`
- `agent-workflow-foundation/workflow/legacy-stages.md`
- `agent-workflow-foundation/workflow/project-templates.md`
- `agent-workflow-local/project-template.json`
- `docs/evaluations/core-project-templates-2026-11-24.md`
