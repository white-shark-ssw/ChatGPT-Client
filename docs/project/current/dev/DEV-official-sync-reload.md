# DEV-official-sync-reload

## Status

**Active — special isolated research task; static feasibility established, callable bridge / Runtime still pending**

- **Work ID**: `DEV-official-sync-reload`
- **Routing aliases / keywords**: `官方App同步重载 / 官方App同步 / 官方App重载 / official sync reload / 同步重载研究`
- **Task**: Independently research whether the modified official ChatGPT iOS app can expose user-triggered `同步当前会话` and `重载当前会话` controls, and determine the smallest evidence-backed injection path.
- **User intent / acceptance criteria**: This task remains fully isolated from every other Active development task. Do not modify, reuse, advance or depend on another task's checkpoint, branch, PR, Candidate, research Probe state owner or product files. Research from the supplied official-app sample itself. Distinguish static feasibility from real-device Runtime proof.
- **Baseline**: `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`. Supplied local official-app archive `/mnt/data/ChatGPT_Decrypted.zip`, SHA-256 `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`; bundle `com.openai.chat`, version `1.2026.202`, build `30140022279`, MinimumOSVersion `17.0`.
- **Working branch / PR / head commit**: `research/official-sync-reload-20260904`; no PR; initial checkpoint commit `f495b399fd82f3398ae0252687031651abff093d`.
- **Candidate identity**: Product Candidate **Not allocated**. A future modified official-app package must use a task-specific research artifact identity only; never consume/reuse ChatGPTClient product build numbers or another task's research identity.

## Current evidence

- Exact `ChatGPT.framework/ChatGPT` is a ~126 MB arm64 Mach-O. Static strings prove official conversation machinery including `ConversationPollingManager`, `RepositoryRefreshRequirement`, `TurnExchangeReloadTracker`, `RemoteConversationRefreshTaskKey`, `AsyncTaskConversationObserver`, `TriggerAsyncStatusPollingConversationObserver`, `ConversationResumeFetchRecovery` and related repository fetch-task state.
- **Current-conversation Sync is strongly supported by official code**: `ChatGPTConversation/ConversationViewModel.swift` contains `refresh(conversation:emptyPlaceholderPolicy:)`, `_isRefreshing`, and failure text `Could not refresh the current conversation`. Its initializer explicitly accepts `needsInitialRefresh` and `initialRefreshEmptyPlaceholderPolicy`.
- Repository-level official paths include `refresh(conversationID:)`, `refreshConversation(_:)`, `refreshConversations(withRequirement:)`, `fetchConversation(for:refreshConversationID:)`, `refresh(id:remoteId:gizmo:historyAndTrainingDisabled:requestTrackingData:emptyPlaceholderPolicy:)`, and coordinator-provider `refreshCurrentConversationIfIdle(_:)`.
- Swift/ObjC metadata proves `_TtC19ChatGPTConversation21ConversationViewModel` is a real Objective-C-runtime class with **264 runtime ivars**, including `_isRefreshing`, `_conversationCoordinator`, `$__lazy_storage_$_conversationRepository`, `_currentRemoteId`, `_messagesViewModel`, `_isApplicationActive`, and `_viewIsVisible`. The class has no ObjC base-method list for the target refresh operation: the useful refresh API is Swift-only/non-exported, so `performSelector:` / plain `dlsym` is not a justified implementation.
- `_TtC23ChatGPTConversationRoot25ConversationRootViewModel` is also an Objective-C-runtime class. It has a direct 8-byte `$__lazy_storage_$_conversationViewModel` field, `_conversationCoordinator`, `$__lazy_storage_$_conversationCoordinatorProvider`, `$__lazy_storage_$_conversationRepository`, and `explicitActions`. This provides a plausible runtime bridge to the **official current ConversationViewModel** without inventing a second conversation authority once a safe live Root VM reference is acquired.
- `DefaultConversationCoordinatorProvider` has `conversationCoordinators`, `coordinatorsSubject`, `observers`, and `observerProviders`; `DefaultConversationRepository` owns the authoritative fetch/cache task machinery.
- ARM64 xref/function-start analysis independently located the official refresh failure/method code regions and async continuation chains. This confirms the strings participate in executable paths, but the exact externally callable Swift ABI entry is **not yet proven safe to invoke from injected C/ObjC code**.
- **Reload must remain distinct from Sync**. `reloadConversationOnNextAppear` was mapped to `ChatGPTProjects.ProjectDetailViewModel`; it is rejected as a generic chat reload entry. `ConversationStateResetManager.resetConversationStateIfNeeded()` is explicitly logged as `Resetting conversation state after app was backgrounded`; it is too broad and is not accepted as a manual hard-reload action.
- Official analytics/protobuf constants independently distinguish historical-conversation visit triggers `RELOAD`, `EXPLICIT_REFRESH`, and `FOREGROUND_REFETCH`, supporting separate semantics rather than implementing Reload as a renamed Sync.
- The supplied archive is already modified: `Assets.framework/Assets` weak-loads an existing enhancer dylib and `Assets.troll-fools.bak` is a pre-injection backup. For this Work, any future package should restore/use the backup `Assets` as the injection base and load only a **new uniquely named task-owned dylib**, so it does not execute or depend on another task's enhancer.

