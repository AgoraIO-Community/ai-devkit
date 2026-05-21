# generate

Generate progressive disclosure documentation for a repository from scratch.

## Required Capabilities

- **Required:** read repo files, write markdown files, inspect source and config
- **Optional:** web access to fetch ai-devkit from GitHub when the target repo does not vendor these docs locally
- **Optional:** sub-agents or parallel passes for large repos
- **Fallback:** if sub-agents are unavailable, read large modules in multiple local passes and synthesize manually

## Workflow

### 1. Read the standard

Read `docs/progressive-disclosure-standard.md` to understand the L0/L1/L2 architecture, file naming rules, token budgets, and content density targets.

### 2. Read existing project context

Read all markdown files and config/setup files in the repo root first:

- All `*.md` files
- Config files such as `package.json`, `Cargo.toml`, `go.mod`, `pyproject.toml`, `Dockerfile`, CI config
- Setup scripts such as `init.sh`, `bootstrap.sh`, `setup.py`

### 3. Map and deep-read the codebase

1. List the directory structure (top 3 levels)
2. Identify repo type
3. Identify major modules, packages, or service boundaries

For each major module:

- Read all source files, or a representative set if the module is very large
- Summarize purpose, key abstractions, public interfaces, internal patterns, external dependencies, and gotchas

If the repo is large:

- Split the reading into multiple passes
- Use sub-agents only if the tool supports them well

### 4. Synthesize and plan

Using the module summaries:

- Map the primary data flow
- Identify conventions consistent across modules
- Identify external interfaces
- Compile gotchas
- List key topics for each L1 file
- Identify 2-4 L2 deep dive topics when justified

Create an L2 deep dive when:

- an L1 file would need more than 10 lines to explain a subsystem
- the topic has complex multi-step sequences
- the topic changes frequently and benefits from isolated maintenance

### 5. Generate docs

Create files in this order:

1. `docs/ai/L0_repo_card.md`
2. all 8 L1 files in `docs/ai/L1/`
3. `docs/ai/L1/L2/_index.md`
4. any needed L2 deep dives

Also create or update:

- `AGENTS.md` at repo root using the expanded template from section 4.7 of the progressive disclosure standard. It must include all three sections: **How to Load**, **Git Conventions**, and **Doc Commands**.
- `CLAUDE.md` only if the repo uses Claude Code. If it already exists, add the `@AGENTS.md` reference without replacing content.

### 6. Verify

Structural checks:

- all relative links resolve
- L0 is under 50 lines
- each L1 file is 80-200 lines
- each L1 file starts with a one-line purpose statement
- each L1 file ends with `## Related Deep Dives`
- any L2 deep dive starts with `> **When to Read This:**`
- `AGENTS.md` has How to Load, Git Conventions, and Doc Commands
- `CLAUDE.md` references `@AGENTS.md` if present

Content self-test:

- Ask a common task question and trace the answer path from L0 to L1 and then L2 if needed
- If the answer path is unclear, improve cross-links or add an L2 doc
