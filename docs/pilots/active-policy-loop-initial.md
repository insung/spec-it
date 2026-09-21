# Active policy loop initial pilot

이 문서는 2026-09-21 한 고위험 Python HTTP API의 격리 worktree에서 수행한 약식 측정이다. 대상 제품의 기능 성공, 사용자 수용, 모든 Claude 환경의 hook 성공을 뜻하지 않는다.

## 범위와 기준선

- 대상 source는 수정하지 않고 local Claude settings만 임시 worktree에 두었다.
- 기존 application test 164개와 Ruff format/lint 기준선은 모두 통과했다.
- 프로젝트가 고정한 유효한 이전 policy release를 그대로 사용했고 최신 후보로 업그레이드하지 않았다.
- runner는 별도 model/API 호출을 하지 않았다.

## 분류와 비용

설명, no-change, 문서 질문, API/DB/config 변경, read/write tool, read-only shell의 9개 hand-labeled scenario를 각 12회 실행했다.

| 관측 | 결과 |
| --- | --- |
| 수정 후 분류 불일치 | 0 / 9 scenarios |
| Light p50 | 7.59–8.19 ms |
| Light 관측 p95 최대 | 9.85 ms |
| Hard p50 | 44.34–69.63 ms |
| Hard 관측 p95 최대 | 109.50 ms |
| Hard context | 2,196–4,508 characters |
| 선택 규칙 | 5–8 rules |
| 별도 hook model call | 0 |

문자 수는 tokenizer와 모델에 독립적인 원시 측정이다. 실제 모델 input token과 과금으로 바꾸어 주장하지 않는다.

## 발견한 오탐

첫 실제 `UserPromptSubmit`에서 “API를 설명하되 파일은 수정하지 마”가 `수정`만 보고 Hard로 상승했다. 이 1건을 실패 반례로 추가하고 한국어·영어 no-change 표현을 제거한 뒤 같은 요청은 Light 무출력으로 재검증했다. 위의 0/9는 수정 후 수치이며 최초 실패를 숨기지 않는다.

## 실제 Claude lifecycle 관측

Claude Code 2.1.276에서 project-local `UserPromptSubmit` command hook이 실행되어 구조화 context를 반환하는 것까지 확인했다. 실행 환경에는 Claude 로그인이 없어 model turn은 인증 실패했고 보고된 API usage와 비용은 0이었다. 또한 관리 sandbox가 Claude의 session environment 디렉터리 생성을 막아 `SessionStart` 전체 경로는 완료하지 못했다.

따라서 이번 파일럿이 입증한 것은 runner/adapter 계약, project-local prompt hook 연결, 지연·context 크기와 초기 오탐 수정이다. 실제 과금, authenticated model behavior, 모든 lifecycle event, timeout/fail-open의 실환경 수용은 후속 파일럿으로 남는다.
