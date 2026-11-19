## Why

Claude CL-005 and Codex's independent review found that collaboration examples
can become false work items, archival can absorb standing notes, and diagnostic
indicators can imply capabilities that were never checked. The human requested
reconciliation followed by a whole-project refactor.

## What Changes

- Share Markdown visibility rules across collaboration parsing and restart lint.
- Separate metadata, item bodies, and standing sections; preserve archival evidence.
- Compare actual timestamp instants and recognize documented agent aliases.
- Improve recipient diagnostics and optional-tool failure handling.
- Keep tooling guidance consistent with the three canonical stages.
- Add explicit install version selectors, accurate diagnostic labels, managed-block
  refresh, regression cases, and a repeatable validation command with CI.
- Label external proposals and record assumption-review decisions and limitations.

## Capabilities

### New Capabilities

- `workflow-integrity`: reliable collaboration discovery, archival, diagnostics,
  and maintenance checks without adding a required runtime dependency.

### Modified Capabilities

- None. Existing optional-tool policy is retained; this change hardens its
  implementation and clarifies diagnostics.

## Impact

Existing entry points, file paths, JSON fields, manual agent activation, and
authority remain compatible. Collaboration authors must keep metadata in the
initial field block and use level 4–6 headings inside items. OS metadata becomes
ignored. CI installs a pinned OpenSpec validator; local validation can skip it.
Branch publication and deferred suggestion decisions remain separate actions.
