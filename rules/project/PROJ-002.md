---
id: PROJ-002
title: Python Lambda layout
status: active
introduced: 0.1.0
scope: python-aws-lambda
condition: "A deploy unit selects python, aws-lambda, and sam profiles."
statement: "MUST keep handler.py and feature directories without src depth and place deployment definitions in visible deploy/."
forbidden: ["Hide deployment definitions in .deploy/.", "Introduce src/ in the Lambda deploy unit."]
evidence: ["Repository tree matches the selected profile template."]
exception: {allowed: true, requirements: ["External packaging constraint, impact, and architecture-owner approval."]}
approver: [architecture-owner]
rationale: "A fixed shallow Lambda structure reduces navigation and AI interpretation cost."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# PROJ-002 — Lambda layout

규모가 커져도 이 profile을 선택한 deploy unit은 구조를 유지하고, 크기 문제는 모듈 경계나 deploy unit 분리로 해결합니다.
