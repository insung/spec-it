# Profiles

프로필은 규칙 문장을 복사하지 않고 규칙 ID와 parameter default를 합성합니다. 한 프로젝트는 risk 축에서 정확히 하나를 선택하고, 나머지 축은 실제 필요만 선택합니다. 충돌은 사람이 해결합니다.

## Initial reference profiles

- Risk: [low](risk/low.yaml), [standard](risk/standard.yaml), [high](risk/high.yaml)
- Project kind: [backend-service](project-kind/backend-service.yaml), [serverless-function](project-kind/serverless-function.yaml)
- Language: [python](language/python.yaml)
- Runtime: [aws-lambda](runtime/aws-lambda.yaml)
- Deployment: [sam](deployment/sam.yaml)
- Capability fixtures: [rds](capability/rds.yaml), [dynamodb](capability/dynamodb.yaml), [redis](capability/redis.yaml), [otel](capability/otel.yaml)
