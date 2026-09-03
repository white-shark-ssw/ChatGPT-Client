# DEV-official-sync-reload

## Status

**Active — special isolated research task; static feasibility established, runtime metadata bridge implementation beginning**

- **Work ID**: `DEV-official-sync-reload`
- **Routing aliases / keywords**: `官方App同步重载 / 官方App同步 / 官方App重载 / official sync reload / 同步重载研究`
- **Task**: Independently research whether the modified official ChatGPT iOS app can expose user-triggered `同步当前会话` and `重载当前会话` controls, and determine the smallest evidence-backed injection path.
- **User intent / acceptance criteria**: This task remains fully isolated from every other Active development task. Do not modify, reuse, advance or depend on another task's checkpoint, branch, PR, Candidate, research Probe state owner or product files. Research from the supplied official-app sample itself. Distinguish static feasibility from real-device Runtime proof.
- **Baseline**: `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`. Supplied local official-app archive `/mnt/data/ChatGPT_Decrypted.zip`, SHA-256 `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`; bundle `com.openai.chat`, version `1.2026.202`, build `30140022279`, MinimumOSVersion `17.0`.
- **Working branch / PR / head commit**: `research/official-sync-reload-20260904`; no PR; verified head before current write batch `70f1cda2b4ef6f9a74751a5e658050d1ae2afe2d`.
- **Candidate identity**: Product Candidate **Not allocated**. Any modified official-app package uses task-specific research identity only; never consume/reuse ChatGPTClient product build numbers or another task's research identity.

## Current evidence

- Exact `ChatGPT.framework/ChatGPT` is an arm64 Mach-O. Static strings prove official conversation machinery including `ConversationPollingManager`, `RepositoryRefreshRequirement`, `TurnExchangeReloadTracker`, `RemoteConversationRefreshTaskKey`, `AsyncTaskConversationObserver`, `TriggerAsyncStatusPollingConversationObserver`, `ConversationResumeFetchRecovery` and repository fetch-task state.
- **Current-conversation Sync is strongly supported by official code**: `ChatGPTConversation/ConversationViewModel.swift` contains `refresh(conversation:emptyPlaceholderPolicy:)`, `_isRefreshing`, and failure text `Could not refresh the current conversation`. Its initializer accepts `needsInitialRefresh` and `initialRefreshEmptyPlaceholderPolicy`.
- Repository-level official paths include `refresh(conversationID:)`, `refreshConversation(_:)`, `refreshConversations(withRequirement:)`, `fetchConversation(for:refreshConversationID:)`, `refresh(id:remoteId:gizmo:historyAndTrainingDisabled:requestTrackingData:emptyPlaceholderPolicy:)`, and coordinator-provider `refreshCurrentConversationIfIdle(_:)`.
- Swift/ObjC metadata proves `_TtC19ChatGPTConversation21ConversationViewModel` and `_TtC23ChatGPTConversationRoot25ConversationRootViewModel` are Objective-C-runtime classes. Root VM contains `$__lazy_storage_$_conversationViewModel`; Conversation VM contains `_isRefreshing`, `_conversationCoordinator`, `$__lazy_storage_$_conversationRepository`, `_currentRemoteId`, `_messagesViewModel`, `_isApplicationActive`, `_viewIsVisible`, and other official state.
- The useful refresh method is Swift-only/non-exported, so `performSelector:` / plain `dlsym` is not justified.
- ARM64 direct xref decoding now precisely locates executable references: refresh failure string `0x05851a30` is referenced at `0x00bfa31c`; `refresh(conversation:emptyPlaceholderPolicy:)` string `0x05852510` is referenced at `0x00bfc87c`; history `refresh(conversationID:)` string `0x05832a20` has executable references including `0x005b803c`, `0x04000b18`, `0x04000f14`; coordinator-provider `refreshCurrentConversationIfIdle(_:)` string `0x05943710` has executable references around `0x03e07e70`/`0x03e07eec`. These prove live code participation but do **not** yet identify a safe foreign-call Swift async ABI entry.
- Because async entry/resume/closure thunks are interleaved around the xrefs, direct calls to nearby stripped addresses are explicitly rejected until Runtime metadata/IMP evidence proves a callable thunk.
- **Reload remains distinct from Sync**. `reloadConversationOnNextAppear` maps to project detail only; `ConversationStateResetManager.resetConversationStateIfNeeded()` is broad background-reset behavior and is rejected for manual reload. Official trigger constants distinguish `RELOAD`, `EXPLICIT_REFRESH`, and `FOREGROUND_REFETCH`.
- Supplied archive already contains an unrelated injected enhancer, but `Assets.framework/Assets.troll-fools.bak` is the pre-injection Assets binary. Comparing it with the modified Assets shows the injection mechanism adds one `LC_LOAD_WEAK_DYLIB`; original `ncmds=44`, `sizeofcmds=4768`, command end `0x12c0`, with zero header padding through `0x8000` (27,968 bytes). Therefore this Work can independently start from `.bak` and add only its own dylib without retaining another enhancer.

