from __future__ import annotations

import hashlib
import re
import subprocess
from pathlib import Path

from .model import PolicyView, RuleCard, RuleRef


class PolicyUnavailable(RuntimeError):
    """The pinned project policy cannot be read consistently."""


def _policy_field(text: str, key: str) -> str:
    match = re.search(r"(?ms)^policy:\s*\n(?P<body>(?:^[ \t]+.*(?:\n|\Z))*)", text)
    if not match:
        raise PolicyUnavailable("policy block is missing")
    field = re.search(rf"(?m)^\s+{re.escape(key)}:\s*(.+?)\s*$", match.group("body"))
    if not field:
        raise PolicyUnavailable(f"policy.{key} is missing")
    return field.group(1).strip().strip("'\"")


def _top_level_field(text: str, key: str) -> str:
    field = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", text)
    if not field:
        raise PolicyUnavailable(f"{key} is missing")
    return field.group(1).strip().strip("'\"")


def _policy_digest(policy_root: Path, tag: str) -> str:
    listed = subprocess.run(
        [
            "git",
            "ls-tree",
            "-r",
            "--name-only",
            tag,
            "--",
            "VERSION",
            "rules",
            "profiles",
            "schemas",
        ],
        cwd=policy_root,
        capture_output=True,
        text=True,
    )
    if listed.returncode != 0:
        raise PolicyUnavailable(f"cannot enumerate policy source at {tag}")
    paths = sorted(path for path in listed.stdout.splitlines() if path)
    if "VERSION" not in paths:
        raise PolicyUnavailable(f"VERSION is unavailable at {tag}")

    digest = hashlib.sha256()
    for path in paths:
        content = subprocess.run(
            ["git", "show", f"{tag}:{path}"],
            cwd=policy_root,
            capture_output=True,
        )
        if content.returncode != 0:
            raise PolicyUnavailable(f"cannot read {path} at {tag}")
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(content.stdout)
        digest.update(b"\0")
    return f"sha256:{digest.hexdigest()}"


def _lock_rules(text: str) -> tuple[RuleRef, ...]:
    match = re.search(
        r"(?ms)^rules:\s*\n(?P<body>.*?)(?=^[A-Za-z_][A-Za-z0-9_-]*:|\Z)", text
    )
    if not match:
        raise PolicyUnavailable("lock rules are missing")
    ids = re.findall(
        r"(?m)^\s*(?:-\s*)?id:\s*([A-Z][A-Z0-9-]*-\d+)\s*$", match.group("body")
    )
    sources = re.findall(
        r"(?m)^\s*source:\s*(rules/[^\s]+\.md)\s*$", match.group("body")
    )
    if not ids or len(ids) != len(sources):
        raise PolicyUnavailable("lock rule IDs and sources are incomplete")
    if len(ids) != len(set(ids)):
        raise PolicyUnavailable("lock contains duplicate rule IDs")
    return tuple(
        RuleRef(id=rule_id, source=source) for rule_id, source in zip(ids, sources)
    )


def load_policy_view(project_root: Path, policy_root: Path) -> PolicyView:
    manifest_path = project_root / ".architecture" / "manifest.yaml"
    lock_path = project_root / ".architecture" / "lock.yaml"
    if not manifest_path.is_file() or not lock_path.is_file():
        raise PolicyUnavailable("manifest.yaml and lock.yaml are required")

    manifest = manifest_path.read_text(encoding="utf-8")
    lock = lock_path.read_text(encoding="utf-8")
    manifest_source = _policy_field(manifest, "source")
    manifest_version = _policy_field(manifest, "version")
    lock_source = _policy_field(lock, "source")
    lock_version = _policy_field(lock, "version")
    if manifest_source != lock_source or manifest_version != lock_version:
        raise PolicyUnavailable("manifest and lock policy identities differ")
    if not re.search(r"(?m)^generated:\s*true\s*$", lock):
        raise PolicyUnavailable("lock is not marked generated")

    tag = f"v{lock_version}"
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{tag}^{{commit}}"],
        cwd=policy_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise PolicyUnavailable(f"pinned policy tag {tag} is unavailable locally")

    expected_manifest_digest = _top_level_field(lock, "manifest_digest")
    actual_manifest_digest = f"sha256:{hashlib.sha256(manifest.encode()).hexdigest()}"
    if expected_manifest_digest != actual_manifest_digest:
        raise PolicyUnavailable("manifest digest differs from the lock")

    expected_policy_digest = _top_level_field(lock, "policy_digest")
    actual_policy_digest = _policy_digest(policy_root, tag)
    if expected_policy_digest != actual_policy_digest:
        raise PolicyUnavailable("pinned policy digest differs from the lock")

    return PolicyView(
        source=lock_source,
        version=lock_version,
        rules=_lock_rules(lock),
        tag=tag,
    )


def load_rule_card(policy_root: Path, view: PolicyView, rule: RuleRef) -> RuleCard:
    result = subprocess.run(
        ["git", "show", f"{view.tag}:{rule.source}"],
        cwd=policy_root,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise PolicyUnavailable(f"{rule.id} source is unavailable at {view.tag}")
    frontmatter = result.stdout.split("---", 2)
    if len(frontmatter) < 3:
        raise PolicyUnavailable(f"{rule.id} front matter is malformed")
    fields: dict[str, str] = {}
    for line in frontmatter[1].splitlines():
        key, separator, value = line.partition(":")
        if separator and key in {"id", "title", "condition", "statement", "evidence"}:
            fields[key] = value.strip().strip("'\"")
    if fields.get("id") != rule.id:
        raise PolicyUnavailable(f"{rule.id} source identity differs from the lock")
    return RuleCard(
        id=rule.id,
        title=fields.get("title", "untitled rule"),
        condition=fields.get("condition", "condition unavailable"),
        statement=fields.get("statement", "statement unavailable"),
        evidence=fields.get("evidence", "evidence unavailable"),
    )
