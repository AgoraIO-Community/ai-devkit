# Spec & TDD Profile for Progressive Disclosure Docs

This document defines the optional spec and TDD profile for repos that adopt
a spec-first, test-driven workflow for AI-centric development. It supplies
the canonical workflow templates used during the Plan and Implementation
phases of the AI SDLC.

## Opt-In Principle

- The profile is additive and optional.
- Repos without `docs/specs/` remain ordinary PD repos.
- The base L0/L1/L2 model, 8-file structure, and `AGENTS.md` template remain
  valid for non-adopters.
- The profile defines artifact shapes and workflow templates. It does not
  mandate a specific tool — specs can be produced by Spec Kit, Superpowers,
  spec-first-tdd, or hand-authored.

## Scope

The profile covers four concerns:

1. The artifact shape for in-flight specs.
2. The lifecycle for specs from draft through archive.
3. Three canonical AI engineering workflows that are materialised into each
   adopting repo's `docs/ai/L1/05_workflows.md` at PD docs bootstrap.
4. The commit message convention that bridges specs to git history.

The workflows defined here are what Model A executes during the **Plan**
phase (spec creation and review) and the **Implementation** phase (TDD and
PD docs verification) of the AI SDLC. Cross-verification by a second model
from an independent training lineage is encoded as explicit steps within
each workflow.

## Lifecycle Overview

Specs move through four states. Location changes when the state changes.

| Status      | Location                                          |
| ----------- | ------------------------------------------------- |
| Draft       | `docs/specs/SPEC-NNN-<short-name>.md`             |
| In Progress | `docs/specs/SPEC-NNN-<short-name>.md`             |
| Done        | `docs/specs/SPEC-NNN-<short-name>.md` (briefly)   |
| Archived    | `docs/specs/archive/<YYYY-QN>/SPEC-NNN-<...>.md`  |

The top-level `docs/specs/` directory holds only in-flight specs. Completed
specs move to `docs/specs/archive/<YYYY-QN>/` after PD docs are updated.
Archived specs are for humans, audits, and retrospective evaluation. They
are **not** part of the agent operating surface.

## What Makes a Good Spec

A spec is the durable record of what is being built. To be useful in an
AI-centric flow, a spec must satisfy these nine principles:

1. **Executable** — every acceptance criterion maps to a runnable check,
   named in the spec.
2. **Reviewable in under 5 minutes** — a mid-level engineer who has not
   seen the change should be able to review the whole spec quickly.
3. **Granular at the right level** — under-descriptive specs create
   unpredictable execution paths; over-descriptive specs are never read
   by humans.
4. **Explicit about edge cases** — edge cases live in their own section,
   not buried inside the happy path.
5. **Decided, not deferred** — when multiple implementation approaches are
   reasonable, the spec names them and picks one with a reason. Approach
   decisions are made in the spec, not in implementation.
6. **Bounded by what it isn't** — an explicit out-of-scope list prevents
   the AI from "helpfully" doing more than asked.
7. **Traceable end-to-end** — every acceptance criterion maps to at least
   one test case; every test case traces back to a criterion. No orphans
   on either side.
8. **Closed-loop verifiable** — the spec names the verification mechanism
   (unit, integration, e2e) and the specific tooling.
9. **Durable** — once approved, changes are appended as timestamped notes,
   not edited in place.

## Spec Template

