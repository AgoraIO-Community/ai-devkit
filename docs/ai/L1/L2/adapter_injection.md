# Adapter Injection

> **When to Read This:** Load this document when you are editing hook scripts,
> plugin manifests, skill entry points, or the compatibility claims for a
> supported tool.

## Overview

The adapter layer is optional. Its job is to bootstrap context for tools that
support skills or session-start hooks without becoming the source of truth for
repo behavior.

## Current Surfaces

| Surface | Path | Role |
| ------- | ---- | ---- |
| Claude plugin | `.claude-plugin/` | manifest and hook wiring |
| Cursor plugin | `.cursor-plugin/` | manifest and hook wiring |
| session-start hook | `hooks/session-start` | injects ai-devkit context |
| Windows wrapper | `hooks/run-hook.cmd` | cross-platform hook entry |
| skill adapter | `skills/ai-devkit/SKILL.md` | optional adapter entry point |
| Codex install doc | `.codex/INSTALL.md` | manual adapter guidance |

## Behavioral Constraints

- Hook output must be subordinate to repo-local `AGENTS.md`.
- Skill wrappers should route users to canonical docs, not fork behavior.
- Compatibility claims in README should reflect the actual shipped surface.
- Tool-specific files should stay thin and explicit.

## Change Checklist

1. Edit the hook or adapter file.
2. Check the plugin manifest or install doc that points to it.
3. Re-check README compatibility wording.
4. Run validation.

## See Also

- [Back to Architecture](../02_architecture.md)
- [Back to Interfaces](../06_interfaces.md)
- [Back to Security](../08_security.md)
