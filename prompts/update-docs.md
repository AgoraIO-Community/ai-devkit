Your task is to update this repository's Progressive Disclosure documentation
to reflect recent code or convention changes.

Read these files from the ai-devkit repo:

1. https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/workflows/progressive-disclosure-docs.md#update — the update workflow
2. https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/workflows/progressive-disclosure-docs.md#test — the test workflow
3. https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/standard/progressive-disclosure-standard.md — the full standard

Steps:

1. Read the existing docs/ai/ tree end to end.
2. Read recent git history (git log --oneline -20) to identify what changed.
3. Compare docs/ai/ claims against the current source code.
4. Update only the docs that have drifted — do not regenerate from scratch.
5. If a change affects Level one, check whether the related Level two deep
   dives also need updating.
6. Update last_reviewed in docs/ai/L0_repo_card.md.
7. Run the test workflow. Fix failures and retest until all pass.

Rules:

- Only change docs that are actually stale. Do not rewrite docs that are
  already accurate.
- Preserve the existing structure and style.
- Use the real terminology from the codebase, not generic filler.

When finished:

1. Summarize what you changed and why.
2. Commit with: docs: update progressive disclosure documentation
