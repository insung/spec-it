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

## 0.2.0 examples

[user-message-contract](user-message-contract/README.md)는 가상 내보내기 한도 오류·번역·비노출·모르는 code/locale의 작은 계약 예입니다. schema 검사와 실제 동작 검증을 구분하며 실행 테스트는 없습니다. 기존 0.1.0 manifest fixture는 해당 기준선용으로 유지하며 0.2.0으로 자동 재해석하지 않습니다.
