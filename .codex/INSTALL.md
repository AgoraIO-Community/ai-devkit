# ai-devkit for Codex

## Install

```bash
git clone https://github.com/AgoraIO-Community/ai-devkit.git
```

Point Codex at `AGENTS.md` when you are in a repo that already adopted the
standard. If you are loading ai-devkit directly, use `skills/ai-devkit/SKILL.md`
as the adapter entry point.

## What it provides

- **Portable repo standard** — `AGENTS.md` plus `docs/ai/`
- **Canonical workflow docs** — `docs/workflows/generate.md`, `update.md`, `test.md`, `fix.md`
- **Shared policy** — `docs/policy/agent-policy.md`
- **Optional helpers** — git and docs skills for tools that support skill loading

## Current Status

- **Recommended path:** adopt `AGENTS.md` and `docs/ai/` in the target repo
- **Codex plugin/hook:** not shipped here
- **Codex review loop:** supported through the README prompt and CLI examples

## Files

- `AGENTS.md` — repo entry point when the standard is adopted
- `docs/policy/agent-policy.md` — canonical shared policy
- `docs/workflows/` — canonical workflow docs
- `skills/ai-devkit/` — adapter layer for skill-aware tools
