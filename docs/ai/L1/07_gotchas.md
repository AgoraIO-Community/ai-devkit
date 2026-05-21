# 07 Gotchas

> Known traps that cause policy drift, broken prompts, stale docs, or misleading compatibility claims.

## Highest-Risk Drift Areas

- Shared policy copied into multiple files
- README prompts referencing old workflow paths
- skill wrappers diverging from canonical workflows
- root `AGENTS.md` promising behavior not backed by `docs/ai/`
- standard template text that breaks when copied into another repo

## Path-Change Traps

- Moving workflow docs without updating README prompts
- Updating canonical files but leaving old skill-path docs as stale full copies
- Changing plugin entry points without updating manifests
- Breaking deep-dive links from L1 after renaming L2 docs

## Claim-Accuracy Traps

- Saying a tool is fully supported when only markdown consumption is documented
- implying hooks exist for Codex when only install guidance exists
- calling wrappers canonical after moving workflows into `docs/workflows/`
- describing the repo as AGENTS-first while keeping core behavior only in plugins

## Self-Hosting Traps

- Forgetting that this repo is now a live adopter of the standard
- Treating `docs/ai/` as optional example content instead of real repo docs
- Updating repo structure without updating `03_code_map.md`
- Changing conventions without updating `04_conventions.md` and L0 `Last Reviewed`

## Adapter Traps

- Assuming hook-injected skill text should override repo-local instructions
- Describing tool support more broadly than the actual adapter surface supports
- Forgetting that Codex is supported primarily through markdown and CLI flows, not a shipped hook
- Treating plugin metadata as the place to explain repo behavior

## Template Traps

- Hardcoding ai-devkit-only local paths into a template intended for other repos
- Omitting `fix docs` from doc command lists
- Re-introducing the PR-number commit rule even though the shipped workflow cannot satisfy it
- claiming "works with any agent" instead of describing required capabilities

## Review Traps

- marking docs as accurate without checking source files
- closing a finding by adding related text somewhere else
- changing canonical docs without running validation
- changing only the wrapper because it was easier to find

## Recovery Rules

- Fix canonical sources first.
- Preserve compatibility when public references likely exist.
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
- Assume wrappers need review whenever canonical paths move.
- Assume self-hosted `docs/ai/` must change when public positioning changes.
- Assume README wording can become product drift if it stops matching shipped files.

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — Common drift paths and how to correct them.
- [adapter_injection.md](L2/adapter_injection.md) — Hook-specific and plugin-specific caveats.
