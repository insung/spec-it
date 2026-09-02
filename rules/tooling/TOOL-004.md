---
id: TOOL-004
title: Clarification progress is visible
status: active
introduced: 0.1.0
scope: spec-it-clarify
condition: "A clarification interview has unresolved decisions."
statement: "MUST show resolved count, open count, current decision frontier, and an estimated remaining-round range before each round."
forbidden: ["Present an unbounded sequence of questions without progress visibility.", "Continue asking after the human delegates remaining choices to stated recommendations."]
evidence: ["Clarification summary contains progress and recorded delegation scope."]
exception: {allowed: true, requirements: ["Single-decision clarification where the remaining count is self-evident."]}
approver: [intent-owner]
rationale: "Visible bounds let humans control interruption cost and decide when to delegate."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# TOOL-004 — Bounded clarification

예상 라운드는 확정치가 아니라 현재 의존성 그래프를 기준으로 한 범위입니다. 새 사실이 frontier를 늘리면 이유를 함께 알립니다.
