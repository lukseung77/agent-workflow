# Project Types And Templates

The core handles communication between agents and the user: role boundaries,
questions, decisions, review messages, queues, durable records, and handoffs.
Grill-Me is a core interview capability across all project types, with its
grilling dependency and host adapter in `workflow/grill-me.md`. Core inclusion
does not imply installation, automatic invocation, or an interview at every step.

`templates/project-types.json` is the authoritative project-type/template catalog.
A type groups one or more templates. Each template owns its process, stages,
gates, source-root default, required integrations, handoff approach, and whether
stage transitions trigger tooling reviews. The origin registry owns tool origins
and integration adapters; the catalog selects tool IDs rather than duplicating
their installation instructions.

## Initial Choices

| Project type | Template ID | Process and requirements |
|---|---|---|
| SW Development (`sw-development`) | `openspec-github` | OpenSpec development process and GitHub repository; additional capabilities chosen for actual project needs |
| Proposal PT Making (`proposal-pt-making`) | `chatgpt-claude-manual` | MarkItDown read-in; ChatGPT RFP/TOC/slide planning; user transfers instructions to Claude's PowerPoint plugin; return and review manually |

Ask the project type first and then the template, even when the type currently
has only one template; a single choice may be presented for confirmation. Reuse
an explicit choice already supplied by the user. Do not infer SW Development
merely because a folder is a Git repository, or install tools from every type.

## Local Selection And Guided Setup

Initialization records the selected type/template, required capability IDs,
workflow path, stage names, and guided-installation policy in
`agent-workflow-local/project-template.json`. Project facts link to this record;
installation state retains selection IDs for future template merges. Required
capabilities start unverified. Inspect the existing environment, record actual
results in local tooling inventory, and guide missing installation or host setup.
Template selection alone does not authorize package installation, host changes,
account creation, repository publication, or cross-app automation.

Required manual capabilities with unresolved plugin identities stay explicitly
unverified until the actual plugin and official origin are identified. Do not
pretend a catalog entry is an executable integration. Choose additional optional
tools only for a demonstrated capability gap under `workflow/tooling.md`.

Project-local overrides retain normal precedence. A template update uses the
foundation's conflict-aware merge rather than resetting the selected process or
task state. Switching type/template is a separate scope decision: review artifact
mapping, accepted decisions, prerequisites, and history before changing the local
workflow. There is no automatic switching command in this version.

Existing consumers without selection are marked `legacy-unselected` on update;
their source paths, local process, and prior stage defaults are retained. New
setup requires a valid type/template pair. To add a reusable template, add a
catalog entry and its focused workflow, register any actual new origins, and
validate fresh setup and update behavior. Multiple templates per type need no
change to the core communication model.
