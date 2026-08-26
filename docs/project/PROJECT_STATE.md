# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone / iOS 17.0 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + one-detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`, version `0.1.0 (9)`: **merged Stable production native-read baseline for tested scope**. Product source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA-256 `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`. Runtime acceptance covers native shell, production list, two distinct details, current-branch extraction and visible user/assistant rendering on iPhone / iOS 17.0. Stable is scoped, not Frozen.

b8 remains historical partial/failing evidence only; b9's two successful detail reads supersede any inference that the earlier one-off HTTP 500 represented a systematic current read failure.

## Current active candidate

`DEV-conversation-recovery-0.1.0-b11`, version `0.1.0 (11)`, is the active recovery UX follow-up on `dev/conversation-recovery-20260826` / PR #10.

- Product/config source: **`8ab510265d891fc6b7eb048f03a5a683ec94b44b`**.
- Validation: **Code written + static/source diff reviewed. CI has not run. Artifact not produced. Runtime not tested.**
- Expected IPA: `ChatGPTClient-0.1.0-b11-dev-conversation-recovery.ipa`.
- b11 only adds non-blocking manual latest-sync feedback and build/candidate identity. It does not change `ConversationRepository`, endpoints, headers, auth, recovery request semantics or the authoritative state owner.
- Exact feedback product diff: one file, `ConversationFeature.swift`, 21 additions / 0 deletions.
- The existing GitHub connector could not emit a new Actions run for the b11 head and exposes no `workflow_dispatch` write action. Old failed run `32985845398` tested old `bdb18407...`, not b11, and is not evidence for b11.
- PR #10 is open/unmerged; branch compare remains `behind_by=0` against `main@a43762d255e699a753011103b7e1a6bb5416cb30`.

### Accepted b10 runtime inside the same Work

`DEV-conversation-recovery-0.1.0-b10` / `0.1.0 (10)` remains the accepted **core recovery runtime evidence** while b11 closes the UX gap.

