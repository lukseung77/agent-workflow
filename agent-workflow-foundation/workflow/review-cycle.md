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

### Combined Review And Gate Concurrence

A review request may also ask for readiness concurrence. Name the proposed
transition, reviewed content, relevant gate criteria, and required reviewers.
Each consultant can give findings and an explicit `concur`, `blocked`, or
`conditional` gate assessment in one response. A generic "no blockers" review
does not imply concurrence unless it expressly covers the named transition.

The lead reconciles findings, verifies the gates, accounts for every assigned
reviewer, and records readiness in the consolidation status. Conditional support
counts only after its conditions are resolved and current evidence supports
retaining that concurrence. Apply the freshness rules below to substantive
changes; request focused re-review when needed. Do not repeat a consultant
concurrence round merely because the same review also served as a gate check.
The human still confirms the transition. This changes the number of review
rounds, not stage criteria, reviewer authority, or missing-response requirements.

---

## Step 2: Consultants Self-Direct

### Optional Critical Review Techniques

Start with the stated goal and check where execution fails it. For consequential
or uncertain decisions, select a useful technique rather than applying every one:

- Strongest counterargument: identify a credible alternative and when it would be preferable.
- Pre-mortem: explain plausible failure paths using current evidence or explicit assumptions.
- Disconfirming evidence: name observations, tests, or metrics that would reject the approach.
- Socratic critique: use `workflow/question-model.md` for decision-changing questions.

Use the existing finding format: cite the affected claim or file, evidence and
uncertainty, impact, and a proportionate correction. A hypothetical failure is not
a demonstrated defect. Do not require a fixed number of flaws, an adversarial
persona, extra approvals, or an interview before every implementation. State when
no material issue is found. Keep reviews focused; link supporting detail instead
of pasting long alternatives. Necessary evidence has no arbitrary length cap.

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

Before consolidation, including on resume, inspect responses to the lead's open
review requests with `collab_queue.py <agent> --refs REQUEST-ID`, then retrieve
selected findings with `--id ITEM-ID`. Lookup includes completed and archived
items; an empty active recipient queue does not establish review completion.

When consultant responses are available and any human wait/proceed direction
permits consolidation, the lead:

1. Reads consultant review items referencing the request ID.
2. Verifies any user-provided responder signal against those files.
3. Adopts, partially adopts, does not adopt, or defers each finding with a short rationale; deferred findings name an owner or re-evaluation trigger.
4. Integrates adopted feedback into source-of-truth files.
5. Posts a consolidation summary and marks the `review-request` done only when
   the requested review scope is complete and applicable completion gates pass.

Before closing a consolidation, put any remaining required work in a separate
`open` or `active` item addressed to its owner and link its ID in the summary.
The consolidation may finish once review and disposition are complete; unfinished
implementation must remain discoverable in a generated queue. Optional suggestions
may stay deferred with a rationale instead of becoming mandatory tasks.

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

`collab_lint.py --check-completion` checks named reviewer responses and a
consolidation from the requester, including numbered archives as evidence.
Broadcast reviewer rosters, authorized skips, and exact finding-to-disposition
mapping still require the lead's explicit check; a passing linter alone does not
establish full formal completion. Superseded requests require no completion.

---

## Continuing Work

Session activation follows `workflow/agent-workflow.md#trigger-model`; posting a
request never launches an agent or grants new write authority. A running lead
can consolidate available responses without restarting. For another draft,
post the next review request; for a stage transition, post readiness and obtain
concurrence and user confirmation under `workflow/stages.md`.
