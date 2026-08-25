# Project State

_Last updated: 2026-08-25._

## Current accepted baseline

Repository governance baseline: `main@f4ba767fde90c0258da19a92283e9f337532ca35`.

The product goal is now explicitly defined by the user as development of an **iOS native ChatGPT client**. No application/product source baseline has been added yet, so implementation details must still be established from future source and current protocol/runtime evidence.

## Current development candidates

None recorded.

There are no active Development/Feature checkpoints under `docs/project/current/dev/`.

## Current architecture

Product architecture is not implemented yet.

Current accepted architecture-level direction is only that the product is an iOS native client. Historical material recommends native conversation/navigation/message/composer state and treating Web technology, if used at all, as a possible authentication bootstrap rather than a chat runtime, but those implementation details remain reference guidance until adopted by a current development task.

Governance architecture: root `AGENTS.md` → `docs/project/START_HERE.md` → session router/checkpoints and durable project-state documents under `docs/project/`.

## Current development direction

Build the new product from an iOS-native baseline rather than converting the previous WebView client into the new source baseline.

The user-provided previous-project history pack is available as experience/reference. Its old WebView implementation, endpoint names, diagnoses, framework suggestions, and MVP plan must not be treated as current implementation facts or current ChatGPT protocol contracts. See `HISTORICAL_REFERENCE.md`.

## Known issues / constraints

- Product language/framework, dependency, Xcode project structure, build/test, CI, version/build, exact deployment target, distribution, and module ownership are not yet verified.
- ChatGPT private/internal protocol details can change and must be established from current evidence before implementation.
- Historical WebView performance/lifecycle problems are useful design warnings, not proof of present native-client behavior.
- These fields must be refreshed automatically when real product files, protocol evidence, tests, artifacts, or runtime results are added.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Historical experience is lower authority than the user's latest requirement, current source, and current runtime/protocol evidence.
