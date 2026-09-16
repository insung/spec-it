---
name: spec-it-impact
description: Inspect the impact of a material change and return a revision-bound handoff, including unchanged consumers and inaccessible sources. Use before implementation, after scope drift, at completion, or for brownfield and late-entry recovery. Does not adopt policy, approve intent, or modify project files.
---

# spec-it:impact

변경의 적용 범위와 조사 한계를 읽기 전용으로 반환한다. 문서 허브나 관계 파일은 필수가 아니다. 이 Phase 0 스킬은 상시 watcher, QA runner, 정책 validator가 아니다.

## 조사 진입점

프로젝트 AGENTS, 활성 요청/명세, 승인 기록, 제공된 원본, Git 상태와 이전 조사 결과부터 읽는다. manifest/lock이 있으면 정확한 고정 소스를 사용한다. 없으면 `shadow assessment`로 후보를 구별하며 현재 코드를 승인된 의도나 정책 채택으로 간주하지 않는다.

작업 위치에 맞는 모드를 선택한다. 모드를 모두 순회할 필요는 없다.

| 모드 | 확인할 차이 |
| --- | --- |
| preflight | 의도·예상 변경에서 실행 경로와 외부 경계 발견 |
| delta | 이전 조사 revision/dirty 상태/외부 출처와 현재 상태 비교 |
| completion | 실제 diff와 승인 범위 비교; 연결된 미변경 소비자·검증 공백 확인 |
| brownfield | 채택 전 사실·후보·레거시·미결정과 안전한 작업 범위 구분 |
| late-entry | 이미 바뀐 내용, 실제 확인 가능한 시작점, 사라진 사전 증거와 복구 검증 계획 |

## 발견과 신선도

변경 파일만 읽지 않는다. 요청과 관련된 caller/strategy/consumer, 설정을 쓰고 읽는 곳, 저장 필드, 공개 계약, 테스트 관찰 경계를 검색한다. import만 있는 관계인지 실제 실행/배포 경로인지 근거를 구분한다. 관계 파일이 있으면 탐색의 단서로 사용하고 현재 소스로 재확인한다. 코드 diff가 없어도 승인/디자인/외부 계약 revision 변화가 결과를 바꿀 수 있다.

각 후보 경로를 `applies`(적용 근거), `excluded`(사유·결정 근거), `open`(사람의 미결정), `unknown`(접근/관찰 불가)으로 구분한다. 이 상태는 조사 용어이며 check 결과 enum이 아니다. 한 원격 소비자가 미접근이라고 전체를 미적용으로 처리하지 않는다.

결과에 다음을 명시한다. 작은 변경이면 짧은 표나 문단으로 충분하다.

- 확인 시각 `observed_at`(시간대 포함) 또는 시각 미확인 사유. 출처별 마지막 관측과 승인 시점은 구분한다.
- 조사 root/파일/경계, 사용한 검색·관계 근거, 조사하지 못한 범위.
- 이전/현재 commit 또는 snapshot, dirty 내용 식별자. HEAD만으로 미커밋 상태를 식별하지 않는다. 안전하게 digest/patch 식별자를 남길 수 없으면 그 한계와 재조회 조건을 기록하고 비밀값을 복사하지 않는다.
- 원본 locator/section, revision 또는 허용된 snapshot/digest, 의도 승인 근거. revision이 없거나 최신 조회가 불가능하면 `unknown`과 한계를 남긴다. 확인 시각만으로 버전 동일성을 증명하지 않는다.
- 발견한 변경과 미변경 관계, 영향받는 의도/시나리오/증거, 남은 사람 결정과 다음 담당 절차.
- **재검토 조건**: 새 세션/재개, HEAD·dirty·원본 revision 변화, 새 caller/설정/계약 발견, 접근 권한 변화 시 관련 결론을 다시 대조한다. 이번 조사에서 실제 적용되는 조건과 확인할 위치를 적는다.

이전 결과와 달라진 항목만 다시 평가한다. 과거 run은 당시 관찰로 보존하고 현재 사용 가능 여부를 별도로 표시한다. 열 번 재독 같은 횟수로 종료하지 않는다. 확인한 범위의 관계·근거·미결정·미접근을 다음 작업자가 찾을 수 있으면 조사 인계를 끝낼 수 있다. 접근 밖의 변경을 자동 감지하거나 모든 경로 발견을 보장하지 않는다.

## 반환과 인계

파일을 생성·수정하거나 명령으로 코드를 변경하지 않는다. 조사 결과를 반환하고, 지속 기록이 필요한 경우 **호출자가 기존 권한 범위에서** 활성 변경 기록에 저장한다. 선택적 [영향 기록 형식](../../templates/project/change-impact.md)을 사용할 수 있지만 파일명/폴더 생성이나 별도 관계 저장소를 강제하지 않는다. 다른 세션의 dirty 변경을 되돌리지 않는다.

위 템플릿 링크는 정책 source 배치 기준이다. 스킬 폴더만 따로 설치되어 링크가 없으면 프로젝트에 기록된 정책 source에서 해당 상대 경로를 찾거나, 이 문서의 반환 항목으로 인계한다. 템플릿을 찾기 위해 임의 설치·전역 설정 변경을 하지 않는다.

의도 초안은 `spec-it-specify`, 중요한 미결정은 `spec-it-clarify`, 승인된 정책 투영은 `spec-it-converge`, 고정 규칙에 대한 판정은 `spec-it-check`의 책임이다. 다른 스킬이 설치되지 않았으면 필요한 조사/결정 묶음과 역할을 설명해 인계하며 호출 성공을 꾸미지 않는다. 승인된 범위의 무관한 작업까지 멈출 이유는 없지만 미결정이 바꾸는 구현은 먼저 결정받는다. late-entry에서는 사후 명세/테스트를 과거 승인이나 사전 실패 테스트로 소급하지 않는다.
