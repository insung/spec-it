---
id: RULE-002
title: Separate enforcement target from implementation state
status: active
introduced: 0.1.0
scope: policy-rules
condition: "A rule declares enforcement."
statement: "MUST declare mode as manual, validator, ci, or runtime and implementation as planned, advisory, or implemented."
forbidden: ["Report an unimplemented target as passing enforcement.", "Omit implementation state."]
evidence: ["Rule front matter validates against rule-frontmatter.schema.json."]
exception: {allowed: false, requirements: []}
approver: [architecture-owner]
rationale: "Target and reality must be distinct so policy maturity is not overstated."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# RULE-002 — Honest enforcement state

Phase 0의 planned 검사는 `human-review` 또는 `not-implemented` 설명으로 드러냅니다.
