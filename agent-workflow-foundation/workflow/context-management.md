# Context Management

Use this file when a project, document set, or agent session is getting large enough that startup or review context becomes expensive.

## Default Read Order

Follow `workflow/rule-precedence.md`. Do not maintain another startup order here.

When available, use `scripts/collab_queue.py` for a compact active queue, then load one selected item with `--id`. Read full historical collaboration threads only when a selected item or source file points to them.

## Restart Snapshot

Keep `agent-workflow-local/current-state.md` limited to:

- `updated`
- `current_stage`
- `current_artifact`
- `next_lead_action`
- `active_blockers`

Tasks belong in collaboration items and generated queues. Confirmed decisions belong in source-of-truth files. Historical activity belongs in collaboration files and archives.

Validate the snapshot with:

```sh
python3 <foundation-root>/scripts/collab_lint.py --root . --strict-state
```

Projects with additional stage names may pass repeatable `--allowed-stage NAME` options.

## File Shape

- Keep bootstrap files short enough to read every session.
- Put durable policy in shared workflow files.
- Put project-local facts, rules, and overrides according to `workflow/local-project-files.md`.
- Put current project state in `current-state.md`.
- Put stable project decisions in source-of-truth files.
- Put large examples, lessons, and source notes in references.
- Prefer topic files over one giant product document.
- Exclude operational installation/tool inventory, archived collaboration history, project-maintenance records, and raw external proposals from routine startup; load them only when the selected task needs them.

## Handoff Summaries

A useful handoff summary includes:

- session ID under `workflow/collaboration-format.md#session-identification`
- current stage
- lead agent and consultants
- source-of-truth root or inventory pointer
- next unresolved question or blocker
- recently reconciled feedback
- exact files changed since the last handoff

Avoid restating entire specs. Link to the relevant source files instead.

## Collaboration Thread Hygiene

- Use generated queues for scan-first orientation when available.
- Treat persistent indexes as optional compatibility files and do not require parallel updates when generated queues are in use.
- Summarize long review threads before asking another agent to act on them.
- Reconcile consultant feedback in one place so later agents do not repeat the same review.

## Archives

- Keep unresolved items in the live collaboration file regardless of age.
- Archive resolved items by size, not by calendar period.
- The default archive threshold is 20 KB of resolved content per live collaboration file.
- Use numbered per-agent files under `docs/collaboration-archives/`.
- Archive and legacy files remain readable when referenced but are excluded from normal startup reads.
- Use `scripts/collab_archive.py --dry-run` before writing archives.
- Item and standing-section boundaries follow `workflow/collaboration-format.md#parser-boundaries`.
- Completion validation reads numbered archives when resolving review evidence;
  active queues continue to read live collaboration files only.

## When To Split Files

Split a file when:

- startup requires reading many sections unrelated to the current task
- unrelated decisions are repeatedly edited together
- consultant feedback often says "this belongs somewhere else"
- agents paste long excerpts instead of linking focused source files

Do not split when the result would create many tiny files with no stable ownership.
