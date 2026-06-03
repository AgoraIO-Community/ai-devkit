Fix the review findings for this repo's progressive disclosure docs.

Read these files from the ai-devkit repo
(https://github.com/AgoraIO-Community/ai-devkit.git):

1. docs/workflows/progressive-disclosure-docs.md#fix — the fix workflow
2. docs/standard/progressive-disclosure-standard.md — the full standard

Follow the Fix workflow:

1. Read docs/ai/test-results.md for findings.
2. For each finding, trace it to the actual source code.
3. Patch the exact cited doc files at the correct disclosure level.
4. Record a finding-to-fix matrix in docs/ai/test-results.md.
5. Re-run structural checks.
6. Commit with: docs: fix review findings
