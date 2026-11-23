# New Project Setup

Use the same foundation installer for every project, including the repository
that develops the foundation. Keep the user's chosen project folder as root. Use the supplied source path or
repository URL; ask for its location only if unknown. The running agent is setup
lead unless assigned otherwise. Establish missing purpose, users, outcomes, and
platform through `workflow/question-model.md` before implementation choices.
If GitHub creation is requested, connect it to this chosen folder within the
authorized visibility/publication scope; do not relocate the project.

1. Select the foundation source, project name, participating agents, lead, and
   source-of-truth root from supplied context; ask only for missing decisions.
2. From the chosen project folder, run:

   ```sh
   python3 <foundation-root>/scripts/foundation.py init --project . --source SOURCE --project-name NAME --agents codex,claude,gemini --lead codex
   ```

   Use the actual roster and lead, and `--source-root PATH` when the project
   uses a different source-of-truth location. Existing local configuration and
   host text are preserved. The default installed directory is
   `agent-workflow-foundation/`; it contains product source only.
3. Review the generated project facts, local rules, state, host entry files,
   and optional restrictions. Roles and lenses are authoritative in project facts.
4. For a new project, create the initial scope/index from interview answers in
   the recorded source root. For an existing project, inspect the inventory and
   affected files; retain its stage, accepted decisions, and collaboration history.
5. Select candidate capabilities from `third-party/origins.json` for the product
   and follow `workflow/tooling.md` for installation, verification, and local
   inventory. Consider Grill Me for an explicitly requested planning interview;
   its dependency/host adapter is `workflow/grill-me.md`. Freshness review timing
   is defined only in `workflow/tooling-review.md`; setup is not a trigger.
6. Run foundation collaboration lint with `--root . --strict-state`, verify the
   project queues, and log setup completion and any unresolved gaps in the
   current project's own collaboration file.

See `workflow/foundation-lifecycle.md` for source acquisition, compatibility,
customization, update review, conflict handling, and rollback. Existing projects on an
older layout use `workflow/migration.md`; new projects have no legacy startup.
