# 01 패키지 구조

계획: [plan의 단계 표](plan.md#단계)

## 변경 대상

| 구분 | 경로 | 이유 |
| --- | --- | --- |
| Create | `plugin.json`, `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.codex-plugin/plugin.json`, `.agents/plugins/marketplace.json` | 참고 git-workflow와 동일한 두 호스트 배포 진입점 |
| Create | `scripts/check-package.mjs` 및 필요한 검사 테스트 | 설치 범위·자료·링크 계약 구조 검사 |
| Modify | `.gitignore` | 프로젝트 로컬 `.worktree/` 제외 |

## 작업

| # | 작업 | 완료 | 처리 내용 |
| --- | --- | --- | --- |
| 1 | 이름 spec-it·패키지 버전 0.1.0 및 marketplace source 경로 일치 | [ ] | |
| 2 | 6개 추적 스킬과 필수 정책·프로필·schema·template·references 동봉 경로 보존 | [ ] | |
| 3 | 정상·오류 구조 검사 및 Git archive에서 검사 가능하도록 구현 | [ ] | |
| 4 | pair 자동 발행 및 hook/설치 부수 실행 없이 metadata 작성 | [ ] | |

## 검증

| 사례 | AC | 명령·작업 디렉토리 | 기대 결과 | 결과 |
| --- | --- | --- | --- | --- |
| <a id="tc-01"></a>TC-01 | AC-01, AC-06 | `node scripts/check-package.mjs`, 리포 루트; Claude manifest/marketplace validate | names/versions/source/6 skills 일치, 공식 host 검사 범위 명시 | 미실행 |
| <a id="tc-02"></a>TC-02 | AC-03, AC-06 | 임시 Git archive export에서 package 검사 및 잘못된 package fixtures 검사 | 필수 참조 접근 가능, 깨진 링크/누락 자료/버전 불일치 거부 | 미실행 |

## 제외 범위

- 규칙·기존 스킬 동작 의미 변경, 발행 tag·Release, 사용자 전역 설정
