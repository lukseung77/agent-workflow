# New Project Setup — File Structure Checklist

This checklist covers the file and directory setup for a new project.
It is called from `project-init.md` (Step 5) after the user interview and GitHub repo creation are complete.
Work through it top to bottom. Check off each item before moving to the next.

---

## 1. Confirm Prerequisites

These must be done before this checklist begins (handled in `project-init.md`):

- [ ] Workflow files fetched from `https://github.com/lukseung77/agent-workflow`
- [ ] User interview complete (project title, purpose, primary user, core outcomes, platform, tools)
- [ ] GitHub repo created and cloned locally
- [ ] `openspec/explorations/product-scope.md` created from interview answers

---

## 2. Confirm Project Context

- [ ] Identify who the other agents will be (names and roles)
- [ ] Identify who the lead agent is and who the consultants are
- [ ] Confirm source-of-truth path: `openspec/explorations/`

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

## 5. Set Up Agent Instruction Files

- [ ] Copy `templates/agent-common.md` → project root `agent-common.md`
  - This is the shared rules file all agents read first — no edits needed
- [ ] Copy the instruction file for each agent in the project:
  - Claude: copy `templates/CLAUDE.md` → project root `CLAUDE.md`
  - Codex: copy `templates/CODEX.md` → project root `CODEX.md`
  - Gemini: copy `templates/GEMINI.md` → project root `GEMINI.md`
- [ ] In each agent instruction file, fill in:
  - `[Project Name]`
  - Role (`lead` or `consultant`) — delete the inapplicable definition
  - `[spec/exploration path]` — the source-of-truth location for this project
  - Current stage and one-sentence focus description
  - Any project-specific constraints or guardrails
- [ ] Confirm each file opens with: `Read agent-common.md first.`

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

- Do not start writing to source-of-truth files until this checklist is complete.
- The user interview and GitHub repo creation happen in `project-init.md` before this checklist runs — do not repeat those steps here.
- If you are the lead agent, proceed directly to `project-init.md` Step 6 (begin exploration) after this checklist is done.
- If you are a consultant agent doing the setup, notify the lead agent that setup is complete before beginning any review work.
