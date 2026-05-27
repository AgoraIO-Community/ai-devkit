# ai-devkit

Git conventions and progressive disclosure documentation for AI-assisted
development. Works with AI coding agents that read repo files.

## Table of Contents

- [What it does](#what-it-does)
- [How it works](#how-it-works)
- [Create docs](#create-docs)
- [Review docs](#review-docs)
- [Fix review findings](#fix-review-findings)
- [Multi-agent review with Codex](#multi-agent-review-with-codex)
- [Recipe profile](#recipe-profile)
- [Progressive disclosure docs](#progressive-disclosure-docs)
- [Compatibility](#compatibility)
- [Repo layout](#repo-layout)
- [References](#references)

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

1. docs/workflows/progressive-disclosure-docs.md#generate — the generation workflow
2. docs/workflows/progressive-disclosure-docs.md#test — the test workflow
3. docs/standard/progressive-disclosure-standard.md — the full standard

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

1. docs/workflows/progressive-disclosure-docs.md#test — the test workflow
2. docs/standard/progressive-disclosure-standard.md — the full standard

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

1. docs/workflows/progressive-disclosure-docs.md#fix — the fix workflow
2. docs/standard/progressive-disclosure-standard.md — the full standard

Follow the Fix workflow:

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

The canonical workflow doc is [docs/workflows/progressive-disclosure-docs.md](docs/workflows/progressive-disclosure-docs.md#review-with-codex).
The prompt below is a self-contained version for copy-paste.

### How it works

Claude Code invokes Codex directly via `codex exec` in the Bash tool. Codex
runs in a read-only sandbox, reviews the docs against source code, and returns
findings to Claude's context. Claude then fixes the findings and sends Codex
back to verify. Just the `codex` binary on PATH is needed.

### Prompt

Paste this into a Claude Code session after docs have been generated:

````
Run a multi-agent review cycle on this repo's progressive disclosure docs
using Codex as an independent reviewer.

Read the fix workflow from the ai-devkit repo:
https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/workflows/progressive-disclosure-docs.md#fix

## Phase 1: Claude review

1. Read all files in docs/ai/ and compare every factual claim against the
   actual source code in this repo.
2. For each inaccuracy or gap, note the finding, the doc file, and the source
   file you checked.
3. Follow the Fix workflow to close each finding.
4. Commit: docs: fix findings from claude review

## Phase 2: Codex review

Run this command to get Codex's independent review:

```
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

## Phase 3: Fix Codex findings

1. Parse Codex's findings.
2. For each finding, follow the Fix workflow — trace to source, patch the
   exact doc file, record in the finding-to-fix matrix in test-results.md.
3. Commit: docs: fix findings from codex review

## Phase 4: Codex verification

Resume the Codex session to verify fixes:

```
echo "I fixed the findings you reported. Re-read docs/ai/ and verify each
fix against source. Report any remaining issues using the same FINDING format,
or say NO FINDINGS if everything is accurate." \
  | codex exec --skip-git-repo-check resume --last 2>/dev/null
```

If Codex reports new findings, repeat phases 3-4. Max 3 rounds.

## Rules

- Do not mark findings as fixed without checking the source file.
- Do not use generate or update to close findings — use the Fix workflow.
- Update last_reviewed in L0 when done.
````

### Batch across repos

To generate and review docs for multiple repos at once, run Claude Code from
a parent directory containing cloned repos. Claude generates docs for each
repo on a `docs/progressive-disclosure` branch, runs the Claude review cycle,
then the Codex review cycle, and pushes each branch when done.

## Recipe profile

Use [docs/standard/recipe-profile.md](docs/standard/recipe-profile.md) when a repo is a reusable
starter that should publish extension points and support child verticals. The
profile is optional — repos without `Recipe Role` in L0 are unaffected.

See [examples/recipe-base](examples/recipe-base/README.md) and
[examples/recipe-vertical](examples/recipe-vertical/README.md) for structural
fixtures.

## Progressive disclosure docs

The [standard](docs/standard/progressive-disclosure-standard.md) defines three levels:

| Level  | Name       | What it is                              | Token target |
| ------ | ---------- | --------------------------------------- | ------------ |
| **L0** | Repo Card  | Identity + L1 index. Always loaded.     | 300-500      |
| **L1** | Summaries  | 8 structured summaries. Loaded upfront. | 300-600 each |
| **L2** | Deep Dives | Full specs. Loaded only when needed.    | No limit     |

Token targets are recommendations, not hard limits — large repos may need more
at L1. The goal is keeping default context small so 80% of agent tasks complete
with L0+L1 alone (~4,000 tokens).

## Compatibility

Compatibility is capability-based, not absolute. Any tool that reads repo
files can consume `AGENTS.md` and `docs/ai/`.

- **Claude Code** — tested; plain markdown plus multi-agent review
- **Cursor** — tested; plain markdown consumption
- **Codex** — tested; plain markdown plus CLI reviewer role
- **Gemini** — untested; plain markdown consumption expected to work
- **Other tools** — expected to work if the tool reads repo files

## Repo Layout

| Path | Purpose |
| ---- | ------- |
| [AGENTS.md](AGENTS.md) | primary repo entry point for agents |
| [docs/ai](docs/ai/L0_repo_card.md) | this repo's own progressive-disclosure docs |
| [docs/workflows](docs/workflows/progressive-disclosure-docs.md) | canonical docs workflows |
| [docs/standard/recipe-profile.md](docs/standard/recipe-profile.md) | recipe inheritance profile for reusable starter repos |
| [docs/standard/agent-policy.md](docs/standard/agent-policy.md) | canonical shared policy |
| [docs/guides/multi-repo-orchestration.md](docs/guides/multi-repo-orchestration.md) | coordinating agents across repos |
| [examples/minimal-repo](examples/minimal-repo/README.md) | minimal structural fixture for adopters |
| [examples/recipe-base](examples/recipe-base/README.md) | base recipe fixture |
| [examples/recipe-vertical](examples/recipe-vertical/README.md) | vertical recipe fixture |
| [docs/standard/progressive-disclosure-standard.md](docs/standard/progressive-disclosure-standard.md) | full standard |

## References

- [Progressive Disclosure Standard](docs/standard/progressive-disclosure-standard.md) — full spec
- [Recipe Profile](docs/standard/recipe-profile.md) — inheritance for reusable starter repos
- [Multi-Repo Orchestration Guide](docs/guides/multi-repo-orchestration.md) — coordinating agents across repos (WIP)
- [Agent Policy](docs/standard/agent-policy.md) — canonical shared policy
