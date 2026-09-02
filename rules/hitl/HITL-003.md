---
id: HITL-003
title: Bounded autonomous retries
status: active
introduced: 0.1.0
scope: agent-work
condition: "A test or implementation attempt fails repeatedly for the same objective."
statement: "MUST stop after two distinct tested hypotheses fail and present the evidence."
forbidden: ["Repeat the same attempt with cosmetic variation.", "Continue unbounded paid execution."]
evidence: ["Attempt log names two hypotheses, observations, and remaining blocker."]
exception: {allowed: true, requirements: ["Human authorizes a new bounded retry budget."]}
approver: [intent-owner]
rationale: "A hypothesis limit bounds time and compute while preserving useful autonomy."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# HITL-003 — Retry boundary

새 증거로 문제가 바뀌었다면 새 가설로 셀 수 있지만, 단순 재실행은 별도 가설이 아닙니다.