```markdown
# SPEC-NNN: [One-line title]

> **Status:** Draft | In Progress | Done | Archived
> **Owner:** [name or team]
> **Created:** YYYY-MM-DD
> **Related PD:** [links to relevant docs/ai/ files]

## What we're building

[2–4 plain-language sentences. Describe the change as a user-visible
behaviour, not an implementation.]

## Why

[1–2 sentences. The problem this solves. Skip if obvious from context.]

## Acceptance criteria

Verifiable behaviours the change must exhibit. Each must map to at least
one test case below.

- AC-1: Given [state], when [action], then [outcome]
- AC-2: ...

## Edge cases

Behaviours at the boundaries. Each maps to a test case or is explicitly
out of scope.

- EC-1: ...
- EC-2: ...

## Design decisions

When multiple reasonable implementations exist, name them and pick one.

- Decision: [chosen approach]
  - Alternatives considered: [other options]
  - Rationale: [why this one]

## Test cases

| ID    | Type        | Description | Maps to | Status |
| ----- | ----------- | ----------- | ------- | ------ |
| TC-1  | unit        | ...         | AC-1    | TODO   |
| TC-2  | integration | ...         | AC-2    | TODO   |

Status values: TODO → Red → Green → Refactored.

## Verification

- Mechanism: [unit / integration / e2e]
- Tooling: [pytest / Playwright / agent-browser / etc.]
- Rationale: [why this level is appropriate for this change]

## Out of scope

[What this spec deliberately doesn't cover. 2–4 explicit exclusions.]

## Notes

[Decisions made during the build, surprises, deferred items. Appended
with timestamps. This is what makes the spec airtight retroactively.]

## Spec self-check

- [ ] Every acceptance criterion is executable
- [ ] Spec is reviewable in under 5 minutes
- [ ] Granularity is appropriate (not under, not over)
- [ ] Edge cases have their own section
- [ ] Design decisions are made, not deferred
- [ ] Out-of-scope list is present
- [ ] Every AC maps to a test case and vice versa
- [ ] Verification mechanism is named
- [ ] Changes will be appended as notes, not edited in place
```

## Worked Example

```markdown
# SPEC-001: Refresh access tokens before expiry

> **Status:** In Progress
> **Owner:** Auth squad
> **Created:** 2026-05-27
> **Related PD:** [08_security](../ai/L1/08_security.md),
> [06_interfaces](../ai/L1/06_interfaces.md),
> [07_gotchas](../ai/L1/07_gotchas.md)

## What we're building

The API client refreshes access tokens automatically when they are within
60 seconds of expiry. The refresh happens before the next outbound request,
is not triggered for tokens still comfortably valid, and surfaces a single
typed error if the refresh itself fails.

## Why

Users hit sporadic 401s on long-running sessions because we only refresh
on receiving a 401, which races with in-flight requests. Refreshing
proactively eliminates the race.

## Acceptance criteria

- AC-1: Given a token expiring in <60s, when any client method is called,
  then a refresh is performed before the original request.
- AC-2: Given a token expiring in >60s, when any client method is called,
  then no refresh is performed.
- AC-3: Given a refresh failure, when a refresh is attempted, then the
  client raises `TokenRefreshError` with the original cause attached.
- AC-4: Given two concurrent calls both triggering refresh, then only one
  refresh request is sent to the auth server.

## Edge cases

- EC-1: Token already expired (not within window — already expired). Treat
  as immediate refresh.
- EC-2: System clock skew >60s. Out of scope; document as known limitation.
- EC-3: Refresh succeeds but new token is also expired. Raise
  `TokenRefreshError`; do not retry.

## Design decisions

- Decision: Refresh on demand at request time, not via background timer.
  - Alternatives considered: Background timer that refreshes proactively
    independent of request flow.
  - Rationale: Refresh-on-demand is simpler, has no clock dependency, and
    the 60s window is generous enough that latency impact is negligible.

## Test cases

| ID    | Type        | Description                                       | Maps to | Status |
| ----- | ----------- | ------------------------------------------------- | ------- | ------ |
| TC-1  | unit        | Token expiring in 30s triggers refresh            | AC-1    | Green  |
| TC-2  | unit        | Token expiring in 5min does not trigger refresh   | AC-2    | Green  |
| TC-3  | unit        | Refresh 500 raises TokenRefreshError              | AC-3    | Red    |
| TC-4  | unit        | Refresh timeout raises TokenRefreshError          | AC-3    | TODO   |
| TC-5  | integration | Two concurrent calls share one refresh request    | AC-4    | TODO   |
| TC-6  | unit        | Already-expired token triggers immediate refresh  | EC-1    | TODO   |
| TC-7  | unit        | Refresh returning expired token raises            | EC-3    | TODO   |

## Verification

- Mechanism: unit + one integration test for the concurrency case
- Tooling: pytest with `httpx_mock` for unit; pytest with real auth server
  fixture for integration
- Rationale: Token logic is pure enough for unit coverage; the dedup case
  requires real concurrent timing.

## Out of scope

- Refresh token rotation (separate concern, will be SPEC-002)
- Background refresh on idle (deliberately deferred — see approach decision)
- Caching the refreshed token across processes (single-process scope)

## Notes

- 2026-05-27: Decided against background timer. See approach decision.
- 2026-05-28: Confirmed auth server already deduplicates by refresh token,
  but client-side dedup still wanted to avoid wasted requests. See
  [07_gotchas: refresh stampede](../ai/L1/07_gotchas.md#refresh-stampede).

## Spec self-check

- [x] Every acceptance criterion is executable
- [x] Spec is reviewable in under 5 minutes
- [x] Granularity is appropriate
- [x] Edge cases have their own section
- [x] Design decisions are made
- [x] Out-of-scope list is present
- [x] Every AC maps to a test case and vice versa
- [x] Verification mechanism is named
- [x] Changes will be appended as notes
```

