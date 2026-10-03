# Agent work cycle

spec-it은 AI가 규칙을 기억했다고 가정하지 않습니다. 프로젝트의 `AGENTS.md`, 승인된 manifest와 결정적 lock이 매 작업의 진입점이고, lock에 연결된 규칙만 실제 적용 대상으로 판정합니다.

프로젝트별 설계·인프라 질문도 기본 진입점인 `AGENTS.md`와 고정된 정책 안내에서 시작한다. 별도 스킬 설치는 필수 조건이 아니며, 미발행 후보인 [함께 판단하고 구현하기](pair-work-cycle.md)의 짧은 대화 절차를 비교할 수 있다. AI는 확인한 프로젝트 사실과 해당 lock 규칙을 바탕으로 잠정 판단·미확인·다음 작은 검증을 제시한다. 일반 개념 질문에는 바로 답하고, 질문만으로 변경 명세나 승인 결정을 만들지 않는다.

## 작업 전

1. `AGENTS.md`, project intent, manifest, lock, 활성 change spec과 관련 ADR을 읽습니다.
2. 요청과 예상 변경 표면을 분류하고 적용 규칙과 프로필을 확인합니다.
3. 저장소에서 알 수 있는 언어·runtime·dependency·IaC·외부 경계는 조사합니다.
4. 관측 가능한 동작, 보안, 데이터, 비용, 가용성에 남은 인간 판단만 `spec-it:clarify`로 보냅니다.

manifest와 lock이 없는 brownfield 저장소는 채택 전이므로 `shadow assessment`만 수행합니다. 후보 프로필과 예상 충돌을 제시할 수 있지만 준수·위반으로 단정하지 않습니다.

미발행 후보의 [impact](../skills/spec-it-impact/SKILL.md)는 위 조사에서 실제 경로와 연결된 미변경 소비자, 출처 revision/dirty 상태·확인 시각·미접근 범위·재검토 조건을 반환합니다. 호출자가 승인된 범위에서 기존 변경 기록에 저장할 수 있습니다. material 의도는 정상 예시·반례·유지 조건으로 되읽고 필요한 차이만 질문합니다. 관계 파일, QA 폴더, 전체 설문은 필수가 아닙니다.

## 구현 중

모든 파일 저장마다 정책 전체를 다시 읽지 않습니다. 다음 material signal을 새로 추가하거나 발견했을 때만 관련 프로필을 재판정합니다.

- dependency 또는 import
- IaC·배포 topology·runtime setting
- environment configuration 또는 secret access
- 외부 client·network boundary·event source
- database, cache, stream 또는 저장 payload
- 공개 API·message·schema·권한·오류 계약
- 승인된 기획/디자인의 의미·revision, 적용 유형·전략·미변경 소비자 관계

마지막 항목은 후보의 영향 조사 보완입니다. 매 변경마다 프로필을 추가한다는 뜻은 아닙니다. 새 세션/재개 시 이전 기록과 현재 commit/dirty/원본 상태를 대조하고 달라진 결론만 재검토합니다. 미접근은 변경 없음이 아니며 watcher 없이 외부 변경을 자동 발견한다고 하지 않습니다. 뒤늦게 시작하면 `late-entry`로 기존 작업·빠진 사전 증거·사후 검증을 구분합니다.

기존 승인 결정과 guardrail이 signal을 포함하면 작업을 계속하고 완료 report에 근거를 남깁니다. 미결정, 규칙 충돌, hard constraint, 비용·가용성 budget 초과가 생기면 구현을 멈추고 선택지·추천·영향·예상 diff·rollback·증거를 사람에게 제시합니다.

## 완료 전과 CI

완료 전에는 실제 diff로 적용 규칙을 다시 계산합니다. 새 코드의 규칙 위반, 누락된 테스트·benchmark·결정·예외를 `pass`, `warn`, `fail`, `not-applicable`, `human-review` 중 하나로 보고합니다. CI는 changed-file scan과 저비용 정적 검사를 기본으로 하고, 부하·복구 같은 비싼 증거는 profile trigger가 있을 때만 요구합니다.

후보의 완료 검토는 원문→해석→시나리오→유형/경로→관찰 증거를 양방향으로 확인합니다. 테스트 내부의 일관성이나 반복 횟수는 원문 누락이 없다는 증명이 아닙니다. 과거 실행은 유지하며 정정된 기획/환경의 재검증 필요를 별도로 표시합니다. 구체적인 선택 절차와 분산 도구 경계는 [의도와 검증](intent-and-verification.md)을 참고합니다. 이는 고정 규칙에 없는 의무를 만들어 판정하는 근거가 아닙니다.

`0.7.0`의 스킬은 이 순서를 수행하는 instruction입니다. active policy loop는 명시적으로 local opt-in한 Claude Code 프로젝트에서 이 checkpoint를 자동 호출합니다. hook이 없는 프로젝트에는 영향을 주지 않으며, 상시 watcher·범용 validator·CI 차단 기능으로 간주하지 않습니다.

정본 규칙: [INFRA-001](../rules/infrastructure/INFRA-001.md), [INFRA-002](../rules/infrastructure/INFRA-002.md), [HITL-001](../rules/hitl/HITL-001.md), [HITL-002](../rules/hitl/HITL-002.md), [TOOL-001](../rules/tooling/TOOL-001.md).
