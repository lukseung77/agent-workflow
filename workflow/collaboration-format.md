# Collaboration File Format

This file defines the standard message format for per-agent collaboration files.

## Goals

- Low token cost per read
- Fast scan by humans and agents
- Explicit traceability between suggestion and response
- Explicit status tracking
- No file-lock conflicts between agents

## Rules

1. Each agent writes only to its own collaboration file, except for allowed operational updates to `agent-workflow-local/references/reference.md`.
2. Cross-agent messages must name the target agent explicitly.
3. Durable decisions do not belong here — put them in the source-of-truth files.
4. Work discovery uses `status: open|active` plus `to: <agent>|all`. Message `type` controls handling, not visibility.
5. `to: all` means every agent except the sender. Name the sender explicitly when self-addressing is intentional.
6. Lifecycle status and finding disposition are separate:
   - `open` — awaiting work
   - `active` — work started but incomplete
   - `done` — work completed
   - `superseded` — replaced by a later item
7. Only the lead records formal finding disposition: `adopted`, `partially_adopted`, or `not_adopted`.
8. Every response must explain why the decision was made.
9. Prefer one-line bullets and short rationale over long prose.
10. Reference exact file paths and line numbers when relevant.

## Message Format

### Outgoing item (question, review, gap, status, suggestion)

```md
### [ID] Title
- `date`: YYYY-MM-DD
- `created_at`: YYYY-MM-DDTHH:MM:SS+HH:MM (optional)
- `from`: <agent>
- `to`: <agent | all | user>
- `type`: status | question | gap | review-request | review | suggestion
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
- `created_at`: YYYY-MM-DDTHH:MM:SS+HH:MM (optional)
- `from`: <agent>
- `to`: <agent | all | user>
- `type`: response
- `status`: done
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
| `review-request` | Lead agent signalling that a draft is ready for consultant review; includes ready-to-paste prompts |
| `review` | A consultant's structured assessment in response to a `review-request` |
| `suggestion` | A non-blocking improvement idea; can be declined without consequence |
| `response` | A reply to any of the above, referencing the original ID |

`date` must be exact `YYYY-MM-DD`. When `created_at` is present, it must be ISO 8601 with `Z` or a UTC offset and its calendar date must match `date`.

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
- During consolidation, only the lead may merge equivalent findings into a `canonical_id`.
- Preserve every `source_finding_id`.
- Similar but distinct findings remain separate.
- After deduplication, the lead may assign:
  - `P0`: correctness, compliance, security, or delivery blocker
  - `P1`: required before submission, acceptance, or implementation
  - `P2`: optional improvement
- The lead records disposition for each canonical finding.

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
python3 ../agent-workflow/scripts/collab_queue.py <agent>
python3 ../agent-workflow/scripts/collab_queue.py <agent> --id ITEM-ID
```

The default output is compact. Use `--full` for all active item details or `--json` for automation. Queues sort newest first for presentation but never expire or hide older unresolved work.

Projects that cannot run the script may retain persistent index files as a compatibility fallback. Such indexes should contain active items only.

## Defined Terms

Any term that has been formally defined in the project's domain model or source-of-truth files is a **defined term**.

Whenever an agent refers to a defined term — in collaboration files, exploration files, proposals, or any project document — format it as:

```
<span style="color: #0066cc">**TERM NAME**</span>
```

This renders as bold blue all-caps text in local markdown viewers (VS Code, Obsidian, Typora).

> **GitHub note:** GitHub strips inline `style` attributes and will not render the color. On GitHub the term will appear as plain bold text. This is acceptable — the all-caps convention still distinguishes defined terms from prose.

Rules:
- Always use all capital letters for defined terms, regardless of where they appear in a sentence
- Apply the format every time the term is used, not just on first use
- If a project has not yet established a domain model, do not invent defined terms — wait until the exploration stage produces confirmed definitions
- When a new term is formally confirmed during exploration, add it to the domain model file and begin using the format immediately

Example — before:
> The rider creates a ride plan and attaches a route plan to it.

Example — after:
> The rider creates a <span style="color: #0066cc">**RIDE PLAN**</span> and attaches a <span style="color: #0066cc">**ROUTE PLAN**</span> to it.

## Writing Style

- Lead the item with the most important fact.
- Avoid repeating content already in source-of-truth files — link instead.
- If something is resolved in a source-of-truth file, mark the collaboration item `done` and comment it out.
- One decision per item. Split compound decisions into separate items.
- Use the defined-term format for all confirmed domain terms (see Defined Terms section above).

## Operating Pattern

1. Agent writes a compact item in its own collaboration file.
2. Target agent discovers it by recipient and lifecycle status, then replies in its own file referencing the original ID.
3. Lead agent integrates accepted outcomes into source-of-truth files.
4. Agents mark completed items `done`; archival is size-based and separate.
5. User is asked one question at a time by whichever agent is consolidating the decision queue.
