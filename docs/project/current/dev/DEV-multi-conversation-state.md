# DEV-multi-conversation-state

## Status

**Active — b18 Runtime accepted for tested historical-scroll matrix; b19 is measurement-only and exact product source is prepared; no LRU behavior has been chosen or implemented; Stable/Frozen = No**

- Work ID: `DEV-multi-conversation-state`
- Branch: `dev/multi-conversation-state-20260827`
- Target main: `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`
- Last Runtime Candidate: `DEV-multi-conversation-state-0.1.0-b18`
- Reserved Candidate: `DEV-multi-conversation-state-0.1.0-b19` / `0.1.0 (19)` — measurement only

## b19 exact scope

Enrich existing `conversation / resident.*` diagnostics with current-process task VM memory values: physical footprint, resident size, task memory-limit remaining when available, device physical memory, sample status/kernel error. No new timer/polling, no LRU/capacity, no retry/fallback/watchdog, no Repository/auth/protocol/parser/Send-Stream changes.

## Exact source preparation

- Diagnostics blob `5e927b43792535586d8406e1ca5f46cf51c6f041`
- Xcode blob `8530571220ba034d49d629031483cccaa6af61a1`
- Workflow blob `da751e26c2cd0da15b15f3e7aac9730e3b7158fc`
- Build script blob `5cac0fcb7a7a201afa57dfe2895eca84970ffad4`
- Syntax-only parse passed for new task-VM sampling construct.
- Product diff remains exactly four files: Diagnostics.swift, Xcode project, workflow, build script. ConversationFeature/Repository unchanged.
- Earlier sibling off-branch commits caused solely by docs checkpoint advancement were never published and are not Candidate sources.
- `main` advanced from `0ea4d729...` to `3cbb5c9a...` through merged PR #18. Compare evidence shows only `CONVERSATION_LIST_CACHE_PLAN.md`, `DEVELOPMENT_PLAN.md`, `START_HERE.md`, and `UI_INTERACTION_BASELINE.md`; no b19 product/config/state-owner overlap. Open PR count is 0.

## Evidence

- b18: Code + Static + CI + Artifact + tested Runtime accepted; Work not Stable.
- b19 Code: prepared, publication pending.
- b19 Static: source review + syntax parse passed; iPhoneOS compile pending.
- b19 CI/Artifact/Runtime: pending.

## Remaining gates

- b19 real iPhone footprint/headroom evidence and evidence-backed LRU decision.
- isolated Reload replacement-under-load.
- natural failed-resident navigation.
- supported account-switch isolation when route exists.
- non-personal workspace isolation Unknown/Unverified.

## Next exact action

Fast-forward branch ref to a product commit created from the current docs-only head using the four fixed product blobs, then validate the one intended b19 CI run. Do not update this checkpoint again before the ref move.