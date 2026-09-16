# 변경 영향 기록 — 선택적 시작점

프로젝트가 지속 인계를 선택했을 때 사용하는 형식이다. 공개 schema나 새 의무가 아니며 기존 문서/이슈의 같은 항목으로 대체할 수 있다. 읽기 전용 impact 결과를 저장하는 것은 호출자의 권한이다.

- Change / 활성 명세: <ID와 정본 위치>
- 모드: <preflight / delta / completion / brownfield / late-entry>
- 확인 시각 observed_at: <시간대 포함 시각 또는 미확인 사유>
- 조사자·범위: <root, 파일, 검색/관계 근거, 미조사 영역>
- 이전 → 현재 기준: <commit/snapshot + dirty 내용 식별자; 기준 부재는 unknown>
- 정책: <고정 source/version/revision 또는 미채택 shadow assessment>

## 출처와 관측

| Source / section | 승인 권한·근거 | 관측 revision/snapshot | 확인 시각 | 접근·신선도 한계 |
| --- | --- | --- | --- | --- |
| <원본 locator> | <의도/디자인/계약 담당 승인 또는 open> | <관측값 또는 unknown> | <시간대 포함> | <마지막 확인 이후/접근 불가 등> |

## 영향 관계

| 의도/Scenario | 유형·경로·경계 | 변경/미변경 | 관계 출처 | 상태 | 근거·후속 |
| --- | --- | --- | --- | --- | --- |
| <ID> | <caller → 설정/저장 → 선택 → 관찰> | <changed/unchanged> | <파일/계약 revision> | <applies/excluded/open/unknown> | <제외 근거·결정자 또는 조사 필요> |

관계가 없다는 판단과 접근하지 못했다는 사실을 구분한다. 이전 관계 기록은 힌트이며 완전한 시스템 목록이 아니다.

## 재개와 인계

- 발견한 차이 / 영향받는 결정·시나리오·run: <기존 결과를 덮어쓰지 않고 재검토 대상을 연결>
- 재검토 trigger와 확인 위치: <새 세션, commit/dirty, 기획/디자인/계약 revision, 새 소비자, 접근 권한 변화 중 해당 항목>
- 미결정 / 결정자 / 다음 절차: <중요 차이만 질문, 확인된 범위는 재질문하지 않음>
- late-entry인 경우: <이미 변경한 내용, 실제 시작 기준, 누락된 사전 증거, 사후 재현/회귀 계획>
- 보존/공개 경계: <비밀·원본 복사 제한, 저장 담당자>

관련 실행 안내: [impact](../../skills/spec-it-impact/SKILL.md), [의도와 검증](../../docs/intent-and-verification.md). 이 파일만으로 승인·정책 준수·상시 변경 탐지가 성립하지 않는다.
