# AI DevKit

**An operating model for AI-centric software engineering.**

AI DevKit publishes standards and workflow templates for AI-centric software engineering — a model in which AI agents do the bulk of execution work and humans make the highest-leverage decisions. It combines a documentation standard (Progressive Disclosure docs) with a multi-model lifecycle that runs from work intake to release.

## The AI Software Development Lifecycle

AI DevKit publishes standards. The diagrams below depict the lifecycle those standards enable inside an adopting repo.

![AI Software Development Lifecycle flow](docs/img/ai-sdlc-flow.svg)

*Work flows from intake (story, epic, bug, or feature) through Plan, Implementation, and Release. The Lead AI executes the workflow; the Verifier AI independently checks key transitions. The Plan phase produces a spec; the Implementation phase produces working code, tests, and updated docs.*

```mermaid
sequenceDiagram
    participant W as Work item
    participant H as Human
    participant A as Lead AI (A)
    participant B as Verifier AI (B)
    participant PD as Progressive Disclosure docs
    participant CI as Release

    W->>H: story / epic / bug / feature

    Note over H,PD: Plan — Lead AI runs the spec workflow
    H->>A: kickoff
    A->>PD: read level one + workflow
    A->>A: scan code, draft spec (acceptance criteria, edges, test plan)
    A->>B: cross-verify (restate acceptance criteria)
    B-->>A: divergences flagged
    A->>H: spec for review
    H-->>A: approval

    Note over A,PD: Implementation — Lead AI runs test-driven development + Progressive Disclosure docs
    A->>PD: read gotchas + conventions
    A->>A: Red — write failing tests
    A->>B: handoff for Green
    B-->>A: implementation + tests pass
    A->>A: Refactor
    A->>PD: update affected level one files
    A->>B: cross-verify doc updates
    B-->>A: doc review

    A->>CI: deliverable (code, docs, git)

    Note over CI,H: Release — human approves
    CI->>CI: run verification suite
    CI->>H: ready to merge
    H-->>CI: approve & merge
```

*The same flow shown as interactions. The Lead AI reads and updates Progressive Disclosure docs at each phase boundary, and the Verifier AI checks key transitions independently.*

## Lead AI and Verifier AI

**Lead AI** executes the workflow — it reads the procedure from Progressive Disclosure docs and works through it step by step. **Verifier AI** independently checks key transitions — it's a second AI from a different training lineage.

Which provider takes which role can vary per phase and per repo. What matters is that the two AIs come from independent training lineages. A single AI is confidently wrong in ways invisible to itself, and asking the same model to review its own output rarely catches the error. Two independent lineages catch different mistakes.

## Plan

**What it is.** Plan turns a work item — story, epic, bug, or feature — into an approved spec: a short markdown file with acceptance criteria, edge cases, approach decisions, and a test plan. The human approves the spec before any code is written.

**How it works.** Lead AI executes the spec-creation workflow from the adopting repo's `docs/ai/L1/05_workflows.md`. The workspace draws on the work item, the relevant Progressive Disclosure docs, existing code, and the human. The workflow includes explicit cross-verification steps that consult Verifier AI — for example, having Verifier AI independently restate the acceptance criteria to surface ambiguities. The phase ends when the human signs off the spec.

**Artifact.** `docs/specs/SPEC-NNN-<short-name>.md` — title, status, acceptance criteria, edge cases, approach decisions, test cases, out-of-scope list, verification plan, and notes. See [spec-profile.md](docs/standard/spec-profile.md) for the template and the nine principles a good spec must satisfy.

<details>
<summary>Draft a spec</summary>

Run: `cat prompts/draft-spec.md | claude --dangerously-skip-permissions`

````
Draft a spec for this change using the ai-devkit spec template.

Read the spec profile from the ai-devkit repo:
https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/standard/spec-profile.md

1. Read the relevant source code and docs/ai/ files to understand the
   current state.
