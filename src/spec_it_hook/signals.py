from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
from typing import Any


SIGNAL_PATTERNS: dict[str, tuple[str, ...]] = {
    "api": (
        "api",
        "endpoint",
        "http",
        "openapi",
        "route",
        "status",
        "sse",
        "websocket",
        "adapter/inbound/http",
        "엔드포인트",
        "응답 필드",
        "상태 코드",
    ),
    "data": (
        "database",
        "db ",
        "migration",
        "column",
        "table",
        "sql",
        "cache",
        "stream",
        "payload",
        "데이터베이스",
        "마이그레이션",
        "컬럼",
        "테이블",
    ),
    "security": (
        "auth",
        "permission",
        "secret",
        "token",
        "password",
        "credential",
        "권한",
        "인증",
        "비밀",
    ),
    "dependency": (
        "dependency",
        "requirements.txt",
        "pyproject.toml",
        "package.json",
        "import ",
        "의존성",
    ),
    "infrastructure": (
        "docker",
        "compose",
        "terraform",
        "deploy",
        "runtime",
        "infrastructure",
        "iac",
        "배포",
        "인프라",
    ),
    "configuration": (
        ".env",
        "environment",
        "config/",
        "settings",
        "환경 변수",
        "설정",
    ),
    "intent": (
        ".architecture/changes",
        ".architecture/decisions",
        ".architecture/exceptions",
        "adr-",
        "change spec",
        "decision",
        "결정",
        "예외",
    ),
}

MUTATION_WORDS = (
    " add ",
    " change ",
    " create ",
    " delete ",
    " implement ",
    " modify ",
    " remove ",
    " replace ",
    " update ",
    "추가",
    "변경",
    "구현",
    "수정",
    "삭제",
    "교체",
    "만들",
    "바꿔",
)

NEGATED_MUTATION_PATTERNS = (
    r"\b(?:do\s+not|don't|never)\s+(?:add|change|create|delete|edit|implement|modify|remove|replace|update)\b",
    r"\bwithout\s+(?:adding|changing|creating|deleting|editing|implementing|modifying|removing|replacing|updating)\b",
    r"\bread[- ]only\b",
    r"(?:추가|변경|구현|수정|삭제|교체)(?:하지|하지는)\s*(?:마|말|않)",
)

READ_ONLY_TOOLS = {"Read", "Grep", "Glob", "WebSearch", "WebFetch"}
WRITE_TOOLS = {"Write", "Edit", "NotebookEdit", "MultiEdit"}


def classify_signals(text: str) -> list[str]:
    lowered = f" {text.lower().replace(chr(92), '/')} "
    return [
        signal
        for signal, patterns in SIGNAL_PATTERNS.items()
        if any(pattern in lowered for pattern in patterns)
    ]


def prompt_is_material(prompt: str, signals: list[str]) -> bool:
    lowered = prompt.lower()
    for pattern in NEGATED_MUTATION_PATTERNS:
        lowered = re.sub(pattern, " ", lowered)
    lowered = f" {lowered} "
    return bool(signals and any(word in lowered for word in MUTATION_WORDS))


def tool_text(event: dict[str, Any]) -> str:
    return json.dumps(event.get("tool_input", {}), ensure_ascii=False, sort_keys=True)


def tool_is_mutation(event: dict[str, Any]) -> bool:
    name = str(event.get("tool_name", ""))
    if name in READ_ONLY_TOOLS:
        return False
    if name in WRITE_TOOLS:
        return True
    if name not in {"Bash", "PowerShell"}:
        return True
    command = str(event.get("tool_input", {}).get("command", "")).strip()
    if not command:
        return True
    if re.search(
        r"(?:^|[;&|]\s*)(rm|mv|cp|mkdir|touch|chmod|chown|git\s+(?:add|commit|push|merge|rebase|checkout|switch|reset|clean)|pip\s+install|npm\s+(?:install|uninstall)|sed\s+-i)\b",
        command,
    ):
        return True
    if re.search(r"(?:^|\s)(?:>|>>)(?:\s|$)", command):
        return True
    read_prefixes = (
        "cat ",
        "find ",
        "git diff",
        "git log",
        "git rev-parse",
        "git show",
        "git status",
        "grep ",
        "head ",
        "ls",
        "pwd",
        "rg ",
        "sed -n ",
        "tail ",
    )
    return not command.startswith(read_prefixes)


def changed_paths(project_root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "status", "--porcelain", "--untracked-files=all"],
        cwd=project_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return []
    paths: list[str] = []
    for line in result.stdout.splitlines():
        if len(line) < 4:
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path)
    return paths
