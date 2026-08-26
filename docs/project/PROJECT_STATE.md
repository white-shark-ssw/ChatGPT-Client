# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

`DEV-app-foundation-0.1.0-b1` remains the merged Stable foundation baseline. `DEV-auth-bootstrap-0.1.0-b6` remains the merged Stable authentication/account-context baseline for the tested iPhone / iOS 17.0 environment.

`DEV-protocol-read-0.1.0-b7`, version `0.1.0 (7)`, remains the merged accepted diagnostic conversation-read protocol evidence baseline for the tested Plus/personal list + one-detail path.

`DEV-native-read-path-0.1.0-b9`, version `0.1.0 (9)`, remains the **merged Stable production native-read baseline for the tested scope**. Exact product/config source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact ID `9610449216`; IPA SHA-256 `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`. It reached **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** for native shell, production list, two distinct selected conversation details, current-branch extraction and visible user/assistant message rendering on iPhone / iOS 17.0. Stable here is scoped acceptance, not Frozen.

`DEV-native-read-path-0.1.0-b8` remains historical partial/failing evidence: shell/list worked after explicit login, but one detail request returned HTTP 500 after 30,935.12 ms before parse/render. b9's two successful distinct detail reads show that b8 failure is not evidence of a systematic current native-read implementation failure.

## Current active candidate

`DEV-conversation-recovery-0.1.0-b10`, version `0.1.0 (10)`, is the active manual conversation-recovery test candidate on `dev/conversation-recovery-20260826` / PR #10. Exact product/config source `89129913cb29a35db9dec7a6d5670d1b3b76bc23`; CI run `32982836557` passed; artifact ID `9612167843`; IPA `ChatGPTClient-0.1.0-b10-dev-conversation-recovery.ipa`; IPA SHA-256 `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`; GitHub ZIP digest `sha256:5a4818f2ea10569092e4144630372d2fecc62a2fcc87d03010ad2116947d224c`.

b10 is **Code written + CI passed + Artifact produced** only. Runtime/manual/real-device behavior is still Unverified and b9 remains the accepted production baseline until b10 is explicitly tested and accepted.

b10 keeps the accepted b9 auth/session/header/endpoint behavior unchanged. `ConversationRepository` remains the sole production selected/detail/current-branch owner and now supplies two explicit manual recovery operations: `同步最新消息` fetches fresh server detail while preserving the previously loaded detail on failure; `重载当前会话` clears the authoritative selected detail before a fresh detail request and rebuild. The conversation overflow exposes both actions, and terminal `重新加载` uses the full-reload operation. No automatic retry/watchdog/timer/resend/fallback path was added.

## Delivery direction

Small real-device milestones remain the delivery model:

- **V0.1 read-use**: official-style native shell + conversation list/detail/message rendering + manual latest-message sync/current-conversation reload. b10 is the first complete Code+CI+Artifact candidate for this loop; real-device acceptance remains pending.
- **V0.2 chat-use**: V0.1 + text send/new conversation + streaming + stop + user-visible reasoning interaction + reasoning-to-final double haptic + manual recovery integration.
- **V0.3 daily-use refinement**: Markdown export, long-conversation tuning, attachments and other daily-use features.

Candidate identity/evidence separation remains mandatory.

## UI / interaction direction

`docs/project/UI_INTERACTION_BASELINE.md` remains authoritative.

- Official ChatGPT iOS interaction is the default where acceptable; use native UIKit/system behavior rather than pixel-perfect copying.
- b9 real-device testing accepted the first production split sidebar/detail read shell for the tested iPhone/iOS 17.0 scope.
- b10 adds loaded-state conversation overflow entries for `同步最新消息` and `重载当前会话`; terminal `重新加载` is routed through the full-reload operation. These interactions are Code+CI+Artifact only until real-device/manual acceptance.
- `同步最新消息` and `重载当前会话` remain explicit user actions; no automatic watchdog/retry/resend chain is accepted.
- Markdown export remains a project enhancement, not official-App evidence.
- Reasoning UI/haptic requirements remain future `DEV-send-stream` work.

## Authentication evidence

- Embedded Google login and default persistent `WKWebsiteDataStore` remain the accepted authentication architecture.
- `AuthSessionStore` remains the in-memory account-context owner; copied WebKit cookies and session bearer are transient only.
- b9 launch again began with 0 total / 0 matched WebKit cookies and `missing_required_session_fields`; after the user explicitly opened login/account verification, WebKit had 48/29 then 49/30 total/matched cookies, Plus/personal account context verified, and production reads succeeded.
- Therefore install/update persistence of usable WebKit authentication remains **Unknown / Unverified**. Do not interpret b9 native-read success or b10 CI success as proof that persistence is fixed.
- No automatic retry, fallback, User-Agent spoof, Cloudflare bypass or hidden/shadow WebView is accepted.

## Conversation-read evidence

### Accepted b7 protocol evidence

- List `GET /backend-api/conversations?offset=0&limit=28&order=updated`: HTTP 200, 28 items / total 29.
- First diagnostic detail: HTTP 200, 13,152,411 bytes, mapping 2068 / message nodes 2067, current node present+mapped, returned identity matched.
- End-to-end diagnostic probe `status=ok` in 13,573.66 ms.

