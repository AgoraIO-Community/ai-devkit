# ai-dev-kit

A practical guide and toolkit for consistent AI-assisted development. Works with
any AI coding agent — the practices are about how your team works, not which
tool you use.

This repo provides two things: a guide to the practices that make AI-assisted
development reliable across a team, and installable skills that teach AI agents
to follow those practices automatically.

## Table of Contents

- [Install](#install)
- [How it works](#how-it-works)
- [Skills Library](#skills-library)
- [AI Documentation Standard](#ai-documentation-standard)
- [Multi-Repo Orchestration (WIP)](#multi-repo-orchestration-wip)
- [Using with Superpowers](#using-with-superpowers)

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

## How it works

A session-start hook injects git conventions (lowercase commits, no AI tool
names, present tense) into every session automatically. Detailed skill
workflows load on demand via the Skill tool.

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
