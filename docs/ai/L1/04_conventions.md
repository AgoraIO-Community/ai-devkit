# 04 Conventions

> Repo-specific writing and maintenance conventions for ai-devkit itself.

## Source-of-Truth Order

1. `docs/policy/agent-policy.md`
2. `docs/progressive-disclosure-standard.md`
3. `docs/recipe-profile.md` when recipe inheritance is involved
4. canonical docs under `docs/workflows/`
5. repo entry point in `AGENTS.md`
6. adapter summaries and wrappers under `skills/` and plugin docs

## Policy Rules

- Repo-local `AGENTS.md` overrides plugin-injected defaults.
- Canonical docs workflows live under `docs/workflows/`.
- Compatibility wrappers may summarize, but should not become the only place a workflow is defined.
- Public product claims should match shipped assets and documented support.

## Writing Style

- Prefer direct, technical prose over marketing language.
- Treat compatibility as capability-based rather than universal.
- Link to canonical docs instead of duplicating long procedures.
- When self-hosted `docs/ai/` changes, keep it factual and repo-specific.

## Documentation Layout Rules

- Keep canonical product procedures under `docs/workflows/`.
- Keep self-hosted repo knowledge under `docs/ai/`.
- Keep adapter entry points thin when they only exist for compatibility.
- Keep root `AGENTS.md` focused on loading instructions and durable conventions.

## Canonical References

- [docs/policy/agent-policy.md](../../policy/agent-policy.md) is the canonical shared policy.
- [docs/recipe-profile.md](../../recipe-profile.md) is the canonical recipe extension profile.
- [docs/workflows/generate.md](../../workflows/generate.md), [docs/workflows/update.md](../../workflows/update.md), [docs/workflows/test.md](../../workflows/test.md), and [docs/workflows/fix.md](../../workflows/fix.md) are canonical procedures.
- They stay outside `docs/ai/` because they are shipped product docs, not deep dives about this repo.

## Change Discipline

- Fix contradictions before adding new features or docs.
- Update all public entry points in the same change when a path or command name moves.
- Preserve compatibility when old workflow paths are likely to be referenced externally.
- Keep experimental guidance clearly labeled as non-normative.

## Git Conventions

| Topic | Rule |
| ----- | ---- |
| commit format | `type: description` or `type(scope): description` |
| allowed types | `feat`, `fix`, `chore`, `test`, `docs` |
| casing | lowercase after prefix |
| tense | present tense |
| banned content | AI tool names in commit messages |
| branch format | `type/short-description` |

## Testing and Validation

- Prefer a validator over manual confidence for cross-file consistency.
- Re-run validation after editing README, standard text, `AGENTS.md`, or workflow locations.
- When changing docs behavior, check both canonical workflow docs and adapter wrappers.
- When changing standard text, update self-hosted `docs/ai/` if its descriptions become stale.

## TDD and Review

- Prefer updating validation or fixtures alongside behavior changes.
- Review before commit is mandatory for cross-file doc changes.
- When behavior changes, add or update checks before declaring the repo consistent.
- Use fixtures or the self-hosted repo docs as the first proof that the standard works.

## Style Checks Before Commit

| Check | Why |
| ----- | --- |
| path references use canonical docs | avoids wrapper drift |
| command lists include `fix docs` | keeps lifecycle complete |
| no impossible workflow rules | prevents conventions from contradicting shipped helpers |
| self-hosted docs still describe the repo accurately | keeps ai-devkit credible as a live adopter |

## Anti-Patterns

- Treating README as the only product definition
- changing skill wrappers without the canonical workflow docs
- adding policy text to plugin metadata and forgetting the standard
- copying template text into adopting repos with broken local links
- claiming support for a tool feature that is not actually shipped

## Maintenance Bias

- Prefer small, coherent changes that update canonical docs and adapters together.
- Avoid introducing new top-level surfaces unless they solve a discoverability problem.
- Prefer validation over memory for any cross-file guarantee.

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — How canonical policy and workflows propagate across the repo.
- [adapter_injection.md](L2/adapter_injection.md) — Adapter-specific constraints that affect how conventions are delivered.
