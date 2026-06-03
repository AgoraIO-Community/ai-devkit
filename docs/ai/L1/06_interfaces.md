# 06 Interfaces

> Public interfaces exposed by ai-devkit through repo docs and canonical workflows.
>
> This repo is documentation-only, so its interfaces are markdown files with
> stability expectations rather than API contracts or event schemas. This file
> is lighter than it would be for a service or application repo.

## Primary Interfaces

| Interface | Consumer | Contract |
| --------- | -------- | -------- |
| `AGENTS.md` | any repo-aware agent | tells the agent how to load this repo |
| `docs/ai/` | agents and humans in this repo | structured self-description of the repo |
| `docs/workflows/progressive-disclosure-docs.md` | agents following ai-devkit procedures | canonical docs generation, update, test, fix, and review workflows |
| `docs/standard/agent-policy.md` | maintainers | canonical shared policy text |
| `docs/standard/recipe-profile.md` | maintainers and adopters | recipe inheritance rules for base and vertical repos |
| `docs/standard/spec-profile.md` | adopters and maintainers | spec template, TDD workflow, and nine spec principles |
| `docs/standard/system-profile.md` | adopters and maintainers | system dev environment profile |
| `docs/standard/progressive-disclosure-standard.md` | adopters and maintainers | normative spec |
| `prompts/*.md` | users running prompts via CLI | standalone pipeable prompt files |

## Repo-Local Loading Contract

- Root `AGENTS.md` must point to `docs/ai/L0_repo_card.md`.
- Agents should load all 8 L1 files.
- L2 is opt-in by task.
- Repo-local `AGENTS.md` is the authoritative source for conventions.

## Workflow Contract

- `generate` creates `AGENTS.md` plus `docs/ai/`.
- `update` refreshes existing docs after changes.
- `test` checks whether docs guide an agent correctly.
- `fix` closes findings from review or testing.
- `review with codex` runs an independent Codex review loop after docs exist.

## Supported Interaction Styles

| Style | Supported | Notes |
| ----- | --------- | ----- |
| plain repo reading | Yes | the core delivery path |
| independent CLI review | Yes | Codex reviewer loop in README |

## Compatibility Contract

- Canonical workflows live in `docs/workflows/`.
- README prompts reference canonical paths.

## Stability Expectations

- `AGENTS.md` path should remain stable.
- Canonical workflow docs should remain under `docs/workflows/`.

## Non-Interfaces

- `docs/ai/` is not the canonical home for product workflows; it only describes this repo.

## Interface Review Questions

- Is this file canonical or supplementary?
- Does this interface point at a real file on disk?
- Does a public claim describe this interface accurately?

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — Contract boundaries between policy, workflows, and self-hosted repo docs.
