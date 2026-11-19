# Project Init — Agent Script

When a user asks you to set up a new project using this workflow, follow these steps in order.
This is the entry point. Complete each step before moving to the next.

## Your Role: Lead Agent

**By running this script, you become the setup lead and default project lead unless the user explicitly assigns that role elsewhere.**

Follow `<workflow-root>/workflow/role-boundaries.md` for generic lead, consultant, and user authority. During setup, the lead agent owns:

- All GitHub operations: `git push`, `git pull`, `gh` commands — only you run these
- All writes to source-of-truth files (`openspec/`, `spec/`, etc.)
- Stage transitions: declare readiness and record the transition only after agent concurrence and user confirmation under `<workflow-root>/workflow/stages.md`
- Integrating accepted decisions from consultant agents into source-of-truth files
- Tiebreaker when consultant agents disagree

Record the lead and consultant assignments in `agent-workflow-local/project-facts.md`. Role assignments remain active until the user explicitly changes them.

---

## Step 1: Fetch Workflow Files

Fetch or copy the workflow repository:

```
https://github.com/lukseung77/agent-workflow
```

Preferred local layouts:

```
../agent-workflow
./agent-workflow
```

Use `../agent-workflow` for a shared sibling checkout or `./agent-workflow` for a project-vendored downstream copy.

Do not copy shared global workflow rules into `agent-workflow-local/`.

The shared rules should stay in `<workflow-root>/workflow/`.
The new project should keep only project-local overrides in `./agent-workflow-local/`.

Read these shared workflow files before continuing:

```
<workflow-root>/workflow/rule-precedence.md
<workflow-root>/workflow/agent-workflow.md
<workflow-root>/templates/new-project-setup.md
```

Follow the canonical read order after the project bootstrap exists. Read topic files only when the current setup step requires them.

Use task routing for additional rules when a setup step needs them.

---

## Step 2: Interview The User — Project Purpose

Ask unanswered questions **one at a time**, following
`workflow/question-model.md`. Read supplied briefs first and skip facts already
established. A remaining-question estimate is optional when useful.

| # | Question |
|---|----------|
| Q1 | What is the project title or name? |
| Q2 | What problem does this project solve, or what is its main goal? |
| Q3 | Who is the primary user? |
| Q4 | What are the 2–3 core outcomes you want from this project? |

Record each answer. These go directly into the initial `product-scope.md` in checklist section 6.

---

## Step 3: Interview The User — Tools And Platform

Continue with any unanswered platform and tool questions:

| # | Question |
|---|----------|
| Q5 | What platform or environment is this for? (e.g. Android, iOS, web app, desktop, API, CLI) |
| Q6 | Are there any tools, languages, or frameworks already decided? ("None yet" is a valid answer.) |

**Scope boundary:** only ask about platform and already-decided tools. Do not ask about architecture, libraries, database choices, or implementation approach — those are deferred to the proposal stage.

Record the answers. These go into the initial scope document under a `Tools And Platform` section.

---

## Step 4: Prepare The Repository

Reuse an existing local repository when available. For a new local-only project,
initialize Git in its project directory and create a minimal README and initial
commit; a GitHub remote is optional. Record the chosen repository path in project
facts. Continue to Step 5 without GitHub when offline or local-only.

Run the following GitHub setup only when the user has requested or confirmed
remote creation; reuse known name/visibility choices without asking again:

1. Propose a repository name based on the project title (lowercase, hyphenated, e.g. `my-project`)
2. Ask the user whether they want it public or private
3. Confirm the name and visibility before creating
4. Create the repository:
   ```
   gh repo create [name] --[public|private] --description "[one-sentence purpose]"
   ```
5. Clone it locally and set it as the working directory
6. Create an initial commit:
   - `README.md` containing the project title and one-sentence purpose

Success criteria for this step:

- The local repository exists and is the working directory.
- If GitHub setup was requested, its remote exists with the confirmed visibility.
- The project has an initial commit with a minimal `README.md`.

Continue to Step 5. The environment bootstrap runs after the workflow files
exist so the initial Graphify index includes the initialized project structure.

---

## Step 5: Run The File Setup Checklist

Follow `templates/new-project-setup.md` to complete the full project structure:

- Create `docs/` and all collaboration files
- Create `agent-workflow-local/` for project facts, local rules, per-agent assignments, and current state
- Create `agent-workflow-local/references/reference.md` and `agent-workflow-local/references/markitdown/`
- Verify generated collaboration queues, or create active-only compatibility indexes when scripts cannot run
- Use the source root recorded in project facts; `openspec/explorations/` is the default, not a required migration for an existing project
- Record stable paths, roles, stage tracking, and active source-of-truth inventory in `agent-workflow-local/project-facts.md`
- Record only project-specific workflow rules in `agent-workflow-local/rules.md`
- In checklist section 6, create `product-scope.md` under that source root using the Q1–Q6 answers and this initial template:

```md
# Product Scope

## Status

Active Exploration

## Purpose

[Answer from Q2]

## Primary User

[Answer from Q3]

## Core Outcomes

[Answer from Q4, as bullet list]

## Platform And Tools

- Platform: [Answer from Q5]
- Decided tools: [Answer from Q6, or "None decided yet — deferred to proposal stage"]

## Exploration Map

(Files will be added here as exploration progresses)

## Open Areas

(To be determined during exploration)
```

Success criteria for this step:

- The collaboration files, local workflow files, and source-of-truth directory all exist.
- The copied templates have been filled in with real agent names, roles, and paths.
- A new agent could join the project and orient itself without asking setup questions.

Optional tool initialization is handled once in the checklist using
`docs/agent-tooling.md`; use its commands, opt-ins, and diagnostic definitions.

---

## Step 6: Begin Exploration

After setup is confirmed complete (all checklist items in `new-project-setup.md` done):

1. Log the transition in your collaboration file as a `status` item: "Setup complete — entering Exploration stage"
2. Begin the domain model exploration with the first question:

   > "What are the main things a user creates, manages, or interacts with in this project?"

3. Ask follow-up questions **one at a time**, recording confirmed answers directly into `domain-model.md` under the recorded source root as you go
4. After the domain model is started, move to the next exploration file — ask the user which area to explore next, or suggest the most logical next area based on the answers so far

**Exploration continues until all agents concur the space is proposal-ready and the user has answered all blocking questions. See `workflow/stages.md` for gate criteria.**

---

## Notes

- Use `workflow/question-model.md` for interview pacing and optional progress estimates.
- If the user provides existing PDFs, office files, web exports, or archives, track them in `agent-workflow-local/references/reference.md`, convert them with MarkItDown or another reliable extractor, and summarize them before writing source-of-truth files
- If the user says "I'll handle the GitHub repo myself," skip remote creation and use their local repository or supplied URL when available
- If the user already has a brief or existing documents, read them before Step 2 and skip any questions already answered
- If another agent will also be joining the project, complete setup fully before briefing them — they should join a working structure, not a half-initialized one
