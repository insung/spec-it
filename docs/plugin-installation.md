# 플러그인 설치와 전환

패키지 `0.1.0`은 정책 `0.7.0`의 스킬 6개와 저장소 루트의 `rules/`, `profiles/`, `schemas/`, `templates/`, 관련 `docs/`·references를 함께 제공합니다. 폴더 구조를 유지해야 상대 참조를 읽을 수 있습니다. `spec-it-pair` 후보는 발행하지 않습니다.

## Claude Code

Claude Code에서 다음 명령을 실행합니다. 로컬 clone을 사용할 때 첫 명령의 `insung/spec-it` 대신 clone 경로를 사용합니다.

```text
/plugin marketplace add insung/spec-it
/plugin install spec-it@spec-it
```

설치 뒤 새 세션을 시작합니다. CLI에서는 `claude plugin marketplace add <clone-path>`와 `claude plugin install spec-it@spec-it`를 사용하고, `claude plugin details spec-it@spec-it`로 components를 확인합니다. 대표 호출은 `/spec-it:spec-it-check 이 프로젝트를 변경 없이 점검해줘`입니다.

갱신은 `/plugin marketplace update spec-it` 후 `/plugin update spec-it@spec-it`, 제거는 `/plugin uninstall spec-it@spec-it`입니다. CLI 대응은 `claude plugin marketplace update spec-it`, `claude plugin update spec-it@spec-it`, `claude plugin uninstall spec-it@spec-it`입니다. 갱신·제거 뒤 새 세션에서 다시 확인합니다.

## Codex

설치된 CLI의 `codex plugin --help`에서 지원 여부를 먼저 확인합니다.

```sh
codex plugin marketplace add insung/spec-it
codex plugin add spec-it@spec-it
codex plugin list --json
```

로컬 clone도 `codex plugin marketplace add <clone-path>`로 등록합니다. 설치 뒤 새 chat을 열어 스킬 목록과 `$spec-it:spec-it-check`를 확인하고 `이 프로젝트를 변경 없이 점검해줘`라는 요청과 함께 호출합니다. 앱의 목록은 현재 chat의 스킬 발견과 다를 수 있으므로 새 세션의 발견 출력을 확인합니다.

갱신은 `codex plugin marketplace upgrade spec-it` 후 `codex plugin add spec-it@spec-it`, 제거는 `codex plugin remove spec-it@spec-it`입니다. marketplace 등록까지 지우려면 `codex plugin marketplace remove spec-it`를 별도로 실행합니다. 설치된 CLI 버전에 따라 명령 지원이 다르면 `--help`를 기준으로 확인합니다.

## 이름 대응

| 문서 논리 이름 | 폴더/frontmatter | Claude 호출 / Codex 발견 이름 |
| --- | --- | --- |
| `spec-it:specify` | `spec-it-specify` | `spec-it:spec-it-specify` |
| `spec-it:clarify` | `spec-it-clarify` | `spec-it:spec-it-clarify` |
| `spec-it:converge` | `spec-it-converge` | `spec-it:spec-it-converge` |
| `spec-it:check` | `spec-it-check` | `spec-it:spec-it-check` |
| `spec-it:evolve` | `spec-it-evolve` | `spec-it:spec-it-evolve` |
| `spec-it:impact` | `spec-it-impact` | `spec-it:spec-it-impact` |

Claude는 앞에 `/`, Codex는 발견 이름 앞에 `$`를 붙여 호출합니다. Codex 0.157.1의 새 app-server `skills/list`에서 namespace 포함 이름 6개를 확인했습니다.

하이픈 name을 유지하므로 기존 개별 스킬 요청도 계속 식별할 수 있습니다. 호스트의 표시 이름·namespace는 실제 목록에서 확인합니다.

## 개별 설치에서 전환

1. `.agents/skills`, 개인 skills 디렉터리, Claude skills 디렉터리의 spec-it 복사본·symlink와 소유자를 확인합니다. 사용자 설정과 프로젝트 파일을 백업합니다.
2. 플러그인을 설치하고 새 세션에서 6개 스킬 및 패키지 자료 접근을 확인합니다.
3. 본인이 직접 설치한 중복 복사본·symlink만 제거하거나 설치 위치 밖으로 옮깁니다. 공유 설치, 다른 사람의 파일, 출처가 불명확한 항목은 소유자에게 확인합니다. 정책 원본과 채택 프로젝트를 삭제하지 않습니다.
4. 새 세션에서 중복 발견이 해소됐는지 확인합니다. 문제가 있으면 플러그인을 제거하고 보관한 개별 설치를 복원합니다.

이 패키지는 전환 스크립트나 전역 설정 변경을 실행하지 않습니다. 개별 폴더만 복사하면 루트 자료 상대 경로가 깨질 수 있으므로 전체 repository-root 패키지 구조를 보존합니다.

## 정책과 설치의 경계

플러그인 갱신은 패키지 캐시만 갱신합니다. 채택 프로젝트의 `AGENTS.md`, manifest, lock, ADR, exact policy version과 digest를 자동 변경하지 않습니다. 정책 갱신은 사람이 승인한 clarify → converge → check 절차로 별도 진행합니다. `rules/`가 유일한 규칙 정본이며 동봉된 최신 소스가 기존 프로젝트 pin을 대체하지 않습니다.

설치는 Claude active policy loop 훅을 자동 활성화하지 않습니다. 프로젝트 로컬 opt-in과 [정책 루프 안내](active-policy-loop.md)의 별도 절차를 따릅니다. Codex에 새로운 정책 루프 adapter를 제공하지 않습니다.

스킬의 Phase 0 instruction-only·배포 금지 문구는 정책 진화 절차의 범위를 설명합니다. 이번 사용자가 별도 승인한 패키징 작업과 구분하며, evolve 호출이 자동으로 플러그인 발행까지 승인하는 것은 아닙니다. 기존 `.architecture/manifest.yaml`의 `git-source-only`는 정책 0.7.0 자체 투영 당시 입력으로 보존합니다.

## 검증 범위

`node scripts/check-package.mjs`는 manifest·버전·발행 목록·필수 자료·상대 링크를 검사합니다. `node --test scripts/check-package.test.mjs`는 정상 구조와 잘못된 버전·누락 자료·범위 외 스킬·깨진 링크·부수실행 metadata를 검증합니다. 템플릿 AGENTS의 생성 대상 `.architecture/` 링크는 채택 후 생성되는 경로로 구분합니다. 정적 성공은 호스트 실행 성공을 증명하지 않습니다.

실제 설치·신규 프로세스 발견·대표 모델 호출은 따로 기록합니다. 모델 호출이 미실행이면 `human-review`이며 발견 결과만으로 AC-02 전체를 pass로 보고하지 않습니다. 이번 구현의 [검증 인계](git-workflows/2026-10/03_1_plugin-install/handoff.md)를 참고합니다.

공식 자료: [Claude Code 플러그인](https://code.claude.com/docs/en/plugins), [Claude marketplace](https://code.claude.com/docs/en/plugin-marketplaces), [Codex 플러그인](https://developers.openai.com/codex/plugins/).
