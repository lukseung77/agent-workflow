from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CollaborationToolsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.project = Path(self.temp.name)
        (self.project / "docs").mkdir()
        (self.project / "docs" / "collaboration-codex.md").write_text(
            """# Collaboration: Codex

## Active

### [CX-001] Review draft
- `date`: 2026-06-07
- `created_at`: 2026-06-07T10:00:00+09:00
- `from`: codex
- `to`: gemini
- `type`: review-request
- `status`: open
- `request`: Review the draft.
- `refs`: spec.md

### [CX-002] Broadcast
- `date`: 2026-06-07
- `from`: codex
- `to`: all
- `type`: status
- `status`: active

### [CX-003] Older reminder
- `date`: 2026-06-06
- `from`: codex
- `to`: gemini
- `type`: question
- `status`: open
""",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_script(self, name: str, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python3", str(ROOT / "scripts" / name), *args, "--root", str(self.project)],
            text=True,
            capture_output=True,
            check=False,
        )

    def test_queue_filters_recipient_and_sender(self) -> None:
        gemini = self.run_script("collab_queue.py", "gemini")
        self.assertEqual(gemini.returncode, 0)
        self.assertIn("CX-001", gemini.stdout)
        self.assertIn("CX-002", gemini.stdout)
        self.assertLess(gemini.stdout.index("CX-001"), gemini.stdout.index("CX-003"))

        codex = self.run_script("collab_queue.py", "codex")
        self.assertEqual(codex.returncode, 0)
        self.assertNotIn("CX-002", codex.stdout)

    def test_selected_json_item(self) -> None:
        result = self.run_script("collab_queue.py", "gemini", "--id", "cx-001", "--json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["id"], "CX-001")

    def test_lint_accepts_current_schema(self) -> None:
        result = self.run_script("collab_lint.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_lint_rejects_timezone_free_timestamp(self) -> None:
        path = self.project / "docs" / "collaboration-codex.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "2026-06-07T10:00:00+09:00", "2026-06-07T10:00:00"
            ),
            encoding="utf-8",
        )
        result = self.run_script("collab_lint.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("must include Z or a UTC offset", result.stdout)

    def test_strict_restart_snapshot(self) -> None:
        state_dir = self.project / "agent-workflow-local"
        state_dir.mkdir()
        (self.project / "spec.md").write_text("# Spec\n", encoding="utf-8")
        (state_dir / "current-state.md").write_text(
            """# Current State

- `updated`: 2026-06-07
- `current_stage`: Proposal
- `current_artifact`: spec.md
- `next_lead_action`: Review the proposal.
- `active_blockers`: None
""",
            encoding="utf-8",
        )
        result = self.run_script("collab_lint.py", "--strict-state")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_strict_restart_snapshot_rejects_unknown_stage(self) -> None:
        state_dir = self.project / "agent-workflow-local"
        state_dir.mkdir()
        (state_dir / "current-state.md").write_text(
            """# Current State

- `updated`: 2026-06-07
- `current_stage`: Custom
- `current_artifact`: None
- `next_lead_action`: Continue.
- `active_blockers`: None
""",
            encoding="utf-8",
        )
        result = self.run_script("collab_lint.py", "--strict-state")
        self.assertEqual(result.returncode, 1)
        self.assertIn("is not allowed", result.stdout)

    def test_archive_dry_run_reports_threshold_match(self) -> None:
        path = self.project / "docs" / "collaboration-codex.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "- `status`: active", "- `status`: done"
            ),
            encoding="utf-8",
        )
        result = self.run_script(
            "collab_archive.py", "--threshold-bytes", "1", "--dry-run"
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("collaboration-archives", result.stdout)

    def test_lint_detects_duplicate_id(self) -> None:
        path = self.project / "docs" / "collaboration-codex.md"
        content = path.read_text(encoding="utf-8")
        path.write_text(
            content
            + "\n### [CX-001] Duplicate\n"
            + "- `date`: 2026-06-07\n"
            + "- `from`: codex\n"
            + "- `to`: gemini\n"
            + "- `type`: question\n"
            + "- `status`: open\n",
            encoding="utf-8",
        )
        result = self.run_script("collab_lint.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate", result.stdout)

    def test_lint_detects_invalid_type(self) -> None:
        path = self.project / "docs" / "collaboration-codex.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "- `type`: review-request", "- `type`: bogus-type"
            ),
            encoding="utf-8",
        )
        result = self.run_script("collab_lint.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid type", result.stdout)

    def test_lint_detects_invalid_status(self) -> None:
        path = self.project / "docs" / "collaboration-codex.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "- `status`: open\n- `request`:", "- `status`: bogus\n- `request`:"
            ),
            encoding="utf-8",
        )
        result = self.run_script("collab_lint.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("invalid status", result.stdout)

    def test_lint_detects_missing_required_field(self) -> None:
        path = self.project / "docs" / "collaboration-codex.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "- `from`: codex\n- `to`: gemini\n- `type`: review-request\n",
                "- `to`: gemini\n- `type`: review-request\n",
            ),
            encoding="utf-8",
        )
        result = self.run_script("collab_lint.py")
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing fields", result.stdout)

    def test_lint_treats_legacy_status_as_warning_not_error(self) -> None:
        path = self.project / "docs" / "collaboration-codex.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "- `status`: open\n- `request`:", "- `status`: accepted\n- `request`:"
            ),
            encoding="utf-8",
        )
        result = self.run_script("collab_lint.py")
        self.assertEqual(result.returncode, 0)
        self.assertIn("1 warning", result.stdout)

    def test_archive_writes_and_removes_resolved_items(self) -> None:
        path = self.project / "docs" / "collaboration-codex.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "- `status`: active", "- `status`: done"
            ),
            encoding="utf-8",
        )
        result = self.run_script("collab_archive.py", "--threshold-bytes", "1")
        self.assertEqual(result.returncode, 0)
        archive_dir = self.project / "docs" / "collaboration-archives"
        self.assertTrue(archive_dir.exists())
        archives = list(archive_dir.glob("codex-*.md"))
        self.assertEqual(len(archives), 1)
        remaining = path.read_text(encoding="utf-8")
        self.assertNotIn("CX-002", remaining)


