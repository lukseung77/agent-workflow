# Agent Workflow

This GitHub repository develops and publishes **agent-workflow-foundation**, or
**foundation**, as its delivered product:
reusable workflow rules, project-local templates, first-party scripts and skills,
and references to third-party origins. This repository is also its first consumer.
Consumers install or export `agent-workflow-foundation/`; the root local instance,
reviews, specifications, and tests support development of that product.

```text
agent-workflow-foundation/       # Product copied or exported to consumers
  workflow/                     # Shared rules and lifecycle guidance
  templates/agent-workflow-local/ # Source of every project's local configuration
  templates/                    # Host entry and collaboration templates
  templates/project-types.json  # Project types and template requirements
  templates/project-types/      # Template-specific workflows and handoff formats
  scripts/                      # First-party lifecycle/collaboration tooling
  skills/                       # First-party skill only
  third-party/origins.json       # Origins, not vendored third-party code
  guides/                       # Reusable operating guidance
agent-workflow-local/           # This project's instantiated and customized instance
docs/                          # This project's collaboration and maintenance history
openspec/                      # This project's product specs and change records
tests/                         # Product acceptance/regression checks
scripts/validate.py             # Repository maintenance validator
```

## Use The Product

Start an agent in the chosen project folder and identify this foundation's local
path or source repository. Follow the foundation's
[`templates/new-project-setup.md`](agent-workflow-foundation/templates/new-project-setup.md).
An agent needs that source location or an installed entry skill; an empty folder
cannot identify the foundation by itself.

Use the actual participating agents and lead. A local source copies current
product files; a Git URL uses committed source. The project folder stays the
project root. Setup copies only the foundation, instantiates its local templates,
and preserves existing configuration and collaboration history.

The core handles agent/user communication and includes Grill-Me. New setup asks
for a project type and template: initially SW Development (OpenSpec and GitHub),
or Proposal PT Making (MarkItDown, ChatGPT planning, and manual handoff to Claude
for PowerPoint production and review). Templates own stages and gates. Setup
guides installations; selecting a template does not silently install or publish.

For updates, review the plan before applying it under the authorized request:

```sh
python3 agent-workflow-foundation/scripts/foundation.py update --project . --source SOURCE
python3 agent-workflow-foundation/scripts/foundation.py update --project . --source SOURCE --apply
```

See the [lifecycle procedure](agent-workflow-foundation/workflow/foundation-lifecycle.md)
for merging customizations and resolving conflicts. Existing projects using the
pre-foundation layout must follow the [migration guide](agent-workflow-foundation/workflow/migration.md);
old startup pointers are not a supported new-project path. Third-party capabilities are
selected from their [origin registry](agent-workflow-foundation/third-party/origins.json),
installed from current official guidance when authorized, and recorded locally.
No third-party tool or skill implementation is bundled in the foundation.

## Develop This Product

This project's roles, local overrides, state, and maintainer authority are in
`agent-workflow-local/`, instantiated using that same installer. Normal startup
begins with the root host entry file and the foundation's rule-precedence guide.
Generic changes belong in product source; project-only decisions remain local.
Review history is retained in `docs/collaboration-archives/` and can be retrieved
with the foundation's collaboration lookup tools.

Run `python3 scripts/validate.py --require-openspec` to validate the product and
this consuming instance. Export only the distributable foundation with:

```sh
python3 agent-workflow-foundation/scripts/foundation.py export --output /tmp/agent-workflow-foundation.zip
```

GitHub can hold the source and this project's development records; exported
consumer packages contain only the foundation. Publication is a separate action.
Change and rollback records are in `docs/change-log.md`.
