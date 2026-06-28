# Review Cycle Protocol

The review cycle is the repeating loop between a draft and a consolidated update.
Per-agent collaboration files carry authoritative review state. Generated recipient queues expose active work without maintaining a second index. The user starts or resumes agent sessions and may identify responders or direct the lead to wait, consolidate, or proceed.

---

## How It Works

```
Lead drafts → posts review-request
  → user starts consultant A → generates queue → self-directs review → writes to own collab file
  → user starts consultant B → same
  → user starts lead → reads consultant files → consolidates → updates source-of-truth
```

No prompts to paste. No context to explain. The files are the trigger.

---

## Step 1: Lead Posts Review Request

After completing any draft, the lead posts a `review-request` in its collaboration file:

```md
### [XX-NNN] Review Request — [Topic]
- `date`: YYYY-MM-DD
- `from`: [lead]
- `to`: all
- `type`: review-request
- `status`: open
- `formal`: false
- `scope`: [topic]
- `why`: [one sentence — what was drafted and why review is needed]
- `request`: Read the listed files and leave feedback in your own collaboration file referencing this ID.
- `refs`: [file path(s)]
```

Set `formal: true` only when reviewer accounting, stable finding IDs, deduplication, priority, disposition, and completion validation are required.

---

## Step 2: Consultants Self-Direct

When the user starts a consultant agent, the consultant:

1. Generates its queue with `scripts/collab_queue.py`.
2. Selects an addressed open review request.
3. Reads the request and files listed in `refs`.
4. Posts a `review` item in its own collaboration file referencing the request ID.
5. Marks its response `done`.

Consultant review format:

```md
### [YY-NNN] Review — [XX-NNN] [Topic]
- `date`: YYYY-MM-DD
- `from`: [consultant]
- `to`: [lead]
- `type`: review
- `status`: done
- `refs`: [XX-NNN], [file path(s)]

Findings:
- [finding 1]
- [finding 2]
```

For `formal: true`, replace free-form findings with the canonical finding table from `workflow/collaboration-format.md`.

---

## Step 3: Lead Consolidates

When the user starts the lead after consultants have responded, the lead:

1. Reads consultant review items referencing the request ID.
2. Verifies any user-provided responder signal against those files.
3. Adopts, partially adopts, or does not adopt each finding with a short rationale.
4. Integrates adopted feedback into source-of-truth files.
5. Posts a consolidation summary and marks the `review-request` done.

Consolidation summary format:

```md
### [XX-NNN+1] Consolidation — [XX-NNN]
- `date`: YYYY-MM-DD
- `from`: [lead]
- `to`: all
- `type`: status
- `status`: done
- `refs`: [XX-NNN], [consultant review IDs]

Adopted:
- [finding] from [agent] → [what changed in which file]

Partially adopted:
- [finding] from [agent] → [what changed, what was excluded and why]

Not adopted:
- [finding] from [agent] → [reason]
```

## Formal Review Consolidation

For `formal: true`, the lead additionally:

1. Accounts for every requested reviewer as processed or explicitly skipped by user direction.
2. Deduplicates only findings that describe the same issue at the same location.
3. Assigns one `canonical_id` after deduplication.
4. Preserves every `source_finding_id`.
5. Assigns canonical priority only after deduplication.
6. Records exactly one disposition for every canonical finding.
7. Runs `scripts/collab_lint.py`.

A formal review may close only when reviewer accounting is complete, every processed finding maps exactly once, every canonical finding has a disposition, and lint reports zero errors. Informal reviews do not require this heavier gate.

---

## User's Action Set

| Step | User does |
|------|-----------|
| Lead finishes draft | Nothing — lead posts review-request |
| Trigger consultant reviews | Start each consultant agent |
| Trigger consolidation | Start lead agent; optionally identify responders and direct wait/proceed |

The files carry review content. The user does not relay prompts, findings, or responses between sessions.

---

## Triggering The Next Cycle

After consolidation, if more drafting is needed, the lead continues and posts another `review-request`. Consultants pick it up on next session start.

After consolidation, if the stage is complete, the lead posts a stage-readiness `status` item. Consultants concur or raise blockers on next session. User confirms the stage transition.
