# Workspace Integrations

Use `workflow/tooling.md`. These are team applications, not agent
prompt skills; selection does not require provisioning a server automatically.

| Registry ID | Setup and trigger | Representative verification | Fallback / retirement |
|---|---|---|---|
| `openproject` | Connect an existing team deployment or provision one only when requested, using official hosting/API instructions. Establish task/roadmap ownership and account/service scope. | Read a known project/task through a supported connector or API. For explicitly authorized writes, make a reversible test and verify its result. Record external IDs and the synchronization direction without credentials. | Use the existing Git-backed records. Disconnect the selected connector; do not delete projects, tasks, or the deployment as a configuration cleanup. |
| `appflowy` | Connect the team's selected workspace using current official deployment and supported integration mechanisms. Check actual API/connector availability before claiming automated sync exists. | Read a known document, verify identity and ownership, and test only authorized reversible edits. Record workspace/page mappings and synchronization limitations. | Use project files and links; manual linking is valid if no suitable connector is available. Disconnect configuration without deleting user content. |

Before synchronizing, record canonical ownership for requirements, tasks,
decisions, and documents in project facts/local rules. Define conflict handling,
direction, and refresh behavior. External team planning may be authoritative
for assigned records, while foundation collaboration queues remain agent-message
lifecycle records; do not silently mirror them into competing task queues.
Use connector capabilities when sufficient and verify them before resorting to
browser automation. No connector, credentials, server, or sync daemon is bundled.
