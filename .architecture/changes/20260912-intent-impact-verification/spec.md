---
id: 20260912-intent-impact-verification
scope: change
status: accepted
owners:
  - intent-owner
  - architecture-owner
created_on: "2026-09-12"
affects:
  - behavior
  - architecture
---

# 기획 의도·영향 범위·검증 추적의 자기 적용 파일럿

이 파일은 이번 변경의 유일한 의도 명세다. [수용 사례](acceptance-cases.md), [영향도](impact.yaml), [검증 기록](verification.md)은 연결된 설계·증거이며 공통 정책이 아니다. 전체 6단계와 승인된 `v0.5.0` 공개 절차를 완료했다. [기준선 결과](baseline/results.md)는 24개 합성 사례 중 22개 충족·2개 일부 미충족이며, [최종 후보 결과](candidate/results.md)는 독립 감사에서 발견한 세 문제를 고친 뒤 24개 모두 충족이다. [구현 기록](implementation.md)은 새 규칙 없이 기존 권한을 재사용하는 DEC-009와 실제 파일을 연결한다.

## 진행 단계

| 단계 | 작업 | 상태 | 종료 증거 |
| --- | --- | --- | --- |
| 1 | 명세·출처 추적·수용 사례 초안 작성 | complete | SRC/REQ/AC 각 24개와 STR-001 |
| 2 | 기준선 불일치 조사·구현 설계 확정 | complete | BASE-ISSUE-001 조사, DEC-003/004/006/007 처리, case set v1 고정, STR-002 |
| 3 | 기존 0.4.0의 행동 테스트 | complete | 7개 수행 문맥·8개 원본 응답, 24개 판정과 GAP-001/002, STR-003 |
| 4 | 정책·스킬·템플릿 구현 | complete | DEC-009, instruction/선택 template, 24개 요구 매핑, STR-004 |
| 5 | 구현 후 테스트·독립 검증 | complete | 최종 후보 24/24 met, 독립 감사 IV-01/F-1/BEH-001 해소, STR-005 |
| 6 | 릴리스 준비·최종 확인 | not-started | 최종 source digest, lock/projection, migration, release 증거와 승인 |

단계 수는 기능별 작업량이나 진행률 백분율이 아니다. 2단계 완료는 기존 릴리스의 결함 수정 또는 정책 구현 완료를 뜻하지 않는다. 실제 commit·tag·원격 공개는 각각 실행 권한과 결과를 확인한 뒤 기록한다.

## 기준선과 권한

- 적용 정책: `0.4.0`, tag `v0.4.0`, commit `6a4ea01eb09bfb116ff24fd2d5253889086f9a77`.
- 프로젝트 입력: [project](../../project.md), [manifest](../../manifest.yaml), [lock](../../lock.yaml), [ADR-0001](../../decisions/ADR-0001.md). 선택 프로필은 `risk/standard`다.
- 이번에 작성한 파일 형식은 프로젝트 내부 파일럿이다. `impact.yaml`은 아직 공개 schema 계약이 아니며 다른 프로젝트에 필수가 아니다.
- 다음 버전 후보는 `0.5.0`이다. 후보 규칙이나 version 문자열을 현재의 승인된 정책으로 사용하지 않는다.
- 첫 진행 요청은 명세 패키지 작성, 후속 ‘총 단계와 현재 단계를 알려주고 다음 단계 진행’ 요청은 2단계 조사·설계 구체화의 실행 근거다. 이미 동의된 제품 방향 안에서 기술적 설계 선택을 기록하며, 정책 채택·릴리스 승인을 새로 만들어 기록하지 않는다.
- 이어진 ‘다음 단계 진행’과 ‘계속’ 요청에 따라 3단계의 합성 입력·독립 행동 응답·평가 기록을 `baseline/`에 보존한다. 수용 사례 v1의 고정본은 변경하지 않는다.
- 3단계 완료 후 ‘좋아 진행해줘’ 요청은 4단계 구현의 실행 근거다. 설치된 스킬·원격 서비스·원고·commit/tag 변경은 포함하지 않는다.
- 기준선 검사에서 tag의 실제 정책 digest와 lock 기록의 불일치를 발견했다. [BASE-ISSUE-001](verification.md)에 발생 구간과 처리 방침을 기록했다. 3단계는 정확한 tag/commit과 재계산 digest를 고정한 비교 실험으로 진행한다. 기존 lock의 무결성 결함은 유지되며, 후속 정상 수렴/릴리스에서는 최종 source로 계산한 lock이 필요하다.

