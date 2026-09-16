# 검증 기록 — 6단계 및 v0.5.0 공개 완료

Change: `20260912-intent-impact-verification`. 대상: [spec](spec.md), [cases v1](acceptance-cases.md), [impact](impact.yaml). 최종 확인일: `2026-09-16`. 이전 단계의 당시 관찰은 아래에 보존한다.

## 상태 요약

- 명세 패키지: 1~6단계와 승인된 commit·annotated tag·push·원격 공개 완료.
- 정책·스킬 구현: 스킬·템플릿·설명 구현 완료. DEC-009에 따라 규칙/profile/schema는 추가하지 않았다. [실제 파일과 요구 매핑](implementation.md).
- 기준선 행동 실행: completed — 7개 독립 수행 문맥, 8개 원본 응답, 24개 사례 중 22개 met·2개 unmet. [상세 판정](baseline/results.md), [실행 메타데이터](baseline/run-manifest.json).
- 후보 행동 실행: completed — 최종 후보 `CAND-STAGE5-20260915-04`의 24개 합성 사례 모두 met. 실패·중단 run도 보존한다.
- 후보의 독립 검증: completed — 네 감사 기록에서 IV-01·F-1·BEH-001을 발견·수정·재검증. 접근 가능한 사용자 원문을 대조했지만 원문 전체의 의미상 무누락은 계속 human-review다.
- 공통 정책 validator/CI enforcement: not-implemented.
- `0.5.0`: annotated `v0.5.0`으로 발행. [릴리스 체크리스트](../../../docs/releases/0.5.0-checklist.md)와 [release snapshot](release-snapshot.json)에 identity와 공개 검증을 기록한다.
- 기존 기준선: BASE-ISSUE-001 발생 구간과 처리 방침 확인. BAS-003에서 정렬 방식으로 기록값을 재현했고 `0.5.0` 후보 lock은 전역 경로 정렬로 정상 재계산했다. 기존 `v0.4.0` 배포물의 불일치와 당시 실행 명령 원본의 불확실성은 이력으로 남아 있다.

## 기준선 관찰 BAS-001

방법: 로컬 소스의 읽기 전용 정적 검토. revision `6a4ea01eb09bfb116ff24fd2d5253889086f9a77`, tag `v0.4.0`; 시작 worktree는 clean. 연결된 기준선 파일은 변경 명세를 제외하고 그대로 유지한다.

| 사례 | 관찰 대상 | 문서상 지원과 남은 간극 |
| --- | --- | --- |
| AC-001/003/013 | TST-002, change-spec template | 독립 수용 검증은 있음. 원문→유형→실행 경로→관찰 결과의 구체적 계약은 없음 |
| AC-002/016 | GOV-001/002, evolve routing, clarify | 사실/질문/제안/승인 분리와 권한·충돌 해소는 이미 지원함. 정정 기록 fixture로 행동을 확인할 필요 |
| AC-004 | TOOL-002, project/manifest/lock, release checklist | 발행 기준선 고정과 미발행 worktree 경계는 이미 있음 |
| AC-005/008/009/010 | RULE-003, traceability docs, change-spec | 신선도와 규칙 추적 기반은 있음. 외부 QA case revision/run/원본 revision의 공통 계약은 미구체화 |
| AC-006 | TST-003/006, 기존 DATA-009 참조 | 환경·DB 검증 관련 기반은 있음. 제품 조합별 시나리오 연결은 별도 파일럿 필요 |
| AC-007/012 | TST-002, tdd-and-verification | 같은 AI의 오해 자기 검증 문제를 설명함. 고객 목적/탐색/결함 재검증 계약은 미구체화 |
| AC-011 | evolve routing | 비공개 맥락과 공통 정책의 분리는 있음. 외부 원고 반영은 이 저장소의 동작 대상이 아님 |
| AC-014/017 | specify, clarify | 한 문장 시작·사실 조사·필요한 질문·위임 재사용은 이미 있음 |
| AC-015 | specify, clarify | 의도와 의사결정은 있음. 예시/반례 되읽기와 사용자 정정 후 연결 갱신 절차는 미구체화 |
| AC-018 | check, agent-work-cycle | brownfield shadow assessment와 기존 코드/신규 변경 구분은 이미 있음 |
| AC-019 | TST-001, check | 사후 테스트를 TDD로 부르지 않는 기준은 있음. 작업 도중 도입의 durable reconciliation 절차는 미구체화 |
| AC-020/021 | specify/check, agent-work-cycle | preflight·material signal·완료 diff 검사는 있음. impact 스킬과 세션 간 조사 기준/관계 기록은 없음 |
| AC-022/023/024 | TST-001/002, RULE-002, active change directory | 테스트·독립 문맥·증거 정직성 기반은 있음. 이번 draft로 자기 적용 실험을 시작함 |

