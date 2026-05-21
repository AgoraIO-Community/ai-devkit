---
name: docs
description: Documentation generation and verification using the progressive disclosure standard. Use when the user wants to generate, update, test, or fix repo documentation.
---

# docs

Canonical workflow docs live under `docs/workflows/`. This skill namespace is a compatibility layer for tools that load workflows via `skills/`.

## Skills

| Skill      | Description                                                 | Canonical Workflow            |
| ---------- | ----------------------------------------------------------- | ----------------------------- |
| `generate` | generate L0/L1/L2 docs for the repo from scratch            | `docs/workflows/generate.md` |
| `update`   | update existing docs after code changes — only what changed | `docs/workflows/update.md`   |
| `test`     | verify generated docs meet the standard                     | `docs/workflows/test.md`     |
| `fix`      | close review findings by tracing each to source code        | `docs/workflows/fix.md`      |

## Standard

All generated documentation follows the progressive disclosure standard:

- **L0** — repo card
- **L1** — 8 topic files
- **L2** — deep dives for complex topics
