# Reliability, recovery, and operations

상태를 보관하는 프로젝트는 RPO, RTO, backup, restore 방법과 운영 소유자를 프로젝트 manifest 또는 연결 문서에 기록합니다. 실제 restore test가 없는 백업은 복구 가능성이 입증된 것으로 보지 않습니다.

증거의 유효기간은 공통 고정 일수가 아니라 위험 등급, 변경 유형, 규제·운영 조건이 정합니다. 구조·권한·storage engine·복구 절차가 바뀌면 재검증 trigger가 됩니다.

정본 규칙: [REL-001](../rules/reliability/REL-001.md), [RULE-003](../rules/rule-system/RULE-003.md).