## 왜 필요한가

기획을 읽고 구현한 경우에도 별도 실행 경로를 놓칠 수 있고, 같은 해석으로 만든 테스트는 그 누락을 확인하지 못할 수 있다. 사용자는 AI가 무엇을 이해했는지, 무엇이 미확정인지, 어느 경로를 검증했는지 직접 볼 수 있어야 한다. QA는 기획 적합성뿐 아니라 고객 문제 해결과 기획 밖의 위험 탐색도 다뤄야 한다.

참고한 비공개 사고 기록에는 한 유형의 누락을 확인한 뒤 다른 유형까지 확정된 요구로 잘못 해석했다가 정정한 내용이 있다. 이 문서에서는 이를 합성 사례로 일반화한다. 당시 집중 분산은 사용자의 회고에 따른 가설이며 근본 원인으로 확정하지 않는다. 원본 애플리케이션의 현재 코드·배포 상태를 이번 작업에서 재검증한 것은 아니다.

## 사용자가 관찰할 결과와 되읽기 초안

사용자가 한 문장으로 시작하면 AI는 저장소에서 사실을 조사한 뒤 다음 정도의 설명을 제시한다.

> 제가 이해한 목적은 제외 대상으로 지정한 항목이 실제 선택 결과에 나오지 않도록 하는 것입니다. 확인한 경로는 A와 B이고, 두 경로에 같은 결과가 필요하다는 승인 근거가 있습니다. C는 ‘추가해도 된다’는 의견과 ‘미제공’ 설계가 충돌합니다. C의 적용 여부만 결정이 필요합니다. 제외 목록에 없는 항목과 기존 지역 조건은 유지되어야 합니다. 각 경로에서 설정 저장과 실제 선택 결과를 따로 확인하겠습니다.

이는 질문 형식의 예시다. 실제 발견·승인 근거 없이 경로 또는 의도를 만들어 넣지 않는다. 질문은 정상 예시·반례·선택에 따른 결과를 포함하고, 이미 승인된 결정은 반복해서 묻지 않는다. 원문과 다른 해석을 사용자가 수정하면 관련 시나리오와 증거를 다시 검토한다.

## 입력 출처와 보존 범위

아래 `SRC`는 이 대화에서 현재 확인할 수 있는 사용자 요청의 논점별 식별자다. 설명은 공개 가능한 요약이며 원문 직접 인용이 아니다. U01은 최초 사고 검토 요청, U02는 QA 경험 요청, U03/U04는 그에 대한 주석 묶음, U05는 적용 방법 요청, U06은 0.4.0과 이해 누락 질문, U07은 질문·최소 기획 질문, U08은 되읽기 동의, U09는 브라운필드 질문, U10은 SSOT 없는 발견 질문, U11은 자기 적용 질문, U12는 첫 진행 요청, U13은 단계 안내와 다음 단계 진행 요청을 가리킨다.

이 표는 확인 가능한 논점을 추적하며, 전체 대화 원문이나 비공개 사고 문서의 대체 정본이 아니다. 외부 검토자가 해당 원문을 보지 못하면 원문 누락 감사는 `human-review`로 남는다. 회사·사람·배포처·비공개 링크는 공개 저장소에 복사하지 않는다. 과거 AI 답변의 제안을 사용자 결정으로 승격하지 않는다.

