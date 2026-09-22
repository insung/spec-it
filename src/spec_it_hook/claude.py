from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .model import Evaluation
from .runner import PolicyLoop


EVENT_NAMES = {
    "SessionStart": "session-start",
    "UserPromptSubmit": "prompt-submit",
    "PreToolUse": "pre-tool",
    "PostToolUse": "post-tool",
    "Stop": "turn-stop",
}


@dataclass
class ClaudeHookResult:
    evaluation: Evaluation
    claude_output: dict[str, Any]

    def __getattr__(self, name: str) -> Any:
        return getattr(self.evaluation, name)


class ClaudeHookAdapter:
    def __init__(self, loop: PolicyLoop) -> None:
        self.loop = loop

    def evaluate(self, payload: dict[str, Any], *, enabled: bool) -> ClaudeHookResult:
        claude_event_name = str(payload.get("hook_event_name", ""))
        event = {
            "event_name": EVENT_NAMES.get(claude_event_name, "unknown"),
            "session_id": str(payload.get("session_id", "unknown-session")),
            "prompt": payload.get("prompt", ""),
            "tool_name": payload.get("tool_name", ""),
            "tool_input": payload.get("tool_input", {}),
            "source": payload.get("source", ""),
            "stop_hook_active": payload.get("stop_hook_active", False),
        }
        evaluation = self.loop.evaluate(event, enabled=enabled)
        return ClaudeHookResult(
            evaluation=evaluation,
            claude_output=self._output(claude_event_name, evaluation),
        )

    def _output(self, event_name: str, result: Evaluation) -> dict[str, Any]:
        if result.denied and event_name == "PreToolUse":
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": result.context,
                }
            }
        if not result.context:
            return {}
        if event_name == "SessionStart":
            return {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": result.context,
                }
            }
        if event_name == "UserPromptSubmit":
            return {"additionalContext": result.context}
        if event_name in {"PreToolUse", "PostToolUse"}:
            return {
                "hookSpecificOutput": {
                    "hookEventName": event_name,
                    "additionalContext": result.context,
                }
            }
        if event_name == "Stop":
            return {"systemMessage": result.context}
        return {"systemMessage": result.context}
