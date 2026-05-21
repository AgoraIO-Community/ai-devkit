# 02 Architecture

> High-level delivery model for the standard, canonical workflows, and optional adapters.

## Core Layers

| Layer | Role | Canonical Location |
| ----- | ---- | ------------------ |
| Repo entry point | tells agents how to load the repo | `AGENTS.md` |
| Self-hosted PD docs | describes this repo using the same standard it ships | `docs/ai/` |
| Shared policy | central policy text for conventions and command semantics | `docs/policy/agent-policy.md` |
| Canonical workflows | actionable procedures for docs work | `docs/workflows/` |
| Adapter layer | optional skill and plugin surfaces | `skills/`, `hooks/`, plugin dirs |
| Product/reference docs | standard spec and higher-level guides | `docs/` |

## Delivery Model

- The **primary product** is the repo-local standard: `AGENTS.md` plus `docs/ai/`.
- The **canonical maintenance procedures** live under `docs/workflows/`.
- The **adapter layer** exists for tools that support skills or session-start hooks.
- The **same repo self-adopts the standard**, so ai-devkit is both the spec and a working example.

## Data Flow

```text
docs/policy/agent-policy.md
          |
          v
docs/progressive-disclosure-standard.md -----> AGENTS.md -----> docs/ai/
          |                                       |
          v                                       v
docs/workflows/ ----------------------------> skills/ wrappers
                                                  |
                                                  v
                                           hooks/plugin adapters
```

## Architectural Rules

- Canonical policy should not live only inside adapter files.
- Canonical workflow logic should not live only inside `skills/`.
- Root `AGENTS.md` is the repo entry point, not the plugin hook payload.
- `docs/ai/` describes this repo; it does not replace product docs like the full standard.

## Change Propagation

| If You Change | Also Review |
| ------------- | ----------- |
| shared policy | `AGENTS.md`, standard template section, adapter summaries |
| workflow paths | README prompts, skill wrappers, install docs |
| standard template | root `AGENTS.md`, self-hosted `docs/ai/`, validation rules |
| hook behavior | plugin configs, adapter deep dive, compatibility claims |

## Repo Self-Hosting

- This repo now uses the same `docs/ai/` structure that it recommends to other repos.
- That makes the repo a live fixture for the standard.
- It also means doc drift here is product drift, not just internal inconsistency.

## Tooling Model

- Claude and Cursor have explicit plugin surfaces in-repo.
- Codex is supported primarily through plain markdown plus CLI review flows.
- Gemini has lightweight metadata, not a full injected adapter path.
- Other tools can still use the repo through `AGENTS.md` and `docs/ai/`.

## Architectural Boundaries

| Boundary | Intent |
| -------- | ------ |
| `docs/ai/` vs `docs/workflows/` | self-description stays separate from product workflow docs |
| standard vs adapters | normative rules should not depend on plugin support |
| shared policy vs README | README may summarize, but policy starts in the canonical policy file |

## Why This Architecture Exists

- It keeps portable repo knowledge inside the repo that needs it.
- It keeps ai-devkit-specific workflow docs in one canonical place.
- It limits plugins to the role they are good at: optional bootstrap context.
- It reduces drift caused by copying policy into many unrelated files.

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — Source-of-truth hierarchy and change propagation rules.
- [adapter_injection.md](L2/adapter_injection.md) — Hook and adapter mechanics across supported tools.
