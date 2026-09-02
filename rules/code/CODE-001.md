---
id: CODE-001
title: Comments explain contracts and reasons
status: active
introduced: 0.1.0
scope: source-code
condition: "A comment or API documentation is added or changed."
statement: "MUST document public contracts and SHOULD comment only reasons, constraints, or non-obvious decisions after simplifying structure."
forbidden: ["Restate code line by line.", "Use comments to compensate for avoidable branching or poor names."]
evidence: ["Review distinguishes contract documentation from implementation rationale."]
exception: {allowed: true, requirements: ["Generated or teaching code context."]}
approver: [architecture-owner]
rationale: "Reason-focused comments remain useful after implementation details change."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# CODE-001 — Useful comments

Python docstring과 Go exported comment의 세부 형식은 language profile이 정의합니다.
