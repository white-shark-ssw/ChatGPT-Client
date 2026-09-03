# DEV-official-sync-reload

## Status

**Active — OfficialSyncReloadInspector v0.1 is Code/CI/Artifact/package-ready; Human Runtime owner discovery is pending. No ChatGPTClient product Candidate allocated.**

- **Work ID**: `DEV-official-sync-reload`
- **Routing aliases / keywords**: `官方App同步重载 / 官方同步重载 / sync reload / 官方App刷新 / 官方App重载`
- **Task**: Determine whether the supplied modified/decrypted official ChatGPT iOS app can safely gain explicit `同步` and `重载` controls, and establish the smallest evidence-backed injection/call path.
- **User intent / acceptance criteria**: Add user-triggered recovery controls to the official app if its existing conversation state owner can be invoked without duplicate Send, guessed polling/retry, or a second conversation/message authority. `同步` should reconcile the current conversation with server truth. `重载` should be a stronger explicit current-conversation rebuild/reload, not resend/regenerate/Stop.
- **Baseline**: branch from `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`. Exact supplied official source ZIP SHA-256 `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`. Official identity remains `com.openai.chat` / `1.2026.202` / `30140022279`.
- **Working branch / PR / head commit**: `dev/official-sync-reload-20260904`; PR pending creation; exact inspector source/CI head before this checkpoint update `448cecbcf760ab506a8f894b0d4817d177df5f28`.
- **Candidate identity**: ChatGPTClient Product Candidate `Not allocated`; b96 remains owned/unallocated by parallel `DEV-send-stream`. Task-local research identity is `OfficialSyncReloadInspector-v0.1` only.

## Current evidence

- Exact official `Assets.framework` weak-loads `@rpath/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`, so a task-local chained dylib can attach research UI without patching `ChatGPT.framework`.
- Exact-binary strings expose existing official refresh/recovery machinery including `ConversationViewModel.refresh(conversation:emptyPlaceholderPolicy:)`, `DefaultConversationCoordinatorProvider.refreshCurrentConversationIfIdle(_:)`, `HistoryViewController.refresh(conversationID:)`, `DefaultConversationRepository.fetchConversation(for:refreshConversationID:)`, `ConversationPollingManager`, `ConversationResumeFetchRecovery`, `conversationRefreshTasks`, `needsInitialRefresh`, and `RemoteConversationRefreshTaskKey`.
- Additional Mach-O inspection confirms all five primary candidate types are present in `__TEXT,__objc_classname`: `_TtC19ChatGPTConversation21ConversationViewModel`, `_TtC14ChatGPTHistory21HistoryViewController`, `_TtC13Conversations29DefaultConversationRepository`, `_TtC13Conversations38DefaultConversationCoordinatorProvider`, `_TtC13Conversations26ConversationPollingManager`. Therefore the classes are Objective-C-runtime registered.
- The human-readable Swift method names such as `refreshCurrentConversationIfIdle` / `fetchConversation...` are not present as same-named selectors in `__TEXT,__objc_methname`; only generic refresh-related selectors such as `refresh` are present. Class registration therefore does **not** prove the desired Swift methods are safely callable through `performSelector` or identify the live owner instance.
- v0.1 intentionally performs no Sync/Reload mutation. Its floating `SR` menu only runs runtime inspection, exports JSONL and clears the inspector log. It records structural class/method/property/ivar/controller/view class metadata only; no conversation IDs, titles, prompt/response content, auth values, request headers or URLs.

## v0.1 exact identities

