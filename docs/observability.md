# Observability

관측 가능성은 애플리케이션 경계의 구조화 로그와 correlation ID에서 시작합니다. trace와 metric의 범위는 프로젝트 위험과 운영 프로필이 정합니다.

도메인 코어가 OpenTelemetry SDK를 직접 호출하는 방식은 피합니다. 예를 들어 RTB의 `NoAd` 원인은 도메인이 타입이 있는 결정 이유로 반환하고, application 또는 adapter가 이를 span attribute, metric, log로 변환합니다. 이 구분은 “도메인 판단을 관측하지 않는다”가 아니라 “관측 도구가 도메인 의미를 소유하지 않는다”는 뜻입니다.

사용자·회사·권한처럼 서비스가 소유하는 업무 정보는 telemetry metadata가 아니라 업무 데이터 저장소의 대상입니다.

정본 규칙: [OBS-001](../rules/observability/OBS-001.md), [OBS-002](../rules/observability/OBS-002.md).
