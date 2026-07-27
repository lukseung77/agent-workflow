# Agent Collaboration Workflow

A generic, file-based multi-agent collaboration workflow for software and product projects.
Designed for async coordination between AI agents (Claude, Codex, Gemini, or others) and a human decision-maker, across exploration, proposal, and implementation stages.

---

## Why This Exists

When multiple AI agents work on the same project simultaneously, they need a way to:

- share findings without overwriting each other's work
- track open questions and decisions explicitly
- escalate genuine product decisions to the human without drowning them in noise
- preserve a clear audit trail from question to decision to spec update

This workflow uses one authoritative collaboration file per agent, generated active queues, typed messages with explicit IDs and lifecycle statuses, and a lead agent who integrates adopted decisions into source-of-truth files.

For the reusable coworking rules that sit above any one project, read:

- `workflow/rule-precedence.md`
- `workflow/agent-workflow.md`
- `workflow/local-project-files.md`
- `workflow/role-boundaries.md`
- `workflow/question-model.md`
- `workflow/diagrams.md`
- `workflow/ai-coworking-guide.md`
- `workflow/context-management.md`
- `workflow/markitdown.md`
- `skills/multi-agent-coworking/SKILL.md`

Lead agents from other projects can submit reusable improvement proposals in
`docs/external-lead-suggestions.md`. These proposals are not active rules until
they are reviewed and adopted into a canonical workflow file.

---

## Core Concepts

### Agents

Each agent has a **role**:

- **Lead agent** — owns the source of truth files (spec, openspec, etc.); integrates accepted decisions from other agents; has final say on synthesis
- **Consultant agents** — read the relevant state, indexes, and focused source files; write only to their own collaboration file except for allowed reference-registry updates; surface gaps, conflicts, and risks; do not write directly to the source of truth
- **User** — makes product/scope decisions that agents cannot resolve; is asked one question at a time, not a batch

### Files

The recommended layout is now split between one shared workflow repo and project-local overrides:

```text
shared-workspace/
├── agent-workflow/
│   ├── workflow/
│   │   ├── rule-precedence.md
│   │   ├── agent-workflow.md
│   │   ├── agent-workflow-codex.md
│   │   ├── agent-workflow-claude.md
│   │   ├── agent-workflow-gemini.md
│   │   ├── local-project-files.md
│   │   ├── role-boundaries.md
│   │   ├── question-model.md
│   │   ├── diagrams.md
│   │   ├── ai-coworking-guide.md
│   │   ├── context-management.md
│   │   ├── markitdown.md
│   │   ├── stages.md
│   │   └── review-cycle.md
│   └── skills/
│       └── multi-agent-coworking/
└── some-project/
    └── agent-workflow-local/
        ├── project-facts.md
        ├── rules.md
        ├── agent-workflow.md
        ├── agent-workflow-codex.md
        ├── agent-workflow-claude.md
        ├── agent-workflow-gemini.md
        ├── current-state.md
        └── references/
            ├── reference.md
            └── markitdown/
```

Projects should keep only local facts, local rules, local overrides, and current-state material in their own repository.

The shared workflow repo should remain the default home for generic rules.
Each agent gets one authoritative collaboration file in `docs/`:

- `collaboration-[agent].md` — full message thread for that agent

Active work is generated from those files with `scripts/collab_queue.py`. Persistent `collaboration-index-[agent].md` files are compatibility fallbacks only.

Reusable maintenance tools:

- `scripts/collab_queue.py` — compact recipient queues and selected-item detail
- `scripts/collab_lint.py` — read-only schema and restart-state validation
- `scripts/collab_archive.py` — threshold-based resolved-item archives

A shared `docs/collaboration-format.md` defines the message format all agents follow.

The source of truth (spec, exploration files, etc.) lives outside these files. Collaboration files are the communication layer, not the product layer.

### Context Budget

Agents should scan before they deep-read. Follow `workflow/rule-precedence.md` for startup order and `workflow/context-management.md` for the detailed context policy. Use `workflow/markitdown.md` when bulky PDFs, office documents, exported tickets, or other non-Markdown inputs need conversion before agent review.

### Triggering

Files carry state, but they do not automatically trigger another agent across tools or platforms.

In practice, the user still starts or messages the next agent session. Once started, that agent can self-direct by reading the collaboration and source-of-truth files.

### Messages

Each item in a collaboration file is a typed, ID-tracked message:

