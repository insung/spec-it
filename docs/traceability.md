# Rule traceability

손으로 관리하는 거대한 `rule → document → profile → validator → test` 표는 또 하나의 정본이 되어 쉽게 낡습니다. 추적 관계는 다음 소스에서 계산합니다.

| Edge | Canonical source |
| --- | --- |
| rule identity and enforcement | each `rules/<category>/<ID>.md` front matter |
| document → rule | relative links in `docs/` |
| profile → rule | each `profiles/<axis>/<name>.yaml` `rules` array |
| infrastructure profile → decision and evidence shape | profile `traits` and `evaluation` block |
| project → profile | `.architecture/manifest.yaml` |
| project → thresholds and guardrails | manifest `parameters` and linked ADRs |
| project → resolved rule | `.architecture/lock.yaml` |
| rule → expected evidence | rule front matter `evidence` |
| validator status | rule front matter `enforcement.implementation` |
| semantic examples | `examples/README.md` and fixture paths |

Phase 0에서는 이 연결을 수동·구조 검사로 확인합니다. Phase 1 validator가 위 소스에서 traceability graph를 생성하고, 실제 프로젝트 pilot로 구조가 안정된 뒤 연결되지 않은 규칙을 CI 실패로 승격합니다. 생성 graph는 정본으로 손수 수정하지 않습니다.

## 변경과 QA의 연결 — 미발행 후보

위 표는 정책 규칙의 추적이고, 사용자 의도→Scenario→실행 경로→Case/Run의 연결은 별도입니다. [의도와 검증](intent-and-verification.md)은 기존 도구의 정본을 유지하며 상위 변경 기록에서 출처 revision·관찰 시각·결함·재검증을 조회하는 선택 방법을 설명합니다. 이 기록을 정책 SSOT나 자동 생성 graph로 취급하지 않습니다. 링크만으로 통합 UI·동기화·최신 상태 확인이 구현되지는 않습니다.
