# 07 Gotchas

> Known traps that cause policy drift, broken prompts, stale docs, or misleading compatibility claims.
>
> This repo is documentation-only, so gotchas are about consistency and drift
> rather than runtime behavior. This file is lighter than it would be for a
> service or application repo.

## Highest-Risk Drift Areas

- Shared policy copied into multiple files
- README prompts referencing old workflow paths
- Root `AGENTS.md` promising behavior not backed by `docs/ai/`
- Standard template text that breaks when copied into another repo

## Path-Change Traps

- Moving workflow docs without updating README prompts
- Breaking deep-dive links from L1 after renaming L2 docs
- Changing file locations without updating the validator

## Claim-Accuracy Traps

- Saying a tool is fully supported when only markdown consumption is documented
- Describing the repo as AGENTS-first while keeping core behavior elsewhere
- Claiming compatibility without verifying the tool can read repo files

## Self-Hosting Traps

- Forgetting that this repo is a live adopter of the standard
- Treating `docs/ai/` as optional example content instead of real repo docs
- Updating repo structure without updating `03_code_map.md`
- Changing conventions without updating `04_conventions.md` and L0 `Last Reviewed`

## Template Traps

- Hardcoding ai-devkit-only local paths into a template intended for other repos
- Omitting `fix docs` from doc command lists
- Re-introducing the PR-number commit rule even though the shipped workflow cannot satisfy it
- Claiming "works with any agent" instead of describing required capabilities

## Review Traps

- Marking docs as accurate without checking source files
- Closing a finding by adding related text somewhere else
- Changing canonical docs without running validation

## Recovery Rules

- Fix canonical sources first.
- Run validation before and after path changes.
- Update self-hosted docs whenever repo behavior changed.
- Prefer precise capability claims over optimistic language.

## Review Questions

- Which file is the source of truth for this claim?
- Does this public prompt still point at the canonical path?
- Would a repo copying the template get a valid local instruction set?
- Did the change update both the product docs and this repo's self-description?

## Healthy Defaults

- Assume canonical docs are right until proven stale by source changes.
- Assume self-hosted `docs/ai/` must change when public positioning changes.
- Assume README wording can become product drift if it stops matching shipped files.

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — Common drift paths and how to correct them.
