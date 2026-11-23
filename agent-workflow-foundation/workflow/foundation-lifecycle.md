# Foundation Lifecycle

The foundation is the reusable product: rules, templates, first-party scripts
and skills, and a third-party origin registry. Its consuming project has a
separate `agent-workflow-local/`, host entry files, and collaboration history.
The foundation's own repository uses the same installation and update process.

## Setup In The Chosen Project Folder

Keep the directory selected by the user as the project root. Obtain a local
foundation or its repository URL; a fresh agent needs that source location or
an installed entry skill to discover the product. A repository source exports
only its `agent-workflow-foundation/` child, never its project state or history.

Follow `templates/new-project-setup.md` for the single initialization command
and guided setup.

SOURCE can be a foundation directory, its containing repository, or an explicit
HTTPS/SSH Git URL. Local paths copy actual working-tree contents, including unpublished
product changes; Git URLs retrieve committed content. The content fingerprint in
local installation state identifies what was installed. No remote project
repository, third-party installation, or host plugin is created by this command.

Initialization copies the foundation, instantiates its local templates, adds
managed startup blocks to participating host files, and creates missing empty
collaboration files. It preserves existing local configuration, host text, and
collaboration history. Repeating init is a no-op; use update for new defaults.

For the foundation repository itself, SOURCE and the installed foundation path
can be the same directory. This registers the product in place and instantiates
the same templates used by every other consumer.

## Customization And Updates

Customize project facts, local rules, state, and optional agent restrictions.
General rule changes belong in the foundation source; instance-specific changes
do not automatically become product defaults.

```sh
python3 <foundation-root>/scripts/foundation.py update --project . --source SOURCE
python3 <foundation-root>/scripts/foundation.py update --project . --source SOURCE --apply
```

The first command is read-only review. The second applies a conflict-free plan
under the already authorized update request. It updates unchanged product files
and uses recorded template bases to merge local configuration with new defaults.
Non-overlapping template edits merge using Git when available. Overlapping edits,
locally changed product files, and modified files deleted upstream are conflicts;
no update files are written while any conflict remains. Inspect and reconcile
those paths, or explicitly retain a reviewed deviation with `--keep-local PATH`
using its `foundation/...` or `project/...` plan key. This is not blanket approval
to ignore a behavioral incompatibility.

Installation state records the source, fingerprint, file hashes, and template
bases. Back up the consumer or use its version control before applying an update;
individual writes are atomic, but a multi-file update is not a crash-atomic
transaction. Preserve this metadata for later comparisons. Do not reset project
state or rerun scope interviews just because the foundation was updated.

Review affected behavior, run the consumer's collaboration lint and relevant
checks, and record adopted/deferred changes and rollback information in its own
collaboration history. The foundation repository follows this same process.

## Existing Local Files And Migration

Pre-existing local files are preserved as deliberate customizations. Their merge
base is the incoming template, not the local content: using local content as the
base could overwrite those customizations on a later template update. A migrated
consumer must review its first update, and overlapping template edits may require
manual reconciliation. Existing-layout inventory and mechanical migration are in
`workflow/migration.md`. Third-party lifecycle is owned by `workflow/tooling.md`.
