# Integration and load testing

외부 경계가 바뀌면 선택된 프로젝트 프로필이 지정한 통합 테스트가 작동합니다. 순수 도메인 변경은 근거와 함께 면제될 수 있습니다. Lambda도 모든 것을 실제 AWS에서 시험할 필요는 없습니다. fixture와 fake는 unit, SAM/container는 component 또는 contract, 임시 AWS stack은 true integration으로 구분합니다.

부하 테스트는 위험 등급과 변경 trigger로 실행합니다. 공통 결과에는 latency 분포, throughput, error·timeout·throttle, saturation, 요청·이벤트당 비용, 준비·실행·분석·복구에 든 운영시간이 포함됩니다.

측정 템플릿은 인프라 유형별로 달라집니다. WAS는 CPU·memory·connection·queue, Lambda는 duration·concurrency·cold start·throttle, Redis는 memory·eviction·hit ratio·latency, RDS는 connection·lock·IOPS·query latency, DynamoDB는 consumed capacity·throttle, OpenSearch는 heap·shard·index·query latency, stream은 lag·throughput·retention·retry를 중심으로 봅니다.

정본 규칙: [TST-003](../rules/testing/TST-003.md), [TST-004](../rules/testing/TST-004.md), [TST-005](../rules/testing/TST-005.md).
