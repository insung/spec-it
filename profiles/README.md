# Profiles

프로필은 규칙 문장을 복사하지 않고 규칙 ID와 parameter default를 합성합니다. 한 프로젝트는 risk 축에서 정확히 하나를 선택하고, 나머지 축은 실제 필요만 선택합니다. 충돌은 사람이 해결합니다.

## Initial reference profiles

- Risk: [low](risk/low.yaml), [standard](risk/standard.yaml), [high](risk/high.yaml)
- Project kind: [backend-service](project-kind/backend-service.yaml), [serverless-function](project-kind/serverless-function.yaml)
- Language draft 0.2.0: [python](language/python.yaml)
- Runtime draft 0.2.0: [aws-lambda](runtime/aws-lambda.yaml)
- Deployment: [sam](deployment/sam.yaml)
- Capability fixtures: [rds](capability/rds.yaml), [dynamodb](capability/dynamodb.yaml), [otel](capability/otel.yaml)
- Capability draft 0.2.0: [redis](capability/redis.yaml)
- Capability drafts 0.2.0: [http-api](capability/http-api.yaml), [shared-domain-library](capability/shared-domain-library.yaml)

## 미발행 0.2.0 프로필 초안

`backend-service`, `serverless-function`, `python`, `aws-lambda`, `rds`, `redis`는 새 규칙이나 구조를 연결한 `version: 0.2.0`, `status: draft` 후보입니다. `http-api`와 `shared-domain-library`는 새로 추가된 선택형 capability 초안입니다. 기존 0.1.0을 대신 해석하는 파일이 아닙니다. 0.1.0에 고정된 프로젝트는 그 기준선의 Git revision에서 프로필을 읽으며 이 작업 트리의 변경본을 조용히 사용하지 않습니다. 배포·재수렴·lock 갱신은 별도 승인 후 수행합니다.

backend-service와 serverless-function은 [ARCH-005](../rules/architecture/ARCH-005.md), [MSG-001](../rules/messages/MSG-001.md), [MSG-002](../rules/messages/MSG-002.md)를 연결하고 rds는 [DATA-007](../rules/data/DATA-007.md)과 ARCH-005를 연결합니다. 실제 적용 여부는 각 규칙의 `condition`으로 판정합니다. 사용자 안내 없는 배치나 프로시저 없는 RDS 프로젝트에 불필요한 구현을 추가하지 않고 `not-applicable` 근거를 남깁니다. 상세 프론트엔드 프로필은 여전히 보류 상태입니다.

공통 code 의미 규칙은 backend·serverless와 Python profile에 연결됩니다. Python은 Ruff 기반 lint contract를 사용하되 다른 언어가 추가되면 그 생태계의 도구를 별도로 선택합니다. `aws-lambda`와 `redis`는 첫 `infrastructure` trait reference로서 activation signal부터 revisit trigger까지 같은 평가 구조를 제공합니다. 실제 threshold는 공통 파일이 아니라 프로젝트 manifest와 ADR에서 정합니다.

HTTP endpoint가 있다는 이유만으로 backend-service 전체에 API 규칙을 넣지 않습니다. 프로젝트는 `capability/http-api`를 명시적으로 선택합니다. protobuf나 WebSocket은 실제 프로젝트가 고유 규칙과 검증기를 요구할 때 별도 capability를 추가하며, 그전에는 [공통 API 계약 원칙](../docs/api-design-and-lifecycle.md)을 사용해 프로젝트 계약으로 구체화합니다.
