# API design and lifecycle

API 설계는 이름을 즉석에서 정하는 일이 아니라 resource, query, command, aggregate, job 중 무엇을 제공하는지 분류하는 일에서 시작합니다. HTTP에만 해당하는 표기와 transport에 독립적인 계약 원칙을 구분합니다.

정본 규칙: [ARCH-006](../rules/architecture/ARCH-006.md), [API-001](../rules/api/API-001.md), [API-002](../rules/api/API-002.md), [API-003](../rules/api/API-003.md), [API-004](../rules/api/API-004.md), [COMP-001](../rules/compatibility/COMP-001.md).

## 계약과 코드 경계

각 경계는 책임이 다른 타입을 사용합니다.

| 경계 | 소유하는 내용 | 소유하지 않는 내용 |
| --- | --- | --- |
| transport request/response | wire 이름, 형식, 직렬화, 공개 필드, transport 인증 정보 | 업무 판단과 persistence entity |
| application command/query/result | 유스케이스 의도와 필요한 값, 호출 결과 | HTTP status, protobuf annotation, serializer 객체 |
| domain value/entity | 업무 불변식과 상태 전이 | transport와 framework 표현 |

컨트롤러는 transport DTO를 application command/query로 항상 명시적으로 매핑합니다. 필드가 우연히 같아도 같은 타입을 재사용하지 않습니다. 이는 mapper class를 무조건 크게 만들라는 뜻이 아닙니다. 작은 함수나 계약 기반 생성도 가능하지만 의존성은 adapter에서 멈춥니다.

입력 검증도 분리합니다. JSON 형식·길이·파싱은 transport, 해당 사용자가 이 명령을 수행할 수 있는지는 application, 금액·상태 같은 불변식은 domain이 소유합니다. 검증 코드의 디렉터리가 아니라 판단의 의미로 경계를 판정합니다.

## HTTP 경로 문법

새 HTTP API의 기본 문법은 다음과 같습니다.

```text
/v{major}/{plural-resource}/{resource_id}/{plural-child}/{child_id}/{command}
```

- 버전은 `/v1`, `/v2`처럼 외부 계약의 major를 나타냅니다. API 생성일은 metadata와 changelog에 기록합니다.
- collection segment는 복수형 lower-kebab-case입니다.
- path variable과 query parameter 이름은 lower-snake-case입니다.
- 첫 collection은 내부 클래스나 조직 이름이 아니라 외부에 제공하는 resource입니다.
- nesting은 소유권이나 canonical identity를 표현할 때 사용합니다. 단순 filter는 query로 표현합니다.
- 같은 item에 canonical URL을 하나 둡니다. 특정 사용자의 목록은 `/join-requests?member_id=...` 또는 의미가 승인된 `/me/...` projection으로 모델링합니다.

```text
POST /v1/companies/{company_id}/join-requests
GET  /v1/companies/{company_id}/join-requests
GET  /v1/companies/{company_id}/join-requests/{join_request_id}
POST /v1/companies/{company_id}/join-requests/{join_request_id}/approve
```

`join-requests`는 단순 동사가 아니라 ID, 상태, 승인·거절·취소, 이력을 가진 resource입니다. 즉시 membership이 만들어지고 신청 생명주기가 없다면 `members` 생성으로 모델링할 수 있습니다.

## HTTP method와 변경 의미

| 종류 | 기본 method | 계약에 필요한 내용 |
| --- | --- | --- |
| resource 생성 | POST | 중복 요청, 생성 결과, `Location`, 권한 |
| writable representation 교체 | PUT | 필수·누락 필드, server-owned 필드, 동시성 |
| 일부 변경 | PATCH | media type, 누락/null, 배열, atomicity, 충돌 |
| 업무 command | POST | 가능한 상태, 권한, 멱등성, 결과 미확인, 후속 작업 |
| 조회 | GET | 범위·권한·pagination·존재 비노출 정책 |

PUT의 전체는 DB row 전체가 아니라 계약이 공개한 writable representation 전체입니다. PATCH는 unrestricted mass assignment가 아니며 두 방식 모두 editable allowlist와 권한 검사를 갖습니다. 경쟁 수정은 ETag/If-Match, revision, 조건부 갱신 등 선택한 방법을 계약에 기록합니다.

승인·거절·취소는 단순 status 필드 쓰기가 아니라 업무 command입니다. command endpoint는 `POST .../{id}/approve` 형태로 통일하고, 중복 호출과 응답 유실 뒤 재시도를 검증합니다. 장기 실행이면 `202 Accepted`와 상태를 조회할 job resource를 검토합니다.

## JSON과 다른 protocol

소유하는 HTTP JSON field는 중첩을 포함해 lower-snake-case입니다.

```json
{
  "join_request_id": "jr-123",
  "company_id": "company-1",
  "created_at": "2026-09-04T09:00:00Z"
}
```

외부 표준이 정한 필드와 사용자가 제공한 opaque map key는 변환하지 않습니다. 공개된 camelCase 계약도 스타일만을 이유로 깨지 않고 version과 migration으로 처리합니다.

공통 원칙은 wire 이름이 아니라 versioned contract, distinct transport mapping, compatibility, ownership, provider-consumer verification입니다.

| 방식 | 정본 예 | 이름 규칙 |
| --- | --- | --- |
| HTTP + JSON | OpenAPI 또는 승인된 code-first 위치 | 이 profile의 path와 snake_case 규칙 |
| HTTP + SSE | OpenAPI 3.2 `itemSchema`, 연결된 schema 또는 승인된 실행 계약 | SSE field와 `data` payload 계약을 각각 적용 |
| protobuf RPC | `.proto` | protobuf schema가 정한 이름과 generated API convention |
| WebSocket + JSON | AsyncAPI·JSON Schema 등 선택한 계약 | JSON payload에는 승인된 JSON naming profile |
| WebSocket + protobuf | `.proto`와 framing 계약 | protobuf 규칙 |

SSE와 WebSocket은 payload 형식 자체가 아니므로 JSON 규칙을 자동으로 적용하지 않습니다. SSE는 handshake와 stream 시작 전·후 오류, event framing, 완료·재연결을 함께 계약합니다. 실제 protobuf·WebSocket 프로젝트가 생기기 전에는 새 profile을 만들지 않고 이 공통 원칙으로 clarify합니다.

## collection 밖의 형태

- singleton: `settings`처럼 부모당 하나인 resource.
- aggregate: `summary`처럼 원본 collection과 다른 계산 결과.
- batch: 전체 원자성인지 item별 결과인지 명시한 작업.
- search: GET query로 표현하기 어려운 크기·구조·보안 근거가 있을 때 별도 contract.
- job: 요청 수락과 완료가 분리된 장기 작업.

이를 일반적인 collection/item 규칙의 숨은 예외로 두지 않고 계약 종류로 선언합니다.

자료: [HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110.html), [PATCH](https://www.rfc-editor.org/rfc/rfc5789.html), [JSON Merge Patch](https://www.rfc-editor.org/rfc/rfc7396.html), [Google AIP resource names](https://google.aip.dev/122).