2. Create docs/specs/SPEC-NNN-<short-name>.md using the template from the
   spec profile.
3. Fill in: What we're building, Why, Acceptance criteria, Edge cases,
   Approach decisions, Test cases, Verification, Out of scope.
4. Run the spec self-check at the bottom.
5. Summarize the spec and flag anything that needs human decision.
````

> Standalone file: `prompts/draft-spec.md`

</details>

<details>
<summary>Review a spec</summary>

Run: `cat prompts/review-spec.md | claude --dangerously-skip-permissions`

````
Review the spec at docs/specs/SPEC-NNN.md.

Read the spec profile from the ai-devkit repo:
https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/standard/spec-profile.md

1. Read the spec end to end. Confirm it satisfies the nine spec principles.
2. Restate each acceptance criterion in your own words. Flag any that are
   ambiguous.
3. For each acceptance criterion, name the test case(s) that would verify
   it. Flag any criterion with no obvious test case.
4. List edge cases the spec doesn't cover. Propose adding them or marking
   them out-of-scope.
5. Confirm approach decisions are made and rationale is recorded.
6. Append your findings to the Notes section, or list blocking issues if
   the spec isn't ready.
````

> Standalone file: `prompts/review-spec.md`

</details>

## Implementation

**What it is.** Implementation turns an approved spec into a deliverable bundle: code, tests, updated Progressive Disclosure docs, and the structured commit message. The human is available on demand for clarifications but is not in the inner loop.

**How it works.** Lead AI executes the implementation workflow from the adopting repo's `docs/ai/L1/05_workflows.md`. The workspace draws on the spec, the existing code, Progressive Disclosure docs, the testing tools, the human (on demand), and Verifier AI. The workflow runs Red, Green, Refactor for the test-driven development discipline and then Progressive Disclosure docs verification, with cross-verification steps that involve Verifier AI at key transitions. For test-driven development specifically, the workflow specifies a handoff: one model writes the failing tests, a second model from an independent training lineage implements — preserving test-author and implementer separation.

Once implementation is complete, the affected Progressive Disclosure docs are updated to reflect the new reality and the spec is archived to `docs/specs/archive/`. Archived specs are not part of the agent operating surface — Progressive Disclosure docs carry everything an agent needs going forward. The archive exists for human audits and retrospectives.

**Artifact.** Test files, code changes, updated Progressive Disclosure docs, and a structured commit message. See [spec-profile.md](docs/standard/spec-profile.md) for the canonical workflows.

<details>
<summary>Run a test-driven development cycle</summary>

Run: `cat prompts/run-tdd.md | claude --dangerously-skip-permissions`

````
Implement the spec at docs/specs/SPEC-NNN.md using test-driven development.

Read the spec profile from the ai-devkit repo:
https://github.com/AgoraIO-Community/ai-devkit/blob/main/docs/standard/spec-profile.md

1. Read the spec. Read docs/ai/L1/07_gotchas.md and
   docs/ai/L1/04_conventions.md before writing any code.
2. Red: Write the failing tests, one per acceptance criterion and edge
   case. Run the test suite to confirm they fail for the right reason.
3. Green: Write the minimum code to make the tests pass. No premature
   abstraction, no scope expansion beyond what the spec requires.
4. Refactor: Improve naming, remove duplication, check against
   04_conventions.md. Tests must stay green.
5. Update the spec's test case status column as you go
   (TODO → Red → Green → Refactored).
6. Use normal conventional commits. Add a Spec: SPEC-NNN trailer.
````

> Standalone file: `prompts/run-tdd.md`

</details>

## Release

**What it is.** The verification gate before deploy. Release is the human's second checkpoint — after spec approval at the front.

**How it works.** The deliverable bundle is pushed to a release branch where continuous integration runs the full verification suite: tests, lints, doc-freshness checks against the eight level one files, and spec-to-test traceability checks. The release mechanism downstream of continuous integration is system-dependent and outside AI DevKit's scope — teams can auto-promote on green, route through human review, or use any other release model they prefer.

