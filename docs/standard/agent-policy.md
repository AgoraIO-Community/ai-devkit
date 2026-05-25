# Agent Policy

This file is the canonical source for ai-devkit's shared agent-facing policy.
Other entry points may summarize or mirror it, but changes should start here.

## Precedence

- Repo-local `AGENTS.md` is the authoritative source for repo conventions.
- When a repo vendors workflow docs locally, prefer those local workflow docs.

## Git Conventions

### Commit messages

- Format: `type: description` or `type(scope): description`
- Types: `feat:`, `fix:`, `chore:`, `test:`, `docs:`
- Lowercase after prefix
- Present tense
- No AI tool names

### Branch names

- Format: `type/short-description`
- Lowercase
- Hyphen-separated

### General rules

- No `Co-Authored-By` trailers
- No `--no-verify`
- Do not modify `git config` identity settings
- Spec before plan, plan before code
- Review before commit
- Prefer TDD when behavior changes

## Doc Commands

| Command       | When to use                                             |
| ------------- | ------------------------------------------------------- |
| `generate docs` | The repo does not have `docs/ai/` yet                   |
| `update docs`   | Code or conventions changed and existing docs must catch up |
| `test docs`     | You need to verify that the docs guide an agent correctly   |
| `fix docs`      | You are closing findings from a docs review or test run     |
