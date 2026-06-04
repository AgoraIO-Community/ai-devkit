# AI Agent Instructions

This repository uses progressive disclosure documentation. Docs live under
`docs/ai/` in three levels.

## How to Load

1. Read [docs/ai/L0_repo_card.md](docs/ai/L0_repo_card.md) to identify the repo.
2. Load all 8 files in `docs/ai/L1/`. They are small and are meant to be read together.
3. Follow L2 deep-dive links only when L1 is not detailed enough for the task.

## Git Conventions

These rules mirror [docs/standard/agent-policy.md](docs/standard/agent-policy.md).

### Commit messages — conventional commits

- **Format:** `type: description` or `type(scope): description`
- **Types:** `feat:`, `fix:`, `chore:`, `test:`, `docs:`
- **Lowercase after prefix**
- **Present tense**
- **No AI tool names**

### Branch names

- **Format:** `type/short-description`
- **Lowercase and hyphen-separated**

### General rules

- **Repo-local instructions win.** This `AGENTS.md` is the authoritative source for repo conventions.
- **No `Co-Authored-By` trailers**
- **No `--no-verify`**
- **No git config identity changes**
- **Spec before plan, plan before code**
- **Review before commit**
- **Prefer TDD when behavior changes**

## Doc Commands

These commands mirror [docs/standard/agent-policy.md](docs/standard/agent-policy.md).

| Command         | When to use                                             |
| --------------- | ------------------------------------------------------- |
| `generate docs` | The repo does not have `docs/ai/` yet                   |
| `update docs`   | Code or conventions changed and existing docs must catch up |
| `test docs`     | You need to verify that the docs guide an agent correctly   |
| `fix docs`      | You are closing findings from a docs review or test run     |

Detailed workflow docs for this repo live in:

- [docs/workflows/progressive-disclosure-docs.md](docs/workflows/progressive-disclosure-docs.md)