**Artifact.** The release branch, continuous integration workflow, merge record back to the spec via the structured commit message convention (see [spec-profile.md](docs/standard/spec-profile.md#commit-and-pr-convention)), and the archived spec.

## AI Dev Environment

**What it is.** One workspace where the AI can run the whole system end to end. When a system spans multiple repos — an API, an SDK, a frontend, shared infrastructure — the Lead AI needs to run, stop, and test everything from a single place.

**How it works.** It's a container of containers. The outer container is the workspace. Inside it, each component runs in its own container, managed by docker-compose. Infrastructure dependencies (databases, caches, message queues) also run as containers. The Lead AI can start, stop, restart, and test any component without leaving the workspace.

The whole thing runs locally or in the cloud. Cloud workspaces are useful for team handoff — another engineer picks up the same workspace and the same agent context. The environment includes built-in tooling: Playwright for browser testing, Terraform for infrastructure provisioning. All agent sessions are audited — giving you reproducibility, traceability, and evals for debugging agent behaviour.

The system repo contains a system card (`docs/ai/SYSTEM.md`) that lists which repos belong to the system, how they connect, and what contracts they share. Component repos are cloned into a `components/` directory inside the dev environment. Changes to component code are reflected immediately via volume mounts.

**Artifact.** A system repo with `System Role: system` in the level zero card, `SYSTEM.md` alongside it, docker-compose config, devcontainer config, and setup/start/stop/test scripts. See [system-profile.md](docs/standard/system-profile.md) for the full profile.

## Progressive Disclosure docs

**What it is.** Progressive Disclosure docs give every repository a consistent operating surface for AI agents. They are read at the start of every phase to orient Lead AI, and updated at the end of every cycle to reflect the new reality. They are the substrate the lifecycle runs on, and the place where each adopting repo's localised workflow templates live.

**How it works.** Each repository has three tiers:

- **Level zero** — a 300–500 token identity card (`docs/ai/L0_repo_card.md`)
- **Level one** — eight fixed structured summary files in `docs/ai/L1/`
- **Level two** — on-demand deep dives under `docs/ai/L1/L2/`

The eight level one files are the minimum complete operating surface for an AI agent:

| File              | Agent question it answers              |
| ----------------- | -------------------------------------- |
| `01_setup`        | How do I run this?                     |
| `02_architecture` | How is this shaped?                    |
| `03_code_map`     | Where do I edit?                       |
| `04_conventions`  | How do we write code here?             |
| `05_workflows`    | How do I perform this task?            |
| `06_interfaces`   | What contracts must I preserve?        |
| `07_gotchas`      | What will break if I touch it naively? |
| `08_security`     | What trust boundaries must I respect?  |

These eight categories define the minimum complete operating surface an AI agent needs to work safely in any repository. They cover orientation, local engineering practice, contracts, tribal knowledge, and security boundaries. The set is deliberately fixed so agents, tooling, prompts, and reviewers can rely on a consistent structure across an organisation, while repo-specific depth is handled through level two.

**Workflows are part of Progressive Disclosure docs.** Each adopting repo's `05_workflows.md` carries the spec-creation, implementation, and Progressive Disclosure docs verification workflows — materialised from ai-devkit's canonical templates at bootstrap, with repo-specific tooling filled in. This is what Lead AI executes during Plan and Implementation.

**Artifact.** `AGENTS.md` at the repo root, `docs/ai/L0_repo_card.md`, and the eight level one files. Optional `docs/ai/RECIPE.md` for reusable starter repos. See [progressive-disclosure-standard.md](docs/standard/progressive-disclosure-standard.md) for the full standard.

<details>
<summary>Create docs</summary>

Paste this into any AI agent session.

Run: `cat prompts/create-docs.md | claude --dangerously-skip-permissions`

````
Your task is to add progressive disclosure documentation and git conventions
to this repository.

Before starting:

1. Confirm you are inside the target repo's checked-out folder.
2. Ask whether to work on the current branch or create a new one.

Read these files from the ai-devkit repo
(https://github.com/AgoraIO-Community/ai-devkit.git):

1. docs/workflows/progressive-disclosure-docs.md#generate — the generation workflow
2. docs/workflows/progressive-disclosure-docs.md#test — the test workflow
3. docs/standard/progressive-disclosure-standard.md — the full standard

Deliverables:

1. Add AGENTS.md at the repo root using the expanded template from section 4.7
   of the progressive disclosure standard.
2. Generate progressive disclosure docs under docs/ai/.
3. Preserve and integrate with existing repo docs — don't overwrite them.
4. If CLAUDE.md already exists, add a reference to AGENTS.md using that file's
   existing conventions — don't replace content.
5. Apply these git conventions:
   - conventional commits
   - branch naming: type/short-description
   - no AI tool names in commit messages

Requirements:

- Read the whole repo, not just top-level files. Delegate large modules when
  the tool supports it.
- Read existing markdown, config, and CI files for project context.
- Use the real structure and terminology of the repo — no generic filler.
- Do not invent subsystems or workflows that aren't present yet.
- AGENTS.md must include How to Load, Git Conventions, and Doc Commands.
- Generate level zero, level one, and level two docs according to the standard. Add level two docs only
  where deeper detail is justified.
- After generating, run the test workflow. Fix failures and retest until all
  pass. Test results are saved to docs/ai/test-results.md.

When finished:

1. Summarize what you added.
2. Call out any assumptions, gaps, or ambiguous areas.
3. Commit with: docs: add progressive disclosure documentation
4. Push and create a PR.
````

> Standalone file: `prompts/create-docs.md`

</details>

<details>
<summary>Review docs</summary>

After docs are generated, use a second agent session to review quality.
This prompt is read-only — it reports findings without changing files.

Run: `cat prompts/review-docs.md | claude --dangerously-skip-permissions`

````
Review this repo's progressive disclosure docs and provide feedback only.
Do not change files.

Read these files from the ai-devkit repo
(https://github.com/AgoraIO-Community/ai-devkit.git):

1. docs/workflows/progressive-disclosure-docs.md#test — the test workflow
2. docs/standard/progressive-disclosure-standard.md — the full standard

Do this:

1. Read docs/ai/test-results.md.
2. Read the full docs/ai/ tree.
3. Compare the docs to the real codebase.
4. Use git log --oneline -30 to propose 3-5 additional test questions
   based on real recent changes.
5. Read 2-3 complex or under-documented source files and assess whether
   the docs cover them well.
6. Report gaps, inaccuracies, weak test coverage, and recommended new
   test cases.

Do not edit docs, do not update test-results.md, and do not commit.
````

> Standalone file: `prompts/review-docs.md`

</details>

<details>
<summary>Fix review findings</summary>

After a review produces findings, use this prompt to close them. Each
finding is traced to source code and patched at the correct disclosure
level.

Run: `cat prompts/fix-review-findings.md | claude --dangerously-skip-permissions`

````
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
````

> Standalone file: `prompts/fix-review-findings.md`

Do not use the generate or review prompts to close findings — they are not
finding-driven.

</details>

<details>
<summary>Multi-agent review with Codex</summary>

Use one agent as the orchestrator and Codex CLI as an independent reviewer.
This catches issues that a single model misses since different training
lineages have different blind spots.

Requires: [Codex CLI](https://github.com/openai/codex) installed and on PATH.

The canonical workflow doc is [docs/workflows/progressive-disclosure-docs.md](docs/workflows/progressive-disclosure-docs.md#review-with-codex).

Run: `cat prompts/review-with-codex.md | claude --dangerously-skip-permissions`

````
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
````

> Standalone file: `prompts/review-with-codex.md`

**Batch across repos.** Run from a parent directory containing cloned repos.
The orchestrator generates docs for each repo on a
`docs/progressive-disclosure` branch, runs the review cycle, and pushes each
branch when done.

</details>

<details>
<summary>Generate and review docs (all-in-one)</summary>

A combined prompt that runs the full pipeline: generate docs, self-test,
Codex review, fix findings, and verify — in a single session.

Run: `cat prompts/generate-and-review-docs.md | claude --dangerously-skip-permissions`

> Standalone file: `prompts/generate-and-review-docs.md`

</details>

## Getting started

Three adoption levels, each moving further along the AI-centric axis.

**Just legibility (still AI-assisted).** Add `AGENTS.md` and `docs/ai/` to a single repo using the Create docs prompt above. Agents can now read the repo; humans still do the engineering.

**Spec-driven development (partially AI-centric).** Add `docs/specs/` and adopt the spec template for new work. Pair an AI agent with the test-driven development discipline.

**Full multi-model flow (fully AI-centric).** Configure two model providers, adopt the Plan → Implementation → Release cycle with cross-verification at every phase, route a release branch through doc-freshness verification. This is the diagram's operating model.

## Setting up slash commands and skills

The prompts above work as copy-paste in any agent session. If your tool
supports custom commands, you can wrap them for faster access:

- **Claude Code** — add prompts as custom slash commands via
  `claude-code-commands/` or as skills
- **Cursor** — add as `.cursor/commands/` or rules
- **Codex** — use `codex exec` with the prompt as the argument

The content is identical regardless of the wrapper. The prompts are the
source of truth; tool-specific configuration is just a convenience layer.

## Profiles

**Recipe profile.** Use [docs/standard/recipe-profile.md](docs/standard/recipe-profile.md)
when a repo is a reusable starter that should publish extension points and
support child verticals. The profile is optional — repos without
`Recipe Role` in the level zero card are unaffected. See [examples/recipe-base](examples/recipe-base/README.md) and
[examples/recipe-vertical](examples/recipe-vertical/README.md) for
structural fixtures.

**System profile.** Use [docs/standard/system-profile.md](docs/standard/system-profile.md)
when a repo describes a multi-component system and provides a containerised
dev environment. The profile is optional — repos without `System Role` in
the level zero card are unaffected.

## Compatibility

Compatibility is capability-based, not absolute. Any tool that reads repo
files can consume `AGENTS.md` and `docs/ai/`.

- **Claude Code** — tested; plain markdown plus multi-agent review
- **Cursor** — tested; plain markdown consumption
- **Codex** — tested; plain markdown plus CLI reviewer role
- **Gemini** — untested; plain markdown consumption expected to work
- **Other tools** — expected to work if the tool reads repo files

## Repository contents

- `docs/standard/` — the normative Progressive Disclosure docs spec, recipe profile, spec profile, system profile, and agent policy
- `docs/ai/` — this repo applied to itself (a working example of a standards repo's Progressive Disclosure docs)
- `docs/img/` — diagrams (AI Software Development Lifecycle flow)
- `examples/` — fixture repos showing Progressive Disclosure docs, recipes, and the full lifecycle
- `docs/workflows/` — canonical Progressive Disclosure docs workflows (generate, update, test, fix, review)
- `docs/guides/` — supplementary guides
- `scripts/` — freshness checks, validators

## Status

| Layer                                | Status   |
| ------------------------------------ | -------- |
| Progressive Disclosure docs core (level zero/one/two, 8 files) | Stable   |
| Recipe profile (base/vertical)       | Beta     |
| Spec profile                         | Draft    |
| Test-driven development profile      | Draft    |
| Multi-model flow conventions         | Draft    |
| System profile (dev environment)     | Draft    |
| Shared cloud environments            | Planned  |
| Evaluation loop                      | Planned  |
