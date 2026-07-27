# Collaboration File Format

This file defines the standard message format for all agent collaboration files in this project.
Use it for collaboration structure only. Broader operating rules live in the shared agent templates.

## Agent Roles

| Agent | Role | Writes To |
|-------|------|-----------|
| [Lead] | Lead — integrates accepted decisions into source-of-truth files | `collaboration-[lead].md`, all source-of-truth files |
| [Agent A] | Consultant — surfaces gaps and reviews; does not write to spec | `collaboration-[agent-a].md`; allowed reference-registry rows |
| [Agent B] | Consultant — surfaces gaps and reviews; does not write to spec | `collaboration-[agent-b].md`; allowed reference-registry rows |

Fill in agent names and roles before distributing to agents.

## Source of Truth

Durable product decisions live in the files listed in `agent-workflow-local/project-facts.md`.

Collaboration files are the communication layer only. Do not write product decisions here.

## Rules

Follow `../agent-workflow/workflow/collaboration-format.md` for the canonical schema, recipient semantics, lifecycle statuses, formal finding rows, and queue commands.

Project-specific facts in this file are limited to the agent roster and source-of-truth root or inventory pointer.

## Message Format

### Outgoing item

```md
### [ID] Title
- `date`: YYYY-MM-DD
- `from`: <agent>
- `to`: <agent | all | user>
- `type`: status | question | gap | review-request | review | suggestion
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
- `status`: done
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

## Defined Terms

Any term formally defined in this project's domain model is a **defined term**. Format every reference as:

```
<span style="color: #0066cc">**TERM NAME**</span>
```

Always all-caps. Apply on every use, not just the first. Only use for terms confirmed in the domain model.

> GitHub strips inline styles — the color will not render there. All-caps bold still distinguishes defined terms in plain markdown.

## Startup

Follow `../agent-workflow/workflow/rule-precedence.md`. Generate the current agent queue when scripts are available; use persistent indexes only as a compatibility fallback.
