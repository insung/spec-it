---
id: ARCH-002
title: Organize modules by feature or domain
status: active
introduced: 0.1.0
scope: application-architecture
condition: "A project contains multiple business capabilities."
statement: "SHOULD organize top-level modules by feature or domain boundary before technical layer."
forbidden: ["Create a repository-wide services or utils bucket without a bounded responsibility."]
evidence: ["Project map identifies capability ownership and external boundaries."]
exception: {allowed: true, requirements: ["Reason and navigation impact."]}
approver: [architecture-owner]
rationale: "Feature boundaries preserve cohesion and give AI a smaller change surface."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# ARCH-002 — Feature or domain modules

작은 Lambda의 평면 구조는 [PROJ-002](../project/PROJ-002.md)가 구체화합니다.
