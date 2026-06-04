# 05 Workflows

> Step-by-step maintenance flows for the standard, canonical docs, and self-hosted repo docs.

**Note:** ai-devkit is a standards repo — its canonical workflow procedures live
in `docs/workflows/` and `docs/standard/spec-profile.md`. Adopting repos get
materialised copies of these workflows in their own `05_workflows.md` at
bootstrap. This file describes how to maintain ai-devkit itself.

## Common Tasks

| Task | Start Here | Also Review |
| ---- | ---------- | ----------- |
| change shared policy | `docs/standard/agent-policy.md` | `AGENTS.md`, standard template |
| change standard wording | `docs/standard/progressive-disclosure-standard.md` | `README.md`, `docs/ai/`, validator |
| change recipe inheritance rules | `docs/standard/recipe-profile.md` | recipe fixtures, standard references, README |
| change docs workflow behavior | `docs/workflows/progressive-disclosure-docs.md` | README prompts |
| change repo self-description | `docs/ai/` | `AGENTS.md`, `last_reviewed` |
| change a prompt | `prompts/X.md` | `README.md` `<details>` block for the same prompt |

## Update Shared Policy

1. Edit `docs/standard/agent-policy.md`.
2. Update any mirrored summaries in `AGENTS.md`.
3. Update the standard template if the change affects copied repo instructions.
4. Run validation.

## Update the Standard

1. Edit `docs/standard/progressive-disclosure-standard.md`.
2. Check whether the change affects:
   - root `AGENTS.md`
   - `docs/ai/`
   - canonical workflows
   - README claims
3. Update the affected files in the same change.
4. Run validation.

## Update Canonical Workflows

1. Edit the target file in `docs/workflows/`.
2. Update README prompts if file locations or command semantics changed.
3. Run validation.

## Canonical Workflow Link

- [progressive-disclosure-docs](../../workflows/progressive-disclosure-docs.md) — generate, update, test, fix, and review

This file stays outside `docs/ai/` because it is a reusable product procedure.
This L1 file describes how ai-devkit uses and maintains it.

## Update Self-Hosted Docs

1. Change the affected `docs/ai/` file.
2. Update `docs/ai/L0_repo_card.md` `Last Reviewed`.
3. Verify related deep-dive links still make sense.
4. Run validation.

## Update a Prompt

1. Edit `prompts/X.md` with the new prompt text.
2. Copy the same text into the corresponding `<details>` block in `README.md`.
3. Verify the `Run:` command and `> Standalone file:` reference are correct.
4. Commit both files together.

## Review Loop

1. Compare public promises to shipped files.
2. Compare root `AGENTS.md` to the standard template intent.
3. Compare `docs/ai/` to the current repo layout.
4. Record any findings before making broad rewrites.

## Path-Move Rules

- If a canonical file moves, update every public reference in the same change.
- Do not move files just to reduce top-level clutter if it breaks discoverability.
- Treat path changes as product changes, not cosmetic cleanup.

## Self-Hosting Workflow

1. update the product docs
2. update `docs/ai/` if repo behavior changed
3. update `Last Reviewed` in L0
4. run validation
5. scan `README.md` and `AGENTS.md` for stale public claims

## Regenerate Presentation

When `presentation.md` or `presentation/player.html` changes:

1. Source the API key: `source .env && export TTS_KEY`
2. Regenerate audio: `python3 presentation/generate.py` (all slides) or `python3 presentation/generate.py N` (single slide)
3. Translate `presentation/subs/en.srt` to `presentation/subs/zh.srt` (keep timestamps identical, keep technical terms in English)
4. Start HTTP server if needed: `python3 -m http.server 8090 -d presentation &`
5. Record video: `nvm use 22 && node presentation/record.mjs`
6. Output lands in `presentation/runs/`

See [elevenlabs_voiceover.md](L2/elevenlabs_voiceover.md) for API details, audio tag reference, and script conventions.

## Related Deep Dives

- [policy_delivery.md](L2/policy_delivery.md) — Detailed change propagation for policy and workflow updates.
- [elevenlabs_voiceover.md](L2/elevenlabs_voiceover.md) — TTS API reference and presentation pipeline.
