# ai-devkit for Codex

## Install

```bash
git clone https://github.com/AgoraIO-Community/ai-devkit.git
```

Point Codex at `skills/ai-devkit/SKILL.md` as the entry point.

## What it provides

- **Progressive disclosure docs** — `AGENTS.md` and `docs/ai/` work well as the primary Codex integration path
- **Git conventions** — available through `AGENTS.md` in adopting repos, or through `skills/ai-devkit/SKILL.md` when loaded directly
- **Git skills** — ship (commit+push), pr (create PR), sync (rebase onto main)
- **Docs skills** — generate (create docs from scratch), update (refresh after changes), test (verify docs)

## Current Status

- **Tested:** Codex reading `AGENTS.md` plus progressive disclosure docs
- **Not shipped here:** a Codex-specific session-start hook or plugin mechanism
- **Recommended usage:** adopt the AGENTS.md template in the target repo, then use the docs/ai structure as the main source of truth

## Files

- `skills/ai-devkit/SKILL.md` — main conventions and skill directory
- `skills/ai-devkit/git/` — git workflow skills
- `skills/ai-devkit/docs/` — documentation skills
