# Shared domain core libraries — 미발행 0.2.0 초안

도메인 코어를 library로 분리하는 것은 Clean Architecture와 양립합니다. 별도 repository인지가 아니라 domain이 transport, framework, persistence, telemetry에 의존하지 않는지가 기준입니다. 실제 독립 consumer가 없거나 릴리스 조율 비용이 더 크면 같은 repository의 module boundary가 더 저렴할 수 있습니다.

정본 규칙: [ARCH-001](../rules/architecture/ARCH-001.md), [ARCH-003](../rules/architecture/ARCH-003.md), [ARCH-004](../rules/architecture/ARCH-004.md), [ARCH-006](../rules/architecture/ARCH-006.md), [COMP-001](../rules/compatibility/COMP-001.md), [COMP-002](../rules/compatibility/COMP-002.md), [TST-002](../rules/testing/TST-002.md).

## Library boundary

공유 후보는 여러 consumer에서 같아야 하는 business invariant, calculation, state transition, value object입니다. HTTP DTO, ORM model, cloud client, application별 authorization orchestration, 화면 문구는 기본적으로 포함하지 않습니다. 모든 회사 도메인을 하나의 거대한 SDK에 넣지 않고 변화와 소유권이 함께 움직이는 bounded capability로 나눕니다.

같은 library 이름만으로 같은 결과를 보장하지 않습니다. version, configuration, input meaning, data, clock, policy activation이 같아야 합니다. 모든 consumer가 같은 날 정책을 바꿔야 한다면 package 배포와 별도로 activation version과 전환 계획을 둡니다.

## Release impact

library release는 다음을 밝힙니다.

- changed capability와 관측 가능한 이전/새 동작.
- public contract와 SemVer 판단.
- security, data, calculation, migration, configuration 영향.
- 최소·지원·지원 종료 version.
- 회귀 fixture와 검증 결과.

함수 signature가 같아도 자격 조건·한도·계산·상태 전이가 바뀌면 behavior impact입니다. 반대로 사용하지 않는 additive capability 때문에 모든 consumer가 즉시 update할 필요는 없습니다.

## Consumer assessment

각 알려진 consumer는 다음 중 하나로 판정합니다.

| 판정 | 의미 | 다음 행동 |
| --- | --- | --- |
| `update-required` | 사용 경로에 보안·데이터 손상·중대한 오류 또는 강제 migration이 있음 | 위험 기반 기한, update 또는 승인된 임시 완화 |
| `update-planned` | 사용 중인 동작 변경이나 유효한 개선이 있음 | regression과 배포 일정 |
| `not-required` | 변경된 capability를 쓰지 않고 현재 pin이 지원 중임 | 근거와 재검토 trigger |
| `impact-unknown` | 사용·전이·배포 근거가 부족함 | 담당자 평가; 영향 없음으로 간주하지 않음 |

정적 import 검색은 출발점일 뿐 reflection, transitive usage, remote call, configuration activation을 놓칠 수 있습니다. lockfile/SBOM, capability usage, tests, runtime artifact를 함께 봅니다.

## Update and deployment states

```text
observed → assessed → update-planned → merged → deployed → verified
```

merged는 repository의 새 version이고 deployed는 특정 environment의 artifact에 포함된 version입니다. verified는 그 environment에서 계약과 수용 기준을 확인한 상태입니다. 각 전이는 library release, consumer commit과 lock, build artifact, deployment identity, test evidence를 연결합니다.

[core library impact template](../templates/project/core-library-impact.yaml)은 한 consumer의 판단을 기록하는 시작점입니다. 거대한 수동 중앙 목록을 또 하나의 정본으로 만들지 않습니다. 실제 dependency bot, artifact registry, CI/CD integration은 프로젝트가 도구를 선택한 뒤 이 필드에서 생성합니다.

자료: [Semantic Versioning](https://semver.org/).
