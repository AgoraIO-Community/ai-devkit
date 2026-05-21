# 06 Interfaces

> Public interfaces exposed by ai-devkit through repo docs, canonical workflows, skills, and hooks.

## Primary Interfaces

| Interface | Consumer | Contract |
| --------- | -------- | -------- |
| `AGENTS.md` | any repo-aware agent | tells the agent how to load this repo |
| `docs/ai/` | agents and humans in this repo | structured self-description of the repo |
| `docs/workflows/` | agents following ai-devkit procedures | canonical docs generation, update, test, and fix workflows |
| `docs/policy/agent-policy.md` | maintainers and adapters | canonical shared policy text |
| `docs/recipe-profile.md` | maintainers and adopters | recipe inheritance rules for base and vertical repos |
| `docs/progressive-disclosure-standard.md` | adopters and maintainers | normative spec |

## Adapter Interfaces

| Interface | Consumer | Contract |
| --------- | -------- | -------- |
| `skills/ai-devkit/SKILL.md` | skill-aware tools | high-level adapter entry point |
| `skills/ai-devkit/docs/*.md` | legacy or skill-path consumers | compatibility wrapper to canonical workflow docs |
| `skills/ai-devkit/git/*.md` | skill-aware tools | optional git helper procedures |
| `hooks/session-start` | Claude/Cursor plugin hooks | injects ai-devkit context at session start |
| plugin manifests | tool-specific plugin loaders | describe where the adapter entry points live |

## Repo-Local Loading Contract

- Root `AGENTS.md` must point to `docs/ai/L0_repo_card.md`.
- Agents should load all 8 L1 files.
- L2 is opt-in by task.
- Repo-local `AGENTS.md` wins over injected adapter defaults.

## Workflow Contract

- `generate` creates `AGENTS.md` plus `docs/ai/`.
- `update` refreshes existing docs after changes.
- `test` checks whether docs guide an agent correctly.
- `fix` closes findings from review or testing.
- `review_codex` runs an independent Codex review loop after docs exist.

## Supported Interaction Styles

| Style | Supported | Notes |
| ----- | --------- | ----- |
| plain repo reading | Yes | the core delivery path |
| skill loading | Yes | adapter convenience only |
| session-start hook injection | Yes, for supported tools | subordinate to repo-local instructions |
| independent CLI review | Yes | Codex reviewer loop in README |

## Compatibility Contract

- Canonical workflows live in `docs/workflows/`.
- Skill wrappers must point to those canonical docs.
- README prompts must reference canonical paths, not wrappers, unless a compatibility example is intentional.
- Install docs may reference adapters, but should not redefine workflow behavior.

## Hook Contract

- `hooks/session-start` reads `skills/ai-devkit/SKILL.md`.
- Claude and Cursor hook config point to the hook scripts.
- The hook injects ai-devkit context, but that context is subordinate to repo-local instructions.

## Stability Expectations

- `AGENTS.md` path should remain stable.
- canonical workflow docs should remain under `docs/workflows/`.
- wrapper paths may stay longer than the canonical layout if compatibility requires it.
- adapter docs must not silently redefine canonical workflow steps.

## Non-Interfaces

- `package.json` is not an execution interface; it is metadata only.
- `CHANGELOG.md` is not a canonical workflow source.
- `GEMINI.md` is a thin tool-facing file, not the source of repo policy.
- `docs/ai/` is not the canonical home for product workflows; it only describes this repo.

## Interface Review Questions

- Is this file canonical or adapter-level?
- Would a repo-local agent still work without the adapter?
- Does this interface point at a real file on disk?
- Does a public claim describe this interface accurately?

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — Contract boundaries between policy, workflows, and self-hosted repo docs.
- [adapter_injection.md](L2/adapter_injection.md) — Hook and plugin interface details.
