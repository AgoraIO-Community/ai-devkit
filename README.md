# ai-devkit

Git conventions and progressive disclosure documentation for AI-assisted
development. Works with any AI coding agent.

## Table of Contents

- [What it does](#what-it-does)
- [How it works](#how-it-works)
- [Create docs](#create-docs)
- [Review docs](#review-docs)
- [Fix review findings](#fix-review-findings)
- [Multi-agent review with Codex](#multi-agent-review-with-codex)
- [Progressive disclosure docs](#progressive-disclosure-docs)
- [Compatibility](#compatibility)
- [Install as a skill (optional)](#install-as-a-skill-optional)
- [References](#references)
- [License](#license)

## What it does

1. **Git conventions** — conventional commits (`feat:`, `fix:`, `chore:`),
   branch naming (`type/short-description`), no AI tool names
2. **Progressive disclosure docs** — a three-level doc architecture (L0/L1/L2)
   that makes repos self-describing for AI agents
3. **Prompts** — copy-paste prompts for generating, reviewing, and fixing docs
   in any agent session

## How it works

The output is `AGENTS.md` plus `docs/ai/` — plain markdown files saved in the
repo. Any agent that reads repo files can use them. No install required.

Paste a prompt into your agent session. The prompt tells the agent to read the
ai-devkit workflows from GitHub and apply them to your repo.

## Create docs

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

## Fix review findings

After a review produces findings, use this prompt to close them. Each finding
is traced to source code and patched at the correct disclosure level.

````
Fix the review findings for this repo's progressive disclosure docs.

Read these files from the ai-devkit repo
(https://github.com/AgoraIO-Community/ai-devkit.git):

1. skills/ai-devkit/docs/fix.md — the fix workflow
2. docs/progressive-disclosure-standard.md — the full standard

Follow the fix.md workflow:

1. Read docs/ai/test-results.md for findings.
2. For each finding, trace it to the actual source code.
3. Patch the exact cited doc files at the correct disclosure level.
4. Record a finding-to-fix matrix in docs/ai/test-results.md.
5. Re-run structural checks.
6. Commit with: docs: fix review findings
````

Do not use the generate or review prompts to close findings — they are not
finding-driven.

## Multi-agent review with Codex

You can use Claude Code as the orchestrator and Codex CLI as an independent
reviewer. This catches issues that a single agent misses, since each model
has different blind spots.

Requires: [Codex CLI](https://github.com/openai/codex) installed and on PATH.

### The loop

1. **Generate** — create docs using the prompt above
2. **Claude review** — review docs, then fix findings
3. **Codex review** — Claude shells out to Codex for an independent read-only review
4. **Fix** — Claude closes Codex's findings
5. **Verify** — Claude resumes the Codex session to confirm fixes
6. Repeat 4-5 until Codex reports no new findings

### Codex review command

Claude runs this via Bash to get Codex's independent review:

```bash
codex exec -m gpt-5.4 \
  --config model_reasoning_effort="medium" \
  --sandbox read-only \
  --full-auto \
  --skip-git-repo-check \
  "Read every file in docs/ai/ and compare each factual claim against
the actual source code. For each doc file, report findings as:

FINDING: [description]
FILE: [doc file]
SOURCE: [source file checked]
SEVERITY: high | medium | low
RECOMMENDATION: [what to fix]

If everything is accurate, say: NO FINDINGS" 2>/dev/null
```

### Codex verification

After fixing, resume the Codex session to verify:

```bash
echo "I fixed the findings. Re-read docs/ai/ and verify each fix against
source. Report remaining issues or say NO FINDINGS." \
  | codex exec --skip-git-repo-check resume --last 2>/dev/null
```

### Batch across repos

To generate and review docs for multiple repos at once, run Claude Code from
a parent directory containing cloned repos. Claude generates docs for each
repo on a `docs/progressive-disclosure` branch, runs the Claude review cycle,
then the Codex review cycle, and pushes each branch when done. The
[skill-codex](https://github.com/skills-directory/skill-codex) plugin can
also be used to invoke Codex from within Claude Code.

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

## Install as a skill (optional)

The prompts above work without installing anything. If you prefer skill-based
invocation, install the plugin for your tool. Note that skill triggers like
"test" and "generate" can conflict with other work — use the prompts if you
run into ambiguity.

**Claude Code**

```
/plugin marketplace add AgoraIO-Community/ai-devkit
/plugin install ai-devkit@ai-devkit
```

**Cursor (via `npx skills`)**

```bash
npx skills add AgoraIO-Community/ai-devkit
```

**Other tools (via [`npx skills`](https://github.com/anthropics/skills))**

```bash
npx skills add AgoraIO-Community/ai-devkit
```

Use `--list` to preview discovered skills or `--skill ai-devkit` to install the
main entry-point explicitly.

**Manual (any agent)**

```bash
git clone https://github.com/AgoraIO-Community/ai-devkit.git
```

Point your agent at `skills/ai-devkit/SKILL.md` as the entry point.

### Available skills

| Skill    | What it does                                           |
| -------- | ------------------------------------------------------ |
| ship     | commit staged changes and push to remote               |
| pr       | create a pull request with generated title and summary |
| sync     | rebase current branch onto latest main                 |
| generate | create L0/L1/L2 progressive disclosure docs            |
| update   | update existing docs after code changes                |
| test     | verify docs give agents the right context              |
| fix      | close review findings by tracing each to source code   |

## References

- [Progressive Disclosure Standard](docs/progressive-disclosure-standard.md) — full spec
- [Multi-Repo Orchestration Guide](docs/multi-repo-orchestration.md) — coordinating agents across repos (WIP)
- [Superpowers](https://github.com/obra/superpowers) — complementary spec/plan/TDD/review workflow

## License

MIT