## Scope / isolation

- **Files / modules in scope**: this Work's checkpoint/docs; new `research/official-sync-reload/` source/tooling; local inspection of the supplied official app archive; task-owned injected dylib/package only.
- **State owner / shared dependencies**: no second conversation/message store. Sync must flow through official current-conversation/repository ownership. Reload remains pending exact official teardown/reopen evidence.
- **Frozen / do-not-touch**: every other Active task checkpoint/branch/PR/Candidate, especially `DEV-send-stream`, `dev/send-stream-20260829`, PR #29, its Probe sources/artifacts and b95/b96 identity, plus ChatGPTClient product source.
- **Parallel conflicts checked against**: same supplied official binary may be independently inspected, but this Work may not read/modify/reuse another task's implementation state. Injection code and artifact identity here are unique.

## Current implementation batch recovery point

- **Known branch head before batch**: `70f1cda2b4ef6f9a74751a5e658050d1ae2afe2d`.
- **Intent**: add a task-owned Runtime metadata probe only; no Sync/Reload trigger yet.
- **Planned writes**: `research/official-sync-reload/OfficialSyncReloadProbe.mm`, task-local README/build/package helper, and a dedicated research CI workflow if repository permissions allow it.
- **Probe responsibilities**: exact official build gate; enumerate target class methods/ivars with IMP/image offsets; bounded scan from current UIKit controller roots for live Root/Conversation VM instances; visible `SR` research entry; exportable local diagnostic text. It must not call refresh, issue network requests, poll, retry, or own conversation state.
- **Packaging rule**: restore/copy `Assets.troll-fools.bak`, inject one weak load for a uniquely named `OfficialSyncReloadProbe` dylib, and do not load the supplied unrelated enhancer.
- **Recovery rule**: if this write chain is interrupted, re-read this checkpoint and actual branch contents, then create only missing files. Do not touch any other Work.

## Progress / validation

- **Completed**: governance routing; independent Work ID/branch; baseline/archive identity verification; static string/source-owner analysis; Swift field metadata + ObjC runtime class/ivar analysis; precise ARM64 xrefs; rejection of unsafe direct Swift-address calls; independent Assets injection feasibility.
- **Validation state**: branch isolation verified; local static binary evidence is strong. **No Runtime metadata probe built yet; no research IPA; no real-device Runtime; Stable/Frozen No.**
- **Pending**: build the metadata probe; obtain exact Runtime methods/ivars/live-instance evidence; then choose one official Sync trigger. Generic Reload remains a separate later evidence gate.
- **Next exact action**: create/build the isolated Runtime metadata probe and package a research-only official-app test artifact if build/sign tooling succeeds. Human Runtime should inspect/export metadata only; do not invoke Sync until the callable path is proven.
- **Rejected / do-not-repeat**: another task's Probe/code as implementation authority; b96 or any ChatGPTClient product Candidate; guessed direct Swift address calls; `reloadConversationOnNextAppear` as generic reload; broad state reset as manual reload; guessed HTTP/polling/cadence/retry/watchdog/timer; treating static/CI/artifact as Runtime proof.
- **Open questions / risks**: target methods are Swift-only and stripped; live instance acquisition may require a narrower owner hook after metadata results. Official internal layout is build-specific, so any binary-offset bridge must hard-gate exact official version/build and fail closed on mismatch.
