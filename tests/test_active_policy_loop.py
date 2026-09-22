from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from spec_it_hook.claude import ClaudeHookAdapter
from spec_it_hook.runner import PolicyLoop


MANIFEST = """\
schema_version: 0.1.0
policy:
  source: https://github.com/example/spec-it.git
  version: 0.2.0
project:
  id: example-api
  risk: high
profiles:
  - risk/high
  - capability/http-api
exceptions: []
"""

LOCK = """\
schema_version: 0.2.0
generated: true
policy:
  source: https://github.com/example/spec-it.git
  version: 0.2.0
policy_digest: sha256:{policy_digest}
manifest_digest: sha256:{manifest_digest}
rules:
- enforcement:
    implementation: planned
    mode: validator
  id: API-001
  source: rules/api/API-001.md
- enforcement:
    implementation: implemented
    mode: manual
  id: DATA-009
  source: rules/data/DATA-009.md
- enforcement:
    implementation: implemented
    mode: manual
  id: HITL-001
  source: rules/hitl/HITL-001.md
parameters: {{}}
exceptions: []
"""

RULES = {
    "rules/api/API-001.md": """\
---
id: API-001
title: Version public HTTP paths
condition: "A public HTTP API is created or changed."
statement: "MUST use an explicit major version segment."
forbidden: ["Publish a new unversioned public endpoint."]
evidence: ["OpenAPI path and contract test."]
---
""",
    "rules/data/DATA-009.md": """\
---
id: DATA-009
title: Deliver database changes as release units
condition: "A database definition changes."
statement: "MUST use an immutable ordered migration."
forbidden: ["Apply an unrecorded ALTER statement."]
evidence: ["Migration checksum and post-apply evidence."]
---
""",
    "rules/hitl/HITL-001.md": """\
---
id: HITL-001
title: Stop on material ambiguity
condition: "A material decision is unresolved."
statement: "MUST stop before mutation."
forbidden: ["Guess a material requirement."]
evidence: ["Open decision and decision owner."]
---
""",
}


class PolicyLoopTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.project = self.root / "project"
        self.policy = self.root / "policy"
        self.state = self.root / "state"
        self._init_policy()
        self._init_project()

    def tearDown(self) -> None:
        self.temp.cleanup()

    def _git(self, cwd: Path, *args: str) -> str:
        result = subprocess.run(
            ["git", *args],
            cwd=cwd,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()

    def _init_project(self) -> None:
        (self.project / ".architecture").mkdir(parents=True)
        (self.project / ".architecture" / "manifest.yaml").write_text(
            MANIFEST, encoding="utf-8"
        )
        (self.project / ".architecture" / "lock.yaml").write_text(
            LOCK.format(
                policy_digest=self._policy_digest(),
                manifest_digest=hashlib.sha256(MANIFEST.encode()).hexdigest(),
            ),
            encoding="utf-8",
        )
        (self.project / "README.md").write_text("baseline\n", encoding="utf-8")
        self._git(self.project, "init", "-q")
        self._git(self.project, "config", "user.email", "fixture@example.com")
        self._git(self.project, "config", "user.name", "Fixture")
        self._git(self.project, "add", ".")
        self._git(self.project, "commit", "-qm", "baseline")

    def _init_policy(self) -> None:
        self.policy.mkdir()
        (self.policy / "VERSION").write_text("0.2.0\n", encoding="utf-8")
        for relative, content in RULES.items():
            path = self.policy / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        self._git(self.policy, "init", "-q")
        self._git(self.policy, "config", "user.email", "fixture@example.com")
        self._git(self.policy, "config", "user.name", "Fixture")
        self._git(self.policy, "add", ".")
        self._git(self.policy, "commit", "-qm", "policy")
        self._git(self.policy, "tag", "v0.2.0")

    def _policy_digest(self) -> str:
        paths = self._git(
            self.policy,
            "ls-tree",
            "-r",
            "--name-only",
            "v0.2.0",
            "--",
            "VERSION",
            "rules",
            "profiles",
            "schemas",
        ).splitlines()
        digest = hashlib.sha256()
        for path in sorted(paths):
            content = subprocess.run(
                ["git", "show", f"v0.2.0:{path}"],
                cwd=self.policy,
                check=True,
                capture_output=True,
            ).stdout
            digest.update(path.encode())
            digest.update(b"\0")
            digest.update(content)
            digest.update(b"\0")
        return digest.hexdigest()

    def _refresh_lock_policy_digest(self) -> None:
        lock_path = self.project / ".architecture" / "lock.yaml"
        lock_path.write_text(
            re.sub(
                r"(?m)^policy_digest:\s*sha256:[a-f0-9]{64}$",
                f"policy_digest: sha256:{self._policy_digest()}",
                lock_path.read_text(encoding="utf-8"),
            ),
            encoding="utf-8",
        )

    def _loop(self) -> PolicyLoop:
        return PolicyLoop(
            project_root=self.project,
            policy_root=self.policy,
            state_root=self.state,
        )

    def _hook(self) -> ClaudeHookAdapter:
        return ClaudeHookAdapter(self._loop())

    def test_core_result_does_not_contain_vendor_output(self) -> None:
        result = self._loop().evaluate(
            {"event_name": "session-start", "session_id": "core-session"},
            enabled=True,
        )

        self.assertFalse(hasattr(result, "claude_output"))

    def test_disabled_runner_is_a_true_noop(self) -> None:
        result = self._hook().evaluate(
            {
                "hook_event_name": "SessionStart",
                "session_id": "s1",
                "source": "startup",
            },
            enabled=False,
        )

        self.assertEqual("disabled", result.status)
        self.assertEqual("", result.context)
        self.assertEqual({}, result.claude_output)
        self.assertFalse(self.state.exists())

    def test_session_start_uses_light_without_loading_rule_bodies(self) -> None:
        result = self._hook().evaluate(
            {
                "hook_event_name": "SessionStart",
                "session_id": "s1",
                "source": "startup",
            },
            enabled=True,
        )

        self.assertEqual("light", result.depth)
        self.assertEqual("pass", result.status)
        self.assertEqual([], result.selected_rule_ids)
        self.assertIn("pinned policy 0.2.0", result.context)
        self.assertLessEqual(len(result.context), 4_000)
        self.assertEqual(
            "SessionStart",
            result.claude_output["hookSpecificOutput"]["hookEventName"],
        )

    def test_explanation_prompt_stays_light_and_adds_no_context(self) -> None:
        result = self._hook().evaluate(
            {
                "hook_event_name": "UserPromptSubmit",
                "session_id": "s1",
                "prompt": "현재 API 구조를 설명해줘",
            },
            enabled=True,
        )

        self.assertEqual("light", result.depth)
        self.assertEqual("", result.context)
        self.assertEqual({}, result.claude_output)

    def test_explicit_no_change_instruction_does_not_trigger_hard_mode(self) -> None:
        result = self._hook().evaluate(
            {
                "hook_event_name": "UserPromptSubmit",
                "session_id": "s1",
                "prompt": "현재 API 구조를 설명해줘. 파일은 수정하지 마.",
            },
            enabled=True,
        )

        self.assertEqual("light", result.depth)
        self.assertEqual("", result.context)

    def test_material_api_prompt_escalates_and_reads_only_related_rules(self) -> None:
        result = self._hook().evaluate(
            {
                "hook_event_name": "UserPromptSubmit",
                "session_id": "s1",
                "prompt": "새 API endpoint를 추가하고 HTTP status를 변경해줘",
            },
            enabled=True,
        )

        self.assertEqual("hard", result.depth)
        self.assertEqual(["API-001"], result.selected_rule_ids)
        self.assertIn("Version public HTTP paths", result.context)
        self.assertIn("observed / inferred / human-approved / unknown", result.context)
        self.assertLessEqual(len(result.context), 8_000)
        self.assertEqual(result.context, result.claude_output["additionalContext"])
        self.assertFalse(result.denied)

    def test_each_material_signal_family_escalates_to_hard(self) -> None:
        prompts = {
            "api": "새 API endpoint를 추가해줘",
            "data": "DB migration을 추가해줘",
            "security": "auth permission을 변경해줘",
            "dependency": "requirements.txt dependency를 추가해줘",
            "infrastructure": "Docker deployment를 변경해줘",
            "configuration": "환경 변수 설정을 변경해줘",
        }

        for index, (signal, prompt) in enumerate(prompts.items()):
            with self.subTest(signal=signal):
                result = self._hook().evaluate(
                    {
                        "hook_event_name": "UserPromptSubmit",
                        "session_id": f"signal-{index}",
                        "prompt": prompt,
                    },
                    enabled=True,
                )
                self.assertEqual("hard", result.depth)
                self.assertIn(signal, result.signals)

    def test_more_than_eight_matching_rules_is_explicit_human_review(self) -> None:
        extra_lock_entries = []
        for number in range(2, 10):
            rule_id = f"API-{number:03d}"
            relative = f"rules/api/{rule_id}.md"
            path = self.policy / relative
            path.write_text(
                "---\n"
                f"id: {rule_id}\n"
                f"title: API rule {number}\n"
                'condition: "An API changes."\n'
                'statement: "MUST review the API change."\n'
                'evidence: ["Review evidence."]\n'
                "---\n",
                encoding="utf-8",
            )
            extra_lock_entries.append(f"- id: {rule_id}\n  source: {relative}\n")
        self._git(self.policy, "add", ".")
        self._git(self.policy, "commit", "-qm", "more api rules")
        self._git(self.policy, "tag", "-f", "v0.2.0")
        self._refresh_lock_policy_digest()

        lock_path = self.project / ".architecture" / "lock.yaml"
        lock_path.write_text(
            lock_path.read_text(encoding="utf-8").replace(
                "  source: rules/hitl/HITL-001.md\nparameters: {}\n",
                "  source: rules/hitl/HITL-001.md\n"
                + "".join(extra_lock_entries)
                + "parameters: {}\n",
            ),
            encoding="utf-8",
        )

        result = self._hook().evaluate(
            {
                "hook_event_name": "UserPromptSubmit",
                "session_id": "rule-cap-session",
                "prompt": "새 API endpoint를 추가해줘",
            },
            enabled=True,
        )

        self.assertEqual("human-review", result.status)
        self.assertEqual(8, len(result.selected_rule_ids))
        self.assertIn("selection exceeded", result.context)

    def test_invalid_policy_blocks_mutation_but_not_read_only_recovery(self) -> None:
        lock = (self.project / ".architecture" / "lock.yaml").read_text(
            encoding="utf-8"
        )
        (self.project / ".architecture" / "lock.yaml").write_text(
            lock.replace("  version: 0.2.0", "  version: 0.3.0", 1),
            encoding="utf-8",
        )

        write_result = self._hook().evaluate(
            {
                "hook_event_name": "PreToolUse",
                "session_id": "s1",
                "tool_name": "Write",
                "tool_input": {"file_path": str(self.project / "domain" / "thing.py")},
            },
            enabled=True,
        )
        read_result = self._hook().evaluate(
            {
                "hook_event_name": "PreToolUse",
                "session_id": "s2",
                "tool_name": "Read",
                "tool_input": {
                    "file_path": str(self.project / ".architecture" / "lock.yaml")
                },
            },
            enabled=True,
        )

        self.assertEqual("policy-unavailable", write_result.status)
        self.assertTrue(write_result.denied)
        self.assertEqual(
            "deny",
            write_result.claude_output["hookSpecificOutput"]["permissionDecision"],
        )
        self.assertEqual("policy-unavailable", read_result.status)
        self.assertFalse(read_result.denied)
        self.assertNotIn(
            "permissionDecision", read_result.claude_output["hookSpecificOutput"]
        )

    def test_policy_digest_mismatch_blocks_mutation(self) -> None:
        lock_path = self.project / ".architecture" / "lock.yaml"
        lock_path.write_text(
            re.sub(
                r"(?m)^policy_digest:.*$",
                f"policy_digest: sha256:{'0' * 64}",
                lock_path.read_text(encoding="utf-8"),
            ),
            encoding="utf-8",
        )

        result = self._hook().evaluate(
            {
                "hook_event_name": "PreToolUse",
                "session_id": "policy-digest-session",
                "tool_name": "Write",
                "tool_input": {"file_path": "app.py"},
            },
            enabled=True,
        )

        self.assertEqual("policy-unavailable", result.status)
        self.assertTrue(result.denied)
        self.assertIn("policy digest", result.context)

    def test_manifest_digest_mismatch_blocks_mutation(self) -> None:
        manifest_path = self.project / ".architecture" / "manifest.yaml"
        manifest_path.write_text(MANIFEST + "# changed\n", encoding="utf-8")

        result = self._hook().evaluate(
            {
                "hook_event_name": "PreToolUse",
                "session_id": "manifest-digest-session",
                "tool_name": "Write",
                "tool_input": {"file_path": "app.py"},
            },
            enabled=True,
        )

        self.assertEqual("policy-unavailable", result.status)
        self.assertTrue(result.denied)
        self.assertIn("manifest digest", result.context)

    def test_missing_selected_rule_source_is_policy_unavailable_and_denies_write(
        self,
    ) -> None:
        lock_path = self.project / ".architecture" / "lock.yaml"
        lock_path.write_text(
            lock_path.read_text(encoding="utf-8").replace(
                "rules/api/API-001.md", "rules/api/API-999.md"
            ),
            encoding="utf-8",
        )

        result = self._hook().evaluate(
            {
                "hook_event_name": "PreToolUse",
                "session_id": "missing-rule-session",
                "tool_name": "Write",
                "tool_input": {"file_path": "adapter/inbound/http/router.py"},
            },
            enabled=True,
        )

        self.assertEqual("policy-unavailable", result.status)
        self.assertTrue(result.denied)
        self.assertEqual(
            "deny", result.claude_output["hookSpecificOutput"]["permissionDecision"]
        )

    def test_valid_older_pin_is_not_treated_as_version_drift(self) -> None:
        result = self._hook().evaluate(
            {
                "hook_event_name": "PreToolUse",
                "session_id": "s1",
                "tool_name": "Write",
                "tool_input": {"file_path": str(self.project / "README.md")},
            },
            enabled=True,
        )

        self.assertNotEqual("policy-unavailable", result.status)
        self.assertFalse(result.denied)

    def test_duplicate_hard_fingerprint_does_not_repeat_context(self) -> None:
        event = {
            "hook_event_name": "UserPromptSubmit",
            "session_id": "s1",
            "prompt": "DB migration을 추가해줘",
        }

        first = self._hook().evaluate(event, enabled=True)
        second = self._hook().evaluate(event, enabled=True)

        self.assertEqual("hard", first.depth)
        self.assertEqual(["DATA-009"], first.selected_rule_ids)
        self.assertNotEqual("", first.context)
        self.assertTrue(second.duplicate)
        self.assertEqual("", second.context)
        self.assertEqual({}, second.claude_output)

    def test_stop_reports_material_diff_without_continuing_the_agent(self) -> None:
        api_file = self.project / "adapter" / "inbound" / "http" / "router.py"
        api_file.parent.mkdir(parents=True)
        api_file.write_text("# endpoint changed\n", encoding="utf-8")

        result = self._hook().evaluate(
            {
                "hook_event_name": "Stop",
                "session_id": "s1",
                "stop_hook_active": False,
            },
            enabled=True,
        )

        self.assertEqual("hard", result.depth)
        self.assertIn("API-001", result.context)
        self.assertIn("systemMessage", result.claude_output)
        self.assertNotIn("decision", result.claude_output)
        self.assertNotIn("continue", result.claude_output)

    def test_post_tool_signal_is_rechecked_at_stop_without_source_mutation(
        self,
    ) -> None:
        hook = self._hook()
        post_result = hook.evaluate(
            {
                "hook_event_name": "PostToolUse",
                "session_id": "dirty-signal-session",
                "tool_name": "Write",
                "tool_input": {"file_path": "adapter/inbound/http/router.py"},
            },
            enabled=True,
        )
        stop_result = hook.evaluate(
            {
                "hook_event_name": "Stop",
                "session_id": "dirty-signal-session",
                "stop_hook_active": False,
            },
            enabled=True,
        )

        self.assertEqual("light", post_result.depth)
        self.assertEqual("hard", stop_result.depth)
        self.assertIn("API-001", stop_result.selected_rule_ids)

    def test_state_contains_metrics_but_not_prompt_or_source_text(self) -> None:
        secret_prompt = "API endpoint를 추가해줘 token=super-secret-value"
        self._hook().evaluate(
            {
                "hook_event_name": "UserPromptSubmit",
                "session_id": "metrics-session",
                "prompt": secret_prompt,
            },
            enabled=True,
        )

        state_files = list(self.state.glob("*.json"))
        self.assertEqual(1, len(state_files))
        raw = state_files[0].read_text(encoding="utf-8")
        data = json.loads(raw)
        self.assertNotIn(secret_prompt, raw)
        self.assertNotIn("super-secret-value", raw)
        self.assertEqual(1, data["metrics"]["events"])
        self.assertEqual(1, data["metrics"]["hard_escalations"])
        self.assertGreater(data["metrics"]["output_chars"], 0)
        self.assertFalse((self.project / ".spec-it").exists())

    def test_open_material_decision_blocks_write_but_allows_read_only_bash(
        self,
    ) -> None:
        change = self.project / ".architecture" / "changes" / "active" / "spec.md"
        change.parent.mkdir(parents=True)
        change.write_text(
            "---\nstatus: clarifying\n---\n\nA material decision is still open.\n",
            encoding="utf-8",
        )

        write_result = self._hook().evaluate(
            {
                "hook_event_name": "PreToolUse",
                "session_id": "decision-session",
                "tool_name": "Write",
                "tool_input": {"file_path": str(self.project / "app.py")},
            },
            enabled=True,
        )
        read_result = self._hook().evaluate(
            {
                "hook_event_name": "PreToolUse",
                "session_id": "decision-session",
                "tool_name": "Bash",
                "tool_input": {"command": "git status --short"},
            },
            enabled=True,
        )

        self.assertEqual("human-review", write_result.status)
        self.assertTrue(write_result.denied)
        self.assertFalse(read_result.denied)

    def test_metrics_count_light_and_hard_evaluations_separately(self) -> None:
        loop = self._hook()
        loop.evaluate(
            {"hook_event_name": "SessionStart", "session_id": "cost-session"},
            enabled=True,
        )
        result = loop.evaluate(
            {
                "hook_event_name": "UserPromptSubmit",
                "session_id": "cost-session",
                "prompt": "새 API endpoint를 추가해줘",
            },
            enabled=True,
        )

        state = json.loads(result.state_path.read_text(encoding="utf-8"))
        self.assertEqual(2, state["metrics"]["events"])
        self.assertEqual(1, state["metrics"]["light_evaluations"])
        self.assertEqual(1, state["metrics"]["hard_escalations"])

    def test_cli_emits_valid_json_for_claude_and_no_output_when_disabled(self) -> None:
        script = Path(__file__).parents[1] / "tools" / "spec_it_hook.py"
        event = {
            "hook_event_name": "SessionStart",
            "session_id": "cli-session",
            "source": "startup",
        }
        command = [
            sys.executable,
            str(script),
            "--project-root",
            str(self.project),
            "--policy-root",
            str(self.policy),
            "--state-root",
            str(self.state),
        ]

        disabled = subprocess.run(
            command,
            input=json.dumps(event),
            capture_output=True,
            text=True,
            check=False,
        )
        enabled = subprocess.run(
            [*command, "--enabled"],
            input=json.dumps(event),
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(0, disabled.returncode)
        self.assertEqual("", disabled.stdout)
        self.assertEqual(0, enabled.returncode)
        payload = json.loads(enabled.stdout)
        self.assertEqual("SessionStart", payload["hookSpecificOutput"]["hookEventName"])

    def test_cli_returns_nonzero_without_malformed_stdout_on_invalid_input(
        self,
    ) -> None:
        script = Path(__file__).parents[1] / "tools" / "spec_it_hook.py"
        result = subprocess.run(
            [sys.executable, str(script), "--enabled"],
            input="not-json",
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(3, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertIn("spec-it runner error", result.stderr)

    def test_example_settings_use_exec_form_without_shell_interpolation(self) -> None:
        settings_path = (
            Path(__file__).parents[1]
            / "examples"
            / "claude-hook-pilot"
            / "settings.local.json"
        )
        settings = json.loads(settings_path.read_text(encoding="utf-8"))
        handlers = [
            handler
            for groups in settings["hooks"].values()
            for group in groups
            for handler in group["hooks"]
        ]

        self.assertGreater(len(handlers), 0)
        for handler in handlers:
            self.assertEqual("python3", handler["command"])
            self.assertIsInstance(handler["args"], list)
            self.assertIn("${CLAUDE_PROJECT_DIR}", handler["args"])
            self.assertNotIn("SPEC_IT_ROOT", json.dumps(handler))


if __name__ == "__main__":
    unittest.main()
