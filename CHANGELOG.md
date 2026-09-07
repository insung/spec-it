# Changelog

이 프로젝트는 [Semantic Versioning](https://semver.org/)을 사용합니다. 프로젝트는 정확한 정책 버전을 고정하며 자동 업그레이드하지 않습니다.

## Unreleased — 0.2.0 draft

### Added

- 트랜잭션·후속 작업 소유권 `ARCH-005`, 프로시저 실행 근거와 관리 `DATA-007`.
- 공개 결과 계약 `MSG-001`, 사용자 안내·다국어·로그 경계 `MSG-002`.
- 메시지 계약 설명, YAML 시작 템플릿, JSON Schema와 가상 내보내기 fixture.
- 규칙별 실제 증거, 구조/동작/번역/호환성 검증과 미구현 검사를 구분하는 안내.
- transport/application DTO 분리 `ARCH-006`과 HTTP path·mutation·JSON·canonical contract·audience/lifecycle `API-001`~`API-005`.
- 격리된 통합 환경과 production-derived data 안전 `TST-006`, 공유 core consumer update 추적 `COMP-002`.
- API 설계·공개·수명주기, 공유 도메인 core library 문서와 `http-api`, `shared-domain-library` capability 초안.
- API contract 결정과 core library consumer impact 시작 템플릿, 대화를 정본으로 분류하는 `spec-it:evolve` reference.
- 영어 project identifier와 의미 중심 이름 `CODE-002`·`CODE-003`, 계층 경계의 이름 있는 계약 `CODE-004`, 언어별 lint contract `TOOL-005`.
- 인프라 평가 구조와 bounded 재판정 `INFRA-001`·`INFRA-002`, 플랫폼 선택 전 가용성 계약 `REL-002`, 측정 기반 물리 저장 축약 `DATA-008`.
- 공통 코딩 컨벤션과 AI agent 작업 주기 문서.

### Changed

- backend-service, serverless-function, rds 프로필을 추가 규칙에 연결한 0.2.0 draft 후보로 변경.
- 아키텍처·관측·호환성·프로필 설명과 통합 테스트 계획에 관련 경계와 검사 항목 추가.
- README에 처음 쓰는 사용자의 최소 요청과 AI가 고정된 규칙을 발견하는 작업 흐름을 추가하고, Phase 0 checklist의 `0.1.0` 종료 증거 범위를 명확히 함.
- `spec-it:specify`, `clarify`, `check`가 짧은 요청에서 변경 trigger를 찾고 규칙의 이유·영향·예외를 사용자에게 설명하도록 절차를 보완함.
- Python을 Ruff 기반 lint contract와 공통 code 의미 규칙에 연결하고, Lambda·Redis를 첫 infrastructure trait reference profile로 확장함.
- 다섯 instruction-only 스킬과 프로젝트 AGENTS template에 preflight, material-signal 재판정, 완료 전 diff 검사와 최소 human interruption 경계를 연결함.

### Compatibility and enforcement

- 추가 의무를 갖는 pre-1.0 정책 변경이므로 다음 minor 후보는 0.2.0이다. 0.1.0 patch 수정으로 취급하지 않는다.
- 기존 규칙 ID의 규범 의미와 기존 0.1.0 프로젝트 manifest/lock, VERSION은 유지한다. draft 프로필은 기존 기준선을 대체하지 않는다.
- 릴리스와 프로젝트별 clarify/converge는 별도 승인 대상이다. 새 규칙의 자동 검증은 planned이고 Phase 0 판정은 human-review다.
- 애플리케이션·검증기·생성기·CI·플러그인 구현/배포는 포함하지 않는다.

## 0.1.0 - 2026-09-02

### Added

- Phase 0 헌법, 정책, 규칙, 프로필, 스키마, 템플릿, 예제
- `spec-it:specify`, `clarify`, `converge`, `check`, `evolve`의 instruction-only 명세
- 저장소 자체의 `.architecture` 투영
