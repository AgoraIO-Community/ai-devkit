# test

Verify that progressive disclosure docs give an agent the right context at the right level.

## Required Capabilities

- **Required:** read docs and source code, record results in markdown
- **Optional:** fresh sub-agents or separate sessions for unbiased doc-navigation tests
- **Optional:** git history inspection for better test questions
- **Fallback:** if sub-agents are unavailable, run the questions manually in a clean pass and record that limitation honestly

## Prerequisites

Check that these exist before testing:

- `docs/ai/L0_repo_card.md`
- all 8 L1 files
- `docs/ai/L1/L2/_index.md` if L2 files exist

If core docs are missing, run `generate` first.

## Workflow

### 1. Structural checks

Validate first:

- L0 exists and is under 50 lines
- all 8 L1 files exist and each is 80-200 lines
- each L1 starts with a one-line purpose statement
- each L1 ends with `## Related Deep Dives`
- L1 combined line count is under 1,600
- `docs/ai/L1/L2/_index.md` exists and lists all L2 files
- each L2 file starts with `> **When to Read This:** ...`
- links resolve
- `AGENTS.md` exists and has How to Load, Git Conventions, and Doc Commands
- `CLAUDE.md` references `@AGENTS.md` if present

If structural checks fail, stop and report them before content testing.

### 2. Generate test questions

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

### 3. Run tests

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

### 4. Analyze results

Use these interpretations:

| Result | Meaning | Action |
| ------ | ------- | ------ |
| Correct answer, right level loaded | PD docs working | None |
| Correct answer, but unnecessary L2 | L1 too thin | Expand relevant L1 section |
| Wrong answer, existing L2 not found | Bad cross-reference | Fix L1 deep-dive links |
| Wrong answer, no L2 exists | Missing deep dive | Create the L2 doc |
| No answer found | Missing L1 coverage | Add to relevant L1 file |

### 5. Write results

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

### 6. Fix and retest

If tests failed:

1. use `fix`
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
