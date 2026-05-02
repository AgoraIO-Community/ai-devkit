---
name: fix
description: Close review findings by tracing each one to source code and patching the exact cited docs. Use after "test docs" produces findings, or after a human review identifies gaps.
---

# fix

Close review findings against the progressive disclosure docs. Each finding is traced to source code, patched at the correct disclosure level, and re-verified.

Do NOT use `generate` or `update` for this. Those workflows are not finding-driven — they will add related text without closing the specific finding.

## Prerequisites

- `docs/ai/test-results.md` exists with findings, OR the user provides review findings directly.
- `docs/ai/L0_repo_card.md` and `docs/ai/L1/` exist. If not, run `generate` first.

## Workflow

### 1. Collect findings

Read the prior review output:

- `docs/ai/test-results.md` — check the Recommended Fixes section and any failing rows in Results tables
- If `$ARGUMENTS` specifies findings or a review source, use those instead

Create a checklist of every distinct finding. Each entry must have:

- The exact claim or gap described
- The doc file(s) the review cited — if the review did not cite specific files, identify the target doc files yourself by matching the finding's topic to the L1/L2 file responsibilities

### 2. Trace each finding to source

For each finding:

1. Read the cited doc file(s) to understand what's currently written.
2. Read the actual source code, config, or test files that the finding is about. Do not rely on the review text alone — verify against the repo.
3. Determine the ground truth: what does the code actually do?

### 3. Decide disclosure level

For each finding, decide where the fix belongs:

| Content size/complexity | Target |
| --- | --- |
| 1-3 lines of factual correction | L1 file |
| New section >10 lines | L2 deep dive (add or update) |
| Test coverage observation | `test-results.md` |
| Repo-root doc issue (loading, conventions, commands) | `AGENTS.md` or `CLAUDE.md` |
| Multiple levels affected | Update all affected files |

A common failure mode: fixing an L2 file but missing the L1 file that the review actually cited. Check both.

### 4. Patch docs

For each finding:

- Edit the exact cited file(s) and location(s).
- If adding to L1, keep the file within 80-200 lines. Move detail to L2 if needed.
- If creating a new L2 file, add it to `L2/_index.md` and the relevant L1 `## Related Deep Dives`.
- If the finding is about test coverage that doesn't exist, state that honestly — label as "needed coverage," not "tests to run."

### 5. Maintain finding-to-fix matrix

Build or update this table in `docs/ai/test-results.md` under a `## Review Fix Retest` section:

```markdown
## Review Fix Retest

Retested: [date]

| Finding | Source checked | Docs changed | Result | Notes |
| ------- | -------------- | ------------ | ------ | ----- |
| [exact finding] | [source files read] | [doc files edited] | Pass / Partial / Open | [what was verified] |
```

Status values:

- **Pass** — doc patched, verified against source, sub-agent re-test passed (if applicable)
- **Partial** — doc updated but a coverage gap remains (note what's missing)
- **Open** — intentionally deferred (note why)

The "Source checked" column is critical — it prevents the agent from copying review text into a doc without verifying it against code.

### 6. Structural re-check

After all patches:

- All cross-references resolve
- Each modified L1 file is still 80-200 lines
- Any new L2 files start with `> **When to Read This:** ...`
- `L2/_index.md` lists all L2 files
- `AGENTS.md` has How to Load, Git Conventions, and Doc Commands sections
- `CLAUDE.md` (if present) references @AGENTS.md
- `last_reviewed` in L0 is updated to today

### 7. Report

Summarize what was closed:

```
## Findings Closed

- [finding]: fixed in [file(s)], verified against [source file(s)]
- [finding]: partial — [what remains]
- [finding]: deferred — [reason]
```
