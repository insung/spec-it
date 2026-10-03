# PR 검토 결과

- Issue: [#1](https://github.com/insung/spec-it/issues/1), [plan](plan.md), task 01~03.
- base: `1e880c54f74bc8eaf2d0e98516d7ca04931b3ab3`; 검토 HEAD: `9a5faee69ebcbf6ee5c3f102d60d5fa3255c0db5`; 검토 시작 시 작업본 clean.
- 확인 시각: 2026-10-03T05:47~05:50 UTC. 구현 후 문서 기록 커밋은 source `934236c` 이후 7개 문서·결과 파일에 한정됨을 확인했다.
- 의도 출처: 사용자 요청, Issue AC-01~AC-06 및 승인된 plan.
- 독립 검토 기준: 구현 전에 고정한 `review/issue-1`, `f4196232da5ad3f2e1075f657d3c1a876a516e26`.
- 정책: 기존 `.architecture/manifest.yaml`과 `.architecture/lock.yaml`이 고정한 source `.`, version `0.7.0` 및 locked rule 원문 직접 대조.
- 결과: **fail**. 검사 CLI의 성공 오판과 라이선스 메타데이터를 수정해야 한다. 별도로 두 호스트 대표 모델 호출은 `human-review`이다. 이 결과는 merge 승인이 아니다.

## 공개 지적

1. **AC-01/AC-03, 검사 없이 exit 0이 되는 CLI 진입점** — `scripts/check-package.mjs:71`은 argv 경로의 문자열과 Node의 canonical module URL 경로를 비교한다. macOS의 임시 경로 alias를 통해 같은 파일을 실행하면 조건이 false여서 검사와 출력 없이 exit 0이다. `scripts/smoke-plugin-install.py`도 checker 출력이나 실제 실행을 확인하지 않아 cache 검사를 성공으로 기록할 수 있다. 진입점의 실제 파일 동일성을 확인하고, CLI 실행을 직접 검증하는 회귀 테스트와 smoke assertion을 추가해야 한다. 독립 검토에서 canonical 경로로 검사 본체를 호출하면 정상 구조 및 오류 거부는 동작했다. 이는 검사 본체 전체의 결함과 구분한다.
2. **AC-01/AC-06, 라이선스 메타데이터 불일치** — `plugin.json:11`, `.claude-plugin/plugin.json:10`은 `MIT`를 선언하지만 현재 `LICENSE`와 README는 Apache License 2.0이다. 이번 요청에 라이선스 변경 승인은 없으므로 기존 정본과 package metadata를 일치시켜야 한다.
3. **AC-02, 대표 스킬 호출 증거 미확보** — Claude 설치·component listing 및 Codex 새 app-server `skills/list`는 확인했다. 실제 user prompt를 모델에 전달한 대표 스킬 호출은 두 호스트 모두 미실행이다. 공개 문서와 task는 이를 정직하게 `human-review`로 분리하므로 허위 완료 결함은 없다. AC-02 전체 pass와 merge 추천은 할 수 없다.

## AC별 대조

| AC | 기대 시나리오 | 구현 위치 | 테스트·assertion 및 독립 관측 | 실행 결과 | 판단 |
| --- | --- | --- | --- | --- | --- |
| AC-01 | 두 호스트 metadata·source·version 정합성 및 구조 거부 | plugin manifests, marketplaces, checker | Node package tests 9개; exact HEAD archive의 독립 검사 | 9/9 pass; CLI 경로 alias에서 검사 미실행을 확인 | fail: 진입점과 license 수정 필요 |
| AC-02 | 새 process 설치·발견과 대표 호출 | installation guide, smoke | Claude details Skills 6; Codex fresh skills/list 활성 6개 | 설치·발견 pass; 모델 호출 미실행 | human-review |
| AC-03 | cache 및 export 상대 참조 보존 | repository-root package, checker | canonical archive 검사 정상; 양 호스트 설치된 root package | 설치 pass; smoke의 cache 검사 exit 0만으로 실행을 입증하지 못함 | fail: checker CLI와 smoke evidence 보완 |
| AC-04 | 소유한 개별 설치만 해소, pin·프로젝트 보존 | installation guide | 이름 표·install/update/remove/migration 수동 대조; smoke digest | 기존 policy/settings digest 동일 | pass: 관측한 설정·파일 범위에 한정 |
| AC-05 | 설치가 정책 pin·hook을 바꾸지 않음 | metadata, policy boundary guide | base diff 및 smoke digest, Python loop regression; Claude component counts | policy/AGENTS/SKILL diff 없음; Hooks/Agents/MCP/LSP 0; Python 22/22 | pass: packaging 영향 검사. 일반 정책 강제 pass 의미 아님 |
| AC-06 | 정확한 6개 발행·pair 제외와 증거 범위 구분 | README, skills index, guide, handoff | exact skill inventory, source diff, 수동 문서 대조 | pair 없음; SKILL 행동 지시 무변경; 미실행 분리 | license 및 cache 검사 범위 수정 필요 |

## 고정 입력 재실행

독립 검토자가 고정 입력을 exact HEAD의 새 Git archive 사본에 직접 재실행했다. 검사 본체의 정상·오류·참조 경계 판별을 확인했다. 최초 CLI 실행의 성공 오판을 공개 지적 1로 분리했다. 숨은 입력의 값·기대 지적·통과 기준은 이 공개 기록에 옮기지 않는다. 구현자 자체 fixture는 독립 판정의 유일한 oracle로 사용하지 않았다.

## 실제 실행 근거

| 실행 | 검토 HEAD 결과 |
| --- | --- |
| `node --test scripts/check-package.test.mjs` | exit 0, 9/9 pass |
| `PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests -v` | exit 0, 22/22 pass. 최초 PYTHONPATH 누락 실행은 import error였으며 명령 환경을 바로잡아 재실행했다. |
| `python3 scripts/smoke-plugin-install.py` | exit 0, source exact HEAD; Claude 2.1.282, Codex 0.157.1, Node v23.11.0. 설치·fresh discovery 성공, preservedFiles true, 임시 환경 제거. checker CLI 문제로 cache 참조 검사 완료 주장은 보완 필요. |
| `git diff --check 1e880c54 HEAD` | 출력 없음, exit 0 |
| 정책 원본·SKILL 행동 지시 base diff | VERSION·AGENTS·rules·profiles·schemas·manifest·lock·각 SKILL 지시 변경 없음 |

## 계획 대조

task 01의 checker·metadata, task 02 문서, task 03 격리 설치 helper가 구현되었다. 계획 단계 03은 필수 대표 호출 미실행으로 미완료이며 task의 증거 분리 작업 완료와 AC-02 전체 완료를 구분한다. code/source 이후 커밋은 인계·결과·task/plan·재설치 안내 문서만 변경했다. 원 main의 기존 dirty 파일 및 별도 pair worktree를 확인했으며 리뷰는 이곳을 수정하지 않았다. 원본의 이전 dirty digest는 리뷰 시작 전 증거가 없으므로 root의 전후 기록과 함께 판단해야 한다.

## 정책 대조

| Rule ID | 적용 계기·관찰 | 상태 | 필요한 증거·수정 |
| --- | --- | --- | --- |
| TST-002 | 별도 검토 context와 구현 전 고정 기준으로 독립 실행 | pass | 현재 검토 HEAD의 관측 범위 |
| TST-001 | 새로운 checker/helper 동작, 공개 인계에 red-before-green 실행 기록 없음 | human-review | 초기 failing-test 및 green/refactor의 실제 기록 또는 승인된 면제 근거 |
| RULE-002, TOOL-001 | 설치/발견과 일반 규칙 강제·대표 호출을 구분 | human-review | 미실행 모델 호출과 계획된 일반 validator는 pass로 승격하지 않음 |
| TOOL-002, GOV-001 | 정책 pin·generated lock·rules 정본 보존 | pass | base diff 및 digest, 일반 deterministic lock generation은 계속 human-review |
| SEC-001 | allowlist child env, credential 복제/출력 없음, 전역 설정 digest 보존 | pass | 실행한 격리 설치 범위의 수동 확인 |

## 다음 행동

- checker CLI 경로 동일성·직접 실행 회귀 및 smoke 실제 실행 assertion, license metadata를 수정한 새 HEAD를 재검토한다.
- 대표 모델 호출은 별도 승인 및 실행 증거 확보 전 `human-review`를 유지한다. draft PR에는 이 한계와 검토 결과를 명시할 수 있다.
- root가 검토 기록을 커밋한다. 리뷰 에이전트는 구현 코드·전역 설정·credential·기존 main/pair 작업을 수정하지 않았다.
