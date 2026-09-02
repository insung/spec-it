---
id: CICD-002
title: Mainline and artifact promotion
status: active
introduced: 0.1.0
scope: git-and-deployment
condition: "A repository deploys one or more units."
statement: "SHOULD use main, short-lived branches, path-based unit detection, independent deploy units, and artifact promotion."
forbidden: ["Create permanent environment branches per deploy unit in a growing monorepo."]
evidence: ["Branch and deployment strategy identifies triggers and artifact identity."]
exception: {allowed: true, requirements: ["Project-specific branch constraint and maintenance cost."]}
approver: [architecture-owner]
rationale: "Deploy branches multiply state and make monorepo releases difficult to reason about."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# CICD-002 — Mainline delivery

이 규칙의 monorepo 세부는 [PROJ-003](../project/PROJ-003.md)이 추가합니다.
