Run a multi-agent review cycle on this repo's progressive disclosure docs
using Codex as an independent reviewer.

Read the fix workflow from the ai-devkit repo:
https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/workflows/progressive-disclosure-docs.md#fix

## Phase 1: Primary review

1. Read all files in docs/ai/ and compare every factual claim against the
   actual source code in this repo.
2. For each inaccuracy or gap, note the finding, the doc file, and the source
   file you checked.
3. Follow the Fix workflow to close each finding.
4. Commit: docs: fix findings from primary review

## Phase 2: Codex review

Run this command to get Codex's independent review:

```
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

## Phase 3: Fix Codex findings

1. Parse Codex's findings.
2. For each finding, follow the Fix workflow — trace to source, patch the
   exact doc file, record in the finding-to-fix matrix in test-results.md.
3. Commit: docs: fix findings from codex review

## Phase 4: Codex verification

Resume the Codex session to verify fixes:

```
echo "I fixed the findings you reported. Re-read docs/ai/ and verify each
fix against source. Report any remaining issues using the same FINDING format,
or say NO FINDINGS if everything is accurate." \
  | codex exec --skip-git-repo-check resume --last 2>/dev/null
```

If Codex reports new findings, repeat phases 3-4. Max 3 rounds.

## Rules

- Do not mark findings as fixed without checking the source file.
- Do not use generate or update to close findings — use the Fix workflow.
- Update last_reviewed in level zero when done.
