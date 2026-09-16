# Roadmap and completion

## Phase 0 — policy source

- 문서, 한 규칙 한 파일, 프로필, 스키마, 템플릿, instruction-only 스킬
- 예제 fixture와 실패·충돌 사례
- 공개 운영 문서와 저장소 자체 투영
- 애플리케이션 코드와 실행 validator는 없음

`0.1.0` 완료 판정은 [phase-0 checklist](phase-0-checklist.md), 이후 릴리스의 증분 판정은 각 release checklist([0.2.0](releases/0.2.0-checklist.md), [0.3.0](releases/0.3.0-checklist.md), [0.4.0](releases/0.4.0-checklist.md), [0.5.0](releases/0.5.0-checklist.md))를 사용합니다.

## Phase 1 — minimal tooling

- schema validation, rule resolution, deterministic lock generation
- quick/full/release check와 JSON report
- secret redaction과 종료 코드

## Phase 2 — project pilot

- 실제 Python backend 또는 Lambda/SAM 프로젝트 한 곳에 적용
- false positive, 누락, 사람 개입 비용 측정
- 반복 실패만 validator 후보로 승격

## Phase 3 — enforcement and overlays

- 안정된 규칙의 CI 승격
- language-specific validator
- 비공개 개인·회사 overlay
- 필요가 입증된 AI·frontend·embedded profile