| Source | 위치와 요약 | 분류 | 범위 | 연결 |
| --- | --- | --- | --- | --- |
| SRC-001 | U01: 별도 실행 경로의 기능 누락을 검토해 달라 | fact | private-context | REQ-001 |
| SRC-002 | U01: 여러 업무와 집중 분산이 당시 배경이었다 | fact: 사용자 회고 | private-context | REQ-002 |
| SRC-003 | U01: 여러 번 반복 검토하면 누락을 줄일 수 있는가 | question | public-common | REQ-003 |
| SRC-004 | U02/U03/U06: 기존 릴리스와 완료된 DB 작업의 영향 확인 | approved-decision: 기존 작업 경계 유지 | project-local | REQ-004 |
| SRC-005 | U02: QA 시나리오·결과·버전을 기록하는 절차가 필요하다 | proposal | profile-conditional | REQ-005 |
| SRC-006 | U02: 이전/신규 클라이언트·서버, 회귀, DB까지 검증했던 경험 | fact: 사용자 경험 | private-context | REQ-006 |
| SRC-007 | U02/U04: QA가 고객 문제 해결과 시스템 이해를 확인했으면 한다 | proposal | public-common | REQ-007 |
| SRC-008 | U02/U04: 여러 도구의 변경·결함·검증을 한눈에 볼 수 있는가 | question | project-local | REQ-008 |
| SRC-009 | U03: 기획자·디자이너에게 GitHub 사용을 강제하기 어렵다 | fact: 사용자 제약 | public-common | REQ-009 |
| SRC-010 | U03: 구현/QA 별도 저장소에 QA 영역을 강제하지 않을 방법 | question | profile-conditional | REQ-010 |
| SRC-011 | U03/U04: System Book에도 반영하고 다른 집필 세션과 조율 | approved-decision: 방향 | private-context | REQ-011 |
| SRC-012 | U04: 고칠 위치를 알고 실수를 재발 방지로 연결할 방법 | question | public-common | REQ-012 |
| SRC-013 | U06: AI가 읽고도 누락·왜곡하면 사용자가 어떻게 아는가 | question | public-common | REQ-013 |
| SRC-014 | U06/U07: 최소한 어떤 기획을 제공해야 하는가 | question | public-common | REQ-014 |
| SRC-015 | U07/U08: AI가 필요한 내용을 질문하고 되읽는 방향에 동의 | approved-decision: 방향 | public-common | REQ-015 |
| SRC-016 | U07: 사람/AI/직무 간 모호함과 이해 격차를 줄일 방법 | question | public-common | REQ-016 |
| SRC-017 | U08: 모든 사용자에게 고정 설문을 전부 묻지 않는 방향에 동의 | approved-decision: 방향 | public-common | REQ-017 |
| SRC-018 | U09: 기존 정책이 없는 브라운필드에서의 적용 | question | public-common | REQ-018 |
| SRC-019 | U09: 구현 도중 절차 누락을 발견했을 때의 복구 | question | public-common | REQ-019 |
| SRC-020 | U10: SSOT나 다른 세션 기억 없이 변경을 어떻게 발견하는가 | question | public-common | REQ-020 |
| SRC-021 | U10: 기존 스킬이 너무 커지면 새 스킬로 나눠도 좋다 | approved-decision: 분리 허용 | public-common | REQ-021 |
| SRC-022 | U11: 이번 비코드 작업에도 spec-it과 테스트 우선을 적용 | proposal | project-local | REQ-022 |
| SRC-023 | U11: 대화의 내용을 빠짐없이 구현하고 검증할 수 있는가 | question | project-local | REQ-023 |
| SRC-024 | U12/U13: 명세 패키지 작성 후 단계별 진행과 상태 보고 | approved-decision: 단계 실행 | project-local | REQ-024 |

## 요구사항과 반영 위치

`candidate`는 후속 구현 후보, `boundary`는 이번 변경의 경계, `deferred`는 보존된 후속 과제다. 아래 절차는 승인 검토용이며 새 공통 MUST가 아니다. `AC`는 [수용 사례](acceptance-cases.md)의 동일 ID를 참조한다.

