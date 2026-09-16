# 후보 행동 검증 — 5단계 완료

최종 후보: `CAND-STAGE5-20260915-04`. 최초 4단계 후보와 같은 고정 수용 사례 v1·입력 9개를 사용했다. 7개 과업 문맥의 최종 유효 응답 8개를 부모가 수동 판정했고, 24개 사례가 모두 `met`이다. 기준선 0.4.0은 22 `met` / 2 `unmet`이었다.

이 결과는 단일 합성 실행의 사례 판정이다. 일반적인 AI 성공률, 자동 스킬 선택, 운영 QA, 원문 전체 무누락 또는 릴리스 준비 완료를 뜻하지 않는다.

## 후보 반복과 정정

1. `CAND-STAGE4-20260913-01`: 24개 응답은 모두 기대 행동을 보였다. 첫 독립 의미 감사가 check-report schema와 규칙 밖 advisory 관찰 저장 지침의 충돌 `IV-01`을 발견했다.
2. `CAND-STAGE5-20260915-02`: check 스킬을 정정하고 PK-02/03/05를 재실행했다. 관련 11개 사례는 유지됐다.
3. `CAND-STAGE5-20260915-03`: 두 번째 독립 감사의 승인/위임 상태 종료 문구 충돌 `F-1`을 정정했다. PK-04 재실행은 근거 없는 동시 편집 질문을 새 material-open으로 만들어 AC-017 회귀가 `unmet`이었다. 그 응답은 실패 증거로 보존했다.
4. `CAND-STAGE5-20260915-04`: 관찰된 요구나 기술 trigger 없는 가상 actor/concurrency/consumer/failure/integration을 제품 결정으로 승격하지 않는 guard를 추가했다. PK-04 두 턴 재실행은 승인 3건, material-open 0건으로 정정을 반영했고 AC-014~017이 모두 `met`이었다. 독립 guard 감사도 새 P1/P2 없이 `resolved`로 판정했다.

첫 disposition/PK-04 최종 시도 중 두 차례의 가용량 제한은 응답 없는 환경 중단 또는 부분 첫 턴으로 분리했다. 다른 가용 모델의 새 문맥에서 다시 실행했으며 행동 실패로 세지 않았다. 후보 3의 완성된 두 턴 결과는 가용량과 무관한 실제 행동 실패로 보존했다.

## 최종 사례 판정