이 표의 ‘없음/미구체화’는 조사한 문서의 계약에 대한 판단이다. AI가 반드시 실패한다는 관찰이 아니다. 기존 지원이 있는 사례도 같은 입력으로 실행하여 유지 여부를 검증한다.

## BASE-ISSUE-001 — 기존 lock의 정책 digest 불일치

- 관련 규칙: [TOOL-002](../../../rules/tooling/TOOL-002.md), [RULE-002](../../../rules/rule-system/RULE-002.md).
- 실제 관찰: `v0.4.0` tag와 HEAD가 같은 commit이며 tracked diff가 없는 상태에서 정책 파일 102개의 digest가 lock 기록과 달랐다.
- lock 기록: `sha256:2e54ebfe90ee889af1cc581ee209936b387ee5f913f9504a3ac83611f69b6b4f`.
- 실제 계산: `sha256:3360e1545cf9fe85469f484e3cbd2ba1ebc2ffbdfe4ded2f72255a5bc4c3a5b1`.
- 계산 범위/방식: TOOL-002에 따라 VERSION 및 rules/profiles/schemas의 regular file을 상대 POSIX path 순으로 정렬하고 각 path + NUL + bytes + NUL을 SHA-256에 입력했다. 파일 목록은 Git 목록과 같았다.
- 교차 확인: Ruby로 작업트리 bytes를 계산한 결과와 Node.js로 `git show v0.4.0:<path>`의 tag blob을 계산한 결과가 같았다. 도구를 달리한 계산 검증이며 독립 AI 행동 검증은 아니다.
- manifest digest는 실제 manifest bytes와 일치했다. 기존 정책/lock은 변경하지 않았다.
- 영향: 정확한 commit을 기준으로 읽기와 draft 검토는 가능하지만 lock의 source 검증 완료나 정상 재수렴을 주장할 수 없다.
- 후속: 아래 조사로 현재 불일치 값의 도입 구간과 정정 방침을 선택했다. 기존 tag와 lock은 보존한다.

### BAS-002 — 2단계 이력 조사

방법: 각 commit의 Git blob만으로 같은 TOOL-002 계산을 수행했다. 현재 작업트리나 이번 변경 문서는 digest 입력에 포함하지 않았다.

| Revision | 계산 digest | 당시 lock digest | 관찰 |
| --- | --- | --- | --- |
| c6d9f71 | 7144d722aad84bf8f5eb27f76157e6d0e1e4a0c2f71ab3b365b27629c7ebf3cc | f0f97d693823d14eee1559e8b891bd61190d42f2dc367f5f0ecfcb58375d6c00 | 초기 미발행 초안에도 다른 불일치가 있었음 |
| 8c10d64 | 3056ad720b9c3f806209a103dbd4ac77876b2b273b3555f78e9cabd70278f5ee | 3056ad720b9c3f806209a103dbd4ac77876b2b273b3555f78e9cabd70278f5ee | 일치 |
| c9584bc | 3360e1545cf9fe85469f484e3cbd2ba1ebc2ffbdfe4ded2f72255a5bc4c3a5b1 | 2e54ebfe90ee889af1cc581ee209936b387ee5f913f9504a3ac83611f69b6b4f | 현재 불일치 값 도입 |
| 6a4ea01 / v0.4.0 | 3360e1545cf9fe85469f484e3cbd2ba1ebc2ffbdfe4ded2f72255a5bc4c3a5b1 | 2e54ebfe90ee889af1cc581ee209936b387ee5f913f9504a3ac83611f69b6b4f | 같은 불일치로 릴리스 |

확정된 원인은 `c9584bc`가 기록한 checksum이 그 commit의 규정된 정책 파일 집합을 식별하지 못한다는 것이다. 직전 정상 commit 이후 달라진 정책 입력은 profiles/README.md, db-migration/rds profile, DATA-009/010의 5개 파일이다. 마지막 release commit은 이 정책 입력과 digest를 바꾸지 않고 lock의 초안 표시를 발행 표시로 바꿨다. 따라서 이번 문서 추가가 만든 불일치는 아니다.

