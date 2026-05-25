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

## Why This Matters

- If policy is scattered across ad-hoc files, repos lose the rules.
- If `AGENTS.md` and `docs/ai/` are not real in this repo, the project is selling a pattern it does not use itself.

## Change Propagation

| Change | Required Follow-Up |
| ------ | ------------------ |
| policy wording | update `AGENTS.md` and standard template language |
| workflow move | update README prompts and validator expectations |
| template change | update root `AGENTS.md` and self-hosted `docs/ai/` if descriptions changed |
| compatibility claim | verify the shipped markdown path exists |

## Compatibility Rule

- Public references should point at canonical docs.
- A path move is complete only when all public references are updated.

## See Also

- [Back to Architecture](../02_architecture.md)
- [Back to Conventions](../04_conventions.md)
- [Back to Workflows](../05_workflows.md)
