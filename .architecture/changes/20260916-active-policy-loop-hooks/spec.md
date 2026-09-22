---
id: 20260916-active-policy-loop-hooks
scope: change
status: converged
owners:
  - intent-owner
  - architecture-owner
created_on: "2026-09-16"
affects:
  - behavior
  - architecture
  - cost
---

# 능동형 policy loop와 Claude hook 파일럿

이 파일은 hook 기반 능동형 policy loop의 유일한 의도 명세다. [실행 계획](implementation.md)은 이 명세를 구현 순서와 gate로 투영한 문서이며 공통 정책이나 구현 완료 증거가 아니다.

작성 당시 공개 기준선은 `0.5.0`이었고 작업 트리에는 별도의 `0.6.0` code-rule 후보가 있었다. 이 변경은 그 후보를 덮어쓰지 않고 다음 minor인 `0.7.0`을 목표로 격리했다. 이후 `0.6.0`을 먼저 릴리스하고 이 구현을 병합해 `0.7.0`으로 재수렴했으며, 아래 행동 계약은 그대로 유지한다.

이 변경은 Phase 0 문서 절차를 실행 도구로 옮기는 Phase 1 진입이다. 실행 가능한 runner와 저장소 검증 증거가 생긴 뒤에만 roadmap과 self projection을 Phase 1로 갱신했다.

## 왜 필요한가

현재 spec-it은 규칙, 적용 절차, 사람 중단 조건을 문서와 instruction-only 스킬로 제공한다. 효과는 있었지만 AI가 이를 읽기로 선택했을 때만 작동했고, 실제 작업 중 규칙 누락이나 실행 장치의 부재도 확인됐다. 사용자가 원하는 것은 사고 뒤 위반을 판정하는 법전만이 아니라 작업 시작·material 변화·완료 시점에 현재 행동을 스스로 재판정하게 만드는 장치다.

그 장치는 매 hook마다 모든 규칙과 모든 스킬을 읽게 해서는 안 된다. 비용과 지연을 제한하면서도 중요한 변화가 생기면 관련 규칙으로 깊이를 높여야 한다. 최종 제품·위험 판단과 예외 승인은 계속 사람이 소유한다.

## 사용자가 관찰할 결과

Claude Code에서 명시적으로 파일럿을 켠 프로젝트는 다음처럼 동작한다.

1. 세션 시작과 사용자 요청마다 저비용 `Light` 평가가 실행된다.
2. `Light`는 manifest·lock·활성 변경과 작업 신호를 읽고, 대부분의 비관련 작업은 짧은 no-op으로 끝낸다.
3. API·데이터·보안·인프라·의존성·공개 계약·material 의도 신호가 새로 나타나면 `Hard`로 자동 상승한다.
4. `Hard`는 선택된 규칙만 원문에서 읽어 적용 여부, 관측 사실, 추론, 미결정, 필요한 증거를 평가 카드로 Claude의 현재 문맥에 제공한다.
5. 파일럿의 규칙 판정은 advisory다. 다만 runner가 승인된 policy state를 읽을 수 없거나 material human decision이 미해결임을 확정했고, 다음 도구가 mutation을 수행하려는 경우에는 그 도구 호출만 거부한다. 읽기·조사·복구 작업은 계속 가능하다.
6. 완료 시 실제 diff 기반 결과가 사람에게 보이지만 Stop hook이 AI를 반복 실행시키지는 않는다. 최종 승인과 다음 행동은 사람이 결정한다.

## 작성 당시 0.5.0 기준선과 목표 상태의 차이

| 관점 | `0.5.0` 현재 | 이 변경 이후 목표 |
| --- | --- | --- |
| 시작 조건 | AI가 AGENTS·manifest·lock·스킬을 읽고 절차를 따름 | local opt-in 프로젝트의 Claude lifecycle이 Light를 호출 |
| 규칙 선택 | instruction을 수행한 AI의 판단 | 결정적 signal classifier와 pinned lock이 후보를 좁힘 |
| 작업 중 재판정 | material signal에서 다시 보라는 문서 지침 | prompt·mutation tool·dirty signal checkpoint에서 자동 재판정 |
| 비용 제어 | 관련 규칙만 읽으라는 원칙, 실행 budget 없음 | Light 4,000자·Hard 8,000자/8 rules·dedup budget |
| 결과의 힘 | manual human-review | advisory + policy-unavailable/open-decision mutation의 좁은 deny |
| 완료 확인 | AI가 실제 diff를 읽어 수동 보고 | Stop에서 diff report를 자동 생성하되 AI continuation은 안 함 |
| 도구 범위 | vendor adapter 없음 | vendor-neutral core + Claude-first adapter |
| 실패 의미 | 실행 장치가 없어 실패 계약도 없음 | policy-unavailable과 runner-error/fail-open을 분리 보고 |

## 의도 되읽기와 출처

