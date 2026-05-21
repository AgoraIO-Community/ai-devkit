# Policy Delivery

> **When to Read This:** Load this document when you are changing shared policy,
> workflow locations, template text, or any file that summarizes conventions for
> other entry points.

## Overview

ai-devkit has to keep multiple agent-facing surfaces aligned without pretending
they are all equal. The repo now uses a source-of-truth hierarchy:

1. shared policy
2. standard
3. canonical workflows
4. repo entry point
5. adapter summaries

## Why This Matters

- If policy lives only in adapters, repos without those adapters lose the rules.
- If workflows live only under `skills/`, prompt users get the wrong mental model.
- If `AGENTS.md` and `docs/ai/` are not real in this repo, the project is selling a pattern it does not use itself.

## Change Propagation

| Change | Required Follow-Up |
| ------ | ------------------ |
| policy wording | update `AGENTS.md`, standard template language, and any adapter summaries |
| workflow move | update README prompts, skill wrappers, install docs, and validator expectations |
| template change | update root `AGENTS.md` and self-hosted `docs/ai/` if descriptions changed |
| compatibility claim | verify the shipped adapter or markdown path exists |

## Compatibility Rule

- Public references should point at canonical docs.
- Compatibility wrappers should continue to work for older skill-path references.
- A path move is complete only when public references and wrappers agree.

## See Also

- [Back to Architecture](../02_architecture.md)
- [Back to Conventions](../04_conventions.md)
- [Back to Workflows](../05_workflows.md)
