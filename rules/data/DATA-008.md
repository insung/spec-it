---
id: DATA-008
title: Compact physical storage only with evidence
status: active
introduced: 0.2.0
scope: cost-sensitive-physical-storage
condition: "A project proposes abbreviated field names or a compact physical representation for Redis or another cost-sensitive store."
statement: "MUST first remove unnecessary fields, bound cardinality and lifetime, choose an appropriate data structure or encoding, measure the resulting cost, and version a tested mapping before abbreviating the physical schema."
forbidden: ["Abbreviate domain, public API, event, or application contract names to save storage bytes.", "Introduce an undocumented compact mapping.", "Assume shorter field names reduce total cost without measuring memory, serialization, compatibility, and operations impact."]
evidence: ["Before-and-after measurement, versioned serializer mapping, compatibility tests, rollback path, and total-cost comparison."]
exception: {allowed: true, requirements: ["Externally fixed binary schema or protocol with equivalent versioning, compatibility, and measurement evidence."]}
approver: [data-owner, architecture-owner]
rationale: "Physical compaction is worthwhile only when measured savings exceed the compatibility and maintenance cost it creates."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# DATA-008 — Evidence-based storage compaction

축약은 마지막 수단입니다. 먼저 저장하지 않아도 되는 값, TTL, key cardinality, 중복, 자료구조와 encoding을 검토합니다. 축약을 선택해도 domain과 외부 계약은 의미 있는 이름을 유지하고 storage adapter가 명시적으로 변환합니다.