## Archive Rules

When a spec transitions to `Done` and PD docs have been updated, the spec
is archived. Archive rules:

- **Move, don't copy.** The spec file moves from `docs/specs/` to
  `docs/specs/archive/<YYYY-QN>/`. There is one copy.
- **Read-only after archive.** Archived specs are not edited. If something
  changes about the feature later, that is a new spec.
- **Closing note required.** Before archiving, append a closing note to
  the spec linking to the PD docs commit SHA and naming the affected L1
  files.
- **Not referenced from agent surface.** Archived specs are not linked
  from PD docs, `AGENTS.md`, or any other file an agent reads by default.
  The archive is for humans, audits, and the eval loop — not for
  in-flight context.
- **Archive README.** `docs/specs/archive/README.md` should state:
  *"This directory holds completed specs for human audit and retrospective
  evaluation. It is not part of the agent operating surface. Agents
  working on this repo should rely on PD docs (`docs/ai/`) and git
  history."*

## Commit and PR Convention

Use normal conventional commits as defined in
[agent-policy.md](agent-policy.md) during implementation. Link commits to
specs with a `Spec:` trailer.

### Commits

```
feat: refresh access tokens before expiry

Spec: SPEC-001
```

The `Spec:` trailer is the only addition to the existing commit convention.
All other commit rules (lowercase, present tense, no AI tool names) remain
unchanged.

### PR body or squash commit

The full structured summary belongs in the PR body (or the squash commit
message if the team squashes). In a squash-merge workflow this preserves
the spec's intent in `git log`; in a merge-commit workflow the PR body
is available via `gh pr view` but not `git log`.

```
feat: refresh access tokens before expiry

The API client refreshes access tokens automatically when they are within
60 seconds of expiry. The refresh happens before the next outbound
request, is not triggered for tokens still comfortably valid, and
surfaces a single typed error if the refresh itself fails.

Acceptance criteria:
- Token expiring in <60s triggers refresh before request
- Token expiring in >60s does not trigger refresh
- Refresh failure raises TokenRefreshError with original cause
- Concurrent calls share a single refresh request

PD docs updated: 02_architecture, 06_interfaces, 07_gotchas
Spec: SPEC-001
```

### Archive closing note

The archived spec gets a closing note linking to the merge commit SHA and
naming the affected L1 files. This is the third place the structured
summary appears — PR body, squash commit, and archive note all carry the
same information so it's recoverable from any entry point.

## Canonical AI Engineering Workflows

These three workflows are the canonical templates Model A executes during
the Plan and Implementation phases of the AI SDLC. At PD docs bootstrap,
they are materialised into each adopting repo's `docs/ai/L1/05_workflows.md`
with the repo's specific tooling, paths, and commands filled in.

Each adopting repo's local copy carries a version header so drift against
this canonical source is detectable:

```
<!-- ai-engineering-workflows-version: 1.0.0 -->
```

Cross-verification by a second model from an independent training lineage
is encoded as explicit steps within each workflow, not bolted on around it.
References to "a second model" mean Model B in the SDLC sense — any AI from
a different training lineage than the one executing the workflow.

### Review a spec (Plan phase)

