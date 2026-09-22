from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path
from typing import Any


EMPTY_STATE: dict[str, Any] = {
    "seen": [],
    "dirty_signals": [],
    "metrics": {
        "events": 0,
        "light_evaluations": 0,
        "hard_escalations": 0,
        "noops": 0,
        "denied": 0,
        "output_chars": 0,
        "elapsed_ms_total": 0.0,
        "errors": 0,
    },
}


class StateStore:
    def __init__(self, root: Path, project_root: Path, session_id: str) -> None:
        identity = hashlib.sha256(
            f"{project_root.resolve()}\0{session_id}".encode()
        ).hexdigest()[:20]
        self.root = root
        self.path = root / f"{identity}.json"

    def load(self) -> dict[str, Any]:
        if not self.path.is_file():
            return json.loads(json.dumps(EMPTY_STATE))
        try:
            data = json.loads(self.path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return json.loads(json.dumps(EMPTY_STATE))
        return data

    def save(self, data: dict[str, Any]) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        descriptor, temporary = tempfile.mkstemp(
            prefix=".spec-it-state-", dir=self.root
        )
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                json.dump(data, stream, ensure_ascii=False, sort_keys=True)
                stream.write("\n")
            os.replace(temporary, self.path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
