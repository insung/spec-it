# Guard audit — hypothetical-decision boundary

## Verdict

**Pass.** The clarification skill constrains the stated failure mode without
blocking either valid approval preservation or a later, evidence-led question.
No new P1 or P2 finding was identified in this narrow static audit.

## Resolved

- A hypothetical concurrency mode, actor, consumer, failure mode, or
  integration cannot become a material decision merely because it is a
  conceivable edge case. The skill requires an **observed requirement or
  technical trigger**, keeps the item in discovery otherwise, and requires an
  investigation showing an effect on the approved outcome before elevation
  (`source/skills/spec-it-clarify/SKILL.md:26`). This is directly consistent
  with researching discoverable facts before forming the dependency frontier
  (`:12`) and with the conditional, non-survey prompt bank (`:34`).
- The restriction does not turn into a rule to suppress all later questions.
  The same clause permits elevation after a real observed trigger plus
  investigation, and the skill asks unresolved material choices needed to
  make the stated boundaries testable (`:30`). A recommendation approval is
  expressly limited to the frontier actually shown, rather than later
  material decisions (`:30`). Thus a newly evidenced, out-of-frontier
  consequence can be asked as a new decision package.
- Prior human decisions retain their status: delegation scope must be recorded
  and questions stop inside that scope (`:22`); resolved or delegated choices
  must not be asked again (`:36`); and the finish state preserves approval
  evidence and reserves `pending human confirmation` for choices that lack
  approval or delegation (`:42`). The ``scope it actually covers`` qualifier
  (`:36`), together with the frontier-only approval limit (`:30`), prevents a
  later discovered trigger from being silently treated as covered by a broad
  earlier approval.
- The user material supports this boundary. It describes an actual past
  campaign-class omission and a contemplated-but-not-completed integration,
  rather than authorizing the system to manufacture further actors or
  integrations (`review/user-requests.md:7-9`). It also asks for AI
  clarification/read-back and brownfield discovery (`:37-49`), which aligns
  with evidence-led discovery rather than an unconditional question survey.
- When a legitimate new material question is made, HITL-002 still supplies the
  bounded package requirements (options, recommendation, impact, risk,
  expected diff, rollback, and evidence) (`source/rules/hitl/HITL-002.md:7-15`);
  the skill invokes that package for material choices (`source/skills/spec-it-clarify/SKILL.md:40`).

## Unresolved

- None within the requested guard question. The wording has no internal
  conflict that would require a P1/P2 correction: it distinguishes discovery
  from decision elevation, limits the effect of delegation to its recorded
  scope, and permits evidence-backed newly material questions.

## Static-audit limits

This conclusion checks only the supplied user-request excerpt, the
`spec-it-clarify` instruction, and its directly referenced HITL-002 rule. It
does not establish how a particular agent will gather evidence, record a
decision ledger, interpret an ambiguous delegation, or behave at runtime; it
also cannot establish that the excerpt contains every prior user decision.
