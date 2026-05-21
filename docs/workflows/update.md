# update

Update existing progressive disclosure documentation after code or convention changes.

## Required Capabilities

- **Required:** read repo files and edit markdown
- **Optional:** git history inspection to scope changes
- **Fallback:** if history is unavailable, diff the current docs against the current codebase directly

## Workflow

### 1. Identify what changed

Determine the scope to document:

- Use the requested scope if the user provided one
- Otherwise compare changes since `last_reviewed` in `docs/ai/L0_repo_card.md`
- If no reliable date exists, inspect the last 30 days of changes

Group changes into:

- new modules
- changed interfaces
- new workflows
- new gotchas
- deprecated features
- dependency changes
- removed code

### 2. Read current docs

Read:

1. `docs/ai/L0_repo_card.md`
2. all 8 L1 files
3. `docs/ai/L1/L2/_index.md`

Only read an L2 file when a change directly affects its topic.

### 3. Map changes to docs

Examples:

- new module or package -> `03_code_map.md`
- changed API or contract -> `06_interfaces.md`
- new workflow -> `05_workflows.md`
- new convention -> `04_conventions.md`
- new gotcha -> `07_gotchas.md`
- security model change -> `08_security.md`

### 4. Read the changed code

Read the actual source files, config, and tests behind each documented change.

### 5. Update docs

- change only affected docs
- preserve accurate content
- keep each modified L1 file within 80-200 lines
- create or expand L2 only when detail outgrows L1

If you create a new L2:

1. add it under `docs/ai/L1/L2/`
2. add it to `_index.md`
3. link it from the relevant L1 file

### 6. Update L0

- set `last_reviewed` to today
- update identity or L1 index details if needed

### 7. Verify

- links resolve
- modified L1 files still fit the structure
- new L2 files start with the required callout
- no stale information remains in touched sections
