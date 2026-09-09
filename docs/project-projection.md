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
- `lock.yaml`: 같은 정책 source·released version·content digest와 manifest에서 byte 단위로 동일하게 생성되는 해석 결과. Git source는 해석한 revision도 기록합니다. timestamp를 넣지 않고 직접 수정하지 않습니다.
- `decisions/`: architecture와 infrastructure 판단을 보존하는 ADR.
- `changes/<YYYYMMDD-short-slug>/spec.md`: 활성 변경의 단일 명세. 완료 뒤 지속되는 내용만 정본·manifest·ADR로 옮깁니다.

모노레포는 루트 manifest에 공통 선택을 두고 독립 배포 단위의 unit manifest에는 차이만 선언합니다.

## 정책 source와 release 고정

외부 프로젝트의 `policy.source`는 권한 있는 작업자가 다시 읽을 수 있는 canonical repository 또는 immutable bundle을 가리킵니다. template의 `example.invalid`는 실제 source가 아니며 convergence 전에 반드시 교체합니다. machine-specific absolute path는 다른 환경에서 재현되지 않으므로 허용하지 않습니다. 상대 경로는 정책 저장소 자체의 self projection이나 프로젝트가 함께 versioning하는 vendored policy에만 사용하고 그 경계를 기록합니다.

승인된 project manifest는 발행된 exact version을 선택합니다. 미발행 정책 검토는 commit과 worktree 상태를 shadow assessment report에 기록하며 승인된 manifest version인 것처럼 투영하지 않습니다. lock은 version label만 믿지 않고 canonical policy digest와, Git처럼 제공 가능한 경우 resolved revision을 함께 기록합니다.

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
