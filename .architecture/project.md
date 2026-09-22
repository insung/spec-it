# spec-it project

## Purpose

사람이 의도와 위험을 소유하고 AI가 버전 고정된 규칙과 증거를 사용해 일관되게 구현하도록 하는 공개 가능한 정책 SSOT를 제공한다.

## Users and outcomes

- 개인 개발자는 재사용 가능한 기본 아키텍처를 프로젝트에 투영한다.
- 프로젝트 책임자는 선택·예외·승격의 근거를 Git에서 검토한다.
- AI agent는 짧은 `AGENTS.md`, manifest, lock을 통해 적용 규칙을 동일하게 해석한다.

## Success measures

- 규칙은 하나의 정본 파일과 안정된 ID를 갖는다.
- 프로젝트 조합은 평평한 프로필과 정확한 정책 버전으로 재현된다.
- 미구현 강제는 통과로 표시되지 않는다.
- 공개 core에는 개인·회사 비공개 정보가 없다.

## Boundaries

- Phase 1 진입: Phase 0 정책 source와 instruction-only 스킬에 더해, 명시적으로 활성화한 Claude 프로젝트에서만 동작하는 active policy loop를 제공한다.
- 현재 범위 밖: 범용 schema validator, deterministic lock generator, CI 강제, package/plugin 배포, Codex adapter, 회사 overlay.

## Owners

한 maintainer가 현재 단계의 `intent-owner`, `architecture-owner`, `security-owner`, `data-owner`, `operations-owner` 역할을 겸할 수 있다.
