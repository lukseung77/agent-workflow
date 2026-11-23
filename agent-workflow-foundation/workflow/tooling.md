# Tooling

This is the canonical capability policy and installation lifecycle. The only
catalog is `third-party/origins.json`: it owns capabilities, origins, fit,
activation triggers, and integration pointers. Registry `defaults` apply unless
an entry overrides them. Support does not mean installed or runtime-verified.

Project requirements, accepted architecture, correctness, security, accessibility,
and required checks govern tool preferences. Source wins over a stale graph.
Compression must preserve access to full diagnostics; minimalism cannot remove
required behavior. Capability activities fit the existing three project stages.

## Capability Routing

| Need | Supported options | Focused integration |
|---|---|---|
| Interview and challenge assumptions | Grill Me and grilling | `workflow/grill-me.md` |
| Implementation discipline and codebase understanding | Ponytail, Graphify, Floorplan, selected ECC and Addy Osmani skills | `guides/integrations/engineering.md` |
| Command and response efficiency | RTK, Caveman | `guides/integrations/efficiency.md` |
| Convert references, retrieve library docs, discover skills | MarkItDown, Context7, Find Skills | `guides/integrations/references.md` |
| Product flow, components, and interface review | Wireflow Review, Astryx, Anti-UI Slop, unslop, Web Design Guidelines, 21st MCP | `guides/integrations/product-ui.md` |
| Browser inspection and repeatable acceptance tests | Agent Browser, Playwright | `guides/integrations/browser.md` |
| Source security review, skill inspection, dynamic testing | Cloudflare Security Audit, SkillSpector, Strix | `guides/integrations/security.md` |
| Host setup, hooks, iteration, and Git convenience | Hookify, Claude Code Setup, Ralph Loop, commit-commands | `guides/integrations/host-automation.md` |
| Team planning and shared knowledge | OpenProject, AppFlowy | `guides/integrations/workspaces.md` |
| Specifications and changes | OpenSpec | `guides/tooling-operations.md`; current official origin |

Only load the focused adapter relevant to the current task. Existing topic
rules, accepted specs, project roles, and local overrides retain precedence.
An engineering collection is a source of selected capabilities, not a second
set of governing workflow instructions.

## Installation Lifecycle

1. During setup or a capability-gap review, select tools for actual product
   needs. Reuse available capabilities and choose a primary tool where roles
   overlap. The adapters explain when an additional tool has a distinct role.
2. Read the selected official origin, current install/license instructions,
   and prerequisites. Inspect source/dependencies, choose a compatible release,
   prefer project scope, and reuse existing installation/host authorization. Do not
   install every supported integration merely because it appears in this list.
3. Install via the current upstream-supported mechanism into the consumer's
   dependency environment or host skill/plugin location, outside foundation
   product source. Preserve existing configuration; record additions precisely.
4. Perform the focused adapter's representative verification. Record origin,
   actual package version/revision or hosted endpoint, host/scope, configuration
   locations without credentials, verification evidence, and disable/uninstall
   steps in `agent-workflow-local/tooling.json`. Keep selected, installed,
   configured, and verified statuses distinct; unknown results stay unknown.
5. Updates require reviewing upstream changes and rerunning affected checks.
   Disable the specific integration and revert only its recorded configuration
   changes when retiring it; inspect local edits and shared dependencies first.
   Do not delete user data, unrelated hooks, or other tools' configuration.

Registry integration pointers identify these adapters. Defaults disable silent
installation; `bootstrap_install_supported` explicitly identifies tools the
environment bootstrap can install when requested.
Existing automated environment setup is limited to Ponytail, Graphify, and RTK;
other integrations use their official installers and the adapters above.
Foundation `init`/`update` distribute this guidance, not external installations.

## Integration Scope

Registry `integration_status: catalog-only` identifies capabilities outside the
supported integration set. Do not select them automatically or indirectly enable
their optional media pipelines through another integration. A future explicit
project request can reopen selection. Keep that decision in the consumer.

## Freshness

Follow `workflow/tooling-review.md` for review triggers and evidence. Tool choice
and installation do not themselves require a separate freshness review.
