---
name: spec-it-specify
description: Capture a project-wide or material change specification before implementation, separating human intent from technical discovery. Use when starting a project or a change that affects behavior, contracts, security, data, cost, infrastructure, deployment, or architecture.
---

# spec-it:specify

Create the smallest durable statement of intent that can be clarified and verified. This Phase 0 skill is instruction-only; it does not run a validator or claim policy compliance.

## Source order

Read the project's `AGENTS.md`, `.architecture/project.md`, `manifest.yaml`, `lock.yaml`, and relevant accepted ADRs. Resolve policy rules from the exact `policy.version`; do not copy policy text into the project.

At task start, perform a lightweight profile preflight from the request, planned files, repository language and tooling, dependency manifests, IaC, runtime configuration, external clients, storage, and public contracts. This classifies likely rules; it does not run expensive tests or mutate project policy.

For material behavior or scope uncertainty, use `spec-it-impact` if available to discover variants, execution paths, unchanged consumers, and source freshness. Otherwise return the same bounded discovery facts yourself; a missing optional skill is not a reason to invent coverage. Keep source locator/section, revision or permitted snapshot, approval evidence, observed time, inaccessible areas, and refresh conditions in the active change record. A source link alone does not prove its current contents.

## Minimal entry

A short user intent is sufficient. Do not require the user to know profile names, rule IDs, or architecture vocabulary. Discover repository facts first, then explain the recommended scope and profiles in terms of their practical effect.

Treat a request to add or change a route, controller, transport DTO, OpenAPI or protobuf schema, WebSocket or SSE message, public error, or other observable contract as a material `change` trigger even when the user did not explicitly ask to run spec-it. Before implementation, map the requested and touched surfaces to the pinned rule IDs. If the required capability is not selected, record that as a decision for `spec-it:clarify`; do not silently extend the project profile.

Treat a new dependency or import, IaC or deployment topology, runtime or environment setting, external client or event source, database/cache/stream, or stored payload as an infrastructure re-evaluation signal. If an approved decision and guardrail already covers it, record the coverage and continue. Otherwise add only the material decision to the clarification frontier.

## Scope

- Use `project` scope for a new baseline or a project-wide architecture change.
- Use `change` scope when behavior, public contract, security, data, cost, infrastructure, deployment, or architecture changes.
- A documentation typo, formatting-only edit, or proven non-behavioral refactor may be exempt with a reason.

## Specification

Capture why, affected users, observable outcome, success measures, non-goals, constraints, affected categories, acceptance criteria, rollback boundary, and open decisions. Humans own why, what, acceptance, and core constraints. Research discoverable facts instead of asking the human to supply them.

Read back the smallest consequential interpretation in the user's language: who gets what result, a concrete normal example, a counterexample, and what stays unchanged. Separate source facts, retrospective hypotheses, proposals, and approved decisions. Show source corrections and conflicting role meanings rather than accepting the latest wording as authority. Ask only the unresolved distinction that changes the result; do not turn every template field into a questionnaire or require all stakeholders to agree.

Link original intent to scenario, applicable variant/path, observable result, and planned evidence. Reuse the project's existing identifiers and tools. Small changes can use one row; larger changes may reference a separate QA case set. Evidence can remain outside the implementation repository. Keep deferred requirements with reason, owner, and revisit condition instead of deleting them from the trace.

If work already started, record `late-entry`, the actual known revision and dirty state, work already done, and missing pre-change evidence. Recover intent and plan retrospective reproduction/regression without inventing earlier approval or a failing-before-implementation test. Preserve other sessions' edits. Missing manifest/lock means adoption is still a separate decision.

For change scope, use `.architecture/changes/<YYYYMMDD-short-slug>/spec.md`; add a sequence suffix for same-day collisions. Keep one active specification file. Start in `draft` or `clarifying` when material decisions remain. Do not implement during this skill.

At the end, report what is known, the applicable profiles and rule IDs, the open decision frontier, and whether `spec-it:clarify` is required.