- Source `89129913cb29a35db9dec7a6d5670d1b3b76bc23`; CI run `32982836557` passed; artifact `9612167843`; IPA SHA-256 `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- User tested exact b10 on iPhone / iOS 17.0 and reported no functional recovery problems.
- Full reload visibly cleared the content, showed the reload state, then rebuilt the same conversation.
- Diagnostics independently confirm two loaded-state latest-syncs and two full reloads all completed `status=ok`. Tested syncs had zero added/removed/changed visible messages, which exposed only the missing completion-feedback UX.
- No resend/duplicate-message issue was observed.

## Delivery direction

- **V0.1 read-use**: native shell + list/detail/message rendering + manual latest-message sync/current-conversation reload. Core recovery runtime is accepted on b10; b11 is the final UI-feedback candidate and remains blocked at the CI/Artifact gate.
- **V0.2 chat-use**: V0.1 + send/new conversation + streaming + stop + visible reasoning interaction + reasoning-to-final haptics + recovery integration.
- **V0.3 daily-use refinement**: Markdown export, long-conversation tuning, attachments and other daily-use features.

Small low-risk UX enhancements may be inserted between core phases only when dependencies are merged and conflict scanning is clean. `DEV-conversation-round-count` remains planned after recovery and before send/stream.

## UI / interaction direction

`docs/project/UI_INTERACTION_BASELINE.md` remains authoritative.

- b9 accepted the first production sidebar/detail read shell on iPhone / iOS 17.0.
- b10 runtime accepted loaded-state `同步最新消息`, `重载当前会话`, and terminal full-reload semantics for the tested scope.
- b11 adds visible non-blocking sync progress/result feedback: `正在同步最新消息…` then `已是最新` or `已同步最新消息`. The bounded delayed clear is presentation-only.
- Recovery remains explicit user action only; no automatic watchdog/retry/resend chain.
- Planned round-count UI uses `聊天 · N轮` / `工作 · N轮` when enabled, derived from current active-branch user turns without a second mutable counter or new request.

## Authentication evidence

Embedded Google login and default persistent `WKWebsiteDataStore` remain the accepted architecture. `AuthSessionStore` remains the in-memory account-context owner; copied WebKit cookies/session bearer are transient.

The b10 diagnostic export provides concrete cold-start evidence: the default WebKit cookie store is initially `0/0`, `/api/auth/session` returns HTTP 200 but lacks required session fields, and native list auth fails. After a real visible `WKWebView` navigation, the same default store hydrates to dozens of cookies and account verification succeeds. The user wants normal cold-start verification to be background/invisible.

This auth-resume problem is **separate** from recovery. After recovery merges, the next auth experiment must first test public `WKWebsiteDataStore.default()` background data-store warm-up/data-record + cookie-store initialization, then a single existing account probe. No hidden/shadow WebView, persisted copied auth secrets, or retry/watchdog loop. Visible official verification remains fallback only if background warm-up is proven insufficient on device.

## Conversation-read / recovery evidence

### Accepted b9 runtime

- After explicit login verification, production list returned HTTP 200, 28 items / total 29.
- Position 1 / hash `sha256:e95144bf259d`: 1,529,866 bytes, mapping 337, visible 154, 5,668.41 ms.
- Position 13 / hash `sha256:084c1f4870f3`: 7,503,328 bytes, mapping 2023, visible 843, 20,742.89 ms.
- Both were confirmed fully readable on device.

### Accepted b10 recovery runtime

- `同步最新消息` reuses current selected identity and the existing detail endpoint through `ConversationRepository`; failure preserves existing detail and success replaces it with newest server detail.
- `重载当前会话` clears authoritative selected detail first, then rebuilds from the established detail/current-branch path.
- Recovery spans record previous/current visible counts, added/removed/changed counts and local-state transitions while omitting raw conversation IDs/message bodies.
- Exact device export: position 1/hash `sha256:9e133d262e25` sync 3324.49 ms / reload 3212.97 ms; position 8/hash `sha256:c81f9830d5d3` sync 2670.79 ms / reload 3172.36 ms; all `status=ok`.

### b11 feedback implementation

- On manual latest-sync start, the detail navigation prompt shows `正在同步最新消息…`.
- On success, the currently rendered visible messages are compared against returned visible messages by count/id/role/text/createTime.
- No visible change → `已是最新`; any visible change → `已同步最新消息`.
- The result prompt clears after 1.5 seconds only if the same prompt is still present; load/reload clears stale prompts.
- This does not change repository/state/network/auth semantics.
- CI/Artifact/Runtime for b11 remain pending because no exact-head Actions run could be triggered with available tooling.

## Conversation round-count planned semantics

- Work ID: `DEV-conversation-round-count` / **会话轮数显示**.
- Display: `聊天 · N轮` / `工作 · N轮`; `显示会话轮数` defaults On and hides only the count when Off.
- One user message on the **current active branch** equals one round. Assistant/tool/system/reasoning nodes do not add rounds; Regenerate alone does not increment; branch changes recalculate from the selected branch.
- Count is derived from `ConversationRepository`/current active branch, not a separately persisted mutable counter.
- Schedule: after `DEV-conversation-recovery`, before `DEV-send-stream`, unless future conflict scanning proves another order safer.

## Current architecture

- `AppDelegate`: lifecycle/root setup.
- `RootViewController`: production split shell.
- `ConversationRepository`: conversation summaries, selected identity, loaded detail, current visible branch, latest-message sync and full selected-conversation reload semantics.
- `ConversationSidebarViewController`: list presentation plus settings/login/list reload entry points.
- `ConversationDetailViewController`: detail/message presentation and manual recovery UI; consumer of repository state.
- `AuthWebViewController`: login UI/navigation.
- Default `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: account context and short-lived authorized native transport.
- `ProtocolReadProbe`: diagnostic-only.

## Durable development plan

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Completed / merged / Stable.
3. `DEV-protocol-read` — Completed / merged / Stable for tested diagnostic read scope.
4. `DEV-native-read-path` — Completed / merged / Stable for tested b9 scope.
5. `DEV-conversation-recovery` — **Active b11 candidate; b10 core runtime accepted; b11 Code + static review only, CI/Artifact pending**.
6. `DEV-conversation-round-count` — planned serial UI/data-derived task after recovery.
7. `DEV-send-stream`.
8. `DEV-markdown-export`.
9. `DEV-long-conversation`.
10. `DEV-attachments`.
11. Daily-use conversation features.
12. Advanced capabilities.

Core state-owner work remains serialized; parallel edges require normal conflict scanning.

## Known issues / constraints

- No unit/UI test target; automated validation is Release compile, IPA packaging/inspection and artifact upload.
- b11 cannot yet be called CI-passed or Artifact-produced; available connector tooling cannot issue workflow dispatch and connector-originated writes did not emit Actions.
- Cold-start usable-auth persistence/recovery remains Unverified and has concrete 0-cookie evidence; separate auth-resume work is planned after recovery.
- b9's large tested conversation took 20.74 s end-to-end; performance decomposition remains Unverified.
- Send, streaming, attachments, non-personal workspace behavior, lower iOS runtime and iPad runtime remain Unknown / Unverified.

## Evidence rule

Always distinguish Code written, checks/CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