- 사용자 승인: Light·Hard는 스킬 종류가 아니라 평가 깊이와 비용 budget이다. 첫 구현은 이 두 단계만 둔다.
- 사용자 승인: mode는 runner가 신호와 비용 budget으로 스스로 선택한다. 기본은 Light이며 material signal에서만 Hard로 상승한다.
- 사용자 승인: 첫 adapter와 파일럿은 Claude Code를 대상으로 하고 지정된 고위험 Python HTTP API 저장소에서 수행한다.
- 사용자 승인: 첫 파일럿은 Light 기본, advisory 집행으로 시작한다.
- 사용자 승인: manifest·lock은 적용 자격을 뜻하고, 실제 파일럿 활성화는 프로젝트 로컬 Claude 설정에서 명시적으로 한다. manifest schema에 vendor별 opt-in 필드를 추가하지 않는다.
- 사용자 우려와 반영: hook 실패 때문에 모든 작업이 막히지 않게 읽기·진단 경로는 보존한다. 동시에 이미 판정된 policy state 오류나 material 미결정 뒤의 mutation은 진행시키지 않는다.
- 관측: 현재 `0.5.0`의 `docs/agent-work-cycle.md`는 작업 전, material signal, 완료 전 diff를 정의하지만 숨은 hook·validator·runtime enforcement는 없다고 명시한다.
- 외부 계약 관측: Claude Code hook은 프로젝트 로컬 `.claude/settings.local.json`에서 시험할 수 있고, `SessionStart`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`, `Stop` 수명주기를 제공한다. `SessionStart`는 차단할 수 없고 `PreToolUse`는 명시적 deny로 도구 호출을 차단할 수 있다. command hook의 누락·일반 오류·timeout은 대부분 fail-open이므로 hard gate로 과장하지 않는다. 관측 기준은 2026-09-16의 [Claude Code hooks reference](https://code.claude.com/docs/en/hooks)와 [settings reference](https://code.claude.com/docs/en/settings)다.

공개 spec-it 저장소에는 회사·저장소 고유 이름을 기록하지 않는다. 정확한 파일럿 대상, 브랜치, 실행 로그는 대상 프로젝트의 local 설정과 승인된 project-local evidence가 소유한다.

## 성공과 수용 기준

| ID | Given / when / then | 완료 증거 |
| --- | --- | --- |
| AC-01 | hook이 없는 프로젝트에서 작업하면 기존 동작이 바뀌지 않는다 | 비활성 fixture의 zero side-effect |
| AC-02 | manifest·lock만 있고 local opt-in이 없으면 자동 활성화하지 않는다 | eligible-but-disabled fixture |
| AC-03 | local opt-in과 유효한 manifest·lock이 있으면 세션 시작 시 Light가 현재 policy identity를 확인한다 | SessionStart contract test |
| AC-04 | 설명·읽기 전용 요청에는 추가 model call 없이 Light가 no-op 또는 짧은 context만 반환한다 | 호출·지연·출력 크기 측정 |
| AC-05 | material prompt가 들어오면 Light가 Hard로 상승하고 관련 규칙 ID만 선택한다 | prompt fixture와 selected-rule report |
| AC-06 | 새 API·DB·secret·dependency·IaC signal이 mutation 도구 입력에 나타나면 관련 Hard 카드가 생성된다 | PreToolUse fixture |
| AC-07 | 유효한 policy state에서 발견한 일반 rule finding은 파일럿 중 mutation을 자동 거부하지 않는다 | advisory fixture |
| AC-08 | manifest/lock 내부 무결성 실패·rule source 접근 불능 또는 확정된 material open decision 상태에서 mutation을 시도하면 그 호출만 거부하고 읽기·진단 호출은 허용한다 | deny/read-recovery paired fixture |
| AC-09 | command hook 실행 파일 누락·오류·timeout은 Claude Code 자체가 fail-open할 수 있음을 보고하고 hard enforcement 성공으로 세지 않는다 | fault-injection 결과와 debug log |
| AC-10 | 완료 시 실제 diff가 재분류되지만 Stop은 반복 continuation을 만들지 않는다 | one-turn Stop fixture와 session log |
| AC-11 | 동일 policy·prompt·diff fingerprint에서는 중복 Hard 카드와 같은 사람 질문을 다시 만들지 않는다 | cache/dedup contract test |
| AC-12 | 파일럿 결과에 지연, 출력 문자 수, Hard 상승 횟수, no-op 비율, 오탐, 누락, 중복 질문, hook 오류가 분리되어 기록된다 | pilot report |

## Light와 Hard의 계약

| 구분 | Light | Hard |
| --- | --- | --- |
| 목적 | 적용 자격·신호·신선도·mode 선택 | 선택 규칙의 적용·증거·미결정 평가 |
| 입력 | event metadata, manifest/lock identity, prompt/tool/diff summary, session cache | Light가 고른 signal, 관련 rule 원문, project evidence |
| AI 비용 | hook 자체의 별도 model call 없음 | hook 자체의 별도 model call 없음; 선택 카드가 현재 Claude turn에 주입됨 |
| 정책 읽기 | identity와 index/cache 중심 | 관련 rule 원문만 읽음 |
| 출력 budget | 정상 no-op은 무출력, context는 최대 4,000자 | 최대 8,000자와 선택 규칙 8개; 초과 시 요약과 human-review |
| 상승 조건 | 기본값 | material signal, policy state 이상, completion diff의 새 영향 |
| 하강 조건 | 새 checkpoint에서 material signal이 없고 fingerprint가 바뀜 | 같은 checkpoint 안에서는 임의 하강하지 않음 |

`quick/full/release`는 검사 범위이고, `Light/Hard`는 한 checkpoint의 평가 깊이이며, `advisory/block`은 집행 강도다. 세 축을 같은 mode로 합치지 않는다.

## 명시적 결정

| 결정 | 상태 | 근거와 경계 |
| --- | --- | --- |
| Light와 Hard만 구현 | accepted | Medium·Deep은 사용 데이터가 생길 때까지 만들지 않음 |
| runner가 mode 자동 선택 | accepted | 항상 Light에서 시작하고 정해진 material signal로만 Hard 상승 |
| Claude-first, core는 vendor-neutral | accepted | Claude adapter로 검증한 뒤 Codex adapter를 별도 결정 |
| local explicit activation | accepted | manifest·lock은 자격, `.claude/settings.local.json`은 파일럿 opt-in |
| advisory-first | accepted | rule finding은 경고; 확정된 unusable policy state/open decision 뒤 mutation만 deny |
| 읽기·진단 경로 보존 | accepted | 막힌 상태에서도 원인 확인과 복구는 가능해야 함 |
| Stop continuation 미사용 | accepted | 첫 파일럿은 완료 report만 제공하고 반복 작업을 강제하지 않음 |
| pinned lock만 governing | accepted | latest/candidate policy 자동 비교와 자동 업그레이드는 후속 범위 |
| 사람의 최종 승인 | accepted | AI의 자기평가가 승인·예외·정책 변경을 대신하지 않음 |
| 목표 릴리스 `0.7.0` | selected-for-plan | 기존 별도 `0.6.0` 후보와 변경 범위를 섞기 위한 기술적 routing이며 제품 의도 결정은 아님 |

## 암묵적으로 합의된 경계

- 매 hook에서 모든 spec-it 스킬을 강제하지 않는다. runner가 관련 작업을 선택하고 필요한 경우 기존 스킬로 인계한다.
- Light는 결정적·read-only여야 하며 별도 LLM 호출을 하지 않는다.
- Hard도 첫 파일럿에서는 별도 agent/model을 새로 호출하지 않고 현재 turn에 제한된 평가 카드를 제공한다.
- hook은 코드, 정책, manifest, lock, ADR, exception을 자동 수정하지 않는다.
- AI가 자신의 구현을 근거 없이 pass로 만들지 못하게 `observed`, `inferred`, `human-approved`, `unknown`을 구분한다.
- 세션 cache와 metric은 project source 밖에 두며 명시적 export 전에는 정본이 아니다.
- 최신 spec-it worktree가 있다는 이유만으로 프로젝트의 pinned lock을 바꾸지 않는다.
- 유효한 이전 pinned version은 policy-unavailable이 아니다. latest와의 버전 차이만으로 경고하거나 mutation을 막지 않는다.

## 아직 합의하지 않은 것과 비목표

- Medium·Deep mode의 의미와 도입 시점
- Codex adapter, 다른 AI adapter, 공통 plugin 배포
- 팀 전체가 사용하는 `.claude/settings.json` commit과 조직 managed settings
- CI·release 차단, command hook fail-close 보장, Agent SDK wrapper 도입
- Stop hook의 한 번짜리 자동 continuation 또는 반복 self-repair
- 기존 위반 자동 수정, exception 자동 생성, 정책 자동 evolve/converge
- 범용 latency·token의 영구 임계값; 첫 수치는 파일럿 환경의 초기 budget이며 측정 후 조정한다
- runner 구현 언어와 배포 형식. G1에서 대상 환경에 이미 있는 runtime, zero/low dependency, cross-platform fixture, 시작 비용을 비교해 architecture-owner가 기술 선택한다.
- 대상 애플리케이션의 제품 기능, DB migration, 배포 변경

## 비용과 복구

비용은 event별 wall time, 추가 context 문자 수, Hard 상승 수, 중복 질문과 사람 중단 횟수로 측정한다. token은 모델·tokenizer에 따라 달라지므로 원시 문자 수와 가능할 때 실제 usage를 함께 기록한다. Light의 no-op이 추가 model call을 만들지 않는 것이 첫 비용 gate다.

복구는 대상 프로젝트의 `.claude/settings.local.json`에서 pilot hook 항목을 제거하거나 비활성화하는 것이다. runner와 adapter는 project source를 수정하지 않으며, session cache와 report는 삭제 가능한 비정본이다. 활성화 전후의 설정과 실행 결과를 보존하되 secret, prompt 원문, source code 전문은 metric에 저장하지 않는다.

## 수렴 상태

material open decision은 없다. 실행 중 Claude Code 버전 차이, hook 입력 schema 차이, target repository의 기존 local setting 충돌이 발견되면 구현 결함이나 새 decision으로 분류하고, 추측으로 우회하지 않는다. `0.7.0` 릴리스 수렴에서 self manifest·lock·AGENTS를 함께 갱신했으며, 기존 프로젝트의 pin은 자동 변경하지 않는다.
