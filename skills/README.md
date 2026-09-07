# Skills

Phase 0는 다음 instruction-only 스킬을 제공합니다.

| 논리 이름 | 설치 가능한 폴더 | 역할 |
| --- | --- | --- |
| `spec-it:specify` | `spec-it-specify` | 프로젝트·변경 의도 작성 |
| `spec-it:clarify` | `spec-it-clarify` | 남은 결정 frontier를 보이는 심문 |
| `spec-it:converge` | `spec-it-converge` | 승인된 결정을 프로젝트 산출물로 투영 |
| `spec-it:check` | `spec-it-check` | 읽기 전용 정책 판정 |
| `spec-it:evolve` | `spec-it-evolve` | 공통 SSOT 진화 |

`spec-it:*` namespace는 향후 plugin packaging에서 사용할 논리 이름입니다. Phase 0는 plugin을 배포하지 않으므로 개별 설치 시 실제 skill name은 하이픈 형식입니다.

`spec-it:evolve`는 대화를 곧바로 한 문서로 옮기지 않습니다. [conversation routing procedure](spec-it-evolve/references/document-routing.md)에 따라 질문·제안·확정 결정과 공개 공통·조건부 profile·project-local·private context를 먼저 나눈 뒤 기존 정본을 갱신합니다.

구현 작업에서는 `spec-it:specify`가 task-start profile preflight를 수행하고, material dependency·infrastructure·data·contract signal만 `spec-it:clarify`로 보냅니다. `spec-it:converge`는 승인된 lint contract와 infrastructure threshold를 투영하고, `spec-it:check`는 완료 전 실제 diff와 brownfield legacy finding을 구분해 읽기 전용으로 보고합니다. 상세 checkpoint는 [agent work cycle](../docs/agent-work-cycle.md)에 있습니다.
