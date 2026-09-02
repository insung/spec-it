---
id: PROJ-003
title: Monorepo common and unit manifests
status: active
introduced: 0.1.0
scope: monorepos
condition: "A repository contains multiple independent deploy units."
statement: "MUST keep shared policy selection in the root manifest and declare only differences in each unit manifest."
forbidden: ["Duplicate the complete root manifest in every unit.", "Use deploy branches as environment configuration."]
evidence: ["Resolved lock identifies root inheritance and unit differences."]
exception: {allowed: true, requirements: ["Unit isolation reason and duplicate-maintenance impact."]}
approver: [architecture-owner]
rationale: "Difference-only unit manifests keep shared policy consistent without hiding deploy autonomy."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# PROJ-003 — Monorepo manifests

이 규칙은 모노레포에만 적용됩니다.
