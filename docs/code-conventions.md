# Code conventions

코딩 컨벤션은 모든 언어의 표면 문법을 하나로 만드는 규칙이 아닙니다. spec-it은 사람이 읽고 AI가 검색할 때 필요한 **공통 의미**를 정하고, casing·파일 배치·formatter·linter 같은 표면 규칙은 language profile과 프로젝트 설정이 정합니다. 같은 원칙은 backend, frontend, CLI와 이후 추가될 embedded profile에도 적용할 수 있습니다.

## 공통 계약

- 프로젝트가 소유하는 코드 식별자와 structured log key는 영어를 사용합니다. 표시 문구와 번역 resource는 사용자 언어를 따릅니다.
- 이름은 역할·행위·대상·cardinality를 드러냅니다. `data`, `info`, `obj`, `get_A`처럼 주변 구현을 읽어야만 알 수 있는 이름은 사용하지 않습니다.
- callable은 행동이면 동사에서 시작합니다. predicate, validation, verification, conversion, event handler처럼 관용 prefix가 의미를 전달하는 경우도 동사 역할로 봅니다.
- collection 이름은 자연스러운 복수형을 사용합니다. container type을 반복하지 않으며 실제 `UserCollection` domain type 같은 경우만 예외입니다.
- project-owned callable의 business result와 계층·소유권 경계는 이름 있는 계약을 사용합니다. 짧은 private local helper의 기계적 값만 제한적으로 예외가 될 수 있으며, 계층 경계에는 그 예외를 적용하지 않습니다. 외부 DTO와 application input은 필드가 같다는 이유만으로 자동 통합하지 않습니다.

상세 동사 사전과 `list` 예외는 [CODE-003](../rules/code/CODE-003.md), 경계 데이터는 [CODE-004](../rules/code/CODE-004.md)를 따릅니다.

## 언어와 도구의 책임

예를 들어 Python은 `snake_case`, Kotlin과 TypeScript는 각 생태계의 공식 관례를 사용할 수 있습니다. 공통 정책은 그 차이를 오류로 만들지 않습니다. 대신 각 실행 단위가 formatter, linter/static analyzer, 필요한 type checker, 설정 위치, 실행 명령, 검사 범위와 CI 목표 상태를 선언합니다.

성숙한 linter가 없는 언어도 있을 수 있습니다. 그 경우 컴파일러 경고, formatter, 정적 분석, 제한된 수동 review 등 대체 증거와 재검토 조건을 승인받습니다. 도구 부재를 이유로 의미 규칙 자체가 사라지지는 않습니다.

## Brownfield 적용

기존의 한글·모호한 이름을 즉시 일괄 변경하지 않습니다. `spec-it:check`는 변경된 코드의 새 위반은 실패 후보로, 기존 위반은 위치·영향·안전한 수정 경계를 포함한 지속적인 개선 report로 구분합니다. 기존 이름을 실제로 수정할 때는 caller, serialization, reflection, framework binding, public API와 migration 영향을 먼저 확인합니다.

정본 규칙: [CODE-001](../rules/code/CODE-001.md), [CODE-002](../rules/code/CODE-002.md), [CODE-003](../rules/code/CODE-003.md), [CODE-004](../rules/code/CODE-004.md), [TOOL-005](../rules/tooling/TOOL-005.md).
