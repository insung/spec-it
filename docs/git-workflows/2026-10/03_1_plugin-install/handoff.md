# 구현과 PR 리뷰 인계

- Issue: [#1](https://github.com/insung/spec-it/issues/1)
- Plan: [plan.md](plan.md), 공개 task 01 → 02 → 03 순서 적용
- base: `1e880c54f74bc8eaf2d0e98516d7ca04931b3ab3`
- 구현 커밋: 패키지 `1b2fa8d`, 안내 `fd9dd5d`. 호스트 helper와 최종 결과는 후속 커밋에서 기록합니다.
- 구현 담당: 별도 구현 에이전트. review 브랜치·worktree·검토 기준·숨은 입력은 읽지 않았습니다.
- 정책: VERSION 0.7.0, 기존 manifest/lock·rules·AGENTS 보존. 패키지 version 0.1.0.

## 사용자 의도와 구현 결과

| AC | 구현 | 증거 상태 |
| --- | --- | --- |
| AC-01 | 공통/Claude/Codex manifest와 두 marketplace | package 검사, Claude strict manifest 검사 통과 |
| AC-02 | local marketplace 설치와 새 프로세스 발견 | 두 호스트 설치·발견 성공. 대표 모델 호출 미실행: human-review |
| AC-03 | 저장소 루트 패키지로 상대 참조 보존 | cached package와 Git archive 구조 재검사 |
| AC-04 | 설치/갱신/제거/중복 해소·이름 대응 문서 | 기존 pin·policy·설정 보존 digest 및 base diff |
| AC-05 | 설치 부수 실행 없음, 규칙과 승인 경계 유지 | hooks/agents/MCP/LSP 0, 정책 루프 회귀 검사 |
| AC-06 | 6개 발행·pair 제외·패키지/정책 버전 구분 | 정적·설치·발견·호출 증거 분리 |

## 계획 대비 차이와 판단

- Git 없는 export에서도 작동하는 package checker, 오류 fixture 8개 및 정상 사례를 추가했습니다.
- template AGENTS의 `.architecture/` 생성 대상 링크 5개는 채택 후 생성될 경로여서 exact allowlist로 구분합니다. 실제 스킬 참조 링크는 검사합니다.
- `scripts/smoke-plugin-install.py`는 archive export, 임시 subprocess env, 새 app-server RPC, 캐시 자료 검사와 원본 digest 비교를 재현합니다. 기존 설정/credential을 복제하지 않습니다.
- Codex 실제 발견 이름은 `spec-it:spec-it-check` 등 namespace 포함입니다. 문서에 실측 결과를 반영했습니다.
- SKILL 지시는 변경하지 않았습니다. Phase 0 정책 절차의 배포 금지와 별도로 승인된 이번 packaging 작업을 안내에서 구분합니다.
- 회귀 명령에 `PYTHONPATH=src`가 필요하므로 공개 plan 명령을 보정합니다.

## 검증 요약과 증거

최종 소스 검증 대상은 `934236c14c7266e00f0dc337e9d70ff7958b3610`입니다. 아래 후속 문서 기록·전환 설명 보완은 구현 코드와 구분합니다.

- 환경: macOS arm64, Claude Code 2.1.282, Codex CLI 0.157.1; 2026-10-03 UTC.
- `node --test scripts/check-package.test.mjs`: 정상 1 + negative 8 = 9/9 통과 (`1b2fa8d` 작업본, commit 이전).
- `claude plugin validate .claude-plugin/plugin.json --strict --json`와 marketplace 동일 명령: errors/warnings 0, 각각 exit 0 (`1b2fa8d` 작업본).
- Claude 새 프로세스 `plugin marketplace add <local-package>` → `plugin install spec-it@spec-it` → `plugin details spec-it@spec-it`: 모두 exit 0. Skills 6, Agents/Hooks/MCP/LSP 0.
- Codex `plugin marketplace add <local-package> --json` → `plugin add spec-it@spec-it --json`: exit 0, package version 0.1.0.
- Codex 새 `app-server`: initialize → initialized → `skills/list` (`cwds` 임시 디렉터리, `forceReload: true`). pluginId spec-it@spec-it의 활성 스킬 6개 발견.
- 두 호스트 대표 스킬 모델 호출: 미실행, 유료/live 모델 실행 승인 범위 밖. `human-review`. 발견을 호출 성공으로 간주하지 않습니다.
- 전역 설치, credential 복제, hooks opt-in, 정책 채택·pin 갱신, merge·Release를 실행하지 않았습니다.

## 위험·전달·롤백

- 구현 자기 검증이며 최종 독립 리뷰 판정이 아닙니다. root가 별도 검토 후 push/PR 게시를 담당합니다.
- 원격 설치는 PR merge 전 기본 브랜치에 이 구성이 없어 검증하지 않았습니다. 공개 문서의 원격 명령은 구성이 해당 ref에 있을 때 사용합니다.
- 임시 설치 제거와 scoped commit revert로 롤백합니다. 채택 프로젝트 파일과 사용자 설치는 보존합니다.

## 최종 재현 결과

| 명령 / 사례 | 실제 결과 | 대상·환경·시각 |
| --- | --- | --- |
| `python3 scripts/smoke-plugin-install.py` | exit 0. HEAD archive export 검사, Claude/Codex install, 신규 discovery 6개, 양 cache checker 모두 통과 | `934236c14c7266e00f0dc337e9d70ff7958b3610`, 리포 루트, 2026-10-03T05:45:05Z |
| `node --test scripts/check-package.test.mjs` | 9/9 pass | 같은 clean HEAD, Node v23.11.0, 2026-10-03T05:45 UTC |
| `PYTHONPATH=src python3 -m unittest discover -s tests -v` | 22/22 pass | 같은 HEAD, Python 3.14.2, 2026-10-03T05:45 UTC |
| Claude manifest 및 marketplace `validate --strict --json` | 각각 exit 0, errors/warnings 0 | 같은 HEAD, Claude 2.1.282, 2026-10-03T05:45 UTC |
| base diff: VERSION·AGENTS·manifest·lock·rules·SKILL 지시 | 출력 없음, 정책 pin·digest 입력·행동 지시 보존 | plan baseline `1e880c54` 대비, 2026-10-03T05:45 UTC |
| smoke 전후 설정·정책 파일 SHA-256 비교 | 동일; 임시 HOME/config 제거 완료 | [비밀 없는 실행 결과](verification.json) |

smoke가 대조하는 전역 경로는 원래 사용자 Codex config 및 plugin install/marketplace records, Claude settings 및 plugin records, `.claude.json`입니다. 정책 파일은 VERSION·AGENTS·manifest·lock·rules 전체를 비교합니다. 원시 설정·credential을 복사하거나 출력하지 않습니다. 테스트 설치는 subprocess env allowlist와 임시 config에만 기록합니다.

대표 호출은 두 호스트 모두 human-review이며 필수 AC-02 전체 pass 또는 최종 독립 리뷰 pass를 주장하지 않습니다. 두 호스트 설치/발견과 실제 캐시 자료 접근은 별도 완료입니다. 계획 단계 03은 이 미실행 필수 증거 때문에 [ ]로 남깁니다.

검토자는 source HEAD 이후의 문서 기록만 달라졌는지 확인하고 동일 명령을 재실행할 수 있습니다. Source 이후 보완은 Codex 갱신의 marketplace refresh → remove → add 재설치 안내와 smoke 재현 명령 안내입니다. 원격 기본 branch 설치는 merge 전 검증하지 않았고 유료 모델 실행도 하지 않았습니다.
