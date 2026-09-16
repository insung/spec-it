# 수용 사례 — 선택적 시작점

기존 QA 시트/이슈/별도 QA 저장소의 같은 항목으로 대체할 수 있다. 구현 저장소에 이 파일이나 QA 코드를 만들 필요는 없다. 원문에 대한 독립 관찰의 근거는 [TST-002](../../rules/testing/TST-002.md)를 따른다.

- Change ID / Scenario ID / Case ID: <연결 식별자; 작은 범위는 Scenario와 Case ID 통합 가능>
- Case revision: <고정 revision>
- 의도 원본/section/revision·승인 근거: <locator와 결정자>
- 디자인·화면·계약: <node/section + 승인/관측 revision 또는 사유 있는 N/A>
- 확인할 종류: <기획 적합성 / 고객 목적 / 탐색 가설>
- 적용 유형·실행 경로·경계: <각 경로 applies/excluded/open/unknown과 사유>
- 사전 상태·환경·데이터: <조건과 fixture; DB가 무관하면 N/A 이유>
- 행동: <Given / When>
- 예상 관찰: <Then; 화면/API/선택 결과/DB 상태 중 확인할 위치>
- 반례·경계·유지 조건: <잘못된 입력, 권한/계정 차이, 비대상 동작 등 실제 관련 항목>
- 판정자 / 미결정: <acceptance owner, 결정 근거>

## 변경 이력

| Revision | 변경 이유·승인 | 영향받는 기존 run | 후속 검증 |
| --- | --- | --- | --- |
| <rev> | <기획 정정 등> | <원래 결과는 보존> | <새 run 필요 또는 무관 근거> |

실행 결과는 [verification run](verification-run.md)처럼 별도로 기록한다. 실행 관찰에 맞춰 기존 기대값을 바꾸지 않는다. 탐색 가설이 결함 또는 새 요구가 되면 관찰과 사람 결정을 연결한다.
