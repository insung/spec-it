# Examples and fixtures

예제는 규칙 정본이 아닙니다. Phase 0 합성과 향후 validator의 기대 판정을 보여줍니다.

| Fixture | Expected semantic result |
| --- | --- |
| `python-backend` | pass after implemented checks; planned checks remain human-review |
| `python-lambda-sam` | same, with fixed Lambda layout rules |
| `multi-lambda-monorepo` | root plus difference-only unit manifests |
| `rds-redis-service` | RDS truth and Redis derived-state rules selected |
| `expired-exception` | fail because the exception is expired |
| `profile-conflict` | human-review because two risk profiles are selected |
| `check-report` | valid report that keeps a planned check at human-review |
| `sse-message-contract` | valid HTTP stream contract with distinct before-open and after-open error mappings |
| `claude-hook-pilot` | local opt-in settings example for the 0.7.0 active policy loop |

## 0.2.0 examples

[user-message-contract](user-message-contract/README.md)는 가상 내보내기 한도 오류·번역·비노출·모르는 code/locale의 작은 계약 예입니다. schema 검사와 실제 동작 검증을 구분하며 실행 테스트는 없습니다. 기존 0.1.0 manifest fixture는 해당 기준선용으로 유지하며 0.2.0으로 자동 재해석하지 않습니다.

## 0.4.0 examples

[sse-message-contract](sse-message-contract/README.md)는 generic SSE 응답에서 stream open 전 HTTP 오류와 open 후 typed error event를 구분합니다. schema 구조 예제일 뿐 실제 event framing·재연결·UI 동작을 검증하지 않습니다.

## 절차와 실행 예제

[intent-verification](intent-verification/README.md)은 기획·디자인·구현·별도 QA의 Case/Run revision과 영향 재검토를 연결하는 합성 예제입니다. 실제 QA 실행 결과가 아니며 특정 도구나 QA 폴더를 강제하지 않습니다.

[claude-hook-pilot](claude-hook-pilot/settings.local.json)은 Claude-first runner를 프로젝트 로컬에서 켜는 설정 예제입니다. `/absolute/path/to/spec-it`을 실제 checkout 절대 경로로 바꿔야 하며 팀 shared setting이나 hard enforcement를 뜻하지 않습니다. command와 args를 분리한 exec form으로 경로가 shell에서 재해석되지 않게 합니다.