### Production b9 runtime acceptance

- Exact runtime metadata: `DEV-native-read-path-0.1.0-b9`, app `0.1.0`, build 9, source `d9c9b4da8bde`, Release, iPhone, iOS 17.0.
- After explicit login verification, production list returned HTTP 200, 28 items / total 29, 23,624 bytes.
- Distinct conversation list position 1 / `conversationHash=sha256:e95144bf259d`: HTTP 200, 1,529,866 bytes, mapping 337, visible messages 154, `detailLoad status=ok` in 5,668.41 ms.
- Distinct conversation list position 13 / `conversationHash=sha256:084c1f4870f3`: HTTP 200, 7,503,328 bytes, mapping 2023, visible messages 843, `detailLoad status=ok` in 20,742.89 ms.
- The user explicitly confirmed both conversations were fully readable on device.
- These results prove the production repository/list/detail/current-visible-branch/render pipeline for the tested two Plus/personal conversations. They do not prove all content types, all conversations, non-personal workspaces, iPad, lower iOS, send/streaming or attachments.
- The 20.74 s result is end-to-end `detailLoad`; current diagnostics do not decompose network transfer, JSON parsing/branch extraction and UI update time. Treat it as a long-conversation performance input rather than guessing the bottleneck.

### Conversation-recovery b10 candidate evidence

- Exact candidate/package identity: `DEV-conversation-recovery-0.1.0-b10`, app `0.1.0`, build 10, source `89129913cb29`, minimum OS 14.0, arm64.
- CI run `32982836557` completed successfully and produced artifact `9612167843`.
- Artifact inspection independently matched the generated SHA-256 sidecar: `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- `同步最新消息` reuses the current selected identity and existing detail endpoint through `ConversationRepository`; on success the fresh server detail becomes authoritative, while on failure the previous loaded detail remains available.
- `重载当前会话` clears the current authoritative selected detail first, then uses the same established detail request/current-branch parse pipeline to rebuild it.
- Recovery spans record previous/current visible message counts, added/removed/changed counts and local-state transitions. No raw conversation IDs, message bodies or auth secrets are introduced.
- These are implementation/CI/artifact facts, not runtime behavior proof.

## Diagnostics state

Diagnostics/logging remains a Stable foundation capability with bounded persistence, redacted export and explicit clearing. b9's privacy-safe `conversationHash` + 1-based `listPosition` successfully correlated two distinct real-device selections without raw conversation IDs or message bodies. b10 reuses that identity mechanism and adds count/diff/state-transition recovery spans; real-device usefulness of those new events remains pending.

## Current architecture

- `AppDelegate` owns lifecycle/root setup.
- `RootViewController` owns the production split shell.
- `ConversationRepository` owns production conversation summaries, selected identity, loaded detail, current visible branch, latest-message sync and full selected-conversation reload semantics.
- `ConversationSidebarViewController` owns list presentation plus settings/login/list reload entry points.
- `ConversationDetailViewController` owns current detail/message presentation and the manual recovery UI entries; it remains a consumer of repository state.
- `AuthWebViewController` owns login UI/navigation.
- Default `WKWebsiteDataStore` is the sole persistent auth-secret authority.
- `AuthSessionStore` owns account context and creates short-lived authorized native transport.
- `ProtocolReadProbe` remains diagnostic-only.

## Durable development plan

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Completed / merged / Stable.
3. `DEV-protocol-read` — Completed / merged / Stable for tested personal-account diagnostic read scope.
4. `DEV-native-read-path` — **Completed / merged / Stable for tested b9 native-read scope**.
5. `DEV-conversation-recovery` — **Active b10 test candidate; Code + CI + Artifact; real-device/manual acceptance pending**.
6. `DEV-send-stream` — text send/new conversation + streaming + stop + user-visible reasoning UI/detail + reasoning-to-final double haptic + recovery integration.
7. `DEV-markdown-export` — authoritative current-branch Markdown export.
8. `DEV-long-conversation` — measurement-driven long-conversation performance stabilization; b9 7.50 MB / 2023-node / 20.74 s detail is current production evidence.
9. `DEV-attachments` — native attachment/upload flows after text-chat ownership stabilizes.

Core state-owner work remains serialized; parallel edges require normal conflict scanning.

## Compatibility direction

Deployment target remains iOS 14.0; artifacts are arm64 and declare iPhone+iPad families. Current runtime evidence covers iPhone / iOS 17.0. Lower iOS versions and iPad remain unverified. b10 package inspection confirms the deployment floor and arm64 architecture but is not runtime compatibility evidence.

## Known issues / constraints

- No unit/UI test target yet; automated validation remains Release compile, IPA packaging/inspection and artifact upload.
- Install/update auth persistence remains Unverified because b9 again began with 0/0 WebKit cookies until explicit login verification.
- b10 manual `同步最新消息`, loaded-state `重载当前会话`, and terminal full-reload interaction are not yet real-device tested; Code/CI/Artifact success must not be described as runtime acceptance.
- b9's large tested conversation completed successfully but took 20.74 s end-to-end; performance decomposition remains Unverified.
- Send, streaming, attachments, non-personal workspace behavior, lower iOS runtime and iPad runtime remain Unknown / Unverified.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