| ID | 요구와 완료를 관찰하는 방법 | 처리 | 대상 | 사례 |
| --- | --- | --- | --- | --- |
| REQ-001 | 유형 × 실행 경로 × 경계별로 적용/제외/미결정을 근거와 연결한다 | candidate | impact, 선택 case template | AC-001 |
| REQ-002 | 사고 사실·회고 가설·문서 정정·현재 실측을 구분한다 | boundary | specify, 사고 합성 예제 | AC-002 |
| REQ-003 | 반복 횟수 대신 누락된 연결과 미결정의 해소를 종료 기준으로 사용한다 | candidate | check | AC-003 |
| REQ-004 | 0.4.0·완료 DB 범위를 보존하고 새 버전은 별도 변경으로 다룬다 | boundary | release/migration 계획 | AC-004 |
| REQ-005 | Case ID/revision과 Run ID를 분리하고 결과·근거·확인자를 보존한다 | candidate | 최소 증거 계약; QA 운영 전체는 후속 | AC-005 |
| REQ-006 | 위험에 따라 업데이트 조합·회귀·DB·복구 사례를 선정하고 제외 사유를 남긴다 | candidate | TST-002/003/006 참조, 검증 설명·template | AC-006 |
| REQ-007 | 기획 적합성·고객 문제 해결·탐색 검증을 구분하고 계획의 오류도 발견한다 | candidate | 시나리오/검증 절차 | AC-007 |
| REQ-008 | 상위 변경 기록에서 출처·상태·결함·재검증을 조회하는 계약을 설계한다 | candidate | 참조 계약; 통합 UI/connector는 deferred | AC-008 |
| REQ-009 | 도구를 유지하고 출처별 권한·revision·확인 시각을 연결한다 | candidate | 기존 GOV-001/002, change-spec | AC-009 |
| REQ-010 | 외부 QA 증거를 참조하며 구현 저장소에 QA 코드·폴더를 일괄 생성하지 않는다 | boundary | 적용 조건, 외부 증거 예제 | AC-010 |
| REQ-011 | 파일럿 결과·반례를 System Book에 전달할 수 있게 보존한다 | deferred | 집필 원고 반영은 결과 확인 후 별도 작업 | AC-011 |
| REQ-012 | 결함에서 잘못된 정본/코드/데이터/환경을 식별하고 수정·회귀·재검증을 연결한다 | candidate | 사례·증거 계약 | AC-012 |
| REQ-013 | 원문 의도→해석→시나리오→경로→증거의 연결과 미검증 목록을 사용자에게 보인다 | candidate | specify/check, 선택 추적 항목 | AC-013 |
| REQ-014 | 목적·대상·결과·반례·제약·판정 기준·결정자를 AI가 최소 문서로 정리한다 | candidate | specify/change-spec | AC-014 |
| REQ-015 | 결과 예시·반례를 포함한 되읽기를 하고 중요한 차이만 질문한다 | candidate | clarify | AC-015 |
| REQ-016 | 용어/직무별 충돌은 출처와 선택의 효과를 제시하고 담당 결정자가 해소한다 | candidate | clarify/GOV-001/002 | AC-016 |
| REQ-017 | 질문 목록을 조건부 템플릿으로 제공하고 알려진 사실·승인된 선택은 재질문하지 않는다 | candidate | specify/clarify | AC-017 |
| REQ-018 | 미채택 저장소는 shadow assessment로 시작하고 현재 동작을 요구 승인으로 간주하지 않는다 | candidate | impact/check | AC-018 |
| REQ-019 | late-entry 시 이미 변경한 범위·빠진 증거·재확인 필요를 기록한다 | candidate | impact/specify/check | AC-019 |
| REQ-020 | 조사 범위·기준 revision·변경 신호·접근 불가·유효성 재검토를 세션 밖에도 남긴다 | candidate | impact/선택 relations | AC-020 |
| REQ-021 | 영향 조사 책임을 작은 별도 스킬로 분리하고 기존 5개 스킬과 인계한다 | candidate | spec-it-impact 후보 | AC-021 |
| REQ-022 | 수용 사례를 먼저 고정하고 기준선·구현 후 행동·독립 검증을 구분해 남긴다 | boundary | 이번 변경 패키지 | AC-022 |
| REQ-023 | 출처→요구→산출물→사례를 대조하고 미연결·미검증·후속을 별도 표시한다 | boundary | 이번 추적표/verification | AC-023 |
| REQ-024 | 산출물 4개와 단계별 상태로 진행을 보이며, 각 단계 완료를 전체 구현 완료와 구분한다 | boundary | 현재 변경 패키지 | AC-024 |

## 적용 기준과 제안의 경계

현재 lock에서 직접 관련된 기준은 [GOV-001](../../../rules/governance/GOV-001.md), [GOV-002](../../../rules/governance/GOV-002.md), [GOV-004](../../../rules/governance/GOV-004.md), [HITL-001](../../../rules/hitl/HITL-001.md), [HITL-002](../../../rules/hitl/HITL-002.md), [TST-001](../../../rules/testing/TST-001.md), [TST-002](../../../rules/testing/TST-002.md), [RULE-001](../../../rules/rule-system/RULE-001.md), [RULE-002](../../../rules/rule-system/RULE-002.md), [RULE-003](../../../rules/rule-system/RULE-003.md), [TOOL-002](../../../rules/tooling/TOOL-002.md)다. 규칙 의미는 해당 정본을 따른다.

