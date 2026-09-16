# 최종 후보 독립 의도–구현 감사

## 범위와 결론

`review/user-requests.md`의 사용자 발췌에서 요구를 먼저 추출하고 `source/`의 스킬·템플릿·설명·관련 규칙에 직접 대조했다. 구현자의 평가, 실제 응답 묶음, 기존 독립 검토, 원 작업공간, 메모리, 네트워크는 읽지 않았다. 후보 파일을 수정하거나 실행 행동 시험을 하지 않았다.

**발췌에 나타난 핵심 요구는 절차와 선택적 기록 형식으로 대부분 구체화되어 있다. 치명적 핵심 요구 누락이나 QA 제품·폴더를 모든 구현 프로젝트에 강제하는 변경은 확인하지 못했다.** 다만 확인을 끝낸 결정을 다시 승인 대기로 돌릴 수 있는 스킬 문구 모순 1건이 있다. 실제 자동 선택·행동 재현, 이번 작업의 자기 적용 완료, 원래 사건의 원인 규명은 이 감사의 자료만으로 통과 처리할 수 없다.

여기서 “반영 확인”은 실제 파일에 필요한 지침이 있다는 뜻이다. 지침대로 모델이 항상 행동했다거나 사용자의 실제 시스템에서 QA를 수행했다는 뜻은 아니다.

## 발견 사항

### F-1 — P2 / 상충 지침: 이미 승인·위임한 결정을 종료 보고에서 다시 승인 대기로 표현한다

- 근거: `source/skills/spec-it-clarify/SKILL.md:22`는 제시된 선택의 위임을 승인 증거로 기록하고 그 범위의 질문을 끝내라고 한다. 같은 파일 `:36`도 이미 해결·위임된 선택을 다시 묻지 말라고 한다.
- 반대 지침: 같은 파일 `:42`는 종료 시 항상 “selected profiles and infrastructure thresholds pending human confirmation”을 보고하도록 한다. 미승인인 경우라는 조건이 없다.
- 재현 가능한 상황: 사용자가 현재 frontier의 권장안을 명시적으로 위임하고 material open 항목이 0이 된 경우, 앞부분은 다음 수렴으로 진행하게 하지만 마지막 문장은 같은 선택을 다시 승인 대기로 표시하게 한다.
- 영향: 필요한 차이만 되읽어 확인하고 이미 정한 사항을 반복하지 않는 흐름을 약화한다. 사용자는 결정이 끝났는지 다시 답해야 하는지 알기 어렵고 다음 스킬이 불필요하게 멈출 수 있다.
- 권고: 종료 요약에 실제 승인·위임 상태를 그대로 기록하고, 승인되지 않은 선택에만 `pending human confirmation`을 쓰도록 조건을 명시한다. `spec-it-converge`의 이미 위임된 범위는 재확인하지 않는 조건과 맞춘다.
- 한계: 기준선 파일을 읽지 않았으므로 이번 후보가 새로 만든 회귀라고 주장하지 않는다. 최종 후보 자체에 남은 모순이다.

## 핵심 요구 추적

