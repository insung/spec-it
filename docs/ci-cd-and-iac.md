# CI/CD and IaC

PR 품질 검사는 GitHub Actions 같은 저장소 CI가 맡고, 배포는 CodePipeline·CodeBuild·CodeDeploy 같은 환경별 pipeline이 맡을 수 있습니다. 서비스 이름은 공통 원칙이 아니라 deployment profile의 구현 선택입니다.

기본 흐름은 `main + short-lived branch + path detection + independent deploy unit + immutable artifact promotion`입니다. 모노레포에서도 환경·Lambda별 deploy branch를 늘리지 않습니다. 루트 manifest는 공통값을, 독립 배포 단위의 unit manifest는 차이만 선언합니다.

IaC는 인프라 구조·권한·참조를 소스화합니다. Terraform 또는 OpenTofu를 선택한다면 얕은 module composition과 명시적인 입력·출력을 사용합니다. CloudFormation 형식이나 Pulumi를 포함한 도구 선택은 가독성, preview, drift, 테스트성, 팀 숙련도, 유지비로 프로젝트에서 결정합니다. CDK는 현재 선호 선택지에서 제외하지만 공통 규칙에 제품 금지로 고정하지 않습니다.

Lambda의 SAM 정의는 각 deploy unit 안의 `deploy/`에 둡니다. 자세한 구조는 [프로젝트 투영](project-projection.md)과 [PROJ-002](../rules/project/PROJ-002.md)를 참조합니다.

정본 규칙: [CICD-001](../rules/ci-cd/CICD-001.md), [CICD-002](../rules/ci-cd/CICD-002.md), [IAC-001](../rules/iac/IAC-001.md), [IAC-002](../rules/iac/IAC-002.md).
