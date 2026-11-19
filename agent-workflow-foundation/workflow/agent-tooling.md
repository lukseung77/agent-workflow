# Optional Tooling Policy

Origins and installation guidance live in `third-party/origins.json`; no
third-party tool or skill implementation is bundled. Select capabilities for
the current task, resolve current compatible stable releases from their official
origins, verify the result, and record exact versions and configuration in the
consuming project's `agent-workflow-local/tooling.json`.

Project requirements, correctness, security, accessibility, and required checks
always govern tool preferences. An implementation-minimalism helper must not
remove required behavior. A repository graph supplements source inspection;
source wins over a stale graph. Compressed output must retain a diagnostic path
to the original command or log.

Exploration/proposal may benefit from repository discovery. Implementation may
benefit from minimalism guidance and compact output. Validation/review uses only
capabilities relevant to its evidence. These are activities within the existing
three stages, not additional gates or mandatory tool-loading steps.

First-party scripts own thin instruction adapters and diagnostics. Third-party
installers own their skills, hooks, indexes, and host settings. Preserve user
instructions and use official lifecycle commands instead of copying generated
third-party files into the foundation. Package installation and agent-wide
configuration require their explicit opt-ins; missing optional integrations use
normal source inspection and CLI execution with a warning.

Operational commands and compatibility notes are in `docs/agent-tooling.md`.
