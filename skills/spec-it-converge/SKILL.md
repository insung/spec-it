---
name: spec-it-converge
description: Convert an approved project or change specification into a pinned manifest, resolved policy view, ADRs, and concise AGENTS.md guidance. Use after material clarification is complete or explicitly delegated.
---

# spec-it:converge

Project approved intent into stable repository artifacts. This Phase 0 skill is instruction-only; deterministic lock generation is a target contract, not an implemented executable.

## Preconditions

Read the active spec and decision ledger. Refuse convergence when any open item affects observable behavior, security, data, or cost. Recommend a flat combination from risk, project-kind, language, runtime, deployment, and capability profiles. Obtain human confirmation unless the human already delegated the remaining choices to the stated recommendations.

## Projection

Create or update:

- `.architecture/project.md` for durable purpose and boundaries;
- `.architecture/manifest.yaml` as human-approved input with exact policy version;
- `.architecture/lock.yaml` as a sorted resolved view with a generated marker and no timestamp;
- `.architecture/decisions/` for durable tradeoffs and revisit triggers;
- the managed block of `AGENTS.md`, preserving the user-owned block.

Merge the generated-artifact entries from the project template's gitignore fragment into the repository `.gitignore`. Preserve every existing user entry and comment, avoid duplicates, and do not replace the whole file. At minimum, keep `.spec-it/reports/`, local environment files, caches, and generated check output out of version control unless the project explicitly approves them as evidence.

For executable source, project the repository-owned lint contract: tools or compiler evidence, configuration, commands, source scope, and CI target state. For infrastructure profiles, project approved guardrails and revisit thresholds into manifest parameters and keep evidence and tradeoffs in ADRs. Do not copy common profile prose or invent numeric defaults.

In a monorepo keep shared choices in the root manifest and differences in deploy-unit manifests. Detect profile conflicts; never invent silent precedence.

Ensure the managed `AGENTS.md` block tells agents to perform task-start preflight, material-signal re-evaluation, and pre-completion diff checking. Because Phase 0 has no lock generator, label deterministic-lock evidence `human-review` and do not claim byte reproducibility was mechanically proved. Report every file changed and hand off to `spec-it:check`.
