---
id: INFRA-001
title: Infrastructure profiles expose decision evidence
status: active
introduced: 0.2.0
scope: infrastructure-profiles
condition: "A runtime, deployment, or capability profile declares the infrastructure trait."
statement: "MUST declare activation signals, required decisions, failure scenarios, cost drivers, measurements, guardrails, evidence stages, and revisit triggers."
forbidden: ["Select infrastructure from a product label alone.", "Describe performance without cost and operations evidence.", "Copy one project's numeric threshold into the common profile as a universal limit."]
evidence: ["The infrastructure profile validates with a complete evaluation block and the project records its risk-owned thresholds or explicit not-applicable reasons."]
exception: {allowed: false, requirements: []}
approver: [architecture-owner]
rationale: "A uniform evidence shape lets agents ask technology-specific questions without hard-coding one provider or one project's thresholds."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# INFRA-001 — Infrastructure evaluation contract

공통 프로필은 무엇을 관찰하고 어떤 판단을 내려야 하는지 정의합니다. 실제 숫자는 프로젝트 위험 등급, workload, SLO, 예산과 사용자의 승인으로 정합니다. `revisit_triggers`는 상시 hook이 아니라 기존 결정의 전제가 더는 유효하지 않을 수 있음을 나타내는 조건입니다.
