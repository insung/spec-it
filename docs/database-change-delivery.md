# Database change delivery

이 문서는 [DATA-009](../rules/data/DATA-009.md)를 프로젝트에서 구체화하는 방법을 설명합니다. 규칙은 DB 제품, migration 도구, 저장소 topology와 UI를 고정하지 않습니다.

## 정본과 중앙 릴리즈 보기는 다른 책임이다

SQL 정본은 객체 소유자가 검토할 수 있는 곳에 둡니다. 애플리케이션 저장소, DB 또는 schema 저장소, 중앙 DB 저장소 모두 가능하지만 같은 객체의 경쟁 정본은 두지 않습니다. 객체를 읽거나 호출하는 consumer는 소유자가 아닐 수 있으며 정의 SQL을 복제하지 않습니다.

여러 저장소가 한 기능에 참여하면 중앙 release manifest 또는 immutable bundle이 다음 정보를 연결합니다.

- 원본 저장소, revision, 파일 경로와 checksum
- 대상 engine·database·schema와 소유 객체
- 실행 순서와 선후 의존성
- 애플리케이션 artifact identity와 지원 DB version 또는 capability 범위
- 승인 대상 checksum, 실행 lane, 검증과 복구 분류

manifest-only 방식은 고정 commit과 artifact가 나중에도 동일하게 해석되는지 보장해야 합니다. bundle 방식은 조립 시점의 SQL과 evidence를 변경 불가능한 artifact로 보존합니다. 어느 쪽이든 환경마다 다시 빌드하지 않고 같은 release identity를 승격합니다.

## 자동 실행과 위임 실행

정상 경로는 deployment pipeline의 singleton migration activity입니다. 도구의 DB lock 또는 같은 효과의 serialization으로 두 실행이 같은 변경을 경쟁하지 않게 하고, history에는 적용자·시각·checksum·결과를 남깁니다.

권한 분리 때문에 pipeline이 직접 DDL을 실행할 수 없으면 시스템이 실행 요청 bundle을 만들고 권한 있는 operator가 실행합니다. 이때도 승인 대상과 실제 SQL의 checksum, 실행자·시각·결과, post-apply definition 또는 output verification을 중앙 environment history에 합칩니다. 자동화 비율이 달라도 추적 계약은 같습니다.

애플리케이션 startup은 공유 DDL을 실행하지 않는 것이 기본입니다. 필요한 DB version을 읽고 시작·readiness·traffic을 제한하는 방법은 누락을 일찍 발견하는 선택지입니다. DB 적용 전에도 동작하는 backward-compatible artifact, 배포 전 compatibility gate 같은 다른 방법이 더 적합할 수 있으므로 runtime version check를 보편 구현으로 강제하지 않습니다.

## 실패와 복구

실행 전에는 승인 뒤 checksum 변화, 현재 정의 drift, rehearsal 누락, lock 실패, 요구 DB 상태와 application artifact 불일치를 중단 조건으로 둘 수 있습니다. 어떤 조건을 blocking할지는 risk와 권한 경계가 정합니다.

복구는 SQL keyword가 아니라 이미 발생한 효과를 기준으로 [DATA-009](../rules/data/DATA-009.md)의 네 class 중 하나를 선택합니다. rollback SQL이 존재한다는 사실만으로 안전을 주장하지 않고, 데이터가 이미 쓰였거나 구버전 consumer가 다시 읽을 수 없는 상태인지 검사합니다. 파괴적 변경은 expand-contract, forward fix, replay와 [REL-001](../rules/reliability/REL-001.md)의 restore evidence를 조합합니다.

Flyway, Liquibase, Sqitch, Atlas와 직접 구현은 이 계약을 만족시키는 후보입니다. 제품의 edition, license, engine 지원과 운영 UI는 프로젝트의 별도 도구 결정이며 공통 정책을 바꾸지 않습니다.
