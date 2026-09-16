# 4단계 구현 기록 — 후속 검증·릴리스 준비 완료

상태: 4단계의 instruction 구현과 구조 검사는 완료되었고, 이후 5단계 후보 행동·독립 검증과 6단계 로컬 릴리스 준비도 완료했다. `0.5.0`은 여전히 미발행이며 기준선과 수용 사례 v1은 동결 상태를 유지한다. 당시 단계별 관찰은 아래에 보존하고 최신 결과는 [검증 기록](verification.md)과 [릴리스 체크리스트](../../../docs/releases/0.5.0-checklist.md)를 따른다.

## DEC-009 — 기존 규칙 재사용과 선택적 실행 절차

사용자의 4단계 진행 승인과 DEC-008에 따라 다음처럼 설계를 구체화한다. 2단계의 GOV-005/TST-007/profile 추가 제안은 이번 후보에서 채택하지 않는다. 22개 충족을 모든 환경에서의 성공으로 일반화하지 않지만, 그 결과만으로 새 의무를 추가할 근거도 없다.

| 논점 | 분류·기존 권한 | 구현 위치·호환성 |
| --- | --- | --- |
| 의도 되읽기·정정·필요한 질문 | 승인된 방향; GOV-001/002, HITL-002 | specify/clarify 실행 안내와 선택 change template. 새 정책 의무 없음 |
| 세션 간 영향·신선도 인계 | 승인된 방향, GAP-001; 기존 preflight 지원 | 새 read-only impact와 기존 스킬 인계. 고정 정책 채택·파일 쓰기 권한 확대 없음 |
| 경로별 수용·실행 이력 | 승인된 방향; TST-002/003/006 | 선택 사례/run template와 설명. QA repo/도구/전체 lifecycle 강제 없음 |
| 원칙 문서 전달 | 프로젝트 후속, GAP-002 | 이 변경 디렉터리의 선택 인계 양식. 실제 원고 편집 없음 |
| 불일치 digest | 관찰 사실; TOOL-002 | migration 초안에 전역 경로 정렬 명시. 기존 tag/lock 수정은 하지 않음 |

정책 규칙·profile·schema·VERSION·self manifest/lock·generated AGENTS는 보존한다. 스킬·템플릿도 현재 source에서 변경되므로 설치된 0.4.0과 동일한 bundle로 부르지 않는다. 정책 digest가 같더라도 스킬 bytes가 같다는 증거는 아니다. 5단계에서 전체 후보 파일 snapshot으로 실행 대상을 고정한다.

## 완료 조건과 작업 순서

1. 기존 의무와 중복 대조 및 구현 범위 기록.
2. impact, 기존 스킬 인계, 선택 템플릿과 설명·예제 구현.
3. 구조·보존 검사와 요구사항별 의미 검토.
4. 현재 결과와 미실행 후보 검증을 구분해 인계.

검사 gate는 임시 작업 공간의 GATES.md에 구현 전 작성했다. G1은 동결 증거·정책 입력 보존, G2는 산출물/상대 링크, G3는 6개 스킬 구조, G4는 24개 요구의 처리·공백 보완 수동 검토다. 정책 저장소에 실행 validator나 hook을 추가하지 않는다. 실제 결과와 요구 매핑은 완료 검토 때 아래에 기록한다.

최종 gate 결과: G1~G3은 `/bin/sh`, 정책 저장소 root에서 실제 재실행해 각각 exit 0과 `INTEGRITY_OK` / `STRUCTURE_OK` / `SKILLS_OK count=6`을 확인했다. G4는 아래 24개 매핑과 실제 instruction을 대조한 부모 수동 검토다. 총 4 met / 0 unmet / 0 abandoned이며 3개 runnable gate를 재실행했다. 이 gate 수는 행동 사례 통과 수가 아니다.

구현 전에 G2를 실행했을 때 새 impact 파일 부재로 exit 1을 관찰했고 구현 후 통과했다. 이는 파일 존재 검사에 대한 실패/성공 대조이며 스킬 행동의 red/green이라고 부르지 않는다. [후보 snapshot](implementation-snapshot.json)은 공개 source 221개 파일의 tree hash와 변경 source 24개(기존 16·신규 8)의 개별 hash를 보존한다. 평가자용 변경 디렉터리는 후보 실행 입력에서 제외한다. 이 파일은 validator schema나 발행 lock이 아니다.

## 요구별 구현과 보존 경계

아래 ‘구현’은 instruction/문서 구현이다. 각 REQ에 대응하는 고정 AC의 후보 행동 결과는 전부 `not-run`이며 5단계에서 별도로 판정한다. SRC/REQ/AC의 번호 대응은 [spec](spec.md)과 [동결 사례](acceptance-cases.md)에 있다.

