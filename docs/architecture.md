# Architecture

기본 방향은 기능·도메인 중심의 모듈화와 안쪽을 향하는 의존성입니다. 도메인 코어는 프레임워크, 저장소 SDK, telemetry SDK를 직접 알지 않고 명시적인 입력·출력·오류·결정 이유를 표현합니다.

언어는 이념으로 고정하지 않습니다. 코어의 정확성, 타입 안전성, 성능 요구, 생태계, 팀 숙련도, 경계 비용, 총비용을 비교합니다. Rust는 가능한 선택이고 Python은 데이터·AI 생태계가 결정적일 때 유효한 선택입니다.

미래에 바뀔 수 있다는 이유만으로 port나 공통 인터페이스를 만들지 않습니다. 실제 두 번째 구현, 외부 경계 격리, 명확한 교체 계획 중 근거가 있을 때 도입합니다.

정본 규칙: [ARCH-001](../rules/architecture/ARCH-001.md), [ARCH-002](../rules/architecture/ARCH-002.md), [ARCH-003](../rules/architecture/ARCH-003.md), [ARCH-004](../rules/architecture/ARCH-004.md).
