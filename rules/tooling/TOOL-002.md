---
id: TOOL-002
title: Deterministic resolved lock
status: active
introduced: 0.1.0
scope: project-projection
condition: "A manifest is converged into lock.yaml."
statement: "MUST generate byte-identical lock output from the same exact policy version and manifest input."
forbidden: ["Include timestamps or machine-specific paths.", "Hand-edit generated lock content."]
evidence: ["Repeat-generation byte comparison and generated-file marker."]
exception: {allowed: false, requirements: []}
approver: [architecture-owner]
rationale: "Determinism makes policy resolution reviewable and reproducible across agents."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# TOOL-002 — Deterministic lock

정렬과 serialization 규칙은 Phase 1 generator에서 고정합니다. Phase 0 fixture는 그 목표 형식을 보여줍니다.
