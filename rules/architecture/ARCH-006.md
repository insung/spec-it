---
id: ARCH-006
title: Explicit transport to application mapping
status: active
introduced: 0.2.0
scope: application-boundaries
condition: "A transport adapter accepts input or returns output across an application boundary."
statement: "MUST represent transport contracts and application commands, queries, and results as distinct types and map them explicitly at the adapter boundary."
forbidden: ["Pass an HTTP, RPC, message, or WebSocket DTO into the application or domain as its input type.", "Expose a domain entity directly as a transport response.", "Let serializer, validation-framework, or transport annotations enter the domain core."]
evidence: ["Boundary map identifies transport types, application types, mapping ownership, validation ownership, and tests for both directions.", "Dependency review shows transport and serialization types stop at the adapter boundary."]
exception: {allowed: true, requirements: ["Architecture-owner records the bounded prototype or generated-code boundary, coupling impact, and removal or review trigger under GOV-003."]}
approver: [architecture-owner]
rationale: "Separate boundary types prevent an accidental wire-format change from silently redefining application and domain policy."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# ARCH-006 — Transport mapping boundary

0.2.0에 도입되었습니다. 구조가 같아도 같은 클래스나 schema 객체를 양쪽 경계에서 재사용하지 않습니다. 복사는 목적이 아니라 결합 방지가 목적이므로 mapper는 작게 유지하거나 계약에서 생성할 수 있습니다.

transport DTO는 파싱·형식·전송 인증과 공개 필드를 소유합니다. application command/query는 유스케이스의 의도와 필요한 값만 표현합니다. domain value object와 entity는 업무 불변식을 소유합니다. `services/`라는 디렉터리 이름은 어느 경계인지 판정하는 근거가 아닙니다.

프로토콜이 바뀌어도 이 경계는 유지됩니다. HTTP JSON, protobuf RPC, 이벤트, WebSocket adapter가 같은 application input으로 각각 매핑될 수 있습니다. 자동 검증은 미구현이며 Phase 0 판정은 `human-review`입니다.