class FormalCompletionTest(unittest.TestCase):
    """Tests for --check-completion gate (ELS-012)."""

    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.project = Path(self.temp.name)
        (self.project / "docs").mkdir()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def run_lint(self, *extra_args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                "python3",
                str(ROOT / "scripts" / "collab_lint.py"),
                "--check-completion",
                "--root",
                str(self.project),
                *extra_args,
            ],
            text=True,
            capture_output=True,
            check=False,
        )

    def _write_collab(self, agent: str, content: str) -> None:
        (self.project / "docs" / f"collaboration-{agent}.md").write_text(
            content, encoding="utf-8"
        )

    def test_completion_passes_when_all_criteria_met(self) -> None:
        self._write_collab(
            "claude",
            """# Collaboration: Claude

### [CL-001] Formal review of spec
- `date`: 2026-06-07
- `from`: claude
- `to`: gemini
- `type`: review-request
- `formal`: true
- `status`: done
- `refs`: spec.md

### [CL-002] Consolidation — CL-001
- `date`: 2026-06-07
- `from`: claude
- `to`: all
- `type`: status
- `status`: done
- `refs`: CL-001
""",
        )
        self._write_collab(
            "gemini",
            """# Collaboration: Gemini

### [GM-001] Review — CL-001
- `date`: 2026-06-07
- `from`: gemini
- `to`: claude
- `type`: review
- `status`: done
- `refs`: CL-001
""",
        )
        result = self.run_lint()
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_completion_errors_on_open_formal_request(self) -> None:
        self._write_collab(
            "claude",
            """# Collaboration: Claude

### [CL-001] Formal review of spec
- `date`: 2026-06-07
- `from`: claude
- `to`: gemini
- `type`: review-request
- `formal`: true
- `status`: open
- `refs`: spec.md
""",
        )
        result = self.run_lint()
        self.assertEqual(result.returncode, 1)
        self.assertIn("CL-001 is not done", result.stdout)

    def test_completion_errors_when_consolidation_missing(self) -> None:
        self._write_collab(
            "claude",
            """# Collaboration: Claude

### [CL-001] Formal review of spec
- `date`: 2026-06-07
- `from`: claude
- `to`: gemini
- `type`: review-request
- `formal`: true
- `status`: done
- `refs`: spec.md
""",
        )
        self._write_collab(
            "gemini",
            """# Collaboration: Gemini

### [GM-001] Review — CL-001
- `date`: 2026-06-07
- `from`: gemini
- `to`: claude
- `type`: review
- `status`: done
- `refs`: CL-001
""",
        )
        result = self.run_lint()
        self.assertEqual(result.returncode, 1)
        self.assertIn("no consolidation status item", result.stdout)

    def test_completion_errors_when_named_reviewer_has_not_responded(self) -> None:
        self._write_collab(
            "claude",
            """# Collaboration: Claude

### [CL-001] Formal review of spec
- `date`: 2026-06-07
- `from`: claude
- `to`: gemini
- `type`: review-request
- `formal`: true
- `status`: done
- `refs`: spec.md

### [CL-002] Consolidation — CL-001
- `date`: 2026-06-07
- `from`: claude
- `to`: all
- `type`: status
- `status`: done
- `refs`: CL-001
""",
        )
        result = self.run_lint()
        self.assertEqual(result.returncode, 1)
        self.assertIn("no done review from 'gemini'", result.stdout)


if __name__ == "__main__":
    unittest.main()