TST-001의 현재 scope는 `code-changes`다. 이번 비코드 행동 사례는 프로젝트 파일럿의 테스트 우선 계약이며 실행 코드 TDD를 수행했다는 주장이 아니다. 독립 검증은 TST-002에 따라 별도 문맥에서 수행할 후속 gate다. TST-006과 DATA-009는 외부 QA/DB 예제를 설계할 때 참조할 후보이며 현재 self lock에 새로 추가하지 않는다.

| 결정 | 상태 | 소유자 | 현재 제안과 재검토 조건 |
| --- | --- | --- | --- |
| DEC-001: 현 단계 | approved | intent-owner | U12로 초안 작성, U13으로 단계 안내 및 2단계 실행 |
| DEC-002: 의도·되읽기·영향 추적 방향 | approved-direction | intent-owner | 동의된 되읽기·조건부 질문·새 스킬 허용 범위 유지 |
| DEC-003: 규칙/스킬 설계 | superseded-in-part-by-DEC-009 | architecture-owner | 2단계의 새 규칙 제안은 미채택. impact 분리는 유지하고 기존 규칙 실행 절차로 구현 |
| DEC-004: 적용 범위와 버전 | superseded-in-part-by-DEC-009 | intent-owner, architecture-owner | 0.5.0 후보 유지. 모든 risk profile을 보존하고 새 의무를 추가하지 않음 |
| DEC-005: QA 도구와 campaign | deferred | intent-owner | 현 도구/저장소를 유지하는 최소 참조 계약을 먼저 실험. 통합 UI와 campaign schema는 실제 다중 저장소 파일럿 후 필요성 판단 |
| DEC-006: 새 artifact schema | selected-for-pilot | architecture-owner | 최소 항목 계약과 선택 템플릿으로 구현. 공개 schema 추가·기존 schema version 변경은 이번 후보에서 제외 |
| DEC-007: 기존 기준선 digest 불일치 | resolved-for-local-candidate; history-retained | architecture-owner | 발생 구간 c9584bc→v0.4.0 확인. 3단계에서 그룹별 정렬로 기록값 재현; 당시 실행 명령 원본은 미확인. 6단계에서 0.5.0 후보 lock을 전역 경로 정렬로 재계산하고 migration/release 증거에 이력을 보존 |
| DEC-008: 기준선 이후 구현 우선순위 | selected-for-pilot | architecture-owner | GAP-001 조사 신선도 인계와 GAP-002 선택적 원칙 문서 인계를 우선 보완. 기존 규칙으로 충족한 행동에 새 의무가 필요한지는 4단계에서 중복 대조 후 재판단 |
| DEC-009: 기존 규칙 재사용 | selected-for-candidate | architecture-owner | 기존 권한과 독립 검증을 재사용. impact·기존 스킬 인계·선택 template로 구현하고 GOV-005/TST-007/profile/schema 추가는 하지 않음. 상세는 implementation.md |

`selected-for-pilot`은 사용자에게서 동의받은 방향 안에서 정한 기술적 구현 선택이다. 새 의무를 이미 발행/채택했다는 의미가 아니다. 기준선 실행으로 중복이나 과도한 절차가 드러나면 사례 기대값을 통과에 맞춰 바꾸지 않고 설계를 재검토한다.

DEC-007은 새 사용자 요구가 아니라 이번 자기 적용에서 발견한 기준선 문제다. 고정 snapshot에 대한 비교 실험은 기존 lock 결함의 면제나 정상 수렴이 아니다. 기존 배포물을 수정하는 patch release가 별도로 필요하면 그 범위를 따로 결정한다.

## 2단계에서 선택한 구현 계약

다음은 2단계 설계 이력이다. **아래 새 규칙·profile 추가는 DEC-009로 미채택되었으며 실행할 현재 계획이 아니다.** 3단계 관찰 이후 선택한 실제 구현 범위는 [implementation](implementation.md)에 기록한다. 영향/의도/증거의 최소 항목은 선택적 실행 절차로 유지한다. 고정 사례의 기대값은 바꾸지 않는다.

### 규칙의 책임과 도입 조건

