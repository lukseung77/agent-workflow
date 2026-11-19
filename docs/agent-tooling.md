# Agent Tooling Operations

`workflow/agent-tooling.md` is the policy source of truth. This page records
the operational setup and compatibility details.

## Install and verify

Run the safe project pass first:

```sh
python3 <workflow-root>/scripts/agent_workflow_env.py init --root . --workflow-root <workflow-root> --agents auto
python3 <workflow-root>/scripts/agent_workflow_env.py doctor --root . --agents auto
```

With explicit approval for package and host changes, rerun:

```sh
python3 <workflow-root>/scripts/agent_workflow_env.py init \
  --root . --workflow-root <workflow-root> --agents codex,claude,agy,antigravity \
  --install-missing --configure-hosts
```

The bootstrap uses `uv tool install graphifyy` (or `pipx install graphifyy`),
`cargo install --git https://github.com/rtk-ai/rtk`, and the upstream agent
commands documented by each tool. It does not pipe a remote script into a
shell. Ponytail's Claude Code install remains interactive because its official
interface is the two `/plugin` prompts; the bootstrap reports that limitation.

Default installation follows upstream releases. To select previously tested
versions, add `--graphify-version VERSION --rtk-revision COMMIT` together with
`--install-missing`. These selectors affect missing tools only; they do not
upgrade or downgrade an installed tool. After testing a new version, record it
in the project's tool inventory before updating those selectors. The repository
does not claim an untested default pin.

Optional commands have a five-minute timeout. An OS error, timeout, or nonzero
exit becomes a warning so independent integrations can continue.

## Diagnostic meaning

`doctor` inspects the selected environment without writing project files.
Unrequested agents display `not checked`; selected missing agents display `!`.
The shared adapter indicator checks the managed instruction block, while the
native Ponytail plugin is reported as unknown. The JSON `tools.ponytail` key
is retained for compatibility and means shared adapter presence, not plugin
installation. Missing optional tools do not change the command's success exit
code; invalid arguments or unreadable configuration return a nonzero exit code.

Reinitialization refreshes the workflow pointer inside the managed `AGENTS.md`
block while preserving surrounding user text. Malformed markers are rejected
without rewriting the file. Correct the block deliberately, then rerun.

A project-local `RTK.md` does not establish that global agent hooks are installed.
With `--configure-hosts`, the upstream RTK CLI still handles requested global
configuration. Antigravity's existing project-scoped adapter can be reused.

## Compatibility

| Tool | Codex | Claude Code | agy / Antigravity |
|---|---|---|---|
| Ponytail | Native Codex plugin when explicitly configured; shared `AGENTS.md` fallback | Native Claude Code plugin; install uses official interactive `/plugin` prompts | `agy` can use the Gemini extension; Antigravity uses the shared `AGENTS.md` instruction adapter |
| Graphify | Project skill via `graphify install --project --platform codex`; `$graphify` discovery | Project skill via `graphify install --project`; Claude adapter | Gemini adapter for `agy`; `graphify antigravity install` for Antigravity |
| RTK | `rtk init --global --codex` hook/instructions when explicitly configured | `rtk init --global` PreToolUse hook when explicitly configured | `rtk init --global --gemini` for `agy`; `rtk init --agent antigravity` project adapter |

“Native” means the upstream host hook/plugin is used. “Instruction adapter”
means the shared workflow rule is exposed through a file the agent already
reads. A missing or unsupported native integration falls back to the shared
policy and normal CLI behavior.

## Graphify lifecycle

The first successful initialization runs `graphify .`. If
`graphify-out/graph.json` already exists, later runs use `graphify update .`.
Use that incremental command after a substantial refactor; do not rebuild for
every trivial edit. If automatic refresh is desired, enable Graphify's own
commit hook through its documented CLI after reviewing the repository's hook
policy.

## Troubleshooting

- `Graphify is missing`: install `graphifyy` with `uv` or `pipx`, ensure the CLI is on `PATH`, and rerun `init`.
- `RTK verification` fails: confirm this is Rust Token Killer with `rtk gain`; a different crates.io project also uses the `rtk` name.
- A compressed RTK result is not enough: rerun the underlying command without compression or inspect the full log.
- Ponytail is unavailable: use the shared YAGNI/reuse ladder in `workflow/agent-tooling.md`.
- An agent is not detected: pass it explicitly with `--agents codex,claude,agy,antigravity`; unsupported integrations are warnings.
- Existing `AGENTS.md` content is preserved. Remove only the marked adapter block if the project no longer uses agent-workflow.

## Upstream references

- [Ponytail](https://github.com/DietrichGebert/ponytail)
- [Graphify](https://github.com/Graphify-Labs/graphify)
- [RTK installation](https://github.com/rtk-ai/rtk/blob/develop/INSTALL.md) and [supported agents](https://github.com/rtk-ai/rtk/blob/develop/README.md)
