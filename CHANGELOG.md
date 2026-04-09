# Changelog

## Unreleased

- make compatibility claims more explicit: tested primarily with Claude Code and Codex
- clarify that `AGENTS.md` is the primary portable delivery path and plugin hooks are optional reinforcement
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
