# Collaboration File Format

This file defines the standard message format for per-agent collaboration files.

## Goals

- Low token cost per read
- Fast scan by humans and agents
- Explicit traceability between suggestion and response
- Explicit status tracking
- No file-lock conflicts between agents

## Rules

1. Each agent writes only to its own collaboration file.
2. Cross-agent messages must name the target agent explicitly.
3. Durable decisions do not belong here — put them in the source-of-truth files.
4. Every item must carry one of these statuses:
   - `open` — awaiting action or response
   - `accepted` — decision accepted, action taken or pending
   - `partially_accepted` — some parts accepted, others not
   - `rejected` — declined with rationale
   - `superseded` — made irrelevant by a later decision
   - `done` — fully resolved and closed
5. Resolved items should be commented out into `## Closed`, not deleted, to preserve audit trail.
6. Every response must explain why the decision was made.
7. Prefer one-line bullets and short rationale over long prose.
8. Reference exact file paths and line numbers when relevant.
9. Whenever an item status changes, update that agent's index file in the same turn.

## Message Format

### Outgoing item (question, review, gap, status, suggestion)

```md
### [ID] Title
- `date`: YYYY-MM-DD
- `from`: <agent>
- `to`: <agent | all | user>
- `type`: status | question | gap | review | suggestion
- `status`: open
- `scope`: file(s) or topic
- `why`: one short sentence — why this matters
- `request`: one short sentence — what action is needed
- `refs`: path:line (optional)

Body (optional) — short bullets only
```

### Response item

```md
### [ID] Response to [original-ID]
- `date`: YYYY-MM-DD
- `from`: <agent>
- `to`: <agent | all | user>
- `type`: response
- `status`: accepted | partially_accepted | rejected | superseded | done
- `decision`: short answer
- `why`: short rationale
- `action`: what changed or what happens next
- `refs`: path:line (optional)
```

## Message Types

| Type | Usage |
|------|-------|
| `status` | Reporting that something happened (workflow change, file updated) |
| `question` | Asking for a decision from another agent or the user |
| `gap` | A conflict or missing rule that could cause implementation divergence |
| `review` | A structured assessment of files or proposals |
| `suggestion` | A non-blocking improvement idea; can be declined without consequence |
| `response` | A reply to any of the above, referencing the original ID |

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

## Index Format

Each agent maintains a separate index file (`collaboration-index-[agent].md`):

```md
# Collaboration Index: [Agent]

This file is the [Agent]-only status index.

- Do not use this file for discussion.
- Detailed notes live in `docs/collaboration-[agent].md`.
- Durable truth lives in [source-of-truth path].

| ID | To | Status | Summary |
|----|----|--------|---------|
| XX-001 | all | done | ... |
| XX-002 | lead | open | ... |
```

## Writing Style

- Lead the item with the most important fact.
- Avoid repeating content already in source-of-truth files — link instead.
- If something is resolved in a source-of-truth file, mark the collaboration item `done` and comment it out.
- One decision per item. Split compound decisions into separate items.

## Operating Pattern

1. Agent writes a compact item in its own file and updates its index.
2. Target agent reads it and replies in its own file, referencing the original ID.
3. Lead agent integrates accepted outcomes into source-of-truth files.
4. All agents mark completed items as `done` and move to `## Closed`.
5. User is asked one question at a time by whichever agent is consolidating the decision queue.
