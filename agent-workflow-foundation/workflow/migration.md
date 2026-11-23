# Existing-Project Migration

Legacy compatibility is limited to existing projects. New projects use only
`templates/new-project-setup.md`. An absent installation state alone does not
identify legacy: look for old workflow pointers, shared overrides, role files,
or wrapper/index files before choosing this procedure.

## Existing Layout And Authority

Older projects may use a sibling/vendored `agent-workflow/` root, a
`docs/collaboration.md` bootstrap, `agent-common.md`/`CODEX.md` wrappers,
`agent-workflow-local/agent-workflow.md` shared overrides, per-agent role text,
and persistent indexes. Before migration, retain the old project's precedence
and role assignments; do not silently apply new defaults over its overrides.
Old shared overrides remain authoritative until reconciled into `rules.md`.
Use live collaboration files as the evidence source; old indexes are only aids.
The current product does not maintain the old root layout or unused wrappers.

## Plan And Mechanical Migration

The existing project's lead performs migration on the human's request. Preserve
a backup or version-control snapshot and note the old workflow root/revision.
Do not automatically stash unrelated work or modify a sibling source repository.
Choose the actual roster, lead, source-of-truth root, and foundation source.

```sh
python3 <foundation-root>/scripts/foundation.py migrate --project . --source SOURCE --project-name NAME --agents ROSTER --lead LEAD
```

This is read-only. Inspect its legacy inventory, exact pointer changes, and manual
review list. Reuse this command with `--apply` for the reviewed mechanical plan.
It installs missing current files through ordinary init, preserves existing
configuration/history, backs up affected old files in local migration metadata,
removes narrowly identified old host pointer lines, and carries shared overrides
verbatim into local rules. It writes `agent-workflow-local/migration.json` and
is idempotent after that receipt. It never deletes old files or vendored trees.
Existing managed startup blocks require normal lifecycle adoption/review rather
than forced replacement. There is no online tooling-review trigger here.

## Lead Semantic Review And Completion

1. Check project facts: retain or explicitly reconcile lead, consultants, review
   lenses, paths, and source-of-truth ownership. Move old role declarations out
   of per-agent files; keep those files only for actual additional restrictions.
   The helper does not infer authority from arbitrary prose.
2. Reconcile carried shared overrides using the rule/reason/replacement format
   in `workflow/local-project-files.md`. Archive the old shared file only after
   confirming all restrictions are active in `rules.md`.
3. Inspect host text and tooling adapters for remaining old paths. Regenerate a
   selected managed tooling pointer with the environment tool only when needed;
   preserve custom instructions and host settings.
4. Run strict collaboration lint and queues for each participating agent and
   user, plus an archived-item lookup when archives exist. Confirm current stage,
   accepted decisions, reference hashes, tools, and message IDs are preserved.
5. Archive only reviewed obsolete wrappers/indexes after checking for unique
   project content. Remove a vendored old workflow copy only after confirming
   ownership, no remaining references, and a recoverable backup. Never remove a
   shared sibling repository as part of a consumer migration.
6. Record old root/revision, new fingerprint, preserved/archived files, checks,
   remaining manual actions, and rollback in the lead's own collaboration file.
   Mechanical application is not semantic migration completion. Prefer one
   reviewed migration commit; publication remains separately authorized.

## First Update And Rollback

Init records incoming template bases while preserving existing local content as
customization. This prevents an update from mistaking local content for an old
upstream template and replacing it. Review the first update carefully; overlapping
customizations require normal reconciliation. Do not replace template bases with
arbitrary local files. Roll back through the migration snapshot/commit or reviewed
backups, preserving work created afterward. Keep evidence until verified.
