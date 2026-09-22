from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path
from typing import Any

from .model import Evaluation, PolicyView, RuleCard, RuleRef
from .policy import PolicyUnavailable, load_policy_view, load_rule_card
from .signals import (
    changed_paths,
    classify_signals,
    prompt_is_material,
    tool_is_mutation,
    tool_text,
)
from .state import StateStore


RULE_PREFIXES: dict[str, tuple[str, ...]] = {
    "api": ("API-", "MSG-", "COMP-"),
    "data": ("DATA-",),
    "security": ("SEC-", "HITL-"),
    "dependency": ("CODE-", "SEC-", "TOOL-"),
    "infrastructure": ("INFRA-", "IAC-", "DEP-", "COST-", "REL-"),
    "configuration": ("CODE-", "SEC-", "TOOL-"),
    "intent": ("GOV-", "HITL-"),
}


class PolicyLoop:
    def __init__(self, project_root: Path, policy_root: Path, state_root: Path) -> None:
        self.project_root = project_root.resolve()
        self.policy_root = policy_root.resolve()
        self.state_root = state_root.resolve()

    def evaluate(self, event: dict[str, Any], *, enabled: bool) -> Evaluation:
        event_name = str(event.get("event_name", ""))
        if not enabled:
            return Evaluation(event_name=event_name, status="disabled", depth="light")

        started = time.perf_counter()
        session_id = str(event.get("session_id", "unknown-session"))
        store = StateStore(self.state_root, self.project_root, session_id)
        state = store.load()
        result = self._evaluate(event, event_name, state)
        elapsed_ms = (time.perf_counter() - started) * 1000
        self._record_metrics(state, result, elapsed_ms)
        store.save(state)
        result.state_path = store.path
        return result

    def _evaluate(
        self, event: dict[str, Any], event_name: str, state: dict[str, Any]
    ) -> Evaluation:
        mutation = event_name == "pre-tool" and tool_is_mutation(event)
        try:
            view = load_policy_view(self.project_root, self.policy_root)
        except PolicyUnavailable as error:
            context = f"spec-it policy unavailable: {error}. Read-only diagnosis remains allowed."
            denied = mutation
            return self._result(
                event_name=event_name,
                status="policy-unavailable",
                depth="hard",
                context=context,
                denied=denied,
            )

        open_decision = self._material_open_decision()
        signals, material = self._event_signals(event, event_name, state)
        if event_name == "post-tool":
            state["dirty_signals"] = sorted(
                set(state.get("dirty_signals", [])) | set(signals)
            )
            return self._result(event_name=event_name, status="pass", depth="light")

        if open_decision and mutation:
            context = (
                "spec-it human-review: a material change decision is open. "
                "Inspect the active change and obtain the decision before mutation."
            )
            return self._result(
                event_name=event_name,
                status="human-review",
                depth="hard",
                signals=signals,
                context=context,
                denied=True,
            )

        if not material:
            if event_name == "session-start":
                context = (
                    f"spec-it active: pinned policy {view.version}. Start in Light mode; "
                    "re-evaluate only when API, data, security, dependency, infrastructure, "
                    "configuration, or material intent signals appear."
                )[:4_000]
                return self._result(
                    event_name=event_name,
                    status="pass",
                    depth="light",
                    context=context,
                )
            return self._result(event_name=event_name, status="pass", depth="light")

        selected, selection_exceeded = self._select_rules(view, signals)
        fingerprint = self._fingerprint(view, event_name, signals, event)
        if fingerprint in state.get("seen", []):
            return self._result(
                event_name=event_name,
                status="human-review" if selection_exceeded else "warn",
                depth="hard",
                signals=signals,
                selected_rule_ids=[rule.id for rule in selected],
                duplicate=True,
            )

        try:
            cards = [load_rule_card(self.policy_root, view, rule) for rule in selected]
        except PolicyUnavailable as error:
            context = (
                f"spec-it policy unavailable: {error}. "
                "Read-only diagnosis remains allowed."
            )
            return self._result(
                event_name=event_name,
                status="policy-unavailable",
                depth="hard",
                signals=signals,
                selected_rule_ids=[rule.id for rule in selected],
                context=context,
                denied=mutation,
            )
        context = self._hard_context(view, signals, cards, selection_exceeded)
        state.setdefault("seen", []).append(fingerprint)
        state["seen"] = state["seen"][-100:]
        status = "warn" if cards and not selection_exceeded else "human-review"
        return self._result(
            event_name=event_name,
            status=status,
            depth="hard",
            signals=signals,
            selected_rule_ids=[card.id for card in cards],
            context=context,
        )

    def _event_signals(
        self, event: dict[str, Any], event_name: str, state: dict[str, Any]
    ) -> tuple[list[str], bool]:
        if event_name == "prompt-submit":
            prompt = str(event.get("prompt", ""))
            signals = classify_signals(prompt)
            return signals, prompt_is_material(prompt, signals)
        if event_name == "pre-tool":
            signals = classify_signals(tool_text(event))
            return signals, bool(signals and tool_is_mutation(event))
        if event_name == "post-tool":
            signals = classify_signals(tool_text(event))
            return signals, False
        if event_name == "turn-stop":
            signals = classify_signals("\n".join(changed_paths(self.project_root)))
            signals = sorted(set(signals) | set(state.get("dirty_signals", [])))
            return signals, bool(signals)
        return [], False

    def _select_rules(
        self, view: PolicyView, signals: list[str]
    ) -> tuple[list[RuleRef], bool]:
        prefixes = tuple(
            prefix for signal in signals for prefix in RULE_PREFIXES.get(signal, ())
        )
        if not prefixes:
            return [], False
        selected = [rule for rule in view.rules if rule.id.startswith(prefixes)]
        return selected[:8], len(selected) > 8

    def _hard_context(
        self,
        view: PolicyView,
        signals: list[str],
        cards: list[RuleCard],
        selection_exceeded: bool,
    ) -> str:
        lines = [
            f"spec-it Hard evaluation — pinned {view.version}; signals: {', '.join(signals)}.",
            "Before mutation, answer each applicable card with observed / inferred / "
            "human-approved / unknown evidence. Do not convert unknown material intent into pass.",
        ]
        if not cards:
            lines.append("No pinned rule matched these signals; report human-review.")
        if selection_exceeded:
            lines.append(
                "Rule selection exceeded the 8-rule budget; the visible cards are partial. "
                "Report human-review instead of inferring pass."
            )
        for card in cards:
            lines.extend(
                [
                    f"- {card.id} — {card.title}",
                    f"  condition: {card.condition}",
                    f"  obligation: {card.statement}",
                    f"  evidence: {card.evidence}",
                ]
            )
        return "\n".join(lines)[:8_000]

    def _material_open_decision(self) -> bool:
        changes = self.project_root / ".architecture" / "changes"
        if not changes.is_dir():
            return False
        for path in changes.glob("*/spec.md"):
            text = path.read_text(encoding="utf-8")
            frontmatter = text.split("---", 2)
            if len(frontmatter) >= 3 and re.search(
                r"(?m)^status:\s*clarifying\s*$", frontmatter[1]
            ):
                return True
            if re.search(
                r"(?mi)^\|[^\n]*\|\s*(behavior|public-contract|security|data|cost|"
                r"infrastructure|deployment|architecture)\s*\|\s*open\s*\|",
                text,
            ):
                return True
        return False

    def _fingerprint(
        self,
        view: PolicyView,
        event_name: str,
        signals: list[str],
        event: dict[str, Any],
    ) -> str:
        relevant = {
            "policy": view.version,
            "event": event_name,
            "signals": signals,
            "prompt": event.get("prompt", ""),
            "tool_name": event.get("tool_name", ""),
            "tool_input": event.get("tool_input", {}),
            "changed_paths": (
                changed_paths(self.project_root) if event_name == "turn-stop" else []
            ),
        }
        serialized = json.dumps(
            relevant, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        )
        return hashlib.sha256(serialized.encode()).hexdigest()

    def _result(
        self,
        *,
        event_name: str,
        status: str,
        depth: str,
        signals: list[str] | None = None,
        selected_rule_ids: list[str] | None = None,
        context: str = "",
        denied: bool = False,
        duplicate: bool = False,
    ) -> Evaluation:
        return Evaluation(
            event_name=event_name,
            status=status,
            depth=depth,
            signals=signals or [],
            selected_rule_ids=selected_rule_ids or [],
            context=context,
            denied=denied,
            duplicate=duplicate,
        )

    def _record_metrics(
        self, state: dict[str, Any], result: Evaluation, elapsed_ms: float
    ) -> None:
        metrics = state["metrics"]
        metrics["events"] += 1
        if result.depth == "hard":
            metrics["hard_escalations"] += 1
        else:
            metrics["light_evaluations"] += 1
        if not result.context:
            metrics["noops"] += 1
        if result.denied:
            metrics["denied"] += 1
        metrics["output_chars"] += len(result.context)
        metrics["elapsed_ms_total"] = round(metrics["elapsed_ms_total"] + elapsed_ms, 3)
