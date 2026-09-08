---
id: COMP-002
title: Consumer-specific shared library updates
status: active
introduced: 0.2.0
scope: shared-domain-library-releases
condition: "A shared domain library release changes behavior, contract, security, data handling, or support state for one or more consumers."
statement: "MUST publish release impact and assess each known consumer as update-required, update-planned, not-required, or impact-unknown with evidence, owner, risk-based due condition, pinned version, and deployed-version verification."
forbidden: ["Require every consumer to update only because a release exists.", "Mark a consumer unaffected solely because signatures did not change.", "Treat a merged dependency update as deployed or verified.", "Silently float a core domain dependency to an unreviewed version."]
evidence: ["Library release record identifies changed capabilities, behavior, compatibility, migration, and support impact.", "Consumer assessment links use evidence, lock or artifact identity, tests, owner, due condition, and observed deployment version."]
exception: {allowed: true, requirements: ["Approved temporary mitigation, risk, expiry or review trigger, and supported-version status under GOV-003."]}
approver: [intent-owner, architecture-owner, security-owner]
rationale: "A shared package only reduces duplication when its behavioral changes and actual deployed consumers remain observable."
origin: {type: design-interview}
enforcement: {mode: ci, implementation: planned}
---

# COMP-002 — Shared core consumer impact

0.2.0에 도입되었습니다. SemVer는 공개 계약을 전달하지만 개별 consumer의 사용 여부와 배포 시점을 대신 판단하지 않습니다. 보안·데이터 손상·잘못된 계산은 위험도에 따라 기한을 정하고, 사용하지 않는 추가 기능은 지원 중인 고정 버전을 유지할 수 있습니다. 판단 근거가 없으면 `impact-unknown`이지 `not-required`가 아닙니다.

상태는 최소한 `observed → assessed → update-planned → merged → deployed → verified`를 구분합니다. 실제 도구는 프로젝트의 패키지 저장소·Git·CI/CD가 정해진 뒤 선택합니다. Phase 0는 템플릿과 `human-review`만 제공합니다.
