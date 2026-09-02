---
id: ARCH-004
title: Select core language by constraints
status: active
introduced: 0.1.0
scope: language-selection
condition: "A project chooses or changes the language of core logic."
statement: "MUST compare correctness, type safety, performance, ecosystem, team skill, boundary cost, and total cost."
forbidden: ["Mandate Rust or Python for all core logic without project evidence."]
evidence: ["ADR records criteria, alternatives, and boundary implications."]
exception: {allowed: true, requirements: ["Organizational language mandate is referenced."]}
approver: [architecture-owner, intent-owner]
rationale: "Language value depends on workload and organizational constraints."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# ARCH-004 — Constraint-based language choice

Python의 데이터·AI 생태계와 Rust 같은 언어의 타입·성능 이점은 같은 비용 모델 안에서 비교합니다.