당시 잘못된 값을 생성한 작업 과정은 Git 내용만으로 확정하지 못했다. 두 가설을 제한적으로 확인했다.

1. 5개 변경 파일 중 일부만 과거 내용으로 계산했는지 32개 조합을 비교했으나 기록값과 일치하지 않았다.
2. lexical/locale 정렬, VERSION의 위치, README 제외 방식의 대표 변형 5개를 비교했으나 기록값과 일치하지 않았다.

2단계 당시 추가 가설 반복은 중단했다. 그 시점에는 기록값을 재현하지 못했다. 이후 BAS-003에서 다른 정렬 규약으로 재현한 결과를 별도로 보존한다. release checklist의 체크 표시는 최종 commit에 대한 재현 가능한 계산 증거를 대신하지 못한다.

### BAS-003 — 3단계 독립 수행자의 추가 발견

[PK-07 원본](baseline/responses/PK-07.md)의 수행자가 같은 102개 파일을 `VERSION → rules → profiles → schemas` 그룹 순서로, 각 그룹 내부만 정렬하면 기존 lock 값 `2e54ebfe…`가 나오는 것을 발견했다. 부모도 `git show v0.4.0:<path>`의 immutable blob으로 재계산하여 확인했다. 전체 상대 경로를 한 번에 정렬하면 규정값 `3360e154…`가 나온다.

이는 불일치의 계산 메커니즘 재현이며 당시 실행 명령 원본을 확보했다는 뜻은 아니다. 기존 tag/lock을 수정하지 않았고 DEC-007의 최종 후보 정정 gate도 유지한다. 독립 문맥이 부모의 앞선 조사에서 놓친 원인을 추가 발견한 실제 사례다.

### DEC-007 처리와 후속 gate

- 3단계 비교 실험: 원래 v0.4.0 tag/commit/lock을 보존하고 실제 digest `3360e154…`를 함께 기록한다. 정상 준수 판정은 하지 않으며 AC-004에서 이 결함의 보고도 검증한다.
- 4~5단계 후보 검토: working source는 미발행 후보로 표시한다. 0.5.0 문자열만 넣은 manifest/lock을 발행 source처럼 사용하지 않는다.
- 6단계 정정: 최종 VERSION 및 rules/profiles/schemas bytes를 고정한 뒤 digest를 재계산하고 후보의 lock/projection과 대조한다. 입력이 바뀌면 다시 계산한다. 0.4.0의 알려진 불일치와 재수렴 안내를 migration/release 기록에 남긴다.
- 별도 0.4.x patch release가 필요한지는 이 작업에서 결정/실행하지 않았다. v0.4.0 tag를 덮어쓰거나 현재 generated lock을 수동으로 고쳐 과거 증거를 지우지 않는다.
- 기준선 결함의 공개 정정은 아직 미완료지만, 비교 실험의 식별 기준과 후속 처리 선택은 완료했다. 이 범위에서 2단계를 닫고 3단계로 진행할 수 있다.

## CASESET-001 — 기준선용 수용 사례 고정

- 파일: [acceptance-cases.md](acceptance-cases.md), revision v1, 상태 baseline-ready.
- 단계: 2. 원시 fixture 작성과 실제 agent 실행은 3단계에 수행한다.
- 내용: case 24개를 PK-01~07의 7개 실행 준비 묶음에 배정. 수행 agent에게 기대값을 제공하지 않는 규약을 포함한다.
- 변경 이력: 실행 전 초안 단계에서 AC-004 digest 반례와 AC-024 단계별 보고를 구체화했다. 이전 행동 run은 없어 변경한 기대값으로 이전 성공을 소급하지 않았다.
- SHA-256: `4979d46c51f083a5f7470688e967db404603c794749097629e445467158bc929`.
- 기대값을 바꾸는 후속 편집은 새 revision과 사유를 보존한다. baseline이 이미 충족한 항목을 실패로 만들기 위해 기대값을 바꾸지 않는다.

## 행동 실행 판정

아래 baseline은 고정 합성 입력의 실제 응답에 대한 수동 판정이며 candidate는 미실행이다. 각 응답과 판단 근거는 [결과표](baseline/results.md)에 있다. 구조 확인 결과를 이 칸에 대신 쓰지 않는다. AC-011/020은 일부 기대 항목이 누락되어 unmet으로 유지한다.

