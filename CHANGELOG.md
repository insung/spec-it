# Changelog

이 프로젝트는 [Semantic Versioning](https://semver.org/)을 사용합니다. 프로젝트는 정확한 정책 버전을 고정하며 자동 업그레이드하지 않습니다.

## Unreleased — active policy loop candidate

- vendor-neutral policy loop core와 Claude Code adapter의 local opt-in 후보.
- Light/Hard 자동 분류, pinned rule card, fingerprint dedup, ephemeral redacted metric.
- 일반 finding은 advisory로 유지하고 policy-unavailable 또는 material open decision 뒤 mutation만 구조화 deny.
- 고위험 Python HTTP API의 격리 worktree 약식 파일럿에서 초기 no-change 오탐을 수정하고 9개 분류 scenario와 기존 164 tests/Ruff 기준선을 재검증.
- 공개 release, VERSION/tag, self manifest/lock upgrade, Codex adapter, CI/release enforcement는 아직 수행하지 않음.

## 0.6.0 - 2026-09-22

### Added

- 설정 loader 내부의 raw map과 runtime consumer 경계의 이름 있는 typed configuration contract를 구분하는 `CODE-005`.
- 외부 정본의 독립적으로 변하는 사실을 주석에 손으로 복제하지 않도록 하는 `CODE-006`.
- 0.5.0 프로젝트의 명시적 재수렴과 human-review 한계를 설명하는 migration guide.

### Changed

- `backend-service`, `serverless-function`, `python` profile이 두 언어 중립 code 규칙을 연결하도록 version을 `0.6.0`으로 올림.
- code convention, comment, configuration 설명이 raw parsing map의 허용 경계와 외부 사실 사본의 예외를 구분하도록 보완.

### Compatibility and enforcement

- 기존 프로젝트에 새 의무를 추가하는 pre-1.0 minor release이며 0.5.0 이하 manifest와 lock을 자동 업그레이드하지 않는다.
- 관측은 한 저장소의 한 작업에서 나왔으므로 두 규칙은 `manual/implemented` human review이며 validator·Ruff rule·CI action으로 승격하지 않는다.
- 한 번 쓰는 환경변수 key의 상수화는 공개 core나 Python profile parameter로 채택하지 않으며 필요하면 private overlay 또는 프로젝트 lint 설정이 소유한다.

## 0.5.0 - 2026-09-16

- 읽기 전용 `spec-it-impact`와 기존 스킬의 되읽기·사용자 정정·조사 신선도·원문 기반 검증 인계 안내.
- 선택적 영향/Case/Run template, 분리 QA 저장소 합성 예제와 기획 적합성·고객 목적·탐색 구분.
- 기존 GOV/TST 규칙을 재사용하며 새 규칙·risk profile·schema 변경과 QA 폴더/도구 강제는 없음.
- [후보 안내](docs/migrations/0.4.0-to-0.5.0.md)에 0.4.0 self lock의 전역/그룹 정렬 digest 불일치와 후속 처리 기록.
- 고정 합성 사례 24개에서 기준선 22/24와 최종 후보 24/24를 관찰하고, 네 차례 독립 감사에서 발견한 IV-01·F-1·BEH-001을 수정·재검증. 이는 일반 성공률이나 실제 제품 QA 통과가 아님.
- `VERSION`·self projection과 lock digest를 `0.5.0` bytes에 맞춰 재수렴하고 annotated tag 기반 release gate를 완료.
- watcher, QA runner, 자동 validator/CI enforcement, 전역 설치와 프로젝트 자동 업그레이드는 제공하지 않음. 기존 다섯 설치 스킬이 live symlink인 환경에서는 worktree 내용이 보일 수 있음.

## 0.4.0 - 2026-09-10

### Added

- 공개 policy source를 content digest와 선택적 immutable revision으로 고정하는 lock schema 0.2.0 계약.
- HTTP streaming wire contract와 stream open 전 HTTP status·open 후 typed event 오류 mapping.
- generic SSE message contract fixture와 0.3.0 프로젝트의 명시적 재수렴 안내.
- EC2 host runtime과 Docker Compose deployment를 분리 평가하는 infrastructure profile.
- EC2의 interruptible capacity, capacity shortage와 replacement recovery를 project threshold 안에서 평가하는 계약.
- 새 project-owned table·column의 `lower-snake-case` 기본값, 명시적 project override와 legacy·외부 소유 identifier 보존을 연결하는 `DATA-010` 및 RDS profile parameter.
- RDS topology, capacity, failover, backup·PITR, restore, maintenance, heavy DDL와 ownership boundary를 다루는 infrastructure evaluation.
- repository-scoped skill discovery와 기존 `.gitignore`를 보존하는 projection 절차.

### Changed

- HTTP API profile, 사용자 메시지 schema·template, governance·projection·reliability 설명과 policy self-projection을 0.4.0 기준선에 맞춤.
- 운영 판단 승인자를 구분할 수 있도록 manifest owner에 선택적 `operations-owner`를 추가.
- `DATA-009`와 `capability/db-migration`이 object decision owner, definition authority와 executor를 구분하고, immutable DB release definition과 그 digest를 참조하는 environment history를 분리하도록 정밀화.
- baseline·desired schema 같은 current-state projection의 authority와 release chain 대조, historical·emergency reconciliation의 증거 한계를 명시하고 특정 migration 제품의 명명법을 공통 기본값에서 제외.

### Compatibility and enforcement

- lock artifact 형식과 조건부 profile 의무가 바뀌는 pre-1.0 minor release이며 0.3.0 project manifest와 lock을 자동 업그레이드하지 않는다.
- deterministic lock generator, policy bundle assembler, DB release·environment evidence schema와 runner, SSE runtime validator, EC2·Compose provision/deploy/rollback executor는 구현하지 않는다.
- 별도 lifecycle 정책, project-specific 사례와 private overlay는 이 공개 공통 릴리스 범위에 포함하지 않는다.

## 0.3.0 - 2026-09-08

### Added

- DB 변경을 version·checksum·객체 소유권·application artifact compatibility·single-executor coordination·environment history·recovery class가 있는 release unit으로 관리하는 `DATA-009`.
- 정기 data pipeline의 terminal output freshness·completeness·integrity·reconciliation, run ledger, accountable alert와 dependency-aware replay를 연결하는 `OBS-003`.
- DB 변경 책임과 정기 데이터 생산 책임을 조건부로 선택하는 `capability/db-migration`, `capability/data-pipeline`.
- 저장소 topology와 자동·위임 실행 lane, recovery class를 설명하는 DB 변경 배포 문서와 data pipeline 운영 문서.
- 0.2.0 프로젝트의 명시적 재수렴 절차와 0.3.0 release checklist.

### Changed

- 규칙·profile·문서 색인, README, project template와 policy self-projection을 0.3.0 기준선에 맞춤.
- compatibility, data, observability 설명이 새 규칙의 책임 경계를 연결하도록 갱신.

### Compatibility and enforcement

- 새 의무를 갖는 pre-1.0 minor release이며 0.2.0 project manifest와 lock은 자동 업그레이드하지 않는다.
- migration runner, release bundle schema, DB connector, drift detector, runtime monitor, alert와 replay executor는 구현하지 않는다.
- 신규 규칙의 enforcement target은 `ci` 또는 `runtime`이지만 implementation은 `planned`이며 Phase 0 판정은 `human-review`다.
- 제품·edition·license, 저장소 위치, UI, project threshold와 MI private overlay는 프로젝트별 별도 결정이다.

## 0.2.0 - 2026-09-08

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

- backend-service, serverless-function, python, aws-lambda, rds, redis, http-api, shared-domain-library 프로필을 0.2.0 활성 정책으로 변경.
- 아키텍처·관측·호환성·프로필 설명과 통합 테스트 계획에 관련 경계와 검사 항목 추가.
- README에 처음 쓰는 사용자의 최소 요청과 AI가 고정된 규칙을 발견하는 작업 흐름을 추가하고, Phase 0 checklist의 `0.1.0` 종료 증거 범위를 명확히 함.
- `spec-it:specify`, `clarify`, `check`가 짧은 요청에서 변경 trigger를 찾고 규칙의 이유·영향·예외를 사용자에게 설명하도록 절차를 보완함.
- Python을 Ruff 기반 lint contract와 공통 code 의미 규칙에 연결하고, Lambda·Redis를 첫 infrastructure trait reference profile로 확장함.
- 다섯 instruction-only 스킬과 프로젝트 AGENTS template에 preflight, material-signal 재판정, 완료 전 diff 검사와 최소 human interruption 경계를 연결함.

### Compatibility and enforcement

- 추가 의무를 갖는 pre-1.0 정책 변경이므로 0.2.0 minor로 릴리스한다. 0.1.0 patch 수정으로 취급하지 않는다.
- 기존 규칙 ID의 규범 의미는 유지한다. 0.1.0 프로젝트 manifest/lock은 자동 변경하지 않으며 migration과 재수렴이 필요하다.
- 정책 릴리스와 프로젝트별 clarify/converge는 별도 승인 대상이다. 새 규칙의 자동 검증은 planned이고 Phase 0 판정은 human-review다.
- 애플리케이션·검증기·생성기·CI·플러그인 구현/배포는 포함하지 않는다.

## 0.1.0 - 2026-09-02

### Added

- Phase 0 헌법, 정책, 규칙, 프로필, 스키마, 템플릿, 예제
- `spec-it:specify`, `clarify`, `converge`, `check`, `evolve`의 instruction-only 명세
- 저장소 자체의 `.architecture` 투영
