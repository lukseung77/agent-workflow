# Tooling Freshness Review

This procedure has exactly two triggers: a confirmed OpenSpec/workflow stage
transition, and an explicit human request. Setup, migration, startup, and resume
do not independently trigger online checks. Setup may select candidates and
follow normal installation guidance without running this review.

The active lead runs the review before substantive work in a confirmed destination
stage. Transitions include regressions and a new change entering the same stage
name, identified by its unique collaboration ID. This follows the foundation's
Exploration/Proposal/Implementation model; changing an artifact alone is not a
stage transition. A stopped agent cannot be launched by a file change; pending
transition work is resumed from its collaboration status. No watcher is installed.

## Invoke

```sh
python3 <foundation-root>/scripts/tooling_review.py --root . --event stage-change --transition-id TRANSITION_ITEM_ID --tools SELECTED_REGISTRY_IDS
python3 <foundation-root>/scripts/tooling_review.py --root . --event manual --tools SELECTED_REGISTRY_IDS
```

Use only the applicable command. Stage comes from local state; `--stage NAME`
can identify a confirmed destination before the snapshot is saved. Reuse an
existing stage event's evidence rather than rechecking its upstream sources. A
manual request always starts a new review. `event-recorded` means this transition
has evidence, not that tools are current; `previous_status` preserves completed
versus degraded results. Use `--json` for full output after a recorded event.

The checker plans and records reviews; it never queries upstream, proves remote
facts, installs tools, changes stage, or starts agents. The lead uses available
network tools for the checks below. Installation lifecycle is in
`workflow/tooling.md`; do not duplicate it here.

## Perform The Review

1. Include selected/installed tools from local inventory, project dependencies,
   and the destination stage's needs. Supply unrecorded selections through
   `--tools`; register an unknown tool's official origin before reviewing it.
   Read only applicable integration adapters. Excluded SEO/voice and visual
   assets/animation stay outside automatic selection and discovery.
2. Check current official releases, tags, package metadata, changelogs, and host
   documentation. Compare installed versions/revisions with the latest stable
   **compatible** release; distinguish newer prereleases and breaking upgrades.
   For uninstalled selections, report the current compatible candidate rather
   than claiming an installed version. For hosted services, inspect current
   documented capabilities/access requirements and record the endpoint/date,
   not an invented server version. Include plugin/skill dependencies and changed
   prompts, hooks, permissions, package sources, licenses, and runtime needs.
3. Search primary sources for relevant new tools or replacements that address
   concrete product/stage gaps. Start with the supported origins and host
   documentation; Find Skills is an optional discovery aid. Do not require
   installing a discovery tool, searching the entire ecosystem, or finding a
   fixed number of new tools. No useful addition is a valid finding. Verify the
   actual upstream origin before recommending a candidate.
4. Record retain, recommend-update, recommend-addition, replace, retire, or defer
   with rationale. Preserve pinned versions and local adaptations until an
   upgrade is selected, authorized, installed, and verified using its adapter.
   Reuse existing authorization; checking freshness does not itself authorize
   package upgrades, paid services, host changes, or product scope changes.
   A recommendation affecting accepted scope follows the existing mini-proposal
   and review rules, not an extra tooling-specific gate.
5. Record checked URLs, observed versions/revisions or service documentation,
   timestamp, compatibility, decisions, and discovery findings. If network,
   authentication, or a source is unavailable, record `unavailable` with the
   limitation and fallback. Do not claim the latest version was verified.
   Optional-tool outages do not block stage work unless a required capability
   or material compatibility/security decision remains unresolved; use ordinary
   blocker handling for those cases. Preserve the existing concurrence/user
   confirmation requirements for the stage transition.

## Record Evidence

Write an evidence report outside the foundation, matching the plan's `context`,
`transition_id`, and selected `tools` keys. Example report shape:

```json
{
  "context": {"stage": "Implementation", "artifact": "openspec/changes/example"},
  "transition_id": "CX-123",
  "checked_at": "2026-11-23T10:00:00+00:00",
  "tools": {
    "grill-me": {
      "status": "unavailable",
      "decision": "retain",
      "summary": "Network unavailable; installed revision retained; latest upstream unknown."
    }
  },
  "discovery": {
    "status": "unavailable",
    "sources": [],
    "summary": "Online discovery unavailable; existing capabilities remain usable."
  }
}
```

Per-tool statuses are `current`, `update-available`, `unavailable`, or
`not-applicable`; checked statuses require `source` (primary HTTPS URL) and
`observed` (version/revision/service documentation observation). Use
`not-applicable` only with a concrete reason, not as a substitute for a failed
check. Discovery uses `checked` with primary-source URLs and a findings summary,
or `unavailable` with a limitation. Describe recommendations in these summaries
or extra report fields; the example is a shape, never evidence to copy as fact.

Record with the same event/options plus `--record REPORT_PATH`. The helper
validates accounting/context and appends to
`agent-workflow-local/tooling-reviews.json`; any unavailable checks produce
`degraded`, otherwise `completed`. These labels validate reported accounting,
not remote facts. Link the review in the lead's collaboration status and briefly
surface material recommendations/limitations in the setup or transition update.
Actual installations remain separately recorded in `tooling.json`; a freshness
review never overwrites that inventory. Retain event evidence for deduplication.
