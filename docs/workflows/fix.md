# fix

Close review findings against progressive disclosure docs by tracing each finding to source and patching the correct disclosure level.

## Required Capabilities

- **Required:** read source files, edit markdown, verify claims against code
- **Optional:** fresh retest sessions or sub-agents after fixes
- **Fallback:** if a clean retest is unavailable, record that the fix was source-verified but not independently retested

## Prerequisites

- review findings exist in `docs/ai/test-results.md` or were provided directly
- `docs/ai/L0_repo_card.md` and the L1 docs already exist

## Workflow

### 1. Collect findings

Read the prior review output:

- `docs/ai/test-results.md`
- any externally provided findings

Create a checklist of distinct findings with:

- the exact claim or gap
- the target doc file or files

### 2. Trace each finding to source

For each finding:

1. read the cited doc file
2. read the source code or config behind the finding
3. determine the ground truth

Do not rely on review text alone.

### 3. Decide disclosure level

Use this rule:

| Content size/complexity | Target |
| --- | --- |
| 1-3 lines of factual correction | L1 |
| New section >10 lines | L2 |
| Repo-root loading or conventions issue | `AGENTS.md` or adapter docs |
| Test coverage observation | `docs/ai/test-results.md` |
| Multiple levels affected | Update all affected files |

A common failure mode is fixing only L2 when the cited problem is really in L1. Check both.

### 4. Patch docs

For each finding:

- edit the exact cited file
- keep L1 concise
- update `_index.md` and L1 links when adding L2
- describe missing test coverage honestly

### 5. Maintain the finding-to-fix matrix

Update `docs/ai/test-results.md` under `## Review Fix Retest` with this table:

```markdown
## Review Fix Retest

Retested: [date]

| Finding | Source checked | Docs changed | Result | Notes |
| ------- | -------------- | ------------ | ------ | ----- |
| [exact finding] | [source files read] | [doc files edited] | Pass / Partial / Open | [what was verified] |
```

Status values:

- **Pass** — doc patched, verified against source, retest passed if available
- **Partial** — doc updated but a coverage gap remains
- **Open** — intentionally deferred

The `Source checked` column is critical. It prevents copying review text into docs without source verification.

### 6. Structural re-check

After fixes:

- validate links
- validate modified L1 structure
- validate any new L2 callouts
- update `last_reviewed` in L0

### 7. Report

Summarize:

- what was fixed
- what remains partial
- what was intentionally deferred
