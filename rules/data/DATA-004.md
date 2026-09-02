---
id: DATA-004
title: Explicit data lifecycle
status: active
introduced: 0.1.0
scope: stored-data
condition: "A system stores or transmits data."
statement: "MUST record classification, owner, retention, deletion method, and access-audit requirement for each data class."
forbidden: ["Use indefinite retention as an implicit default.", "Treat business identity data as telemetry metadata."]
evidence: ["Data inventory or manifest reference covers every stored data class."]
exception: {allowed: true, requirements: ["Reason, approver, impact, and review trigger."]}
approver: [data-owner, security-owner]
rationale: "Unowned data accumulates cost, privacy risk, and deletion ambiguity."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# DATA-004 — Data lifecycle

무기한 보존이 실제 요구라면 명시적인 승인 대상입니다.
