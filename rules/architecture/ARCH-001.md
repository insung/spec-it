---
id: ARCH-001
title: Dependencies point toward domain policy
status: active
introduced: 0.1.0
scope: application-architecture
condition: "Code separates domain, application, and external adapters."
statement: "MUST keep domain policy independent of framework, persistence, transport, and telemetry SDKs."
forbidden: ["Import vendor SDKs into the domain core.", "Let adapters own business decisions."]
evidence: ["Dependency review or architecture test shows inward dependencies."]
exception: {allowed: true, requirements: ["Measured benefit and coupling impact in ADR."]}
approver: [architecture-owner]
rationale: "Stable domain policy should not change with volatile delivery mechanisms."
origin: {type: clean-architecture-adaptation}
enforcement: {mode: validator, implementation: planned}
---

# ARCH-001 — Inward dependencies

프레임워크를 쓰지 않는 것이 목표가 아니라 프레임워크가 업무 의미를 소유하지 않게 하는 것이 목표입니다.
