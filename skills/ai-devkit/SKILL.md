---
name: ai-devkit
description: Portable repo conventions and progressive disclosure documentation for AI-assisted development. Use when a repo wants AGENTS.md conventions, docs/ai guidance, or optional git/docs helper skills.
---

# ai-devkit

ai-devkit is a portable repo standard built around `AGENTS.md` and `docs/ai/`.
Plugins and skills are optional adapters.

## Policy

Default policy mirrors [docs/policy/agent-policy.md](../../docs/policy/agent-policy.md).

- Repo-local `AGENTS.md` overrides plugin-injected defaults.
- Canonical documentation workflows live under `docs/workflows/`.
- Skill files under `skills/` are compatibility wrappers and adapters.

## Available Skills

### git

Optional helper skills for commit, PR, and sync tasks.

| Skill  | Description                                   | Workflow                                 |
| ------ | --------------------------------------------- | ---------------------------------------- |
| `ship` | commit staged changes and push to remote      | Read `skills/ai-devkit/git/ship.md`      |
| `pr`   | create a pull request from the current branch | Read `skills/ai-devkit/git/pr.md`        |
| `sync` | rebase current branch onto latest main        | Read `skills/ai-devkit/git/sync.md`      |

### docs

Canonical workflow docs live under `docs/workflows/`.

| Skill      | Description                                                 | Canonical Workflow            |
| ---------- | ----------------------------------------------------------- | ----------------------------- |
| `generate` | generate L0/L1/L2 docs for the repo from scratch            | `docs/workflows/generate.md` |
| `update`   | update existing docs after code changes — only what changed | `docs/workflows/update.md`   |
| `test`     | verify generated docs meet the standard                     | `docs/workflows/test.md`     |
| `fix`      | close review findings by tracing each to source code        | `docs/workflows/fix.md`      |
