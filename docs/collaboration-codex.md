# Codex Collaboration

### [CX-013] Foundation Product And Self-Consumer Restructure
- `date`: 2026-11-19
- `session_id`: codex-2026-11-19-agent-workflow-foundation-restructure
- `from`: codex
- `to`: all
- `type`: status
- `status`: done
- `scope`: foundation distribution, shared local scaffold, this consuming instance, third-party origins, update lifecycle, and GitHub sync
- `why`: The human defined agent-workflow-foundation as the delivered product, required this repository to consume its own scaffold, and requested restructuring and GitHub sync.
- `refs`: agent-workflow-foundation/foundation.json, agent-workflow-foundation/workflow/foundation-lifecycle.md, agent-workflow-local/project-facts.md, openspec/specs/foundation-consumers/spec.md, openspec/changes/archive/2026-11-19-separate-foundation-and-consumer/, docs/change-log.md

Implemented the discussed product/instance boundary. Reusable rules, templates,
first-party scripts/skill, operations guidance, and third-party origins live in
the foundation. Maintainer rules, collaboration history, specs, tests, and this
project's own customized instance remain outside its package. General reviews and
rule changes target foundation source; local customizations are not promoted by
default. The previous scaffold deferral is superseded by the human's explicit
request to implement the self-consuming structure.

One lifecycle tool initializes both this repository and independent consumers,
records sources/content fingerprints, and reviews/applies updates. Template bases
support three-way merging; conflicts block all planned writes. Product-file
customizations and modified deletions require explicit reconciliation. A manifest
and export command prevent copying the source project's populated state/history.

The third-party catalog contains official origins, packages, and verification
guidance rather than implementations. Current supported installers resolve stable
packages/tags and retain compatibility selectors. Verified origins/version output
are recorded in each consumer's inventory; unverified plugins stay unknown.

Evidence: 59 tests passed; collaboration lint had zero errors/warnings; both main
specs and this change validated before archival; its requirements are now promoted
to the third main spec. Self-consumer/boundary validation covers 47 product
files. This instance was created and updated using the shared tool, retaining its
maintainer customizations. An exported package initialized a separate consumer,
passed lint, produced an empty update plan, and preserved its existing file.
Package: `/private/tmp/foundation-release-check-8mebzxwe/agent-workflow-foundation.zip`.
No remote source clone or real third-party/host installation was exercised; CI
has not yet executed remotely. The optional skill validator remains unavailable
without PyYAML; the first-party skill's unchanged metadata and moved references
were inspected. No dependency was installed to validate that routing edit.

Rollback snapshot: `/private/tmp/agent-workflow-before-foundation-r1e1p2b6.tgz`.
Existing review archives and older suggestion decisions are preserved. The human
authorized commit/push after validation; remote sync is reported in the final reply.

## Resolved History

Resolved items are preserved in [numbered archives](collaboration-archives/).
Retrieve any item with `python3 scripts/collab_queue.py codex --id ITEM-ID`.