## Scope / isolation

- **Files / modules in scope**: this Work's checkpoint/docs; new research source/tooling under a unique task path; local inspection of the supplied official app archive; a future task-owned injected dylib/package only.
- **State owner / shared dependencies**: do not create a second conversation/message store. Sync must flow through official current-conversation/repository ownership. Reload semantics remain pending exact official teardown/reopen evidence.
- **Frozen / do-not-touch**: every other Active task checkpoint/branch/PR/Candidate, especially `DEV-send-stream`, `dev/send-stream-20260829`, PR #29, all of its Probe sources/artifacts, b95/b96 identity, and ChatGPTClient product source.
- **Parallel conflicts checked against**: same supplied official binary may be independently inspected, but this Work may not read/modify/reuse the other task's implementation state. Any injection code and artifact identity here must be unique.

## Progress / validation

- **Completed**: governance routing; independent Work ID/branch; exact baseline/archive identity verification; archive provenance/diff inspection; static string/source-owner analysis; Swift field metadata + ObjC runtime class/ivar analysis; first ARM64 executable xref/function-chain confirmation; rejection of project-only/broad reset routes for generic Reload.
- **Validation state**: branch isolation verified; local static binary evidence is strong. **No injected code written; no CI; no research IPA; no real-device Runtime; Stable/Frozen No.**
- **Pending**: establish the minimal safe live-object bridge to the current Root/Conversation VM; identify a callable official Sync trigger without guessed HTTP; establish generic Reload semantics (likely authoritative teardown/reopen/recreate, not background reset); only then add UI and package a separate research IPA.
- **Next exact action**: determine the least-invasive runtime acquisition mechanism for the live `ConversationRootViewModel` and verify, from executable metadata/call sites, one callable official Sync path. Prefer a version-gated official-object bridge; reject broad lifecycle-notification simulation, manual HTTP, timers/polling/retry, or a second state owner. Do not implement Reload until its stronger state-replacement path is evidenced separately.
- **Rejected / do-not-repeat**: another task's Probe/code as implementation authority; b96 or any ChatGPTClient product Candidate; `reloadConversationOnNextAppear` as generic reload; `ConversationStateResetManager` as manual reload; guessed HTTP/polling/cadence/retry/watchdog/timer; treating string presence or CI/artifact as Runtime proof.
- **Open questions / risks**: target methods are Swift-only and stripped; exact Swift calling ABI/lifetime requirements must be respected. Live instance acquisition must not require a hot global hook if a narrower owner path can be evidenced. Official internal layout is build-specific, so any binary-offset bridge must hard-gate exact official version/build and fail closed on mismatch.
