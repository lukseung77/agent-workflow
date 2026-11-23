# Security Integrations

Follow `workflow/tooling.md` and each official origin's current
prerequisites. These integrations have different targets and execution effects.

| Registry ID | Setup and trigger | Representative verification | Fallback / retirement |
|---|---|---|---|
| `security-audit` | Install Cloudflare's selected security-audit skill/resources for source-grounded security review. Use guidance mode for a focused question. Select full audit scope and satisfy upstream sandbox/independent-agent prerequisites before a full audit. | Trace a candidate finding to a real trust boundary and evidence; distinguish confirmed findings, hardening notes, and unresolved validation. Reproduce only within the authorized environment. | Focused source review remains available. Do not claim full-audit coverage when prerequisites or validation are missing. Remove the selected skill while retaining relevant reports as project evidence. |
| `skillspector` | Install the official scanner in its supported Python environment when inspecting new or changed external skill bundles. Choose static or model-backed analysis explicitly; inspect model/network requirements before enabling them. | Scan an inert sample or staged candidate without executing its payload. Record scanner version, mode, reviewed revision, report, and triaged findings. A clean scan is not a safety certificate. | Inspect source and dependencies directly and state scanning was not performed. Remove only the scanner environment/configuration; retain decision evidence as needed. |
| `strix` | Install the official security agent and current runtime/model prerequisites for an explicitly scoped dynamic test. Record authorized targets, permitted actions, environment, exclusions, and finite resource/model limits before execution. | Use a disposable authorized test target to verify operation and findings. Validate impact and fixes with evidence; a patch or agent assertion alone does not prove remediation. | Use source review and ordinary application tests. Stop owned sessions/containers and retire only recorded configuration; preserve required reports. |

SkillSpector examines agent-skill inputs; Cloudflare guidance reviews product
source; Strix performs dynamic testing. Supporting all three does not imply
running all three on every change. Source-review authorization does not authorize
live exploitation or autonomous external agent launches. Record unavailable
prerequisites and continue narrower authorized checks instead of inventing results.
