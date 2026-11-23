# Host Automation Integrations

Follow `workflow/tooling.md`. These four registry entries are Claude
Code plugins from anthropics/claude-plugins-official; install selected plugins
through the current official marketplace with explicit scope, preserving settings.
Do not copy their hook or slash-command formats into another host speculatively.

| Registry ID | Trigger and setup choices | Representative verification | Fallback / retirement |
|---|---|---|---|
| `hookify` | A repeated concrete behavior benefits from a hook. Review the generated event, pattern, action, and affected scope before enabling it. | Test both a matching and a legitimate nonmatching action on disposable fixtures. Verify warnings/blocking and how to disable the rule without disabling unrelated hooks. | Use project instructions or a deterministic repository check. Disable the specific rule before uninstalling the plugin. |
| `claude-code-setup` | A project needs tailored Claude automation recommendations. Treat its read-only analysis separately from applying suggested configuration. | Verify recommendations reference actual project needs and available host capabilities. Inspect and apply selected changes within existing authorization, recording each separately. | Foundation setup covers startup and roles. Codex/agy use their current native facilities and supported skills; do not invent equivalent plugin names or claim host configuration was performed. |
| `ralph-loop` | A bounded implementation task has objective completion checks and genuinely needs repeated repair. Set finite iteration, elapsed-time, and cost bounds plus cancellation/stagnation handling before starting. | Exercise a small disposable task; verify completion through actual checks and verify cancellation/limit behavior. Record the bounds and loop state. Never accept a completion phrase alone as evidence. | Ordinary bounded agent iteration. Cancel the loop and remove its recorded stop hook/state before retiring the plugin; do not adopt an unlimited default. |
| `commit-commands` | A Claude user requests Git workflow convenience. Inspect the chosen command's effects and repository state before invocation. | Check the intended diff, staging scope, branch, and resulting commit when authorized. Push/PR creation and branch/worktree cleanup have separate effects; perform and verify them only within their authorized scope. | Native git/gh. Remove the plugin without changing Git history or deleting worktrees as an uninstall side effect. |

Current native host documentation governs capability/format compatibility.
No hook can bypass project authority or sandbox permissions. Installing a setup
recommender or Git command collection does not authorize every action it offers.
