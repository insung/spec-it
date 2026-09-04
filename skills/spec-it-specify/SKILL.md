---
name: spec-it-specify
description: Capture a project-wide or material change specification before implementation, separating human intent from technical discovery. Use when starting a project or a change that affects behavior, contracts, security, data, cost, infrastructure, deployment, or architecture.
---

# spec-it:specify

Create the smallest durable statement of intent that can be clarified and verified. This Phase 0 skill is instruction-only; it does not run a validator or claim policy compliance.

## Source order

Read the project's `AGENTS.md`, `.architecture/project.md`, `manifest.yaml`, `lock.yaml`, and relevant accepted ADRs. Resolve policy rules from the exact `policy.version`; do not copy policy text into the project.

## Minimal entry

A short user intent is sufficient. Do not require the user to know profile names, rule IDs, or architecture vocabulary. Discover repository facts first, then explain the recommended scope and profiles in terms of their practical effect.

Treat a request to add or change a route, controller, transport DTO, OpenAPI or protobuf schema, WebSocket or SSE message, public error, or other observable contract as a material `change` trigger even when the user did not explicitly ask to run spec-it. Before implementation, map the requested and touched surfaces to the pinned rule IDs. If the required capability is not selected, record that as a decision for `spec-it:clarify`; do not silently extend the project profile.

## Scope

- Use `project` scope for a new baseline or a project-wide architecture change.
- Use `change` scope when behavior, public contract, security, data, cost, infrastructure, deployment, or architecture changes.
- A documentation typo, formatting-only edit, or proven non-behavioral refactor may be exempt with a reason.

## Specification

Capture why, affected users, observable outcome, success measures, non-goals, constraints, affected categories, acceptance criteria, rollback boundary, and open decisions. Humans own why, what, acceptance, and core constraints. Research discoverable facts instead of asking the human to supply them.

For change scope, use `.architecture/changes/<YYYYMMDD-short-slug>/spec.md`; add a sequence suffix for same-day collisions. Keep one active specification file. Start in `draft` or `clarifying` when material decisions remain. Do not implement during this skill.

At the end, report what is known, the open decision frontier, and whether `spec-it:clarify` is required.
