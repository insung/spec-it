# Data pipeline operations

정기 데이터 pipeline은 실행 프로세스가 끝났다는 사실이 아니라 consumer가 사용할 terminal data outcome을 운영합니다. 정본 규칙은 [OBS-003](../rules/observability/OBS-003.md)입니다.

## 기대와 실제를 분리한다

프로젝트 계약은 언제 어떤 partition이 어떤 terminal dataset에 준비되어야 하는지 정의합니다. run ledger는 실제로 어떤 코드·DB 정의가 어느 partition을 처리했고 어디까지 진행했는지를 기록합니다. monitoring은 둘의 차이를 검사합니다.

```text
expected schedule and output contract
  -> run ledger and terminal data checks
  -> freshness, completeness, integrity, reconciliation
  -> owner alert and consumer state
  -> dependency-aware replay and terminal re-verification
```

중간 step marker는 원인을 좁히는 데 유용하지만 terminal table이 준비됐다는 증거가 아닙니다. 반대로 row가 있다는 사실도 중복·부분 적재가 없음을 증명하지 않습니다. 중요한 consumer와 연결된 terminal output마다 정상적인 빈 결과, expected volume, uniqueness와 control total 중 필요한 검사를 선택합니다.

## 예방, 발견, 복구, 소비자 상태

- **예방**: unique·foreign-key·check constraint, single-run coordination, versioned code와 routine definition으로 표현할 수 있는 오류를 먼저 막습니다.
- **발견**: schedule delay, heartbeat stall, freshness, completeness, integrity와 reconciliation을 별도 신호로 봅니다.
- **복구**: calendar gate 밖에서도 target partition을 선택해 replay할 수 있고, checkpoint·idempotency·deduplication과 dependency를 기록합니다.
- **소비자 상태**: 정상 0건과 준비 중·stale·실패를 같은 빈 화면이나 성공 응답으로 합치지 않습니다.

DB migration system은 pipeline이 사용하는 schema와 routine의 version을 제공하고, data pipeline operations는 그 version이 계속 올바른 데이터를 만드는지 확인합니다. 두 체계는 release identity와 owner를 공유할 수 있지만 배포 시점의 변경 제어와 운영 중의 outcome monitoring을 같은 성공 조건으로 보지 않습니다.
