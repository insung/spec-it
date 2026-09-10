# Profiles

프로필은 규칙 문장을 복사하지 않고 규칙 ID와 parameter default를 합성합니다. 한 프로젝트는 risk 축에서 정확히 하나를 선택하고, 나머지 축은 실제 필요만 선택합니다. 충돌은 사람이 해결합니다.

## Initial reference profiles

- Risk: [low](risk/low.yaml), [standard](risk/standard.yaml), [high](risk/high.yaml)
- Project kind: [backend-service](project-kind/backend-service.yaml), [serverless-function](project-kind/serverless-function.yaml)
- Language: [python](language/python.yaml)
- Runtime: [aws-lambda](runtime/aws-lambda.yaml), [aws-ec2](runtime/aws-ec2.yaml)
- Deployment: [sam](deployment/sam.yaml), [docker-compose](deployment/docker-compose.yaml)
- Capability: [rds](capability/rds.yaml), [dynamodb](capability/dynamodb.yaml), [redis](capability/redis.yaml), [otel](capability/otel.yaml), [http-api](capability/http-api.yaml), [shared-domain-library](capability/shared-domain-library.yaml), [db-migration](capability/db-migration.yaml), [data-pipeline](capability/data-pipeline.yaml)

## 0.2.0 profiles

`backend-service`, `serverless-function`, `python`, `aws-lambda`, `rds`, `redis`, `http-api`, `shared-domain-library`는 `version: 0.2.0`, `status: active`입니다. 0.1.0에 고정된 프로젝트는 그 기준선의 Git revision에서 프로필을 읽으며 0.2.0을 조용히 사용하지 않습니다. 프로젝트별 재수렴과 lock 갱신은 별도 승인 후 수행합니다.

backend-service와 serverless-function은 [ARCH-005](../rules/architecture/ARCH-005.md), [MSG-001](../rules/messages/MSG-001.md), [MSG-002](../rules/messages/MSG-002.md)를 연결하고 rds는 [DATA-007](../rules/data/DATA-007.md)과 ARCH-005를 연결합니다. 실제 적용 여부는 각 규칙의 `condition`으로 판정합니다. 사용자 안내 없는 배치나 프로시저 없는 RDS 프로젝트에 불필요한 구현을 추가하지 않고 `not-applicable` 근거를 남깁니다. 상세 프론트엔드 프로필은 여전히 보류 상태입니다.

## 0.3.0 profiles

`capability/db-migration`은 DB 변경을 작성·요청·실행하는 프로젝트가 선택하고, `capability/data-pipeline`은 정기 또는 외부 trigger로 consumer용 데이터를 생산하는 프로젝트가 선택합니다. RDS를 조회한다는 이유만으로 둘을 자동 선택하지 않습니다. 기존 0.2.0 프로젝트는 0.3.0 shadow assessment와 별도 승인 없이 이 profile을 사용하지 않습니다.

공통 code 의미 규칙은 backend·serverless와 Python profile에 연결됩니다. Python은 Ruff 기반 lint contract를 사용하되 다른 언어가 추가되면 그 생태계의 도구를 별도로 선택합니다. `aws-lambda`와 `redis`는 첫 `infrastructure` trait reference로서 activation signal부터 revisit trigger까지 같은 평가 구조를 제공합니다. 실제 threshold는 공통 파일이 아니라 프로젝트 manifest와 ADR에서 정합니다.

HTTP endpoint가 있다는 이유만으로 backend-service 전체에 API 규칙을 넣지 않습니다. 프로젝트는 `capability/http-api`를 명시적으로 선택합니다. protobuf나 WebSocket은 실제 프로젝트가 고유 규칙과 검증기를 요구할 때 별도 capability를 추가하며, 그전에는 [공통 API 계약 원칙](../docs/api-design-and-lifecycle.md)을 사용해 프로젝트 계약으로 구체화합니다.

## 0.4.0 profiles

`runtime/aws-ec2`는 프로젝트가 관리하는 EC2 host의 topology, capacity acquisition, interruptible capacity, process supervision, patch와 recovery 책임을 평가합니다. `deployment/docker-compose`는 Compose 파일과 배포 조정, immutable image, healthcheck, drain, volume, rollback 계약을 평가합니다. 둘은 독립 축입니다. Compose를 쓴다는 사실만으로 EC2를 선택하지 않으며, 한 host의 Compose 구성만으로 고가용성을 입증하지 않습니다.

`capability/http-api`는 HTTP streaming의 wire contract와 스트림이 열리기 전·후의 오류 mapping을 조건부 결정으로 추가합니다. 기존 비스트리밍 HTTP 프로젝트는 해당 결정을 자동 적용하지 않습니다. `capability/rds`는 새로 소유하는 DB identifier category별 convention과 외부 소유 identifier 보존을 선언하며, 모든 engine에 하나의 casing을 강제하지 않습니다. 또한 topology, capacity, connection, failover, backup·PITR, restore, maintenance와 운영 소유권을 공통 infrastructure evaluation 구조로 평가합니다.
