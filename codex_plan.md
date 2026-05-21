# ai-devkit improvement plan

## Positioning

Make `ai-devkit` a clear, portable standard built around `AGENTS.md` and `docs/ai/`, with plugins and skills treated as optional adapters.

The repo should follow that standard itself so the project is both the spec and a real adopter.

## Priority changes

### 1. Remove contradictions first

- Drop the "PR number appended" commit rule. It conflicts with the shipped `ship` and `pr` flow.
- State one precedence rule everywhere: repo-local `AGENTS.md` overrides plugin-injected defaults.
- Add `fix docs` everywhere doc commands are listed so the workflow is complete.
- Rewrite this repo's root `AGENTS.md` to the standard loader template and back it with a real `docs/ai/` tree.

Why:

- These are current correctness issues, not polish.

### 2. Make one source of truth for conventions

- Create a single canonical source for shared policy text:
  - git conventions
  - doc command list
  - precedence between repo docs and plugins
  - compatibility wording and capability claims
- Generate or validate derived copies in:
  - root `AGENTS.md`
  - `skills/ai-devkit/SKILL.md`
  - relevant README/install snippets

Recommended implementation:

- Add a small validation or generation script instead of continuing to hand-copy rules.

Why:

- The repo is already drifting.

### 3. Rewrite the README around the real product

- Lead with: portable repo conventions + progressive-disclosure docs standard.
- Keep prompts as the main path.
- Treat plugins as optional.
- Replace broad compatibility claims with a capability matrix:
  - plain markdown support
  - skill support
  - session-start hook support
  - multi-agent review support

Also update the motivation for progressive disclosure:

- Lead with curated context, tribal knowledge, and maintainable summaries.
- Keep token budgets as constraints, not the main sales pitch.

Why:

- This matches what the repo actually delivers.

### 4. Make workflows honest about agent capability limits

- Add a short "Required capabilities" section to each workflow.
- Mark steps as:
  - required
  - optional if the agent supports it
  - fallback to manual review

Focus especially on:

- web access or remote file fetching
- repo-wide reading
- sub-agent or multi-agent support

Why:

- The current docs assume stronger agents than many tools actually provide.

### 5. Add staleness and validation checks

- Add a lightweight self-check script to catch:
  - policy drift across duplicated files
  - broken file references
  - mismatches between listed and shipped skills
  - broken hook paths
  - compatibility claims that do not match shipped assets
- Validate this repo's own `docs/ai/` structure against the standard.
- Add at least one fixture docs tree or sample repo layout for structural validation.
- Add a staleness protocol:
  - if `last_reviewed` is old, warn clearly
  - make doc freshness checks easy to run in CI

Why:

- The standard needs executable checks, not only prose.

### 6. Reduce optional surface area without churn

- De-emphasize `ship`, `pr`, and `sync` in top-level messaging.
- Keep them as optional helpers for plugin users.
- Mark experimental content clearly, especially multi-repo orchestration.
- Make documentation workflows first-class docs:
  - move or duplicate `generate`, `update`, `test`, and `fix` under `docs/workflows/`
  - treat `skills/` as the adapter layer that points to those workflows, not the canonical home

### 7. Preserve compatibility during cleanup

- Any change to:
  - workflow paths
  - skill names
  - plugin entry points
  must preserve compatibility for at least one transition step or update every public reference in the same change.
- If workflows move to `docs/workflows/`, keep old references working temporarily or ship the path migration as one atomic docs update.

Do not prioritize:

- moving large numbers of files just to change paths
- reorganizing plugin directories unless it solves a real install problem
- changing the L0/L1/L2 model

Why:

- The biggest problems are inconsistency and positioning, not file layout.

## Suggested order

1. Fix contradictory rules and missing `fix docs` references.
2. Define precedence: repo `AGENTS.md` over plugin defaults.
3. Create the single-source-of-truth mechanism.
4. Rewrite README positioning and compatibility claims.
5. Add capability notes to workflows.
6. Add validation, fixtures, and doc freshness checks.
7. De-emphasize optional git skills and mark experimental docs clearly.
8. Move documentation workflows under `docs/workflows/` while preserving compatibility.

## Deliverables

- updated README
- updated `docs/progressive-disclosure-standard.md`
- added `docs/workflows/` as the canonical home for documentation workflows
- added `docs/ai/` for this repo's own self-description
- updated root `AGENTS.md`
- updated `skills/ai-devkit/SKILL.md`
- one canonical conventions source plus validation script
- fixture docs tree or sample repo layout

## Kept from Claude plan

- prompt-first positioning
- curated-context framing over token-savings marketing
- explicit staleness handling
- de-emphasizing git skills in top-level messaging
- moving documentation workflows to a docs-first location with compatibility protection

## Not adopted

- consolidating plugin directories as a first move
- relaxing the 8-file L1 structure before fixing higher-priority inconsistencies
