# Review Cycle Protocol

The review cycle is the repeating loop between a draft and a consolidated update.
The collaboration index and per-agent files carry all the state — agents self-direct from them on session start. The user's only action is starting each agent.

---

## How It Works

```
Lead drafts → posts review-request → updates index
  → user starts consultant A → reads index → self-directs review → writes to own collab file
  → user starts consultant B → same
  → user starts lead → reads consultant files → consolidates → updates source-of-truth
```

No prompts to paste. No context to explain. The files are the trigger.

---

## Step 1: Lead Posts Review Request

After completing any draft, the lead posts a `review-request` in its collaboration file and updates its index:

```md
### [XX-NNN] Review Request — [Topic]
- `date`: YYYY-MM-DD
- `from`: [lead]
- `to`: all
- `type`: review-request
- `status`: open
- `scope`: [topic]
- `why`: [one sentence — what was drafted and why review is needed]
- `request`: Read the listed files and leave feedback in your own collaboration file referencing this ID.
- `refs`: [file path(s)]
```

Index row:
```
| XX-NNN | all | open | review-request — [topic] |
```

That index entry is what consultants see when they start. Nothing else is needed from the lead.

---

## Step 2: Consultants Self-Direct

Every consultant's session-start checklist (in `agent-common.md`) begins with:
> Read the lead's index. If an open `review-request` exists, that is your first task.

So when the user starts a consultant agent — with no prompt beyond starting the session — the consultant:

1. Reads `docs/collaboration-index-[lead].md`
2. Finds the open `review-request` row
3. Reads the files listed in its `refs`
4. Posts a `review` item in its own collaboration file referencing the request ID
5. Updates its own index

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

---

## Step 3: Lead Consolidates

When the user starts the lead agent after consultants have responded, the lead's session-start checklist surfaces the open `review-request` in its own index. The lead:

1. Reads all consultant collaboration files for `review` items referencing the request ID
2. Accepts, partially accepts, or rejects each finding with a short rationale
3. Integrates accepted feedback into source-of-truth files
4. Posts a consolidation summary and marks the `review-request` done

Consolidation summary format:

```md
### [XX-NNN+1] Consolidation — [XX-NNN]
- `date`: YYYY-MM-DD
- `from`: [lead]
- `to`: all
- `type`: status
- `status`: done
- `refs`: [XX-NNN], [consultant review IDs]

Accepted:
- [finding] from [agent] → [what changed in which file]

Partially accepted:
- [finding] from [agent] → [what changed, what was excluded and why]

Rejected:
- [finding] from [agent] → [reason]
```

---

## User's Action Set

| Step | User does |
|------|-----------|
| Lead finishes draft | Nothing — lead posts review-request automatically |
| Trigger consultant reviews | Start each consultant agent |
| Trigger consolidation | Start lead agent |

The files carry all context. No prompts to paste, no context to explain, no information to relay between sessions.

---

## Triggering The Next Cycle

After consolidation, if more drafting is needed, the lead continues and posts another `review-request`. Consultants pick it up on next session start.

After consolidation, if the stage is complete, the lead posts a stage-readiness `status` item. Consultants concur or raise blockers on next session. User confirms the stage transition.
