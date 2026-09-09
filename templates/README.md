# Templates

템플릿은 시작용 사본이며 규칙 정본이 아닙니다. 규칙 ID와 schema를 연결하되 새 의무를 만들지 않습니다.

- `project/`: AGENTS, project, manifest, lock, ADR, change, exception, environment
- `testing/`: integration과 load test 계획
- `benchmarks/`: 인프라 유형별 측정 항목

## 0.2.0 templates

- [사용자 메시지 계약](project/user-message-contract.yaml): [schema](../schemas/user-message-contract.schema.json), [설명과 검증 방법](../docs/user-messages-and-errors.md), [가상 fixture](../examples/user-message-contract/README.md).
- [통합 테스트 계획](testing/integration-test-plan.md): 트랜잭션·프로시저·공개 결과·메시지의 적용 가능한 검사 항목.
- [API 계약 결정](project/api-contract-decision.md): protocol, resource·command 분류, DTO mapping, audience, lifecycle과 검증 선택.
- [공유 코어 영향 평가](project/core-library-impact.yaml): release가 한 consumer의 고정 버전·배포·검증에 미치는 영향과 진행 상태.
- [프로젝트 manifest](project/manifest.yaml): 실행 source의 lint contract와 프로젝트 소유의 인프라 재검토 threshold 시작점.
- [ADR](project/decision.md): SLO·장애 시나리오·비용·증거 단계·guardrail·재검토 trigger를 함께 기록.
- [Lambda benchmark](benchmarks/lambda.md), [Redis benchmark](benchmarks/redis.md): 기술별 구현 질문과 비용·운영 측정 항목.

`schema_version`은 파일 형식, `contract_version`은 프로젝트의 결과 계약, 정책 버전은 규칙 묶음의 버전입니다. 숫자가 같을 필요는 없습니다. 새 템플릿은 승인된 실제 업무 명세가 아니며 placeholder와 `not-implemented` 사례를 실제 프로젝트에서 구체화합니다.

## 0.4.0 templates

- [프로젝트 lock](project/lock.yaml): released policy source의 `policy_digest`와 선택적 immutable `revision`을 기록하는 schema 0.2.0 시작점.
- [사용자 메시지 계약](project/user-message-contract.yaml): HTTP stream의 before/after-open 오류 mapping을 표현할 수 있는 schema 0.2.0 시작점.
- [프로젝트 manifest](project/manifest.yaml): 배포·복구·비용 판단의 승인자를 구분할 때 사용할 선택적 `operations-owner` 시작점.

템플릿의 zero digest와 placeholder revision은 수렴 완료 값이 아닙니다. 실제 공개 release artifact와 현재 manifest bytes에서 다시 계산해야 합니다.
