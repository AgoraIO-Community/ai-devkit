# ai-devkit

A practical guide to developing software with AI coding tools. Includes an
installable skill for git workflows and progressive disclosure documentation, a
[documentation standard](docs/progressive-disclosure-standard.md) for making
repos self-describing for AI agents, and a
[multi-repo orchestration guide](docs/multi-repo-orchestration.md) (WIP). The
progressive disclosure docs are tool-agnostic markdown; this repo is tested
primarily with Claude Code and Codex.

## Table of Contents

- [Overview](#overview)
- [Install](#install)
- [Compatibility Status](#compatibility-status)
- [Skills Library](#skills-library)
- [AI Documentation Standard](#ai-documentation-standard)
- [Multi-Repo Orchestration (WIP)](#multi-repo-orchestration-wip)
- [Using with Superpowers](#using-with-superpowers)

---

## Overview

The primary way to adopt ai-devkit is through `AGENTS.md` — a single file at
your repo root that gives any AI agent git conventions, doc commands, and doc
loading instructions. No plugin install required. Just copy the template from
the [progressive disclosure standard](docs/progressive-disclosure-standard.md#47-agentsmd-and-claudemd-integration)
into your repo.

For tools that support plugins, installing ai-devkit adds
skills and hooks as a convenience. At session start, a hook injects git
conventions and registers skills for git workflows and progressive disclosure
documentation. Skills load on demand when you invoke them — say "ship it" for
git, or "generate docs" for documentation.

---

## Install

**No install needed** — copy the AGENTS.md template from
[section 4.7](docs/progressive-disclosure-standard.md#47-agentsmd-and-claudemd-integration)
into your repo root. Any AI agent that reads `AGENTS.md` gets git conventions
and doc commands automatically.

The plugin install below is optional — it adds skills (ship, pr, sync) and
session-start hooks where packaged and tested.

**Claude Code** (optional plugin)

```
/plugin marketplace add AgoraIO-Community/ai-devkit
/plugin install ai-devkit@ai-devkit
```

**Any agent** (optional clone)

```bash
git clone https://github.com/AgoraIO-Community/ai-devkit.git
```

Point your agent at `skills/ai-devkit/SKILL.md` as the entry point.

## Compatibility Status

| Tool        | What works well today                                                  | Status |
| ----------- | ---------------------------------------------------------------------- | ------ |
| Claude Code | `AGENTS.md` + `CLAUDE.md`, Claude plugin packaging, session-start hook | Tested |
| Codex       | `AGENTS.md` + progressive disclosure docs                              | Tested |

Notes:

- The most portable part of ai-devkit is the progressive disclosure doc system:
  `AGENTS.md`, `docs/ai/`, and the standard itself.
- Codex works well with progressive disclosure docs in practice, but this repo
  does not ship a Codex-specific session-start hook or plugin integration.
- Claude Code has the strongest packaged integration in this repo today.
- Other tools should be able to consume `AGENTS.md` and `docs/ai/` because they
  are plain markdown, but those paths are not fully tested here yet.
- This repo still contains packaging files for other tools, but they should be
  treated as secondary or experimental until explicitly tested and documented.

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

[Superpowers](https://github.com/obra/superpowers) handles the development
pipeline — spec, plan, build, test, review. ai-devkit ensures consistent git
usage (clean commits, no AI tool advertising) and maintains useful progressive
disclosure documentation. No overlap:

| Concern         | ai-devkit             | Superpowers          |
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
5. ship — commit and push (ai-devkit)
6. pr — create a PR (ai-devkit)
7. generate — update repo docs (ai-devkit)

## License

MIT
