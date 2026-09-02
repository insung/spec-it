---
id: HITL-001
title: Mandatory human stop conditions
status: active
introduced: 0.1.0
scope: agent-work
condition: "Ambiguity or conflict affects observable behavior, public contract, security, data, cost, or infrastructure."
statement: "MUST stop before mutation and request human judgment."
forbidden: ["Guess a material requirement.", "Hide uncertainty behind a test written from the same guess."]
evidence: ["Open decision identifies affected category and blocking question."]
exception: {allowed: false, requirements: []}
approver: [intent-owner]
rationale: "Material intent and risk remain human responsibilities."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# HITL-001 — Mandatory stop

권한 순서와 기존 증거로 명확히 해소되는 단순 충돌은 중단 조건이 아닙니다.
