# DEV-native-read-path

## Status

**Active**

- **Work ID**: `DEV-native-read-path`
- **Routing aliases / keywords**: `官方 App UI 主框架与原生会话读取 / 原生会话读取 / 官方 App UI / native read path`
- **Task**: Build the official-App-style native main shell and establish production conversation list/detail/message read ownership.
- **User intent / acceptance criteria**: Replace the diagnostic landing screen with the first usable native read experience: official-style sidebar/main-chat shell, authenticated native conversation list, selected-conversation identity owned outside UI text, conversation-detail loading, and readable current-branch user/assistant messages. Keep b7 auth/protocol evidence boundaries and do not add speculative retry/fallback behavior.
- **Baseline**: `main` at `2ad48e5b1544dee4611edfaea85583e0a3aa81a8`; accepted runtime baselines `DEV-auth-bootstrap-0.1.0-b6` and `DEV-protocol-read-0.1.0-b7`; iPhone / iOS 17.0 runtime evidence; deployment target iOS 14.0.
- **Working branch / PR / head commit**: `dev/native-read-path-20260826`; PR not created; initial branch head `2ad48e5b1544dee4611edfaea85583e0a3aa81a8` before this checkpoint commit.
- **Candidate identity**: Not allocated. Re-check `BUILD_TEST_INDEX.md`, active checkpoints, real version/build source and CI/artifact identities immediately before first testable artifact.
- **Evidence**: b7 proved Plus/personal list GET and one detail GET with transient bearer + copied ephemeral WebKit cookies. First tested detail was 13,152,411 bytes / 2068 mapping nodes. Current `RootViewController` is diagnostic-only; `ProtocolReadProbe` intentionally persists no production conversation state.
- **Files / modules in scope**: `ChatGPTClient/RootViewController.swift`; new production conversation models/repository/store under `ChatGPTClient/Conversation/`; native sidebar/list/detail/message UI; authentication bridge usage from `AuthSessionStore`; Xcode project membership; diagnostics at conversation lifecycle boundaries; project checkpoint/durable docs when ownership truth changes.
- **State owner / shared dependencies**: New production conversation repository/store will own list payloads, selected conversation identity and loaded detail/current message branch. `AuthSessionStore` remains auth/account-context owner; default WebKit store remains persistent auth-secret authority; `ProtocolReadProbe` remains diagnostic-only.
- **Frozen / do-not-touch**: No Frozen modules. Preserve Stable auth/account and protocol-read diagnostic contracts unless direct current evidence requires a change; do not turn `ProtocolReadProbe` into production state owner.
- **Parallel conflicts checked against**: `docs/project/current/dev/` contained no Active task checkpoints at task creation. No branch/candidate conflict found.
- **Completed**: Governance/session routing; project profile/state/rules/UI baseline review; Active-task conflict scan; real `main` baseline verification; dedicated branch creation; initial production ownership boundary identified from current source.
- **Validation state**: No product code written yet. No local/static checks, CI, artifact or runtime/manual test for this task yet.
- **Pending**: Inspect exact project-file membership and auth-screen sequencing; implement production conversation models/repository; implement list/detail current-branch parsing; replace diagnostic root with native shell/list/read UI; compile/CI; then allocate a unique candidate only when artifact stage is reached.
- **Next exact action**: Inspect `AppDelegate.swift`, `AuthWebViewController.swift`, and `project.pbxproj` on this branch, then implement the smallest production conversation repository API that reuses `AuthSessionStore.probeAccountContext(... createTransientSession: true)` without duplicating auth state.
- **Rejected / do-not-repeat**: No automatic session retry; no UA spoof/Cloudflare bypass; no speculative account/browser headers; no fallback conversation endpoints; no UI-title identity; no naive assumption that every mapping node should become a mounted view; no reuse of `ProtocolReadProbe` as the production repository.
- **Open questions / risks**: Exact message content types beyond the b7 structural counts need current-source parsing that tolerates unsupported visible types without inventing semantics. Large conversations require current-branch extraction and bounded rendering rather than all-node materialization. Runtime behavior below iOS 17.0 and on iPad remains Unverified.
