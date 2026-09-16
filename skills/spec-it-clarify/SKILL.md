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

Validate discoverable technical claims before presenting a choice. Do not promote a hypothetical actor, concurrency mode, consumer, failure mode, or integration into a material product decision without an observed requirement or technical trigger; keep it as a discovery item and elevate it only if investigation shows it can affect the approved outcome. If a human's rationale does not match the observed topology, platform behavior, or evidence, explain the mismatch and compare feasible alternatives instead of recording the rationale as fact. The human keeps the final choice, but do not converge a choice that violates an approved hard constraint or SLO.

For an infrastructure profile, ask only missing required decisions and project-owned thresholds from its evaluation block. A revisit trigger that remains inside an approved guardrail is a reportable observation, not a new question.

For a broad request such as “build a Lambda,” first discover available repository and environment facts. Ask only the unresolved choices needed to select profiles and make behavior, security, data, cost, deployment, and operational boundaries testable. A request to use the recommendations is valid only for the explicitly shown frontier; it is not blanket approval for later material decisions.

## Read-back and correction

Use examples that distinguish interpretations, not just synonyms. For “immediately,” compare the observed result before save, after save on a new selection, and during an already-running action only when those boundaries matter. Use repository discovery or `spec-it-impact` for facts rather than asking the human to find callers. A conditional prompt bank is: who/which scope, when the result changes, what must remain unchanged, and which exception would change acceptance. Ask only unanswered material branches; it is not a mandatory survey.

When a human corrects the interpretation, retain the earlier interpretation as superseded and update affected scope, source decision, examples, scenarios, paths, and evidence validity. Explain the observable difference back to the human. Reuse an approval only for the scope it actually covers; do not keep asking a choice already resolved or delegated. A conflict among planning, design, and operations goes to the designated decision owner with the consequences, not to majority vote or automatic latest-document precedence.

## Stop conditions

Use the decision package required by `HITL-002` for material choices. Do not converge while observable behavior, security, data, or cost has an unresolved decision. Harmless details may be deferred only with reason and a review trigger.

Finish with a decision ledger, the actual material-open count, and the approval state of selected profiles and infrastructure thresholds. Use `pending human confirmation` only for choices that were not approved or delegated; preserve the approval evidence and do not reopen choices covered by a valid delegation. When material-open is zero, name `spec-it:converge` as the next action.
