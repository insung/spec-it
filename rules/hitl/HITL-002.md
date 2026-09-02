---
id: HITL-002
title: Human decision package
status: active
introduced: 0.1.0
scope: agent-work
condition: "An agent requests a material human decision."
statement: "MUST present options, recommendation, impact, risk, expected diff, rollback, and evidence."
forbidden: ["Ask an unbounded question without researched options when facts are discoverable."]
evidence: ["Decision request contains all required fields or marks a field not applicable with reason."]
exception: {allowed: true, requirements: ["Emergency context and omitted fields are recorded."]}
approver: [intent-owner]
rationale: "A bounded decision package minimizes human interruption cost."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# HITL-002 — Decision package

사실 조사와 선택지 축소는 AI의 책임이고 가치·위험의 최종 선택은 사람의 책임입니다.
