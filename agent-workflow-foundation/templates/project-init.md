# Project Initialization

When asked to set up a project with the foundation, treat the user's selected
working folder as the project root. Reuse its repository and files. If a new
GitHub remote is requested, connect it to this folder; do not clone elsewhere
or change the chosen project root. Remote creation, visibility, and publication
follow the user's authorization and known preferences.

The running agent is setup lead unless the user assigns another lead. Record
roles in project facts; use `workflow/role-boundaries.md` for authority.

## Locate The Foundation

Use a source path or Git repository URL provided by the user. A repository
contains its product under `agent-workflow-foundation/`. Copy only that product,
not the source project's local instance, reviews, history, or maintenance rules.
Read `workflow/foundation-lifecycle.md` and follow `templates/new-project-setup.md`.
If the user has not identified a source and no installed foundation is available,
ask for its location rather than assuming an unrelated repository is the source.

## Establish Missing Project Context

Read supplied briefs and existing project facts first. For a new project,
establish name, purpose, primary users, core outcomes, platform, and already
chosen tools. Ask missing decision-changing questions one at a time using
`workflow/question-model.md`; no fixed question count is required. Defer
unsettled implementation choices to the proposal work.

## Instantiate And Begin Work

The installer creates the same local structure for this repository and other
consumers. Populate the initial scope in the chosen source root with purpose,
users, outcomes, platform, and confirmed constraints. Keep project-specific
values in the instance; a general change belongs in foundation product source.
After lint and queue checks, record setup and begin the appropriate stage.
An existing project resumes its current stage without repeating exploration.

Optional tooling setup is described in `docs/agent-tooling.md`. Review its
current origins, select needed capabilities, and preserve installation/host
configuration opt-ins. Foundation setup never silently installs every tool.