- Exact source/CI head: `448cecbcf760ab506a8f894b0d4817d177df5f28`.
- First CI run `33798505661 / 100791906647`: **failed deterministically at compile** because Objective-C `UIViewController` does not expose Swift spelling `.children`; no Artifact emitted.
- Minimal correction: only `.children` -> `.childViewControllers` in the controller traversal.
- Corrected CI run `33798682666 / 100792481086`: **success**; build, Mach-O validation, ad-hoc codesign inspection and Artifact upload all passed.
- Canonical research Artifact: `9910185423`, Artifact ZIP digest `sha256:90917895444a0ae5ccdefad78cbe8a78cb97ee96469c3082c7a8c4b28b6a4285`.
- Exact `ChatGPTSyncReloadInspector.dylib`: arm64 Mach-O, ad-hoc signed, SHA-256 `06ec42e956446792a3839bd4a50073037ec0709ca14a94f9b9fc6bfb150bda9f`.
- Exact local research IPA: `ChatGPT-Official-SyncReloadInspector-v01-TrollStore-20260904.ipa`, SHA-256 `f5d4001b79d019fc68e0d556becd3ac1e487a7259e036159d96908b096b602bf`.
- Package verification: ZIP integrity passes; bundle identity/version/build remain `com.openai.chat` / `1.2026.202` / `30140022279`; compared by file content against the exact pristine official source ZIP there are exactly three intended differences: add original enhancer backup, add v0.1 research marker, replace the original enhancer path with the inspector dylib. Both enhancer-path dylibs are packaged mode `0755`; original enhancer backup bytes preserve SHA-256 `aae66c63a7122d301be5025305b92ec63b8da020fdceef22df9bec7cc1acc7b3`.

## Scope / parallel safety

- **Files / modules in scope**: this checkpoint; `scripts/research/official_ios_sync_reload/**`; `.github/workflows/research-official-ios-sync-reload.yml`.
- **State owner / shared dependencies**: official app's own conversation owner is the target; exact live owner/instance remains to be proven. The enhancer load slot is packaging infrastructure only.
- **Frozen / do-not-touch**: `ChatGPTClient/**`, `ChatGPTClient.xcodeproj/**`, product `.github/workflows/ios-foundation.yml`, `scripts/research/official_ios_realtime_probe/**`, parallel `DEV-send-stream` checkpoint/branch/PR, and all b95/b96 product identities.
- **Parallel conflicts checked against**: `DEV-send-stream` remains Active on `dev/send-stream-20260829`, PR #29, independently owning the official realtime Probe and product Send/Stream work. This task uses its own branch, checkpoint, source path, workflow and research artifact identity. Sharing the same user-supplied pristine official ZIP is allowed; emitted dylibs/IPAs must remain uniquely identified and must not overwrite each other's research artifacts.

## Validation state

**Code written / exact source scoped / corrected dedicated CI passed / Artifact produced / dylib identity verified / research IPA produced and independently diff-verified / Human Runtime pending / Sync implementation not yet written / Reload implementation not yet written / Stable-Frozen No.**

## Next exact action

Install exact `ChatGPT-Official-SyncReloadInspector-v01-TrollStore-20260904.ipa` on the test device, fully launch official ChatGPT, open a normal existing conversation, tap `SR` -> `检查运行时` once, then `SR` -> `导出日志`. Analyze `ChatGPTSyncReloadInspector.jsonl` for the five candidate classes' exposed selectors/type encodings and the live conversation controller/view hierarchy. Do **not** add or invoke Sync/Reload until this Runtime snapshot identifies a real callable owner or rejects direct ObjC dispatch.

## Rejected / do-not-repeat

- Direct guessed `/backend-api/conversation/{id}` refresh from a second session.
- Guessed polling cadence, retry/timer/watchdog or duplicate state owner.
- Duplicate Send/regenerate/Stop as a substitute for Reload.
- Calling human-readable Swift symbol strings as guessed Objective-C selectors.
- Hard-coding stripped Swift function offsets before instance ownership and ABI are evidenced.
- Modifying or repurposing the parallel `official_ios_realtime_probe` to carry this feature.
- Treating CI/Artifact/package success as proof that Sync/Reload works at Runtime.

## Open questions / risks

- The refresh methods may remain Swift-direct even though their classes are ObjC-runtime registered.
- The live owner may be an injected dependency hidden behind SwiftUI/Observation; if so, the next evidence step should observe a natural official refresh call rather than synthesize a second repository or guess an object graph.
- Official version updates can invalidate any binary-offset technique; prefer runtime type/selector/state-owner evidence over hard-coded offsets.

## Batch recovery point — v0.1 source/CI/package

**Closed.** All intended task-local source/workflow writes completed, corrected CI passed, Artifact `9910185423` was produced, and exact research IPA identity/diff were verified. Recovery must not replay the failed run or repackage under a different hash without recording a new task-local research identity.
