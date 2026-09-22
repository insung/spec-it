---
id: CODE-006
title: Comments do not duplicate externally owned mutable facts
status: active
introduced: 0.6.0
scope: source-code-comments-and-docstrings
condition: "A source comment or docstring refers to a fact whose authoritative value or location is owned outside that source artifact and can change independently."
statement: "MUST identify the durable authority or semantic reason and MUST NOT maintain an independently edited literal copy that can become stale without a corresponding code change."
forbidden: ["Copy a mutable price, ratio, limit, version, or policy value from another authority into a hand-maintained comment.", "Use a section number or other unstable document location as the only link to the authoritative decision.", "Present an external fact as current without a version, derivation, or review trigger when the code does not enforce it."]
evidence: ["Comment review identifies the authority and shows that any retained value is generated, version-pinned, or an invariant that must change with the code."]
exception: {allowed: true, requirements: ["The text is generated from the same authority, records immutable version-specific evidence, or explains an invariant whose change necessarily requires the adjacent code to change; the boundary is evident or recorded."]}
approver: [architecture-owner]
rationale: "Comments stay trustworthy when independently changing facts have one authority and source text preserves only durable reasons or verifiable references."
origin: {type: design-interview}
enforcement: {mode: manual, implementation: implemented}
---

# CODE-006 — No hand-maintained external fact copies

주석은 외부 사실의 두 번째 정본이 아닙니다. 외부 가격표, 운영 정책, 문서 목차처럼 코드와 독립적으로 바뀌는 사실은 안정된 문서 ID·결정 ID·계약 위치를 가리키고, 코드에 필요한 의미와 제약을 설명합니다. 현재 숫자나 절 번호를 다시 적는 것만으로는 정본 연결이 되지 않습니다.

반대로 protocol version처럼 코드 분기와 함께 바뀌어야 하는 상수의 의미, 생성된 주석, 특정 release를 분석한 불변 증거까지 금지하지 않습니다. 중요한 경계는 그 문장이 코드 수정 없이 낡을 수 있는 독립 편집 사본인지입니다.