| 대상 | 추가할 의미와 기존 규칙과의 차이 | 적용·증거·한계 |
| --- | --- | --- |
| GOV-005 — 의도 해석 근거 | GOV-001은 권한, GOV-002는 승인 여부를 다룬다. 새 규칙은 원문의 목적/대상/결과/반례/제약을 해석한 근거와 되읽기·정정 기록을 다룬다 | material change에서 최소 의도와 출처를 확인. 승인된 의미를 재사용할 수 있으며 질문 전체 세트는 불필요. intent-owner 소유, 명시적 material 미결정을 생략하는 예외는 없음 |
| TST-007 — 적용 범위와 수용 증거 | TST-002는 검증 문맥의 독립성을 다룬다. 새 규칙은 승인 시나리오마다 변형/경로/경계/결과 증거의 연결과 누락을 다룬다 | standard/high 동작 변경에 적용. 하나의 경로면 한 행으로 충분. 외부 QA 증거와 사유 있는 N/A 허용. 증거 누락을 통과시키는 자동 면제는 없음 |
| spec-it-impact | 현재 각 스킬의 preflight 신호를 조사·관계·확인 한계가 남는 결과로 구체화한다 | read-only 조사, 문맥 재사용, `preflight/delta/completion/brownfield/late-entry` 모드. 승인/정책 투영/수정/준수 판정은 기존 스킬에 인계 |

두 규칙은 인터뷰에서 도출한 공통 설계 후보이며 단일 사고를 자동 강제로 승격한 것이 아니다. 4단계에서는 `origin.type: design-interview`, `enforcement.mode: manual`, `implementation: advisory`로 검토했으나 DEC-009에 따라 새 규칙으로 채택하지 않았다. 5단계에서 실패와 적용 부담을 검토했고 자동 validator/CI 승격은 포함하지 않는다. 6단계는 기존 규칙을 재사용하는 instruction·선택 템플릿만 로컬 릴리스 후보로 준비했다.

GOV-005의 profile 후보는 risk/low·standard·high, TST-007은 risk/standard·high다. 정책 파일에 존재한다는 이유만으로 선택하지 않은 프로젝트를 위반으로 판정하지 않는다. low에서 명시적으로 검증을 요청하면 같은 절차를 선택적으로 쓸 수 있다. profile 도입은 정상 재수렴 때만 일어난다.

### 최소 데이터와 소유권

- 의도: why, affected users, observable result, example/counterexample, unchanged constraints, acceptance owner, source locator/revision, unresolved decision. 모르는 정보는 unknown/open으로 표시한다. 사용자가 모든 칸을 미리 채울 필요는 없다.
- 영향: 조사 시점/기준 commit/dirty 식별자, 조사 경로와 소비자, 판단 근거, 적용/제외/미결정/미접근, 재확인 trigger. 발견한 후보 관계와 확인한 관계를 구분한다.
- 시나리오: Change ID, Scenario/Case ID와 revision, 의도 근거, 적용 변형/경로, 예상 관찰, 검증 위치. code/UI/DB가 실제로 관련될 때만 각각 연결한다.
- 실행: Run ID, case/intent/fixture/build revision, 환경과 관련 DB 상태, 예상/실제 결과, 증거, 확인자, defect/fix/retest. 불필요한 DB 항목은 사유 있는 N/A다.
- 출처 연결: 상위 change 기록이 원본 링크와 역할을 소유하고 하위 기록은 ID로 참조한다. 특정 도구·중앙 서비스·파일 배치는 고정하지 않는다. relation 파일은 선택 사항이며 상시 동기화의 증거가 아니다.

specify는 승인된 쓰기 범위에서 의도와 영향 기록을 저장하고 clarify는 결정 기록을 갱신한다. impact와 check는 결과/갱신 필요를 반환한다. 읽기 전용 호출 중에는 기록을 몰래 수정하지 않는다. 쓰기가 허용되지 않으면 인계할 출력에 조사 기준과 미확인 범위를 담는다. 외부 QA 정본에 대한 쓰기는 그 권한을 별도로 따른다.

### 산출물과 인계

4단계 대상은 새 규칙 2개와 impact 스킬, 기존 specify/clarify/converge/check/evolve의 필요한 인계, change-spec 및 선택 증거 템플릿, work-cycle/traceability/verification 설명과 합성 예제다. 긴 모드별 설명은 필요한 reference로 분리하고 짧은 스킬을 위해 불필요한 파일을 만들지 않는다. 공개 schema와 별도 QA profile/campaign engine은 추가하지 않는다.

3단계에는 기존 0.4.0 스킬을 주고 같은 사용자 요청을 수행시킨다. 존재하지 않는 impact 스킬을 호출하게 해서 실패를 만들지 않는다. 5단계에는 후보 스킬을 주되 원시 자료와 요청은 같은 revision으로 사용한다. 구현 방향이나 기대 답안은 수행 agent에 제공하지 않고 평가자가 보유한다. 이 본문은 설계 기록이며 실행 agent에게 주는 입력이 아니다.

