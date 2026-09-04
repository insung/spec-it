---
name: spec-it-clarify
description: Resolve material architecture and product decisions through a bounded dependency-aware interview. Use when a spec has ambiguity affecting behavior, contracts, security, data, cost, infrastructure, deployment, architecture, or profile conflicts.
---

# spec-it:clarify

Turn open decisions into explicit human-owned choices without making the interview feel endless. This Phase 0 skill is instruction-only.

## Build the frontier

Read the active spec, project manifest, profiles, rule sources, and evidence. Separate discoverable facts from value or risk choices. Research facts first. Build a dependency graph and ask only decisions whose prerequisites are resolved.

Before every round show:

- resolved decision count;
- open decision count;
- questions in the current frontier;
- estimated remaining-round range;
- any reason the estimate changed.

Batch the whole current frontier. Number questions stably, give a recommended answer and concrete tradeoff, and avoid asking downstream questions early. A human may answer directly, amend the option, or delegate stated remaining choices to the recommendations. Record the delegation scope as the approval evidence and stop asking within that scope.

Ask in the user's language, not in policy vocabulary. For every question explain why the decision is needed now, the recommended default, the cost or risk of each meaningful option, and which artifact or implementation boundary will change. Do not dump every applicable rule when a smaller decision package is sufficient.

For a broad request such as “build a Lambda,” first discover available repository and environment facts. Ask only the unresolved choices needed to select profiles and make behavior, security, data, cost, deployment, and operational boundaries testable. A request to use the recommendations is valid only for the explicitly shown frontier; it is not blanket approval for later material decisions.

## Stop conditions

Use the decision package required by `HITL-002` for material choices. Do not converge while observable behavior, security, data, or cost has an unresolved decision. Harmless details may be deferred only with reason and a review trigger.

Finish with a decision ledger, zero-material-open confirmation, selected profiles pending human confirmation, and the next action `spec-it:converge`.
