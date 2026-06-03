# Progressive Disclosure Docs

> Canonical workflows for generating, updating, testing, fixing, and
> reviewing progressive disclosure documentation.

## Generate

Generate progressive disclosure documentation for a repository from scratch.

### Required Capabilities

- **Required:** read repo files, write markdown files, inspect source and config
- **Optional:** web access to fetch ai-devkit from GitHub when the target repo does not vendor these docs locally
- **Optional:** sub-agents or parallel passes for large repos
- **Fallback:** if sub-agents are unavailable, read large modules in multiple local passes and synthesize manually

### Workflow

#### 1. Read the standard

Read `docs/standard/progressive-disclosure-standard.md` to understand the L0/L1/L2 architecture, file naming rules, token budgets, and content density targets.

#### 2. Read existing project context

Read all markdown files and config/setup files in the repo root first:

- All `*.md` files
- Config files such as `package.json`, `Cargo.toml`, `go.mod`, `pyproject.toml`, `Dockerfile`, CI config
- Setup scripts such as `init.sh`, `bootstrap.sh`, `setup.py`

#### 3. Map and deep-read the codebase

1. List the directory structure (top 3 levels)
2. Identify repo type
3. Identify major modules, packages, or service boundaries

For each major module:

- Read all source files, or a representative set if the module is very large
- Summarize purpose, key abstractions, public interfaces, internal patterns, external dependencies, and gotchas

If the repo is large:

- Split the reading into multiple passes
- Use sub-agents only if the tool supports them well

#### 4. Synthesize and plan

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

#### 5. Generate docs

Create files in this order:

1. `docs/ai/L0_repo_card.md`
2. all 8 L1 files in `docs/ai/L1/`
3. `docs/ai/L1/L2/_index.md`
4. any needed L2 deep dives

Also create or update:

- `AGENTS.md` at repo root using the expanded template from section 4.7 of the progressive disclosure standard. It must include all three sections: **How to Load**, **Git Conventions**, and **Doc Commands**.
- `CLAUDE.md` only if the repo uses Claude Code. If it already exists, add the `@AGENTS.md` reference without replacing content.

#### 6. Verify

Structural checks:

- all relative links resolve
- L0 is under 50 lines
- each L1 file targets 80-200 lines (smaller stubs are acceptable for structural fixtures and inherited recipe slots)
- each L1 file starts with a one-line purpose statement
- each L1 file ends with `## Related Deep Dives`
- any L2 deep dive starts with `> **When to Read This:**`
- `AGENTS.md` has How to Load, Git Conventions, and Doc Commands
- `CLAUDE.md` references `@AGENTS.md` if present

Content self-test:

- Ask a common task question and trace the answer path from L0 to L1 and then L2 if needed
- If the answer path is unclear, improve cross-links or add an L2 doc

## Update

Update existing progressive disclosure documentation after code or convention changes.

### Required Capabilities

- **Required:** read repo files and edit markdown
- **Optional:** git history inspection to scope changes
- **Fallback:** if history is unavailable, diff the current docs against the current codebase directly

### Workflow

#### 1. Identify what changed

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

#### 2. Read current docs

Read:

1. `docs/ai/L0_repo_card.md`
2. all 8 L1 files
3. `docs/ai/L1/L2/_index.md`

Only read an L2 file when a change directly affects its topic.

#### 3. Map changes to docs

Examples:

- new module or package -> `03_code_map.md`
- changed API or contract -> `06_interfaces.md`
- new workflow -> `05_workflows.md`
- new convention -> `04_conventions.md`
- new gotcha -> `07_gotchas.md`
- security model change -> `08_security.md`

#### 4. Read the changed code

Read the actual source files, config, and tests behind each documented change.

#### 5. Update docs

- change only affected docs
- preserve accurate content
- target 80-200 lines per L1 file; smaller stubs are acceptable for structural fixtures and inherited recipe slots
- create or expand L2 only when detail outgrows L1

If you create a new L2:

1. add it under `docs/ai/L1/L2/`
2. add it to `_index.md`
3. link it from the relevant L1 file

#### 6. Update L0

- set `last_reviewed` to today
- update identity or L1 index details if needed

#### 7. Verify

- links resolve
- modified L1 files still fit the structure
- new L2 files start with the required callout
- no stale information remains in touched sections

## Test

Verify that progressive disclosure docs give an agent the right context at the right level.

### Required Capabilities

