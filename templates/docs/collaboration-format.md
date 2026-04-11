# Collaboration File Format

This file defines the standard message format for all agent collaboration files in this project.

## Agent Roles

| Agent | Role | Writes To |
|-------|------|-----------|
| [Lead] | Lead — integrates accepted decisions into source-of-truth files | `collaboration-[lead].md`, all source-of-truth files |
| [Agent A] | Consultant — surfaces gaps and reviews; does not write to spec | `collaboration-[agent-a].md` only |
| [Agent B] | Consultant — surfaces gaps and reviews; does not write to spec | `collaboration-[agent-b].md` only |

_Fill in agent names and roles before distributing to agents._

## Source of Truth

Durable product decisions live in: `[path to spec/exploration files]`

Collaboration files are the communication layer only. Do not write product decisions here.

## Rules

1. Each agent writes only to its own collaboration file.
2. Cross-agent messages must name the target agent explicitly.
3. Durable decisions belong in source-of-truth files, not here.
4. Every item must carry a status: `open` | `accepted` | `partially_accepted` | `rejected` | `superseded` | `done`
5. Resolved items are commented out into `## Closed`, not deleted.
6. Every response must explain why the decision was made.
7. Reference exact file paths and line numbers when relevant.
8. Update your index file whenever an item status changes.

## Message Format

### Outgoing item

```md
### [ID] Title
- `date`: YYYY-MM-DD
- `from`: <agent>
- `to`: <agent | all | user>
- `type`: status | question | gap | review | suggestion
- `status`: open
- `scope`: file(s) or topic
- `why`: one short sentence
- `request`: one short sentence
- `refs`: path:line (optional)
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

## ID Convention

Assign a short prefix per agent and increment per item. Example:

- `CL-001` for Claude
- `CX-001` for Codex
- `GM-001` for Gemini

Responses reference both IDs: `### [CL-004] Response to CX-001`

## Operating Pattern

1. Agent writes a compact item in its own file and updates its index.
2. Target agent replies in its own file, referencing the original ID.
3. Lead agent integrates accepted outcomes into source-of-truth files.
4. All agents mark completed items `done` and move them to `## Closed`.
5. User is asked one question at a time by the consolidating agent.