| Case | Requirement | Baseline | Candidate |
| --- | --- | --- | --- |
| AC-001 | REQ-001 | met | met |
| AC-002 | REQ-002 | met | met |
| AC-003 | REQ-003 | met | met |
| AC-004 | REQ-004 | met | met |
| AC-005 | REQ-005 | met | met |
| AC-006 | REQ-006 | met | met |
| AC-007 | REQ-007 | met | met |
| AC-008 | REQ-008 | met | met |
| AC-009 | REQ-009 | met | met |
| AC-010 | REQ-010 | met | met |
| AC-011 | REQ-011 | unmet | met |
| AC-012 | REQ-012 | met | met |
| AC-013 | REQ-013 | met | met |
| AC-014 | REQ-014 | met | met |
| AC-015 | REQ-015 | met | met |
| AC-016 | REQ-016 | met | met |
| AC-017 | REQ-017 | met | met |
| AC-018 | REQ-018 | met | met |
| AC-019 | REQ-019 | met | met |
| AC-020 | REQ-020 | unmet | met |
| AC-021 | REQ-021 | met | met |
| AC-022 | REQ-022 | met | met |
| AC-023 | REQ-023 | met | met |
| AC-024 | REQ-024 | met | met |

## 후속 run에 보존할 필드

실행할 때마다 append하는 독립 run 기록에 다음을 남긴다. 현 단계에서 가짜 run이나 확인자를 생성하지 않는다.

- Run ID, 실행 시각, case ID/revision, intent/fixture revision.
- policy version/commit, 대상 revision과 dirty diff/snapshot 식별자.
- actor/model, 도구·환경, 외부 source revision 또는 확인 한계.
- 예상 결과, 실제 관찰, met/unmet/blocked, 증거 위치와 확인자.
- defect ID, 수정 revision, 후속 run, 남은 결정, 이 결과를 다시 확인할 trigger.

내용을 바꾼 뒤 같은 Run ID를 덮어쓰지 않는다. 이후 실제 실행 기록이 별도 저장소에 있으면 그 정본을 참조한다.

## 구조 검사 STR-001 — 1단계 당시 기록

상태: 구조 확인 완료, 기존 기준선 finding 1건 유지. 방법은 임시 Ruby 읽기 전용 검사, Git diff 확인, Node.js tag blob digest 교차 계산이다. 검사 코드를 정책 validator로 추가하거나 배포하지 않았다.

| 항목 | 실제 관찰 |
| --- | --- |
| 파일 범위 | 새 변경 디렉터리의 4개 파일만 추가됨. 기존 tracked 파일 변경 없음 |
| front matter | 기존 change-spec schema의 required/허용 key, 타입, enum, ID pattern, date, 배열 제약과 일치 |
| YAML | impact와 기준선 lock 파싱 성공; baseline 값 복사와 15개 영향 표면의 상태/참조 확인 |
| 출처/요구/사례 | SRC 24개 → REQ 24개 → AC 24개 연결, 역방향 참조와 영향도 연결에 미정의 ID 없음 |
| 실행 대기 | 24개 사례 각각의 baseline/candidate가 not-run. 실제 행동 run은 0개 |
| 상대 링크 | 27개 상대 파일 링크가 존재하는 파일로 연결됨; 새 규칙/스킬 후보는 존재하는 링크로 꾸미지 않음 |
| 공개 경계 | 알려진 개인 경로·회사명·비공개 시스템 식별자에 대한 제한된 문자열 검사에서 일치 없음. 완전한 비밀정보 감사는 아님 |
| whitespace | 4개 추가 파일 각각에 git diff --no-index --check 실행, 진단 출력 없음 |
| 기준선 | HEAD/tag는 기존 commit, manifest digest는 일치; policy digest는 BASE-ISSUE-001로 불일치 유지 |

초기 검사에서 draft에 옮겨 적은 manifest digest 오타를 찾아 정정했다. 로컬 Ruby 버전이 지원하지 않는 검사 문법과 `git diff --no-index`의 차이 존재 exit 1을 whitespace 실패로 해석한 검사 코드도 수정했다. 제품 동작의 red/green 증거로 세지 않는다.

이는 이 draft의 로컬 구조 확인이다. 실행 validator 제품이나 모든 의미의 준수 검사를 구현한 것이 아니다. ‘24개 연결’은 기록한 항목의 구조적 연결 수이며 원문 전체의 의미상 완전성 또는 24개 기능 구현 완료를 뜻하지 않는다.

