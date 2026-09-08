# Architecture

기본 방향은 기능·도메인 중심의 모듈화와 안쪽을 향하는 의존성입니다. 도메인 코어는 프레임워크, 저장소 SDK, telemetry SDK를 직접 알지 않고 명시적인 입력·출력·오류·결정 이유를 표현합니다.

언어는 이념으로 고정하지 않습니다. 코어의 정확성, 타입 안전성, 성능 요구, 생태계, 팀 숙련도, 경계 비용, 총비용을 비교합니다. Rust는 가능한 선택이고 Python은 데이터·AI 생태계가 결정적일 때 유효한 선택입니다.

미래에 바뀔 수 있다는 이유만으로 port나 공통 인터페이스를 만들지 않습니다. 실제 두 번째 구현, 외부 경계 격리, 명확한 교체 계획 중 근거가 있을 때 도입합니다.

정본 규칙: [ARCH-001](../rules/architecture/ARCH-001.md), [ARCH-002](../rules/architecture/ARCH-002.md), [ARCH-003](../rules/architecture/ARCH-003.md), [ARCH-004](../rules/architecture/ARCH-004.md).

## Transport DTO와 application 입력

[ARCH-006](../rules/architecture/ARCH-006.md)은 HTTP·RPC·event·WebSocket transport type과 application command/query/result를 별도 계약 타입으로 취급하고 adapter에서 명시적으로 매핑합니다. 형태가 같다는 것은 책임과 변경 이유가 같다는 뜻이 아니므로 동일 타입을 경계 양쪽에서 재사용하지 않습니다. domain entity도 응답 DTO로 직접 노출하지 않습니다.

이 구분은 파일이나 mapper 계층을 크게 만드는 규칙이 아닙니다. transport annotation과 공개 필드는 adapter에 남기고 application은 유스케이스 의도를 표현하는 최소 타입을 받게 하는 규칙입니다. 자세한 API 적용은 [API 설계와 전송 계약](api-design-and-lifecycle.md)을 따릅니다.

## 공유 domain core

공유 library는 별도 repository이기 때문에 core가 되는 것이 아니라 안쪽 의존성과 독립된 business policy를 유지할 때 core가 됩니다. 실제 독립 consumer가 없거나 동기화 비용이 크면 같은 repository module이 더 적합할 수 있습니다. 분리한 경우 [공유 도메인 코어 라이브러리](domain-core-libraries.md)와 [COMP-002](../rules/compatibility/COMP-002.md)가 release impact와 consumer별 update를 추적합니다.

## 트랜잭션과 DB 내부 실행

[ARCH-005](../rules/architecture/ARCH-005.md)는 업무 판단과 트랜잭션 조율을 구분합니다. 같은 DB 연결의 트랜잭션으로 여러 DML을 묶을 수 있으므로 프로시저는 원자성의 필수 조건이 아닙니다. 프로시저 호출이나 `BEGIN ... END` 블록만으로 원자성이 생기지도 않습니다. 제약조건·격리 수준·잠금 또는 조건부 갱신을 함께 검증합니다.

| 책임 | 기본 위치 |
| --- | --- |
| 자격·한도·가격·상태 전이 | 도메인 코드 |
| 작업 순서·트랜잭션·재시도·후속 작업 | 애플리케이션 |
| 조회·조인·대량 집계·일괄 갱신 | DB adapter와 SQL |
| 유일성·참조 무결성 | DB 제약조건 |
| 측정 근거·제한된 실행 권한·레거시 호환을 갖춘 DB 내부 실행 | 승인된 프로시저 |

[DATA-007](../rules/data/DATA-007.md)은 프로시저 허용 근거와 SQL 정의·호출자·소유권·권한·테스트·배포·복구를 연결합니다. 핵심 업무 판단을 SQL에 남기는 것은 ARCH-001 예외로 다루고 경쟁하는 정본을 만들지 않습니다. 대량 계산을 무조건 애플리케이션 메모리로 옮기거나 DB 무결성 제약을 없애는 방향이 아닙니다.

레거시는 먼저 정의와 호출자를 확보하고 목표 DB에서 현행 동작을 수용 사례로 고정합니다. 이후 변경 비용과 위험이 높은 판단부터 adapter 경계를 통해 점진적으로 이동합니다. 전환 중인 레거시를 새 규칙에 이미 준수한다고 처리하지 않습니다. 새 규칙은 기존 0.1.0 프로젝트에 자동 적용되지 않습니다.
