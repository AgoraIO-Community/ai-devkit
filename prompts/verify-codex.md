## Verify with Codex

After completing the work above, use Codex as an independent Verify AI.

Read the fix workflow from the ai-devkit repo:
https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/workflows/progressive-disclosure-docs.md#fix

### Step 1: Codex review

Run this command to get Codex's independent review:

```
codex exec \
    --config 'model_reasoning_effort = "medium"' \
    --sandbox read-only \
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

**Running inside a container or CI** (where the OS sandbox can't initialise —
e.g. `bwrap: … Operation not permitted`): the host is already isolated, so
replace `--sandbox read-only --full-auto` with
`--dangerously-bypass-approvals-and-sandbox`, and use `codex exec` instead of
bare `codex` (the bare form opens an interactive TUI that won't work headless):

```
codex exec -m gpt-5.4 \
  --config model_reasoning_effort="medium" \
  --dangerously-bypass-approvals-and-sandbox \
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

### Step 2: Fix findings

For each finding Codex reported:

1. Read the cited doc file AND the source file side by side.
2. Determine the ground truth from the source code.
3. Patch the exact doc file at the correct level.
4. Do NOT blindly accept findings — verify each one against source.
5. Commit: docs: fix findings from codex review

### Step 3: Re-verify

Resume the Codex session to verify fixes:

```
echo "I fixed the findings you reported. Re-read docs/ai/ and verify each
fix against source. Report any remaining issues using the same FINDING format,
or say NO FINDINGS if everything is accurate." \
  | codex --skip-git-repo-check resume --last 2>/dev/null
```

In a container/CI environment, use `codex exec` with the bypass flag instead:

```
codex exec -m gpt-5.4 \
  --config model_reasoning_effort="medium" \
  --dangerously-bypass-approvals-and-sandbox \
  --skip-git-repo-check \
  "I fixed the findings you reported. Re-read docs/ai/ and verify each
fix against source. Report any remaining issues using the same FINDING format,
or say NO FINDINGS if everything is accurate." 2>/dev/null
```

If Codex reports new findings, repeat steps 2-3. Max 3 rounds.

### Rules

- Do not mark findings as fixed without checking the source file.
- Update last_reviewed in Level zero when done.
