---
id: INFRA-002
title: Re-evaluate infrastructure on material change signals
status: active
introduced: 0.2.0
scope: agent-assisted-implementation
condition: "A task starts, a material infrastructure signal appears, implementation finishes, or changed files enter policy CI."
statement: "MUST re-evaluate applicable infrastructure profiles at the bounded checkpoints and continue without interruption when approved decisions and guardrails still cover the change."
forbidden: ["Install a hidden per-save hook or always-on watcher by default.", "Interrupt the human for a trigger already covered by an approved decision and guardrail.", "Continue silently when a new decision, rule conflict, hard constraint, or approved budget is exceeded."]
evidence: ["Task report links the trigger to an existing decision or records the human decision, exception, or required evidence before completion."]
exception: {allowed: true, requirements: ["A repository-owned tool uses a different documented checkpoint strategy with equivalent coverage and measured lower total cost."]}
approver: [architecture-owner, intent-owner]
rationale: "Bounded re-evaluation catches infrastructure drift while avoiding the cost and noise of checking every edit."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# INFRA-002 — Bounded re-evaluation

기본 checkpoint는 작업 시작 preflight, 구현 중 새 dependency·import·IaC·environment setting·external client·storage payload 발견, 완료 전 diff 검사, CI changed-file 검사입니다. 기존 결정 안이면 보고만 하고 계속합니다. 미결정·충돌·보안·데이터·가용성 hard constraint 또는 비용 예산 초과가 있을 때만 사람에게 판단 package를 제시합니다.
