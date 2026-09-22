# Secrets and configuration

IaC는 secret container, 접근 정책, runtime reference를 정의할 수 있지만 실제 secret value를 소스에 기록하지 않습니다. AWS Lambda와 SAM도 runtime에서 Secrets Manager 같은 외부 secret store를 참조하는 방식으로 구성할 수 있습니다.

프로젝트는 `.env.example`과 필요한 경우 `.env.<name>.example`만 추적합니다. `.env`, `.env.dev`, `.env.prod`를 포함한 실제 환경 파일은 Git에서 제외합니다. example에는 키 이름과 안전한 가상 값만 둡니다.

문자열 기반 환경 값을 읽고 합치는 loader 내부에서는 map을 사용할 수 있습니다. 그 결과가 composition root나 runtime consumer로 이동할 때는 허용 필드, 타입, 선택 여부와 기본값 의미가 드러나는 이름 있는 설정 계약으로 변환합니다. 특정 Python library나 settings framework를 공통 기본값으로 강제하지 않습니다.

로컬의 숨은 Git hook은 Phase 0에서 자동 설치하지 않습니다. 보안·데이터 손상 검사는 즉시 자동화 후보로 다루고, 일반 누락은 독립된 작업에서 반복 확인된 뒤 hook 또는 CI 승격을 검토합니다.

정본 규칙: [SEC-001](../rules/security/SEC-001.md), [SEC-002](../rules/security/SEC-002.md), [PROJ-001](../rules/project/PROJ-001.md), [CODE-005](../rules/code/CODE-005.md).
