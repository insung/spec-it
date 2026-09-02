---
id: COST-002
title: Total cost is the primary optimization criterion
status: active
introduced: 0.1.0
scope: architecture-and-operations
condition: "Two or more acceptable options remain."
statement: "MUST compare money, human time, AI execution time, operations, change, and expected failure cost using project-stage weights."
forbidden: ["Use cloud price alone as total cost.", "Optimize performance without stating its cost impact."]
evidence: ["ADR or change spec contains a cost comparison and assumptions."]
exception: {allowed: true, requirements: ["Reason and impact are recorded."]}
approver: [intent-owner, architecture-owner]
rationale: "Cheap infrastructure can be expensive when implementation and operations time are ignored."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# COST-002 — Total cost

가중치는 프로젝트 단계와 위험 프로필에서 정합니다. 추정치는 범위와 불확실성을 함께 기록합니다.