| 사용자 요구 | 후보의 실제 구현 근거 | 판정과 한계 |
| --- | --- | --- |
| 기획을 읽었는데 유형별 적용이 빠지는 문제와 부작용을 발견 | `skills/spec-it-impact/SKILL.md:26-39`의 caller/strategy/consumer, 설정 쓰기·읽기, 저장·계약·관찰 경계 탐색; `examples/intent-verification/README.md`의 A/B 경로 및 미변경 caller 예 | 반영 확인. 변경 파일 밖의 소비자를 찾으며 미접근을 미적용으로 바꾸지 않는다. 원 사건의 실제 원인은 조사 자료가 없어 미확인이다. |
| 열 번 반복 같은 규칙보다 누락 여부를 알 수 있는 검토 | `docs/intent-and-verification.md:15-21`, `skills/spec-it-check/SKILL.md:16-20` | 원문↔해석↔시나리오↔경로↔관찰의 양방향 대조, 끊긴 연결과 수정 대상 보고로 구체화했다. 반복 횟수와 AI 작성 표 내부 일관성은 원문 완전성의 증거가 아니라고 명시한다. |
| AI가 왜곡을 줄이도록 사람이 제공할 최소 기획과 질문 | `skills/spec-it-specify/SKILL.md`의 Minimal entry/Specification, `templates/project/change-spec.md`의 Read-back and source, `docs/intent-and-verification.md:5-9` | 한 문장 의도부터 시작하고 기술 사실은 AI가 조사한다. 정상 예·반례·유지 조건·대상·시점으로 구체화하며 모든 서식의 사전 작성을 요구하지 않는다. |
| AI의 실제 되읽기, 정정과 이해 격차 감소 | `skills/spec-it-specify/SKILL.md:36`, `skills/spec-it-clarify/SKILL.md`의 Read-back and correction, `templates/project/AGENTS.md:17` | 단순 동의 대신 결과 차이를 되읽고 정정 시 시나리오와 증거 유효성을 갱신한다. 역할 충돌은 결정자에게 보내며 모든 이해관계자의 일치를 요구하지 않는다. F-1 문구 정리가 필요하다. |
| QA를 기획 일치 검사에 한정하지 않고 고객 문제 해결과 제품 이해에 연결 | `docs/intent-and-verification.md:23-29`, `templates/testing/acceptance-case.md` | 기획 적합성·고객 목적·탐색 가설을 분리하고 실제 결과 경계를 확인하게 한다. 저장 성공이 실제 제외 성공을 대신하지 않는 예도 있다. 실제 고객 목적 달성의 관찰 자료는 프로젝트에서 필요하다. |
| 이전→신규 업데이트, 클라이언트/서버 조합, 회귀, DB 확인 | `docs/intent-and-verification.md:29`, `templates/testing/verification-run.md:8-11`, `rules/testing/TST-003.md`, `rules/testing/TST-006.md` | 지원 조합·순서, 이전/이후 데이터, null/default, 부분 적용, 쓰기 후 rollback, 비대상 회귀가 명시된다. 위험별 선정이며 모든 조합 실행을 강제하지 않는다. 계획과 실제 실행을 구별한다. |
| QA 사례·버전·실행 결과 관리, 정상 확인 코멘트 보존 | `templates/testing/acceptance-case.md`, `templates/testing/verification-run.md:3-25`, `docs/intent-and-verification.md:37` | Case revision과 Run ID를 분리하고 실패→수정→후속 run을 보존한다. 당시 대상·환경·기대·관찰·확인자·완료 코멘트를 기록한다. 새 기획으로 과거 통과를 덮어쓰지 않는다. |
| Notion/Figma 등 원래 도구를 유지하며 변경 전체를 추적 | `docs/intent-and-verification.md:31-39`, `docs/traceability.md`의 변경과 QA의 연결 | 원본 권한을 유지하고 상위 변경 기록과 Change/Scenario ID로 연결한다. 원문 링크 반복 복사나 팀 전체 GitHub 이전을 요구하지 않는다. 자동 수집·동기화·통합 UI는 제공하지 않는다고 정확히 구별한다. |
| QA 시트 위치 선택 및 구현·QA 저장소 분리 | `docs/intent-and-verification.md:35`, `examples/intent-verification/README.md`, `templates/testing/acceptance-case.md:3`, `skills/spec-it-converge/SKILL.md` | 기존 문서 DB·시트·이슈·별도 QA 저장소를 허용하고 구현/QA commit과 결과 참조로 연결한다. 새 QA 폴더나 사례 schema는 수렴 전제조건이 아니다. |
| 문제 발생 시 무엇을 고칠지 파악하고 재발 방지 | `skills/spec-it-check/SKILL.md:20`, `templates/testing/verification-run.md:19-24`, `examples/intent-verification/README.md` 마지막 문단 | 결정·디자인·계약·코드·데이터·환경을 구분하고 원인 불확실성을 보존한다. 결함→수정→회귀 case→후속 run으로 연결한다. 개별 가설을 확정 원인이나 모든 프로젝트의 새 공통 의무로 승격하지 않는다. |
| 브라운필드, 절차 누락, 세션 간 발견과 SSOT 부재 | `skills/spec-it-impact/SKILL.md:12-47`, `templates/project/change-impact.md`, `skills/spec-it-specify/SKILL.md`의 late-entry | 미채택 shadow assessment와 구현 후 late-entry를 분리한다. commit뿐 아니라 dirty·원본 revision·관측 시각·미접근·재검토 trigger를 인계한다. 관계 파일과 문서 허브는 필수가 아니다. 기록 없는 과거를 꾸미지 않는다. |
| 기존 스킬이 커지면 새 스킬로 분리 | `skills/spec-it-impact/SKILL.md:43-47`, `skills/README.md` | 영향 조사를 독립 read-only 역할로 분리하고 specify/clarify/converge/check의 책임을 구분했다. 미설치 대체 인계와 별도 설치 시 템플릿 상대 링크의 복구 경로도 있다. |
| System Book 반영 여부와 다른 작성 세션 의존성 | `skills/spec-it-evolve/SKILL.md:20`, `skills/spec-it-evolve/references/document-routing.md` | 원칙 문서 인계에 문제·관찰/가설·결정·반례·근거·공개 경계를 보존하며 분석은 독립 진행 가능하다고 한다. 같은 원고 수정 전 최신 상태와 겹침 확인을 요구한다. 실제 비공개 원고 인계·반영 여부는 이 후보만으로 확인할 수 없다. |
| 이번 비코드 작업에도 먼저 사례를 만들고 구현·검증 | `skills/spec-it-evolve/SKILL.md:18`, `docs/tdd-and-verification.md:7`, `rules/testing/TST-002.md` | baseline/candidate 실제 응답과 독립 검토를 구별하는 절차는 있다. baseline 통과를 억지로 red로 만들지 않으며 사후 테스트를 사전 TDD로 소급하지 않는다. 이번 작업이 실제 그 순서로 실행됐는지는 허용 자료 밖이므로 미확인이다. |
| 0.4.0과의 영향 확인, 무단 설치·출시 없이 진행 | `docs/migrations/0.4.0-to-0.5.0.md:3-24`, `CHANGELOG.md:5-11`, `.architecture/manifest.yaml`, `AGENTS.md:4-11` | 미발행 후보 및 현재 0.4.0 고정을 분명히 한다. 정책 digest와 스킬 source 동일성을 구분하고 기존 lock 문제를 숨기지 않는다. 이번 정적 감사는 실제 원격 tag·release 상태를 검증하지 않았다. |

