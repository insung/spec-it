# Agent work cycle

spec-it은 AI가 규칙을 기억했다고 가정하지 않습니다. 프로젝트의 `AGENTS.md`, 승인된 manifest와 결정적 lock이 매 작업의 진입점이고, lock에 연결된 규칙만 실제 적용 대상으로 판정합니다.

## 작업 전

1. `AGENTS.md`, project intent, manifest, lock, 활성 change spec과 관련 ADR을 읽습니다.
2. 요청과 예상 변경 표면을 분류하고 적용 규칙과 프로필을 확인합니다.
3. 저장소에서 알 수 있는 언어·runtime·dependency·IaC·외부 경계는 조사합니다.
4. 관측 가능한 동작, 보안, 데이터, 비용, 가용성에 남은 인간 판단만 `spec-it:clarify`로 보냅니다.

manifest와 lock이 없는 brownfield 저장소는 채택 전이므로 `shadow assessment`만 수행합니다. 후보 프로필과 예상 충돌을 제시할 수 있지만 준수·위반으로 단정하지 않습니다.

## 구현 중

모든 파일 저장마다 정책 전체를 다시 읽지 않습니다. 다음 material signal을 새로 추가하거나 발견했을 때만 관련 프로필을 재판정합니다.

- dependency 또는 import
- IaC·배포 topology·runtime setting
- environment configuration 또는 secret access
- 외부 client·network boundary·event source
- database, cache, stream 또는 저장 payload
- 공개 API·message·schema·권한·오류 계약

기존 승인 결정과 guardrail이 signal을 포함하면 작업을 계속하고 완료 report에 근거를 남깁니다. 미결정, 규칙 충돌, hard constraint, 비용·가용성 budget 초과가 생기면 구현을 멈추고 선택지·추천·영향·예상 diff·rollback·증거를 사람에게 제시합니다.

## 완료 전과 CI

완료 전에는 실제 diff로 적용 규칙을 다시 계산합니다. 새 코드의 규칙 위반, 누락된 테스트·benchmark·결정·예외를 `pass`, `warn`, `fail`, `not-applicable`, `human-review` 중 하나로 보고합니다. CI는 changed-file scan과 저비용 정적 검사를 기본으로 하고, 부하·복구 같은 비싼 증거는 profile trigger가 있을 때만 요구합니다.

Phase 0의 스킬은 이 순서를 수행하는 instruction입니다. 숨은 hook, 상시 watcher, 실행 validator나 CI 차단 기능은 아직 제공하지 않습니다.

정본 규칙: [INFRA-001](../rules/infrastructure/INFRA-001.md), [INFRA-002](../rules/infrastructure/INFRA-002.md), [HITL-001](../rules/hitl/HITL-001.md), [HITL-002](../rules/hitl/HITL-002.md), [TOOL-001](../rules/tooling/TOOL-001.md).
