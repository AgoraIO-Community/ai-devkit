# System Profile for Progressive Disclosure Docs

This document defines the optional system profile for repos that describe
and orchestrate a multi-component system spanning multiple repositories.

## Opt-In Principle

- The system profile is additive and optional.
- Repos without `System Role` in L0 remain ordinary PD repos.
- The base L0/L1/L2 model, 8-file structure, and `AGENTS.md` template
  remain valid for non-system repos.
- Component repos that belong to a system are ordinary PD repos. They do
  not need to know they are part of a system — the system repo knows.

## What a System Repo Is

A system repo does not contain application code. It describes a system
made up of component repos and provides the means to run, test, and
develop against the full system locally.

It answers two questions:

1. **What is this system?** — which repos, how they connect, what
   contracts they share.
2. **How do I run it?** — a containerised dev environment that Model A
   can start, stop, and test without leaving the system repo.

## L0 Fields

These fields are optional and only apply when a repo opts into the system
profile.

| Field           | Meaning                                              |
| --------------- | ---------------------------------------------------- |
| `System Role`   | `system` — this repo describes a multi-component system |
| `System Name`   | human-readable name for the system                   |
| `Components`    | count of component repos                             |

## System Card: `docs/ai/SYSTEM.md`

System repos publish `docs/ai/SYSTEM.md` as a sibling to
`L0_repo_card.md`. This is the system-level equivalent of a repo's L0
card — which repos exist, what they do, how they connect.

```markdown
# [System Name] — System Card

> [One-line description of the system]

## Component Registry

| Repo             | Role           | Language   | Description                 |
| ---------------- | -------------- | ---------- | --------------------------- |
| `org/user-api`   | api-service    | TypeScript | User management REST API    |
| `org/user-sdk`   | sdk-library    | TypeScript | TypeScript SDK for User API |
| `org/web-app`    | frontend-app   | TypeScript | Customer-facing web app     |

## Dependency Map

user-api (provider) → user-sdk (consumer) → web-app (consumer)

## Shared Conventions

| Convention     | Value                          |
| -------------- | ------------------------------ |
| API versioning | URL path prefix (`/v1/`)       |
| Auth mechanism | JWT                            |
| Error format   | `{ error: { code, message } }` |

## Cross-Component Contracts

List the interface contracts that span component boundaries. Each
contract names the provider, the consumer, and the verification
mechanism.

- `user-api` provides `/v1/users` → `user-sdk` consumes via generated
  client. Verified by contract tests in both repos.
- `user-sdk` exports `getUser(id)` → `web-app` consumes. Verified by
  type-checking against published types.
```

The component registry can be populated by reading L0 cards from each
component repo. The rest is maintained in the system repo.

## Dev Environment

The system repo provides a containerised dev environment that runs the
full system locally. The environment is defined in the system repo and
clones or mounts component repos at startup.

### Architecture: Containers Within a Container

The dev environment uses a two-level container architecture:

```
┌─────────────────────────────────────────────────┐
│  Outer container (dev environment)              │
│  - System repo mounted                         │
│  - Docker daemon running (DinD or socket mount) │
│  - Model A works here                          │
│                                                 │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐     │
│  │ user-api  │ │ user-sdk  │ │ web-app   │     │
│  │ container │ │ container │ │ container │     │
│  └───────────┘ └───────────┘ └───────────┘     │
│                                                 │
│  ┌───────────┐ ┌───────────┐                    │
│  │ postgres  │ │ redis     │                    │
│  │ container │ │ container │                    │
│  └───────────┘ └───────────┘                    │
└─────────────────────────────────────────────────┘
```

The outer container is the dev environment — this is where Model A
operates. Inside it, each component runs in its own container, managed
by docker-compose or an equivalent orchestrator. Infrastructure
dependencies (databases, caches, message queues) also run as containers.

Model A can start, stop, restart, and test any component from within the
outer container. It has full control over the system without affecting
the host.

### Dev Environment Configuration

The system repo contains the environment definition at its root:

| File                    | Purpose                                        |
| ----------------------- | ---------------------------------------------- |
| `docker-compose.yml`    | defines all component and infra containers     |
| `.devcontainer/`        | devcontainer config for the outer environment  |
| `scripts/setup`         | clones component repos, installs dependencies  |
| `scripts/start`         | starts the full system                         |
| `scripts/stop`          | stops all containers                           |
| `scripts/test`          | runs cross-component and integration tests     |
| `scripts/test-component`| runs tests for a single named component        |

### Agent Commands

Model A uses these commands from within the dev environment:

```
scripts/setup              # first-time setup: clone repos, build images
scripts/start              # start all components
scripts/stop               # stop all components
scripts/test               # run cross-component tests
scripts/test-component api # run tests for a single component
docker-compose logs api    # tail logs for a component
docker-compose restart api # restart a single component
```

These are shell scripts, not agent-specific tooling. Any agent that can
run shell commands can use them.

### Component Repo Mounting

Component repos are cloned into a `components/` directory inside the dev
environment. Changes made by Model A to component code are reflected
immediately in the running containers via volume mounts.

```
system-repo/
├── components/
│   ├── user-api/        # cloned from org/user-api
│   ├── user-sdk/        # cloned from org/user-sdk
│   └── web-app/         # cloned from org/web-app
├── docker-compose.yml
├── .devcontainer/
├── scripts/
├── docs/
│   └── ai/
│       ├── L0_repo_card.md
│       ├── SYSTEM.md
│       └── L1/
└── AGENTS.md
```

Model A can edit code in any component, restart that component's
container, and run tests — all without leaving the dev environment.

## Cross-Component Workflows

When a change spans multiple components, Model A works in the system
repo's dev environment:

1. Read `SYSTEM.md` to understand which components are affected.
2. Start the dev environment if not already running.
3. For each affected component, follow the normal Plan → Implementation
   cycle within that component's code (under `components/`).
4. Run `scripts/test` to verify cross-component contracts.
5. Push changes from each component directory to its own repo.

The system repo's `05_workflows.md` carries the cross-component workflow
templates, materialised from ai-devkit's canonical templates at
bootstrap.

## AGENTS Loading Additions

When `System Role` is absent, use the normal PD loading protocol.

When `System Role: system`:

1. Load `docs/ai/L0_repo_card.md`
2. Load `docs/ai/SYSTEM.md` — the system card
3. Load all 8 local L1 files
4. For each component in the registry, read its L0 card to understand
   what it does
5. Follow component L1/L2 links only when working on that component's
   code

## Validation Expectations

- The component registry must list repos that exist and are accessible
- Each component in the registry should have PD docs (L0 at minimum)
- `scripts/start` must bring up all components to a testable state
- `scripts/test` must run cross-component verification
- The dependency map must match the actual contract relationships
- Changes to component code should be committed to the component repo,
  not the system repo

## Fixtures

- [system-example](../../examples/system-example/README.md) — a fixture
  showing a system repo with three components and a containerised dev
  environment (planned).
