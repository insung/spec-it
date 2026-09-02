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

정본 규칙: [RULE-001](../rules/rule-system/RULE-001.md), [RULE-002](../rules/rule-system/RULE-002.md), [RULE-003](../rules/rule-system/RULE-003.md), [TOOL-001](../rules/tooling/TOOL-001.md), [TOOL-003](../rules/tooling/TOOL-003.md).
