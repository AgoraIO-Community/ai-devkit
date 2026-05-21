# 03 Code Map

> Directory map and file ownership guide for ai-devkit maintenance work.

## Top-Level Tree

```text
.
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── docs/
│   ├── ai/
│   ├── shared/
│   ├── workflows/
│   ├── multi-repo-orchestration.md
│   └── progressive-disclosure-standard.md
├── hooks/
├── skills/
├── .claude-plugin/
├── .cursor-plugin/
├── .codex/
└── gemini-extension.json
```

## Core Files

| Path | Responsibility |
| ---- | -------------- |
| `AGENTS.md` | primary repo entry point and loader instructions |
| `README.md` | public product positioning and quick-start usage |
| `docs/progressive-disclosure-standard.md` | normative spec for the docs model |
| `docs/recipe-profile.md` | first-class extension profile for reusable starter repos |
| `docs/policy/agent-policy.md` | canonical shared policy |
| `docs/workflows/` | canonical docs procedures |
| `docs/ai/` | self-hosted PD docs for this repo |
| `scripts/validate-ai-devkit` | repo validation and compliance checks |

## Adapter Surface

| Path | Responsibility |
| ---- | -------------- |
| `skills/ai-devkit/SKILL.md` | adapter entry point for skill-aware tools |
| `skills/ai-devkit/docs/*.md` | compatibility wrappers to canonical workflows |
| `skills/ai-devkit/git/*.md` | optional git helper workflows |
| `hooks/session-start` | injects ai-devkit context for supported plugin setups |
| `hooks/hooks.json` | Claude hook wiring |
| `hooks/hooks-cursor.json` | Cursor hook wiring |
| `hooks/run-hook.cmd` | Windows wrapper for hook execution |

## Plugin Metadata

| Path | Responsibility |
| ---- | -------------- |
| `.claude-plugin/plugin.json` | Claude plugin manifest |
| `.claude-plugin/marketplace.json` | Claude marketplace metadata |
| `.cursor-plugin/plugin.json` | Cursor plugin manifest |
| `.codex/INSTALL.md` | Codex adapter instructions |
| `gemini-extension.json` | Gemini extension metadata |
| `GEMINI.md` | lightweight Gemini-facing redirect |

## Where To Edit

| Goal | Edit First |
| ---- | ---------- |
| change policy wording | `docs/policy/agent-policy.md` |
| change standard rules | `docs/progressive-disclosure-standard.md` |
| change recipe inheritance rules | `docs/recipe-profile.md` |
| change prompt/workflow guidance | `docs/workflows/` |
| change adapter summaries | `skills/ai-devkit/` |
| change hook behavior | `hooks/` |
| change public positioning | `README.md` |
| change self-hosted repo docs | `docs/ai/` |

## Files To Avoid Treating As Canonical

- `skills/ai-devkit/docs/*.md` wrappers
- adapter metadata files that summarize capabilities
- plugin config manifests that only point at existing code
- root-level install notes that depend on the canonical docs

## Search Anchors

- Search for `fix docs` when aligning command lists.
- Search for `docs/workflows/` when validating canonical workflow references.
- Search for `repo-local` when validating precedence wording.
- Search for `docs/ai/` when checking self-hosted standard adoption.

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — Canonical file ownership and propagation model.
- [adapter_injection.md](L2/adapter_injection.md) — Tool-specific adapter surfaces and hook wiring.
