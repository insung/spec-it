---
id: TOOL-001
title: Read-only check contract
status: active
introduced: 0.1.0
scope: spec-it-check
condition: "A policy check is executed."
statement: "MUST be read-only, produce terminal and JSON output, use closed result states, and return defined exit codes."
forbidden: ["Modify project files during check.", "Mark missing evidence or unimplemented checks as pass."]
evidence: ["Check contract test and check-report schema validation."]
exception: {allowed: false, requirements: []}
approver: [architecture-owner]
rationale: "A predictable read-only checker is safe for local and CI use."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# TOOL-001 — Check contract

상태는 `pass`, `warn`, `fail`, `not-applicable`, `human-review`입니다. 종료 코드는 `0` 통과(경고 포함), `1` 정책 위반, `2` 사람 결정 또는 증거 누락, `3` 검사기 오류입니다. 모드는 `quick`, `full`, `release`입니다.
