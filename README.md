# ai-devkit

Git conventions and progressive disclosure documentation for AI-assisted
development. Works with any AI coding agent.

## What it does

1. **Git conventions** — conventional commits (`feat:`, `fix:`, `chore:`),
   branch naming (`type/short-description`), no AI tool names
2. **Progressive disclosure docs** — a three-level doc architecture (L0/L1/L2)
   that makes repos self-describing for AI agents
3. **Skills** — workflows for git (ship, pr, sync) and docs (generate, update,
   test)

The primary delivery mechanism is `AGENTS.md`. It gives any agent the repo's
conventions, doc loading instructions, and doc commands in one file — no plugin
required.

## Quick start

### Add docs to an existing repo

Paste this prompt into any AI agent session inside your target repo:

````
Create a branch for this work:

git checkout -b docs/progressive-disclosure

Your task is to add progressive disclosure documentation and git conventions
to this repository.

Read these files from the local ai-devkit clone:

1. skills/ai-devkit/docs/generate.md — the generation workflow
2. skills/ai-devkit/docs/test.md — the test workflow
3. docs/progressive-disclosure-standard.md — the full standard

Clone URL: https://github.com/AgoraIO-Community/ai-devkit.git

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

- Read the whole repo, not just top-level files. Delegate large modules when the tool supports it.
- Read existing markdown, config, and CI files for project context.
- Use the real structure and terminology of the repo — no generic filler.
- AGENTS.md must include How to Load, Git Conventions, and Doc Commands.
- Generate L0, L1, and L2 docs according to the standard.
- After generating, run the test workflow. Fix failures and retest until all pass.
- Test results are saved to docs/ai/test-results.md.

When finished:

1. Summarize what you added.
2. Call out any assumptions, gaps, or ambiguous areas.
3. Commit with: docs: add progressive disclosure documentation
4. Push and create a PR.
````

### Set up a new repo

Paste this prompt into an agent session inside a new or early-stage repo:

````
Create a branch for this work:

git checkout -b docs/progressive-disclosure

Your task is to set up this repository with progressive disclosure docs and
git conventions from the start.

Read these files from the local ai-devkit clone:

1. skills/ai-devkit/docs/generate.md — the generation workflow
2. skills/ai-devkit/docs/test.md — the test workflow
3. docs/progressive-disclosure-standard.md — the full standard

Clone URL: https://github.com/AgoraIO-Community/ai-devkit.git

Deliverables:

1. Add AGENTS.md at the repo root using the section 4.7 template.
2. Add progressive disclosure docs under docs/ai/.
3. Establish git conventions for future work:
   - conventional commits
   - branch naming: type/short-description
   - no AI tool names in commit messages
4. Make the docs honest about what exists today — don't invent architecture.

Requirements:

- Inspect all existing source, config, and markdown files before writing docs.
- Do not invent subsystems or workflows that aren't present yet.
- Keep L0 concise. Create L1 summaries that match actual code layout.
- Add L2 docs only where deeper detail is justified.
- Include Doc Commands in AGENTS.md so future agents can update and test docs.
- Run the test workflow and fix issues before finishing.

When finished:

1. Summarize the resulting documentation structure.
2. Identify which docs will need updates as the repo grows.
3. Commit with: docs: add repo conventions and progressive disclosure docs
4. Push and create a PR.
````

### Just want git conventions?

Copy the AGENTS.md template from
[section 4.7](docs/progressive-disclosure-standard.md#47-agentsmd-and-claudemd-integration)
into your repo root. Any AI agent that reads `AGENTS.md` gets git conventions
and doc commands automatically. No install needed.

## Install (optional)

The plugin adds skills (ship, pr, sync) and session-start hooks as a
convenience. The AGENTS.md template works without it.

**Claude Code**

```
/plugin marketplace add AgoraIO-Community/ai-devkit
/plugin install ai-devkit@ai-devkit
```

**Any agent**

```bash
git clone https://github.com/AgoraIO-Community/ai-devkit.git
```

Point your agent at `skills/ai-devkit/SKILL.md` as the entry point.

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
| Codex       | Tested — AGENTS.md + progressive disclosure docs |
| Others      | AGENTS.md and docs/ai/ are plain markdown — should work with any tool that reads repo files |

## References

- [Progressive Disclosure Standard](docs/progressive-disclosure-standard.md) — full spec
- [Multi-Repo Orchestration Guide](docs/multi-repo-orchestration.md) — coordinating agents across repos (WIP)
- [Superpowers](https://github.com/obra/superpowers) — complementary spec/plan/TDD/review workflow

## License

MIT