| Type | When to use |
|------|-------------|
| `status` | Reporting that something has happened |
| `question` | Asking another agent or the user for a decision |
| `review` | A structured assessment of a file or set of files |
| `gap` | A conflict or missing rule that blocks progress |
| `response` | Replying to another agent's message by ID |
| `suggestion` | A non-blocking improvement idea |

---

## Workflow Stages

### 1. Exploration

**Goal:** establish shared understanding of the problem space before writing any spec.

- Agents read existing materials and ask clarifying questions
- Conflicts and gaps are logged in collaboration files, not resolved unilaterally
- User resolves genuine product decisions one at a time
- Stage ends when: all major conflicts are resolved and agents concur the space is ready for proposal

**Gate criteria:**
- No unresolved direct conflicts
- All domain terms defined and agreed
- User has answered all blocking questions
- Agents have independently confirmed readiness

### 2. Proposal

**Goal:** write a structured spec from the settled exploration.

- Lead agent drafts proposals into spec files
- Consultant agents review proposals and log feedback
- User approves or adjusts proposals
- Stage ends when: a proposal is accepted and merged

**Gate criteria:**
- Exploration files are stable (no open conflicts)
- Proposal covers the settled scope — no speculative scope
- User has explicitly accepted the proposal

### 3. Implementation

**Goal:** build from the accepted spec.

- Agents work from spec files, not from exploration files or collaboration notes
- Any change to scope goes back through a mini-proposal cycle
- Collaboration files track implementation status and blockers

---

## Roles In Detail

See `workflow/role-boundaries.md` for lead, consultant, and user responsibilities. Project-specific assignments belong in `agent-workflow-local/project-facts.md` and per-agent local files.

---

## Setting Up A New Project

**If you are an AI agent and the user just asked you to set up a project:**
Read `templates/project-init.md`. That is your entry point; it covers fetching these files, interviewing the user, creating the GitHub repo, and beginning exploration.

**If you are setting up manually:**

1. Copy `templates/docs/` into your project's `docs/` directory
2. Rename `collaboration-[agent].md` for each agent you are using
3. Copy `templates/agent-common.md` and your agent's instruction file (`CLAUDE.md`, `CODEX.md`, or `GEMINI.md`) into the project root
4. Copy `templates/project-facts.md` to `agent-workflow-local/project-facts.md`
5. Copy `templates/local-rules.md` to `agent-workflow-local/rules.md`
6. Copy `templates/reference.md` to `agent-workflow-local/references/reference.md` and create `agent-workflow-local/references/markitdown/`
7. Decide which agent is the lead and which are consultants — write this in `docs/collaboration-format.md` and `agent-workflow-local/project-facts.md`
8. Have each agent read `docs/collaboration-format.md` before writing anything

---

## File Layout In A Project

```
your-project/
├── CLAUDE.md                               # Agent join instructions
├── docs/
│   ├── collaboration-format.md             # Message format spec + agent roles
│   ├── collaboration-[lead].md             # Lead agent thread
│   ├── collaboration-[consultant-a].md     # Consultant A thread
│   └── collaboration-[consultant-b].md     # Consultant B thread (if used)
├── agent-workflow-local/
│   ├── project-facts.md                    # Stable paths, roles, stage tracking, source-of-truth inventory
│   ├── rules.md                            # Project-specific workflow rules only
│   ├── agent-workflow.md                   # Short project-wide overrides or local map
│   ├── agent-workflow-[agent].md           # Per-agent assignment and restrictions
│   ├── current-state.md
│   └── references/
│       ├── reference.md                    # External reference registry
│       └── markitdown/                     # Converted Markdown outputs
└── [source-of-truth files]                 # Spec, exploration, domain model, etc.
```

---

## Key Rules (Quick Reference)

1. Follow `workflow/rule-precedence.md` before acting.
2. Use `workflow/role-boundaries.md` for write, GitHub, and stage authority.
3. Use `workflow/collaboration-format.md` for message schema and generated queues.
4. Use `workflow/question-model.md` for user questions and remaining-question estimates.
5. Use `workflow/local-project-files.md` for project-local file placement.
6. Use `workflow/diagrams.md` when a diagram is requested.
7. Use `workflow/markitdown.md` for bulky external references.

---

## Anti-Patterns To Avoid

- Copying shared workflow rules into local project files without a packaging need.
- Maintaining a second authoritative collaboration index when generated queues work.
- Letting collaboration notes become the only record of accepted product decisions.
- Asking the user to resolve items agents can classify and resolve themselves.
- Loading full history before generated queues and focused source files.
