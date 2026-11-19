# New Project Setup

Use the same foundation installer for every project, including the repository
that develops the foundation. Keep the user's chosen project folder as root.

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
5. Select third-party capabilities from `third-party/origins.json`. Use current
   official installers only when authorized. Record verified installed versions
   in local tooling inventory; missing optional tools are not setup blockers.
6. Run foundation collaboration lint with `--root . --strict-state`, verify the
   project queues, and log setup completion and any unresolved gaps in the
   current project's own collaboration file.

See `workflow/foundation-lifecycle.md` for source acquisition, compatibility,
customization, update review, conflict handling, and rollback. Existing legacy
entry wrappers remain usable but new projects need only their host entry files.
