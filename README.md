# spec-it

> Spec it. Build it. Prove it.

`spec-it`은 사람이 의도를 결정하고 AI가 일관되게 구현·검증하도록 만드는 아키텍처 정책 SSOT입니다. 긴 프롬프트 대신 버전이 고정된 규칙, 합성 가능한 프로필, 프로젝트 manifest와 결정 기록을 사용합니다.

이 프로젝트는 GitHub Spec Kit과 이름이 비슷하지만 별개의 독립 프로젝트입니다. 형식 호환, 의존성, adapter를 전제로 하지 않습니다.

## 현재 상태

- 버전: `0.1.0`
- 단계: Phase 0 — 문서·정책·프로필·스키마·템플릿·instruction-only 스킬
- 배포: 공개 Git 저장소용 소스만 제공
- 미구현: validator/CLI, CI 강제, runtime enforcement, 패키지·플러그인 배포

현재 스킬은 판단 절차를 안내하고 `human-review` 또는 `not-implemented`를 정직하게 보고합니다. 결정적 검사를 수행한다고 주장하지 않습니다.

## 시작점

1. [헌법](docs/constitution.md)에서 권한과 우선순위를 읽습니다.
2. [프로젝트 투영](docs/project-projection.md)에서 프로젝트가 보유할 최소 파일을 확인합니다.
3. [프로필](docs/profiles.md)에서 평평한 합성 모델을 선택합니다.
4. [규칙 색인](rules/README.md)에서 적용 규칙을 확인합니다.
5. [스킬](skills/README.md)로 명세·명확화·수렴·검사·진화를 수행합니다.

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
