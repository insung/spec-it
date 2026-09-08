# Phase 0 checklist

이 문서는 공개 정책 `0.1.0`이 Phase 0을 종료할 때 사용한 저장소 수준의 완료 증거다. 개별 프로젝트의 준수 체크리스트나 이후 릴리스의 합격 판정이 아니다.

## 적용 범위

- 대상: Git에 고정된 `0.1.0` 정책 기준선
- 의미: 문서·규칙·프로필·스키마·템플릿·instruction-only 스킬의 구조와 연결이 Phase 0 완료 조건을 충족함
- 제외: 애플리케이션 동작 준수, 실행 validator, CI 강제, runtime enforcement
- 후속 릴리스: `0.2.0`과 `0.3.0`은 각각의 release checklist([0.2.0](releases/0.2.0-checklist.md), [0.3.0](releases/0.3.0-checklist.md))를 사용함

- [x] 모든 합의가 규칙 ID 또는 명시 문서에 연결되어 있다.
- [x] 각 규칙에 scope, condition, normative statement, forbidden, evidence, exception, approver, example이 있다.
- [x] 각 규칙에 enforcement mode와 implementation 상태가 있다.
- [x] 규칙 front matter, profile, manifest, unit manifest, lock, ADR, change spec, check report, exception, external reference schema가 유효하다.
- [x] 초기 profile 조합과 fixture가 schema를 통과한다.
- [x] profile 충돌과 만료 예외가 성공으로 처리되지 않는다.
- [x] 보류 항목마다 재검토 trigger가 있다.
- [x] 링크와 목차가 완전하다.
- [x] 회사·개인 비공개 정보가 없다.
- [x] 애플리케이션 코드와 실행 validator가 없다.
