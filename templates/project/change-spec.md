---
id: 20260101-short-slug
scope: change
status: draft
owners:
  - intent-owner
created_on: "2026-01-01"
affects:
  - behavior
---

# Why

<Problem and affected users>

# Observable outcome

<What changes from the user's perspective>

# Read-back and source

AI가 조사 후 채우고 사람은 중요한 해석 차이만 확인합니다. 모든 항목을 사전 설문으로 요구하지 않습니다. 기존 기획 도구의 원본을 이 문서로 대체하거나 복사할 필요는 없습니다.

- 원본/section·revision 또는 허용된 snapshot: <의도/디자인/계약별 정본>
- 승인 근거·결정자 / 마지막 관측 시각: <승인과 관측을 구별; 미확인은 unknown>
- 이해한 대상·범위·적용 시점: <사용자에게 보이는 결과로 되읽기>
- 정상 예시 / 반례 / 유지할 동작: <다른 해석을 구별할 구체적 사례>
- 정정·충돌·가설: <이전 해석과 변경된 시나리오; 회고를 확정 원인으로 쓰지 않음>

# Success and acceptance

- Measure: <threshold>
- Given/when/then: <acceptance criterion>

| 원본 의도 | Scenario / 적용 유형·경로 | 예상 관찰 | 검증 계획/실행 근거 | 미결정·미접근·후속 |
| --- | --- | --- | --- | --- |
| <locator/section> | <ID, applies/excluded/open/unknown과 사유> | <화면/로직/DB 등 관측> | <계획은 실행 통과가 아님; 외부 QA 참조 가능> | <소유자·재개 조건> |

작은 변경은 한 행이면 충분합니다. 필요할 때만 [영향 기록](change-impact.md), [사례](../testing/acceptance-case.md), [실행](../testing/verification-run.md)의 항목을 재사용합니다. 행 수나 반복 검토 횟수는 원문 완전성의 증명이 아닙니다.

# Constraints and non-goals

- Constraint: <hard boundary>
- Non-goal: <excluded work>

# Cost and rollback

- Total cost assumption: <money, time, operations, failure>
- Rollback boundary: <safe reversal>

# Decisions

재개 시 원본 revision·commit/dirty·관계·접근 권한 변화를 확인할 위치와 조건을 남깁니다. late-entry라면 이미 변경한 범위, 실제 시작 기준과 누락된 사전 증거를 기록하며 과거 승인/TDD로 소급하지 않습니다.

| Decision | Category | Status | Owner | Evidence |
| --- | --- | --- | --- | --- |
| <question> | behavior | open | intent-owner | <link> |
