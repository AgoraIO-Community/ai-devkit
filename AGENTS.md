# Agent Conventions

This repo provides skills (slash commands) for AI-assisted development. The skills are plain markdown files in `skills/`.

## Repo Structure

| Path                  | Purpose                                         |
| --------------------- | ----------------------------------------------- |
| `skills/git/`         | Git workflow commands (ship, pr, sync)           |
| `skills/docs/`        | Documentation generation command                 |
| `README.md`           | Overview and install instructions                |
| `AGENTS.md`           | Agent conventions (this file)                    |

## Conventions

1. **Commit messages:** lowercase start, no AI tool names, present tense, no Co-Authored-By.
2. **PR titles:** lowercase start, under 70 characters.
3. **Slash commands are simple markdown.** A command is a prompt with `$ARGUMENTS` placeholder. No scripts, no execution logic.

## Skills

| Skill           | Entry Point              | Commands                         |
| --------------- | ------------------------ | -------------------------------- |
| Git workflow    | `skills/git/SKILL.md`    | `/git:ship`, `/git:pr`, `/git:sync` |
| Documentation   | `skills/docs/SKILL.md`   | `/docs`                          |
