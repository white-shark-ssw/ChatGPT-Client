# DEV-official-sync-reload

## Status

**Active — isolated Runtime metadata Probe v0.1 packaged; Human Runtime is the current gate**

- **Work ID**: `DEV-official-sync-reload`
- **Routing aliases / keywords**: `官方App同步重载 / 官方App同步 / 官方App重载 / official sync reload / 同步重载研究`
- **Task**: Independently research whether the modified official ChatGPT iOS app can expose user-triggered `同步当前会话` and `重载当前会话` controls, and determine the smallest evidence-backed injection path.
- **User intent / acceptance criteria**: This task remains fully isolated from every other Active development task. Do not modify, reuse, advance or depend on another task's checkpoint, branch, PR, Candidate, research Probe state owner or product files. Research from the supplied official-app sample itself. Distinguish static feasibility from real-device Runtime proof.
- **Baseline**: `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`. Supplied official-app archive `/mnt/data/ChatGPT_Decrypted.zip`, SHA-256 `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`; bundle `com.openai.chat`, version `1.2026.202`, build `30140022279`, MinimumOSVersion `17.0`.
- **Working branch / PR / head commit**: `research/official-sync-reload-20260904`; no PR; exact source/CI head `60d761073e23568c964bf18aa250881871591da1` before this checkpoint update.
- **Candidate identity**: ChatGPTClient product Candidate **Not allocated**. Research identity is `OfficialSyncReloadProbe-v01`; it does not consume/reuse any product build number or another task's research identity.

## Current evidence

- Exact `ChatGPT.framework/ChatGPT` is arm64 Mach-O. Static strings prove official conversation machinery including `ConversationPollingManager`, `RepositoryRefreshRequirement`, `TurnExchangeReloadTracker`, `RemoteConversationRefreshTaskKey`, `AsyncTaskConversationObserver`, `TriggerAsyncStatusPollingConversationObserver`, `ConversationResumeFetchRecovery` and repository fetch-task state.
- **Current-conversation Sync is strongly supported by official code**: `ChatGPTConversation/ConversationViewModel.swift` contains `refresh(conversation:emptyPlaceholderPolicy:)`, `_isRefreshing`, and failure text `Could not refresh the current conversation`. Its initializer accepts `needsInitialRefresh` and `initialRefreshEmptyPlaceholderPolicy`.
- Repository-level official paths include `refresh(conversationID:)`, `refreshConversation(_:)`, `refreshConversations(withRequirement:)`, `fetchConversation(for:refreshConversationID:)`, `refresh(id:remoteId:gizmo:historyAndTrainingDisabled:requestTrackingData:emptyPlaceholderPolicy:)`, and coordinator-provider `refreshCurrentConversationIfIdle(_:)`.
- Swift/ObjC metadata proves `_TtC19ChatGPTConversation21ConversationViewModel` and `_TtC23ChatGPTConversationRoot25ConversationRootViewModel` are Objective-C-runtime classes. Root VM contains `$__lazy_storage_$_conversationViewModel`; Conversation VM contains `_isRefreshing`, `_conversationCoordinator`, `$__lazy_storage_$_conversationRepository`, `_currentRemoteId`, `_messagesViewModel`, `_isApplicationActive`, `_viewIsVisible`, and other official state.
- The useful refresh method is Swift-only/non-exported, so `performSelector:` / plain `dlsym` is not justified.
- ARM64 direct xref decoding located executable references: refresh failure string `0x05851a30` -> `0x00bfa31c`; `refresh(conversation:emptyPlaceholderPolicy:)` string `0x05852510` -> `0x00bfc87c`; history `refresh(conversationID:)` `0x05832a20` -> `0x005b803c`, `0x04000b18`, `0x04000f14`; coordinator-provider `refreshCurrentConversationIfIdle(_:)` `0x05943710` -> around `0x03e07e70`/`0x03e07eec`. These prove live code participation but do not identify a safe foreign-call Swift async ABI entry.
- Direct calls to neighboring stripped Swift addresses remain rejected because async entry/resume/closure thunks are interleaved.
- **Reload remains distinct from Sync**. `reloadConversationOnNextAppear` maps to project detail only; `ConversationStateResetManager.resetConversationStateIfNeeded()` is broad background-reset behavior and is rejected for manual reload. Official trigger constants distinguish `RELOAD`, `EXPLICIT_REFRESH`, and `FOREGROUND_REFETCH`.
- Supplied archive contains an unrelated enhancer injection, but `Assets.framework/Assets.troll-fools.bak` is the pre-injection Assets binary. Original Assets has `ncmds=44`, `sizeofcmds=4768`, load-command end `0x12c0`, and zero header padding through `0x8000`, sufficient for this Work's independent weak-load command.

## Probe v0.1 implementation

- **Purpose**: Runtime metadata/live-object acquisition only. It does **not** invoke Sync/Reload, issue network requests, poll, retry, schedule a watchdog, or own conversation state.
- **Source**: `research/official-sync-reload/OfficialSyncReloadProbe.mm` plus task-local `build_probe.sh`, `patch_assets_load.py`, `package_probe.sh` and dedicated workflow `.github/workflows/official-sync-reload-research.yml`.
- **Exact build gate**: `com.openai.chat` / `1.2026.202` / `30140022279`; mismatched builds fail closed.
- **Runtime behavior**: small `SR` entry on the key window. Tap enumerates Root/Conversation VM Objective-C methods and ivars with IMP/image offsets, bounded-scans current UIKit controller/object roots for live Root/Conversation VM instances, reads Root VM's known conversation-VM object ivar when available, and lets the user export `DEV-official-sync-reload-v01.txt`.
- **Privacy/state boundary**: no auth headers/tokens, prompt/chat body, raw conversation ID or secondary conversation/message store is recorded.
- **Known compile note**: one iOS-deprecation warning remains in the statically unreachable pre-iOS13 fallback for `UIApplication.windows`; target app MinimumOSVersion is iOS17.0. It is not a build failure and does not justify unrelated churn before Runtime.

