---
id: CODE-003
title: Names communicate role and cardinality
status: draft
introduced: 0.2.0
scope: project-owned-source
condition: "A project-owned callable, type, component, collection, boolean, event handler, or conversion identifier is added or changed."
statement: "MUST name the identifier for its observable role, action, subject, and cardinality using the selected language profile's syntax."
forbidden: ["Use placeholders such as get_A, data, info, obj, or manager without a specific domain role.", "Encode a container type such as list or collection when plurality already communicates cardinality and the container is not a domain concept.", "Use check, validate, or verify interchangeably when their outcomes or side effects differ."]
evidence: ["Changed-name review maps each identifier to the semantic vocabulary and the language profile's official casing and syntax."]
exception: {allowed: true, requirements: ["Generated, framework-required, external-contract, test-fixture, or narrowly scoped conventional name and its boundary are evident or recorded."]}
approver: [architecture-owner]
rationale: "Stable semantic distinctions let readers and agents predict behavior without opening every implementation."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# CODE-003 — Semantic naming

공통 의미는 다음과 같습니다. 언어별 casing과 관용 표기는 language profile이 정합니다.

| Form | Meaning |
| --- | --- |
| `get_<singular>` | 식별되거나 유일한 한 값을 조회하며 없음 처리 계약을 가짐 |
| `get_<plural>` | 조건에 맞는 복수 값을 조회 |
| `get_<plural>_by_<criterion>` | 복수 조회의 선택 기준을 이름에 드러냄 |
| `search_<plural>` | 검색어·ranking·복합 조건처럼 검색 의미가 있음 |
| `list_<plural>` | 외부 표준·SDK·framework 또는 프로젝트가 명시적으로 채택한 collection enumeration convention |
| `is_<state>` | 주어 자체의 현재 상태 판정 |
| `has_<noun>` | 주어가 값·관계·능력을 보유하는지 판정 |
| `can_<verb>` | 현재 조건에서 행위를 수행할 수 있는지 판정 |
| `should_<verb>` | 정책·전략상 행위를 선택해야 하는지 판정 |
| `check_<noun>` | 상태를 검사하고 결과·진단을 반환할 수 있음 |
| `validate_<noun>` | 입력이나 상태가 선언된 규칙에 맞는지 판정하고 실패 계약을 가짐 |
| `verify_<noun>` | 외부 증거나 실제 결과를 기대값과 대조해 확인 |
| `to_<target>` / `from_<source>` | 표현 간 변환 |
| `on_<event>` | framework나 UI event handler |

`get_users_collection`은 기본적으로 사용하지 않습니다. `UserCollection` 자체가 실제 domain type이면 `get_user_collection`처럼 그 개념을 이름에 사용할 수 있습니다. `list_users`는 금지어가 아니라 선택된 외부 표준 또는 프로젝트 관례가 있을 때만 사용합니다.

복수 값은 언어가 허용하는 자연스러운 복수형으로 cardinality를 드러냅니다. 단순히 마지막 글자 `s`를 기계적으로 검사하지 않으며 `people`, `children` 같은 불규칙 복수와 domain vocabulary를 허용합니다.
