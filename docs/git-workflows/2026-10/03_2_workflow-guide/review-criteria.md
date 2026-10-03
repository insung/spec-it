# Issue #2 검토 기준

구현 전에 고정한 검토 입력이다. 구현 담당은 이 브랜치와 검증 입력을 읽지 않는다.

## 사용 방법

Issue #2, plan, task와 handoff를 읽고 다음 표를 실제 diff와 대조한다. 링크·Mermaid 렌더링은 직접 실행한다. 고정 입력의 읽기 사례는 검토 담당이 문서를 직접 읽어 판단한다. 스킬 지시 변경이 없어 모델 응답 시나리오 반복 실행은 해당 없음이다.

## AC별 기준

| AC | 기계 확인 | 판단 질문 | 실패로 보는 예 |
| --- | --- | --- | --- |
| AC-01 | Mermaid 파싱·렌더링 | 미채택·채택·중요 변경·설명 요청을 구분하는가 | 일반 개념 질문에 새 명세·승인 강제 |
| AC-02 | manifest/lock 관련 필드·링크 확인 | 선택과 해석 결과, 변경·작성 책임을 구분하는가 | lock 직접 편집 안내 |
| AC-03 | policy.py와 TOOL-002 대조 | identity가 준수 판정이나 자동 생성 증명이 아님을 밝히는가 | digest 일치로 모든 규칙 준수 주장 |
| AC-04 | 6개 발행 스킬 원문과 표 대조 | 사용 조건·입력·산출물·파일 수정 여부·인계가 정확한가 | check가 자동 수정하거나 모든 스킬 순회 강제 |
| AC-05 | 용어 포함 확인 | finding/advisory, human-review/advisory, skill/runner, pair/loop 구분과 사례가 있는가 | advisory를 중요도 낮음 또는 pass로 정의 |
| AC-06 | baseline VERSION·원격 base·후보 상태 대조 | hook core와 독립 검증 runner를 구분하는가 | 미커밋 runner를 0.7.0 기본 기능으로 소개 |
| AC-07 | runner.py·claude.py·policy.py와 설명 대조 | 모델 호출 없음·mutation deny·fail-open을 정확히 한정하는가 | 모든 규칙 위반 자동 차단·범용 validator 주장 |
| AC-08 | Markdown 링크·Mermaid 렌더링·git diff --check | README·docs에서 접근하고 원문 연결 및 검토 증거가 있는가 | 후보 문서에 깨진 링크 또는 소스 대조 없이 pass |

## 우회 확인

| 확인 | 방법 |
| --- | --- |
| 완료 표시에 근거 존재 | task 완료 행과 diff/commit 비교 |
| 실행 결과와 검토 대상 일치 | handoff 명령·HEAD·작업본 상태 대조 |
| 정책 변경·후보 혼입 부재 | base...HEAD 파일 목록 및 정책 디렉토리 무변경 확인 |
| 병행 작업 보존 | 원래 checkout과 후보 파일의 변경 전·후 digest 비교 |

## 공통 확인

정본 규칙을 복제하지 않고 링크한다. 승인된 문서 경계만 변경한다. 댓글 기록은 없는 경우 해당 없음, 있는 경우 resolved·추적 여부를 확인한다. 머지 승인과 PR 생성은 구분한다.
