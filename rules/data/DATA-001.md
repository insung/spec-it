---
id: DATA-001
title: RDS is the relational default comparison
status: active
introduced: 0.1.0
scope: primary-data-store
condition: "Business data has relationships, transactions, or evolving query needs."
statement: "SHOULD use RDS as the default comparison option."
forbidden: ["Select a non-relational store without comparing transaction and query costs."]
evidence: ["Storage ADR includes data model, queries, consistency, scale, and cost."]
exception: {allowed: true, requirements: ["Reason and impact are recorded."]}
approver: [data-owner, architecture-owner]
rationale: "Relational storage is the safer default for business identity, company, and permission data."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# DATA-001 — Relational default

기본 비교점은 자동 선택이 아니라 다른 선택이 설명해야 할 기준입니다.
