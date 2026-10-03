# 구현과 PR 리뷰 인계

- Issue: [#2](https://github.com/insung/spec-it/issues/2). 원격 PR 생성 전이며 구현 담당은 push·게시·PR을 수행하지 않았다.
- Plan / Todo: [plan](plan.md), [task-01-guides](task-01-guides.md). 구현과 자기 검사는 완료, parent의 브라우저 렌더링 확인 완료, 독립 최종 검토는 다음 담당의 확인 대기.
- base: `d0b8a8f5577c322d3e9cfc8a1010f84182b71503`; 제품 문서 commit: `ee98521e76db354e534d56dd1cbca780bf3e8df4`; 최종 제품 HEAD: `2bda88025689509124638df578477c3830ed4a03`.
- 실행 위치: 저장소 전용 workflow-guide checkout, `docs/workflow-guide` 브랜치. 제품 커밋 후 작업본 clean 확인. 확인 시각: `2026-10-03T21:01:29+09:00`.
- 실행 담당: 별도 구현 subagent. 자기 원문 대조는 독립 최종 검토가 아니다. review/issue-2 및 검토 기준/입력 파일을 읽거나 전달받지 않았다.
- spec-it: `.architecture/manifest.yaml`과 `lock.yaml`의 self pin `0.7.0` 및 현재 원문을 읽음. 정책·pin 변경 없음. 후보는 지정된 source 파일만 읽기 전용 관찰.

## 사용자 의도와 구현 결과

| AC | 기대 | 구현 위치 | TC | 자기 검사 결과·한계 |
| --- | --- | --- | --- | --- |
| AC-01 | 미채택/채택/material/일반 설명 및 검토 전용 진입점 | [사용 흐름](../../../workflow-guide.md#요청에서-시작점-고르기) | TC-01 / F01 | 본문·표·다이어그램 경로 대조. parent 최종 렌더링 확인 |
| AC-02 | manifest/lock 역할·내용·갱신·직접 수정 경계 | [파일 표](../../../workflow-guide.md#무엇을-기준으로-읽고-바꾸나) | TC-01 | 입력과 해석 결과·ADR·예시를 원문 대조 |
| AC-03 | version/revision/digest 차이·범위·한계 | [identity](../../../workflow-guide.md#versionrevisiondigest가-각각-확인하는-것) | TC-01 | TOOL-002·lock schema·policy reader 대조. revision 필드 검증과 의미 준수 한계 명시 |
| AC-04 | 스킬 조건·입출력·수정·인계 | [스킬 표](../../../workflow-guide.md#필요한-스킬만-사용하기) | TC-01 | 6개 baseline skill 및 pair 후보의 원문 대조. 모든 스킬 순회 없음 |
| AC-05 | 용어 및 혼동 관계와 사례 | [용어](../../../terminology.md) | TC-02 | finding/advisory·human-review/advisory·skill/runner·pair/loop 구분 |
| AC-06 | hook/독립 검증 runner·발행/후보/미구현 | [상태표](../../../workflow-guide.md#두-runner와-후보의-상태) | TC-02 | 2026-10-03 정적 관찰, 후보 release 부재와 재검토 조건 명시. 실행·발행 증명 없음 |
| AC-07 | 미구현 집행·Light/Hard 호출·좁은 deny | [hook 경계](../../../workflow-guide.md#hook이-안내하고-좁게-거부하는-경계) | TC-02 | 별도 모델 호출 없음·일반 advisory·좁은 mutation deny·fail-open 한계 대조 |
| AC-08 | 색인·링크·렌더링·원문 대조 | README/docs 색인과 두 안내 | TC-03 / F01 / F02 | 125개 local 링크·anchor 통과. parent 렌더링 및 선택 화면 검사 확인 |

## 계획 대비 차이와 판단

- 문서 4개만 제품 커밋에 포함. 공통 정책·SKILL.md·runtime·schema·manifest·lock 변경 없음. 기존 설명 문서·병행 후보는 그대로 보존.
- parent의 공개 AC 설명을 이용했다. 원격 `GH_TOKEN=$(gh auth token --user insung) gh issue view 2 --repo insung/spec-it`는 구현 환경에서 token/네트워크 오류로 실패했고 parent가 실제 조회한 공개 계약을 전달했다. 검토 기준은 전달받지 않았다.
- parent의 중간 원문 검토 지적(읽기 전용 check의 구현 경유 방지, 미해소 결정의 구현 보류, warn과 pass 구분)을 제품 커밋 전에 반영했다.
- Mermaid 렌더링은 parent 담당이다. 초기 용어 도식의 360px 가독성 지적을 받아 `2bda880`에서 줄였다. 최종 결과는 아래 parent 전달 증거로 기록하며 구현 담당 직접 화면 검사와 구분한다. 계획 이탈 없음.

## 검증 요약과 증거

| TC/AC | 사례 | 기대 | 실제·상태 | 명령·실행 위치 | 대상·시각 |
| --- | --- | --- | --- | --- | --- |
| TC-01 / AC-01~04 | 기준 파일·6개 SKILL·policy reader 대조 | 역할·권한·identity 일치 | 자기 정적 대조 통과 | 해당 baseline 파일 `cat`, `sed`, `rg`; 저장소 루트 | 최종 제품 `2bda880`, 2026-10-03 KST |
| TC-02 / AC-05~07 | 용어·후보·hook 원문 대조 | 허위 발행/실행/자동화 없음 | 자기 정적 대조 통과, 후보 실행 없음 | baseline active-policy-loop·src/spec_it_hook/policy.py 및 허용 후보 파일 읽기; 각 source 루트 | 최종 제품 `2bda880`, 2026-10-03 KST |
| TC-03 / AC-08 | 두 안내와 두 색인 local 링크 및 fragment | 존재와 heading 일치 | 125개 통과 | Python 표준 라이브러리로 Markdown 링크 추출, Path.exists 및 heading/HTML id 대조; 저장소 루트 | 최종 제품 `2bda880`, 2026-10-03 KST |
| TC-F02 / 전체 | whitespace 및 범위 | 문서만 변경·공백 오류 없음 | 통과 | `git diff --check`; `git diff --check d0b8a8f HEAD`; `git diff d0b8a8f HEAD --name-only`; 저장소 루트 | 최종 제품 `2bda880`, 2026-10-03T21:01:29+09:00 |
| TC-F01 / AC-01·08 | Mermaid 3개 화면 렌더링 | 오류·잘림·겹침 없음 | parent 렌더링 통과 및 선택 화면 검사 확인 | Mermaid 11.16.1 + Chromium/Playwright; 3개 도식 × 1000/736/360px (9 screenshots) | 최종 제품 `2bda880`, 2026-10-03 KST |

parent는 최종 workflow 도식을 736px, compact 용어 도식을 360px에서 시각 확인했다. 두 번째 도식은 내용이 그대로이며 앞서 736px에서 확인했다. 이 화면들에서 잘림·겹침이 없었고 9개 렌더링은 모두 성공했다. 모든 screenshot의 pixel-level 검사를 주장하지 않는다. 첫 흐름은 길어 좁은 화면에서 viewer zoom이 필요할 수 있다. 초기 렌더링은 당시 관찰로 남기고 최종 렌더링은 `2bda880`에 묶는다.

parent 추가 검사: 변경/신규 링크·anchor 71개 통과(초안 handoff 포함), policy identity `0.7.0` / `v0.7.0` / 30 locked rules 통과, 병행 후보 32개 파일 digest 불변. 구현 담당의 125개 검사는 두 안내·두 색인 전체 기존 링크를 포함하며, handoff 추가 시 134개로 재검사하여 통과했다. 검사 범위가 달라 수가 다르다. 임시 렌더링/링크 스크립트·화면 파일은 공유 문서나 커밋에 넣지 않는다.

제품 커밋 이전에 잘못된 schema 색인 링크 1개를 발견해 실제 manifest schema로 고친 뒤 125개 전체를 다시 검사했다. 제품 커밋 뒤 diff/범위 확인까지 수행했다. 설명 문서이므로 unit test와 SKILL RED/GREEN은 해당 없음이다. candidate runner/model/API/로그인/Issue 게시를 실행하지 않았다.

## 커밋과 문서 상태

- 제품 커밋: `ee98521` — `docs(workflow-guide): 정책 적용 흐름과 검토 용어 안내`.
- 추가 제품 커밋: `2bda880` — `docs(workflow-guide): 좁은 화면의 용어 다이어그램 간소화`.
- progress/handoff 문서는 다음 별도 기록 커밋에 포함한다. 자기 hash 기록을 위한 amend는 하지 않는다.
- `.comments/` 디렉터리와 추적 파일 없음: N/A. 열린 thread를 포함하지 않았다.
- 문서는 현재 로컬이며 원격 docs/PR 링크는 검증하지 않았다.

## 위험·전달·다음 검토

- parent는 최종 제품 HEAD를 고정해 독립 검토와 Mermaid 화면 검사를 수행하고 실제 결과를 기록한다. TC-F01 parent 확인을 전달받아 plan 단계 전체와 자기 검사 상태를 완료로 기록했다. 독립 최종 검토 완료를 뜻하지 않는다.
- 승인된 push/PR은 parent가 담당한다. 머지는 별도 사용자 승인이다. 서비스 배포 없음. 롤백 경계는 plan을 따른다.
- 후보 내용은 미커밋 관찰 시점에만 유효하다. 후보 발행·source/설치·pin 변경 시 원문을 다시 확인해야 한다.
