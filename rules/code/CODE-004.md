---
id: CODE-004
title: Business results and layer boundaries use named data contracts
status: draft
introduced: 0.2.0
scope: project-owned-business-data
condition: "A project-owned callable returns business data, or project-owned data crosses a layer, module, package, process, transport, persistence, or public callable boundary."
statement: "MUST represent the result or boundary data with a named contract whose fields and meaning can be discovered without positional or implicit dictionary knowledge."
forbidden: ["Return an unnamed tuple or ad hoc dictionary as business data from a project-owned callable.", "Pass unnamed business data across a layer boundary.", "Reuse a transport DTO as an application contract solely because its current fields happen to match."]
evidence: ["Callable and boundary review identifies the named request, result, value object, schema, or approved external contract and its mapping responsibility."]
exception: {allowed: true, requirements: ["A private local helper returns a mechanically obvious value that does not cross a layer or ownership boundary, or an external protocol requires the shape; containment is explicit and any broader business-data exception is approved."]}
approver: [architecture-owner]
rationale: "Named boundary data remains understandable when agents inspect only the local caller or callee and when contracts evolve independently."
origin: {type: clean-architecture-adaptation}
enforcement: {mode: validator, implementation: planned}
---

# CODE-004 — Named boundary values

계층 내부의 짧은 private helper에서 기계적으로 명백하고 즉시 소비되는 tuple 또는 dictionary까지 금지하지 않습니다. 일반 project-owned callable이 business result를 반환하거나 controller→application service, application→domain, domain→adapter, package API, event, persistence mapping처럼 소유권이나 의미가 바뀌는 경계에서는 이름 있는 계약을 사용합니다. 계층 경계에는 local-helper 예외를 적용하지 않습니다.

외부 JSON DTO와 application input이 같은 필드를 가지더라도 기본적으로 별도 역할입니다. 실제로 동일한 타입을 공유하려면 두 경계가 같은 소유권·변경 이유·검증·오류 의미를 가진다는 근거가 필요합니다.
