# Review Cycle Protocol

The review cycle is the repeating loop between a draft and a consolidated update.
Per-agent collaboration files carry authoritative review state. Generated recipient queues expose active work without maintaining a second index. Session activation follows the Trigger Model in `workflow/agent-workflow.md`.

---

## How It Works

```
Lead drafts -> posts review-request
  -> addressed consultants read request and review independently
  -> consultants write findings in their own collaboration files
  -> lead reads responses, consolidates, and updates source-of-truth
```

This is a work-dependency sequence, not a prescribed sequence of agent launches.
Consultants may review in either order or in parallel unless the request states
a dependency. Agent names and reviewer count come from project assignments and
the request; this protocol does not require a fixed Codex/Claude/Gemini order.

## Requests And Activation

- A collaboration file records what work is requested. Writing or updating it
  does not launch, wake, notify, or resume another agent by itself.
- By default, the human starts, resumes, or messages the relevant session to
  read its queue. A fresh session is not required for each review step.
- Optional orchestration may activate sessions only when the user explicitly
  asks or project-local rules allow it, as defined in `workflow/agent-workflow.md`.
  This protocol does not itself authorize agent invocation or install a watcher.
- An already-running lead may continue consolidation when responses are
  available; it need not be restarted. In the manual workflow, the human can
  message or resume it to check the files.
- Activation messages may point to a request ID, but requests, findings, and
  consolidation remain in collaboration files. Human approval decisions remain
  human decisions; agents record them under the applicable decision rules.
- Activation does not expand write authority, waive review completion gates, or
  confirm a stage transition. For this canonical repository, also follow
  `workflow/master-governance.md`.

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

### Reviewed Content And Freshness

Requests and reviews identify the reviewed scope and content in `refs` or the
body: use a commit SHA for committed content, or an identifiable snapshot/diff
including relevant untracked files for working-tree reviews. A commit is not
required. HEAD plus "dirty" alone does not distinguish successive edits; if
content changes during review, state the uncertainty and verify affected areas.

Before closing a review, the lead compares subsequent changes with reviewed
content. Recheck affected findings and dependent areas; request focused re-review
for substantive behavior, contract, or architectural changes. For trivial edits,
current checks and a brief rationale may suffice. Record why retained concurrence
still applies; this does not waive required formal or stage-review gates.

When a consultant starts, resumes, or is directed to check for work, it:

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

Before consolidation, including on resume, the lead checks its own open review requests and looks for consultant
`review` items referencing each request ID, even if its recipient queue is empty.
Completed reviews use `status: done` and are intentionally absent from active
queues; requests sent to `all` also exclude the sender. An empty recipient queue
therefore does not establish that there is nothing to consolidate.

When consultant responses are available and any human wait/proceed direction
permits consolidation, the lead:

1. Reads consultant review items referencing the request ID.
2. Verifies any user-provided responder signal against those files.
3. Adopts, partially adopts, or does not adopt each finding with a short rationale.
4. Integrates adopted feedback into source-of-truth files.
5. Posts a consolidation summary and marks the `review-request` done only when
   the requested review scope is complete and applicable completion gates pass.

If responses are still missing, record which reviewers remain and keep the
request open; silence or elapsed time is not a completed review. Integrating
available findings does not by itself close the request. Formal reviewer skips
require the user direction described below.

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

Verification claims supporting review completion or a stage/acceptance decision
follow `workflow/collaboration-format.md#verification-evidence`. Repeated failures
follow `workflow/decision-protocol.md#failures-and-retries`.

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

## Manual Activation Default

| Step | User does |
|------|-----------|
| Lead finishes draft | Nothing — lead posts review-request |
| Activate consultant reviews | Start, resume, or message each requested consultant; either order or parallel unless the request states a dependency |
| Activate consolidation | Message or resume the lead to check responses if it is not already continuing; optionally identify responders and direct wait/proceed |

The files carry review content, so the user need not relay findings or repeat
review context between sessions. Authorized orchestration may replace manual
activation, but does not replace required human decisions or file records.

---

## Triggering The Next Cycle

After consolidation, if more drafting is needed, the lead continues and posts another `review-request`. Consultants pick it up when their sessions next check for work under the activation rules above.

After consolidation, if the stage is ready, the lead posts a stage-readiness `status` item. Consultants concur or raise blockers when their sessions next check for work. The user confirms the stage transition under `workflow/stages.md`; publishing the status item alone does not advance the stage.
