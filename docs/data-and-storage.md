# Data and storage

관계, 트랜잭션, ad-hoc query가 중심이면 RDS를 기본 비교점으로 삼습니다. DynamoDB는 검증된 access pattern, 규모, 지연, 가용성, 비용 근거가 있을 때 선택합니다. Redis는 정본이 아닌 파생·임시 상태에 사용하고 손실과 stale 허용 범위를 선언합니다.

저장소 선택은 제품의 사용자·회사·권한 같은 업무 데이터 모델과 읽기·쓰기 패턴을 먼저 정의한 뒤 프로젝트에서 확정합니다. OpenSearch는 검색·분석 요구가 정당화할 때, Kinesis와 Kafka는 소비자 모델·재생 기간·생태계·운영비를 비교해 프로필로 선택합니다.

진단 로그는 구조화 JSON 또는 OpenTelemetry를 기본 비교점으로 두고, 장기 이벤트 계약은 Avro·Protobuf·JSON Schema 중 호환성 요구에 맞춰 선택합니다. CSV는 운영 이벤트 계약의 기본값이 아닙니다.

DB schema·routine·reference data·backfill 변경은 [DATA-009](../rules/data/DATA-009.md)에 따라 versioned release unit으로 관리합니다. SQL 정본의 위치와 실행 도구는 프로젝트가 선택하지만 checksum, 소유권, application compatibility, environment history와 recovery class는 재현 가능해야 합니다. 자세한 적용 방법은 [DB 변경 배포](database-change-delivery.md)를 봅니다.

새로 소유하는 관계형 DB identifier는 [DATA-010](../rules/data/DATA-010.md)에 따라 schema·table·column과 다른 객체 category별 convention을 선언합니다. 공통 정책이 한 casing을 모든 engine에 강제하지는 않지만, 한 소유 경계에서 선언 없이 섞지 않습니다. legacy·외부 소유 identifier는 원래 계약을 보존하고 project-owned adapter나 mapping에서 연결합니다.

정본 규칙: [DATA-001](../rules/data/DATA-001.md), [DATA-002](../rules/data/DATA-002.md), [DATA-003](../rules/data/DATA-003.md), [DATA-004](../rules/data/DATA-004.md), [DATA-005](../rules/data/DATA-005.md), [DATA-006](../rules/data/DATA-006.md), [DATA-009](../rules/data/DATA-009.md), [DATA-010](../rules/data/DATA-010.md).
