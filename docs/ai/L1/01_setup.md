# 01 Setup

> Local setup, quick commands, and validation steps for working on ai-devkit itself.

## Purpose

- This repo is mostly markdown, JSON, and shell glue.
- There is no app server to boot and no package install step required for basic maintenance.
- The main setup work is having the right local CLI tools for validation and review loops.

## Prerequisites

| Item | Required | Why |
| ---- | -------- | --- |
| `git` | Yes | inspect history, validate path changes, manage branch flow |
| `rg` | Recommended | fast repo search for duplicated policy or broken paths |
| `python3` | Recommended | run `scripts/validate-ai-devkit` |
| Markdown-capable editor | Yes | most work is doc and config editing |
| `gh` | Optional | validate PR helper behavior and GitHub workflows |
| `codex` | Optional | run the independent review loop described in the README (use `codex --full-auto "$(curl ...)"`, not piped stdin) |
| `node` 22+ | Optional | run `presentation/record.mjs` (Playwright requires Node 18+, 22 recommended) |
| `ffmpeg` | Optional | compose video frames into MP4 during recording |
| `TTS_KEY` in `.env` | Optional | ElevenLabs API key for audio generation (`source .env && export TTS_KEY`) |

## Quick Commands

| Task | Command |
| ---- | ------- |
| list tracked files | `rg --files` |
| inspect current repo status | `git status --short` |
| review recent commit style | `git log --oneline -10` |
| validate this repo | `python3 scripts/validate-ai-devkit` |
| inspect workflow docs | `rg -n "^#|^##" docs/workflows` |
| inspect self-hosted PD docs | `rg -n "^#|^##" docs/ai` |

## Working Modes

- **Use mode:** read `AGENTS.md`, then `docs/ai/`, then the specific workflow docs you need.
- **Maintain mode:** update the standard and the canonical workflows together.
- **Review mode:** compare public claims in README against what is actually shipped.

## Typical Edit Surfaces

| Change Type | Start Here |
| ----------- | ---------- |
| repo policy or conventions | `docs/standard/agent-policy.md` |
| standard wording or template | `docs/standard/progressive-disclosure-standard.md` |
| workflow behavior | `docs/workflows/progressive-disclosure-docs.md` |
| repo entry point | `AGENTS.md` |
| self-hosted PD docs | `docs/ai/` |
| examples and fixtures | `examples/` |

## Validation Expectations

- Run `python3 scripts/validate-ai-devkit` after any cross-file documentation change.
- Re-run validation after moving files or changing link targets.
- When modifying workflows, verify canonical docs and README prompts stay aligned.
- When modifying `AGENTS.md`, verify it still points cleanly into `docs/ai/`.

## Optional Tooling

- `gh` matters only if you are testing GitHub-facing instructions.
- `codex` matters only if you are exercising the multi-agent review loop.
- No Node install is needed for normal repo maintenance.

## Common Failure Modes

- Changing shared policy in one file and forgetting mirrored entry points.
- Editing `docs/ai/` without updating `last_reviewed` in L0.
- Moving canonical workflows without preserving old references.

## Local Change Checklist

1. Edit the canonical source first.
2. Update mirrored entry points.
3. Run validation.
4. Re-open the affected files and check link resolution manually.
5. Update self-hosted `docs/ai/` if repo behavior changed.

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — How policy and workflow text moves from canonical docs into repo entry points.
