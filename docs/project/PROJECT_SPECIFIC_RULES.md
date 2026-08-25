# Project-Specific Rules

This file contains rules specific to this repository/product. Do not copy assumptions from another project into this file.

Populate/change these rules only from explicit user requirements, verified product/runtime constraints, real source architecture, accepted test results, confirmed compatibility/deployment requirements, or durable technical decisions.

## Product contracts

- The current product goal is an **iOS native ChatGPT client**.
- The previous-project history pack is reference material only. It is not current product source, current protocol documentation, or proof that a historical implementation should be reused.

## Repository governance contract

- The repository uses the AI Governance Rules as the dynamic authority for AI-assisted work.
- Every new work session must read root `AGENTS.md` first and then `docs/project/START_HERE.md` before substantive work.
- When repository evidence changes materially, the corresponding checkpoint and durable `docs/project/` records must be refreshed in the same work cycle.

## Protocol evidence contract

- Do not implement ChatGPT private/internal Web API behavior from historical endpoint names, old request shapes, or memory alone.
- Before implementing a protocol capability, establish current evidence for the relevant URL/path, method, authentication/account context, headers, request body, response/stream shape, IDs/state semantics, and failure behavior as applicable.
- If current evidence contradicts historical notes, current evidence wins and durable docs must be corrected.

## Compatibility / deployment constraints

- Platform direction: iOS native application.
- Distribution/install form: IPA installed through TrollStore.
- Intended user-device OS versions do not exceed iOS 17.0. Do not introduce a required API, dependency, framework setting, or deployment configuration that makes iOS > 17.0 mandatory unless the user explicitly changes this requirement.
- iOS 17.0 is an environment ceiling, **not** the minimum deployment target.
- Prefer the lowest practical minimum deployment target compatible with the real required features/APIs/dependencies and validated runtime behavior.
- Until an Xcode project and concrete dependencies exist, the exact minimum deployment target remains `Unknown / Unverified`; do not guess a numeric floor.
- Exact iPhone/iPad device-family support remains Unknown / Unverified.

## Critical invariants

- Historical WebView code must not become the new source baseline merely because it existed in the previous project.
- Any future WebView use, including login/bootstrap use, must be justified by the current task and current evidence; no chat-WebView architecture is inherited automatically.
- A future build/config change that raises the minimum supported iOS version must be treated as a compatibility change and justified against this project's “lower is better” requirement.

## Frozen business or architecture rules

None recorded yet.

## Code style / naming constraints

Follow existing repository style until explicit project-specific constraints are verified.

## Prohibited routes / known dangerous regressions

- Do not revive old WebView compensation mechanisms such as speculative timers, watchdogs, DOM scans, Shadow WebView recovery, or fallback chains without a current concrete failure mode and evidence.
- Do not use UI text or title matching as a substitute for a verified conversation identity/state owner when the native implementation is introduced.
- Do not select iOS 17.0 as the deployment target merely because the user's highest target OS is iOS 17.0.

## Historical reference

See `docs/project/HISTORICAL_REFERENCE.md` for distilled previous-project lessons. That document is advisory evidence, not a current implementation contract.

## Rule maintenance

Rules work may update this file proactively when a durable project-specific constraint is confirmed. Never turn a temporary hypothesis or historical suggestion into a permanent current rule.
