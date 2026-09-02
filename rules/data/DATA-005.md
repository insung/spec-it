---
id: DATA-005
title: Versioned event contracts
status: active
introduced: 0.1.0
scope: durable-events
condition: "An event is consumed across a deploy, team, or retention boundary."
statement: "MUST define a versioned schema and compatibility policy using Avro, Protobuf, JSON Schema, or an approved equivalent."
forbidden: ["Use CSV as the default service event contract.", "Publish unversioned free-form JSON across a durable boundary."]
evidence: ["Schema artifact, owner, compatibility mode, and producer-consumer contract test."]
exception: {allowed: true, requirements: ["Short-lived internal use, owner, removal trigger, and impact."]}
approver: [data-owner, architecture-owner]
rationale: "Durable events outlive producers and need explicit evolution rules."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# DATA-005 — Event contracts

포맷은 생태계, schema evolution, payload, 언어와 운영비로 선택합니다. Avro는 가능한 기본 후보이지 모든 로그의 고정 포맷이 아닙니다.
