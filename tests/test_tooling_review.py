from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

FOUNDATION = Path(__file__).resolve().parents[1] / "agent-workflow-foundation"
sys.path.insert(0, str(FOUNDATION / "scripts"))
import tooling_review as review


class ToolingReviewTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.local = self.root / "agent-workflow-local"
        self.local.mkdir()
        self.state("Exploration")
        (self.local / "tooling.json").write_text(json.dumps({"tools": {"grill-me": {"installed": True}}}))

    def state(self, stage, artifact="spec/change-one"):
        (self.local / "current-state.md").write_text(
            f"- `current_stage`: {stage}\n- `current_artifact`: {artifact}\n")

    def plan(self, event="stage-change", transition="CX-100", tools=()):
        return review.plan(self.root, FOUNDATION, event, transition_id=transition, tools=tools)

    def evidence(self, request, unavailable=False):
        return {"context": request["context"], "transition_id": request["transition_id"],
                "checked_at": "2026-11-23T10:00:00+00:00",
                "tools": {key: {"status": "unavailable" if unavailable else "current",
                                 "source": "https://github.com/mattpocock/skills",
                                 "observed": "reviewed commit", "decision": "retain",
                                 "summary": "Network unavailable" if unavailable else "Compared upstream revision"}
                          for key in request["tools"]},
                "discovery": {"status": "checked", "sources": ["https://github.com/mattpocock/skills"],
                              "summary": "No additional capability needed"}}

    def test_check_is_read_only_and_completed_event_is_not_repeated(self):
        before = (self.local / "tooling.json").read_bytes()
        request = self.plan()
        self.assertEqual(request["status"], "review-required")
        self.assertFalse((self.root / review.RECORD).exists())
        review.record(self.root, request, self.evidence(request))
        self.assertEqual(self.plan()["status"], "event-recorded")
        self.assertEqual((self.local / "tooling.json").read_bytes(), before)

    def test_changed_stage_and_changed_artifact_require_review(self):
        request = self.plan()
        review.record(self.root, request, self.evidence(request))
        self.state("Proposal")
        self.assertEqual(self.plan()["status"], "review-required")
        self.state("Exploration", "spec/change-two")
        self.assertEqual(self.plan()["status"], "review-required")

    def test_same_stage_new_transition_requires_review_and_resume_reuses_it(self):
        request = self.plan("stage-change", "CX-100")
        review.record(self.root, request, self.evidence(request))
        self.assertEqual(self.plan("stage-change", "CX-100")["status"], "event-recorded")
        self.assertEqual(self.plan()["status"], "event-recorded")
        self.assertEqual(self.plan("stage-change", "CX-101")["status"], "review-required")
        with self.assertRaises(ValueError):
            self.plan("stage-change", None)

    def test_unavailable_checks_remain_degraded_and_do_not_loop_on_resume(self):
        request = self.plan()
        review.record(self.root, request, self.evidence(request, unavailable=True))
        self.assertEqual(self.plan()["status"], "event-recorded")
        self.assertEqual(self.plan()["previous_status"], "degraded")

    def test_missing_accounting_or_stale_context_cannot_record_completion(self):
        request = self.plan()
        evidence = self.evidence(request)
        for mutate in (lambda e: e["tools"].clear(),
                       lambda e: e["context"].update(stage="Implementation"),
                       lambda e: e["tools"]["grill-me"].pop("source"),
                       lambda e: e["discovery"].update(sources=[])):
            invalid = copy.deepcopy(evidence)
            mutate(invalid)
            with self.assertRaises(ValueError):
                review.record(self.root, request, invalid)
        self.assertFalse((self.root / review.RECORD).exists())

    def test_added_selection_is_due_and_excluded_categories_are_not_selected(self):
        request = self.plan()
        review.record(self.root, request, self.evidence(request))
        requested = self.plan(tools=("openspec", "canvas-design"))
        self.assertEqual(requested["status"], "review-required")
        self.assertIn("openspec", requested["tools"])
        self.assertNotIn("canvas-design", requested["tools"])
        self.assertEqual(requested["excluded"], ["canvas-design"])
        with self.assertRaises(ValueError):
            self.plan(tools=("unknown-tool",))

    def test_only_manual_and_stage_events_are_supported_and_manual_is_fresh(self):
        request = self.plan("manual", None)
        review.record(self.root, request, self.evidence(request))
        self.assertEqual(self.plan("manual", None)["status"], "review-required")
        for event in ("setup", "resume"):
            with self.assertRaises(ValueError):
                self.plan(event)

    def test_template_requirements_are_reviewed_and_stage_trigger_is_template_owned(self):
        profile_path = self.local / "project-template.json"
        profile_path.write_text(json.dumps({"stage_tooling_review": False,
                                             "required_tools": ["grill-me", "markitdown"]}))
        self.state("TOC Planning", "None")
        with self.assertRaisesRegex(ValueError, "manual tooling reviews only"):
            self.plan()
        request = self.plan("manual", None)
        self.assertEqual(set(request["tools"]), {"grill-me", "markitdown"})
        self.assertEqual(request["context"]["stage"], "TOC Planning")
        self.assertFalse((self.root / review.RECORD).exists())
        profile_path.write_text(json.dumps({"stage_tooling_review": True,
                                             "required_tools": ["grill-me", "openspec", "github"]}))
        self.assertEqual(set(self.plan()["tools"]), {"grill-me", "openspec", "github"})


if __name__ == "__main__":
    unittest.main()
