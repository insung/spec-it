# Observability

관측 가능성은 애플리케이션 경계의 구조화 로그와 correlation ID에서 시작합니다. trace와 metric의 범위는 프로젝트 위험과 운영 프로필이 정합니다.

도메인 코어가 OpenTelemetry SDK를 직접 호출하는 방식은 피합니다. 예를 들어 RTB의 `NoAd` 원인은 도메인이 타입이 있는 결정 이유로 반환하고, application 또는 adapter가 이를 span attribute, metric, log로 변환합니다. 이 구분은 “도메인 판단을 관측하지 않는다”가 아니라 “관측 도구가 도메인 의미를 소유하지 않는다”는 뜻입니다.

사용자·회사·권한처럼 서비스가 소유하는 업무 정보는 telemetry metadata가 아니라 업무 데이터 저장소의 대상입니다.

정기 data pipeline은 process log만이 아니라 terminal output의 freshness·completeness·integrity와 reconciliation을 관측합니다. [OBS-003](../rules/observability/OBS-003.md)은 run ledger, accountable alert와 dependency-aware replay evidence를 요구하며, 구체적인 threshold와 정상 빈 결과의 의미는 프로젝트가 정합니다. 자세한 적용 방법은 [데이터 파이프라인 운영](data-pipeline-operations.md)을 봅니다.

정본 규칙: [OBS-001](../rules/observability/OBS-001.md), [OBS-002](../rules/observability/OBS-002.md), [OBS-003](../rules/observability/OBS-003.md).

## 사용자 안내와 진단의 분리

[MSG-001](../rules/messages/MSG-001.md), [MSG-002](../rules/messages/MSG-002.md)는 내부 원인과 공개 결과를 분리합니다. API는 안전한 code·parameter·요청 추적 식별자를, 표현 계층은 사용자 안내를, 운영 경계는 비밀정보가 제거된 진단을 담당합니다. 예상된 한도 거절은 반드시 error 로그나 운영 알림을 뜻하지 않습니다. 기록 수준·샘플링·알림 조건은 프로젝트의 위험과 비용에 따라 정합니다.

후속 작업은 로그를 파싱해서 실행하지 않습니다. [ARCH-005](../rules/architecture/ARCH-005.md)의 전달·재시도 정책과 실제 작업 상태가 정본입니다. 자세한 계약과 검증 흐름은 [사용자 메시지와 오류](user-messages-and-errors.md)를 봅니다.
