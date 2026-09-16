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

## 미발행 후보 — 선택적 의도·검증 기록

- [변경 명세](project/change-spec.md): 최소 의도 되읽기·원본·경로·검증 연결. 전 항목을 사전 설문으로 요구하지 않습니다.
- [영향 기록](project/change-impact.md): 확인 시각, revision/dirty 상태, 미변경 소비자와 재검토 조건. 읽기 전용 조사 결과의 저장은 호출자 권한입니다.
- [수용 사례](testing/acceptance-case.md), [실행 기록](testing/verification-run.md): Case revision과 Run ID, 외부 QA repo·증거·실패/수정/재검증 연결.

새 schema나 공통 필수 폴더가 아닙니다. 기존 문서/QA 도구의 동등한 항목으로 대체할 수 있고 구현 저장소에 QA 코드가 없어도 됩니다. [설명](../docs/intent-and-verification.md), [분리 저장소 예제](../examples/intent-verification/README.md)를 참고합니다.
