---
id: DATA-009
title: Govern database changes as release units
status: active
introduced: 0.3.0
scope: database-change-delivery
condition: "A project authors, requests, or applies a database schema, stored-routine, reference-data, or backfill change."
statement: "MUST manage each database change as a versioned, checksummed, ordered release unit with distinct object decision ownership, authoritative definition source, execution responsibility, immutable release identity, application compatibility, serialized execution, environment evidence, post-apply verification, and an explicit recovery class."
forbidden: ["Keep the only authoritative change or current definition in a live database, transient ticket, or operator workstation.", "Treat the repository that stores SQL or the principal that can execute it as the object decision owner without an explicit ownership decision.", "Use every application instance's startup path as the normal executor for shared database DDL.", "Change an approved migration or release definition without invalidating its checksum and approval.", "Add environment execution results in a way that changes the approved release identity they claim to apply.", "Maintain a current-state definition projection beside migration history without declaring its authority and reconciliation method.", "Apply migrations without a history record and a database lock or equivalent serialization.", "Promote an application artifact to a database state outside its declared compatibility range.", "Present a reconstructed historical or emergency record as evidence that pre-apply approval and checks ran.", "Promise automatic rollback for every DDL or data change."]
evidence: ["The release manifest or immutable bundle links the object decision owner, authoritative definition repository, revision and path, executor or delegated lane, checksum, target engine and database, affected objects, execution order, application artifact identities, and compatibility range.", "The approved release definition has an immutable digest, and each per-environment record references that digest while identifying the approval target, executor or delegated operator, start and end time, execution result, lock outcome, dry run or rehearsal, and post-apply verification result.", "When a baseline or other current-state definition projection coexists with migration history, the project declares which artifact is authoritative, how the projection is derived or reviewed, and evidence that it matches the approved release chain before promotion.", "Each change is classified as reversible, expand-contract or forward-fix, replayable data change, or restore-dependent, with stop conditions and tested recovery evidence appropriate to its effects."]
exception: {allowed: true, requirements: ["Data-owner and architecture-owner approval records scope, impact, alternative controls, and expiry or review trigger under GOV-003.", "An emergency or historical change is labeled as reconciliation rather than a normal pre-approved release, has an incident or provenance reference, captures the executed SQL and result, and sets a deadline or condition to reconcile the live definition with versioned source and history."]}
approver: [data-owner, architecture-owner]
rationale: "A database change is safely deployable only when its exact content, ownership, compatible consumers, execution, and recovery remain traceable across environments."
origin: {type: design-interview}
enforcement: {mode: ci, implementation: planned}
---

# DATA-009 — Database change delivery

0.3.0에 도입되었습니다. SQL 정본의 위치와 실행 도구를 고정하지 않고, 변경이 어느 저장소에서 왔든 한 릴리즈의 적용 대상과 결과를 재현할 수 있게 합니다. 객체 소유 저장소, DB 또는 schema 저장소, 중앙 DB 저장소를 선택할 수 있으며, 여러 저장소가 참여하면 중앙 release manifest 또는 같은 역할의 immutable bundle이 전체 순서와 artifact identity를 연결합니다. 객체를 호출한다는 이유만으로 그 객체의 정본을 복제하지 않습니다.

## 소유권과 보관·실행 책임

DB 변경은 다음 세 책임을 구분합니다.

- **object decision owner**: 객체의 업무 의미, 호환성과 변경 승인을 책임집니다.
- **definition authority**: 실행 가능한 현재 정의와 migration 정본을 보관하고 review 가능한 revision을 제공합니다.
- **executor**: 승인된 release identity를 대상 환경에 적용하거나 delegated operator에게 전달합니다.

한 저장소나 사람이 여러 책임을 겸할 수 있지만 겸임 사실을 명시합니다. SQL을 중앙 DB 저장소에 둔다는 이유만으로 그 저장소가 모든 객체의 업무 의미를 소유하지 않으며, 실행 권한이나 definer를 가졌다는 사실도 변경 승인 권한을 증명하지 않습니다. consumer와 writer 목록은 영향을 찾는 자료이고 object decision ownership을 대신하지 않습니다.

## 릴리즈 정의와 환경 증거

승인 대상인 release definition은 SQL 내용·순서·checksum, application compatibility와 recovery class를 묶은 immutable identity를 가집니다. 승인 뒤 내용을 바꾸면 새 digest와 승인이 필요합니다.

