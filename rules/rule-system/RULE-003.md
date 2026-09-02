---
id: RULE-003
title: Risk-based evidence freshness
status: active
introduced: 0.1.0
scope: time-sensitive-evidence
condition: "Evidence can become stale, including scans, restore tests, and load tests."
statement: "MUST define validity or rerun triggers by risk profile and material changes rather than one global period."
forbidden: ["Treat stale evidence as current because no global expiry exists."]
evidence: ["Profile declares freshness or rerun triggers; lock resolves them."]
exception: {allowed: true, requirements: ["Human-review records current risk and next trigger."]}
approver: [architecture-owner]
rationale: "Evidence ages at different rates according to risk and system change."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# RULE-003 — Evidence freshness

고정된 공통 기간을 만들지 않습니다.
