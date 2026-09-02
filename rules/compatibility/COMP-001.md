---
id: COMP-001
title: Backward-compatible public changes
status: active
introduced: 0.1.0
scope: public-contracts
condition: "A public API, event, or database schema changes."
statement: "MUST preserve backward compatibility or include human approval, version change, migration, and rollback plan."
forbidden: ["Ship an unversioned breaking change.", "Migrate data without rollback or irreversible-impact approval."]
evidence: ["Contract tests and compatibility or migration record."]
exception: {allowed: true, requirements: ["Breaking-change package and intent-owner approval."]}
approver: [intent-owner, data-owner]
rationale: "Consumer and data migration cost is part of the feature cost."
origin: {type: design-interview}
enforcement: {mode: ci, implementation: planned}
---

# COMP-001 — Compatibility by default

내부 구현 세부는 공개 계약이 아니며 profile이 계약 표면을 구체화합니다.
