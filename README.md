# ai-devkit

Git conventions and progressive disclosure documentation for AI-assisted
development. Works with any AI coding agent.

## Table of Contents

- [What it does](#what-it-does)
- [How it works](#how-it-works)
- [Install skill](#install-skill)
- [Create docs](#create-docs)
- [Review docs](#review-docs)
- [Skills](#skills)
- [Progressive disclosure docs](#progressive-disclosure-docs)
- [Compatibility](#compatibility)
- [References](#references)
- [License](#license)

## What it does

1. **Git conventions** — conventional commits (`feat:`, `fix:`, `chore:`),
   branch naming (`type/short-description`), no AI tool names
2. **Progressive disclosure docs** — a three-level doc architecture (L0/L1/L2)
   that makes repos self-describing for AI agents
3. **Skills** — workflows for git (ship, pr, sync) and docs (generate, update,
   test)

## How it works

The **docs** (`docs/ai/` + `AGENTS.md`) are repo context — plain files on disk
that agents read when they enter the repo. No install required.

The **skills** are optional workflows that generate and maintain those docs.
Install them for convenient natural-language commands (`generate docs`,
`test the docs`), or use the explicit prompts below — both are equivalent ways
to get the same result.

## Install skill

The skill adds workflows for git (ship, pr, sync) and docs (generate, update,
test).

**Claude Code**

```
/plugin marketplace add AgoraIO-Community/ai-devkit
/plugin install ai-devkit@ai-devkit
```

**Cursor**

```bash
npx skills add AgoraIO-Community/ai-devkit
```

**`npx skills`** (cross-agent CLI from [anthropics/skills](https://github.com/anthropics/skills))

```bash
npx skills add AgoraIO-Community/ai-devkit
```

Use `--list` to preview discovered skills or `--skill ai-devkit` to install the
main entry-point explicitly.

**Any agent**

```bash
git clone https://github.com/AgoraIO-Community/ai-devkit.git
```

Point your agent at `skills/ai-devkit/SKILL.md` as the entry point.

## Create docs

### With the skill

```
generate docs
```

Runs the full generation workflow: reads your repo, creates `AGENTS.md`,
and generates L0/L1/L2 docs under `docs/ai/`.
See [skills/ai-devkit/docs/generate.md](skills/ai-devkit/docs/generate.md) for
the complete workflow.

### With a prompt

Paste this into any AI agent session:

````
Your task is to add progressive disclosure documentation and git conventions
to this repository.

Before starting:

1. Confirm you are inside the target repo's checked-out folder.
2. Ask whether to work on the current branch or create a new one.

Read these files from the ai-devkit repo
(https://github.com/AgoraIO-Community/ai-devkit.git):

1. skills/ai-devkit/docs/generate.md — the generation workflow
2. skills/ai-devkit/docs/test.md — the test workflow
3. docs/progressive-disclosure-standard.md — the full standard

Deliverables:

1. Add AGENTS.md at the repo root using the expanded template from section 4.7
   of the progressive disclosure standard.
2. Generate progressive disclosure docs under docs/ai/.
3. Preserve and integrate with existing repo docs — don't overwrite them.
4. If CLAUDE.md already exists, add a reference to AGENTS.md using that file's
   existing conventions — don't replace content.
5. Apply these git conventions:
   - conventional commits
   - branch naming: type/short-description
   - no AI tool names in commit messages

Requirements:

- Read the whole repo, not just top-level files. Delegate large modules when
  the tool supports it.
- Read existing markdown, config, and CI files for project context.
- Use the real structure and terminology of the repo — no generic filler.
- Do not invent subsystems or workflows that aren't present yet.
- AGENTS.md must include How to Load, Git Conventions, and Doc Commands.
- Generate L0, L1, and L2 docs according to the standard. Add L2 docs only
  where deeper detail is justified.
- After generating, run the test workflow. Fix failures and retest until all
  pass. Test results are saved to docs/ai/test-results.md.

When finished:

1. Summarize what you added.
2. Call out any assumptions, gaps, or ambiguous areas.
3. Commit with: docs: add progressive disclosure documentation
4. Push and create a PR.
````

## Review docs

### With the skill

```
test docs
```

Runs the test workflow against existing docs and reports gaps.
See [skills/ai-devkit/docs/test.md](skills/ai-devkit/docs/test.md) for
the complete workflow.

### With a prompt

After docs are generated, use a second agent session to review quality.
This prompt is read-only — it reports findings without changing files.

````
Review this repo's progressive disclosure docs and provide feedback only.
Do not change files.

Read these files from the ai-devkit repo
(https://github.com/AgoraIO-Community/ai-devkit.git):

1. skills/ai-devkit/docs/test.md — the test workflow
2. docs/progressive-disclosure-standard.md — the full standard

Do this:

1. Read docs/ai/test-results.md.
2. Read the full docs/ai/ tree.
3. Compare the docs to the real codebase.
4. Use git log --oneline -30 to propose 3-5 additional test questions
   based on real recent changes.
5. Read 2-3 complex or under-documented source files and assess whether
   the docs cover them well.
6. Report gaps, inaccuracies, weak test coverage, and recommended new
   test cases.

Do not edit docs, do not update test-results.md, and do not commit.
````

## Skills

| Skill    | What it does                                           |
| -------- | ------------------------------------------------------ |
| ship     | commit staged changes and push to remote               |
| pr       | create a pull request with generated title and summary |
| sync     | rebase current branch onto latest main                 |
| generate | create L0/L1/L2 progressive disclosure docs            |
| update   | update existing docs after code changes                |
| test     | verify docs give agents the right context              |

Usage — just ask your agent in natural language: "ship it", "create a pr",
"generate docs", "test the docs".

## Progressive disclosure docs

The [standard](docs/progressive-disclosure-standard.md) defines three levels:

| Level  | Name       | What it is                              | Token target |
| ------ | ---------- | --------------------------------------- | ------------ |
| **L0** | Repo Card  | Identity + L1 index. Always loaded.     | 300-500      |
| **L1** | Summaries  | 8 structured summaries. Loaded upfront. | 300-600 each |
| **L2** | Deep Dives | Full specs. Loaded only when needed.    | No limit     |

Token targets are recommendations, not hard limits — large repos may need more
at L1. The goal is keeping default context small so 80% of agent tasks complete
with L0+L1 alone (~4,000 tokens).

## Compatibility

| Tool        | Status |
| ----------- | ------ |
| Claude Code | Tested — plugin + AGENTS.md + CLAUDE.md |
| Cursor      | Tested — plugin + AGENTS.md |
| Codex       | Tested — AGENTS.md + progressive disclosure docs |
| Others      | AGENTS.md and docs/ai/ are plain markdown — should work with any tool that reads repo files |

## References

- [Progressive Disclosure Standard](docs/progressive-disclosure-standard.md) — full spec
- [Multi-Repo Orchestration Guide](docs/multi-repo-orchestration.md) — coordinating agents across repos (WIP)
- [Superpowers](https://github.com/obra/superpowers) — complementary spec/plan/TDD/review workflow

## License

MIT
