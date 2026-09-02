---
id: COST-001
title: Absolute constraints precede cost
status: active
introduced: 0.1.0
scope: architecture-decisions
condition: "Options are compared."
statement: "MUST reject options that violate security, law, data integrity, or approved reliability limits before cost ranking."
forbidden: ["Trade an absolute constraint for lower spend without an approved policy exception."]
evidence: ["Decision record lists hard constraints before option cost."]
exception: {allowed: true, requirements: ["Rule-specific approved exception where legally permitted."]}
approver: [security-owner, data-owner, intent-owner]
rationale: "Cost optimization is valid only inside the safe and lawful solution space."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# COST-001 — Absolute constraints first

안전·법·무결성·합의된 신뢰성 한계를 통과한 선택지만 총비용 비교 대상이 됩니다.