## Exact CI / Artifact evidence

- First CI `33802366432 / 100804670064` failed before compilation because shallow checkout made `origin/main...HEAD` lack a merge-base. This was a workflow-history configuration failure, not a source compile failure.
- Deterministic workflow correction at `60d761073e23568c964bf18aa250881871591da1`: full checkout history + normal `git fetch origin main`; source behavior unchanged.
- **Passing dedicated research CI**: Run `33802426752`, Job `100804864632` — success.
- Scope guard diff against `main` contained only this task's workflow/checkpoint and `research/official-sync-reload/**`; no `ChatGPTClient/**`, Xcode project, product build script or permanent product CI changes.
- Built dylib: arm64 Mach-O dynamic library, install name `@rpath/OfficialSyncReloadProbe-v01.dylib`, ad-hoc signed in CI.
- Dylib SHA-256: `f3e6aab756cbf5445b0ac6c958ae55b02a3263e484e7beb0aaff125ec0f1255c`.
- Artifact: `9911569997`, name `DEV-official-sync-reload-runtime-metadata-v01`, Artifact ZIP digest `sha256:22db9e773c3bae406a9d3d9ff89ab31b3284f1756e01f329cf387e2788fc252d`.

## Exact research IPA package evidence

- Local package identity: `ChatGPT-Official-SyncReloadResearch-v01-TrollStore-20260904.ipa`.
- IPA SHA-256: `bcdb8a0609f7bf6a5257862f07f3ba4c350259db1e02655f60c15bc7bccba03a`.
- ZIP integrity passes.
- Official bundle identity remains exactly `com.openai.chat` / `1.2026.202` / `30140022279` / MinimumOSVersion `17.0`.
- Package starts from exact supplied ZIP, restores `Assets.framework/Assets.troll-fools.bak` as the Assets injection base, then adds only `@rpath/OfficialSyncReloadProbe-v01.dylib`.
- Final Assets load-command check contains this task's Probe and no `ChatGPTEnhancer` load command.
- File-hash diff against the supplied ZIP is exactly four intended payload changes: **changed** `Frameworks/Assets.framework/Assets`; **removed** the supplied unrelated `Frameworks/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`; **added** `Frameworks/OfficialSyncReloadProbe-v01.dylib`; **added** `DEV-official-sync-reload.txt` research marker. No other payload file hash changed.
- Because modifying Assets invalidates its original code signature, this research IPA relies on the user's normal TrollStore install-time re-sign flow with TrollStore `ldid` installed. Package/ZIP success is not launch proof.

## Scope / isolation

- **Files / modules in scope**: this Work's checkpoint/docs; `research/official-sync-reload/**`; dedicated research workflow; local official-app inspection/package only.
- **State owner / shared dependencies**: no second conversation/message store. Sync must flow through official current-conversation/repository ownership. Reload remains pending exact official teardown/reopen evidence.
- **Frozen / do-not-touch**: every other Active task checkpoint/branch/PR/Candidate, especially `DEV-send-stream`, `dev/send-stream-20260829`, PR #29, its Probe sources/artifacts and b95/b96 identity, plus ChatGPTClient product source.
- **Parallel isolation result**: this task's compiled dylib/package does not execute or depend on the supplied unrelated enhancer. No other task's branch/checkpoint/source/artifact was modified.

## Progress / validation

- **Code written**: Yes — isolated Runtime metadata Probe v0.1 + task-local build/package tooling.
- **Static/local package checks passed**: Yes — exact source ZIP identity, bundle identity, Mach-O load-command isolation, four-file payload hash diff, ZIP integrity.
- **CI passed**: Yes — exact Run/Job `33802426752 / 100804864632`.
- **Artifact produced**: Yes — dylib Artifact `9911569997`; research IPA SHA recorded above.
- **Runtime/manual/real-device tested**: **No / Pending**.
- **Stable/Frozen**: **No**.

## Human Runtime gate / next exact action

Install exact `ChatGPT-Official-SyncReloadResearch-v01-TrollStore-20260904.ipa` through TrollStore on the recorded iOS17 device, fully relaunch the official app, open a normal conversation, tap the floating `SR` button, tap `重新扫描` once if needed after the conversation is visibly loaded, then `分享日志` and return `DEV-official-sync-reload-v01.txt` to this Work. Also report whether the official app launched normally and whether the SR panel showed `Root VM` / `Conversation VM` as found.

The decisive v0.1 evidence is: (1) target classes exist at Runtime; (2) actual Objective-C method/thunk list + IMP offsets; (3) whether the live current Root VM and Conversation VM are reachable from the bounded official UI object graph. **Do not add or invoke Sync yet** until this Runtime result identifies a safe official call/owner bridge. Generic Reload remains a separate later evidence gate.

## Rejected / do-not-repeat

Another task's Probe/code as implementation authority; b96 or any ChatGPTClient product Candidate; guessed direct Swift address calls; `reloadConversationOnNextAppear` as generic reload; broad state reset as manual reload; guessed HTTP/polling/cadence/retry/watchdog/timer; treating static/CI/Artifact/package success as Runtime proof.
