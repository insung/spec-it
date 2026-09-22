# spec-it

> Spec it. Build it. Prove it.

`spec-it`은 사람이 의도를 결정하고 AI가 일관되게 구현·검증하도록 만드는 아키텍처 정책 SSOT입니다. 긴 프롬프트 대신 버전이 고정된 규칙, 합성 가능한 프로필, 프로젝트 manifest와 결정 기록을 사용합니다.

이 프로젝트는 GitHub Spec Kit과 이름이 비슷하지만 별개의 독립 프로젝트입니다. 형식 호환, 의존성, adapter를 전제로 하지 않습니다.

## 현재 상태

- 버전: `0.7.0`
- 단계: Phase 1 진입 — Phase 0 정책 source + local opt-in active policy loop
- 배포: 공개 Git 저장소용 소스만 제공
- 미구현: 범용 validator/CLI, CI 강제, fail-close runtime enforcement, 패키지·플러그인 배포

현재 스킬은 판단 절차를 안내하고 `human-review` 또는 `not-implemented`를 정직하게 보고합니다. Claude-first active policy loop는 고정 policy identity와 material signal을 결정적으로 확인하지만, 일반 규칙 준수를 판정하는 범용 validator라고 주장하지 않습니다.

### 0.7.0 공개 기준선

`0.7.0`은 vendor-neutral core와 Claude Code adapter로 구성된 local opt-in active policy loop를 추가합니다. Light/Hard 분류, 고정된 tag의 rule card, fingerprint dedup, redacted ephemeral metric을 제공하며, policy state가 유효하지 않거나 material human decision이 열린 뒤의 mutation만 좁게 거부합니다. 일반 finding은 advisory이고 command hook 자체의 누락·오류·timeout은 fail-open일 수 있습니다.

기존 프로젝트는 자동 업그레이드하거나 자동 활성화하지 않습니다. [0.6.0 → 0.7.0 migration guide](docs/migrations/0.6.0-to-0.7.0.md)에 따라 정확한 tag와 digest로 재수렴한 뒤 프로젝트 로컬 설정에서 별도로 켭니다. 사용법과 실패 경계는 [active policy loop](docs/active-policy-loop.md), 최초 약식 측정은 [initial pilot](docs/pilots/active-policy-loop-initial.md), 릴리스 증거는 [0.7.0 release checklist](docs/releases/0.7.0-checklist.md)를 참고합니다.

### 0.6.0 공개 기준선

`0.6.0`은 설정 loader 밖의 경계에 이름 있고 typed된 설정 계약을 요구하는 `CODE-005`와 외부 정본의 변동 사실을 주석에 독립 사본으로 두지 않는 `CODE-006`을 추가합니다. 두 규칙은 manual human review이며 validator, Ruff rule 또는 CI action을 추가하지 않습니다. 공개 기준선은 annotated tag `v0.6.0`으로 식별하며, 기존 프로젝트는 [migration guide](docs/migrations/0.5.0-to-0.6.0.md)에 따라 별도로 재수렴해야 합니다. 릴리스 증거와 한계는 [0.6.0 release checklist](docs/releases/0.6.0-checklist.md)에 기록합니다.

### 0.5.0 공개 기준선

`0.5.0`은 사람의 원문 의도에서 영향 경로와 검증 증거까지 연결하는 instruction-only 절차를 추가합니다. 새 read-only `spec-it-impact`, 기존 스킬의 되읽기·정정·신선도 인계, 선택적 영향/Case/Run 템플릿과 합성 예제를 제공합니다. 새 규칙·risk profile·공개 schema나 통합 QA 도구를 강제하지 않습니다.

공개 기준선은 annotated tag `v0.5.0`으로 식별합니다. 기존 프로젝트는 자동 업그레이드하지 않으며, 상세한 채택 경계는 [0.4.0 → 0.5.0 migration guide](docs/migrations/0.4.0-to-0.5.0.md), 릴리스 증거와 한계는 [0.5.0 release checklist](docs/releases/0.5.0-checklist.md)에 있습니다.

