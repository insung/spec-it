# Reliability, recovery, and operations

상태를 보관하는 프로젝트는 RPO, RTO, backup, restore 방법과 운영 소유자를 프로젝트 manifest 또는 연결 문서에 기록합니다. 실제 restore test가 없는 백업은 복구 가능성이 입증된 것으로 보지 않습니다.

증거의 유효기간은 공통 고정 일수가 아니라 위험 등급, 변경 유형, 규제·운영 조건이 정합니다. 구조·권한·storage engine·복구 절차가 바뀌면 재검증 trigger가 됩니다.

API 서버처럼 요청 시점을 통제할 수 없는 시스템도 플랫폼 이름만으로 가용성을 판정하지 않습니다. allowed downtime, replica와 failure domain, health/readiness, deployment loss budget, recovery path, traffic shape와 운영 소유자를 먼저 정합니다. EC2, Fargate, Kubernetes, serverless는 그 요구를 만족시키는 topology 후보이며 어느 이름도 단독으로 무중단을 보장하지 않습니다.

EC2 위 Docker Compose는 runtime과 deployment의 두 판단입니다. EC2 profile은 host 수, failure domain, traffic removal, process supervision과 patch·recovery 책임을 다루고, Compose profile은 immutable image, rendered config, healthcheck, drain, volume과 rollback을 다룹니다. Compose 파일이 유효하다는 증거는 host 장애를 견디는 topology의 증거가 아닙니다.

사람이 플랫폼을 선택해도 AI는 선택 이유가 실제 topology와 맞는지 검토하고, 불일치하면 반론과 대안을 제시합니다. 최종 선택은 사람이 하지만 승인된 hard constraint나 SLO를 만족하지 못한 상태는 수렴으로 기록하지 않습니다.

정본 규칙: [REL-001](../rules/reliability/REL-001.md), [REL-002](../rules/reliability/REL-002.md), [RULE-003](../rules/rule-system/RULE-003.md).
