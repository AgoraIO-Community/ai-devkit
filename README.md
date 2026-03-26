# ai-dev-kit

Skills that teach AI agents git conventions and documentation generation.

## Install

Add this repo as a skill for your AI coding tool. For Claude Code:

```bash
claude mcp add-skill https://github.com/BenWeekes/ai-dev-kit
```

Or clone and reference locally:

```bash
git clone https://github.com/BenWeekes/ai-dev-kit.git
```

## Skills

### /git — Git workflow conventions

Commit, push, and PR commands that enforce consistent conventions:

- **lowercase start** — commit messages and PR titles start lowercase
- **present tense** — "add feature" not "added feature"
- **no AI tool names** — no mentions of claude, cursor, copilot, etc.
- **no Co-Authored-By** — clean commit authorship

| Command      | What It Does                                                             |
| ------------ | ------------------------------------------------------------------------ |
| `/git:ship`  | Commit staged changes and push (enforces conventions)                    |
| `/git:pr`    | Create a PR from current branch to main with generated title and summary |
| `/git:sync`  | Pull latest from main, rebase current branch on top                      |

### /docs — Documentation generation

Generates progressive disclosure documentation (L0/L1/L2) following the
[Progressive Disclosure Documentation Standard](https://github.com/BenWeekes/ai-dev/blob/main/progressive-disclosure-standard.md).

| Command | What It Does                                                            |
| ------- | ----------------------------------------------------------------------- |
| `/docs` | Generate L0/L1/L2 docs for the repo following the PD standard          |

## Using with other skills

These skills work well alongside:

- [Superpowers](https://github.com/obra/superpowers) — spec, plan, TDD, review workflow
- [Spec Kit](https://github.com/github/spec-kit) — executable specifications

A typical combined workflow:

1. `/spec` — capture what you want to build
2. `/plan` — plan how to build it
3. `/tdd` — implement with tests
4. `/review` — review the changes
5. `/git:ship` — commit and push
6. `/git:pr` — create a PR
7. `/docs` — update repo docs if needed

## Related

- [AI-Assisted Development Guide](https://github.com/BenWeekes/ai-dev) — practices and standards for AI-assisted development
