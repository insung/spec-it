# Profile composition

프로젝트별 거대한 통합 프로필을 만들지 않고 다음 축을 평평하게 합성합니다.

```text
profiles/
├── risk/
├── project-kind/
├── language/
├── runtime/
├── deployment/
└── capability/
```

예를 들어 Python Lambda는 `risk/standard + project-kind/serverless-function + language/python + runtime/aws-lambda + deployment/sam`으로 표현합니다. EC2에서 Docker Compose로 배포하는 서비스는 필요가 확인될 때 `runtime/aws-ec2 + deployment/docker-compose`를 독립적으로 선택합니다. RDS, Redis, OpenTelemetry 같은 능력은 필요할 때 capability 축에서 추가합니다.

HTTP API와 공유 domain library도 각각 `capability/http-api`, `capability/shared-domain-library`로 선택합니다. backend라는 이유만으로 HTTP 규칙을 적용하지 않습니다. protobuf·WebSocket profile은 실제 project에서 고유 규칙이나 validator가 필요해질 때 추가합니다.

새 프로필은 실제 프로젝트의 필요, 고유 규칙, 반복되는 독립 축, 별도 템플릿·validator 중 적어도 하나가 있을 때 추가합니다. 프로필의 필수 규칙이 충돌하면 조용한 우선순위를 만들지 않고 `spec-it:clarify`가 사람 결정을 요청합니다.

프로필은 규칙 본문을 복사하지 않고 규칙 ID, parameter default, evidence freshness, conflict declaration만 보유합니다. 형식은 [profile schema](../schemas/profile.schema.json)가 정합니다.

## Infrastructure trait

runtime·deployment·capability profile이 구체적인 인프라 판단을 제공하면 `traits: [infrastructure]`를 선언하고 다음 구조를 모두 제공합니다.

- activation signals
- required decisions
- failure scenarios
- cost drivers
- measurements
- guardrails
- evidence stages
- revisit triggers

공통 프로필은 관찰할 항목을 정하고 숫자를 보편값으로 고정하지 않습니다. 프로젝트 manifest와 ADR이 risk, workload, SLO와 예산에 맞는 threshold를 승인합니다. `runtime/aws-lambda`, `runtime/aws-ec2`, `deployment/docker-compose`, `capability/redis`가 같은 평가 구조를 사용합니다. runtime profile은 실행 host와 failure domain을, deployment profile은 artifact와 교체 절차를 소유하므로 도구 이름만으로 서로를 자동 선택하지 않습니다.

정본 규칙: [INFRA-001](../rules/infrastructure/INFRA-001.md), [INFRA-002](../rules/infrastructure/INFRA-002.md).
