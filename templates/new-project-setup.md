# New Project Setup — First Agent Todo

This checklist is for the first agent joining a new project using this workflow.
Work through it top to bottom. Check off each item before moving to the next.

---

## 1. Understand The Workflow

- [ ] Read `workflow/README.md` (overview, concepts, anti-patterns)
- [ ] Read `workflow/collaboration-format.md` (message format and rules)
- [ ] Read `workflow/stages.md` (stage progression and gate criteria)
- [ ] Read `workflow/decision-protocol.md` (when to escalate, how to handle conflicts)

---

## 2. Understand The Project

- [ ] Read any existing project brief, PRD, or background documents
- [ ] Identify the current stage: Exploration / Proposal / Implementation
- [ ] Identify who the other agents will be (names and roles)
- [ ] Identify where the source of truth will live (spec path, exploration path, etc.)
- [ ] Identify who the lead agent is and who the consultants are

---

## 3. Create The Docs Directory

- [ ] Create `docs/` in the project root if it does not exist
- [ ] Copy `templates/docs/collaboration-format.md` → `docs/collaboration-format.md`
- [ ] Fill in the agent roles table in `docs/collaboration-format.md`:
  - Agent name
  - Role (lead or consultant)
  - Which files they write to
- [ ] Fill in the source-of-truth path in `docs/collaboration-format.md`

---

## 4. Create Per-Agent Collaboration Files

For each agent (including yourself):

- [ ] Copy `templates/docs/collaboration-agent.md` → `docs/collaboration-[agentname].md`
- [ ] Replace `[Agent Name]` with the actual agent name
- [ ] Replace `[XX]` ID prefix with the agent's assigned prefix (e.g. `CL`, `CX`, `GM`)
- [ ] Copy `templates/docs/collaboration-index-agent.md` → `docs/collaboration-index-[agentname].md`
- [ ] Replace `[Agent Name]` and `[agent]` with the actual agent name
- [ ] Replace `[source-of-truth path]` with the actual path

---

## 5. Set Up CLAUDE.md

- [ ] Copy `templates/CLAUDE.md` → project root `CLAUDE.md` (or merge into existing)
- [ ] Fill in `[Project Name]`
- [ ] Fill in your role (lead or consultant)
- [ ] Fill in the read-order file list (adjust paths for this project)
- [ ] Fill in your ID prefix
- [ ] Fill in the current stage and a one-sentence description of the current focus
- [ ] Fill in the source-of-truth path
- [ ] Add any project-specific constraints or guardrails

---

## 6. Set Up Source Of Truth Structure

If starting from scratch (Exploration stage):

- [ ] Create the source-of-truth directory (e.g. `openspec/explorations/` or `spec/`)
- [ ] Create a top-level index or overview file (e.g. `product-scope.md`) with:
  - Project purpose
  - Primary user
  - Core outcomes
  - Map of exploration files (once they exist)

If joining mid-project:

- [ ] Read all existing source-of-truth files before writing anything
- [ ] Note any gaps or conflicts in your collaboration file (do not edit source-of-truth yet)

---

## 7. Log The Setup

In your own collaboration file (`docs/collaboration-[yourname].md`):

- [ ] Add a `status` item confirming the workflow is initialized
- [ ] List the agents, their roles, and their file paths
- [ ] Note the current stage
- [ ] Note any immediate open questions you spotted during setup
- [ ] Update your index file with this first item

---

## 8. Brief Other Agents

Write a short onboarding note in your collaboration file addressed `to: all` that tells other agents:

- [ ] Which files to read first when they join
- [ ] What stage the project is in
- [ ] What their role is
- [ ] What is currently open or blocked

---

## 9. Confirm Readiness

Before considering setup complete:

- [ ] All collaboration files exist and are named correctly
- [ ] `docs/collaboration-format.md` has agent names, roles, and source-of-truth path filled in
- [ ] `CLAUDE.md` is complete and correct for this project
- [ ] Your own collaboration file has at least one `status` item logged
- [ ] Your index file is up to date
- [ ] Any immediate gaps or conflicts spotted during setup are logged (not silently fixed)

---

## Notes

- Do not start writing to source-of-truth files until setup is complete.
- Do not ask the user questions during setup unless a critical piece of information (like the lead agent identity) is genuinely unknown.
- If you are both setting up the workflow and also the lead agent, you may begin Exploration work immediately after step 9.
- If you are a consultant agent doing the setup, notify the lead agent that setup is complete before beginning any review work.
