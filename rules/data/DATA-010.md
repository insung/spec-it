---
id: DATA-010
title: Declare owned database identifier conventions
status: active
introduced: 0.4.0
scope: relational-database-identifiers
condition: "A project adds or changes a project-owned relational database schema, table, column, constraint, index, view, or routine identifier."
statement: "MUST declare the naming convention for each project-owned database identifier category, apply it consistently within the approved ownership boundary, and preserve externally owned identifiers at integration boundaries."
forbidden: ["Mix undeclared casing conventions within one owned database contract.", "Rename a legacy or externally owned database identifier only to satisfy local style without compatibility and migration evidence.", "Assume source-code or HTTP field naming automatically governs physical database identifiers."]
evidence: ["Manifest parameters or a linked database contract name the owned identifier categories, conventions, ownership boundary, legacy treatment, and externally owned behavior.", "DDL or migration review and integration tests cover new names, mappings, quoted-identifier requirements, and compatibility with existing consumers."]
exception: {allowed: true, requirements: ["Data-owner and architecture-owner approve the bounded legacy or external contract, mapping strategy, compatibility impact, and revisit trigger under GOV-003."]}
approver: [data-owner, architecture-owner]
rationale: "Explicit ownership and naming boundaries prevent accidental casing drift without rewriting external or legacy schemas."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# DATA-010 — Database identifier conventions

공통 정책은 모든 database engine에 하나의 casing을 강제하지 않습니다. 프로젝트는 새로 소유하는 schema, table, column, constraint, index, view와 routine identifier의 convention을 정하고, engine의 case folding과 quoted identifier 동작을 함께 검토합니다. 같은 convention을 여러 category에 쓸 수 있지만 명시적으로 기록합니다.

legacy 또는 외부 소유 schema를 호출할 때는 그 identifier를 그대로 유지하고 storage adapter나 query mapping에서 project-owned 이름과 연결합니다. 기존 identifier를 바꾸려면 단순 style 정리가 아니라 versioned migration, 구·신 consumer compatibility, rollback 또는 forward-fix와 운영 증거가 필요합니다. 자동 검증은 미구현이며 Phase 0 판정은 `human-review`입니다.
