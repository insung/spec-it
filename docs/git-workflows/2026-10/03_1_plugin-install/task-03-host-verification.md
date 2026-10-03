# 03 호스트 검증과 인계

계획: [plan의 단계 표](plan.md#단계)

## 변경 대상

| 구분 | 경로 | 이유 |
| --- | --- | --- |
| Create | `docs/git-workflows/2026-10/03_1_plugin-install/handoff.md` | 대상 commit·명령·관측·미실행 증거 |
| Modify | 같은 디렉토리 `plan.md`, `task-*.md` | 실제 처리 내용 및 결과 |

## 작업

| # | 작업 | 완료 | 처리 내용 |
| --- | --- | --- | --- |
| 1 | 임시 subprocess environment에만 config/home 경로 지정, global 설정·credential 복제 없이 격리 | [ ] | |
| 2 | Claude 문서화 절차로 local marketplace 설치, 신규 discovery/components 조회 | [ ] | |
| 3 | Codex 문서화 절차로 local marketplace 설치, 신규 app-server skills/list 조회 | [ ] | |
| 4 | 대표 스킬 호출 실제 증거와 설치/발견을 분리. 미실행 사유 human-review 기록 | [ ] | |
| 5 | 전체 회귀 검사·export 검사·전후 파일 보존 검사 및 검토 인계 | [ ] | |

## 검증

| 사례 | AC | 명령·작업 디렉토리 | 기대 결과 | 결과 |
| --- | --- | --- | --- | --- |
| <a id="tc-05"></a>TC-05 | AC-02, AC-03, AC-06 | 임시 환경 `claude plugin marketplace add <local-package>`, `claude plugin install spec-it@spec-it`, `claude plugin details spec-it@spec-it`; Codex 대응 marketplace/add 및 app-server skills/list | 두 호스트 설치·새 process 발견·실제 참조 접근을 개별 기록. 대표 호출은 실제 호출 없으면 미실행 | 미실행 |
| <a id="tc-06"></a>TC-06 | AC-04, AC-05, AC-06 | 사용자 설정/기존 policy 파일 digest 전후 대조; `python3 -m unittest discover -s tests -v`; `git diff --check` | 사용자 설정/기존 pin 동일, 회귀 없음. 미확보 증거를 pass 처리하지 않음 | 미실행 |

명령 옵션은 설치된 CLI `--help`와 공식 문서를 재확인해 실제 실행 명령을 handoff에 남긴다. 임시 환경은 subprocess의 env dictionary로 지정한다. 셸에서 HOME/CODEX_HOME 시스템 변수를 작업 변수로 재선언하지 않는다. 글로벌 credential을 복제하거나 유료 모델 호출로 대표 호출을 강행하지 않는다. 실제 hook 활성화 없이 설치 전후 상태를 대조한다.

## 제외 범위

- 유료/live 모델 호출, 글로벌 사용자 설치·계정 변경, merge·release
