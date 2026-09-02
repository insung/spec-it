---
id: ARCH-003
title: No speculative ports
status: active
introduced: 0.1.0
scope: application-architecture
condition: "A port, interface, or abstraction is proposed."
statement: "MUST justify it with a real second implementation, external-boundary isolation, or an approved replacement plan."
forbidden: ["Create abstraction only because replacement may happen someday."]
evidence: ["Change spec names the concrete variability or boundary."]
exception: {allowed: true, requirements: ["Architecture-owner records the learning goal and removal trigger."]}
approver: [architecture-owner]
rationale: "Unused abstractions add interpretation and maintenance cost."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# ARCH-003 — Evidence before abstraction

테스트 seam 자체가 실제 외부 경계를 격리하는 경우에는 근거가 될 수 있습니다.
