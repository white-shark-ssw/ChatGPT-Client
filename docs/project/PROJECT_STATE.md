# Project State

_Last updated: 2026-08-25._

## Current accepted baseline

Repository governance baseline: `main@bf71cb1152c2b114559af0ae1d74384566cc2a64`.

The product goal is explicitly defined by the user as development of an **iOS native ChatGPT client**. Distribution is intended as an IPA installed through TrollStore. The target user-device environment does not exceed iOS 17.0, while compatibility with lower iOS versions is preferred where practical.

No application/product source baseline has been added yet, so implementation details and the exact minimum deployment target must still be established from future source, toolchain/API requirements, and runtime evidence.

## Current development candidates

None recorded.

There are no active Development/Feature checkpoints under `docs/project/current/dev/`.

## Current architecture

Product architecture is not implemented yet.

Current accepted architecture-level direction is only that the product is an iOS native client. Historical material recommends native conversation/navigation/message/composer state and treating Web technology, if used at all, as a possible authentication bootstrap rather than a chat runtime, but those implementation details remain reference guidance until adopted by a current development task.

Governance architecture: root `AGENTS.md` → `docs/project/START_HERE.md` → session router/checkpoints and durable project-state documents under `docs/project/`.

## Current development direction

Build the new product from an iOS-native baseline rather than converting the previous WebView client into the new source baseline.

Compatibility direction:

- produce/install an IPA through TrollStore;
- do not require iOS newer than 17.0 for the intended environment;
- when the Xcode project and feature/API requirements are known, choose the lowest practical deployment target that can be built and validated reliably;
- do not confuse the iOS 17.0 environment ceiling with the minimum deployment target.

The user-provided previous-project history pack is available as experience/reference. Its old WebView implementation, endpoint names, diagnoses, framework suggestions, and MVP plan must not be treated as current implementation facts or current ChatGPT protocol contracts. See `HISTORICAL_REFERENCE.md`.

## Known issues / constraints

- Product language/framework, dependency, Xcode project structure, build/test, CI, version/build, exact minimum deployment target, signing/packaging pipeline, and module ownership are not yet verified.
- ChatGPT private/internal protocol details can change and must be established from current evidence before implementation.
- New libraries/framework choices must not silently raise the required OS above the accepted compatibility envelope.
- Historical WebView performance/lifecycle problems are useful design warnings, not proof of present native-client behavior.
- These fields must be refreshed automatically when real product files, protocol evidence, tests, artifacts, or runtime results are added.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Historical experience is lower authority than the user's latest requirement, current source, and current runtime/protocol evidence.
