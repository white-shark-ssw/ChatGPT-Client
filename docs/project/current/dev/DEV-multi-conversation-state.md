# DEV-multi-conversation-state

## Status

**Active — b18 Runtime accepted for tested historical-scroll matrix; b19 measurement-only product source is prepared and requires direct branch-ref publication; no LRU behavior has been chosen or implemented; Stable/Frozen = No**

- Work ID: `DEV-multi-conversation-state`
- Branch: `dev/multi-conversation-state-20260827`
- Current target main: `0ea4d7296f574722ec665b40633ecba42fc680e8`
- Last Runtime Candidate: `DEV-multi-conversation-state-0.1.0-b18` / `0.1.0 (18)`
- Reserved Candidate: `DEV-multi-conversation-state-0.1.0-b19` / `0.1.0 (19)` — measurement only

## b19 contract

b19 exists only to measure actual current-process memory while several conversations remain resident. It adds memory snapshot fields to existing `conversation / resident.*` diagnostics. It does **not** add LRU eviction, capacity constants, retry, timer, watchdog, fallback, polling, Repository changes, auth changes, protocol changes, parser changes, or future Send/Stream state.

Fields include process physical footprint, resident size, task memory-limit remaining bytes when returned, device physical memory, and sampling status/error.

## Exact source preparation

- Diagnostics blob `5e927b43792535586d8406e1ca5f46cf51c6f041`
- Xcode blob `8530571220ba034d49d629031483cccaa6af61a1`
- Workflow blob `da751e26c2cd0da15b15f3e7aac9730e3b7158fc`
- Build script blob `5cac0fcb7a7a201afa57dfe2895eca84970ffad4`
- Syntax-only parse passed for task-VM sampling construct.
- Exact prepared commit after the latest docs-only head is `172ac394be6dad0f6d07e1ccd6cf70f60cf0bc1e`, tree `abd11c0a98530b21d6114bacb60f015f9348200c`, parent `9c97d687d43fc0d3793df30a724bc6254bddba08`.
- Parent->product compare contains exactly 4 files: Diagnostics.swift, Xcode project, workflow, build script. ConversationFeature/Repository are unchanged.
- Earlier sibling off-branch product commits were never published and are not Candidate sources.
- main's latest merged planning changes do not overlap these product/config files; open PR list is empty.

## Evidence labels

- b18: Code + Static + CI + Artifact + tested Runtime accepted; Work not Stable.
- b19 Code: prepared, publication pending.
- b19 Static: source review + syntax parse passed; iPhoneOS compile pending.
- b19 CI: pending.
- b19 Artifact: pending.
- b19 Runtime memory evidence: pending.
- Stable/Frozen: No.

## Remaining gates

- Exact b19 memory measurements and evidence-backed normal-LRU decision.
- Isolated same-target Reload replacement-under-load.
- Natural failed resident navigation with no implicit retry.
- Supported account-switch isolation when a real route exists.
- Non-personal workspace isolation remains Unknown/Unverified.

## Next exact action

Directly fast-forward the branch ref to a product commit built from the latest docs-only head, then validate the single intended b19 CI run and Artifact. Do not create another docs-only checkpoint before that ref move.