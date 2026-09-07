# Cost and infrastructure promotion

총비용은 클라우드 청구액뿐 아니라 개발·검토·배포·운영·복구에 쓰는 사람 시간과 AI 실행시간, 실패의 기대비용을 포함합니다. 프로젝트 단계와 위험 등급이 각 항목의 가중치를 정합니다.

인프라는 `local → single host/EC2 → non-production pilot → managed/serverless/container option → orchestration option`의 증거 기반 선택지로 봅니다. 이 순서는 승격 의무가 아닙니다. 측정 결과와 운영 역량이 현재 단계를 정당화하면 EC2에 머물 수 있습니다. EKS는 가능한 orchestration 선택지일 뿐 종착점이 아닙니다.

OpenSearch 같은 관리형 서비스도 처음부터 전제하지 않습니다. 가벼운 설치 또는 파일럿으로 처리량, 장애 복구, 운영시간, 저장량, 요청당 비용을 측정한 뒤 승격합니다. 판단은 별도 로그 서비스가 아니라 Git ADR과 manifest 이력에 기록합니다.

구체적인 인프라 프로필은 활성화 신호, 필수 결정, 장애 시나리오, 비용 driver, 측정 항목, guardrail, 증거 단계와 재검토 trigger를 같은 구조로 제공합니다. 공통 프로필은 무엇을 볼지 정하고, 프로젝트는 위험 등급·workload·SLO·예산에 맞는 실제 threshold를 승인합니다.

증거는 필요에 따라 `구현 전 추정 → 개발·합성 benchmark → 비운영 실측 → 위험 기반 사전 운영 검증 → 운영 관측`으로 성숙합니다. 모든 작업이 다섯 단계를 전부 실행하는 것은 아니지만, 아직 없는 증거를 통과로 표시하지 않습니다.

구현 중 새 dependency, IaC, runtime setting, 외부 client 또는 저장 payload가 발견되어도 파일 저장마다 전체 검사를 돌리지 않습니다. 작업 시작, material signal 발견, 완료 전 diff, CI changed-file scan에서만 관련 프로필을 재판정합니다. 기존 결정과 guardrail이 포함하면 계속하고, 미결정·충돌·hard constraint·예산 초과일 때만 사람에게 묻습니다.

정본 규칙: [COST-001](../rules/cost/COST-001.md), [COST-002](../rules/cost/COST-002.md), [DEP-001](../rules/deployment/DEP-001.md), [DEP-002](../rules/deployment/DEP-002.md), [INFRA-001](../rules/infrastructure/INFRA-001.md), [INFRA-002](../rules/infrastructure/INFRA-002.md).