## 구조 검사 STR-002 — 2단계

상태: 구조 확인 완료. 로컬 Ruby/Git 읽기 전용 검사 프로세스가 exit 0으로 종료했다. STR-001의 과거 개수와 결과는 보존한다.

| 항목 | 관찰 |
| --- | --- |
| 진행/결정 | spec의 6단계 상태와 impact의 completed [1,2]/next 3 일치. 7개 결정 참조 해소 |
| 추적 | SRC/REQ/AC 각 24개, 양방향 연결과 영향도 참조 일치 |
| 실행 준비 | PK 7개에 case 24개가 중복/누락 없이 배정. 행동 run은 여전히 0개 |
| case 고정 | CASESET-001 SHA-256과 파일 bytes 일치 |
| 영향 | 16개 표면의 적용/제외/미결정/미접근 상태 확인. low QA 기본 제외와 공개 schema 보존 확인 |
| 파일 구조 | 기존 front matter 제약, YAML, 상대 파일 링크 28개 확인 |
| 범위/공개 경계 | 변경 패키지 4개만 존재. 알려진 private marker 일치와 whitespace 진단 없음 |
| 기준선 | HEAD와 모든 tracked 파일 보존. 기존 digest 결함은 미해결로 표시되어 있음 |

이 exit 0은 draft 구조 검사의 실제 종료값이다. spec-it validator의 실행/준수 통과, 24개 행동 사례 통과 또는 독립 검증 완료를 뜻하지 않는다.

## 구조 검사 STR-003 — 3단계 최종 확인

확인일: `2026-09-13`. 임시 Node.js/Ruby 읽기 전용 검사로 아래 항목을 확인했다. 검사 프로그램을 정책 validator로 추가하지 않았다.

| 항목 | 실제 관찰 |
| --- | --- |
| 범위 | 변경 패키지 23개 파일; tracked 정책·스킬·lock 변경 없음 |
| case 고정 | 수용 사례 v1 SHA-256 유지. 실행 후 기대값 수정 없음 |
| 입력·응답 보존 | 입력 9개와 원본 응답 8개의 hash/bytes가 run-manifest와 일치. 응답 8개 모두 임시 실행 공간 원본과 byte 일치 |
| 합성 소스 | PK-05-source의 6개 코드 블록이 임시 app 파일과 일치. 이 Markdown 자체가 실행 공간에 복사된 것으로 주장하지 않음 |
| 실행·판정 | 7개 packet에 24개 case가 중복/누락 없이 연결. manifest·결과표·이 문서가 22 met/2 unmet으로 일치. candidate는 24개 모두 not-run |
| 구조 | 기존 front matter 제약, YAML, 완료 단계 [1,2,3]/다음 4, 영향 표면 17개와 요구 참조 확인 |
| 링크·whitespace | spec/verification/results의 상대 파일 링크 60개 해소. 추가 파일 23개에 whitespace 진단 없음 |
| 기준선 보존 | export의 tag 파일 213개가 원래 Git blob과 byte 일치; tree digest 일치. HEAD는 v0.4.0 commit 유지 |
| 기존 결함 재현 | 같은 정책 파일 102개에 전역/그룹 정렬을 각각 적용해 BAS-003의 두 digest 재현 |

첫 최종 검사에서는 PK-05-source Markdown도 실행 공간에 복사되어 있다고 가정하여 ENOENT로 중단됐다. 실제 제공 형태인 6개 app 파일과의 대조로 검사를 바로잡았고 Node.js 재실행은 exit 0이었다. 이는 검사 경로 가정의 수정이지 행동 사례의 성공/실패 변경이 아니다. Ruby 구조 검사는 별도로 성공했다.

원본 응답은 내용·표 형식까지 그대로 보존했다. 위 검사는 산출물 보존과 연결의 검사이며 의미상 원문 완전성, 공개정보 안전성 전체 감사, 실제 제품 QA 통과 또는 자동 스킬 활성화의 증거가 아니다.

## 구조 검사 STR-004 — 4단계

확인일: `2026-09-13`. `spec-it-evolve`의 중복·호환성 검토, `skill-creator`의 구조 검사와 `unlazy`의 사전 gate/재실행 방식을 적용했다. 설치·hook·실행 validator는 저장소에 추가하지 않았다.

