from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "agent-workflow-foundation"
sys.path.insert(0, str(FOUNDATION / "scripts"))
import foundation as lifecycle


class FoundationLifecycleTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "upstream/agent-workflow-foundation"
        shutil.copytree(FOUNDATION, self.source, ignore=shutil.ignore_patterns("__pycache__"))
        self.project = self.root / "consumer"
        self.context = {
            "project_name": "Consumer", "foundation_root": "agent-workflow-foundation",
            "source_root": "spec", "agents": ["codex", "claude"], "lead": "codex",
            "consultants": "claude", "today": "2026-11-19",
        }

    def install(self):
        return lifecycle.initialize(self.project, self.source, str(self.source), self.context)

    def installed(self, name):
        return self.project / "agent-workflow-foundation" / name

    def test_init_preserves_host_and_project_customizations_and_is_idempotent(self):
        local = self.project / "agent-workflow-local"
        local.mkdir(parents=True)
        (local / "rules.md").write_text("My custom project rules\n")
        (self.project / "AGENTS.md").write_text("Preserve host instructions\n")
        self.install()
        self.assertEqual((local / "rules.md").read_text(), "My custom project rules\n")
        self.assertIn("Preserve host instructions", (self.project / "AGENTS.md").read_text())
        self.assertIn("Lead: codex", (local / "project-facts.md").read_text())
        before = (self.project / lifecycle.STATE).read_bytes()
        self.assertEqual(self.install()["status"], "already initialized")
        self.assertEqual((self.project / lifecycle.STATE).read_bytes(), before)
        self.assertEqual((self.project / "AGENTS.md").read_text().count(lifecycle.START), 1)

    def test_repository_source_copies_only_foundation_and_export_excludes_consumer_state(self):
        (self.source.parent / "private-state.md").write_text("Not distributable\n")
        with lifecycle.source_tree(str(self.source.parent), self.root) as source:
            lifecycle.initialize(self.project, source, str(self.source.parent), self.context)
        self.assertFalse(self.installed("private-state.md").exists())
        self.assertFalse(self.installed("agent-workflow-local").exists())
        output = self.root / "foundation.zip"
        result = subprocess.run([sys.executable, str(FOUNDATION / "scripts/foundation.py"), "export", "--source", str(self.source.parent), "--output", str(output)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        with zipfile.ZipFile(output) as archive:
            names = archive.namelist()
        self.assertIn("agent-workflow-foundation/templates/agent-workflow-local/rules.md", names)
        self.assertFalse(any("private-state" in name or name.endswith("foundation-state.json") for name in names))

    def test_review_is_read_only_and_apply_updates_product_without_resetting_state(self):
        self.install()
        state = self.project / "agent-workflow-local/current-state.md"
        state.write_text(state.read_text().replace("Setup", "Implementation"))
        source = self.source / "workflow/agent-workflow.md"
        source.write_text(source.read_text() + "\nNew shared rule.\n")
        before = (self.project / lifecycle.STATE).read_bytes()
        plan = lifecycle.update(self.project, self.source, str(self.source))
        self.assertEqual(plan["status"], "review")
        self.assertNotIn("New shared rule.", self.installed("workflow/agent-workflow.md").read_text())
        self.assertEqual((self.project / lifecycle.STATE).read_bytes(), before)
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True)
        self.assertEqual(result["status"], "applied")
        self.assertIn("New shared rule.", self.installed("workflow/agent-workflow.md").read_text())
        self.assertIn("Implementation", state.read_text())

    def test_template_update_three_way_merges_non_overlapping_customizations(self):
        template = self.source / "templates/agent-workflow-local/rules.md"
        template.write_text("\n".join(f"Rule {number}" for number in range(30)) + "\n")
        self.install()
        local = self.project / "agent-workflow-local/rules.md"
        local.write_text(local.read_text().replace("Rule 2\n", "Local customized rule 2\n"))
        template.write_text(template.read_text().replace("Rule 26\n", "New shared rule 26\n"))
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True)
        self.assertEqual(result["status"], "applied", result)
        self.assertIn("Local customized rule 2", local.read_text())
        self.assertIn("New shared rule 26", local.read_text())

    def test_product_conflict_prevents_all_writes(self):
        self.install()
        target = self.installed("workflow/agent-workflow.md")
        target.write_text("Locally customized product\n")
        (self.source / "workflow/agent-workflow.md").write_text("Different upstream product\n")
        (self.source / "workflow/new-rule.md").write_text("New rule\n")
        before = (self.project / lifecycle.STATE).read_bytes()
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True)
        self.assertIn("foundation/workflow/agent-workflow.md", result["conflicts"])
        self.assertEqual(target.read_text(), "Locally customized product\n")
        self.assertFalse(self.installed("workflow/new-rule.md").exists())
        self.assertEqual((self.project / lifecycle.STATE).read_bytes(), before)

    def test_host_template_update_preserves_existing_user_instructions(self):
        self.project.mkdir()
        host = self.project / 'AGENTS.md'
        host.write_text('Personal instructions outside the managed block.\n')
        self.install()
        template = self.source / 'templates/CODEX.md'
        template.write_text(template.read_text() + '\nNew shared host guidance.\n')
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True)
        self.assertEqual(result['status'], 'applied', result)
        self.assertIn('Personal instructions outside the managed block.', host.read_text())
        self.assertIn('New shared host guidance.', host.read_text())
        self.assertEqual(host.read_text().count(lifecycle.START), 1)

    def test_template_conflict_can_be_reviewed_and_explicitly_retained(self):
        self.install()
        template = self.source / "templates/agent-workflow-local/rules.md"
        local = self.project / "agent-workflow-local/rules.md"
        local.write_text(local.read_text().replace("No local overrides are active.", "Local behavior."))
        template.write_text(template.read_text().replace("No local overrides are active.", "Different incoming behavior."))
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True)
        key = "project/agent-workflow-local/rules.md"
        self.assertIn(key, result["conflicts"])
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True, keep_local=(key,))
        self.assertEqual(result["status"], "applied")
        self.assertIn("Local behavior.", local.read_text())
        self.assertEqual(lifecycle.update(self.project, self.source, str(self.source))["conflicts"], [])

    def test_upstream_deletion_removes_only_unchanged_product_files(self):
        (self.source / "workflow/remove.md").write_text("Original\n")
        (self.source / "workflow/keep.md").write_text("Original\n")
        self.install()
        self.installed("workflow/keep.md").write_text("User customization\n")
        (self.source / "workflow/remove.md").unlink()
        (self.source / "workflow/keep.md").unlink()
        blocked = lifecycle.update(self.project, self.source, str(self.source), apply=True)
        self.assertIn("foundation/workflow/keep.md", blocked["conflicts"])
        self.assertTrue(self.installed("workflow/remove.md").exists())
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True, keep_local=("foundation/workflow/keep.md",))
        self.assertEqual(result["status"], "applied")
        self.assertFalse(self.installed("workflow/remove.md").exists())
        self.assertEqual(self.installed("workflow/keep.md").read_text(), "User customization\n")

    def test_foundation_repository_uses_same_installer_in_place(self):
        self.project = self.source.parent
        self.install()
        facts = (self.project / "agent-workflow-local/project-facts.md").read_text()
        self.assertIn("Consumer", facts)
        self.assertEqual(json.loads((self.project / lifecycle.STATE).read_text())["source"], "agent-workflow-foundation")
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True)
        self.assertEqual(result["status"], "applied")

    def test_escaping_and_symlink_destinations_are_rejected_before_writes(self):
        self.context["foundation_root"] = "../outside"
        with self.assertRaises(ValueError):
            self.install()
        self.assertFalse((self.project / "AGENTS.md").exists())
        self.context["foundation_root"] = "agent-workflow-foundation"
        self.project.mkdir()
        (self.project / "agent-workflow-foundation").symlink_to(self.source)
        with self.assertRaises(ValueError):
            self.install()
        self.assertFalse((self.project / lifecycle.STATE).exists())

    def test_cli_initialization_records_a_reusable_local_source(self):
        result = subprocess.run([sys.executable, str(FOUNDATION / "scripts/foundation.py"), "init", "--project", str(self.project), "--source", str(self.source.parent), "--project-name", "CLI project", "--agents", "codex", "--project-type", "sw-development", "--template", "openspec-github"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("CLI project", (self.project / "AGENTS.md").read_text())
        self.assertEqual(json.loads((self.project / lifecycle.STATE).read_text())["source"], str(self.source.resolve()))

    def cli(self, *args):
        return subprocess.run([sys.executable, "-B", str(FOUNDATION / "scripts/foundation.py"),
                               *args, "--source", str(self.source), "--project", str(self.project)],
                              capture_output=True, text=True)

    def test_missing_or_mismatched_selection_fails_without_writes(self):
        for args in ((), ("--project-type", "sw-development"),
                     ("--project-type", "sw-development", "--template", "chatgpt-claude-manual"),
                     ("--project-type", "unknown", "--template", "openspec-github")):
            with self.subTest(args=args):
                result = self.cli("init", *args)
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertFalse(self.project.exists())

    def test_each_template_records_its_process_and_unverified_requirements(self):
        for kind, template, source_root, requirements in (
            ("sw-development", "openspec-github", "openspec", {"grill-me", "openspec", "github"}),
            ("proposal-pt-making", "chatgpt-claude-manual", "proposal", {"grill-me", "markitdown"}),
        ):
            with self.subTest(kind=kind):
                self.project = self.root / kind
                result = self.cli("init", "--project-type", kind, "--template", template)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                profile = json.loads((self.project / "agent-workflow-local/project-template.json").read_text())
                self.assertEqual(profile["source_root"], source_root)
                self.assertEqual(set(profile["required_tools"]), requirements)
                self.assertEqual(profile["installation"], "guided")
                self.assertEqual(profile["capability_status"], "not-verified")
                self.assertTrue((self.project / profile["workflow"]).exists())
                facts = (self.project / "agent-workflow-local/project-facts.md").read_text()
                self.assertIn(template, facts)
                self.assertNotIn("{{", facts)
                self.assertFalse((self.project / source_root).exists())  # No external tool bootstrap.
                before = (self.project / lifecycle.STATE).read_bytes()
                self.assertEqual(self.cli("init").returncode, 0)
                self.assertEqual((self.project / lifecycle.STATE).read_bytes(), before)

    def test_proposal_stages_validate_and_sw_stages_are_rejected(self):
        result = self.cli("init", "--project-type", "proposal-pt-making", "--template", "chatgpt-claude-manual")
        self.assertEqual(result.returncode, 0, result.stdout)
        state = self.project / "agent-workflow-local/current-state.md"
        original = state.read_text()
        for stage, expected in (("RFP Analysis", 0), ("TOC Planning", 0), ("Slide Creation", 0),
                                ("Final Review", 0), ("Implementation", 1)):
            state.write_text(original.replace("Setup", stage))
            lint = subprocess.run([sys.executable, "-B", str(FOUNDATION / "scripts/collab_lint.py"),
                                   "--root", str(self.project), "--strict-state"], capture_output=True, text=True)
            self.assertEqual(lint.returncode, expected, lint.stdout + lint.stderr)

    def test_update_old_consumer_adds_compatibility_record_without_choosing_type(self):
        self.install()
        # Model an installation made before template selection was introduced.
        state_path = self.project / lifecycle.STATE
        state = json.loads(state_path.read_text())
        state["project_bases"].pop("agent-workflow-local/project-template.json")
        (self.project / "agent-workflow-local/project-template.json").unlink()
        state_path.write_text(json.dumps(state))
        local_state = self.project / "agent-workflow-local/current-state.md"
        local_state.write_text(local_state.read_text().replace("Setup", "Implementation"))
        before = local_state.read_bytes()
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True)
        self.assertEqual(result["status"], "applied", result)
        profile = json.loads((self.project / "agent-workflow-local/project-template.json").read_text())
        self.assertEqual(profile["status"], "legacy-unselected")
        self.assertIsNone(profile["project_type"])
        self.assertEqual(profile["source_root"], "spec")
        self.assertEqual(local_state.read_bytes(), before)

    def test_multiple_templates_and_explicit_source_root_survive_update(self):
        path = self.source / "templates/project-types.json"
        data = json.loads(path.read_text())
        templates = data["project_types"]["sw-development"]["templates"]
        templates["second-template"] = {**templates["openspec-github"], "name": "Second SW choice"}
        path.write_text(json.dumps(data))
        result = self.cli("init", "--project-type", "sw-development", "--template", "second-template", "--source-root", "custom-spec")
        self.assertEqual(result.returncode, 0, result.stdout)
        templates["second-template"]["stages"].append("Delivery")
        path.write_text(json.dumps(data))
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True)
        self.assertEqual(result["status"], "applied", result)
        profile = json.loads((self.project / "agent-workflow-local/project-template.json").read_text())
        self.assertEqual(profile["template_id"], "second-template")
        self.assertEqual(profile["source_root"], "custom-spec")
        self.assertIn("Delivery", profile["stages"])

    def test_selection_customization_conflict_keeps_all_update_files_unchanged(self):
        result = self.cli("init", "--project-type", "proposal-pt-making", "--template", "chatgpt-claude-manual")
        self.assertEqual(result.returncode, 0, result.stdout)
        local = self.project / "agent-workflow-local/project-template.json"
        profile = json.loads(local.read_text())
        profile["handoff"] = "local-custom-handoff"
        local.write_text(json.dumps(profile, indent=2) + "\n")
        catalog_path = self.source / "templates/project-types.json"
        data = json.loads(catalog_path.read_text())
        data["project_types"]["proposal-pt-making"]["templates"]["chatgpt-claude-manual"]["handoff"] = "different-upstream-handoff"
        catalog_path.write_text(json.dumps(data))
        before = (self.project / lifecycle.STATE).read_bytes()
        result = lifecycle.update(self.project, self.source, str(self.source), apply=True)
        self.assertIn("project/agent-workflow-local/project-template.json", result["conflicts"])
        self.assertEqual((self.project / lifecycle.STATE).read_bytes(), before)
        self.assertEqual(json.loads(local.read_text())["handoff"], "local-custom-handoff")


if __name__ == "__main__":
    unittest.main()
