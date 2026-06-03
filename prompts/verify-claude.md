## Verify with Claude

After completing the work above, use Claude as an independent Verify AI.

Read the fix workflow from the ai-devkit repo:
https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/workflows/progressive-disclosure-docs.md#fix

### Step 1: Claude review

Run this command to get Claude's independent review:

```
claude --dangerously-skip-permissions -p "Read every file in docs/ai/ and compare each factual claim against the actual source code. For each doc file, report findings as:

FINDING: [description]
FILE: [doc file]
SOURCE: [source file checked]
SEVERITY: high | medium | low
RECOMMENDATION: [what to fix]

If everything is accurate, say: NO FINDINGS"
```

### Step 2: Fix findings

For each finding Claude reported:

1. Read the cited doc file AND the source file side by side.
2. Determine the ground truth from the source code.
3. Patch the exact doc file at the correct level.
4. Do NOT blindly accept findings — verify each one against source.
5. Commit: docs: fix findings from claude review

### Step 3: Re-verify

Run Claude again to verify fixes:

```
claude --dangerously-skip-permissions -p "I fixed the findings you reported. Re-read docs/ai/ and verify each fix against source. Report any remaining issues using the same FINDING format, or say NO FINDINGS if everything is accurate."
```

If Claude reports new findings, repeat steps 2-3. Max 3 rounds.

### Rules

- Do not mark findings as fixed without checking the source file.
- Update last_reviewed in Level zero when done.