| 항목 | 관찰 |
| --- | --- |
| 구현 범위 | 기존 source 16개 수정·신규 8개. 새 impact, 기존 5개 스킬, 선택 template·문서·예제·index·미발행 changelog/migration |
| 규칙 경계 | GOV-005/TST-007 추가 미채택. 기존 규칙·모든 profile·schema·VERSION·self manifest/lock·generated AGENTS 보존 |
| 기존 증거 | case v1과 입력 9개·응답 8개의 hash 유지. baseline 22 met/2 unmet과 candidate 24 not-run 유지 |
| 구조 | 6개 skill entrypoint에 bundled quick_validate 성공. front matter/schema 항목·YAML·24개 요구 매핑·17개 영향 표면·상대 링크와 whitespace 확인 |
| GAP-001 | impact 결과와 선택 양식에 관측 시각/미확인 사유·revision/dirty·관계·재검토 조건 추가. 행동 재검증은 미실행 |
| GAP-002 | 조건부 evolve 인계와 프로젝트 원칙 인계에 반례·공개 범위·최신 원고 확인 추가. 원고 조회/편집/전달은 미실행 |
| gate | G1/G2/G3 재실행 exit 0·EXPECT 일치, G4는 부모의 수동 의미 대조. 4 met/0 unmet/0 abandoned. 독립 행동 판정과 별개 |
| 후보 식별 | [snapshot](implementation-snapshot.json)의 공개 source 221개 tree hash와 변경 24개 hash 재확인. 평가자 입력/기대값/응답을 담은 변경 디렉터리는 제외 |
| 재검토 | source bytes가 달라지면 새 snapshot ID로 보존하고 5단계 평가 대상을 다시 고정. policy digest만으로 스킬 동일성을 판정하지 않음 |

G2 최초 실행은 아직 없는 impact 파일에서 실패했고 구현 후 통과했다. 이는 구조 gate의 관찰이지 실제 행동의 실패→수정→성공 증거가 아니다. 같은 작성자의 의미 검토로 후보의 24개 사례를 met으로 올리지 않는다. 0.4.0 digest 불일치의 최종 정정은 6단계에 남아 있다.

## 독립 검토 인계

검토자는 현재 접근 가능한 사용자 원문, 승인 방향, 기준선 소스, cases v1에서 시작한다. 구현자가 작성한 요구 표만 읽어서는 원문 누락을 검증할 수 없다. 원문을 볼 수 없으면 그 부분을 `human-review`로 유지하고 합성 사례 검토만 수행한다. 현재 작성 세션의 재독은 독립 검증으로 세지 않는다.

현재 다음 후보 검증 전에 다시 물어야 할 새로운 제품 의도 결정은 없다. DEC-009는 2단계 규칙/profile 추가 제안 대신 기존 규칙과 선택적 절차를 재사용한 실제 구현 선택이다. DEC-007의 후속 정정, DEC-005 통합 QA 도구와 System Book 후속은 기존 경계를 유지한다.

다음은 5단계 후보 실행·독립 검증이며 6단계 릴리스 준비도 남아 있다. 현재 결과를 일반적인 모델 성공률이나 실제 애플리케이션 QA 통과로 해석하지 않는다. 현재 세션의 재독이나 digest 계산을 독립 행동 검증으로 세지 않는다.

## 구조·행동 검사 STR-005 — 5단계

확인일: `2026-09-15`. 고정 사례 v1과 입력 9개를 유지하고, 후보 source를 독립 문맥에 제공해 실제 응답을 수집했다. 독립 의미 감사의 finding은 숨기지 않고 후보 revision과 선택 재실행으로 처리했다.

