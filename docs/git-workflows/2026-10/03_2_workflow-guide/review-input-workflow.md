# TC-R01 고정 입력: 안내 독자의 경계 질문

검토 담당이 완성 문서만 읽어 다음 요청에 대한 답을 찾고 원문 소스와 대조한다.

## 입력

1. 정책을 채택하지 않은 기존 리포를 수정 없이 살펴보고 싶다.
2. 이미 채택한 리포에 새 DB를 추가하려 한다. manifest만 수정하면 검토 기준도 바뀌는가?
3. lock digest가 일치하면 자동 생성과 모든 규칙 준수를 증명하는가?
4. hook에서 finding이 나왔는데 advisory다. 결과가 pass이며 중요하지 않다는 뜻인가?
5. check로 오류를 고쳐 달라고 하면 runner가 수정·테스트·예외 승인을 자동 수행하는가?
6. active policy loop의 Hard가 별도 AI를 호출하는가? hook 오류에서도 확실히 차단되는가?
7. runner와 pair가 0.7.0 release의 독립 검증 기본 실행인가?

## 기대 지적

| ID | 기대 답·위험 | 근거 | 기대 판정 |
| --- | --- | --- | --- |
| F1 | 채택 전 shadow assessment이며 수정·채택은 별도 승인 | AC-01 | 반대 안내면 fail |
| F2 | 승인 입력 변경 후 재수렴, lock 직접 편집 금지 | AC-02 | 자동 변경 주장 시 fail |
| F3 | identity 확인일 뿐 generator·의미 준수 증명 아님 | AC-03 | 증명 주장 시 fail |
| F4 | finding은 관찰, advisory는 처리 효과. pass나 중요도와 별개 | AC-05 | 혼동 시 fail |
| F5 | check는 읽기 전용. 후보 runner의 실행 경계도 분리 | AC-04, AC-06 | 권한 확대 시 fail |
| F6 | Hard는 관련 규칙 context, 별도 모델 없음. hook 자체 오류는 fail-open 가능 | AC-07 | 보편 차단 주장 시 fail |
| F7 | hook core runner는 발행 소스, pair·독립 검증 runner는 확인된 후보 상태와 구분 | AC-06 | 출시 혼동 시 fail |

지적하지 않아야 하는 것: 기존 규칙의 human-review나 후보 상태 자체, 문서 변경에 runtime 단위 테스트 미추가.

## 통과 기준

7개 입력의 답을 안내와 링크된 정본에서 찾을 수 있어야 한다. 직접 내용 대조 1회와 링크·렌더링 기계 검사를 실시한다. 별도 스킬 실행 시나리오는 없음이다.
