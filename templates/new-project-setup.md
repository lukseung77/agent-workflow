# New Project Setup — File Structure Checklist

This checklist covers the file and directory setup for a new project.
It is called from `project-init.md` after the user interview and repository setup are complete.
Work through it top to bottom. Check off each item before moving to the next.

---

## 1. Confirm Prerequisites

These must be done before this checklist begins (handled in `project-init.md`):

- [ ] Workflow root fetched or copied from `https://github.com/lukseung77/agent-workflow`
- [ ] User interview complete (project title, purpose, primary user, core outcomes, platform, tools)
- [ ] Local repository initialized or existing checkout selected; GitHub remote optional
- [ ] `openspec/explorations/product-scope.md` created from interview answers

---

## 2. Confirm Project Context

- [ ] Identify who the other agents will be (names and roles)
- [ ] Identify who the lead agent is and who the consultants are
- [ ] Optionally assign consultant review lenses, such as fixed-reference/domain or architecture/breadth
- [ ] Confirm source-of-truth root: `openspec/explorations/`

---

## 3. Create The Docs Directory

- [ ] Create `docs/` in the project root if it does not exist
- [ ] Create `agent-workflow-local/` in the project root if it does not exist
- [ ] Create a short `docs/collaboration.md` bootstrap file that points agents to:
  - the chosen workflow root, normally `../agent-workflow/` or `./agent-workflow/`
  - `<workflow-root>/workflow/`
  - `<workflow-root>/skills/`
  - `./agent-workflow-local/`
- [ ] Copy `templates/docs/collaboration-format.md` → `docs/collaboration-format.md`
- [ ] Fill in the agent roles table in `docs/collaboration-format.md`:
  - Agent name
  - Role (lead or consultant)
  - Which files they write to
- [ ] Fill in the source-of-truth root or inventory pointer in `docs/collaboration-format.md`

---

## 4. Create Project-Local Workflow Files

- [ ] Create `agent-workflow-local/agent-workflow.md`
  - project-wide workflow overrides only
- [ ] Copy `templates/project-facts.md` -> `agent-workflow-local/project-facts.md`
  - stable local paths, roles, stage tracking, and source-of-truth inventory
- [ ] Copy `templates/local-rules.md` -> `agent-workflow-local/rules.md`
  - project-specific workflow rules only
- [ ] Create `agent-workflow-local/agent-workflow-[agent].md` for each participating agent
  - project-specific agent role and restrictions only
- [ ] Copy `templates/current-state.md` -> `agent-workflow-local/current-state.md`
  - five-field restart snapshot only
- [ ] Create `agent-workflow-local/references/`
- [ ] Create `agent-workflow-local/references/markitdown/`
- [ ] Copy `templates/reference.md` -> `agent-workflow-local/references/reference.md`
  - reference registry for original files, content hashes, conversion status, and converted Markdown paths
- [ ] Do not copy shared global workflow rules into `agent-workflow-local/`, `docs/`, or other project files; if vendoring is needed, keep the downstream copy contained in `./agent-workflow/`
- [ ] Keep local workflow files short; move large project specifics into focused source-of-truth files

---

## 5. Create Per-Agent Collaboration Files

For each agent (including yourself):

- [ ] Copy `templates/docs/collaboration-agent.md` → `docs/collaboration-[agentname].md`
- [ ] Replace `[Agent Name]` with the actual agent name
- [ ] Replace `[XX]` ID prefix with the agent's assigned prefix (e.g. `CL`, `CX`, `GM`)
- [ ] Confirm `python3 <workflow-root>/scripts/collab_queue.py [agentname]` can generate the active queue
- [ ] If scripts cannot run in the project environment, copy `templates/docs/collaboration-index-agent.md` as a compatibility fallback and keep only active rows
- [ ] Run `python3 <workflow-root>/scripts/collab_lint.py --root . --strict-state`

---

## 6. Set Up Source Of Truth Structure

If starting from scratch (Exploration stage):

- [ ] Create the source-of-truth directory (e.g. `openspec/explorations/` or `spec/`)
- [ ] Create a top-level index or overview file (e.g. `product-scope.md`) with:
  - Project purpose
  - Primary user
  - Core outcomes
  - Map of exploration files (once they exist)
- [ ] Record the active source-of-truth files in `agent-workflow-local/project-facts.md`

If joining mid-project:

- [ ] Read all existing source-of-truth files before writing anything
- [ ] Note any gaps or conflicts in your collaboration file (do not edit source-of-truth yet)

If importing existing source material:

- [ ] Convert bulky or non-Markdown material before agent review when practical
- [ ] Check `agent-workflow-local/references/reference.md` before reading or converting reference files
- [ ] Store converted Markdown in `agent-workflow-local/references/markitdown/`
- [ ] Record source path, source SHA-256, conversion status, converted Markdown path, and converted Markdown SHA-256 in `agent-workflow-local/references/reference.md`
- [ ] Mark `_OLD` files as `obsolete` in the registry when discovered, but do not read or convert them unless the user explicitly asks for old material
- [ ] Summarize decision-relevant content before writing confirmed decisions into source-of-truth files

---

## 7. Log The Setup

In your own collaboration file (`docs/collaboration-[yourname].md`):

- [ ] Add a `status` item confirming the workflow is initialized
- [ ] List the agents, their roles, and their file paths
- [ ] Note the current stage
- [ ] Note any immediate open questions you spotted during setup

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
- [ ] `agent-workflow-local/` exists with project facts, local rules, shared override, per-agent, and current-state files
- [ ] `agent-workflow-local/references/reference.md` and `agent-workflow-local/references/markitdown/` exist
- [ ] `agent-workflow-local/project-facts.md` has stable paths, roles, stage tracking, and source-of-truth inventory filled in
- [ ] `agent-workflow-local/rules.md` contains only project-specific rules or says no local overrides are active
- [ ] `docs/collaboration-format.md` has agent names, roles, and source-of-truth root or inventory pointer filled in
- [ ] `docs/collaboration.md` correctly points to the shared workflow repo and local overrides
- [ ] Large imported documents are linked or summarized rather than pasted into collaboration threads
- [ ] Your own collaboration file has at least one `status` item logged
- [ ] Generated queues work, or active-only compatibility indexes exist
- [ ] Collaboration lint reports zero errors
- [ ] Any immediate gaps or conflicts spotted during setup are logged (not silently fixed)

Success criteria:

- Any agent can join the project, read the bootstrap files, and know where to write.
- The lead agent can begin Exploration without guessing file locations, roles, or source-of-truth ownership.
- No setup rule is duplicated across local project files unless the duplication is intentional and clearly scoped.

---

## Notes

- Do not start writing to source-of-truth files until this checklist is complete.
- The user interview and repository creation happen in `project-init.md` before this checklist runs. Do not repeat those steps here.
- If you are the lead agent, proceed directly to `project-init.md` Step 6 (begin exploration) after this checklist is done.
- If you are a consultant agent doing the setup, notify the lead agent that setup is complete before beginning any review work.
