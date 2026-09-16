# 5단계 발견·처리 기록

## ENV-001 — 설치 경로의 live symlink

- 분류: 환경/인계 정확성. 후보 응답의 수용 사례 실패와 별도다.
- 관찰: 기존 specify/clarify/converge/check/evolve 설치 경로 5개가 저장소의 해당 스킬 폴더를 가리키는 symlink였다. 후보 소스를 수정하면 이 경로로 읽는 내용도 바뀐다.
- 영향: 설치 명령이나 링크 변경이 없더라도 다른 세션이 미발행 instruction을 읽을 수 있다. source의 VERSION/정책 digest가 변하지 않은 것으로 스킬 bytes의 불변을 추정할 수 없다. 새 impact의 전역 설치 여부는 별개다.
- 정정: 4단계에서 설치 명령·symlink 자체는 수정하지 않았지만 ‘설치된 스킬 내용이 변경되지 않았다’고 설명할 수는 없다. 기준선·후보 행동 실행은 모두 설치 경로 대신 별도 export를 사용했다.
- 현재 처리: 사실을 사용자에게 알리고 이번 평가를 고정 snapshot으로 분리했다. 원래 링크를 제거/변경하거나 다른 세션을 중단하지 않았다.
- 후속: 6단계 공개 안내에 live source symlink와 immutable release 설치의 차이를 명시할 필요가 있다. 실제 설치 경로 전환은 사용자가 그 범위를 승인할 때 수행한다. owner: intent-owner/환경 운영 담당; 재검토: 발행/설치 방식 선택 또는 symlink 대상 변경 시.

## 가용량 중단

PK-02/03의 첫 실행은 응답 생성 전 가용량 한도로 중단되었다. 사용자 계속 요청 후 동일 입력으로 재개했고 두 응답을 확보했다. 이를 unmet 행동 사례나 새로운 입력 revision으로 세지 않는다. 원본 입력과 이어진 응답의 신원을 실행 manifest에 남긴다.

## IV-01 — advisory 관찰과 check-report schema 충돌

- 발견: 첫 독립 감사가 정책 규칙 밖 의도·QA 관찰을 지속 기록하라는 지침과 모든 result에 `rule_id`를 요구하는 기존 check-report schema의 충돌을 P2로 보고했다.
- 처리: schema·규칙은 바꾸지 않았다. `spec-it-check`가 정책 JSON에는 고정 규칙 결과만 저장하고, 규칙 밖 관찰은 명시적으로 승인된 상위 change/issue/handoff 위치가 있을 때만 호출자에게 인계하도록 정정했다. 임의 rule ID·schema 밖 필드·기본 QA 폴더 생성을 금지했다.
- 검증: PK-02/03/05 재실행에서 관련 완료·분산 추적·brownfield/late-entry 사례 11개가 유지됐다. 독립 disposition 감사는 `resolved`, 새 P1/P2 없음으로 판정했다.

## F-1 — 승인·위임 상태와 종료 문구 충돌

- 발견: 두 번째 독립 감사가 `spec-it-clarify`의 “승인·위임된 선택은 다시 묻지 않음”과 무조건 `pending human confirmation`으로 종료하라는 문구의 충돌을 P2로 보고했다.
- 처리: 실제 material-open 수와 승인 상태를 보고하고, 승인·위임되지 않은 선택만 확인 대기로 표시하도록 고쳤다.
- 검증: 독립 disposition 감사는 해결됐다고 판정했다. 다만 후보 3의 PK-04 재실행은 관찰 근거 없는 동시 편집을 새 material-open으로 만들어 아래 BEH-001을 추가로 드러냈다.

## BEH-001 — 가상의 경계를 새 제품 결정으로 승격

- 발견: 후보 3의 PK-04 두 번째 응답은 사용자가 범위·시점·예외를 확정했는데도 실제 동시 편집 신호 없이 충돌 정책 질문을 만들었다. AC-017은 그 run에서 `unmet`이다.
- 처리: `spec-it-clarify`가 관찰된 요구나 기술 trigger 없는 가상 actor/concurrency/consumer/failure/integration을 material decision으로 올리지 않고 discovery 항목으로 두도록 제한했다.
- 검증: 최종 후보 4의 같은 두 턴은 승인 3건·material-open 0건을 보고했다. 독립 guard 감사는 이 제한이 실제 새 trigger의 정당한 질문을 막지 않으며 새 P1/P2가 없다고 판정했다.

## 최종 가용량 기록

후보 3 PK-04 첫 최종 시도는 첫 응답 뒤, disposition 첫 시도는 응답 전에 가용량 한도로 중단됐다. 부분 첫 응답은 보존했고 다른 가용 모델의 독립 문맥에서 재실행했다. 이는 BEH-001과 달리 환경 중단으로 분류한다.
