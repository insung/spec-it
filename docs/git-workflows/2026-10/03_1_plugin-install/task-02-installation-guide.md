# 02 설치·전환 안내

계획: [plan의 단계 표](plan.md#단계)

## 변경 대상

| 구분 | 경로 | 이유 |
| --- | --- | --- |
| Modify | `README.md`, `skills/README.md`, `.architecture/project.md` | 현재 package 배포·범위와 기존 policy 자체 투영 관계 |
| Create | `docs/plugin-installation.md` | 설치·갱신·제거·중복 전환·호스트별 이름 대응 |

## 작업

| # | 작업 | 완료 | 처리 내용 |
| --- | --- | --- | --- |
| 1 | 공식 설치 명령과 신규 세션, 발견·실제 호출 이름 대응 안내 | [x] | 구현 및 자기 검증, `fd9dd5d`. 상세 근거는 [handoff](handoff.md) |
| 2 | 개별 설치 전환 시 직접 소유한 복사/심볼릭 링크만 해소하도록 안내 | [x] | 구현 및 자기 검증, `fd9dd5d`. 상세 근거는 [handoff](handoff.md) |
| 3 | 갱신·제거 후에도 프로젝트 파일과 정책 pin 보존 명시 | [x] | 구현 및 자기 검증, `fd9dd5d`. 상세 근거는 [handoff](handoff.md) |
| 4 | packaging version과 정책 version, historical 자기 투영 및 human-review 경계 정합성 확보 | [x] | 구현 및 자기 검증, `fd9dd5d`. 상세 근거는 [handoff](handoff.md) |

## 검증

| 사례 | AC | 명령·작업 디렉토리 | 기대 결과 | 결과 |
| --- | --- | --- | --- | --- |
| <a id="tc-03"></a>TC-03 | AC-04, AC-06 | README·스킬 색인·설치 문서 수동 대조, 리포 루트 | 6개 이름, 후보 제외, 설치/갱신/제거/전환 안내 일치 | 통과: `934236c`, 수동 대조 및 기존 policy/skill source base diff 0·설정 digest 동일 |
| <a id="tc-04"></a>TC-04 | AC-04, AC-05 | 기존 VERSION/manifest/lock/rules와 base diff, 링크 검사 | 정책 정본·사람 승인 유지, pin/manifest digest 보존, 훅 비활성 기본값 | 통과: `934236c`, 수동 대조 및 기존 policy/skill source base diff 0·설정 digest 동일 |

## 제외 범위

- manifest·lock 재수렴, 새 정책 release, 기존 사용자 설치 자동 삭제