## 구현 후보와 사이드 이펙트

- 질문 증가: 결정에 영향이 있는 누락만 질문하고 승인 근거가 있는 답을 재사용한다. AC-017로 경미한 작업 부담을 확인한다.
- 잘못된 확신: 파일/ID 존재, AI 요약, 테스트 통과만으로 완전성을 선언하지 않는다. 관찰 범위 밖은 `unknown`, 미결정은 `open`, 실행 증거 없음은 `not-run`이다.
- 추적 문서의 노후화: 정본을 복제하지 않고 revision과 관계를 저장한다. 출처·기준 commit·dirty 상태·관련 결정 변경은 해당 연결과 실행 결과의 재검토 신호다.
- 비용과 조사 범위: 변경과 연결된 경로·소비자를 우선 조사한다. 전사 저장소 검색이나 상시 감시는 포함하지 않는다. 미접근 관계는 한계와 소유자를 기록한다.
- 스킬 중복과 도입 부담: 조사 결과는 한 번 생성해 인계하고 결정/수렴/판정은 기존 스킬 소유로 둔다. 외부 도구나 QA 저장소 도입은 필수가 아니다.
- 개인정보/회사 정보: 예제는 합성한다. 원문 공개나 비공개 시스템 접근이 필요하면 그 범위를 별도로 정한다.

## 검증 순서와 종료 기준

1. 수용 사례 v1을 정책 구현 전에 작성하고 draft 검토 상태로 보존한다.
2. 0.4.0의 문서상 지원을 조사한다. 이 관찰은 행동 테스트의 red 증거가 아니다.
3. 수용 사례가 승인되면 0.4.0에 동일 입력으로 행동 검증을 수행한다. 이미 충족되는 사례는 유지 테스트가 된다. 실패를 일부러 만들어 기록하지 않는다.
4. 승인된 범위의 정책·스킬·템플릿을 구현하고 같은 사례와 반례를 재검증한다. 기대값 수정 시 사람의 결정과 case revision을 연결한다.
5. 독립 검토자는 구현 결론 대신 원문·승인 의도·사례·관찰 자료에서 시작한다. 원문 접근 제한과 같은 모델의 상관된 오해 가능성도 기록한다.
6. SRC 전부에 REQ, REQ 전부에 AC, 구현한 REQ 전부에 실제 파일과 관찰 결과가 연결되어야 한다. `deferred`를 구현 완료로 세지 않는다. 의미상 누락 감사는 계속 `human-review`다.
7. release에는 material open 결정 해소, 승인된 적용 사례의 증거, 알려진 한계, 변경된 projection/예제/index/migration 확인이 필요하다. 릴리스 뒤에만 해당 버전을 프로젝트 채택 대상으로 삼는다.

1단계의 완료 기준은 4개 draft 파일의 존재·연결·형식·기준선 보존이었다. 2단계의 완료 기준은 실제 불일치 구간/미확인 원인/처리 방침 기록, 중복을 검토한 구현 계약, 고정된 case set과 다음 실행 규약이다. 전체 기능 완료 기준과 분리한다. 과거 대화 중 현재 확인할 수 없는 원문까지 누락 없음을 증명하지 않는다.

## 비용·복구·비목표

현재 비용은 문서 작성과 로컬 읽기/구조 검사다. 후속 비용은 질문 횟수·필요 라운드, 조사 경로 수, 실행 시간, 오탐/누락을 파일럿에서 관찰하며 임의의 공통 임계값을 만들지 않는다.

1단계의 복구 범위는 4개 draft 파일이었다. 4단계는 impact에 명시한 스킬·템플릿·문서와 프로젝트 인계 기록으로 확장한다. 이 세션의 변경만 검토 단위로 관리하고 다른 세션의 수정을 덮어쓰지 않는다. 기존 v0.4.0, 설치된 스킬 사본·프로젝트 lock·정책 tag를 자동 변경하지 않는다.

비목표는 애플리케이션 버그 수정, 완료된 DB 작업 재구현, 운영 QA 실행, 통합 UI/connector/watcher, 실행 validator/CI 강제, System Book 원고 수정, package/plugin 배포다. 이러한 후속 과제의 근거와 재개 조건은 추적에서 유지한다.
