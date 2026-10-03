---
issue: "#1"
status: ready
branch: "feat/plugin-install"
base: "main"
created: "2026-10-03"
---

# 플러그인 설치 지원 계획

## 요청

> spec-it 을 플러그인 설치 형태로 변경해줘. 참고할 프로젝트는 git-workflow 를 참고해줘.

- 해석: [Issue #1](https://github.com/insung/spec-it/issues/1)의 Claude Code·Codex 플러그인 패키지와 설치 안내 구현
- 남은 결정: 없음. 실제 호스트 호출에 필요한 유료 모델 실행은 승인 범위 밖이며 미확보 증거는 human-review

## 현재 동작과 변경 이유

| 현재 동작 | 근거 위치 | 바꿀 결과 |
| --- | --- | --- |
| 공개 정책 버전 0.7.0, Git source 배포 | `VERSION`, `README.md` 현재 상태 | 별도 패키지 버전 0.1.0과 두 호스트 플러그인 설치 지원 |
| 하이픈 이름 개별 설치, plugin namespace는 논리 이름 | `skills/README.md`, `skills/*/SKILL.md` | 기존 이름 보존과 실제 호스트 호출·논리 이름의 대응 안내 |
| 패키지 배포 제외, manifest distribution git-source-only | `.architecture/project.md`, `.architecture/manifest.yaml` | 현재 패키징 상태와 고정된 0.7.0 자체 정책 투영의 차이 명시 |
| manifest raw text digest 검사, lock generator 미구현 | `src/spec_it_hook/policy.py`, `.architecture/lock.yaml` | 기존 manifest/lock 보존, 설치가 재수렴을 대신하지 않는 경계 |
| 두 호스트 manifests 및 marketplace 제공 | 참고 저장소 `git-workflow/plugin.json`, `.claude-plugin/`, `.codex-plugin/`, `.agents/plugins/marketplace.json` | 같은 구조로 spec-it 명세·정책 자료 동봉 |

## 범위

| 구분 | 내용 |
| --- | --- |
| 포함 | 공통 manifest, 두 호스트 metadata/marketplace, 6개 추적 스킬·기존 참조의 패키지 경로, 설치/전환 문서, 패키지 및 격리 호스트 검사, `.worktree/` ignore |
| 제외 | rules 의미 변경, 새 policy version/tag/Release, 새 adapter, hook 자동 활성화, pair 발행, 사용자 전역 설치 변경, 유료 모델 호출 |
| 미변경 소비자 | 개별 설치 사용자, 기존 채택 프로젝트, 0.7.0 자체 정책 투영, Claude active policy loop |
| 호환성·데이터·운영 | 하이픈 폴더/frontmatter 보존. 플러그인 갱신과 정책 pin 재수렴 별개. 기존 미커밋·병행 worktree 보존 |

발행 목록은 `spec-it-specify`, `spec-it-clarify`, `spec-it-converge`, `spec-it-check`, `spec-it-evolve`, `spec-it-impact` 6개다. impact의 현재 미발행 후보 표기는 이번 패키지의 설치 대상으로 명확히 전환하되 동작 절차를 확장하지 않는다. pair는 대상에서 제외한다. Claude의 실제 호출은 `/spec-it:spec-it-check`처럼 plugin namespace와 기존 frontmatter name의 조합이며 논리 이름 `spec-it:check`와 구분한다. Codex는 실제 발견 출력으로 이름을 확인하고 그 결과를 안내에 반영한다.

패키지 metadata version은 `0.1.0`, 정책 `VERSION`과 기존 manifest/lock version은 `0.7.0`으로 분리한다. 고정된 자체 투영의 `distribution: git-source-only`는 해당 정책 채택 당시 입력이며 현재 플러그인 배포 상태가 아니다. 문서에 이를 설명한다. manifest 수정과 lock digest 손편집으로 이번 패키징 상태를 재투영하지 않는다.

## 단계

| 단계 | 제목 | 설명 | 검증 사례 | 완료 |
| --- | --- | --- | --- | --- |
| [01](task-01-plugin-package.md) | 패키지 구조 | manifest와 marketplace, 자료 경로 및 구조 검사 | [TC-01](task-01-plugin-package.md#tc-01), [TC-02](task-01-plugin-package.md#tc-02) | [ ] |
| [02](task-02-installation-guide.md) | 설치·전환 안내 | 이름 대응, 수명 주기, 정책 경계 | [TC-03](task-02-installation-guide.md#tc-03), [TC-04](task-02-installation-guide.md#tc-04) | [ ] |
| [03](task-03-host-verification.md) | 호스트 검증과 인계 | 격리 설치·발견·호출 증거, 회귀 검사 | [TC-05](task-03-host-verification.md#tc-05), [TC-06](task-03-host-verification.md#tc-06) | [ ] |

실행 순서: 01 → 02 → 03. 실패하면 해당 단계에서 보완한다. 검토 기준은 plan 커밋에서 분기한 `review/issue-1`에 먼저 고정하고 구현 세션은 읽지 않는다.

## 최종 검증

| 사례 | AC | 명령·작업 디렉토리 | 기대 결과 | 필요 승인 | 결과 |
| --- | --- | --- | --- | --- | --- |
| <a id="tc-f01"></a>TC-F01 | AC-01, AC-03, AC-06 | `node scripts/check-package.mjs`, 리포 루트; Git archive export에서도 재검사 | 6개 스킬·동봉 참조·manifest·상대 링크 일치, 구조 검사와 호스트 실행 구분 | 없음 | 미실행 |
| <a id="tc-f02"></a>TC-F02 | AC-02, AC-04, AC-05 | 격리 subprocess env의 Claude/Codex marketplace 설치·신규 discovery; 전후 policy/project/settings digest 비교 | 호스트별 실제 설치/발견/호출 단계 결과와 설정 보존 증거, 미실행은 human-review | 유료 호출은 별도 승인 필요, 이번 범위 제외 | 미실행 |
| <a id="tc-f03"></a>TC-F03 | AC-05, AC-06 | `python3 -m unittest discover -s tests -v`; `git diff --check`, 리포 루트 | 기존 정책 루프 회귀 없음, 규칙·pin·hook 자동 변경 없음 | 없음 | 미실행 |

패키지 검사에는 정상 구조뿐 아니라 잘못된 버전·누락 참조·범위 외 스킬·깨진 링크를 거부하는 의미 있는 사례를 포함한다. 단순 문서 문구를 그대로 모방하는 테스트는 추가하지 않는다.

## 전달과 롤백

| 항목 | 내용 |
| --- | --- |
| 전달 방법 | 구현 로컬 커밋 → 별도 에이전트 검토 → 작업 브랜치 push → Issue #1 연결 PR. 검토 미실행 필수 증거는 PR에 명시 |
| 필요 승인 | 사용자 요청에 구현·검증·커밋·push·PR 포함. merge·Release·전역 설치·유료 모델 실행은 포함하지 않음 |
| 적용 후 확인 | 원격 PR head/base/Issue 연결 및 게시된 근거 링크 재조회. 호스트 미실행 항목을 완료로 표현하지 않음 |
| 롤백 | PR에서 scoped commit revert, 임시 격리 환경 제거. 기존 전역 설치/채택 프로젝트 manifest·lock은 보존 |

## 결정과 변경 기록

| 날짜 | 구분 | 내용 | 영향 AC·단계 | 상태 |
| --- | --- | --- | --- | --- |
| 2026-10-03 | 요청 변경 | Issue 작성 이후 사용자가 서브에이전트 구현·검증·PR 요청. Issue 작성 당시 구현 제외를 이번 승인으로 확장 | 전체 | 승인 |
| 2026-10-03 | 결정 | 추적된 6개 스킬만 설치 대상으로 포함, pair 및 병행 작업 제외 | AC-06·01 | 승인 |
| 2026-10-03 | 결정 | 기존 하이픈 name/폴더 보존, 실제 호출과 논리 이름의 대응 안내 | AC-02, AC-04·02 | 승인 |
| 2026-10-03 | 결정 | 패키지 0.1.0과 정책 0.7.0 분리, 고정 자체 manifest/lock 보존 | AC-01, AC-04, AC-05·01/02 | 승인 |
| 2026-10-03 | 결정 | 두 호스트 격리 설치/발견은 모델 없이 시도, 대표 호출 증거 부족 시 human-review | AC-02, AC-06·03 | 승인 |
