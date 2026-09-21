from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class RuleRef:
    id: str
    source: str


@dataclass(frozen=True)
class PolicyView:
    source: str
    version: str
    rules: tuple[RuleRef, ...]
    tag: str


@dataclass(frozen=True)
class RuleCard:
    id: str
    title: str
    condition: str
    statement: str
    evidence: str


@dataclass
class Evaluation:
    event_name: str
    status: str
    depth: str
    signals: list[str] = field(default_factory=list)
    selected_rule_ids: list[str] = field(default_factory=list)
    context: str = ""
    denied: bool = False
    duplicate: bool = False
    state_path: Path | None = None
