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
│   ├── img/
│   ├── standard/
│   │   ├── progressive-disclosure-standard.md
│   │   ├── agent-policy.md
│   │   ├── recipe-profile.md
│   │   ├── spec-profile.md
│   │   └── system-profile.md
│   ├── workflows/
│   │   └── progressive-disclosure-docs.md
│   └── guides/
│       └── multi-repo-orchestration.md
├── examples/
│   ├── minimal-repo/
│   ├── recipe-base/
│   └── recipe-vertical/
├── presentation/
├── prompts/
└── scripts/
    └── validate-ai-devkit
```

## Core Files

| Path | Responsibility |
| ---- | -------------- |
| `AGENTS.md` | primary repo entry point and loader instructions |
| `README.md` | public product positioning and quick-start usage |
| `docs/standard/progressive-disclosure-standard.md` | normative spec for the docs model |
| `docs/standard/recipe-profile.md` | first-class extension profile for reusable starter repos |
| `docs/standard/spec-profile.md` | spec template, TDD workflow, and nine spec principles |
| `docs/standard/system-profile.md` | system-level dev environment profile |
| `docs/standard/agent-policy.md` | canonical shared policy |
| `docs/workflows/progressive-disclosure-docs.md` | canonical docs procedures |
| `docs/ai/` | self-hosted PD docs for this repo |
| `scripts/validate-ai-devkit` | repo validation and compliance checks |
| `prompts/` | standalone pipeable prompt files (`cat prompts/X.md \| claude`) |
| `docs/img/` | diagrams (AI SDLC flow SVG) |
| `examples/` | structural fixtures for adopters |
| `presentation/` | presentation video pipeline (audio, timing, subtitles) |

## Core Workflows

| Path | Responsibility |
| ---- | -------------- |
| `docs/workflows/progressive-disclosure-docs.md` | generate, update, test, fix, and review progressive disclosure docs |

## Where To Edit

| Goal | Edit First |
| ---- | ---------- |
| change policy wording | `docs/standard/agent-policy.md` |
| change standard rules | `docs/standard/progressive-disclosure-standard.md` |
| change recipe inheritance rules | `docs/standard/recipe-profile.md` |
| change prompt/workflow guidance | `docs/workflows/progressive-disclosure-docs.md` |
| change public positioning | `README.md` |
| change a prompt | `prompts/X.md`, then mirror in `README.md` `<details>` block |
| change self-hosted repo docs | `docs/ai/` |
| change validation checks | `scripts/validate-ai-devkit` |

## Files To Avoid Treating As Canonical

- root-level install notes that depend on the canonical docs
- README wording that summarizes but should not redefine policy

## Search Anchors

- Search for `fix docs` when aligning command lists.
- Search for `docs/workflows/` when validating canonical workflow references.
- Search for `repo-local` when validating precedence wording.
- Search for `docs/ai/` when checking self-hosted standard adoption.

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — Canonical file ownership and propagation model.
