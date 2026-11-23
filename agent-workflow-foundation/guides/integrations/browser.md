# Browser Integrations

Use `workflow/tooling.md` for installation and inventory. These
capabilities support product validation within the existing stages.

| Registry ID | Setup and trigger | Representative verification | Fallback / retirement |
|---|---|---|---|
| `agent-browser` | Install the official CLI and required browser runtime when interactive inspection needs a driver beyond the host's available browser tool. Check current OS/runtime support and session handling. | Open a local test page, inspect state, perform a reversible interaction, and verify the resulting state. Record CLI/browser versions and driver configuration without cookies or credentials. | Use the available host browser. Close owned sessions and remove only its configuration/runtime when no other integration needs them. |
| `playwright` | Add the supported test package to the web application's development environment and install the required browsers/system dependencies from official instructions. Reuse existing configuration. | Run a meaningful critical user journey with assertions, including an error/recovery path where material. Verify the configured browsers locally and in CI; retain useful traces for failures. Record versions and actual test command/results. | Use another established acceptance-test framework or document a manual check when automation is unavailable. Remove only owned tests/configuration and unneeded packages. |

Prefer the existing host driver for exploratory interaction and Playwright for
repeatable regression tests. Both may be selected for these distinct roles;
installing two interactive drivers alone adds no coverage. Use test accounts and
the selected target environment; browser availability does not authorize live
submissions, publication, or unrelated account changes. Tests must assert product
behavior rather than merely prove that a screenshot can be taken.
