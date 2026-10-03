# 01 설명과 진입 안내 정리

계획: [plan의 단계 표](plan.md#단계)

## 변경 대상

| 구분 | 경로 | 이유 |
| --- | --- | --- |
| Create | docs/pair-work-cycle.md, docs/s3-shared-library-pairing.md | 협업 절차와 별도 S3 설명 |
| Create | docs/pilots/pair-workflow-acceptance.md, skills/spec-it-pair/SKILL.md | 기존 후보·미검증 수용 사례 보존 |
| Modify | README.md, docs/README.md, docs/agent-work-cycle.md, skills/README.md, CHANGELOG.md | 진입점·색인·후보 상태 연결 |
| Modify | templates/project/AGENTS.md, skills/spec-it-converge/SKILL.md | 일반 질문·프로젝트 질문 구분의 짧은 안내 |

## 작업

| # | 작업 | 완료 | 처리 내용 |
| --- | --- | --- | --- |
| 1 | 원본 후보 11개 파일의 스냅샷·diff 대조 후 이 범위만 반입 | [ ] | |
| 2 | AGENTS 기본 진입점과 pair 후보의 선택적·미발행 상태를 각 진입 안내에 명시 | [ ] | |
| 3 | S3 여섯 단계와 공통화 조건·어댑터/도메인·접근 한계 설명 정리 | [ ] | |
| 4 | 현재 없는 검증 runner 문서 참조 제거 및 현재 상태 설명 보완 | [ ] | |
| 5 | 색인·Unreleased·일반 질문 안내 정합성 확인 | [ ] | |

## 검증

| 사례 | AC | 명령·작업 디렉토리 | 기대 결과 | 결과 |
| --- | --- | --- | --- | --- |
| <a id="tc-01"></a>TC-01 | AC-01, AC-02, AC-06 | 진입 안내·pair 후보·템플릿·converge 원문 대조, 리포 루트 | pair 필수·자동 실행·새 권한·일반 질문 강제 없음 | 미실행 |
| <a id="tc-02"></a>TC-02 | AC-03, AC-04, AC-06 | S3 문서와 ARCH-001/002/003 및 domain-core-libraries 대조, 리포 루트 | 여섯 단계와 실제/미래 소비자·로컬/공유 모듈·어댑터/도메인 구분, 깨진 runner 참조 부재 | 미실행 |

## 제외 범위

- 새 규칙·정책 변경·후보 발행·런타임·실제 S3 구현
- 검토 기준 브랜치와 검토 입력의 열람
