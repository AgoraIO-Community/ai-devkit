# 05 Workflows

> Step-by-step maintenance flows for the standard, canonical docs, adapters, and self-hosted repo docs.

## Common Tasks

| Task | Start Here | Also Review |
| ---- | ---------- | ----------- |
| change shared policy | `docs/policy/agent-policy.md` | `AGENTS.md`, standard template, adapter summaries |
| change standard wording | `docs/progressive-disclosure-standard.md` | `README.md`, `docs/ai/`, validator |
| change recipe inheritance rules | `docs/recipe-profile.md` | recipe fixtures, standard references, README |
| change docs workflow behavior | `docs/workflows/` | skill wrappers, README prompts |
| change hook or plugin behavior | `hooks/`, plugin manifests | README compatibility claims, deep dives |
| change repo self-description | `docs/ai/` | `AGENTS.md`, `last_reviewed` |

## Update Shared Policy

1. Edit `docs/policy/agent-policy.md`.
2. Update any mirrored summaries in `AGENTS.md`.
3. Update the standard template if the change affects copied repo instructions.
4. Check adapter summaries for stale wording.
5. Run validation.

## Update the Standard

1. Edit `docs/progressive-disclosure-standard.md`.
2. Check whether the change affects:
   - root `AGENTS.md`
   - `docs/ai/`
   - canonical workflows
   - README claims
3. Update the affected files in the same change.
4. Run validation.

## Update Canonical Workflows

1. Edit the target file in `docs/workflows/`.
2. Confirm the corresponding wrapper under `skills/ai-devkit/docs/` still points at the right path.
3. Update README prompts if file locations or command semantics changed.
4. Run validation.

## Canonical Workflow Links

- [generate](../../workflows/generate.md)
- [update](../../workflows/update.md)
- [test](../../workflows/test.md)
- [fix](../../workflows/fix.md)
- [review_codex](../../workflows/review_codex.md)

These files stay outside `docs/ai/` because they are reusable product procedures.
This L1 file describes how ai-devkit uses and maintains them.

## Update Adapters

1. Change the hook, plugin manifest, or skill wrapper.
2. Verify the adapter still points at a canonical doc instead of inventing new behavior.
3. Check compatibility claims in README and install docs.
4. Run validation.

## Update Self-Hosted Docs

1. Change the affected `docs/ai/` file.
2. Update `docs/ai/L0_repo_card.md` `Last Reviewed`.
3. Verify related deep-dive links still make sense.
4. Run validation.

## Review Loop

1. Compare public promises to shipped files.
2. Compare canonical docs to adapter wrappers.
3. Compare root `AGENTS.md` to the standard template intent.
4. Compare `docs/ai/` to the current repo layout.
5. Record any findings before making broad rewrites.

## Path-Move Rules

- If a canonical file moves, update every public reference in the same change.
- Keep compatibility wrappers when external prompts are likely to rely on old paths.
- Do not move files just to reduce top-level clutter if it breaks discoverability.
- Treat path changes as product changes, not cosmetic cleanup.

## Self-Hosting Workflow

1. update the product docs or adapter behavior
2. update `docs/ai/` if repo behavior changed
3. update `Last Reviewed` in L0
4. run validation
5. scan `README.md` and `AGENTS.md` for stale public claims

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — Detailed change propagation for policy and workflow updates.
- [adapter_injection.md](L2/adapter_injection.md) — Adapter update sequence for hooks and plugin surfaces.
