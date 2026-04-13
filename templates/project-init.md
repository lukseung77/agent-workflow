# Project Init — Agent Script

When a user asks you to set up a new project using this workflow, follow these steps in order.
This is the entry point. Complete each step before moving to the next.

## Your Role: Lead Agent

**By running this script, you become the lead agent for this project.**

Lead agent responsibilities that belong to you and no one else (unless the user explicitly says otherwise):

- All GitHub operations: `git push`, `git pull`, `gh` commands — only you run these
- All writes to source-of-truth files (`openspec/`, `spec/`, etc.)
- Stage transitions: only you declare when the project moves from Exploration → Proposal → Implementation
- Integrating accepted decisions from consultant agents into source-of-truth files
- Tiebreaker when consultant agents disagree

Consultant agents write only to their own `docs/collaboration-[agent].md`. They do not push to GitHub, do not edit source-of-truth files, and do not trigger stage changes.

This role assignment is permanent unless the user explicitly transfers it.

---

---

## Step 1: Fetch Workflow Files

Fetch the shared workflow repository:

```
https://github.com/lukseung77/agent-workflow
```

Preferred local layout:

```
../agent-workflow
```

Do not copy the shared global workflow rules into the new project by default.

The shared rules should stay in `../agent-workflow/workflow/`.
The new project should keep only project-local overrides in `./agent-workflow-local/`.

Read these shared workflow files before continuing:

```
workflow/rule-precedence.md
workflow/agent-workflow.md
workflow/agent-workflow-[agent].md
workflow/stages.md
workflow/review-cycle.md
```

Read these setup-oriented files as needed:

```
README.md
workflow/ai-coworking-guide.md
templates/project-init.md
templates/new-project-setup.md
templates/docs/collaboration-format.md
templates/docs/collaboration-agent.md
templates/docs/collaboration-index-agent.md
```

Do not start the user interview until you understand the workflow.

---

## Step 2: Interview The User — Project Purpose

Ask these questions **one at a time**. Wait for each answer before asking the next. Do not ask multiple questions in one message.

| # | Question |
|---|----------|
| Q1 | What is the project title or name? |
| Q2 | What problem does this project solve, or what is its main goal? |
| Q3 | Who is the primary user? |
| Q4 | What are the 2–3 core outcomes you want from this project? |

Record each answer. These go directly into the initial `openspec/explorations/product-scope.md` after setup.

---

## Step 3: Interview The User — Tools And Platform

Continue one at a time:

| # | Question |
|---|----------|
| Q5 | What platform or environment is this for? (e.g. Android, iOS, web app, desktop, API, CLI) |
| Q6 | Are there any tools, languages, or frameworks already decided? ("None yet" is a valid answer.) |

**Scope boundary:** only ask about platform and already-decided tools. Do not ask about architecture, libraries, database choices, or implementation approach — those are deferred to the proposal stage.

Record the answers. These go into the initial `product-scope.md` under a `Tools And Platform` section.

---

## Step 4: Create The GitHub Repository

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

---

## Step 5: Run The File Setup Checklist

Follow `templates/new-project-setup.md` to complete the full project structure:

- Create `docs/` and all collaboration files
- Create `agent-workflow-local/` for project-local shared rules, per-agent rules, and current state
- Create `openspec/explorations/` as the source-of-truth directory
- Create `openspec/explorations/product-scope.md` using the Q1–Q6 answers:

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

---

## Step 6: Begin Exploration

After setup is confirmed complete (all checklist items in `new-project-setup.md` done):

1. Log the transition in your collaboration file as a `status` item: "Setup complete — entering Exploration stage"
2. Begin the domain model exploration with the first question:

   > "Let's start mapping out the domain. What are the main things this project works with — the core objects or concepts a user creates, manages, or interacts with? (For example, in a ride-planning app the core objects are routes, ride plans, and recorded rides.)"

3. Ask follow-up questions **one at a time**, recording confirmed answers directly into `openspec/explorations/domain-model.md` as you go
4. After the domain model is started, move to the next exploration file — ask the user which area to explore next, or suggest the most logical next area based on the answers so far

**Exploration continues until all agents concur the space is proposal-ready and the user has answered all blocking questions. See `workflow/stages.md` for gate criteria.**

---

## Notes

- Never ask more than one question per message throughout this entire flow
- If the user says "I'll handle the GitHub repo myself," skip Step 4 and ask for the repo URL to clone
- If the user already has a brief or existing documents, read them before Step 2 and skip any questions already answered
- If another agent will also be joining the project, complete setup fully before briefing them — they should join a working structure, not a half-initialized one