| Case | Final | 최종 관찰 |
| --- | --- | --- |
| AC-001 | met | PK-01: A/B 경로를 각각 찾고 B의 설정 조회·필터 부재와 양쪽 회귀 사례를 연결했다. |
| AC-002 | met | PK-01: C의 충돌 기록을 `open`으로 유지하고 집중 분산은 원인 가설로 구분했다. |
| AC-003 | met | PK-02-r2: 10회 검토보다 B 실행 증거 유무로 M2/M3 완료를 판정했다. |
| AC-004 | met | PK-07: 0.4.0 발행 기준선과 0.5.0 미발행 후보를 구별하고 DB 정책 재구현을 제외했다. |
| AC-005 | met | PK-03-r2: rev1의 실패·수정 후 통과를 보존하고 rev4에 새 case/run이 필요함을 기록했다. |
| AC-006 | met | PK-06: client/server/DB 조합, 전이·회귀·복구 위험을 조건별 적용/제외/미결정으로 설계했다. |
| AC-007 | met | PK-01: 저장 성공과 실제 선택 실패를 구분해 고객 목적 미충족을 보고했다. |
| AC-008 | met | PK-03-r2: 분산 정본을 CHG/S/run으로 조회하되 자동 수집·통합 UI로 과장하지 않았다. |
| AC-009 | met | PK-03-r2: 승인 rev8과 관측 rev9, 접근 불가한 최신 기획을 구분하고 재검토 조건을 남겼다. |
| AC-010 | met | PK-03-r2: repo-A/repo-B revision과 외부 QA 증거를 연결하고 구현 repo에 QA 폴더를 요구하지 않았다. |
| AC-011 | met | PK-07: 문제·관찰·가설·결정·반례·규칙 후보·증거·공개 경계와 최신 원고 재확인을 인계했다. |
| AC-012 | met | PK-02-r2: 문서 충돌, 코드 누락, fixture/환경 미확정을 서로 다른 수정 대상으로 분류했다. |
| AC-013 | met | PK-02-r2: 원본 A/B에서 파생 명세의 B 누락을 찾아 끊긴 연결과 수정 위치를 보여 줬다. |
| AC-014 | met | PK-04-r4: 한 문장과 코드 snapshot에서 목적·범위·예시·반례·유지 조건·질문을 도출했다. |
| AC-015 | met | PK-04-r4: 캠페인별 해석을 계정 공통으로 대체하고 A/B·시점·계정 격리 사례를 갱신했다. |
| AC-016 | met | PK-04-r4: 역할별 시점 차이를 구체화해 intent-owner에게 요청하고 그 답을 최종 결정으로 보존했다. |
| AC-017 | met | PK-04-r4: 승인된 오타는 재질문하지 않고, 사용자 답변 뒤 근거 없는 가상 질문 없이 material-open 0을 보고했다. |
| AC-018 | met | PK-05-r2: manifest/lock 없는 저장소를 shadow assessment로 다루고 현재 코드를 승인 의도로 삼지 않았다. |
| AC-019 | met | PK-05-r2: late-entry 기준·dirty 변경·사라진 사전 증거와 사후 회귀 계획을 구별했다. |
| AC-020 | met | PK-05-r2: c1/d1과 c2/d2, 실제 조사 파일·hash·관측 시각, 미변경 B 소비자, C unknown과 재검토 trigger를 기록했다. |
| AC-021 | met | PK-05-r2: impact는 조사/한계를 반환하고 clarify/converge/check의 결정·투영·판정 책임을 분리했다. |
| AC-022 | met | PK-07: case 작성·정적 조사·실제 baseline·candidate·독립 검증·릴리스 상태를 분리했다. |
| AC-023 | met | PK-07: 외부 QA 삭제는 누락, 근거 있는 deferred는 추적된 미구현으로 판정했다. |
| AC-024 | met | PK-07: P1/P2의 단계 상태를 구분하고 정책·설치·tag·릴리스 완료로 확대하지 않았다. |

## 독립 감사 disposition

- [첫 감사](independent-review-initial.md): `IV-01` P2 발견. 최종 후보에서 정책 JSON과 별도 승인된 advisory 기록 인계를 분리해 해소했다.
- [두 번째 감사](independent-review-second.md): `F-1` P2 발견. 최종 후보에서 실제 승인/위임 상태를 보존하도록 해소했다.
- [disposition 감사](independent-disposition.md): IV-01/F-1과 QA 강제·자동화 과장 위험을 모두 `resolved`, 새 P1/P2 없음으로 판정했다.
- [guard 감사](independent-guard-audit.md): 가상 경계를 제품 결정으로 승격하지 않는 제한과, 실제 새 trigger가 있을 때의 질문 가능성이 양립하며 새 P1/P2가 없다고 판정했다.

독립 감사는 제공된 사용자 발췌와 후보 source의 정적 의미 검토다. 비공개 사고 원문 전체, 일반 작업에서의 자동 skill activation, 다른 모델/프로젝트 재현성은 감사 범위가 아니다.

## 남은 비차단 한계와 다음 단계

- 기존 설치 스킬 5개는 저장소를 가리키는 live symlink여서 미발행 후보 내용이 그 경로에서 보인다. 설치 명령이나 링크를 변경한 것은 아니지만 설치 내용 불변이라고 말할 수 없다.
- 새 `spec-it-impact`의 전역 설치와 자동 선택은 실행하지도 검증하지도 않았다.
- 기준선 0.4.0 lock의 알려진 정책 digest 정렬 불일치는 유지한다.
- 최종 VERSION, self manifest/lock/projection, migration/changelog의 발행 문구, commit/tag/원격 공개는 6단계에서 별도 확인한다.
