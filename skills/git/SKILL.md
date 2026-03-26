# Git Workflow Conventions

This skill provides git commands that enforce consistent conventions across AI-assisted development.

## Commit Message Rules

- **lowercase start** — first character must be lowercase
- **present tense** — "add feature" not "added feature"
- **no AI tool names** — no mentions of claude, cursor, copilot, cody, aider, gemini, codex, chatgpt, gpt-3, gpt-4
- **no Co-Authored-By** — do not add Co-Authored-By trailers
- **concise** — one line summarizing the change

## Commands

| Command     | What It Does                                                             |
| ----------- | ------------------------------------------------------------------------ |
| `/git:ship` | Commit staged changes and push (enforces conventions above)              |
| `/git:pr`   | Create a PR from current branch to main with generated title and summary |
| `/git:sync` | Pull latest from main, rebase current branch on top                      |
