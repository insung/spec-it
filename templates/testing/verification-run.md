# 검증 실행 — 선택적 시작점

이 형식은 QA 코드·도구·폴더를 강제하지 않는다. 하나의 run 기록은 당시 기대/관찰을 보존하고 후속 결과로 덮어쓰지 않는다. 수정이 필요한 기록 오류는 정정 이력으로 남긴다. 이 템플릿의 상태는 프로젝트 예시이며 공식 check enum이 아니다.

- Run ID / Change ID: <새 실행 식별자와 상위 기록>
- Case/Scenario ID + revision / suite revision: <고정 사례 또는 case-set snapshot>
- 출처 기준: <기획·디자인·계약의 승인 revision/snapshot>
- 대상: <구현 repo commit + dirty/artifact digest, QA repo commit; 무관 항목은 N/A 사유>
- 환경/도구: <build, 설정, client/server 지원 조합, fixture, DB migration/schema/data 상태 또는 N/A>
- 실행 시각·실행자/모델·관찰자: <실제 확인값; 미실행/미확인은 그대로 기록>
- 안전 경계: <격리/외부 side-effect sink/cleanup/중단 조건의 승인된 계획 참조>

| Case@revision / 경로 | 예상 결과 | 실제 관찰 | 상태 | 증거·확인자 |
| --- | --- | --- | --- | --- |
| <ID와 경로> | <실행 당시 기대> | <관찰 또는 미실행 이유> | <not-run/met/unmet/blocked 등 프로젝트 상태> | <불변 결과 위치와 확인자> |

## 결함·정정·재검증

- 결함: <ID, 예상과 실제의 차이, 재현 입력>
- 고칠 대상 / 원인 확실성: <원본 의도·디자인·계약·코드·데이터·환경 또는 조사 중>
- 수정 근거: <승인/commit/artifact와 회귀 case revision>
- 후속 run / 재확인자: <이 run을 유지한 채 새 결과 연결>
- 현재 사용 가능 여부: <출처/build/환경 변화로 재검토 필요 여부; 당시 결과와 구별>
- 마지막 조회 시각 / 접근 불가 / 재검토 trigger: <원격 링크만으로 최신 통과를 추정하지 않음>
- 완료 코멘트: <어떤 버전·조건에서 무엇을 확인했고 정상/실패/미확인인지, 남은 범위>

경계 테스트와 데이터 안전의 정본은 선택된 [TST-003](../../rules/testing/TST-003.md), [TST-006](../../rules/testing/TST-006.md)이며, DB 변경 전달은 적용 시 [DATA-009](../../rules/data/DATA-009.md)를 참조한다. 이 문서 작성만으로 해당 테스트를 실행하거나 승인받은 것이 아니다.
