from __future__ import annotations

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
FOUNDATION = ROOT / "agent-workflow-foundation"
sys.path.insert(0, str(FOUNDATION / "scripts"))
import foundation
import foundation_migration


class MigrationTest(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name) / "consumer"
        shutil.copytree(ROOT / "tests/fixtures/legacy-agent-workflow", self.root)
        self.context = {"project_name": "Legacy", "foundation_root": "agent-workflow-foundation",
                        "source_root": "specs", "agents": ["codex", "claude"], "lead": "codex",
                        "consultants": "claude", "today": "2026-11-23"}

    def migrate(self, apply=False):
        return foundation_migration.migrate(self.root, FOUNDATION, str(FOUNDATION), self.context, apply)

    def test_preview_is_read_only_and_apply_preserves_state_and_history(self):
        state = (self.root / "agent-workflow-local/current-state.md").read_bytes()
        history = (self.root / "docs/collaboration-codex.md").read_bytes()
        self.assertEqual(self.migrate()["status"], "review")
        self.assertFalse((self.root / foundation.STATE).exists())
        result = self.migrate(True)
        self.assertIn("semantic review required", result["status"])
        self.assertEqual((self.root / "agent-workflow-local/current-state.md").read_bytes(), state)
        self.assertEqual((self.root / "docs/collaboration-codex.md").read_bytes(), history)
        host = (self.root / "AGENTS.md").read_text()
        self.assertNotIn("Read CODEX.md", host)
        self.assertIn("preserve this content", host)
        self.assertIn(foundation.START, host)
        self.assertTrue((self.root / "CODEX.md").exists())
        self.assertIn("Do not publish", (self.root / "agent-workflow-local/rules.md").read_text())
        self.assertFalse(json.loads((self.root / "agent-workflow-local/tooling-reviews.json").read_text())["reviews"])
        lint = subprocess.run([sys.executable, str(FOUNDATION / "scripts/collab_lint.py"),
                               "--root", str(self.root), "--strict-state"], capture_output=True, text=True)
        self.assertEqual(lint.returncode, 0, lint.stdout + lint.stderr)
        self.assertEqual(self.migrate(True)["status"], "already migrated")

    def test_new_project_is_not_misclassified_as_legacy(self):
        shutil.rmtree(self.root)
        self.root.mkdir()
        with self.assertRaises(ValueError):
            self.migrate()
        self.assertFalse((self.root / foundation.STATE).exists())

    def test_existing_overrides_remain_customizations_on_first_update(self):
        self.migrate(True)
        upstream = self.root.parent / "upstream"
        shutil.copytree(FOUNDATION, upstream)
        template = upstream / "templates/agent-workflow-local/rules.md"
        template.write_text(template.read_text() + "\nA new upstream default.\n")
        rules = self.root / "agent-workflow-local/rules.md"
        result = foundation.update(self.root, upstream, str(upstream), apply=True)
        self.assertIn("Do not publish", rules.read_text())
        self.assertIn(result["status"], ("applied", "conflict"))

    def test_symlinked_legacy_content_is_rejected_before_writes(self):
        path = self.root / "CODEX.md"
        path.unlink()
        outside = self.root.parent / "outside.md"
        outside.write_text("private")
        path.symlink_to(outside)
        with self.assertRaises(ValueError):
            self.migrate(True)
        self.assertFalse((self.root / foundation.STATE).exists())
