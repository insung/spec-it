# Compatibility and migrations

공개 API, 이벤트, DB schema는 하위 호환을 기본 방향으로 봅니다. breaking change에는 사람 승인, 버전 변화, migration, rollback이 함께 설계됩니다. 이 원칙은 아무 변화도 허용하지 않는다는 뜻이 아니라 소비자와 데이터의 전환 비용을 변경의 일부로 취급한다는 뜻입니다.

정본 규칙: [COMP-001](../rules/compatibility/COMP-001.md).

## 결과 계약과 DB 루틴 — 미발행 0.2.0 초안

[MSG-001](../rules/messages/MSG-001.md)은 stable code·parameter 타입·안전한 fallback을 연결합니다. 프론트·백엔드는 구현 코드를 공유하지 않고 언어 중립 계약을 따를 수 있지만 계약 의존성 자체는 남습니다. 새 code를 추가할 때도 구버전 소비자를 검사하며 생성된 타입만으로 실행 중인 구버전의 안전을 주장하지 않습니다. 형태가 같아도 한도·권한·상태 전이 의미가 바뀌면 동작 계약을 다시 검토합니다.

[DATA-007](../rules/data/DATA-007.md)에 따라 SQL migration과 구·신 호출자의 인수/반환 형태를 함께 검사합니다. DB DDL의 암묵적 commit과 이미 변한 데이터는 단순 rollback으로 복구되지 않을 수 있으므로 복원 또는 전진 수정 계획을 명시합니다. 프로시저 이름에 버전을 붙이는 것은 선택지이지 모든 DB에 강제할 이름 규칙이 아닙니다.

추가 의무가 있는 수정 프로필은 `0.2.0`의 `draft`입니다. 기존 `0.1.0` 프로젝트와 예제 manifest/lock은 그대로 둡니다. 정책 배포와 프로젝트별 재명확화·재수렴은 별도 승인 작업이며, 이 작업 트리를 `0.1.0` 정본으로 대신 사용하지 않습니다.

## 공유 core library — 미발행 0.2.0 초안

[COMP-002](../rules/compatibility/COMP-002.md)는 새 release 자체를 모든 consumer의 update 명령으로 취급하지 않습니다. library가 바꾼 capability와 동작을 공개하고, 각 알려진 consumer는 `update-required`, `update-planned`, `not-required`, `impact-unknown` 중 하나와 근거·owner·위험 기반 기한을 기록합니다.

버전 수정 PR의 merge와 운영 배포·검증을 같은 완료 상태로 보지 않습니다. 고정 dependency, consumer commit/lock, immutable build artifact, environment의 deployment identity, 실행 검증을 연결합니다. 자세한 판단과 시작 템플릿은 [공유 도메인 코어 라이브러리](domain-core-libraries.md)를 따릅니다.
