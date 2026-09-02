---
id: DATA-003
title: Redis stores derived or temporary state
status: active
introduced: 0.1.0
scope: cache-and-ephemeral-state
condition: "Redis is used."
statement: "MUST keep recoverable, derived, cache, lock, rate-limit, or explicitly temporary state with loss and staleness policy."
forbidden: ["Use Redis as the only copy of durable business truth without an approved exception."]
evidence: ["Data inventory states source of truth, TTL, eviction, recovery, and stale tolerance."]
exception: {allowed: true, requirements: ["Durability design, backup, restore test, and data-owner approval."]}
approver: [data-owner, architecture-owner]
rationale: "Redis cost and eviction behavior are safest when durable truth exists elsewhere."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# DATA-003 — Redis data boundary

메모리 사용량, eviction, hit ratio와 latency는 부하·비용 측정에 포함합니다.
