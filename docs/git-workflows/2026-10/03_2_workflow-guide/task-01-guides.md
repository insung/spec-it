# 01 흐름·용어 안내

계획: [plan의 단계 표](plan.md#단계)

## 변경 대상

| 구분 | 경로 | 이유 |
| --- | --- | --- |
| Create | docs/workflow-guide.md | 전체 흐름·파일·스킬의 사용 시점 안내 |
| Create | docs/terminology.md | 용어와 혼동하기 쉬운 관계 설명 |
| Modify | README.md, docs/README.md | 안내 진입 경로 |
| Modify | 이 작업 디렉토리 plan.md, task-01-guides.md | 실제 진행 기록 |
| Create | 이 작업 디렉토리 handoff.md | 검증 결과와 인계 |

## 작업

| # | 작업 | 완료 | 처리 내용 |
| --- | --- | --- | --- |
| 1 | 고정 정책과 스킬·hook 구현을 대조하여 진입점별 전체 흐름 작성 | [ ] | |
| 2 | manifest·lock·digest·ADR 관계와 변경 예시 작성 | [ ] | |
| 3 | 스킬 사용 조건·입력·산출물·수정 경계와 인계 정리 | [ ] | |
| 4 | 용어·사례·발행/후보/미구현 상태 설명 | [ ] | |
| 5 | 색인 연결·검증·주제별 커밋·인계 기록 | [ ] | |

## 검증

| 사례 | AC | 명령·작업 디렉토리 | 기대 결과 | 결과 |
| --- | --- | --- | --- | --- |
| <a id="tc-01"></a>TC-01 | AC-01, AC-02, AC-03, AC-04 | 정책·스킬·hook 원문 대조, 리포 루트 | 진입점·파일 역할·identity 한계·조건별 스킬 인계의 일치 | 미실행 |
| <a id="tc-02"></a>TC-02 | AC-05, AC-06, AC-07 | 용어표·상태표와 원문 대조, 리포 루트 | 용어 포함·관계 구분·후보 경계·별도 모델 호출 및 deny 설명의 정확성 | 미실행 |
| <a id="tc-03"></a>TC-03 | AC-08 | 새 안내·색인 링크 검사 및 git diff --check, 리포 루트 | 로컬 링크 존재·공백 오류 없음 | 미실행 |

## 제외 범위

- 정책·SKILL.md 지시·스키마·pin·runtime 코드 변경
- 후보 문서 또는 runner 구현을 이 브랜치로 가져오기
- review/issue-2 브랜치·worktree와 review-criteria.md·review-input 파일 읽기
