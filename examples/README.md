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
