---
id: DATA-002
title: DynamoDB requires access-pattern evidence
status: active
introduced: 0.1.0
scope: primary-data-store
condition: "DynamoDB or another key-value primary store is proposed."
statement: "MUST document access patterns, key design, consistency, scale, hot-partition risk, and cost evidence."
forbidden: ["Select DynamoDB only because traffic may grow."]
evidence: ["Storage ADR and representative capacity estimate or pilot."]
exception: {allowed: true, requirements: ["Prototype purpose and exit criteria."]}
approver: [data-owner, architecture-owner]
rationale: "Key-value performance depends on known access patterns and disciplined key design."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# DATA-002 — Evidence for DynamoDB

규모가 작아도 serverless 운영비가 총비용을 낮춘다는 근거가 있으면 선택할 수 있습니다.
