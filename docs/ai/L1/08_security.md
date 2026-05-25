# 08 Security

> Trust boundaries and safety assumptions for external references, repo hygiene, and content safety.
>
> This repo is documentation-only, so security concerns are about content
> accuracy and not misleading automation rather than auth, secrets, or
> network boundaries. This file is lighter than it would be for a service
> or application repo.

## Trust Boundaries

| Boundary | Risk | Control |
| -------- | ---- | ------- |
| external prompts | users may fetch docs from GitHub | keep canonical paths stable and publicly readable |
| repo-local overrides | external context may conflict with repo docs | declare precedence in policy and `AGENTS.md` |
| CLI review commands | Codex and other CLI tools run in user environment | keep commands explicit and read-only where intended |

## Content Safety

- Do not claim support for a tool feature that is not actually shipped here.
- Do not hide capability gaps behind vague language.
- Do not embed credentials, tokens, or private URLs in workflow docs.
- Keep public install docs safe to copy into another environment.

## Repo Hygiene

- No `--no-verify` in documented git flows.
- No rewritten git identity settings.
- No AI attribution trailers in commits produced by the helper workflows.
- Prefer local relative links for in-repo docs.

## Review Safety

- Verify findings against source before editing docs.
- Treat stale self-hosted docs as a correctness issue, not just documentation debt.
- When path changes happen, verify direct links.
- Prefer a validator over memory when checking cross-file consistency.

## Execution Surfaces

| Surface | Execution Risk |
| ------- | -------------- |
| markdown-only docs | low |
| external review commands | medium, depends on explicit CLI invocation |
| validation script | low, read-only checks |

## Supply-Chain Surface

| Surface | Notes |
| ------- | ----- |
| GitHub clone | public distribution path |
| CLI review loops | safe when commands are explicit and read-only where intended |

## Security Model Summary

- This repo is documentation-heavy, so its biggest security risk is misleading automation, not secret handling.
- The most important control is precise, validated documentation about what runs where.
- The second control is strict precedence: repo-local instructions are authoritative.

## Hard Requirements

- Keep compatibility claims testable against shipped assets.
- Keep canonical docs public and stable enough for prompts to reference safely.

## Security Review Questions

- Does this documentation claim more support than the repo actually ships?
- Would an adopting repo inherit a broken or unsafe default from this text?

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — How policy changes can accidentally weaken guarantees if they drift across files.
