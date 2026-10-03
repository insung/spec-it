---
issue: "https://github.com/insung/spec-it/issues/3"
status: review-pending
branch: "docs/pair-workflow"
base: "main"
created: "2026-10-03"
---

# AGENTS 기반 협업과 S3 공통화 판단 절차 계획

## 요청

> 이번 세션에서 조사한 내용들, 검토한 내용들을 정리하여 issue-create 하여 진행하고 plan-create 를 만들어서 진행해줘. 이미 커밋되거나 머지된 것은 그대로 놔두고 수정될 부분만 이슈에 머지되면 돼

- 해석: 이번 세션의 미커밋 pair·S3 설명과 관련 진입 안내를 별도 변경으로 검토·전달
- 남은 결정: pair 발행·추가 공통화 규칙은 이번 범위 밖, 머지는 최종 변경 검토 후 사용자 승인
- 의도·달성 조건 정본: [Issue #3](https://github.com/insung/spec-it/issues/3)

## 현재 동작과 변경 이유

| 현재 동작 | 근거 위치 | 바꿀 결과 |
| --- | --- | --- |
| 0.7.0 기준선과 active policy loop는 이미 커밋된 상태 | main d9ed1663f95bb6c7746aa79bb99c208d8e07cc1d, VERSION | 기존 이력·정책·실행 코드 보존 |
| pair·S3 설명은 미커밋 후보 | 기존 작업본 docs/pair-work-cycle.md, docs/s3-shared-library-pairing.md, skills/spec-it-pair/SKILL.md | 후보 상태와 확인 범위가 명확한 별도 변경 |
| pair 문서는 스킬을 중심으로 시작해 필수 스킬로 읽힐 가능성 | 기존 작업본 docs/pair-work-cycle.md 첫 문단 | AGENTS 기본 진입점과 선택적 후보 구분 |
| S3 문서가 다른 작업의 검증 도구를 현재 기능으로 연결 | 기존 작업본 docs/s3-shared-library-pairing.md 구현 범위 표 | 현재 기준선에 없는 기능 단정·깨진 링크 제거 |
| 후보 수용 사례는 정적 기대이며 실사용 미검증 | 기존 작업본 docs/pilots/pair-workflow-acceptance.md | 준비한 입력·합성 관찰·미실행·효과 미확인 구분 |

## 범위

| 구분 | 내용 |
| --- | --- |
| 포함 | 세션의 11개 후보 파일 중 Issue 범위의 문서·지침, 검증·인계 기록 |
| 제외 | rules, profiles, schemas, manifest, lock, VERSION, hook 구현, 검증 runner, 플러그인 발행, AWS 호출, 실제 소비자 구현 |
| 미변경 소비자 | 기존 채택 프로젝트·설치 사용자·active policy loop, Issue #1/#2 작업 |
| 호환성·데이터·운영 | instruction-only 후보 및 문서, 정책 의무·설치·자동 활성화·배포 변화 없음 |

원격 default branch와 main SHA를 확인했으며 기존 feature 브랜치의 명명 사례를 참고해 `docs/pair-workflow`를 main에서 분기했다. 다른 작업본을 이동하거나 지우지 않는다. 구현 worktree는 프로젝트 내부 `.worktree/pair-workflow`다. 기존 작업본의 11개 후보 파일은 안전한 임시 스냅샷과 digest로 보존했다.

## 단계

| 단계 | 제목 | 설명 | 검증 사례 | 완료 |
| --- | --- | --- | --- | --- |
| [01](task-01-guidance.md) | 설명과 진입 안내 정리 | 미커밋 후보 반입, AGENTS 기본 경로, S3 문서·현재 상태 정합성 보완 | [TC-01](task-01-guidance.md#tc-01), [TC-02](task-01-guidance.md#tc-02) | [x] |
| [02](task-02-validation.md) | 후보 검증과 인계 | 링크·후보 구조·일반/프로젝트/S3 합성 시나리오·원본 보존 검증과 증거 기록 | [TC-03](task-02-validation.md#tc-03), [TC-04](task-02-validation.md#tc-04), [TC-05](task-02-validation.md#tc-05) | [x] |

실행 순서: 01 → 02. 검증 실패 시 해당 단계 보완 후 영향을 받은 사례 재실행. 계획·검토 기준 작성 세션은 구현하지 않고 별도 구현 세션으로 인계한다.

## 최종 검증

| 사례 | AC | 명령·작업 디렉토리 | 기대 결과 | 필요 승인 | 결과 |
| --- | --- | --- | --- | --- | --- |
| <a id="tc-f01"></a>TC-F01 | AC-01, AC-02, AC-03, AC-04, AC-05, AC-06 | 변경 문서·지침 대조, 전체 상대 링크 검사 및 git diff --check, 리포 루트 | 모순·깨진 링크 부재, 정적·합성·실사용 증거 구분 | 없음 | 통과: 지침50158dee·설명643288b6 및 후속 기록 문서 대조, 상대 링크129개 오류0·diff 공백 검사 |
| <a id="tc-f02"></a>TC-F02 | AC-07, AC-08 | 기준선 대비 diff 경로·원본 후보 digest·계획/검토 분리 대조, 리포 루트 | 허용 경로만 변경, 원본 보존, 계획과 검토 기준 위치 계약 충족 | 없음 | 구현 범위 통과: 허용 경로·원본11개/index 보존·검토자료 미열람; 분리자료 정합성은 부모 세션 확인 |

프로덕션 동작이나 외부 경계를 변경하지 않으므로 AWS 통합·부하 테스트는 대상이 아니다. 지침의 합성 시나리오는 실제 호스트의 자동 선택이나 실프로젝트 효과를 증명하지 않는다. 실패 없는 기준선에 억지로 RED를 만들지 않는다. 추가 스킬의 필요성은 효과 미확인 상태로 남길 수 있다.

## 전달과 롤백

| 항목 | 내용 |
| --- | --- |
| 전달 방법 | 계획·단계별 변경·증거 커밋과 PR, 배포·태그·Release 없음 |
| 필요 승인 | 요청 범위의 Issue·계획·변경 진행, 사용자 최종 승인 후 PR 머지 |
| 적용 후 확인 | 검토한 HEAD와 PR HEAD 일치, Issue 범위와 실제 diff 대조 |
| 롤백 | 새 변경 커밋을 revert하는 별도 검토, 기존 기준선 재작성 금지 |

## 결정과 변경 기록

| 날짜 | 구분 | 내용 | 영향 AC·단계 | 상태 |
| --- | --- | --- | --- | --- |
| 2026-10-03 | 결정 | 프로젝트명 spec-it 유지, AGENTS 기본 안내와 선택적 pair 후보 구분 | AC-01, 01 | 승인 |
| 2026-10-03 | 결정 | 기존 커밋·머지 보존, 수정할 부분만 별도 Issue와 계획으로 진행 | AC-07, AC-08, 전체 | 승인 |
| 2026-10-03 | 결정 | 별도 라이브러리 분리 의무·pair 발행·런타임 구현은 범위 밖 | AC-04, AC-05, 전체 | 승인 |
