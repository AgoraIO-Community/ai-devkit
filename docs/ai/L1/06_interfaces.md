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

## Prompt Interface

Six chainable prompts in `prompts/`:

| Prompt | Purpose |
| ------ | ------- |
| `spec.md` | draft or update a spec |
| `implement.md` | start or continue implementation from spec (TDD) |
| `create-docs.md` | generate Progressive Disclosure docs from scratch |
| `update-docs.md` | update existing docs after code changes |
| `verify-codex.md` | chain: use Codex as Verify AI |
| `verify-claude.md` | chain: use Claude as Verify AI |

Work prompts chain with either verify prompt via `cat` or `curl` piped to an agent.

## Canonical Workflow Contract

The canonical workflow file (`docs/workflows/progressive-disclosure-docs.md`) defines the underlying procedures that the prompts invoke:

- `generate` creates `AGENTS.md` plus `docs/ai/`.
- `update` refreshes existing docs after changes.
- `test` checks whether docs guide an agent correctly.
- `fix` closes findings from review or testing.

## Supported Interaction Styles

| Style | Supported | Notes |
| ----- | --------- | ----- |
| plain repo reading | Yes | the core delivery path |
| CLI prompt piping | Yes | `cat` or `curl` prompts piped to any agent |
| cross-model verification | Yes | chain verify-codex or verify-claude |

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
