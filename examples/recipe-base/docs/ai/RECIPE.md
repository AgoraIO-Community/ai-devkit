---
recipe_version: 1.0.0
recipe_status: stable
extension_points:
  - id: ui.pages
    name: page layer
invariants:
  - id: contracts.env
    summary: required env vars stay stable
stable_contracts:
  - id: api.client
    summary: client interface remains compatible
---

# RECIPE

## Extension Points

- `ui.pages`

## Invariants

- `contracts.env`

## Stable Contracts

- `api.client`

## Internal / Subject to Change

- implementation details
