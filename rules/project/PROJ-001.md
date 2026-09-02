---
id: PROJ-001
title: Environment file convention
status: active
introduced: 0.1.0
scope: all-projects
condition: "A project uses environment-based configuration."
statement: "MUST track only .env.example or .env.<name>.example and ignore .env plus all .env.* value files."
forbidden: ["Commit real credentials or production values.", "Use an example file containing a usable secret."]
evidence: ["Gitignore rules and safe example files."]
exception: {allowed: false, requirements: []}
approver: [security-owner]
rationale: "A uniform convention makes secret leakage easier to prevent across frameworks."
origin: {type: design-interview}
enforcement: {mode: ci, implementation: planned}
---

# PROJ-001 — Environment files

권장 ignore 순서는 `.env`, `.env.*`, `!.env.example`, `!.env.*.example`입니다.
