# review_codex

Run a multi-agent review cycle using Codex as an independent reviewer after progressive-disclosure docs already exist.

## Required Capabilities

- **Required:** `codex` CLI installed and available on `PATH`
- **Required:** ability to read docs and source code in the target repo
- **Optional:** Claude Code or another orchestrator to parse and fix findings between Codex passes
- **Fallback:** if orchestration is unavailable, run the Codex review command manually and apply fixes yourself

## Workflow

### 1. Primary review

Do a normal human or agent review first:

1. Read all files in `docs/ai/`
2. Compare every factual claim against the real codebase
3. Record findings with doc file and source file
4. Use [fix.md](fix.md) to close those findings

### 2. Codex independent review

Run:

```bash
codex exec -m gpt-5.4 \
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

### 3. Fix Codex findings

For each finding:

1. trace it to source
2. patch the exact doc file
3. record it in the finding-to-fix matrix in `docs/ai/test-results.md`
4. update `last_reviewed` in L0 if docs changed

### 4. Codex verification

Run:

```bash
echo "I fixed the findings you reported. Re-read docs/ai/ and verify each
fix against source. Report any remaining issues using the same FINDING format,
or say NO FINDINGS if everything is accurate." \
  | codex exec --skip-git-repo-check resume --last 2>/dev/null
```

If Codex reports new findings, repeat fix and verification. Stop after 3 rounds.

## Rules

- do not mark a finding fixed without checking the source file
- do not use `generate` or `update` to close review findings
- keep the finding-to-fix matrix current

## Batch Across Repos

To run this flow across multiple repos:

1. work from a parent directory containing the cloned repos
2. generate or update docs repo by repo
3. run the primary review
4. run the Codex review
5. fix findings and verify before moving on
