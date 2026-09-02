# Compatibility and migrations

공개 API, 이벤트, DB schema는 하위 호환을 기본 방향으로 봅니다. breaking change에는 사람 승인, 버전 변화, migration, rollback이 함께 설계됩니다. 이 원칙은 아무 변화도 허용하지 않는다는 뜻이 아니라 소비자와 데이터의 전환 비용을 변경의 일부로 취급한다는 뜻입니다.

정본 규칙: [COMP-001](../rules/compatibility/COMP-001.md).
