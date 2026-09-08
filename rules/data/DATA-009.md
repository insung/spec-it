---
id: DATA-009
title: Govern database changes as release units
status: active
introduced: 0.3.0
scope: database-change-delivery
condition: "A project authors, requests, or applies a database schema, stored-routine, reference-data, or backfill change."
statement: "MUST manage each database change as a versioned, checksummed, ordered release unit with object ownership, application compatibility, single-executor coordination, environment evidence, post-apply verification, and an explicit recovery class."
forbidden: ["Keep the only authoritative change or current definition in a live database, transient ticket, or operator workstation.", "Use every application instance's startup path as the normal executor for shared database DDL.", "Change an approved migration without invalidating its checksum and approval.", "Apply migrations without a history record and a database lock or equivalent serialization.", "Promote an application artifact to a database state outside its declared compatibility range.", "Promise automatic rollback for every DDL or data change."]
evidence: ["The release manifest or immutable bundle links source repository, revision, path, checksum, target engine and database, owned objects, execution order, application artifact identities, and compatibility range.", "Per-environment records identify approval target, executor or delegated operator, start and end time, result, lock outcome, dry run or rehearsal, and post-apply verification.", "Each change is classified as reversible, expand-contract or forward-fix, replayable data change, or restore-dependent, with stop conditions and tested recovery evidence appropriate to its effects."]
exception: {allowed: true, requirements: ["Data-owner and architecture-owner approval records scope, impact, alternative controls, and expiry or review trigger under GOV-003.", "An emergency change has an incident reference, captured executed SQL and result, and a deadline to reconcile the live definition with versioned source and history."]}
approver: [data-owner, architecture-owner]
rationale: "A database change is safely deployable only when its exact content, ownership, compatible consumers, execution, and recovery remain traceable across environments."
origin: {type: design-interview}
enforcement: {mode: ci, implementation: planned}
---

# DATA-009 — Database change delivery

0.3.0에 도입되었습니다. SQL 정본의 위치와 실행 도구를 고정하지 않고, 변경이 어느 저장소에서 왔든 한 릴리즈의 적용 대상과 결과를 재현할 수 있게 합니다. 객체 소유 저장소, DB 또는 schema 저장소, 중앙 DB 저장소를 선택할 수 있으며, 여러 저장소가 참여하면 중앙 release manifest 또는 같은 역할의 immutable bundle이 전체 순서와 artifact identity를 연결합니다. 객체를 호출한다는 이유만으로 그 객체의 정본을 복제하지 않습니다.

## 실행 경계

배포 pipeline의 단일 작업이 필요한 권한으로 migration을 실행하는 것이 기본입니다. 각 애플리케이션 인스턴스는 시작할 때 DDL을 직접 실행하지 않습니다. 시작 또는 readiness 단계의 읽기 전용 DB version·capability 검사는 가능한 방어 수단이지만 모든 프로젝트의 고정 구현은 아닙니다. 배포 전 호환성 gate, traffic 전환 조건 또는 runtime check 중 프로젝트 topology에 맞는 방법을 선택합니다.

DB 권한이나 책임 분리 때문에 pipeline이 직접 실행하지 못하는 대상은 같은 릴리즈에서 제외하지 않습니다. 시스템이 checksum이 고정된 실행 요청, 순서, 승인 범위, 검증과 복구 자료를 만들고 권한 있는 operator가 실행한 뒤 결과를 같은 environment history에 기록하는 delegated lane으로 다룹니다. 수동 실행은 감사 밖 우회 경로가 아닙니다.

## 변경과 복구 분류

분류는 `ALTER`, `DROP`, `UPDATE` 같은 SQL keyword만으로 결정하지 않고 이미 기록된 데이터, 구·신 애플리케이션, lock 시간과 운영 부하에 미치는 효과로 정합니다.

- **reversible**: 검증된 되돌리기 작업이 현재 데이터를 손상하지 않고 이전 호환 상태를 복원합니다.
- **expand-contract or forward-fix**: 구·신 호출자를 함께 지원하도록 확장한 뒤 별도 릴리즈에서 정리하거나, 되돌리기보다 다음 수정이 안전합니다.
- **replayable data change**: 대상 범위, checkpoint, 멱등성 또는 deduplication이 있어 중단·재개하거나 다시 계산할 수 있습니다.
- **restore-dependent**: 파괴적 효과를 논리적으로 되돌릴 수 없어 승인된 backup·PITR와 restore rehearsal에 의존합니다.

NULL 허용 column 추가도 새 데이터가 쓰인 뒤 column을 제거하면 파괴적일 수 있습니다. 대형 index 생성은 반드시 데이터 파괴는 아니지만 lock·부하·실행 시간의 별도 운영 위험을 가집니다. tablespace와 online DDL 같은 engine-specific 절차는 공통 분류를 만족한 뒤 프로젝트 runbook에서 구체화합니다.

## 연결 규칙

[DATA-007](DATA-007.md)은 stored routine을 deployable code로 관리하고, [COMP-001](../compatibility/COMP-001.md)은 구·신 소비자 호환을, [ARCH-005](../architecture/ARCH-005.md)은 동시성·부분 실패를, [REL-001](../reliability/REL-001.md)은 restore evidence를, [CICD-001](../ci-cd/CICD-001.md)은 동일 artifact 승격을 정의합니다. DATA-009는 이 증거를 하나의 DB release unit과 environment history로 연결합니다.

자료: [Flyway migrations](https://documentation.red-gate.com/flyway/flyway-concepts/migrations), [Flyway schema history](https://documentation.red-gate.com/flyway/flyway-concepts/migrations/flyway-schema-history-table), [MySQL implicit commit](https://dev.mysql.com/doc/refman/8.4/en/implicit-commit.html). 특정 도구나 application-startup 실행을 요구하지 않습니다. 자동 검증은 미구현이며 Phase 0 판정은 `human-review`입니다.
