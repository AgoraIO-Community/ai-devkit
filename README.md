# ai-devkit

Portable repo conventions and progressive-disclosure docs for AI-assisted
development.

This repo follows its own standard. Start with [AGENTS.md](AGENTS.md) and this
repo's [docs/ai](docs/ai/L0_repo_card.md) tree.

## What It Is

ai-devkit has three parts:

1. **A portable repo standard** built around `AGENTS.md` and `docs/ai/`
2. **Canonical workflow docs** under [docs/workflows](docs/workflows/)
3. **Optional adapters** under `skills/` and plugin config directories

The core value is curated context:

- repo-local conventions
- maintainable summaries of architecture and workflows
- tribal knowledge and gotchas that code alone does not express clearly

## Repo Layout

| Path | Purpose |
| ---- | ------- |
| [AGENTS.md](AGENTS.md) | primary repo entry point for agents |
| [docs/ai](docs/ai/L0_repo_card.md) | this repo's own progressive-disclosure docs |
| [docs/workflows](docs/workflows/) | canonical docs workflows |
| [docs/recipe-profile.md](docs/recipe-profile.md) | recipe inheritance profile for reusable starter repos |
| [examples/minimal-repo](examples/minimal-repo/README.md) | minimal structural fixture for adopters |
| [examples/recipe-base](examples/recipe-base/README.md) | base recipe fixture |
| [examples/recipe-vertical](examples/recipe-vertical/README.md) | vertical recipe fixture |
| [docs/policy/agent-policy.md](docs/policy/agent-policy.md) | canonical shared policy |
| [skills/ai-devkit](skills/ai-devkit/SKILL.md) | optional adapter layer for skill-aware tools |
| [docs/progressive-disclosure-standard.md](docs/progressive-disclosure-standard.md) | full standard |

## Quick Start

### Create docs in another repo

Paste this into an agent session:

```text
Your task is to add progressive disclosure documentation and git conventions to this repository.

Read these files from the ai-devkit repo:
1. docs/workflows/generate.md
2. docs/workflows/test.md
3. docs/progressive-disclosure-standard.md

Deliverables:
1. Add AGENTS.md at the repo root using the standard template.
2. Generate docs under docs/ai/.
3. Preserve existing repo docs.
4. If CLAUDE.md already exists, add a reference to AGENTS.md without replacing content.
5. Apply the documented git conventions.

After generating docs, run the test workflow. Fix findings and retest until the docs are accurate.
```

### Review docs

```text
Review this repo's progressive disclosure docs and provide feedback only.
Do not change files.

Read these files from the ai-devkit repo:
1. docs/workflows/test.md
2. docs/progressive-disclosure-standard.md

Compare docs/ai/ to the real codebase. Report inaccuracies, weak coverage, and recommended new test cases.
```

### Fix review findings

```text
Fix the review findings for this repo's progressive disclosure docs.

Read these files from the ai-devkit repo:
1. docs/workflows/fix.md
2. docs/progressive-disclosure-standard.md

Use fix.md to trace each finding to source, patch the exact doc file, update test-results, and re-check structure.
```

### Multi-agent review with Codex

Use [docs/workflows/review_codex.md](docs/workflows/review_codex.md).

It contains the independent Codex review loop, the `codex exec` commands, the
verification pass, and the batch-across-repos guidance.

### Recipe profile

Use [docs/recipe-profile.md](docs/recipe-profile.md) when a repo is a reusable
starter that should publish extension points and support child verticals.

## Compatibility

Compatibility is capability-based, not absolute.

| Tool | Plain Markdown | Skill Adapter | Session-Start Adapter | Multi-Agent Review |
| ---- | -------------- | ------------- | --------------------- | ------------------ |
| Claude Code | Yes | Yes | Yes | Yes |
| Cursor | Yes | Yes | Yes | Not documented here |
| Codex | Yes | Adapter docs only | No | Yes, as reviewer via CLI |
| Gemini | Yes | Minimal metadata only | No | Not documented here |
| Other tools | Usually yes | Depends on tool | Depends on tool | Depends on tool |

## Optional Adapters

The standard works without plugin installation. Adapters are optional.

### Claude Code

```text
/plugin marketplace add AgoraIO-Community/ai-devkit
/plugin install ai-devkit@ai-devkit
```

### Cursor

```bash
npx skills add AgoraIO-Community/ai-devkit
```

### Manual

```bash
git clone https://github.com/AgoraIO-Community/ai-devkit.git
```

Use:

- `AGENTS.md` when a repo already adopted the standard
- `skills/ai-devkit/SKILL.md` only when you need the adapter layer directly

## Notes

- `ship`, `pr`, and `sync` are optional helpers, not the core product
- canonical docs workflows live in `docs/workflows/`
- repo-local `AGENTS.md` overrides plugin-injected defaults

## References

- [Progressive Disclosure Standard](docs/progressive-disclosure-standard.md)
- [Recipe Profile](docs/recipe-profile.md)
- [Multi-Repo Orchestration Guide](docs/multi-repo-orchestration.md)
- [Agent Policy](docs/policy/agent-policy.md)
