---
id: TOOL-002
title: Deterministic resolved lock
status: active
introduced: 0.1.0
scope: project-projection
condition: "A manifest is converged into lock.yaml."
statement: "MUST resolve the selected policy source and released version to an immutable content digest, record the source revision when available, and generate byte-identical lock output from the same resolved policy and manifest input."
forbidden: ["Resolve an accepted project lock from an unpublished version label alone.", "Include timestamps or machine-specific paths.", "Hand-edit generated lock content."]
evidence: ["Lock records policy source, released version, canonical policy digest, optional source revision, manifest digest, and generated marker.", "Repeat resolution of the same policy and manifest produces byte-identical output."]
exception: {allowed: false, requirements: []}
approver: [architecture-owner]
rationale: "Determinism makes policy resolution reviewable and reproducible across agents."
origin: {type: design-interview}
enforcement: {mode: validator, implementation: planned}
---

# TOOL-002 — Deterministic lock

정렬과 serialization 규칙은 Phase 1 generator에서 고정합니다. Phase 0 fixture는 그 목표 형식을 보여주며 실제 재생성은 `human-review`입니다.

`policy_digest`는 `VERSION`과 `rules/`, `profiles/`, `schemas/` 아래 regular file을 repository-relative POSIX path로 정렬한 뒤, 각 파일마다 UTF-8 path, NUL byte, file bytes, NUL byte를 이어 붙인 값의 SHA-256입니다. Git 배포는 해석한 commit을 `policy.revision`에도 기록합니다. 정책 저장소 자체의 미발행 worktree는 draft 증거일 뿐 외부 프로젝트의 승인된 lock source가 아닙니다.