| 항목 | 실제 관찰 |
| --- | --- |
| 최종 후보 | `CAND-STAGE5-20260915-04`, 공개 source 221개, tree SHA-256 `699aed5164f3ae920c45c2f316aa6fb2b5da046f8ccb0bcd02e269a80a2fe963` |
| 고정 입력 | acceptance v1 SHA-256 `4979d46c…`와 baseline 입력 9개 보존 |
| 행동 결과 | 최종 유효 7개 문맥·8개 응답에서 24/24 `met`; 기준선의 AC-011/020이 후보에서 회복됨 |
| 발견→수정 | 독립 감사 IV-01, F-1과 후보 3 행동 회귀 BEH-001을 각각 source 수정·영향 packet 재실행·독립 disposition으로 닫음 |
| 실패 보존 | 후보 3의 AC-017 `unmet` 응답과 가용량 중단/부분 응답을 원본으로 보존; 최종 성공으로 덮어쓰지 않음 |
| 독립 검토 | 네 개 감사 기록. 최종 disposition/guard 감사에서 알려진 세 finding 해소, 새 P1/P2 없음 |
| 부작용 | 설치 명령·link 수정은 없으나 기존 설치 5개가 live symlink여서 미발행 source 변경이 노출됨. 새 impact 자동 설치/선택은 미검증 |
| 미완료 | 운영 QA, 원문 전체 감사, 일반 자동 skill activation, 최종 lock/projection, commit/tag/원격 공개는 수행하지 않음 |

임시 실행공간의 source·released export·입력·응답 byte를 run manifest와 대조하는 로컬 gate를 사용했다. 이 gate는 자동 spec-it validator가 아니며, 수동 사례 판정과 독립 정적 감사를 대신하지 않는다. 결과와 원본 응답·candidate revision·한계는 [후보 결과](candidate/results.md)와 [run manifest](candidate/run-manifest.json)에 있다.

## 릴리스 준비 검사 STR-006 — 6단계

확인일: `2026-09-16`. 임시 gate를 변경 전에 작성하고, `0.5.0` 투영·lock·release 문서를 갱신한 뒤 실제 worktree에서 재실행했다. 최종 실행은 exit 0이었다. 검사 스크립트는 임시 작업공간에만 두었고 정책 validator나 저장소 도구로 추가하지 않았다.

| gate | 실제 관찰 |
| --- | --- |
| version projection | VERSION, self manifest/lock, AGENTS, README, changelog, migration가 `0.5.0` 로컬 후보와 미발행 경계로 일치 |
| immutable identity | 정책 입력 102개, policy digest `sha256:a88fceb1272d3ddb47ebd08e35bacba70872f4dd5f67766eef5958fb69f316a5`; manifest digest `sha256:2e670edf60788953e98326cfef5407045deb054f047891b991b3b3fb9904c341`; lock/checklist 대조 일치 |
| structure | lock 규칙 30개 source·ID·enforcement 확인, JSON 17개와 YAML parse 성공, manifest/lock의 현재 schema 핵심 제약과 spec front matter 대조 성공 |
| links and skills | 공개 source와 선택 변경 증거 Markdown 162개에서 상대 링크 해소; projection 후에만 유효한 `templates/project/AGENTS.md` 링크 한 파일은 명시적 제외. 여섯 skill에 bundled quick validation 성공 |
| hygiene | `git diff --check` 진단 없음. 공개 source의 제한된 개인 경로·프로젝트 marker 검사 일치 없음 |
| evidence/status | spec `accepted`, impact `release-prepared`와 완료 단계 `[1,2,3,4,5,6]`, changelog의 합성 결과 한계가 일치 |
| publication boundary | 준비 검사 시 staged 파일과 `v0.5.0` tag가 없고 HEAD는 기존 `v0.4.0` commit이었음. 사용자 승인 후 별도 commit/tag/push를 수행하고 원격 identity를 대조 |
| source snapshot | 공개 릴리스 source 222개, tree SHA-256 `20ed1a1048a1c734f2787d49471b3c810e5ceb15b783c5d9b32a960699503778`; 상세 계약은 [release snapshot](release-snapshot.json) |

첫 실행은 로컬 Ruby Psych가 `safe_load_file`을 제공하지 않아 검사 harness가 중단됐다. `File.binread`와 `safe_load` 조합으로 호환되게 고쳤다. 다음 실행은 투영 대상 template의 프로젝트 상대 링크를 이 저장소 상대 링크로 잘못 판정해 중단됐고, 해당 template 한 파일을 별도 projection 계약으로 명시한 뒤 나머지 162개 Markdown을 다시 검사했다. 둘은 릴리스 내용 결함이나 행동 사례 실패가 아니라 검사 환경·범위 가정의 수정이며, 최종 실행 전 과정을 보존한다.

G1~G5는 위 자동·구조 evidence로 met이고 G6의 사용자 설명도 완료했다. 이후 사용자의 별도 공개 승인에 따라 승인된 scope를 commit하고 annotated `v0.5.0` tag와 `main`을 push한 뒤 `HEAD == origin/main == v0.5.0^{}`를 확인했다.
