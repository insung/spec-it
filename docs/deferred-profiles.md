# Deferred profiles

다음 영역은 공통 원칙의 적용 대상이지만 Phase 0 상세 프로필은 만들지 않습니다.

| 영역 | 재검토 trigger | 예상 축 |
| --- | --- | --- |
| 제품 AI | 운영 프롬프트·model call·agent memory가 제품 동작에 포함될 때 | prompt version, eval fixture, safety, model cost, AI observability |
| 개발 agent harness | 실제 프로젝트 pilot에서 반복 누락 또는 불안정한 작업 흐름이 확인될 때 | context assembly, tool permission, memory, eval, trace |
| frontend | 실제 web/mobile UI 프로젝트가 정책을 채택할 때 | accessibility, browser support, performance budget, state model, visual regression, user journey |
| embedded | 실제 board·firmware 프로젝트가 정책을 채택할 때 | HAL, timing, memory, power, toolchain, board revision, SIL/HIL, safety level |

상세 규칙은 실제 사용 사례 없이 미리 만들지 않습니다.

frontend 전용 profile이 보류되어도 [공통 코드 의미 규칙](code-conventions.md)은 frontend의 project-owned identifier, component, hook, event handler, state와 collection에 적용할 수 있습니다. 실제 TypeScript·JavaScript·Kotlin 등 language profile이 추가될 때 해당 생태계의 casing, formatter, linter와 type checker를 연결합니다.