### 0.4.0 공개 기준선

`0.4.0`은 공개 정책 source의 불변 content digest, DB release의 소유·정본·실행 책임과 환경 증거 경계, HTTP streaming의 stream open 전·후 오류 계약, `runtime/aws-ec2`와 `deployment/docker-compose`의 독립 인프라 평가, RDS의 topology·capacity·recovery 및 새 소유 table·column의 `lower-snake-case` 기본값을 추가하거나 정밀화합니다. 공개 기준선은 annotated tag `v0.4.0`으로 식별합니다.

기존 프로젝트는 자동 업그레이드하지 않으며 [0.3.0 → 0.4.0 migration guide](docs/migrations/0.3.0-to-0.4.0.md)에 따라 별도로 재수렴합니다. 릴리스 검증과 known limits는 [0.4.0 release checklist](docs/releases/0.4.0-checklist.md)에 기록합니다.

### 0.3.0 공개 기준선

`0.3.0`은 `0.2.0`의 계약에 DB 변경 release unit과 정기 data pipeline outcome 운영을 추가합니다. DB 변경을 작성·요청·실행하는 프로젝트는 `capability/db-migration`, consumer용 정기 데이터를 생산하는 프로젝트는 `capability/data-pipeline`을 조건부로 선택합니다. 기존 프로젝트는 자동 업그레이드하지 않으며 [migration guide](docs/migrations/0.2.0-to-0.3.0.md)에 따라 별도로 재수렴합니다.

[사용자 메시지와 오류 계약](docs/user-messages-and-errors.md)의 「문서와 코드가 다르지 않은지 어떻게 확인하나」에서 실제 코드 검증 절차와 Phase 0의 한계를 확인할 수 있습니다. 새 schema의 구조 검사 성공은 실제 애플리케이션 준수 판정이 아닙니다.

릴리스의 구조 검증과 미구현 경계는 [0.3.0 release checklist](docs/releases/0.3.0-checklist.md)에 기록합니다.

## 한 문장으로 시작하기

사용자가 규칙 ID나 프로필 이름을 외울 필요는 없습니다. AI에게 의도와 수정 허용 범위만 짧게 알려주고, 발견 가능한 사실은 저장소에서 조사하게 합니다.

정책을 아직 투영하지 않은 기존 프로젝트에서는 다음처럼 시작합니다.

> `/path/to/spec-it`을 기준으로 이 저장소를 브라운필드 shadow assessment 해줘. 먼저 파일을 수정하지 말고 현재 상태, 적용할 프로필 후보, 규칙과 충돌하는 부분, 내가 결정해야 할 것만 이유와 함께 설명해줘.

이미 spec-it을 투영한 프로젝트에서는 더 짧게 요청할 수 있습니다.

> spec-it으로 이 저장소를 점검해줘. 먼저 변경하지 말고 현재 상태와 내가 결정할 것부터 알려줘.

새 프로젝트의 요구가 아직 모호할 때도 긴 설계 문서를 먼저 만들 필요가 없습니다.

> spec-it으로 Lambda 프로젝트를 만들고 싶어. 바로 구현하지 말고 필요한 결정을 나와 먼저 정해줘.

AI는 저장소에서 확인할 수 있는 언어·런타임·배포 방식·기존 계약을 스스로 조사하고, 사용자의 가치 판단이 필요한 질문만 해야 합니다. 질문마다 왜 지금 결정해야 하는지, 권장 기본값, 비용과 위험, 선택에 따라 무엇이 달라지는지를 설명합니다.

## AI가 작업 중 규칙을 찾는 방법

spec-it은 AI의 기억이나 긴 프롬프트에 의존하지 않습니다. 프로젝트에 투영된 파일과 고정된 정책 버전이 작업 진입점입니다.

```text
사용자 요청
  -> AGENTS.md
  -> .architecture/manifest.yaml
  -> .architecture/lock.yaml의 적용 규칙 ID
  -> 작업 시작 profile preflight
  -> 활성 변경 명세와 결정 기록
  -> 구현
  -> material signal이 있을 때만 profile 재판정
  -> 완료 전 실제 diff 검사
  -> spec-it:check
```

