# Rule traceability

손으로 관리하는 거대한 `rule → document → profile → validator → test` 표는 또 하나의 정본이 되어 쉽게 낡습니다. 추적 관계는 다음 소스에서 계산합니다.

| Edge | Canonical source |
| --- | --- |
| rule identity and enforcement | each `rules/<category>/<ID>.md` front matter |
| document → rule | relative links in `docs/` |
| profile → rule | each `profiles/<axis>/<name>.yaml` `rules` array |
| project → profile | `.architecture/manifest.yaml` |
| project → resolved rule | `.architecture/lock.yaml` |
| rule → expected evidence | rule front matter `evidence` |
| validator status | rule front matter `enforcement.implementation` |
| semantic examples | `examples/README.md` and fixture paths |

Phase 0에서는 이 연결을 수동·구조 검사로 확인합니다. Phase 1 validator가 위 소스에서 traceability graph를 생성하고, 실제 프로젝트 pilot로 구조가 안정된 뒤 연결되지 않은 규칙을 CI 실패로 승격합니다. 생성 graph는 정본으로 손수 수정하지 않습니다.