QA·운영 등 환경별 history는 자신이 적용한 release digest를 참조하는 별도 증거입니다. 물리적으로 같은 저장소나 시스템에 보관할 수 있지만, 새 환경의 결과를 추가하는 행위가 승인된 release identity를 바꾸면 안 됩니다. SQL 실행 성공, post-apply definition 검증과 전체 release readiness를 구분하며 unresolved consumer compatibility를 단순 `success`로 덮지 않습니다.

`baseline`, desired schema 또는 current-definition snapshot을 함께 둔다면 그 artifact가 독립 정본인지 release history에서 만든 projection인지 선언합니다. projection이면 운영 반영 뒤에만 손으로 맞추는 절차에 의존하지 않고, 승격 전에 이전 상태와 release chain을 적용한 결과가 새 projection과 같은지 생성 또는 review evidence로 확인합니다.

## 실행 경계

배포 pipeline의 단일 작업이 필요한 권한으로 migration을 실행하는 것이 기본입니다. 각 애플리케이션 인스턴스는 시작할 때 DDL을 직접 실행하지 않습니다. 시작 또는 readiness 단계의 읽기 전용 DB version·capability 검사는 가능한 방어 수단이지만 모든 프로젝트의 고정 구현은 아닙니다. 배포 전 호환성 gate, traffic 전환 조건 또는 runtime check 중 프로젝트 topology에 맞는 방법을 선택합니다.

DB 권한이나 책임 분리 때문에 pipeline이 직접 실행하지 못하는 대상은 같은 릴리즈에서 제외하지 않습니다. 시스템이 checksum이 고정된 실행 요청, 순서, 승인 범위, 검증과 복구 자료를 만들고 권한 있는 operator가 실행한 뒤 결과를 같은 environment history에 기록하는 delegated lane으로 다룹니다. 수동 실행은 감사 밖 우회 경로가 아닙니다.

이미 실행된 변경을 뒤늦게 확보하면 SQL과 결과를 버리지 않고 historical 또는 emergency reconciliation record로 남깁니다. 다만 이 기록은 실행 전 checksum·승인·lock·rehearsal을 수행했다는 증거가 아니며, 정상 경로로 전환할 owner와 due condition을 함께 둡니다.

## 변경과 복구 분류

분류는 `ALTER`, `DROP`, `UPDATE` 같은 SQL keyword만으로 결정하지 않고 이미 기록된 데이터, 구·신 애플리케이션, lock 시간과 운영 부하에 미치는 효과로 정합니다.

- **reversible**: 검증된 되돌리기 작업이 현재 데이터를 손상하지 않고 이전 호환 상태를 복원합니다.
- **expand-contract or forward-fix**: 구·신 호출자를 함께 지원하도록 확장한 뒤 별도 릴리즈에서 정리하거나, 되돌리기보다 다음 수정이 안전합니다.
- **replayable data change**: 대상 범위, checkpoint, 멱등성 또는 deduplication이 있어 중단·재개하거나 다시 계산할 수 있습니다.
- **restore-dependent**: 파괴적 효과를 논리적으로 되돌릴 수 없어 승인된 backup·PITR와 restore rehearsal에 의존합니다.

NULL 허용 column 추가도 새 데이터가 쓰인 뒤 column을 제거하면 파괴적일 수 있습니다. 대형 index 생성은 반드시 데이터 파괴는 아니지만 lock·부하·실행 시간의 별도 운영 위험을 가집니다. tablespace와 online DDL 같은 engine-specific 절차는 공통 분류를 만족한 뒤 프로젝트 runbook에서 구체화합니다.

## 연결 규칙

[DATA-007](DATA-007.md)은 stored routine을 deployable code로 관리하고, [COMP-001](../compatibility/COMP-001.md)은 구·신 소비자 호환을, [ARCH-005](../architecture/ARCH-005.md)은 동시성·부분 실패를, [REL-001](../reliability/REL-001.md)은 restore evidence를, [CICD-001](../ci-cd/CICD-001.md)은 동일 artifact 승격을 정의합니다. DATA-009는 이 증거를 하나의 DB release unit과 environment history로 연결합니다.

자료: [MySQL implicit commit](https://dev.mysql.com/doc/refman/8.4/en/implicit-commit.html). 특정 migration 제품, 파일 이름 규칙 또는 application-startup 실행을 요구하지 않습니다. 자동 검증은 미구현이며 Phase 0 판정은 `human-review`입니다.
