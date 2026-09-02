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

예를 들어 Python Lambda는 `risk/standard + project-kind/serverless-function + language/python + runtime/aws-lambda + deployment/sam`으로 표현합니다. RDS, Redis, OpenTelemetry 같은 능력은 필요할 때 capability 축에서 추가합니다.

새 프로필은 실제 프로젝트의 필요, 고유 규칙, 반복되는 독립 축, 별도 템플릿·validator 중 적어도 하나가 있을 때 추가합니다. 프로필의 필수 규칙이 충돌하면 조용한 우선순위를 만들지 않고 `spec-it:clarify`가 사람 결정을 요청합니다.

프로필은 규칙 본문을 복사하지 않고 규칙 ID, parameter default, evidence freshness, conflict declaration만 보유합니다. 형식은 [profile schema](../schemas/profile.schema.json)가 정합니다.
