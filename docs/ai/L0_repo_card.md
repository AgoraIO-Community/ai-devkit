# ai-devkit — Repo Card

> Portable repo conventions and progressive-disclosure docs for AI-assisted development.

## Identity

| Field | Value |
| ----- | ----- |
| Repo | `AgoraIO-Community/ai-devkit` |
| Type | `developer-tooling` |
| Language | Markdown + Bash + JSON |
| Deploy Target | GitHub-distributed repo, consumed locally by AI agents and plugins |
| Owner | AgoraIO-Community |
| Last Reviewed | 2026-05-21 |

## L1 — Summaries

The Audience column helps agents prioritise: **Use** = consuming the repo's functionality, **Maintain** = modifying internals.

| File | Purpose | Audience |
| ---- | ------- | -------- |
| [01_setup](L1/01_setup.md) | Prerequisites, quick commands, validation, and local usage patterns | Use & Maintain |
| [02_architecture](L1/02_architecture.md) | Delivery model, core layers, and data flow between standard, workflows, and adapters | Maintain |
| [03_code_map](L1/03_code_map.md) | Directory map, file ownership, and where to edit for common changes | Maintain |
| [04_conventions](L1/04_conventions.md) | Policy precedence, writing rules, validation habits, and change discipline | Maintain |
| [05_workflows](L1/05_workflows.md) | Common maintenance tasks for standards, workflows, adapters, and self-hosted docs | Use & Maintain |
| [06_interfaces](L1/06_interfaces.md) | Public interfaces exposed through AGENTS, docs/workflows, skills, and hooks | Use & Maintain |
| [07_gotchas](L1/07_gotchas.md) | Drift risks, path-compatibility traps, and adapter-specific caveats | Maintain |
| [08_security](L1/08_security.md) | Trust boundaries for hooks, shell execution, external references, and repo hygiene | Maintain |
