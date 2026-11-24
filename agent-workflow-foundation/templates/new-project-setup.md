# New Project Setup

Keep the user's chosen project folder as root. Use the supplied foundation
source or ask for its location if unknown. The running agent is setup lead
unless assigned otherwise. Establish missing purpose, users, outcomes, and
constraints through `workflow/question-model.md`; core Grill-Me is available
for an explicitly requested deeper interview.

1. Ask for the **project type**, then its **template**, one question at a time.
   Reuse explicit answers already supplied; confirm even a sole template choice.
   Read `workflow/project-templates.md`. List the actual source's choices with:

   ```sh
   python3 <foundation-root>/scripts/foundation.py templates --source SOURCE
   ```

   Initial choices are SW Development / `openspec-github` and Proposal PT Making /
   `chatgpt-claude-manual`. Templates choose process, stages, gates, and tools;
   the communication core and Grill-Me apply to both.
2. Establish project name, actual participating agents, lead, and source root.
   The template defaults to `openspec/` for SW or `proposal/` for Proposal PT.
   From the chosen folder run (replace TYPE, TEMPLATE, and the roster):

   ```sh
   python3 <foundation-root>/scripts/foundation.py init --project . --source SOURCE --project-name NAME --project-type TYPE --template TEMPLATE --agents codex,claude,gemini --lead codex
   ```

   Use `--source-root PATH` for a deliberate source-root override. Missing or
   mismatched type/template choices fail before writes. The agent conducts the
   interview; the CLI records explicit choices without blocking on terminal input.
   Repeating init on an initialized project remains a no-op.
3. Review generated facts, rules, state, host files, and
   `agent-workflow-local/project-template.json`. Follow its workflow path and
   requirements. Create the initial scope/index in the source root from confirmed
   answers. For an existing project, retain its stage, decisions, and history.
4. **Guide capability setup.** Inspect existing capabilities; record selected,
   installed, configured, and verified states separately in local tooling inventory.
   Every template requires Grill-Me and its grilling dependency. The SW template
   additionally requires OpenSpec and a GitHub repository; the Proposal PT template
   requires MarkItDown, ChatGPT planning, and the user's Claude PowerPoint plugin.
   Identify the exact plugin and official origin before guiding its host setup.
   Guide missing installations under `workflow/tooling.md`; selecting a template
   does not install packages, authenticate, configure hosts, or publish a repository.
   Ask for missing visibility/publication decisions only when repository creation
   is actually requested. Record unresolved prerequisites and continue independent
   work. Select additional capabilities only for concrete project needs.
5. Proposal PT uses manual ChatGPT/Claude handoffs and the template's slide-brief
   format, including TOC, titles, key messages, content, and drawing/layout prompts.
   Follow its analysis, planning, production, and final review gates. No cross-app
   automation is configured. SW follows OpenSpec and its own review/transition gates.
6. Run collaboration lint with `--root . --strict-state`, verify queues, and record
   setup completion and unresolved gaps in the project's collaboration file. Template
   stages are loaded automatically; setup is not an online tooling-review trigger.

Use `workflow/foundation-lifecycle.md` for acquisition, updates, and rollback.
Existing pre-foundation layouts use `workflow/migration.md`. Updates and migration
preserve existing workflows; they never silently select a type/template.
