# User message contract fixture

[contract.yaml](contract.yaml)은 한도 초과 거절 하나의 가상 예제입니다. 0.2.0 [MSG-001](../../rules/messages/MSG-001.md), [MSG-002](../../rules/messages/MSG-002.md)를 설명하며 프로젝트의 계약 승인이나 실제 실행 성공을 의미하지 않습니다. `test_ref: not-implemented:...`는 누락을 정직하게 드러내는 표시입니다.

## 확인할 연결

- `EXPORT_LIMIT_EXCEEDED` → integer `limit` → 언어별 `export.limit_exceeded`.
- 공개 parameter는 전부 필수 primitive 값입니다. 실제 응답에 누락되거나 타입이 다르면 잘못된 계약 응답입니다. 중첩/선택 값이 필요한 프로젝트는 기존 API 계약을 정본으로 사용합니다.
- 사용자 안내는 본 작업의 결과이고 info 로그는 별개입니다. 로그의 허용 필드는 `code`, `request_id`이며 추가 작업은 없습니다.
- 모르는 code는 `common.unknown`, 미지원 locale은 `ko`로 처리하며 자동 재시도하지 않습니다.
- 음수/상한 등 값의 업무 의미, 노출 조건, 늦은 응답, 중복 억제는 실제 테스트가 필요합니다. 영어 문구도 사람의 내용 검토 전입니다.

## 형식 검사와 의미 검사를 구분한다

[JSON Schema](../../schemas/user-message-contract.schema.json)는 필수 필드·타입·닫힌 선택지·HTTP 기본 범위를 검사합니다. 다음 항목은 JSON Schema만으로 보장되지 않습니다.

| 별도 검사 대상 | 기대 결과 |
| --- | --- |
| 중복 outcome code 또는 acceptance case ID | 계약 오류 |
| default locale이 지원 목록/번역 목록에 없음 | 계약 오류 |
| 번역 key 누락 또는 치환 이름과 public parameter 불일치 | 계약 오류 |
| 실제 HTTP 응답의 parameter 값/타입 또는 status가 선언과 다름 | provider 계약 테스트 실패 |
| 승인된 조건과 실제 판단/노출이 다름 | 동작 테스트 실패 |
| 새 오류 code를 구버전 소비자가 처리하지 못함 | 호환성 테스트 실패 |

이 fixture는 정책 합성 manifest가 아닙니다. 기존 0.1.0 예제는 수정하지 않습니다. 의미 검사·조건 실행·타입 생성·번역 런타임은 구현하지 않았으며 Phase 0 자동 검증 판정은 `human-review`입니다.
