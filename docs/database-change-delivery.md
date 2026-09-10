# Database change delivery

이 문서는 [DATA-009](../rules/data/DATA-009.md)를 프로젝트에서 구체화하는 방법을 설명합니다. 규칙은 DB 제품, migration 도구, 저장소 topology와 UI를 고정하지 않습니다.

## 객체 소유권, SQL 정본과 실행은 다른 책임이다

DB 변경은 객체의 업무 의미와 변경을 승인하는 object decision owner, 실행 가능한 SQL 정본을 보관하는 definition authority, 승인된 내용을 적용하는 executor를 구분합니다. 한 저장소나 사람이 여러 책임을 겸할 수 있지만, 중앙 DB 저장소가 SQL을 보관하거나 DB 계정이 DDL 권한을 가졌다는 사실만으로 object decision ownership을 얻지는 않습니다. 객체를 읽거나 호출하는 consumer와 데이터를 쓰는 producer도 영향받는 주체이지 자동으로 소유자가 되지는 않습니다.

SQL 정본은 object decision owner가 검토할 수 있는 곳에 둡니다. 애플리케이션 저장소, DB 또는 schema 저장소, 중앙 DB 저장소 모두 가능하지만 같은 객체의 경쟁 정본은 두지 않습니다. 중앙 저장소 방식을 택하면 객체별 decision owner와 원본 revision을 별도로 연결합니다.

여러 저장소가 한 기능에 참여하면 중앙 release manifest 또는 immutable bundle이 다음 정보를 연결합니다.

- object decision owner, definition authority, 원본 revision과 파일 경로
- 대상 engine·database·schema, 영향받는 객체와 checksum
- 실행 순서와 선후 의존성
- 애플리케이션 artifact identity와 지원 DB version 또는 capability 범위
- 승인 대상 release digest, executor 또는 delegated lane, 검증과 복구 분류

manifest-only 방식은 고정 commit과 artifact가 나중에도 동일하게 해석되는지 보장해야 합니다. bundle 방식은 조립 시점의 SQL과 release definition을 변경 불가능한 artifact로 보존합니다. 어느 쪽이든 환경마다 다시 빌드하지 않고 같은 release identity를 승격합니다.

## 릴리즈 정의와 환경별 이력

승인된 release definition은 SQL, 순서, checksum, compatibility와 recovery class를 포함한 digest를 갖습니다. QA·운영 적용 결과는 그 digest를 참조하는 environment history로 남깁니다. 두 자료를 같은 저장소에 둘 수는 있지만, 새 환경 기록을 추가하기 위해 승인된 release definition 자체를 고치지 않습니다.

환경 이력은 SQL 실행 결과와 post-apply verification을 구분합니다. 명령이 성공했어도 정의가 기대와 다르거나 알려진 consumer의 compatibility가 미해결이면 전체 릴리즈 성공으로 판정하지 않습니다. 승인 기록도 파일 glob이나 움직이는 branch가 아니라 승인한 release digest를 가리킵니다.

## 현재 정의 projection

빈 DB 설치용 baseline, desired schema 또는 current-definition snapshot은 선택 사항입니다. 함께 사용하면 migration history와 경쟁하는 두 번째 정본으로 방치하지 않고 독립 정본인지 파생 projection인지 선언합니다. 파생 projection은 이전 기준선에 승인된 release chain을 적용한 결과와 같음을 승격 전에 생성하거나 대조합니다. 운영 적용이 끝난 뒤 사람의 기억으로만 baseline을 맞추는 절차는 그 등가성을 보장하지 못합니다.

## 자동 실행과 위임 실행

정상 경로는 deployment pipeline의 singleton migration activity입니다. 도구의 DB lock 또는 같은 효과의 serialization으로 두 실행이 같은 변경을 경쟁하지 않게 하고, history에는 적용자·시각·checksum·결과를 남깁니다.

권한 분리 때문에 pipeline이 직접 DDL을 실행할 수 없으면 시스템이 실행 요청 bundle을 만들고 권한 있는 operator가 실행합니다. 이때도 승인 대상과 실제 SQL의 checksum, 실행자·시각·결과, post-apply definition 또는 output verification을 중앙 environment history에 합칩니다. 자동화 비율이 달라도 추적 계약은 같습니다.

이미 실행된 SQL을 나중에 확보하면 버리지 않고 historical 또는 emergency reconciliation으로 보존합니다. 이 기록에는 출처, 실제 SQL, 실행 결과, 확인하지 못한 사전 gate와 정상 경로로 전환할 owner·due condition을 남깁니다. 사후 checksum은 현재 보존된 파일을 식별하지만 실행 전에 같은 내용을 승인했다는 증거는 아닙니다.

애플리케이션 startup은 공유 DDL을 실행하지 않는 것이 기본입니다. 필요한 DB version을 읽고 시작·readiness·traffic을 제한하는 방법은 누락을 일찍 발견하는 선택지입니다. DB 적용 전에도 동작하는 backward-compatible artifact, 배포 전 compatibility gate 같은 다른 방법이 더 적합할 수 있으므로 runtime version check를 보편 구현으로 강제하지 않습니다.

## 실패와 복구

실행 전에는 승인 뒤 checksum 변화, 현재 정의 drift, rehearsal 누락, lock 실패, 요구 DB 상태와 application artifact 불일치를 중단 조건으로 둘 수 있습니다. 어떤 조건을 blocking할지는 risk와 권한 경계가 정합니다.

복구는 SQL keyword가 아니라 이미 발생한 효과를 기준으로 [DATA-009](../rules/data/DATA-009.md)의 네 class 중 하나를 선택합니다. rollback SQL이 존재한다는 사실만으로 안전을 주장하지 않고, 데이터가 이미 쓰였거나 구버전 consumer가 다시 읽을 수 없는 상태인지 검사합니다. 파괴적 변경은 expand-contract, forward fix, replay와 [REL-001](../rules/reliability/REL-001.md)의 restore evidence를 조합합니다.

Migration framework, DB-native script, 작은 project-owned runner 또는 delegated operator 절차는 모두 이 계약의 구현 후보입니다. 제품, 파일 이름 규칙, engine별 lock 명령, 저장소 경로와 운영 UI는 프로젝트의 별도 결정이며 공통 정책을 바꾸지 않습니다.
