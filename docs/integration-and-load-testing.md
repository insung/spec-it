# Integration and load testing

외부 경계가 바뀌면 선택된 프로젝트 프로필이 지정한 통합 테스트가 작동합니다. 순수 도메인 변경은 근거와 함께 면제될 수 있습니다. Lambda도 모든 것을 실제 AWS에서 시험할 필요는 없습니다. fixture와 fake는 unit, SAM/container는 component 또는 contract, 임시 AWS stack은 true integration으로 구분합니다.

환경 이름만으로 신뢰도를 판정하지 않습니다. [TST-006](../rules/testing/TST-006.md)에 따라 무엇을 실제로 연결했고 어떤 데이터와 side effect를 격리했는지 기록합니다.

| 환경 | 기본 목적 | 기본 데이터와 제한 |
| --- | --- | --- |
| local·CI isolated | 실제 engine contract, transaction, migration, failure와 recovery | 결정적 synthetic fixture, 매 실행 격리·정리 |
| stage | 같은 build artifact의 cloud IAM·network·managed service·배포 연결 | synthetic 또는 승인된 비식별 subset, production sink 차단 |
| production | 배포 후 bounded smoke와 핵심 관측 | synthetic actor, destructive·broad load 금지, 즉시 abort·cleanup |

개발 공유 DB에 우연히 남은 데이터를 fixture로 쓰지 않습니다. stage의 작은 instance와 축소 data는 배포 연결 증거이지 production capacity 증거가 아닙니다.

## Production-derived data

합성 데이터로 재현할 수 없는 경우에만 intent·security·data owner가 필요성과 비용을 승인합니다. 원본을 일반 stage에 먼저 복원한 뒤 나중에 masking하지 않습니다.

```text
necessity approval
→ quarantined restore
→ egress/scheduler/email/payment/webhook sinks blocked
→ minimization or de-identification
→ safety gate
→ bounded test
→ TTL destruction and sanitized evidence
```

복원된 원본이 존재하는 동안은 production 수준으로 보호합니다. credential·token을 무효화하고 production endpoint와 account에 연결되지 않았음을 검사합니다. snapshot 시점이 다른 DB·object·stream을 함께 쓰면 일관성 한계를 기록합니다. RDS snapshot은 새 instance로 복원되고 storage를 줄여 복원할 수 없으므로 compute뿐 아니라 storage·보존 시간 비용을 산정합니다.

부하 테스트는 위험 등급과 변경 trigger로 실행합니다. 공통 결과에는 latency 분포, throughput, error·timeout·throttle, saturation, 요청·이벤트당 비용, 준비·실행·분석·복구에 든 운영시간이 포함됩니다.

측정 템플릿은 인프라 유형별로 달라집니다. WAS는 CPU·memory·connection·queue, Lambda는 duration·concurrency·cold start·throttle, Redis는 memory·eviction·hit ratio·latency, RDS는 connection·lock·IOPS·query latency, DynamoDB는 consumed capacity·throttle, OpenSearch는 heap·shard·index·query latency, stream은 lag·throughput·retention·retry를 중심으로 봅니다.

정본 규칙: [TST-003](../rules/testing/TST-003.md), [TST-004](../rules/testing/TST-004.md), [TST-005](../rules/testing/TST-005.md), [TST-006](../rules/testing/TST-006.md).
