---
id: ARCH-005
title: Explicit transaction and follow-up ownership
status: active
introduced: 0.2.0
scope: state-changing-use-cases
condition: "A use case changes persistent state or schedules a consequential follow-up."
statement: "MUST name one transaction owner and define atomicity, concurrency, failure, and follow-up delivery boundaries independently of user-facing messages."
forbidden: ["Assume a stored procedure call is automatically atomic.", "Commit inside an adapter or procedure when the application owns the transaction.", "Use log text or translated messages to trigger business actions.", "Treat an external delivery as atomic with a local database commit without a delivery mechanism."]
evidence: ["Use-case decision names the transaction owner, participating resources, concurrency strategy, and commit/rollback boundary.", "Tests cover partial failure, competing requests, duplicate requests, and follow-up failure where applicable.", "Required external delivery has durable intent, retry, deduplication, and recovery evidence."]
exception: {allowed: true, requirements: ["Architecture-owner approval with scope, impact, evidence, and expiry or review trigger under GOV-003."]}
approver: [architecture-owner, data-owner]
rationale: "Atomicity and recovery depend on explicit resource boundaries rather than the location or language of the code."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# ARCH-005 — Transaction ownership

0.2.0에 도입되었습니다. 0.1.0에 고정된 프로젝트에는 자동 적용되지 않습니다.

업무 판단은 [ARCH-001](ARCH-001.md)의 도메인 경계를 따릅니다. 애플리케이션은 트랜잭션을 조율하고 adapter가 같은 연결에서 DB 연산을 수행하는 것이 기본입니다. 기존 프로시저가 트랜잭션을 소유하는 경우 호출 계약에 명시하고 애플리케이션에서 중첩 트랜잭션처럼 취급하지 않습니다.

## 결정할 경계

- 단일 DB 트랜잭션인지, 원자적으로 묶을 수 없는 외부 API·다른 저장소가 있는지 구분합니다. 트랜잭션 지원 엔진과 같은 연결을 확인합니다.
- 동시 요청에는 DB 제약조건·조건부 갱신·잠금·격리 수준 중 선택한 방법과 충돌 시 결과를 기록합니다. 트랜잭션 선언만으로 동시성 안전을 주장하지 않습니다.
- 요청 시간 초과 후에는 실패와 결과 미확인을 구분합니다. 결제·생성 등 중복 실행 위험이 있는 작업은 결과 조회 또는 멱등성 보장 없이 자동 재시도하지 않습니다.
- 커밋 뒤의 선택적 알림 실패와 본 작업 실패를 구분합니다. 유실이 허용되지 않는 후속 작업은 durable intent와 재시도·중복 처리 정책을 둡니다. 같은 DB의 outbox는 선택지이며 모든 프로젝트의 필수 인프라가 아닙니다.

## 예와 검증

주문·재고 갱신은 동일 트랜잭션, 배송 요청은 내구성 있는 작업 기록을 함께 커밋하고 별도 전달하는 예가 가능합니다. 전달 성공을 DB 커밋 성공과 같은 것으로 보지 않습니다. 읽기 전용 작업으로 후속 효과도 없으면 근거와 함께 `not-applicable`입니다.

자료: [MySQL transaction control](https://dev.mysql.com/doc/refman/8.4/en/commit.html), [Transactional outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html). 본 규칙은 설계 선택이며 이 자료가 모든 프로젝트에 특정 도구를 요구한다는 뜻은 아닙니다. 자동 검증은 미구현이며 Phase 0 판정은 `human-review`입니다.
