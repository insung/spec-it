# spec-it agent entry point

<!-- spec-it:managed:start -->
> Generated guidance block. Do not edit this block directly. Policy version: 0.7.0.

- Read [`.architecture/project.md`](.architecture/project.md) for purpose and non-goals.
- Treat [`rules/`](rules/README.md) as the only normative rule source.
- Use [`.architecture/manifest.yaml`](.architecture/manifest.yaml) as approved input and [`.architecture/lock.yaml`](.architecture/lock.yaml) as the resolved view.
- Treat the Claude active policy loop as a local opt-in adapter, not a universal validator or CI gate.
- Keep public core free of personal and company-specific information.
- Checks without a deterministic implementation remain `human-review`; never report them as passed.
- Do not auto-upgrade policy pins or replace final human approval with hook output.
<!-- spec-it:managed:end -->

<!-- project:owned:start -->
## Project-owned guidance

- Documentation starts in Korean; filenames, rule IDs, schema fields, and code identifiers use English.
- Keep one rule ID in one Markdown file with YAML front matter.
- Non-normative docs, templates, and examples link rule IDs instead of creating new obligations.
<!-- project:owned:end -->
