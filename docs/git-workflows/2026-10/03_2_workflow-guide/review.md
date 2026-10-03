# Issue #2 문서 구현 검토

- Issue: [#2](https://github.com/insung/spec-it/issues/2)
- 계획·작업·실행 근거: [plan](plan.md), [task](task-01-guides.md), [handoff](handoff.md)
- base: `d9ed1663f95bb6c7746aa79bb99c208d8e07cc1d`
- 검토 HEAD: `24472e21d9f817612cef447e599ce66f0502bf62`; 제품 문서 최종 commit: `2bda88025689509124638df578477c3830ed4a03`
- 검토 범위: base부터 검토 HEAD까지 문서 7개. 검토 시작 시 작업본·index clean
- 의도 출처: 실제 GitHub Issue #2 및 사용자의 구현·검증·PR 생성 요청
- 검토 기준: 구현 전 `review/issue-2`의 `fd2874c`, [AC 기준](review-criteria.md), [고정 읽기 입력](review-input-workflow.md)
- 검토 방식: 별도 구현 에이전트와 분리한 현재 세션의 직접 원문·diff 대조 및 기계 검사
- 확인일: 2026-10-03, Asia/Seoul
- 결과: **pass — 이번 문서 변경의 AC-01~08 충족**. 전체 저장소의 자동 정책 준수나 후보 실행·배포를 증명하는 판정이 아님

## AC별 대조

| AC | 기대 시나리오 | 구현 위치 | 대체 검사·실행 결과 | 판단 |
| --- | --- | --- | --- | --- |
| AC-01 | 미채택/채택/중요 변경/설명 요청 및 검토 전용 분기 | [진입점](../../../workflow-guide.md#요청에서-시작점-고르기) | 표·도식 원문 대조, 읽기 전용 N 직행 및 미결정 구현 보류 확인; Mermaid 렌더링 | 충족 |
| AC-02 | 입력/해석 결과·책임·갱신·수정 경계 | [파일 관계](../../../workflow-guide.md#무엇을-기준으로-읽고-바꾸나) | project-projection·manifest/lock schema·converge 대조, DB 추가와 오탈자 사례 확인 | 충족 |
| AC-03 | identity 식별자와 증명 한계 | [식별자](../../../workflow-guide.md#versionrevisiondigest가-각각-확인하는-것) | 고정 TOOL-002 및 policy.py 직접 대조. docs/skills 제외 범위, revision 미검사·generator 미구현 명시 확인 | 충족 |
| AC-04 | 스킬 조건·입출력·수정·인계와 선택 사용 | [스킬](../../../workflow-guide.md#필요한-스킬만-사용하기) | 6개 baseline SKILL 원문과 표 대조. check/impact 읽기 전용·후보 pair 경계 확인 | 충족 |
| AC-05 | 용어와 혼동 관계 사례 | [용어](../../../terminology.md) | 요구 용어 포함, finding/advisory·human-review/advisory·skill/runner·pair/loop 사례 직접 대조. hook 내부 pass 범위 확인 | 충족 |
| AC-06 | 발행/후보/미구현 및 두 runner 구분 | [상태표](../../../workflow-guide.md#두-runner와-후보의-상태) | baseline 파일·VERSION·별도 후보 관찰과 대조. 후보는 문자열 식별, 발행 source 링크와 구별 | 충족 |
| AC-07 | 모델 호출 없음·advisory·좁은 deny·미구현 | [hook 경계](../../../workflow-guide.md#hook이-안내하고-좁게-거부하는-경계) | core/adapter/policy reader 및 active-policy-loop 문서 대조. 범용 enforcement·fail-close 주장 없음 | 충족 |
| AC-08 | 접근 경로·링크·렌더링·근거 | README, docs/README, 위 안내 2개 | 변경/신규 상대 파일·앵커 링크 71개, diff --check 통과. 3개 도식의 9개 렌더링 성공 | 충족 |

문서 설명만 바뀌어 runtime unit test나 스킬 지시 RED/GREEN 시나리오 대상은 없다. 대신 정본 대조·링크·구조·실제 렌더링으로 확인했다. 이 예외 사유는 plan에 구현 전 기록되어 있다.

## 고정 입력 직접 재검토

| 입력 | 기대 경계 | 현재 세션 직접 읽기 결과 |
| --- | --- | --- |
| 1 | 미채택 리포의 읽기 전용 조사 | shadow assessment와 채택 승인 분리 |
| 2 | manifest 변경 후 적용 기준 | 승인 입력 변경과 재수렴, lock 직접 수정 금지 |
| 3 | digest와 준수·생성 증명 | identity만 확인, 의미 준수·결정적 생성 증명 한계 명시 |
| 4 | advisory와 finding의 의미 | 내용과 처리 효과 구분, 중요도/pass와 별개 |
| 5 | check의 실행 권한 | 읽기 전용, 수리·테스트 자동 실행·예외 승인과 구분 |
| 6 | Hard 모델 호출과 hook 오류 | 별도 모델 없음, hook crash/timeout은 fail-open 가능 |
| 7 | runner·pair의 발행 상태 | hook core는 0.7.0, pair·독립 검증 runner는 별도 후보 |

구현 담당의 응답을 채점한 것이 아니라 고정 질문으로 완성 안내와 정본을 직접 대조한 1회 읽기 검사다. 별도 모델 행동 시험은 해당 없음이다.

## 실제 실행과 관찰

- 검토 HEAD에서 Python 표준 라이브러리로 Markdown 상대 링크·heading/HTML id를 확인: 71개 통과. 기존 README 링크는 변경 행만, 새 문서·기록은 전체 검사
- `git diff origin/main --check`: 통과. 정책·SKILL·runtime·schema·manifest·lock 무변경 확인
- `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src`에서 `load_policy_view(Path.cwd(), Path.cwd())`: `0.7.0`, `v0.7.0`, 30 locked rules의 identity 확인 성공
- 검토 HEAD에서 로컬 Mermaid 11.16.1 및 bundled Playwright/Chromium으로 두 문서의 fenced block 3개 파싱·렌더링: 1000/736/360px 각 3개, 9개 화면 생성 성공
- 수정한 첫 도식 736px, 두 번째 도식 736px, 간소화한 용어 도식 360px를 시각 대조: 잘림·노드 겹침 없음. 모든 화면의 pixel-level 검사를 주장하지 않음. 긴 첫 흐름은 좁은 화면에서 확대 필요 가능
- 병행 원래 checkout 및 검증 후보의 사전 기록 파일 32개 SHA-256 재대조: 불변
- `.comments/` 및 추적 댓글 없음: 포함 또는 미해결 댓글 승인 대상 없음

검증 스크립트와 screenshot은 일시 로컬 검사 자료다. 원시 정책 보고서·인증·머신 경로·후보 코드를 저장소에 추가하지 않았다. 실행한 명령의 성공은 위 범위만 증명한다.

## 정책 대조와 한계

- GOV-001/002, HITL-001/002: 설명과 승인·권한을 구분하고 규칙·manifest를 변경하지 않음. 새 인간 판단 미결정 없음
- TST-002: 구현 담당과 검토 기준 작성·최종 판단 세션 분리. 구현 담당은 기준 브랜치 접근 없이 공개 Issue·plan·task만 사용
- RULE-003: 후보 관찰일과 source/발행/설치 변화의 재검토 조건 명시
- TOOL-002: 기존 identity 확인 성공과 결정적 generator 미구현을 구분. generator의 결정성 검증은 여전히 human-review이며 이 PR에서 자동 pass로 승격하지 않음
- TOOL-001/003: 범용 checker 미구현·읽기 전용·ignored 보고서 계약을 설명. 이 기록은 승인된 PR 검토 근거이며 routine policy JSON report가 아님
- 나머지 DB/API/runtime/보안 실행 경계는 새로 변경하지 않음. 전체 정책 자동 검사·실계정 후보 실행·게시 파일럿은 미실행이며 이번 문서 AC의 실행 대상 아님

## 다음 행동

검토 기준과 이 기록만 후속 docs 커밋으로 반입한다. 그 커밋은 제품 문서 변경 없이 검토 증거만 추가하므로 위 제품·실행 증거는 유지한다. 승인된 push·PR 생성 뒤 실제 원격 HEAD·Issue 연결·라벨·담당자·문서 접근을 재확인한다. 이후 제품 문서나 정책 source가 바뀌면 해당 범위를 다시 검토한다. **머지는 사용자 별도 승인 대기**다.
