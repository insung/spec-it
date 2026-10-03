---
name: spec-it-pair
description: Work through project-specific architecture, infrastructure, or implementation questions with the user as a pair. Use when the user asks what this project should choose or wants to design or implement together. Answer generic knowledge questions directly instead.
---

# spec-it:pair

Status: optional, unpublished instruction candidate. Start from project `AGENTS.md` and pinned manifest/lock with existing skills when needed; this candidate is not a required entry point. Source presence does not prove host installation, exposure, or automatic selection. Added necessity and real-project benefit remain unverified.

Keep one shared problem in view while the human and AI investigate, decide, implement, and verify in small steps. The human owns purpose, acceptance, and material risk; the AI investigates discoverable facts and proposes or performs work within the approved scope. Pairing does not grant new edit or external-action authority.

## Enter from the user's question

- Answer the immediate question. For a project-specific recommendation, inspect the available repository, deployment definitions, tests, `AGENTS.md`, project intent, approved manifest/ADRs, and the lock's applicable rule IDs before treating a technology choice as actionable. If the policy is not adopted, describe candidates as a shadow assessment, not compliance.
- Say what is observed, inferred, approved, and unknown. Give a provisional recommendation and the smallest useful next investigation, experiment, or human choice. Ask only about a material distinction that cannot be discovered from the project. A general explanation needs no pair workflow or project artifact.
- Read the pinned constitution when the answer involves tradeoffs, then use applicable pinned rules rather than a memorized philosophy checklist. Check hard constraints, total cost, current product stability, and consistent policy interpretation in that order when relevant. In particular, respect authority and human decision ownership (`GOV-001/002`, `HITL-001/002`), hard constraints and total cost (`COST-001/002`), and the selected infrastructure profile's evaluation and revisit conditions (`INFRA-001/002`). Do not claim an unselected rule applies. Do not present a proposal as an approved decision or an unmeasured outcome as observed.

## Work as a pair

- Let either partner drive a small step: the user may edit while the AI reviews evidence, or the AI may implement within the user's authorized scope while the user guides the outcome. Confirm roles only when ambiguous or consequential; do not require a ceremony for every turn.
- Keep the loop short: current hypothesis, one meaningful check or change, observed result, then the next choice. If an approved decision and guardrail cover the step, continue without asking again. If a new material choice or hard constraint appears, use the bounded decision package from `HITL-002` before the affected mutation.
- When the user corrects the goal or interpretation, update the working hypothesis and any affected evidence. Inspect the actual diff and test result before describing completion. Do not infer unseen editor changes, external state, or a successful policy check.
- For material project or change work, use `spec-it:specify`, `spec-it:clarify`, `spec-it:converge`, `spec-it:impact`, and `spec-it:check` only as their respective conditions require and when those skills are available; otherwise perform the necessary bounded work directly. Preserve an approved decision in the existing change record or ADR when it needs to survive the session; do not create a document for every question. Keep private motivation outside the public policy core.

Finish with the answer or implemented outcome, the evidence and remaining unknowns, and the next action only if one is needed. This skill is an interaction procedure; `rules/` remains the sole normative policy source.