- **Required:** read docs and source code, record results in markdown
- **Optional:** fresh sub-agents or separate sessions for unbiased doc-navigation tests
- **Optional:** git history inspection for better test questions
- **Fallback:** if sub-agents are unavailable, run the questions manually in a clean pass and record that limitation honestly

### Prerequisites

Check that these exist before testing:

- `docs/ai/L0_repo_card.md`
- all 8 L1 files
- `docs/ai/L1/L2/_index.md` if L2 files exist

If core docs are missing, run `generate` first.

### Workflow

#### 1. Structural checks

Validate first:

- L0 exists and is under 50 lines
- all 8 L1 files exist and each targets 80-200 lines (smaller stubs acceptable)
- each L1 starts with a one-line purpose statement
- each L1 ends with `## Related Deep Dives`
- L1 combined line count is under 1,600
- `docs/ai/L1/L2/_index.md` exists and lists all L2 files
- each L2 file starts with `> **When to Read This:** ...`
- links resolve
- `AGENTS.md` exists and has How to Load, Git Conventions, and Doc Commands
- `CLAUDE.md` references `@AGENTS.md` if present

If structural checks fail, stop and report them before content testing.

#### 2. Generate test questions

Create questions in these categories:

**Setup & Build**

- How do I install dependencies and build this project?
- What environment variables are required?
- What local tools are required?

**Test & Run**

- How do I run the test or validation flow?
- How do I start the project locally if it runs as an app or service?

**Conventions**

- What naming conventions does this project use?
- How should errors, reviews, and docs updates be handled?

**Development**

- Use recent git history to identify 2-3 real changes
- Turn those into questions like: "How would I add a similar feature to [area]?"
- These should require architecture knowledge, not just setup

**Deep Dive**

- Pick a complex subsystem and ask about its internals
- Ask about an edge case or non-obvious behavior
- These should only be answerable with L2 detail

If the caller specifies a focus area, weight questions toward that area.

#### 3. Run tests

For each question:

1. Prefer a fresh sub-agent or clean session if available
2. Give only the question and this instruction:
   `After answering, list every file you read to reach your answer.`
3. Do not tell it which docs to read
4. Record the answer, files read, whether the answer was correct, and what level was loaded

Classify results as:

- L0+L1 sufficient
- L2 required and correctly used
- missing L1 coverage
- missing L2
- broken cross-reference

#### 4. Analyze results

Use these interpretations:

| Result | Meaning | Action |
| ------ | ------- | ------ |
| Correct answer, right level loaded | PD docs working | None |
| Correct answer, but unnecessary L2 | L1 too thin | Expand relevant L1 section |
| Wrong answer, existing L2 not found | Bad cross-reference | Fix L1 deep-dive links |
| Wrong answer, no L2 exists | Missing deep dive | Create the L2 doc |
| No answer found | Missing L1 coverage | Add to relevant L1 file |

#### 5. Write results

Save results to `docs/ai/test-results.md`.

**Honesty rules:**

- Do not mark a question as `Pass` unless the answer was actually verified against source
- If a tool limitation prevented a clean sub-agent pass, say so explicitly
- If docs reference tests that do not assert the behavior, label coverage as `needed`, not "tests to run"
- If a question was added after a fix pass but was not actually re-tested, do not include it in the results table

Use this template:

```markdown
# PD Documentation Test Results

Tested: [date]
Agent: [which agent/model]
Repo: [repo name]

## Summary

- Total questions: N
- Passed: N (correct answer, right level)
- L1 gaps: N (needed L2 but L1 should have sufficed)
- L2 gaps: N (needed L2 that doesn't exist)
- Cross-ref issues: N (L2 exists but wasn't found)

## Results

### Setup & Build

| # | Question | Answer Correct? | Files Read | Level Loaded | Result |
| - | -------- | --------------- | ---------- | ------------ | ------ |
| 1 | How do I build? | Yes | L0, 01_setup | L0+L1 | Pass |

### Test & Run

...

### Conventions

...

### Development

...

### Deep Dive

...

## Recommended Fixes

- [ ] Expand 01_setup.md section on [topic] (questions N, N failed)
- [ ] Add deep dive: [topic].md (question N needed detail not in L1)
- [ ] Fix Related Deep Dives link in 02_architecture.md (question N)
```

#### 6. Fix and retest

If tests failed:

