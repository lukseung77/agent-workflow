# Optional Tooling Operations

Use `third-party/origins.json` as the source directory for third-party tools and
skills. Consult each official origin's current instructions before setup; the
foundation carries no vendored implementations or copied skill prompts.

The selected template identifies requirements; selection is separate from actual
installation. Setup guides missing prerequisites without silently installing or
configuring them. Grill-Me is core; OpenSpec/GitHub are required by the initial
SW template, and MarkItDown by the initial Proposal PT template.

The first-party adapter remains optional:

```sh
python3 <foundation-root>/scripts/agent_workflow_env.py init --root . --foundation-root <foundation-root> --agents auto
python3 <foundation-root>/scripts/agent_workflow_env.py doctor --root . --agents auto
```

Initialization adds only the managed shared-policy pointer, uses available
project integrations, and records tool origins and verified version output in
`agent-workflow-local/tooling.json`. It does not install packages or modify
agent-wide hooks by default. `doctor` performs no writes.

`--install-missing` explicitly enables the supported Graphify/RTK installers.
Graphify resolves its current stable package; RTK selects the highest stable
semantic-version tag from its official Git origin. If a stable release cannot
be resolved, setup warns rather than silently installing a development branch.
Use `--graphify-version VERSION` or `--rtk-revision COMMIT` for a project's
reviewed compatibility selection. Existing installed tools are not silently
upgraded or downgraded. Use current upstream instructions for other registry
capabilities instead of installing the whole catalog.

`--configure-hosts` separately enables supported host integrations. Native
plugins may need interactive host actions; check their official origin and
record what was verified. Adapter commands are convenience integrations and may
need a foundation update when upstream interfaces change. Missing optional
capabilities use ordinary source inspection and CLI execution.

## Diagnostic Meaning

The shared adapter indicator detects a valid managed instruction block, not a
native Ponytail plugin. JSON `tools.ponytail` keeps this adapter meaning for
compatibility. Unrequested agents are not checked; native plugin state remains
unknown until verified through the host. Inventory version values are the last
verified command output; current availability and check time are recorded too.
Existing manually verified plugin metadata is preserved.

Optional commands have bounded timeouts and warning-based failure handling.
Verification runs initially and after actual install/configuration/indexing
commands; the final inventory also obtains RTK's installed version. Normal
workflow operation does not require every optional integration.

## GitHub Repository Setup

For the SW template, inspect the local repository and existing remote before
guiding setup. Confirm the intended account/repository, visibility, and publication
scope when creation or publication is requested. Reuse the available connector,
Git client, or official host workflow; do not require a specific CLI merely to use
GitHub. Verify the actual repository identity and access before recording it as
configured. Record repository/service evidence rather than inventing a package
version. Never store credentials in local inventory. The lead coordinates
authorized publication; template selection alone creates no remote repository
and grants no authority to upload project files.

## OpenSpec Integration

When the consumer selects OpenSpec for specifications and change tracking,
install the official package from the registry origin using its currently
supported Node/package environment. Inspect existing specs and host configuration
before initializing or updating generated integrations; preserve local files.
Verify the actual CLI version and run validation on the project's own specs or
a disposable example before recording it as verified. Use the existing stage
and approval rules; installing OpenSpec does not advance a project stage.
Record version, configuration paths, and validation evidence in local inventory.
If unavailable, maintain the accepted project specification files directly and
report any required CLI check as unavailable. Retiring the CLI must not delete
accepted specifications or change history. Other supported tools are routed by
`workflow/tooling.md`.
