# 최종 후보 disposition 독립 감사

## 범위와 한계

`review/user-requests.md`의 사용자 요구와 후보 `source/`의 관련 지침·schema·템플릿만 정적으로 대조했다. 이는 지침의 표현과 상호 일관성 감사일 뿐, agent의 실제 행동·자동 스킬 선택·원문 전체 무누락 감사·실제 QA 실행이나 자동화 완료의 증명이 아니다.

## 판정

### 1. 고정 `rule_id` 보고서와 규칙 밖 의도·QA 관찰의 지속 기록 경계 — resolved

- `schemas/check-report.schema.json`은 각 `results` 항목에 고정 형식의 `rule_id`를 필수로 요구한다.
- `skills/spec-it-check/SKILL.md`는 persisted check report를 적용된 pinned rule ID에 연결된 finding만으로 한정하고, advisory intent/QA/impact/source-freshness 관찰에는 rule ID를 발명하거나 비모델 필드를 추가하지 못하게 한다.
- 같은 지침은 지속 보관을 원할 때에도 이미 승인된 change/issue/handoff 기록과 명시된 위치·쓰기 범위를 별도 조건으로 요구하며, 그렇지 않으면 응답에만 남기고 누락된 owner/location을 밝히게 한다. `docs/intent-and-verification.md`도 Change/Scenario ID와 기존 변경 기록·QA 도구를 연결 대상으로 제시하고, connector·통합 UI가 아니라고 한정한다.

따라서 정책 compliance JSON과 규칙 밖의 관찰 이력은 같은 파일·가짜 rule ID로 섞이지 않으며, 후자의 보존은 명시적으로 승인된 별도 기록에만 가능하다.

### 2. 승인·위임 결정을 clarify 종료에서 재승인 대기로 되돌리는 모순 — resolved

- `skills/spec-it-clarify/SKILL.md`는 유효한 위임 범위에서는 질문을 중단하고, 종료 시 `pending human confirmation`을 미승인·미위임 선택에만 쓰도록 한다.
- `skills/spec-it-converge/SKILL.md`는 이미 남은 선택을 명시된 추천에 위임했으면 추가 human confirmation을 요구하지 않는다.
- intent/design revision, dirty state, new consumer, stale discovery 같은 변화가 생긴 경우에도 converge는 영향 기록을 갱신하고 **새로운** material choice만 clarify로 보내도록 제한한다. 이는 기존 승인/위임을 무효화하지 않고, 그 근거가 더 이상 현재 범위를 덮지 않는 경우만 새 판단으로 분리한다.

### 3. QA 폴더·도구·규칙의 전 프로젝트 강제 및 자동화 완료 과장 — resolved

- `docs/intent-and-verification.md`는 절차를 선택적이라고 명시하고, QA sheet는 기존 문서 DB·스프레드시트·이슈·별도 QA 저장소 중 프로젝트가 쓰는 위치에 둘 수 있다고 한다.
- `templates/README.md`, `templates/testing/acceptance-case.md`, `templates/testing/verification-run.md`은 새 schema·공통 필수 폴더가 아니며 구현 저장소의 QA 코드도 필요 없다고 반복한다.
- `skills/spec-it-converge/SKILL.md`는 QA folder/case schema/external tool migration을 수렴 전제조건으로 만들지 못하게 하고, watcher·QA runner·hook 설치를 묵시적 projection으로 하지 못하게 한다.
- `README.md`, `docs/enforcement-lifecycle.md`, `skills/spec-it-check/SKILL.md`은 Phase 0에 executable validator/report generator가 없고 planned 또는 미구현 검사는 pass가 아니며 실제 exit code도 실행된 checker 없이는 주장하지 못한다고 한정한다.

따라서 후보는 QA 기록의 연결 방식을 제공하지만 저장 위치·도구·폴더·자동 실행을 보편 의무나 구현 완료로 표현하지 않는다.

## 새 P1/P2 직접 발견

없음. 위 결론은 후보의 정적 지침 문구에 대한 것이며, 실제 적용에서 별도 기록 위치의 승인·쓰기 권한과 관찰 증거가 부재하면 그대로 `human-review` 또는 미확정으로 남아야 한다.