When asked to review a spec at `docs/specs/SPEC-NNN.md`:

1. Read the spec end to end. Confirm it satisfies the nine spec principles
   (see top of this document, or the self-check at the bottom of the spec).
2. Restate each acceptance criterion in your own words. If you cannot
   restate it unambiguously, flag it as under-specified.
3. **Cross-verification:** Ask a second model from an independent training
   lineage to independently restate each acceptance criterion. If your
   restatements diverge, flag the criterion as ambiguous and surface to
   the human for reconciliation.
4. For each acceptance criterion, name the test case(s) that would verify
   it. Flag any criterion with no obvious test case.
5. For each named test case, confirm the verification mechanism (unit,
   integration, e2e) is appropriate and the tooling exists in this repo.
6. List edge cases the spec doesn't cover. Propose adding them or marking
   them out-of-scope explicitly.
7. Confirm that design decisions are made and rationale is recorded.
8. Output: an updated spec with your additions appended in the Notes
   section, or a list of blocking issues if the spec isn't ready.

### Run a TDD cycle (Implementation phase)

When asked to implement a spec at `docs/specs/SPEC-NNN.md`:

1. Read the spec. Read `docs/ai/L1/07_gotchas.md` and
   `docs/ai/L1/04_conventions.md` before writing any code.
2. **Red — test author.** One model writes the failing tests, one per
   acceptance criterion and edge case, using `<repo's test framework>`
   in `<repo's test directory>`. Run `<repo's test command>` to confirm
   they fail for the right reason.
3. **Green — implementer (handoff).** A second model from an independent
   training lineage writes the minimum code to make the tests pass.
   Separating test author from implementer is the discipline that
   prevents implementation assumptions from being silently baked into
   tests. No premature abstraction, no scope expansion beyond what the
   spec requires.
4. **Refactor.** Either model improves naming, removes duplication, and
   checks the result against `docs/ai/L1/04_conventions.md`. Tests must
   stay green.
5. Update the spec's test case status column (TODO → Red → Green →
   Refactored) as you go.
6. Output: tests in `<test directory>`, code changes, and an updated spec.

### Verify PD docs are still accurate (Implementation phase)

When asked to verify or refresh PD docs after a change:

1. List the files changed in this branch.
2. For each L1 file in `docs/ai/L1/`, ask whether the change affects what
   that file documents. Be specific — does it change setup commands? Add
   or remove a module? Introduce a new convention or gotcha? Cross a
   trust boundary?
3. For each L1 file flagged as affected, draft the update. Keep within the
   file's existing structure and token budget.
4. **Cross-verification:** Ask a second model from an independent training
   lineage to review the proposed doc updates against the actual code
   changes. Reconcile any disagreements before proceeding.
5. Update the `Last reviewed` date in the L0 identity card if any L1 file
   changed.
6. Generate the commit message using the structured format from the
   profile (spec title, "what we're building" paragraph, acceptance
   criteria bullets, PD docs updated line).
7. Move the spec from `docs/specs/SPEC-NNN.md` to
   `docs/specs/archive/<YYYY-QN>/SPEC-NNN.md`.
8. Append a closing note to the archived spec linking to the PD docs
   commit SHA and the affected L1 files.
9. Output: a patch updating the affected L1 files and L0, the archived
   spec with its closing note, and the structured commit message.

## Validation Expectations

- Specs must satisfy the nine principles before approval. The self-check
  at the bottom of the spec template makes this enforceable.
- Test cases must trace to acceptance criteria and edge cases. No orphans.
- Archived specs must have a closing note linking to the PD docs commit.
- Each adopting repo's `05_workflows.md` must carry the
  `ai-engineering-workflows-version` header so drift against this
  canonical source is detectable.
- Archived specs must not be referenced from PD docs or any other
  agent-readable surface.
- Cross-verification steps in workflows must consult a model from an
  independent training lineage. Same-model self-review does not satisfy
  the cross-verification requirement.

## Fixtures

- [spec-tdd-example](../../examples/spec-tdd-example/README.md) — a fixture
  repo showing the full Plan → Implementation → Release lifecycle,
  including a worked example spec and the resulting commit message.
