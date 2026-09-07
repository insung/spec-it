# Rule and enforcement lifecycle

각 규칙은 강제 목표와 현재 구현 상태를 분리합니다.

```yaml
enforcement:
  mode: ci
  implementation: planned
```

`mode`는 `manual`, `validator`, `ci`, `runtime` 중 하나이고, `implementation`은 `planned`, `advisory`, `implemented` 중 하나입니다. Phase 0 규칙 다수는 목표가 `validator` 또는 `ci`여도 구현 상태가 `planned`입니다.

검사 결과는 `pass`, `warn`, `fail`, `not-applicable`, `human-review`만 사용합니다. 누락된 증거나 미구현 검사는 `pass`가 아닙니다. `spec-it:check`는 읽기 전용이며 사람용 요약과 JSON 보고서를 함께 만들도록 설계됩니다.

보고서는 `.spec-it/reports/YYYY-MM-DDTHH-mm-ssZ_<commit>_<mode>.json`에 생성하고 디렉터리를 Git에서 제외합니다. Phase 0에서는 실제 report generator가 없습니다.

코드 규칙은 가능한 부분을 formatter·linter·static analyzer·type checker로 검사하되 의미 판정과 도구가 다루지 못하는 언어는 review evidence로 보완합니다. 구현 중 프로필 재판정은 숨은 per-save hook이나 watcher가 아니라 작업 시작, material signal, 완료 전 diff, CI changed-file scan에서 실행합니다.

Brownfield에서는 기존 위반과 이번 변경이 만든 위반을 구분합니다. 기존 문제는 위치·영향·안전한 수정 경계를 계속 보고하지만, 정책 채택만으로 대규모 이름 변경이나 구조 변경을 자동 수행하지 않습니다.

정본 규칙: [RULE-001](../rules/rule-system/RULE-001.md), [RULE-002](../rules/rule-system/RULE-002.md), [RULE-003](../rules/rule-system/RULE-003.md), [TOOL-001](../rules/tooling/TOOL-001.md), [TOOL-003](../rules/tooling/TOOL-003.md), [TOOL-005](../rules/tooling/TOOL-005.md), [INFRA-002](../rules/infrastructure/INFRA-002.md).
