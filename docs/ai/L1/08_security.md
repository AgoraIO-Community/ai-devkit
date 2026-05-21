# 08 Security

> Trust boundaries and safety assumptions for hooks, shell execution, external references, and repo hygiene.

## Trust Boundaries

| Boundary | Risk | Control |
| -------- | ---- | ------- |
| hook execution | shell commands run in user environment | keep hooks minimal and inspect paths carefully |
| plugin metadata | tools may load adapter files automatically | keep metadata small and point at canonical docs |
| external prompts | users may fetch docs from GitHub | keep canonical paths stable and publicly readable |
| repo-local overrides | injected context may conflict with repo docs | declare precedence in policy and `AGENTS.md` |

## Hook Safety

- `hooks/session-start` should stay narrow in scope.
- Hook output should describe available context, not silently redefine repo-local rules.
- Windows wrapper behavior should fail safely when bash is unavailable.
- Hook path changes must be validated against the plugin manifests.

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
- When path changes happen, verify both direct links and adapter references.
- Prefer a validator over memory when checking cross-file consistency.

## Execution Surfaces

| Surface | Execution Risk |
| ------- | -------------- |
| markdown-only docs | low |
| plugin manifests | low to medium |
| hook shell scripts | highest in this repo |
| external review commands | medium, depends on explicit CLI invocation |

## Supply-Chain Surface

| Surface | Notes |
| ------- | ----- |
| GitHub clone/install | optional, public distribution path |
| plugin manifests | metadata only, but must point at real files |
| shell hooks | highest-risk execution surface in this repo |
| CLI review loops | safe when commands are explicit and read-only where intended |

## Security Model Summary

- This repo is documentation-heavy, so its biggest security risk is misleading automation, not secret handling.
- The most important control is precise, validated documentation about what runs where.
- The second control is strict precedence: repo-local instructions beat injected defaults.

## Hard Requirements

- Keep hook behavior inspectable and narrow.
- Keep compatibility claims testable against shipped assets.
- Keep canonical docs public and stable enough for prompts to reference safely.

## Security Review Questions

- Does this change expand what runs automatically in a user environment?
- Does this documentation claim more support than the repo actually ships?
- Would an adopting repo inherit a broken or unsafe default from this text?

## Related Deep Dives

- [adapter_injection.md](L2/adapter_injection.md) — Hook behavior, plugin wiring, and execution boundaries.
- [policy_delivery.md](L2/policy_delivery.md) — How policy changes can accidentally weaken guarantees if they drift across files.
