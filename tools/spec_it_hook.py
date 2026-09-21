#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "src"))

from spec_it_hook.claude import ClaudeHookAdapter  # noqa: E402
from spec_it_hook.runner import PolicyLoop  # noqa: E402


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the spec-it Claude hook adapter")
    parser.add_argument(
        "--enabled", action="store_true", help="explicitly enable the local pilot"
    )
    parser.add_argument("--project-root", type=Path)
    parser.add_argument("--policy-root", type=Path, default=REPOSITORY_ROOT)
    parser.add_argument("--state-root", type=Path)
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        event = json.load(sys.stdin)
        project_root = args.project_root or Path(event.get("cwd", os.getcwd()))
        scratchpad = event.get("scratchpad_dir")
        state_root = args.state_root or (
            Path(scratchpad) / "spec-it-policy-loop"
            if scratchpad
            else Path(tempfile.gettempdir()) / "spec-it-policy-loop"
        )
        result = ClaudeHookAdapter(
            PolicyLoop(project_root, args.policy_root, state_root)
        ).evaluate(event, enabled=args.enabled)
    except Exception as error:  # Claude command hooks fail open on non-2 exits.
        print(f"spec-it runner error: {type(error).__name__}: {error}", file=sys.stderr)
        return 3
    if result.claude_output:
        json.dump(
            result.claude_output, sys.stdout, ensure_ascii=False, separators=(",", ":")
        )
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