| Requirement | 실제 산출물·처리 | 아직 증명하지 않은 것 |
| --- | --- | --- |
| REQ-001 | [impact](../../../skills/spec-it-impact/SKILL.md)의 유형·경로·미변경 소비자 조사, [case](../../../templates/testing/acceptance-case.md)의 관찰 경계 | 모든 실환경 경로 발견 |
| REQ-002 | [specify](../../../skills/spec-it-specify/SKILL.md)의 사실/회고/정정 분리 | 원래 앱의 현재 상태·사고 원인 확정 |
| REQ-003 | [check](../../../skills/spec-it-check/SKILL.md)의 반복 횟수 대신 원문·증거 대조 | 의미상 무누락 보장 |
| REQ-004 | [후보 안내](../../../docs/migrations/0.4.0-to-0.5.0.md)의 발행/후보·DB 범위와 digest 이력 | 최종 lock 정정·발행 |
| REQ-005 | [case](../../../templates/testing/acceptance-case.md)와 [run](../../../templates/testing/verification-run.md)의 독립 revision·이력 | QA 운영 제품·runner·전체 campaign |
| REQ-006 | [설명](../../../docs/intent-and-verification.md)의 위험별 조합/회귀/DB/복구와 N/A | 실제 client/server·DB 실행 |
| REQ-007 | [check](../../../skills/spec-it-check/SKILL.md), 설명의 기획 적합성·고객 목적·탐색 구별 | 고객 문제의 실제 해결 |
| REQ-008 | 설명과 [예제](../../../examples/intent-verification/README.md)의 상위 조회·관측·결함/재검증 | 통합 UI·자동 수집 |
| REQ-009 | [change spec](../../../templates/project/change-spec.md), impact의 출처 권한·revision·관측 시각 | 실시간 Notion/Figma 동기화 |
| REQ-010 | case/run·[converge](../../../skills/spec-it-converge/SKILL.md)의 외부 QA 허용·폴더 강제 금지 | 다중 저장소 운영 파일럿 |
| REQ-011 | [원칙 인계](principle-handoff.md), [evolve](../../../skills/spec-it-evolve/SKILL.md)의 조건부 인계. GAP-002 보완 | 원고 조회·수정·전달 완료는 deferred |
| REQ-012 | check·run의 결함 원인 확실성/수정 대상·회귀·재검증 | 특정 결함의 근본 원인 |
| REQ-013 | check의 원문 양방향 검토·끊긴 연결과 수정 위치 | 접근 불가 원문 전체 감사 |
| REQ-014 | specify/change spec의 한 문장 시작·최소 의도와 예시·반례 | 사용자의 모든 암묵지 추론 |
| REQ-015 | [clarify](../../../skills/spec-it-clarify/SKILL.md)의 되읽기·정정·범위와 증거 갱신 | 모든 응답에서 자동 실행 |
| REQ-016 | clarify의 직무별 해석/결정자·위임 범위 | 전원 만족을 완료 조건으로 삼지 않음 |
| REQ-017 | clarify의 조건부 질문 묶음·승인된 결정 재사용, 경미 변경 축약 | 질문 비용/품질의 실제 측정 |
| REQ-018 | impact/check의 shadow assessment·사실/승인 구별 | 미채택 프로젝트의 준수 판정 |
| REQ-019 | impact/specify의 late-entry·사라진 사전 증거·dirty 보존 | 사후 실행을 사전 TDD로 만들지 않음 |
| REQ-020 | impact·[영향 형식](../../../templates/project/change-impact.md)의 observed_at/기준/관계/재검토 조건. GAP-001 보완 | 상시 감지·미접근 변경의 동일성 |
| REQ-021 | 새 impact + 기존 5개 스킬 인계, [AGENTS template](../../../templates/project/AGENTS.md) | 설치된 전역 스킬 동기화 |
| REQ-022 | 동결 baseline·gate 선작성, [TDD 설명](../../../docs/tdd-and-verification.md)의 증거 단계 구별 | 후보 행동/독립 검증은 5단계 |
| REQ-023 | 이 표·spec·impact·[검증 기록](verification.md)의 연결과 deferred 유지 | 원문 의미 전체 무누락 |
| REQ-024 | 6단계 상태와 이 단계의 경계 보고 | 4단계 완료를 전체 완료로 간주하지 않음 |

## 부담·부작용 검토

- 더 많은 기록이 작은 작업까지 확장되는 위험: material scope에서만 되읽기를 상세화하고 이미 승인된 차이는 재질문하지 않는다. 사례/영향은 한 행 또는 기존 도구 항목으로 축약한다.
- 폴더 단독 설치 시 상대 템플릿 링크가 깨지는 위험: impact 본문에 최소 반환 항목을 포함하고 고정 policy source에서 템플릿을 찾거나 본문만으로 반환한다. 임의 설치는 하지 않는다.
- 최신 기획을 무조건 승인으로 해석하는 위험: 관측 revision과 승인 근거를 분리한다. 기존 승인 적용 범위가 달라지면 재확인한다.
- 기록이 실제보다 강한 확신을 주는 위험: 원문 접근·조사 범위·미접근과 후보 미실행을 명시한다. 구조 검사와 행동 검증을 합산하지 않는다.
- 스킬 변경이 policy digest에 포함되지 않는 위험: 5단계에는 전체 후보 source snapshot으로 대상을 고정한다. VERSION만 같다고 baseline으로 평가하지 않는다.
- 통합 운영·원고·새 규칙으로 범위가 커지는 위험: QA 제품/원고 수정/정책 자동 채택은 계속 제외한다. 별도 relations 파일 대신 영향 기록의 관계 표를 재사용한다.

## 5단계 인계

동결 PK-01~07 입력과 사례 v1을 유지하고 후보 스킬의 실제 응답을 새 run으로 수집한다. GAP-001/002는 후보에서 재검증할 항목이지 이번 문서 작성으로 해결이 검증된 항목이 아니다. 나머지 22개는 유지 테스트다. 수행자에게 이 구현표/기대 답안/기준선 결론을 주입하지 않는다.

별도 독립 검토는 접근 가능한 사용자 원문부터 요구 누락과 경계/분류를 확인한다. 원문을 볼 수 없는 부분은 human-review로 둔다. 평소 단순 구현 요청에서의 자동 활성화는 기존 packet으로 입증되지 않으므로, 추가 실험을 한다면 별도 입력/revision/run으로 기록하고 24개 기준선 비교와 섞지 않는다.
