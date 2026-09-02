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

## Stop conditions

Use the decision package required by `HITL-002` for material choices. Do not converge while observable behavior, security, data, or cost has an unresolved decision. Harmless details may be deferred only with reason and a review trigger.

Finish with a decision ledger, zero-material-open confirmation, selected profiles pending human confirmation, and the next action `spec-it:converge`.
