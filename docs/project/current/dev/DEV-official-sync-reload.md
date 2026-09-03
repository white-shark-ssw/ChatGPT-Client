# DEV-official-sync-reload

## Status

**Active — independent official-App research task. No ChatGPTClient product Candidate allocated.**

- **Work ID**: `DEV-official-sync-reload`
- **Routing aliases / keywords**: `官方App同步重载 / 官方同步重载 / sync reload / 官方App刷新 / 官方App重载`
- **Task**: Determine whether the supplied modified/decrypted official ChatGPT iOS app can safely gain explicit `同步` and `重载` controls, and establish the smallest evidence-backed injection/call path.
- **User intent / acceptance criteria**: Add user-triggered recovery controls to the official app if its existing conversation state owner can be invoked without duplicate Send, guessed polling/retry, or a second conversation/message authority. `同步` should reconcile the current conversation with server truth. `重载` should be a stronger explicit current-conversation rebuild/reload, not resend/regenerate/Stop.
- **Baseline**: branch from `main@94f0c5777dad262cd1fb22be49082dbd92c962f2`. Supplied official source ZIP `/mnt/data/ChatGPT_Decrypted.zip` has SHA-256 `bb11734434bee912355b1435930ee2a2e3b1078d42049a59649fd8d500938a80`, matching the exact official source ZIP already recorded by the parallel send/stream research. Official identity recorded there remains `com.openai.chat` / `1.2026.202` / `30140022279`.
- **Working branch / PR / head commit**: `dev/official-sync-reload-20260904`; PR not created; branch created from exact main baseline above. Head will advance with this checkpoint/build batch.
- **Candidate identity**: Product Candidate `Not allocated`. This task must not allocate b96 or any `DEV-send-stream` Candidate. If a standalone official research dylib/IPA is later emitted, assign a task-local research identity such as `OfficialSyncReloadProbe-v0.x` and record exact source/package hashes separately from ChatGPTClient Candidates.
- **Evidence**:
  - Package-level injection entry is present in the supplied ZIP: `Assets.framework` weak-loads `@rpath/ChatGPTEnhancer-0.1.0-alpha60-runtime-image-map.dylib`; therefore an independent chained dylib can attach UIKit controls without altering the official `ChatGPT.framework` binary.
  - Static exact-binary strings expose `ChatGPTConversation.ConversationViewModel`, `refresh(conversation:emptyPlaceholderPolicy:)`, `Conversations.DefaultConversationCoordinatorProvider`, `refreshCurrentConversationIfIdle(_:)`, `ChatGPTHistory.HistoryViewController`, `refresh(conversationID:)`, `Conversations.DefaultConversationRepository`, `fetchConversation(for:refreshConversationID:)`, `ConversationPollingManager`, `ConversationResumeFetchRecovery`, `conversationRefreshTasks`, `needsInitialRefresh`, and `RemoteConversationRefreshTaskKey`.
  - These strings prove existing official refresh/recovery plumbing exists, but do **not** yet prove a callable runtime selector, exact instance owner, invocation ABI, or correct distinction between soft Sync and hard Reload.
- **Files / modules in scope**: this checkpoint; task-local `scripts/research/official_ios_sync_reload/**`; one task-local research workflow `.github/workflows/research-official-ios-sync-reload.yml`. No product source changes are authorized.
- **State owner / shared dependencies**: official app's own conversation owner is the target; exact live owner/instance remains to be proven. The pre-existing enhancer load slot is packaging infrastructure only, not conversation authority.
- **Frozen / do-not-touch**: `ChatGPTClient/**`, `ChatGPTClient.xcodeproj/**`, product `ios-foundation.yml`, `scripts/research/official_ios_realtime_probe/**`, `DEV-send-stream` checkpoint/branch/PR, b95/b96 identities, and all product conversation/repository logic.
- **Parallel conflicts checked against**: `DEV-send-stream` is Active on `dev/send-stream-20260829`, PR #29, head `6fc119c90b950fec565da8febf464a129c9ea022`; its exact product remains b95 and b96 unallocated. This task uses a separate branch and separate research path, and must not modify or repurpose the active realtime Probe. Both may package the same user-supplied official source ZIP, but each emitted research IPA must have a unique artifact identity and must never overwrite the other's dylib/source artifact.
- **Completed**:
  1. Repository governance/session routing read and Development task selected as a new independent task.
  2. Real main / parallel branch / PR / Active checkpoint identity verified.
  3. Exact supplied official ZIP SHA verified against existing recorded official source identity.
  4. Static binary feasibility pass found an existing dylib injection entry plus multiple official current-conversation refresh/recovery symbols.
- **Validation state**: Static/package evidence only. No new code written yet. No CI. No Artifact. No Runtime/manual proof. Stable/Frozen No.
- **Pending**:
  1. Determine whether the candidate official classes/methods are Objective-C-callable at Runtime or are pure Swift-only entry points.
  2. Identify the live current-conversation owner/instance reachable from the official UI without creating a second state store.
  3. Observe one natural official refresh/reload path and map it to its real method/network/state transition.
  4. Only then bind task-local `同步` / `重载` buttons to the proven owner and package a uniquely identified research IPA if justified.
- **Next exact action**: Create a minimal task-local runtime introspection dylib that chains the original enhancer, adds a small `SR` research control, and logs only class availability / ObjC method lists / responder-controller class names for `ConversationViewModel`, `HistoryViewController`, `DefaultConversationRepository`, `DefaultConversationCoordinatorProvider`, and `ConversationPollingManager`. Do not invoke refresh yet. Build it independently and use Runtime evidence to select the real owner before any mutating hook.
- **Rejected / do-not-repeat**: direct guessed `/backend-api/conversation/{id}` refresh from a second session; guessed polling cadence; retry/timer/watchdog; duplicate Send/regenerate; direct patching of stripped Swift function offsets before owner/ABI evidence; modifying the existing realtime Probe to carry this feature; treating static strings as proof the methods are safely callable.
- **Open questions / risks**: Swift-only methods may not be ObjC-dispatchable. The active conversation owner may be an injected dependency hidden behind SwiftUI/Observation, so live-instance discovery may require observing a natural call rather than reaching through UIKit. Official version updates can invalidate any binary-offset technique, so prefer runtime type/selector/state-owner evidence over hard-coded offsets.

## Batch recovery point — Runtime inspector v0.1 source/CI

- **Known branch head before batch**: checkpoint commit `0363a79ff5b8eafe36af6a1409b16d3e1ae1c57f`.
- **Intended writes**: create task-local inspector source, UI, enhancer-chain source, build script and README under `scripts/research/official_ios_sync_reload/`; create `.github/workflows/research-official-ios-sync-reload.yml` last so incomplete source commits do not trigger the research build.
- **Confirmed completed writes**: this recovery checkpoint only.
- **Remaining writes**: all inspector source/build/workflow files, then CI observation and checkpoint refresh.
- **Do not touch during recovery**: any `ChatGPTClient/**`, `ChatGPTClient.xcodeproj/**`, `.github/workflows/ios-foundation.yml`, `scripts/research/official_ios_realtime_probe/**`, `docs/project/current/dev/DEV-send-stream.md`, or any b95/b96 product identity.
- **Next exact action on interruption**: inspect the task-local directory and workflow on `dev/official-sync-reload-20260904`; create only missing files, with the workflow created last.
