# Efficiency Integrations

Follow `workflow/tooling.md` and `guides/tooling-operations.md`. These tools
optimize output during any existing stage; neither changes task requirements.

| Registry ID | Setup and trigger | Representative verification | Fallback / retirement |
|---|---|---|---|
| `rtk` | Use compact command output when verbose commands consume context. Install the official Rust Token Killer release/package, verifying identity before adding any host hooks. The existing bootstrap supports explicit installation/configuration opt-ins. | Compare an ordinary command and a failing command with their original outputs. Confirm exit status, actionable errors, and access to complete diagnostics remain available. Record executable version and any hook configuration. | Run original commands. Disable the RTK hook/wrapper before removing the executable. |
| `caveman` | Use when measured response or tool-output cost justifies it. Choose the skill and/or proxy explicitly using current upstream instructions; do not assume installing a skill authorizes a proxy or host endpoint change. | Compare a representative explanation and command failure with originals. Verify exact code, contracts, findings, and diagnostic recovery. For a proxy, verify the actual routing and restore path before relying on it. | Concise ordinary responses and raw output remain available. Restore previous host routing/configuration before stopping or removing the proxy. |

Choose one primary output-compression layer; stacking RTK and a proxy requires
a demonstrated benefit and verification that errors are not lost twice.
Caveman remains a conditional optimization rather than a default response style.
No claimed token saving substitutes for measuring representative project work.
