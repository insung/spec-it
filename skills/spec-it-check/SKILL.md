---
name: spec-it-check
description: Read a project's pinned spec-it artifacts and report policy status without repairing project files. Use for local review, pre-merge review, release evidence, or diagnosing a policy mismatch.
---

# spec-it:check

Inspect without repairing. Phase 0 has no executable validator, so manual observations and unimplemented checks must remain distinguishable.

## Contract

Select `quick`, `full`, or `release`. Read the exact pinned policy version, manifest, lock, exceptions, relevant files, and evidence. Do not edit project artifacts or policy sources. The only permitted output file is a new ignored report under `.spec-it/reports/` when the user requested a persisted report.

Map changed files and observable contract surfaces to the rule IDs in the lock before judging them. For every applicable finding report the rule ID, trigger, concrete observation, rationale in project terms, practical consequence, and required evidence, exception, or next step. Do not merely quote a normative statement. This explanation is how a user can understand why the project follows the rule and decide whether an exception is justified.

Classify dependency or import, IaC or deployment, runtime or environment configuration, external client or event source, database/cache/stream, stored payload, and public-contract changes as profile re-evaluation signals. Read only the relevant infrastructure evaluation blocks. When an approved decision and guardrail covers the signal, report that coverage and continue; use `human-review` for an unresolved decision, conflict, hard-constraint risk, budget overrun, or missing required evidence.

For executable source, inspect the declared lint contract and run only repository-owned commands that the requested check mode permits. Review project-owned identifiers, semantic callable and collection names, and named layer-boundary data against the selected language and project profiles. A tool's success is evidence for its covered checks, not proof of every semantic rule.

If a brownfield repository has no accepted manifest and lock, label the result `shadow assessment`. Recommend candidate profiles and show likely conflicts, but do not present the repository as compliant or non-compliant with a policy it has not adopted. Keep this assessment read-only unless the user separately approves projection or remediation.

In brownfield reporting, separate violations introduced or touched by the current change from untouched legacy findings. Keep reporting legacy findings with location, impact, and a safe remediation boundary, but do not mass-rename or repair them during a read-only check.

Use only `pass`, `warn`, `fail`, `not-applicable`, and `human-review`. Missing evidence, unresolved decisions, expired exceptions, profile conflicts, and planned-but-unimplemented checks are never `pass`. Explain which observation is manual and which validator is not implemented.

When persisting, use `YYYY-MM-DDTHH-mm-ssZ_<commit>_<mode>.json` and the check-report schema. Secret findings contain only rule ID, path, line, finding type, masked fingerprint, and remediation—never raw text or a recoverable value.

Model exit semantics in the summary: `0` pass with warnings allowed, `1` policy violation, `2` human decision or missing evidence, `3` checker error. Do not claim an actual process exit code unless an executable checker produced it.
