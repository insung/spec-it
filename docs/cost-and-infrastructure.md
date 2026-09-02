# Cost and infrastructure promotion

총비용은 클라우드 청구액뿐 아니라 개발·검토·배포·운영·복구에 쓰는 사람 시간과 AI 실행시간, 실패의 기대비용을 포함합니다. 프로젝트 단계와 위험 등급이 각 항목의 가중치를 정합니다.

인프라는 `local → single host/EC2 → non-production pilot → managed/serverless/container option → orchestration option`의 증거 기반 선택지로 봅니다. 이 순서는 승격 의무가 아닙니다. 측정 결과와 운영 역량이 현재 단계를 정당화하면 EC2에 머물 수 있습니다. EKS는 가능한 orchestration 선택지일 뿐 종착점이 아닙니다.

OpenSearch 같은 관리형 서비스도 처음부터 전제하지 않습니다. 가벼운 설치 또는 파일럿으로 처리량, 장애 복구, 운영시간, 저장량, 요청당 비용을 측정한 뒤 승격합니다. 판단은 별도 로그 서비스가 아니라 Git ADR과 manifest 이력에 기록합니다.

정본 규칙: [COST-001](../rules/cost/COST-001.md), [COST-002](../rules/cost/COST-002.md), [DEP-001](../rules/deployment/DEP-001.md), [DEP-002](../rules/deployment/DEP-002.md).
