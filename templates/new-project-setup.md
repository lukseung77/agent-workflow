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

---

## 2. Confirm Project Context

- [ ] Identify who the other agents will be (names and roles)
- [ ] Identify who the lead agent is and who the consultants are
- [ ] Optionally assign consultant review lenses, such as fixed-reference/domain or architecture/breadth
- [ ] Record the source-of-truth root in project facts; default to `openspec/explorations/` for a new project and preserve an existing confirmed root

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
- [ ] Keep this file as a pointer only; record roles, write assignments, and source-of-truth inventory once in project facts

---

## 4. Create Project-Local Workflow Files

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
- [ ] Keep the generated `AGENTS.md` tooling block as a pointer to `<workflow-root>/workflow/agent-tooling.md`; do not copy the shared policy into project-local rules

### Install Agent Entry Files

- [ ] Copy `templates/agent-common.md` to `agent-common.md`, preserving existing project instructions by merging changes rather than overwriting
- [ ] For Codex, install `templates/CODEX.md` as `CODEX.md` and merge a startup pointer into `AGENTS.md`: `Read CODEX.md for project startup and assignment pointers.` Preserve existing instructions and any tooling-managed block
- [ ] For Claude, install or merge `templates/CLAUDE.md` as `CLAUDE.md`
- [ ] For Gemini, install or merge `templates/GEMINI.md` as `GEMINI.md`
- [ ] Replace project name and workflow-root placeholders only for participating agents; verify their entry files reach the chosen workflow root and local assignment files


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
- [ ] Create the initial scope/index file here, using the interview answers and the product-scope template in `templates/project-init.md`, with:
  - Project purpose
  - Primary user
  - Core outcomes
  - Map of exploration files (once they exist)
- [ ] Record the active source-of-truth files in `agent-workflow-local/project-facts.md`

If joining mid-project:

- [ ] Read the source-of-truth inventory and current state, then inspect files affected by the task and their relevant dependencies; expand reading when gaps or cross-file decisions require it
- [ ] Record unresolved gaps or conflicts in your collaboration file; make updates only within your assigned write authority

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

- [ ] Once project files exist, follow `docs/agent-tooling.md` for optional environment initialization and diagnostics; installation and host configuration require their existing explicit opt-ins

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
- [ ] `agent-workflow-local/` exists with project facts, local rules, per-agent assignments, and current-state files; existing legacy shared overrides remain supported
- [ ] `agent-workflow-local/references/reference.md` and `agent-workflow-local/references/markitdown/` exist
- [ ] Any optional environment diagnostics are recorded using the meanings in `docs/agent-tooling.md`; missing optional tools do not block setup
- [ ] `agent-workflow-local/project-facts.md` has stable paths, roles, stage tracking, and source-of-truth inventory filled in
- [ ] `agent-workflow-local/rules.md` contains only project-specific rules or says no local overrides are active
- [ ] `docs/collaboration-format.md` points to the chosen workflow root, and participating agents have working host entry files
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

- Create the initial scope/index during section 6. Begin substantive feature specifications and implementation only after setup is complete.
- The user interview and repository creation happen in `project-init.md` before this checklist runs. Do not repeat those steps here.
- If you are the lead agent, proceed directly to `project-init.md` Step 6 (begin exploration) after this checklist is done.
- If you are a consultant agent doing the setup, notify the lead agent that setup is complete before beginning any review work.
