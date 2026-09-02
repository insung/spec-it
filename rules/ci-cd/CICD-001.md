---
id: CICD-001
title: Separate quality CI from deployment pipeline
status: active
introduced: 0.1.0
scope: delivery
condition: "A repository has automated delivery."
statement: "SHOULD separate pull-request quality checks from environment deployment while promoting the same immutable artifact."
forbidden: ["Rebuild different source for each environment without traceability."]
evidence: ["Pipeline map links commit, artifact digest, checks, and deployment."]
exception: {allowed: true, requirements: ["Single-stage project reason and rollback method."]}
approver: [architecture-owner]
rationale: "Separation keeps review feedback fast while preserving deployment traceability."
origin: {type: design-interview}
enforcement: {mode: ci, implementation: planned}
---

# CICD-001 — Quality and deployment roles

GitHub Actions와 AWS CodePipeline 계열은 가능한 구현 예이며 공통 규칙의 고정 제품명이 아닙니다.
