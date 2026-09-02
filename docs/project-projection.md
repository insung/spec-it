# Project projection

프로젝트는 공통 규칙 전체를 복사하지 않습니다. 정확한 정책 버전과 선택한 프로필, 예외, 결정 결과만 투영합니다.

```text
AGENTS.md
.architecture/
├── project.md
├── manifest.yaml
├── lock.yaml
├── decisions/
└── changes/
.spec-it/
└── reports/        # Git 제외
```

- `AGENTS.md`: AI가 읽는 짧은 입구. 정책 버전, manifest, 검사 방법을 가리키며 생성 관리 블록과 사용자 블록을 분리합니다.
- `project.md`: 사람이 읽는 프로젝트 목적·경계·성공 기준.
- `manifest.yaml`: 사람의 승인을 받은 선택 입력.
- `lock.yaml`: 같은 정책 버전과 manifest에서 byte 단위로 동일하게 생성되는 해석 결과. timestamp를 넣지 않고 직접 수정하지 않습니다.
- `decisions/`: architecture와 infrastructure 판단을 보존하는 ADR.
- `changes/<YYYYMMDD-short-slug>/spec.md`: 활성 변경의 단일 명세. 완료 뒤 지속되는 내용만 정본·manifest·ADR로 옮깁니다.

모노레포는 루트 manifest에 공통 선택을 두고 독립 배포 단위의 unit manifest에는 차이만 선언합니다.

## Lambda 기준 구조

```text
lambda-a/
├── handler.py
├── domain/
├── services/
├── adapters/
├── tests/
├── deploy/
│   └── template.yaml
├── .env.example
└── .architecture/
```

Lambda profile은 `src/` depth를 만들지 않고 배포 정의를 숨기지 않은 `deploy/`에 둡니다. 실제 `.env*`는 Git에서 제외합니다.

정본 규칙: [PROJ-001](../rules/project/PROJ-001.md), [PROJ-002](../rules/project/PROJ-002.md), [PROJ-003](../rules/project/PROJ-003.md), [TOOL-002](../rules/tooling/TOOL-002.md), [TOOL-003](../rules/tooling/TOOL-003.md).
