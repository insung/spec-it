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

## Repository-scoped discovery

공통 정책과 함께 배포할 때는 각 skill folder를 저장소의 `.agents/skills/` 아래에 두거나 그 위치에서 이 저장소의 `skills/<skill-name>`을 가리키는 symlink를 사용합니다. Agent는 작업 시작 디렉터리에서 저장소 root까지 올라가며 `.agents/skills`를 찾으므로, 공통 skill을 발견해야 하는 세션은 해당 저장소 안에서 시작합니다. nested Git repository가 경계를 만들면 상위 저장소의 skill이 발견되지 않을 수 있습니다.

개인 전역 설치가 의도된 경우에만 `$HOME/.agents/skills/`를 사용합니다. 설치·symlink 변경 후 현재 세션에 skill이 나타나지 않으면 새 task를 시작해 다시 discovery 합니다. 채택 프로젝트의 [AGENTS template](../templates/project/AGENTS.md)은 machine-specific 경로 대신 canonical policy source와 exact version을 기록하고, lock의 digest·revision으로 실제 읽은 내용을 고정합니다. 이 경로 계약은 [OpenAI의 skills 안내](https://learn.chatgpt.com/docs/build-skills)를 따르되, Phase 0 spec-it은 설치 자동화나 plugin package를 제공하지 않습니다.

`spec-it:evolve`는 대화를 곧바로 한 문서로 옮기지 않습니다. [conversation routing procedure](spec-it-evolve/references/document-routing.md)에 따라 질문·제안·확정 결정과 공개 공통·조건부 profile·project-local·private context를 먼저 나눈 뒤 기존 정본을 갱신합니다.

구현 작업에서는 `spec-it:specify`가 task-start profile preflight를 수행하고, material dependency·infrastructure·data·contract signal만 `spec-it:clarify`로 보냅니다. `spec-it:converge`는 승인된 lint contract와 infrastructure threshold를 투영하고, `spec-it:check`는 완료 전 실제 diff와 brownfield legacy finding을 구분해 읽기 전용으로 보고합니다. 상세 checkpoint는 [agent work cycle](../docs/agent-work-cycle.md)에 있습니다.
