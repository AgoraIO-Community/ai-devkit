# Recipe Profile for Progressive Disclosure Docs

This document defines the optional recipe profile for repos that are intended to
be extended as reusable starters.

## Opt-In Principle

- The recipe profile is additive and optional.
- Repos without `Recipe Role` remain ordinary PD repos.
- `repo_type` does not change. Recipe status is orthogonal to repo type.
- The base L0/L1/L2 model, 8-file structure, and `AGENTS.md` template remain valid for non-recipe repos.

## Roles

| Role | Meaning |
| ---- | ------- |
| `base` | a reusable starter that publishes extension points, invariants, and stable contracts |
| `vertical` | a child repo that extends a pinned base recipe |

## L0 Fields

These fields are optional and only apply when a repo opts into the recipe profile.

| Field | Applies To | Meaning |
| ----- | ---------- | ------- |
| `Recipe Role` | base, vertical | `base` or `vertical` |
| `Recipe Version` | base | semantic version for the published recipe contract |
| `Recipe Status` | base | `stable` or `experimental` for the recipe surface |
| `Extends` | vertical | pinned base reference, e.g. `org/base-recipe@v1.2.0` or `org/base-recipe@<sha>` |
| `Locked` | vertical | comma-separated L1 slots inherited without local modification |
| `Overlay` | vertical | comma-separated per-file overlay modes |

## Base Recipe Artifact: `docs/ai/RECIPE.md`

Base recipes publish `docs/ai/RECIPE.md` as a sibling to `L0_repo_card.md`.

It should begin with YAML front matter:

```yaml
recipe_version: 1.0.0
recipe_status: stable
extension_points:
  - id: api.routes
    name: API routes
  - id: prompts.system
    name: system prompt surface
invariants:
  - id: contracts.response-envelope
    summary: response envelope shape stays stable
stable_contracts:
  - id: env.required
    summary: required environment variables
```

Then include these sections:

- `## Extension Points`
- `## Invariants`
- `## Stable Contracts`
- `## Internal / Subject to Change`

## Vertical Overlay Model

Vertical repos extend a pinned base using three per-file modes:

| Mode | Meaning |
| ---- | ------- |
| `inherit` | use the base file as-is |
| `extend` | append child-specific content to the base file |
| `replace` | child file replaces the base file for that slot |

Example:

```text
Overlay: 04_conventions(extend), 05_workflows(extend), 07_gotchas(replace)
```

`Locked` identifies slots that the child intentionally inherits without local modification.

## L1 Slot Rule for Verticals

Vertical repos still expose the 8 standard L1 slots.

- overlaid files contain local content
- locked or inherited files may be lightweight stubs that point to the pinned base repo
- agents still see the same 8-slot structure

This preserves predictability without forcing a child repo to duplicate the full base content.

## AGENTS Loading Additions

When `Recipe Role` is absent, use the normal PD loading protocol.

When `Recipe Role: base`:

1. load `docs/ai/L0_repo_card.md`
2. load `docs/ai/RECIPE.md`
3. load all 8 local L1 files
4. follow local L2 links when needed

When `Recipe Role: vertical`:

1. load the child `docs/ai/L0_repo_card.md`
2. read `Extends` and resolve the pinned base repo/version
3. load the base repo's `AGENTS.md`, L0, and `RECIPE.md`
4. load the child repo's 8 L1 slots and apply `Locked`/`Overlay`
5. read `RECIPE_DELTA.md` if present for a concise child-vs-base diff
6. follow base or child L2 links as needed

## Optional Root Artifact: `RECIPE_DELTA.md`

Vertical repos may add `RECIPE_DELTA.md` at repo root.

Use it for:

- concise "what changed from base" summary
- new routes, env vars, or vendors
- replaced prompts or workflow differences

It is a helper doc, not part of the core `docs/ai/` tree.

## Validation Expectations

- `Extends` must be pinned to a tag or SHA, not an unversioned branch
- base recipes should keep `RECIPE.md` consistent with published interfaces
- vertical repos should keep `Locked` and `Overlay` aligned with their actual L1 files
- agents that ignore the profile should still be able to use the repo as a normal PD repo

## Fixtures

- [recipe-base](../examples/recipe-base/README.md)
- [recipe-vertical](../examples/recipe-vertical/README.md)
