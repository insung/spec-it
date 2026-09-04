# Conversation to canonical document routing

Use this procedure when a conversation proposes, questions, approves, or revises shared spec-it policy. It prevents one conversation from becoming one arbitrary document and prevents an AI recommendation from becoming a human decision.

## Classify before editing

Split the input into the smallest independently classifiable statements. For each statement record:

| Field | Allowed meaning |
| --- | --- |
| status | fact, question, proposal, approved-decision |
| scope | public-common, profile-conditional, project-local, private-context |
| existing authority | rule ID, approved manifest/ADR, external standard, or none |
| target | existing canonical file, proposed new canonical file, open change item, or no-write |
| impact | linked rules, profiles, schemas, templates, examples, migration, enforcement |
| uncertainty | missing human decision or fact to investigate |

Do not infer approval from agreement with a nearby statement, implementation progress, or an AI recommendation. A question and an unapproved proposal remain open items. Preserve private and company-specific motivation outside the public core; only an approved generalized obligation can enter this repository.

## Choose the canonical target

1. Search rule IDs, documents, profiles, schemas, and templates for the same meaning.
2. Update the existing canonical source when its identity and meaning remain stable.
3. Add a rule only for a reusable obligation with clear condition, evidence, exception, owner, and enforcement state.
4. Add or change a profile only for conditional applicability, parameters, evidence freshness, or conflict—not to copy rule prose.
5. Put reasoning, relationships, and choice guidance in `docs/`; it cannot create an obligation.
6. Put machine-readable artifact shape in `schemas/` and a disposable starting copy in `templates/` only when a real repeated artifact needs it.
7. Put one project's version, cost, endpoint inventory, LTS duration, and exception in that project's manifest, ADR, contract, or change spec rather than public defaults.
8. Keep raw discussion, unsupported speculation, and duplicated summaries out of the SSOT.

If several topics appear in one conversation, route them independently. If one topic affects several canonical sources, identify one source of meaning and update only its projections and links.

## Build an edit proposal

Before mutation, show the human a compact routing result: source statement, classification, existing or new target, affected rule IDs, proposed compatibility/version effect, and material open decisions. Do not restart clarification for resolved decisions. Ask only questions whose answers materially change behavior, security, data, cost, infrastructure, profile composition, or public commitments.

When the human delegates ordinary remaining choices to recommendations, record the delegation boundary and proceed. Do not treat delegation as authority for new external actions, publication, project upgrades, or private-data movement.

## Evolve and verify

- Follow one rule ID per file and never silently redefine or reuse an ID.
- Update linked profiles, schemas, templates, examples, indices, changelog, and migrations in the same change only when their projection actually changed.
- Separate policy release from project reconvergence. Never auto-upgrade a pinned project.
- Report each enforcement target and implementation truth. Planned automation is `human-review` or `not-implemented`, never pass.
- Check for duplicate obligations, unresolved relative links, orphaned profile rule IDs, schema failures, private markers, and compatibility impact.
- Report no-op when the discussion is already covered; more files are not evidence of successful evolution.

## Examples of routing

- “Could JSON be camelCase?” is a question until approved. If approved as a conditional HTTP convention, route the obligation to an API rule and explanation to the API document.
- “This service promises two years of LTS” is project-local even when lifecycle metadata is a common obligation.
- “Our company once stored policy in procedures” is private context. A generalized approved boundary may become an architecture or data rule without copying the company case.
- “A shared domain release changed approval calculation” routes release impact to compatibility policy and each consumer's assessment to project artifacts; it does not force unrelated consumers to update.