예를 들어 사용자가 단순히 “가입 승인 API 엔드포인트를 만들어줘”라고 요청해도 AI는 router/controller, 전송 DTO, OpenAPI 같은 공개 계약의 추가를 `change` 범위 trigger로 판정해야 합니다. 구현 전에 잠긴 `http-api` 관련 규칙을 읽고, 승인이라는 동작의 의미·접근 권한·멱등성·공개 범위처럼 코드에서 발견할 수 없는 결정만 `spec-it:clarify`로 돌려보냅니다. 결정이 수렴한 뒤 path·method·DTO 경계·계약 테스트를 구현하고, `spec-it:check`에서 실제 변경과 규칙을 대조합니다.

`AGENTS.md`를 자동으로 읽지 않는 AI 도구에는 해당 파일부터 읽으라는 adapter 또는 시작 요청이 필요합니다. `0.7.0`의 Claude-first active policy loop는 local opt-in에서만 이 checkpoint를 자동 호출하며, 일반 규칙 위반은 advisory로 남기고 policy state 불능 또는 열린 material 결정 뒤 mutation만 좁게 거부합니다. 다른 AI 도구와 hook을 켜지 않은 프로젝트에는 기존 instruction-only 절차가 그대로 적용됩니다.

AI에게는 “이 프로젝트의 `AGENTS.md`와 연결된 spec-it 정책을 먼저 읽고, 적용 규칙과 필요한 인간 결정을 알려준 뒤 작업하며, 완료 전 `spec-it:check` 기준으로 검사해줘” 정도면 충분합니다. 프로젝트가 아직 정책을 채택하지 않았다면 먼저 읽기 전용 shadow assessment를 수행합니다. 자세한 checkpoint는 [agent work cycle](docs/agent-work-cycle.md)에 있습니다.

## 시작점

1. [헌법](docs/constitution.md)에서 권한과 우선순위를 읽습니다.
2. [프로젝트 투영](docs/project-projection.md)에서 프로젝트가 보유할 최소 파일을 확인합니다.
3. [프로필](docs/profiles.md)에서 평평한 합성 모델을 선택합니다.
4. [규칙 색인](rules/README.md)에서 적용 규칙을 확인합니다.
5. [스킬](skills/README.md)로 명세·명확화·수렴·검사·진화를 수행합니다.
6. [AI agent 작업 주기](docs/agent-work-cycle.md)에서 작업 전·중·후 재판정 경계를 확인합니다.

## 저장소 지도

| 경로 | 역할 | 규범성 |
| --- | --- | --- |
| `rules/` | 한 규칙 한 파일의 유일한 규칙 정본 | 규범 |
| `profiles/` | 규칙 ID와 기본값의 합성 묶음 | 규범 |
| `schemas/` | 프로젝트 산출물의 기계 판독 계약 | 규범 |
| `docs/` | 철학, 관계, 선택 절차의 설명 | 비규범; 새 의무를 만들지 않음 |
| `templates/` | 시작용 사본 | 비규범 |
| `examples/` | 합성·충돌·실패 사례 | 비규범 |
| `skills/` | AI가 SSOT를 적용하는 instruction-only 절차 | 절차 |
| `.architecture/` | 이 저장소 자체의 정책 투영 | 프로젝트 정본 |

규칙의 의미는 `rules/`의 개별 Markdown 파일에만 있습니다. 문서·템플릿·예제의 설명이 다르면 규칙 파일을 따릅니다.

## 공개와 비공개 경계

공통 원칙·스키마·검증 계약·예제만 이 저장소에 둡니다. 개인 판단 기록과 회사 고유 프로젝트·인프라·계정·식별 정보는 별도의 비공개 overlay에 둡니다. 비공개 overlay가 공통 규칙을 완화하려면 승인된 예외와 만료 조건이 필요합니다.

## 라이선스

[Apache License 2.0](LICENSE)
