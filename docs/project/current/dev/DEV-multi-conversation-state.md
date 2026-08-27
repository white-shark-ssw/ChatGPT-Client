# DEV-multi-conversation-state

## Status

**Active — b18 Runtime accepted for tested historical-scroll matrix; exact b19 measurement-only Candidate has Code + Static + CI + identity-valid Artifact; real-device process-memory Runtime evidence pending; no LRU behavior has been chosen or implemented; Stable/Frozen = No**

- Work ID: `DEV-multi-conversation-state`
- Branch: `dev/multi-conversation-state-20260827`
- Target main: `3cbb5c9acce26c0004e1d78c9607f2361d83fe05`
- Last Runtime Candidate: `DEV-multi-conversation-state-0.1.0-b18`
- Current exact Candidate: `DEV-multi-conversation-state-0.1.0-b19` / `0.1.0 (19)` — measurement only
- Exact product/config source: `c6accf16c8cf80c719f1e569e356b2bbe664e91e`; tree `9142ebe7c4cd0860428d8fe35ee341507f61d051`.
- CI: Run `33063446367`; Job `98487641474`; success.
- Artifact: `9642715296`; `ChatGPTClient-DEV-multi-conversation-state-0.1.0-b19`; upload ZIP `sha256:7f33f13818b1ef77c83c84b7371fea2b930d4786709b72c9442fe33765b3bafc`.
- IPA: `ChatGPTClient-0.1.0-b19-dev-multi-conversation-state.ipa`; SHA `04861c63278d4a8fdf7c655f80b97f01cf8880d9f362d2f3edf1f55aec8ca8bc`.

## b19 exact scope

Enrich existing `conversation / resident.*` diagnostics with current-process task VM memory values: physical footprint, resident size, task memory-limit remaining when available, device physical memory, sample status/kernel error. No new timer/polling, no LRU/capacity, no retry/fallback/watchdog, no Repository/auth/protocol/parser/Send-Stream changes.

## Exact source / package evidence

- Diagnostics blob `5e927b43792535586d8406e1ca5f46cf51c6f041`.
- Xcode blob `8530571220ba034d49d629031483cccaa6af61a1`.
- Workflow blob `da751e26c2cd0da15b15f3e7aac9730e3b7158fc`.
- Build script blob `5cac0fcb7a7a201afa57dfe2895eca84970ffad4`.
- Source review + syntax-only parse passed before publication.
- Product diff is exactly four files: `Diagnostics.swift`, Xcode project, workflow, build script. `ConversationFeature.swift` / `ConversationRepository` unchanged.
- Run `33063446367` checked out exact `c6accf16c8cf80c719f1e569e356b2bbe664e91e`; build/inspect/upload steps all succeeded.
- Independent Artifact inspection matches sidecar and embedded package identity: `0.1.0 (19)`, candidate `DEV-multi-conversation-state-0.1.0-b19`, source `c6accf16c8cf`, minimum iOS `14.0`, `UIDeviceFamily=[1,2]`, Mach-O arm64.
- Earlier sibling off-branch commits caused solely by docs checkpoint advancement were never published and are not Candidate sources.
- `main` advanced from `0ea4d729...` to `3cbb5c9a...` through merged PR #18. Compare evidence shows only `CONVERSATION_LIST_CACHE_PLAN.md`, `DEVELOPMENT_PLAN.md`, `START_HERE.md`, and `UI_INTERACTION_BASELINE.md`; no b19 product/config/state-owner overlap. Open PR count was 0 at publication guard.

## Evidence labels

- b18: Code + Static + CI + Artifact + tested Runtime accepted; Work not Stable.
- b19 Code: **Yes — exact source published**.
- b19 Static/source: **Passed**.
- b19 CI: **Passed — Run `33063446367`, Job `98487641474`**.
- b19 Artifact: **Produced / identity independently accepted — Artifact `9642715296`**.
- b19 Runtime/manual/real-device: **Pending**.
- Stable/Frozen: **No**.

## Remaining gates

- b19 real iPhone footprint/headroom evidence and evidence-backed LRU decision.
- isolated Reload replacement-under-load.
- natural failed-resident navigation.
- supported account-switch isolation when route exists.
- non-personal workspace isolation Unknown/Unverified.

## Next exact action

Install exact b19 on iPhone/iOS17. Exercise several small and large conversations until multiple residents are retained, repeatedly switch among them, then export diagnostics. Evaluate `processPhysFootprintBytes` and `processMemoryLimitRemainingBytes` together with resident/active/protected counts. Do not choose or implement normal LRU capacity until that Runtime evidence is reviewed.