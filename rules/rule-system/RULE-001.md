---
id: RULE-001
title: Immutable rule identity and single canonical file
status: active
introduced: 0.1.0
scope: policy-repository
condition: "A rule is created, changed, deprecated, or removed."
statement: "MUST keep one rule ID in one Markdown file with YAML front matter and never reuse or silently redefine a published ID."
forbidden: ["Maintain a second hand-edited canonical rule catalog.", "Reuse removed IDs."]
evidence: ["Unique ID scan and lifecycle metadata."]
exception: {allowed: false, requirements: []}
approver: [architecture-owner]
rationale: "Stable identity and one source prevent incompatible agents from resolving different rule copies."
origin: {type: design-interview}
enforcement: {mode: ci, implementation: planned}
---

# RULE-001 — One rule, one file

색인은 링크만 보유하고 생성 catalog는 개별 규칙 파일에서 만들어집니다.