1. use [Fix](#fix)
2. rerun only the failing questions
3. append a retest section to `docs/ai/test-results.md`

Use this retest template:

```markdown
## Review Fix Retest

Retested: [date]

| Finding | Source checked | Docs changed | Result | Notes |
| ------- | -------------- | ------------ | ------ | ----- |
| [exact finding from review] | [source files read] | [doc files edited] | Pass / Partial / Open | [what was verified] |
```

Mark findings as:

- **Pass** — fix verified against source, and the retest answered correctly
- **Partial** — docs updated but a coverage gap remains
- **Open** — intentionally deferred

## Fix

Close review findings against progressive disclosure docs by tracing each finding to source and patching the correct disclosure level.

### Required Capabilities

- **Required:** read source files, edit markdown, verify claims against code
- **Optional:** fresh retest sessions or sub-agents after fixes
- **Fallback:** if a clean retest is unavailable, record that the fix was source-verified but not independently retested

### Prerequisites

- review findings exist in `docs/ai/test-results.md` or were provided directly
- `docs/ai/L0_repo_card.md` and the L1 docs already exist

### Workflow

#### 1. Collect findings

Read the prior review output:

- `docs/ai/test-results.md`
- any externally provided findings

Create a checklist of distinct findings with:

- the exact claim or gap
- the target doc file or files

#### 2. Trace each finding to source

For each finding:

1. read the cited doc file
2. read the source code or config behind the finding
3. determine the ground truth

Do not rely on review text alone.

#### 3. Decide disclosure level

Use this rule:

| Content size/complexity | Target |
| --- | --- |
| 1-3 lines of factual correction | L1 |
| New section >10 lines | L2 |
| Repo-root loading or conventions issue | `AGENTS.md` |
| Test coverage observation | `docs/ai/test-results.md` |
| Multiple levels affected | Update all affected files |

A common failure mode is fixing only L2 when the cited problem is really in L1. Check both.

#### 4. Patch docs

For each finding:

- edit the exact cited file
- keep L1 concise
- update `_index.md` and L1 links when adding L2
- describe missing test coverage honestly

#### 5. Maintain the finding-to-fix matrix

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

#### 6. Structural re-check

After fixes:

- validate links
- validate modified L1 structure
- validate any new L2 callouts
- update `last_reviewed` in L0

#### 7. Report

Summarize:

- what was fixed
- what remains partial
- what was intentionally deferred

## Review with Codex

Run a multi-agent review cycle using Codex as an independent reviewer after progressive-disclosure docs already exist.

### Required Capabilities

- **Required:** `codex` CLI installed and available on `PATH`
- **Required:** ability to read docs and source code in the target repo
- **Optional:** Claude Code or another orchestrator to parse and fix findings between Codex passes
- **Fallback:** if orchestration is unavailable, run the Codex review command manually and apply fixes yourself

### Workflow

#### 1. Primary review

Do a normal human or agent review first:

1. Read all files in `docs/ai/`
2. Compare every factual claim against the real codebase
3. Record findings with doc file and source file
4. Use [Fix](#fix) to close those findings

#### 2. Codex independent review

Run:

```bash
codex -m gpt-5.4 \
  --config model_reasoning_effort="medium" \
  --sandbox read-only \
  --full-auto \
  --skip-git-repo-check \
  "Read every file in docs/ai/ and compare each factual claim against
the actual source code. For each doc file, report findings as:

FINDING: [description]
FILE: [doc file]
SOURCE: [source file checked]
SEVERITY: high | medium | low
RECOMMENDATION: [what to fix]

If everything is accurate, say: NO FINDINGS" 2>/dev/null
```

#### 3. Fix Codex findings

For each finding:

1. trace it to source
2. patch the exact doc file
3. record it in the finding-to-fix matrix in `docs/ai/test-results.md`
4. update `last_reviewed` in L0 if docs changed

#### 4. Codex verification

Run:

```bash
echo "I fixed the findings you reported. Re-read docs/ai/ and verify each
fix against source. Report any remaining issues using the same FINDING format,
or say NO FINDINGS if everything is accurate." \
  | codex --skip-git-repo-check resume --last 2>/dev/null
```

If Codex reports new findings, repeat fix and verification. Stop after 3 rounds.

### Rules

- do not mark a finding fixed without checking the source file
- do not use `generate` or `update` to close review findings
- keep the finding-to-fix matrix current

### Batch Across Repos

To run this flow across multiple repos:

1. work from a parent directory containing the cloned repos
2. generate or update docs repo by repo
3. run the primary review
4. run the Codex review
5. fix findings and verify before moving on
