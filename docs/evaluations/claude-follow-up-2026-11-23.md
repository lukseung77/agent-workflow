# Claude CL-010 / CL-011 Disposition

Reviewed both suggestions against the working product and scripts. The human
requested review and acceptance on 2026-11-23. CL-011 supersedes CL-010 R3/E3
and records this exact human direction: "legacy support is only limited to
existing project. also devise a migration plan to move from older agent-workflow.
tooling review frequency is when openspec stage changes and manual request.
please update your suggestions" (spacing normalized here; verbatim record is in
CL-011). Earlier automatic setup/resume freshness behavior is superseded.

## Consolidated Decisions

| Finding / proposal | Disposition | Result and rationale |
|---|---|---|
| R1; D1–D4; I4/I7 | Adopted | `workflow/tooling.md` owns policy, lifecycle, scope, and adapter routing. `third-party/origins.json` is the sole catalog. Removed the assessment table and obsolete tooling policy/router files. Adapters link the common lifecycle and retain tool-specific behavior. |
| R2; I8 | Adopted | Removed request numbers, correction anecdotes, and repeated exclusion rationale from the registry. General guidance no longer carries the original request's assessment history; that assessment is retained in this repository's evaluation history. |
| R3 as superseded by CL-011 | Adopted with the L3 correction below | Legacy handling is on demand in `workflow/migration.md`. New startup has no old shared-override or persistent-index path. Removed all seven unused pointer/template files. Root README explains the old layout requires migration. |
| R4; E2/I9 | Adopted | `collab_queue.py AGENT --startup` combines the recipient queue, lead-only explicit user items, and references to open lead reviews, including archived responses. It prints a compact offline last-review status. Host templates invoke it; lead duties are in role boundaries. No startup online review runs. |
| R5; I6 | Adopted | Renamed product `docs/` to `guides/` and operations guide to `guides/tooling-operations.md`. Updated product references, registry pointers, manifest, installer-generated adapters, tests, and root README. `docs/` now consistently means consumer documentation. This is a deliberate path migration under the current acceptance request. |
| R6; I2/I7/D11 | Adopted | `templates/new-project-setup.md` is the single setup guide and init-command example. Preserved the prior context/root/role guidance there; lifecycle and READMEs link it. Setup order is candidate selection followed by ordinary selected installation. When separately requested, freshness review occurs between candidates and installation. |
| R7; D5–D9 | Partially adopted | Question pacing is owned by question-model; Grill Me retains only its host/dependency specifics. Decision promotion, upstream authority, reference write exceptions, and placement use focused owners and short cross-references. Kept a few short core-model reminders and navigation links where removing them would obscure startup or authority. No competing procedures remain. |
| R8; I1 | Adopted | Per-stage reviewer bullets removed; one common transition protocol explicitly governs all stages in addition to their individual gate criteria. Concurrence and user confirmation are preserved. |
| R8; I3 | Adopted | Checker result is `event-recorded`; per-tool `current` keeps its version meaning. Recorded event output is one line unless full JSON is requested. |
| R8; I5 | Adopted | Consolidation template now has a Deferred block requiring rationale plus owner/re-evaluation trigger. |
| R8; E4 | Adopted | Shared per-agent adapters are on-demand through task routing instead of mandatory startup reads. Local restrictions and project facts remain startup authority. |
| R8; D12/I4 | Adopted | Constant optional/automatic-install policy and repeated installation wording moved to registry defaults. `bootstrap_install_supported` explicitly marks Graphify and RTK; opt-in package installation remains distinct from silent auto-install. |
| R8 empty directory | Adopted | Removed empty retired product directories; they carry no required distribution content. |
| E1 | Partially adopted | Removed repeated catalog/procedures and unused wrappers while keeping the requested supported integration set. Do not remove useful integration capability merely to reach a particular byte ratio. Final product snapshot is 53 files / 209,443 bytes, including migration code. |

## CL-011 Legacy And Migration Findings

| Finding | Disposition | Result and rationale |
|---|---|---|
| L1 | Adopted | Removed legacy shared override/index handling from current startup and precedence. Existing project migration preserves old restrictions before adopting current rules. |
| L2 | Adopted | Migration guide is routed on demand from rule precedence. |
| L3 | Partially adopted | Detection requires missing foundation state **and** legacy markers. An empty new project also lacks installation state, so missing state alone would incorrectly route every new project to migration. |
| L4 | Adopted | Removed seven unused product pointer files. The current product does not pretend old root-layout paths still work. Consumer-specific custom wrappers remain preserved until reviewed during migration. |
| M1 | Adopted | Added a migration guide with inventory, mechanical conversion, semantic review, verification, archival, recording, first-update review, and rollback. It preserves current stage, accepted scope, collaboration history/IDs, references, and installed tools. |
| M2 | Partially adopted | Added `foundation.py migrate`, read-only by default, with `--apply`. It installs current files, backs up affected content, removes reviewed narrow old host pointers, carries shared overrides, and records a receipt. It deliberately preserves old files/vendored trees and lists semantic role/rule/cleanup tasks rather than deleting or interpreting arbitrary project instructions automatically. Apply reports semantic review still required. |
| M3 proposed merge-base change | Not adopted | Existing local content must remain a customization relative to the incoming template. Recording it as the template base could make a later update replace it as if it were unchanged upstream content. Documented careful first-update review and added a preservation regression test instead. This is not an initialization defect requiring the proposed baseline rewrite. |
| M4 | Adopted | Added an old-layout fixture plus preview/apply/state/history/lint/idempotence, first-update customization, fresh-project detection, and symlink-boundary tests. Also exercised CLI migration from an exported product; no real existing consumer was migrated. |

## CL-011 Tooling Review Findings

| Finding | Disposition | Result and rationale |
|---|---|---|
| T1/T2 | Adopted | Two triggers are defined in tooling-review: confirmed stage change and explicit manual request. Setup still selects tools but no longer triggers freshness review. |
| T3 | Adopted | Removed the every-startup/resume freshness command and missed-review polling. Combined startup only reads offline last-review metadata. A pending transition remains work in its collaboration record. |
| T4 | Adopted | CLI events are now `manual` and `stage-change`; old setup/resume invocation is rejected. Manual requests always review; repeated IDs for a recorded stage event reuse evidence. Historic local records are retained as evidence, not rewritten to claim a different trigger. |
| T5 | Adopted interpretation | Stage changes follow Exploration/Proposal/Implementation, including a new change entering the same named stage via a unique transition ID. Artifact edits alone and mere startup/resume do not trigger online work. No broader hook or background daemon is inferred. |

## Evidence And Limits

- `python3 -B scripts/validate.py --require-openspec`: 71 tests, three main specs,
  zero collaboration lint errors/warnings, 53-file boundary/self-consumer check.
- Literal product-path scan: no broken references. Registry support pointers
  resolve; bootstrap installer capability matches Graphify/RTK only.
- Reviewed/applied this consumer's update: host blocks merged without conflicts.
- Exported foundation initialized a fresh consumer with `guides/`, the combined
  startup command, empty tooling-review history, and no automatic online review.
- Exported CLI migration preview wrote no state; apply preserved old content,
  reported semantic-review work, and passed strict collaboration lint.
- No online freshness review, third-party installation/upgrade, real consumer
  migration, or GitHub publication was performed during this follow-up.

Claude's source suggestions remain in its own collaboration file. CX-019 is the
lead's completed disposition response; author-owned source statuses were not
edited by another agent. This assessment accepts/refines suggestions and does
not claim a new independent consultant concurrence or stage transition.
