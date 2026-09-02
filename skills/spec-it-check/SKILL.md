---
name: spec-it-check
description: Read a project's pinned spec-it artifacts and report policy status without repairing project files. Use for local review, pre-merge review, release evidence, or diagnosing a policy mismatch.
---

# spec-it:check

Inspect without repairing. Phase 0 has no executable validator, so manual observations and unimplemented checks must remain distinguishable.

## Contract

Select `quick`, `full`, or `release`. Read the exact pinned policy version, manifest, lock, exceptions, relevant files, and evidence. Do not edit project artifacts or policy sources. The only permitted output file is a new ignored report under `.spec-it/reports/` when the user requested a persisted report.

Use only `pass`, `warn`, `fail`, `not-applicable`, and `human-review`. Missing evidence, unresolved decisions, expired exceptions, profile conflicts, and planned-but-unimplemented checks are never `pass`. Explain which observation is manual and which validator is not implemented.

When persisting, use `YYYY-MM-DDTHH-mm-ssZ_<commit>_<mode>.json` and the check-report schema. Secret findings contain only rule ID, path, line, finding type, masked fingerprint, and remediation—never raw text or a recoverable value.

Model exit semantics in the summary: `0` pass with warnings allowed, `1` policy violation, `2` human decision or missing evidence, `3` checker error. Do not claim an actual process exit code unless an executable checker produced it.
