---
id: TOOL-005
title: Executable source declares a lint contract
status: active
introduced: 0.2.0
scope: executable-source-projects
condition: "A deploy unit contains project-owned executable source code."
statement: "MUST declare and run a language-appropriate formatter, linter or static analyzer, relevant type checker, pinned configuration, source scope, local command, and CI target state."
forbidden: ["Claim coding-convention compliance from prose review alone when a mature tool can check it.", "Silently use an agent's personal global configuration.", "Fail adoption solely because a language lacks a mature linter without offering an approved alternative evidence path."]
evidence: ["Manifest or project guidance names tool versions or lock source, configuration, commands, scope, and current enforcement state."]
exception: {allowed: true, requirements: ["Mature tooling is unavailable or disproportionate, alternative review or compiler evidence is recorded, and architecture-owner approves a revisit trigger."]}
approver: [architecture-owner]
rationale: "A repository-owned lint contract gives humans and different agents the same inexpensive baseline without inventing a universal toolchain."
origin: {type: design-interview}
enforcement: {mode: ci, implementation: planned}
---

# TOOL-005 — Language-owned lint contract

공통 정책은 모든 언어에 같은 linter를 강요하지 않습니다. language profile이 공식 formatter와 생태계의 성숙한 도구를 선택하고, 프로젝트는 실행 명령과 범위를 고정합니다. Python reference profile은 Ruff를 기본 formatter·linter로 사용합니다. type checker는 프로젝트 위험과 실제 타입 전략에 맞게 선택합니다.