표의 경로는 모두 `source/` 기준이다.

## 과잉·도입·부작용·자동화 오해 구분

### 과잉 요구

읽은 후보에는 QA 제품, 전용 저장소, 공통 QA schema, 모든 업데이트 조합의 실행, 모든 필드 설문, 열 번 재검토를 일반 의무로 추가하는 내용이 없다. 기존 change spec의 `.architecture/changes/.../spec.md` 위치는 유지되지만 이는 기획자·디자이너의 원본 도구나 QA 결과 저장소까지 이전하라는 지침은 아니다. 새 선택 템플릿의 부재를 정책 위반으로 처리하지 않도록 check와 설명 문서가 경계를 둔다.

### 남는 도입 위험 — 결함과 별개

1. **자동 발견·준수의 공백:** 스킬 지침과 AGENTS 투영을 실제 작업 모델이 읽고 따르는지는 실행 증거가 필요하다. `docs/intent-and-verification.md:51`은 명시적인 검토 요청의 합성 실행이 평소 구현 요청에서 자동 선택되는지까지 보장하지 않는다고 밝힌다. 따라서 “이제 적용만 하면 항상 되읽는다”는 완료 보고는 허용되지 않는다.
2. **수동 연결의 유지 비용:** 상위 변경 기록에 source revision, 사례와 run, 외부 QA 결과를 연결하는 업무는 남는다. `docs/intent-and-verification.md:39`의 한계 설명이 적절하다. Redmine+SVN 수준의 통합 경험이 구현됐다고 볼 수 없으며, 기존 도구만으로 유지하기 어려운지는 프로젝트의 실제 운영량으로 판단해야 한다.
3. **검사와 지속 기록의 인계:** impact는 결과를 반환하고 호출자가 승인된 기록에 저장한다(`skills/spec-it-impact/SKILL.md:43`). check의 schema 밖 자문은 응답 또는 별도로 승인된 기록 담당에게 인계한다(`skills/spec-it-check/SKILL.md:32`). 저장 담당·위치가 없으면 다음 세션의 연속성이 확보되지 않는다. 후보는 이 한계를 명시하므로 이를 무단 파일 생성으로 메우면 안 된다.
4. **source 고정 범위:** 후보 안내가 지적한 것처럼 정책 digest만으로 실제 사용하는 스킬·템플릿의 동일성은 입증되지 않는다(`docs/migrations/0.4.0-to-0.5.0.md:11`). 0.4.0 lock 불일치의 과거 계산 사실은 이 감사에서 재현하지 않았다. 해당 문서에 적힌 수치를 독립 계산 결과로 재인용하거나 현재 무결성 통과라고 보고할 수 없다.

