---
name: spec-it-evolve
description: Change the shared spec-it policy SSOT, profiles, schemas, or enforcement level with lifecycle and compatibility discipline. Use for common policy evolution, not for upgrading one project's pinned version.
---

# spec-it:evolve

Evolve the public policy source without turning every local preference into a universal rule. Project policy upgrades belong to a new clarify-and-converge run.

## Change standard

Identify the demonstrated need, affected rules and profiles, false-positive or maintenance impact, compatibility effect, and SemVer result. A new profile needs an actual project need, a unique rule, a repeating independent axis, or a separate template or validator.

Keep one rule ID per Markdown file. Never reuse an ID or silently change its meaning. Every rule has a one-sentence rationale and `origin.type`; add a detailed external reference only for standards, measurements, incidents, enforcement changes, or disputed rules where evidence matters.

Update linked profiles, schemas, examples, index links, changelog, and migration guidance in the same change. Enforcement may be promoted or demoted with evidence and approval. Security or data-loss prevention can become an immediate automation candidate; ordinary policy becomes an automation candidate after the same violation appears in at least two independent tasks.

Finish by reporting compatibility, required project reconvergence, and anything still `planned` or `human-review`. Do not publish packages or plugins in Phase 0.
