# API exposure and documentation — 미발행 0.2.0 초안

문서에 보이는가, 인터넷에서 도달 가능한가, 호출 권한이 있는가는 서로 다른 판단입니다. 같은 `internal`이라는 말로 세 가지를 대신하지 않습니다.

정본 규칙: [API-004](../rules/api/API-004.md), [API-005](../rules/api/API-005.md), [COMP-001](../rules/compatibility/COMP-001.md), [SEC-001](../rules/security/SEC-001.md), [TST-003](../rules/testing/TST-003.md), [TST-006](../rules/testing/TST-006.md).

## API inventory

각 contract 또는 API group은 다음을 식별합니다.

- audience: public, partner, internal 중 승인된 값.
- network exposure: public ingress, private network, local-only 등 실제 도달 경계.
- authentication과 authorization: 자격 증명 방식과 resource/action 권한.
- data classification과 tenant boundary.
- owner, canonical contract, version, support state.
- documentation projection, try-it 대상, example redaction.
- deprecation, replacement, migration, retirement evidence.

브라우저에서 사용하는 internal API는 public network에서 도달할 수 있습니다. private network도 인증·인가를 생략할 근거가 되지 않습니다.

## 공개 문서와 Scalar

OpenAPI는 HTTP 계약의 정본 또는 code-first 정본에서 생성된 기계 판독 projection입니다. Scalar는 승인된 OpenAPI를 보여주는 renderer이며 새 계약을 만들지 않습니다.

public 문서는 allowlist된 path와 schema만 포함합니다. 내부 endpoint를 UI에서 숨기는 것, tag를 감추는 것, 별도 URL을 모르게 하는 것은 접근 통제가 아닙니다. internal contract는 인증된 위치에 두고 공개 예제에서 내부 host, 실제 식별자, credential을 제거합니다.

운영 endpoint의 `try it`은 기본으로 공개하지 않습니다. 필요하면 sandbox server와 synthetic credential을 명시합니다. credential을 제3자 proxy로 보내는 구성은 security-owner의 승인이 필요합니다.

## 한 로직과 여러 adapter

public, partner, internal adapter는 가능한 한 동일한 application use case를 호출합니다. adapter는 공개 필드, 인증 맥락, rate limit, transport status를 소유하고 domain result를 audience별 response로 매핑합니다. 별도 public service와 internal service를 처음부터 복제하지 않습니다. 격리·규제·독립 배포 요구가 비용을 정당화할 때 분리합니다.

같은 로직의 증거는 다음을 포함합니다.

- 같은 domain/application tests.
- 각 transport의 provider contract test.
- audience별 authorization과 다른 tenant 접근 거부.
- 같은 policy version·입력 의미·권한·시간/설정 조건에서의 결과 비교.
- 공개 projection에 internal path와 field가 없다는 검사.

## version과 lifecycle

경로의 `/v1`은 major 계약이고 날짜는 출시 metadata입니다. 날짜 기반 version은 소비자가 시점별 계약을 고정해야 하는 제품 모델일 때만 선택합니다. package version, policy version, API version을 같은 숫자로 맞추지 않습니다.

상태는 최소 `experimental → active → deprecated → sunset → retired`로 구분합니다. deprecated는 새 사용을 권하지 않는 상태이고 sunset은 종료 예정 시각입니다. retirement 전에는 알려진 consumer, 실제 usage, replacement, migration, rollback limit, security exception을 검토합니다.

모든 API의 공통 LTS 기간은 두지 않습니다. LTS를 선택할 때 다음을 프로젝트 결정으로 기록합니다.

- 지원 시작점과 종료일 또는 계산법.
- 포함되는 보안·오류 수정과 제외되는 새 기능.
- 동시에 유지할 major 수와 운영·테스트 비용.
- 종료 통지 기간과 연락 방법.
- 지원 책임자와 재검토 조건.

외부 장기 연동 API의 첫 비교안으로 정식 출시부터 2년을 산정할 수 있지만, 비용·계약 확인 없이 약속하지 않습니다. 문서·changelog·직접 통지와 함께 HTTP `Deprecation`, `Sunset` 신호를 사용할 수 있습니다.

자료: [Deprecation header](https://www.rfc-editor.org/rfc/rfc9745.html), [Sunset header](https://www.rfc-editor.org/rfc/rfc8594.html), [OWASP API inventory](https://owasp.org/API-Security/editions/2023/en/0xa9-improper-inventory-management/), [Scalar configuration](https://scalar.com/products/api-references/configuration).
