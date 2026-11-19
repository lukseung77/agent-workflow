# Foundation Repository Maintenance

These are this project's local rules, not rules distributed to consumers.
Use the ordinary foundation startup, project facts, current state, and queues.
Roles and review lenses are assigned only in `project-facts.md`.

## Product And Instance

`agent-workflow-foundation/` is the delivered product source. Reviews, additions,
removals, and general rule changes target that directory by default. Its local
configuration templates live in `templates/agent-workflow-local/` inside the
foundation. This repository's own `agent-workflow-local/` is an instantiated,
customizable consumer; local changes become product defaults only after explicit
generalization. Apply foundation updates using the same lifecycle tool offered
to other projects. Operational records and history stay outside the product.

## Maintainer Authority

The project lead owns product changes, integration, publication, change records,
and suggestion dispositions. Changes require the human's request or approval;
being lead is not authorization for unrelated work. Project consultants write
only their own `docs/collaboration-<agent>.md`. They do not edit product source,
project facts, reference registries, another agent's file, or Git state without
an explicit human exception.

Requests come through the lead's collaboration file or an explicit human
assessment request. Consultants record origin/scope/date in their own response.
The lead reconciles findings and records adopted/deferred outcomes. Stage gates,
combined review/concurrence, and user confirmation follow the shared foundation;
no missing-concurrence waiver has been approved.

## Distribution And Records

Publish/export the foundation directory as the product. The source repository
can retain its own development configuration and history; consumer installation
must copy only the product. Do not publish secrets or machine-specific private
state. The distribution manifest and export tool define the package boundary.

Maintain concise change and rollback records in `docs/change-log.md`, with one
linked detailed consolidation for each update. Preserve archived reviews and
OpenSpec evidence. Downstream suggestion intake is routed to
`docs/suggestion-intake.md`; older suggestion states retain their recorded
human decisions until a new decision is made.
