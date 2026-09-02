---
id: TOOL-003
title: Ephemeral and redacted check reports
status: active
introduced: 0.1.0
scope: spec-it-check
condition: "A check report is generated."
statement: "MUST write it under .spec-it/reports, exclude that directory from Git, and redact secret values."
forbidden: ["Record raw secret text.", "Commit routine local reports.", "Automatically delete reports in Phase 0."]
evidence: ["Gitignore entry and report fields contain only rule ID, path, line, finding type, masked fingerprint, and remediation for secret findings."]
exception: {allowed: true, requirements: ["ADR or release references commit, digest, or CI artifact URL instead of committing raw report."]}
approver: [security-owner]
rationale: "Reports are useful evidence but can leak secrets and create repository noise."
origin: {type: design-interview}
enforcement: {mode: ci, implementation: planned}
---

# TOOL-003 — Report handling

권장 파일명은 `YYYY-MM-DDTHH-mm-ssZ_<commit>_<mode>.json`입니다. 자동 정리는 Phase 0 범위가 아닙니다.
