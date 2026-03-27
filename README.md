# ai-dev-kit

A practical guide to developing software with AI coding tools. Works with any
agent — Claude Code, Cursor, Codex, Gemini.

This repo contains:

- **ai-dev-kit skill** — git workflow commands (commit, PR, rebase) and
  progressive disclosure documentation (generate, update, verify) that agents
  load on demand
- **[Progressive Disclosure Documentation Standard](docs/progressive-disclosure-standard.md)** —
  the spec for making repos self-describing for AI agents (L0/L1/L2 architecture)
- **[Multi-Repo Orchestration Guide](docs/multi-repo-orchestration.md)** (WIP) —
  coordination patterns for features that span multiple repos

## Table of Contents

- [Overview](#overview)
- [Install](#install)
- [Skills Library](#skills-library)
- [AI Documentation Standard](#ai-documentation-standard)
- [Multi-Repo Orchestration (WIP)](#multi-repo-orchestration-wip)
- [Using with Superpowers](#using-with-superpowers)

---

## Overview

ai-dev-kit installs as a plugin. At session start, a hook injects the main
skill file which sets git conventions (lowercase commits, no AI tool names,
present tense) and registers skills for git workflows and progressive disclosure
documentation. Git conventions are always active. Skills load on demand when you
invoke them — say "ship it" for git, or "generate docs" for documentation.

---

## Install

**Claude Code**

```bash
claude install github.com/BenWeekes/ai-dev-kit
```

**Cursor**

```bash
cursor install github.com/BenWeekes/ai-dev-kit
```

**Any agent**

```bash
git clone https://github.com/BenWeekes/ai-dev-kit.git
```

Point your agent at `skills/ai-dev-kit/SKILL.md` as the entry point.

---

## Skills Library

**Git**

| Skill | What it does                                           |
| ----- | ------------------------------------------------------ |
| ship  | commit staged changes and push to remote               |
| pr    | create a pull request with generated title and summary |
| sync  | rebase current branch onto latest main                 |

**Docs**

| Skill    | What it does                                                 |
| -------- | ------------------------------------------------------------ |
| generate | create L0/L1/L2 progressive disclosure docs from scratch     |
| update   | update existing docs after code changes                      |
| test     | verify docs give agents the right context at the right level |

**Usage examples** — just ask your agent in natural language:

- "ship it" — commits staged changes and pushes
- "create a pr" — opens a pull request with generated title and summary
- "sync with main" — rebases onto latest main
- "generate docs for this repo" — creates progressive disclosure documentation
- "update the docs" — refreshes docs to reflect recent code changes
- "test the docs" — verifies docs give agents the right context

## AI Documentation Standard

Every repo should be self-describing for AI agents. The
[Progressive Disclosure Documentation Standard](docs/progressive-disclosure-standard.md)
defines a three-level architecture:

| Level  | Name       | What it is                                              | Token budget |
| ------ | ---------- | ------------------------------------------------------- | ------------ |
| **L0** | Repo Card  | Identity + L1 index. Always loaded first.               | 300-500      |
| **L1** | Summaries  | Structured summaries for standard work. 8 files.        | 300-600 each |
| **L2** | Deep Dives | Full specs and subsystem docs. Loaded only when needed. | No limit     |

The `generate` skill creates these docs automatically for any repo.

## Multi-Repo Orchestration (WIP)

When features span multiple repos, you need coordination across agents. The
[Multi-Repo Orchestration Guide](docs/multi-repo-orchestration.md) describes
agent tiers, epic lifecycle, and cross-repo review patterns.

## Using with Superpowers

ai-dev-kit and Superpowers cover different concerns with no overlap:

| Concern         | ai-dev-kit             | Superpowers          |
| --------------- | ---------------------- | -------------------- |
| Git conventions | ship, pr, sync         | —                    |
| Documentation   | generate, update, test | —                    |
| Spec & planning | —                      | spec, plan           |
| Development     | —                      | tdd, review          |
| Debugging       | —                      | systematic-debugging |

A typical workflow:

1. spec — capture what you want to build (Superpowers)
2. plan — design the approach (Superpowers)
3. tdd — implement with tests (Superpowers)
4. review — review the changes (Superpowers)
5. ship — commit and push (ai-dev-kit)
6. pr — create a PR (ai-dev-kit)
7. generate — update repo docs (ai-dev-kit)

## License

MIT
