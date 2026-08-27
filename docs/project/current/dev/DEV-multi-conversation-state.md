# DEV-multi-conversation-state

## Status

**Active — b18 Runtime accepted for tested historical-scroll matrix; b19 measurement-only product source is prepared; no LRU behavior has been chosen or implemented; Stable/Frozen = No**

- Work ID: `DEV-multi-conversation-state`
- Branch: `dev/multi-conversation-state-20260827`
- Target main: `0ea4d7296f574722ec665b40633ecba42fc680e8`
- Last Runtime Candidate: `DEV-multi-conversation-state-0.1.0-b18` / `0.1.0 (18)`
- Reserved Candidate: `DEV-multi-conversation-state-0.1.0-b19` / `0.1.0 (19)` — measurement only

## b19 measurement contract

b19 adds actual current-process task VM memory values only to existing `conversation / resident.*` diagnostics events. It does not add LRU eviction, capacity constants, retry, timer, watchdog, fallback, polling, Repository/auth/protocol/parser changes, or future Send/Stream state.

Memory fields: `processPhysFootprintBytes`, `processResidentSizeBytes`, `processMemoryLimitRemainingBytes` when available, `devicePhysicalMemoryBytes`, plus sample status/kernel return on failure.

## Exact prepared source

- Diagnostics blob `5e927b43792535586d8406e1ca5f46cf51c6f041`
- Xcode blob `8530571220ba034d49d629031483cccaa6af61a1`
- Workflow blob `da751e26c2cd0da15b15f3e7aac9730e3b7158fc`
- Build script blob `5cac0fcb7a7a201afa57dfe2895eca84970ffad4`
- Syntax-only parse passed for the task-VM sampling construct.
- Current prepared commit `a806dc21b823b43b52566f65fadb2ea9e88d2ee1`, tree `ca9fda683ccaea9e1b7d60d7f330f37c1b00ed62`, parent `9a1c8b78fc701d983eeacc294fbfa4a7d8ef94ca`.
- Exact product changes remain only Diagnostics.swift, Xcode project, workflow, build script; ConversationFeature/Repository unchanged.
- Earlier sibling product commits were not published; they are not Candidate sources.
- main planning changes are non-overlapping; open PRs were empty at publication gate.

## Evidence labels

- b18: Code + Static + CI + Artifact + tested Runtime accepted; Work not Stable.
- b19 Code: prepared; publication pending.
- b19 Static: source review + syntax parse passed; iPhoneOS compile pending.
- b19 CI: pending.
- b19 Artifact: pending.
- b19 Runtime memory evidence: pending.
- Stable/Frozen: No.

## Remaining gates

1. Publish exact b19 and validate CI/Artifact.
2. Collect real iPhone footprint/headroom data across several small/large residents and repeated switching.
3. Decide LRU only from measured evidence; code change, if justified, uses a new Candidate after b19.
4. Isolated same-target Reload replacement-under-load, natural failed-resident navigation, supported account-switch isolation, and non-personal workspace evidence remain open/conditional.

## Next exact action

Publish the b19 product source by direct branch ref update and then validate the single intended CI run. No further pre-publication docs should be written.