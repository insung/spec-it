---
id: ADR-0001
title: <API contract decision>
status: proposed
date: "<YYYY-MM-DD>"
owners:
  - intent-owner
  - architecture-owner
rules:
  - ARCH-006
  - API-001
  - API-002
  - API-003
  - API-004
  - API-005
review_triggers: []
---

# Contract scope

- Capability and intended outcome: <why this API exists>
- Protocol and payload: <HTTP JSON, protobuf RPC, WebSocket plus payload>
- Canonical contract: <OpenAPI, .proto, schema, or approved code-first path>
- Version and compatibility: <current version and consumer migration>
- Audience / network / authn / authz: <record separately>
- Data classification and tenant boundary: <classification and ownership>

# Resource and operation classification

| Operation | Resource/query/command/aggregate/job | Canonical path or method | Idempotency and concurrency | Owner |
| --- | --- | --- | --- | --- |
| <operation> | <classification> | <contract reference> | <behavior> | <owner> |

# Boundary mapping

| Transport type | Application command/query/result | Mapper owner | Transport validation | Domain validation |
| --- | --- | --- | --- | --- |
| <request/response> | <application type> | <adapter> | <format> | <invariant> |

# Documentation and lifecycle

- Documentation projection and renderer: <public/internal projection; Scalar if selected>
- Try-it environment and credential policy: <disabled or sandbox>
- Support state and LTS decision: <state, duration, cost owner>
- Deprecation, replacement, notice, and retirement evidence: <references>

# Verification

- Provider contract tests: <reference>
- Consumer compatibility tests: <reference>
- Authorization and tenant-negative tests: <reference>
- Integration environment and evidence: <reference>
- Open decisions: <must be empty before convergence for material behavior>
