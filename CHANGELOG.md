# Changelog

## Unreleased

- restructure docs/ — add standard/ and guides/, merge workflow files into progressive-disclosure-docs.md
- **breaking:** remove adapter layer (skills/, hooks/, plugin configs, GEMINI.md). Use the copy-paste prompts in the README instead.
- make compatibility claims capability-based and explicit about test status
- clarify that `AGENTS.md` is the primary portable delivery path; no install required
- align the docs test guidance with the expanded `AGENTS.md` template requirements

## 1.1.0

- migrate to skill-based architecture with session-start hook
- replace slash commands with Skill tool discovery
- add hooks/ for ambient convention injection at session start
- add plugin configs for multiple platforms
- delete commands/ directory

## 1.0.0

- initial release with slash commands
- git conventions: ship, pr, sync
- docs generation: generate, update, test
- progressive disclosure documentation standard
- multi-repo orchestration guide
