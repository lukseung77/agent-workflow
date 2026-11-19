## Context

The repository uses a small Python standard-library toolset and focused Markdown
rules. Retain that structure and address shared behavior instead of adding a
framework or automated controller. Baseline and dispositions live in
`docs/project-evaluation.md`; the human authorized the refactor directly.

## Goals / Non-Goals

Goals: dependable queues, complete archives, truthful diagnostics, consistent
rules/templates, and checks that run locally and in CI.

Non-goals: new stage gates, orchestration, a new message database, changing
consultant permissions, merging branches, or deciding deferred intake proposals.

## Decisions

1. The shared parser hides fenced code and comments, accepts metadata only before
   the body, and ends items at unprotected level 1–3 headings. Raw item text and
   line numbers remain available for archival.
2. Recipient warnings use file-based agent discovery plus explicit allowed names.
   Warnings preserve projects where some agent files have not been created yet.
3. Queue ordering compares aware UTC instants. Legacy dates remain usable.
4. Numbered archives provide completion evidence but never active queue work.
   Archive creation refuses to overwrite an existing path. Single-writer
   governance remains necessary; this is not a concurrent archival transaction.
5. Optional command failures are isolated. Shared-adapter checks do not claim a
   native plugin is installed. Managed blocks refresh without replacing user text.
6. Installation selectors are explicit; no arbitrary upstream version becomes a
   new required default. Existing tools are not reinstalled by version selection.
7. CI and local maintenance share one validator. Missing local OpenSpec is reported
   as skipped; CI requires it. Agent packages and host hooks are never configured.

## Risks / Trade-offs

- Authors who previously relied on metadata bullets in the body must move those
  fields to the header; this prevents accidental lifecycle changes.
- Authors using level 3 body headings must change them to level 4 or deeper.
- The parser supports the documented Markdown subset, not every Markdown dialect.
- Formal reviewer rosters/skips and disposition mapping still need lead review.
- Optional CLI integration tests use fakes; real installation and host integration
  are not exercised by repository validation.

## Migration Plan

Keep paths and commands stable, update authoring templates and canonical guidance
together, and document diagnostic semantics. Validate the repository before
downstream adoption. Roll back by restoring changed files from baseline
`04ea42048d38b50d166b03fad8fd609fc368ba6b`, preserving consultant input and any
user changes; no installation or host-state rollback is required for this refactor.
