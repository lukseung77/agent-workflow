# Collaboration File Format

This file defines the standard message format for per-agent collaboration files.

## Rules

1. Write authority follows `workflow/role-boundaries.md`; reference-registry exceptions follow `workflow/markitdown.md` and local restrictions.
2. Cross-agent messages must name the target agent explicitly.
3. Promote decisions under `workflow/decision-protocol.md#recording-decisions`.
4. Work discovery uses `status: open|active` plus `to: <agent>|all`. Message `type` controls handling, not visibility.
5. `to: all` means every agent except the sender. Name the sender explicitly when self-addressing is intentional.
6. Lifecycle status and finding disposition are separate:
   - `open` — awaiting work
   - `active` — work started but incomplete
   - `done` — work completed
   - `superseded` — replaced by a later item
7. Only the lead records formal finding disposition: `adopted`, `partially_adopted`, `not_adopted`, or `deferred`. Deferred findings name an owner or re-evaluation trigger.
8. Every response must explain why the decision was made.
9. Prefer one-line bullets and short rationale over long prose.
10. Reference exact file paths and line numbers when relevant.

## Message Format

### Item Template

Use this header for every item; omit optional fields that do not apply.

```md
### [ID] Title
- `date`: YYYY-MM-DD
- `created_at`: YYYY-MM-DDTHH:MM:SS+HH:MM (optional)
- `session_id`: session identifier (when required below)
- `from`: <agent>
- `to`: <agent | all | user>
- `type`: status | question | gap | review-request | review | suggestion | response
- `status`: open
- `formal`: false (review-request only; optional, defaults to false)
- `scope`: file(s) or topic
- `why`: why the item matters
- `request`: requested action, when applicable
- `refs`: original item IDs and source paths, when applicable
- `decision`: short answer (non-review replies)
- `action`: next action or completed change (non-review replies)

Body: focused findings, reasoning, or evidence when needed.
```

For a reply, name the original ID in the title and `refs`; completed replies
normally use `status: done`. Completed review assessments use `type: review`
and the review guidance in `workflow/review-cycle.md`; other replies use
`type: response`. Acknowledgment alone is not a completed review.

### Parser Boundaries

Keep each item header at column one as `### [ID] Title`. Put its metadata in the
initial contiguous field block, before body text or a blank separator. Later
metadata-looking bullets are body content and cannot change routing or status.
Fenced code blocks (backticks or tildes) and HTML comments never create items or
metadata. Use headings of level 4–6 inside an item; a heading of level 1–3 ends
the item and starts another item or a standing section. These boundaries also
govern archival, so standing notes remain in the live file.

## Message Types

| Type | Usage |
|------|-------|
| `status` | Reporting that something happened (workflow change, file updated) |
| `question` | Asking for a decision from another agent or the user |
| `gap` | A conflict or missing rule that could cause implementation divergence |
| `review-request` | Lead agent signalling that a draft is ready for consultant review; carries scope, file references, and requested review |
| `review` | A consultant's structured assessment in response to a `review-request` |
| `suggestion` | A non-blocking improvement idea; can be declined without consequence |
| `response` | A non-review reply; completed review assessments use `review`, referencing the original ID |

`date` must be exact `YYYY-MM-DD`. Optional `created_at` must be ISO 8601 with
`Z` or a UTC offset and its calendar date must match `date`.

### Session Identification

Include `session_id` for handoffs and status items summarizing a session. Prefer
the native conversation/session/run ID; if unavailable, use
`<agent>-<YYYY-MM-DD>-<project>-<slug>` and label it as a fallback. Other items
need no session ID unless project-local rules require one.

## Formal Review Findings

Informal reviews may use short bullets. A review request marked `formal: true` uses stable finding rows:

```md
| finding_id | location | category | what | why | correction |
|------------|----------|----------|------|-----|------------|
| GM-004-F01 | spec.md:42 | contradiction | ... | ... | ... |
```

- Use one issue per row.
- `correction` is optional.
- Consultants describe impact in `why`; they do not assign canonical priority.
- The lead uses these canonical priority values:
  - `P0`: correctness, compliance, security, or delivery blocker
  - `P1`: required before submission, acceptance, or implementation
  - `P2`: optional improvement
- Consolidation, source finding preservation, disposition assignment, and closure
  follow `workflow/review-cycle.md#formal-review-consolidation`.

## Verification Evidence

Claims that checks passed must identify the actual check, outcome, and relevant
content/version; cite concise output or an evidence reference when supporting
review completion, acceptance, or a stage gate. Distinguish passed, failed,
skipped, and blocked checks. File existence or model agreement alone does not
prove execution or requirement satisfaction. Reuse reliable current evidence;
rerun when changed content or uncertainty makes it stale. Scale evidence to the
claim, without mandatory command receipts for ordinary prose reviews.

When transcribing findings, preserve their substance and reference the original
agent/item. Optional `authored_by` metadata may identify an author different from
`from` (the recorder); it grants no permission to write another agent's file.

## Agent Aliases

- `agy` is an alias for `gemini`; address collaboration items to `gemini` in files, but treat user requests mentioning `agy` as requests for Gemini.

## ID Convention

Assign a short prefix per agent and increment per item:

- `CL-001` for Claude
- `CX-001` for Codex
- `GM-001` for Gemini
- Adapt prefixes for any agent names used in your project

Responses reference both the response ID and the original:

```
### [CL-004] Response to CX-001
```

## Active Queue

Collaboration files are authoritative. Generate an active queue with:

```sh
python3 <foundation-root>/scripts/collab_queue.py <agent>
python3 <foundation-root>/scripts/collab_queue.py <agent> --id ITEM-ID
python3 <foundation-root>/scripts/collab_queue.py <agent> --refs REQUEST-ID
```

`--id` retrieves a uniquely identified live or numbered-archive item regardless
of status or recipient. `--refs` lists items referencing an exact request ID,
including completed and archived reviews; the agent argument filters only the
default active queue. Missing or duplicate IDs fail rather than select silently.

The default output is compact. Use `--full` for all active item details or `--json` for automation. Queues sort newest first for presentation but never expire or hide older unresolved work.

Timestamp order uses actual UTC instants. Date-only legacy items use midnight
UTC; malformed timestamps fall back to the date and are diagnosed by lint.
The `agy` alias works in queue arguments as well as recipient fields.

Lint warns on sender/recipient names not represented by a collaboration file
(except `all` and `user`). Use repeatable `--allowed-agent NAME` for legitimate
participants without a file. Warnings preserve compatibility; inspect them before
relying on a queue because a misspelled recipient can hide work.


## Defined Terms

Use `workflow/defined-terms.md` when writing or reviewing formally defined domain terms in collaboration files or other project documents.

## Writing Style

- Lead the item with the most important fact.
- Avoid repeating content already in source-of-truth files — link instead.
- If something is resolved in a source-of-truth file, mark the collaboration item `done` and leave it parseable for `scripts/collab_archive.py`; do not comment it out.
- One decision per item. Split compound decisions into separate items.
