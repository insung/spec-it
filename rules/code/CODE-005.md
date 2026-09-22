---
id: CODE-005
title: Configuration boundaries use named typed contracts
status: active
introduced: 0.6.0
scope: project-owned-configuration
condition: "Project-owned configuration leaves parsing or loading code and crosses a layer, module, package, composition, or runtime-consumer boundary."
statement: "MUST expose the allowed fields, value types, optionality, and default semantics through a named contract that consumers can discover without choosing string keys or conversion methods."
forbidden: ["Pass a raw string map across a project-owned configuration boundary.", "Make each consumer select a string key and conversion method to reveal the field's type or meaning.", "Treat a class that only wraps an untyped map with generic accessors as a typed configuration contract."]
evidence: ["Boundary review identifies the named configuration contract, its fields and types, the loader-to-contract mapping, and the consumers that receive it."]
exception: {allowed: true, requirements: ["A raw map is contained inside a parser, loader, or external-library adapter and does not cross into runtime consumers; any externally required dynamic shape is isolated and documented at that boundary."]}
approver: [architecture-owner]
rationale: "A named typed configuration contract makes invalid combinations and conversion ownership visible before runtime consumers depend on implicit string knowledge."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# CODE-005 — Named configuration contracts

환경 변수, `.env`, secret store 또는 원격 설정을 처음 읽는 adapter 내부에서는 문자열 map을 사용할 수 있습니다. 파싱이 끝나 composition root나 runtime consumer로 전달할 때는 허용 필드, 타입, 선택 여부와 기본값 의미를 이름 있는 계약으로 바꿉니다.

이 규칙은 특정 구현 도구를 강제하지 않습니다. 언어와 프로젝트는 immutable settings object, record, dataclass, validated model 등 적절한 표현을 선택할 수 있습니다. 이름 있는 `Config` 클래스라도 소비자가 `get("PORT")`, `int_of("PORT")`처럼 키와 변환 방법을 매번 선택해야 한다면 계약의 타입 의미가 경계에 드러나지 않으므로 충족하지 않습니다.
