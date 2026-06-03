# 04 Conventions

> Repo-specific writing and maintenance conventions for ai-devkit itself.

## Source-of-Truth Order

1. `docs/standard/agent-policy.md`
2. `docs/standard/progressive-disclosure-standard.md`
3. `docs/standard/recipe-profile.md` when recipe inheritance is involved
4. `docs/standard/spec-profile.md` when spec/TDD workflow is involved
5. `docs/standard/system-profile.md` when system dev environment is involved
6. canonical docs under `docs/workflows/`
7. repo entry point in `AGENTS.md`

## Policy Rules

- Repo-local `AGENTS.md` is the authoritative source for repo conventions.
- Canonical docs workflows live under `docs/workflows/`.
- Public product claims should match shipped assets and documented support.

## Writing Style

- Prefer direct, technical prose over marketing language.
- Treat compatibility as capability-based rather than universal.
- Link to canonical docs instead of duplicating long procedures.
- When self-hosted `docs/ai/` changes, keep it factual and repo-specific.

## Documentation Layout Rules

- Keep canonical product procedures under `docs/workflows/`.
- Keep self-hosted repo knowledge under `docs/ai/`.
- Keep root `AGENTS.md` focused on loading instructions and durable conventions.

## Prompt Dual-Presence Rule

- Each prompt exists in two places: `prompts/X.md` (standalone, pipeable) and `README.md` (embedded in `<details>` blocks).
- `prompts/X.md` is the source of truth for running; `README.md` is for reading.
- When updating a prompt, change both places in the same commit.

## Canonical References

- [docs/standard/agent-policy.md](../../standard/agent-policy.md) is the canonical shared policy.
- [docs/standard/recipe-profile.md](../../standard/recipe-profile.md) is the canonical recipe extension profile.
- [docs/workflows/progressive-disclosure-docs.md](../../workflows/progressive-disclosure-docs.md) is the canonical procedures file.
- They stay outside `docs/ai/` because they are shipped product docs, not deep dives about this repo.

## Change Discipline

- Fix contradictions before adding new features or docs.
- Update all public entry points in the same change when a path or command name moves.
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
- When changing standard text, update self-hosted `docs/ai/` if its descriptions become stale.

## TDD and Review

- Prefer updating validation or fixtures alongside behavior changes.
- Review before commit is mandatory for cross-file doc changes.
- When behavior changes, add or update checks before declaring the repo consistent.
- Use fixtures or the self-hosted repo docs as the first proof that the standard works.

## Style Checks Before Commit

| Check | Why |
| ----- | --- |
| path references use canonical docs | avoids drift |
| command lists include `fix docs` | keeps lifecycle complete |
| no impossible workflow rules | prevents conventions from contradicting shipped content |
| self-hosted docs still describe the repo accurately | keeps ai-devkit credible as a live adopter |

## Anti-Patterns

- Treating README as the only product definition
- adding policy text in ad-hoc locations and forgetting the standard
- copying template text into adopting repos with broken local links
- claiming support for a tool feature that is not actually shipped

## Maintenance Bias

- Prefer small, coherent changes that update canonical docs together.
- Avoid introducing new top-level surfaces unless they solve a discoverability problem.
- Prefer validation over memory for any cross-file guarantee.

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — How canonical policy and workflows propagate across the repo.