### 자동화되었다고 오해할 표현

핵심 새 문서와 스킬은 watcher·runner·validator·CI enforcement의 미구현, 합성 사례, 계획/관찰, 과거 통과/현재 유효성, 수동 점검/자동 통과를 반복해서 구분한다. 읽은 범위에서 이 한계를 뒤집는 새 자동화 완료 주장은 확인하지 못했다. `README.md`의 “...정도면 충분합니다” 같은 일반 사용 설명도 자동 차단이 없다는 앞 문단과 함께 읽어야 하며 실제 준수율의 증거가 되지 않는다.

## 완료 주장과 이번 감사의 한계

- `source/CHANGELOG.md:11`과 `source/docs/migrations/0.4.0-to-0.5.0.md:28`은 후보 행동 실행·독립 검증·최종 lock 확인 등을 미완료로 적고 있다. 실제 작업에서 완료된 항목이 있다면 최종 인계에서 그 증거와 현재 상태를 구별해야 한다. 이 감사는 응답 묶음이나 기존 평가를 읽지 않았으므로 이 상태가 오래된 것인지 판정하지 않는다. 발행은 사용자 발췌의 승인 범위 밖이므로 미발행 자체를 미완료 결함으로 세지 않는다.
- `source/.architecture/`에는 self manifest/lock/project/ADR가 있지만 읽을 수 있는 후보 범위에서 이번 변경의 활성 명세와 사전 사례·실행 기록은 확인되지 않았다. 이 기록이 임시 또는 비공개 작업 영역에 존재할 수 있으므로 공개 source에 억지로 추가해야 한다는 결론은 내리지 않는다. 자기 적용의 실제 실행 완료는 별도 증거 확인 대상이다.
- 사용자 원문 발췌는 첨부 경로, annotation 메타데이터, 중복 진행 요청, 중간 AI 답변, 과거 대화 전체와 비공개 사고 문서 자체를 포함하지 않는다. “너의 계획에 동의한다”가 승인한 구체적 계획을 여기서 완전히 복원할 수 없다. 사용자 발췌에 직접 드러난 의도에 대한 감사이지 원문 전체 무누락 감사는 아니다.
- 원래 Kotlin/Golang 관련 사건의 코드·기획 원본을 조사하지 않았다. 여러 업무 병행은 사용자 회고이고 원인 가설로 취급해야 한다. 후보가 이를 일반 규칙의 확정 사고 원인으로 복사하지 않은 것은 적절하다.
- 본 결과는 instruction의 정적 의미 감사다. 자동 validator 판정, 일반 모델 성공률, 실제 고객 목적 달성, 운영 QA 완료, release 준비 완료를 뜻하지 않는다.

## 최종 판정

핵심 의도에 대한 정적 지원은 확인했다. F-1의 승인 상태 종료 문구를 정리하는 것이 좋다. 실제 행동 및 자기 적용 증거는 이 독립 감사가 보지 않은 별도 자료와 대조해야 하며, 현재 후보는 도입 가능한 절차 초안과 자동화된 누락 방지 시스템을 분명히 구별하고 있다.
