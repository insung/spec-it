---
id: DATA-007
title: Govern stored routines as deployable code
status: active
introduced: 0.2.0
scope: stored-database-routines
condition: "A project introduces or changes stored procedures, functions, or triggers used by the product."
statement: "MUST justify stored execution and manage the routine definition, ownership, verification, compatibility, and deployment as versioned code."
forbidden: ["Keep the only authoritative definition in a live database.", "Move domain decisions into routines merely because a transaction is required.", "Maintain competing application and SQL implementations as business-policy authorities.", "Assume routine DDL or data changes can always be rolled back."]
evidence: ["ADR records set-based execution, measured benefit, restricted DB access, or legacy compatibility rationale and revisit trigger.", "Versioned SQL, caller inventory, change reviewers, deployment identity, and effective DB privileges are recorded.", "Target-engine tests and migration rehearsal cover results, failure, concurrency, old/new callers, and recovery."]
exception: {allowed: true, requirements: ["Architecture-owner and data-owner approval with impact and expiry or review trigger under GOV-003.", "An emergency change has an incident reference and a deadline to reconcile live state with the versioned source."]}
approver: [architecture-owner, data-owner]
rationale: "Stored execution can be efficient while remaining reviewable, reproducible, and accountable."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# DATA-007 — Stored-routine boundary

0.2.0에 도입되었습니다. 기본 업무 판단은 [ARCH-001](../architecture/ARCH-001.md)에 따라 도메인 코드가 소유합니다. SQL은 조회·조인·대량 집계·일괄 갱신에 사용할 수 있습니다. 프로시저 도입은 다음 중 해당 근거를 ADR에 남깁니다.

1. 집합 연산이나 왕복 감소의 성능·총비용 이점을 대표 데이터에서 측정했습니다.
2. 테이블 직접 접근 대신 제한된 실행 권한을 제공하는 DB 인터페이스가 필요합니다.
3. 기존 호출자와의 호환을 유지해야 하고 전환 범위·재검토 조건이 정해졌습니다.

핵심 업무 판단을 DB에 남기는 것은 별도 [ARCH-001 예외](../architecture/ARCH-001.md)입니다. 판단의 단일 정본과 수용 사례를 지정하고 애플리케이션에 같은 판단을 복제하지 않습니다. DB의 UNIQUE·FK·CHECK 등 무결성 제약은 제거 대상이 아닙니다.

## 변경과 배포

프로시저 정의 SQL과 migration 이력을 Git에서 관리합니다. 업무 의미 승인자, 코드/DB 검토자, 배포 주체를 기록하되 작은 프로젝트는 겸임할 수 있습니다. 개발자 개인 계정에 종속된 definer·권한도 운영 전 검토합니다. CI 계정에 무제한 권한을 주는 것을 의미하지 않습니다.

새 설치와 기존 버전 업그레이드를 목표 DB 엔진/버전에서 검사합니다. 본문과 인수·결과의 계약을 함께 검토하고 [ARCH-005](../architecture/ARCH-005.md)의 트랜잭션 소유권, [COMP-001](../compatibility/COMP-001.md)의 구·신 호출자 호환과 복구 계획을 연결합니다. 운영 직접 수정은 정상 배포 경로가 아니며, 승인된 긴급 절차 이후 정본과 운영 정의를 대조합니다.

## 예와 검증

대량 집계 프로시저를 보존하면서 호출 adapter와 수용 테스트를 추가하는 것은 가능합니다. 단순 권한 분기를 테스트 없이 프로시저로 옮기는 것은 허용 근거가 아닙니다. 프로시저를 사용하지 않는 프로젝트는 그 사실을 확인하고 `not-applicable`로 분류합니다. 정의를 확보하지 못한 레거시는 준수로 처리하지 않습니다.

자료: [SQL migrations](https://documentation.red-gate.com/fd/migrations-271585107.html), [MySQL implicit commit](https://dev.mysql.com/doc/refman/8.4/en/implicit-commit.html). 도구는 프로젝트가 선택합니다. 자동 검증은 미구현이며 Phase 0 판정은 `human-review`입니다.
