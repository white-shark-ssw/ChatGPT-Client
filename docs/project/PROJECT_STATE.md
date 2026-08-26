# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

`DEV-app-foundation-0.1.0-b1` remains the merged Stable foundation baseline. `DEV-auth-bootstrap-0.1.0-b6` remains the merged Stable authentication/account-context baseline for the tested iPhone / iOS 17.0 environment.

`DEV-protocol-read-0.1.0-b7`, version `0.1.0 (7)`, remains the merged accepted conversation-read protocol evidence baseline. It reached **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** for the tested Plus/personal list + one-detail diagnostic read path on iPhone / iOS 17.0.

`DEV-native-read-path-0.1.0-b8` reached real-device testing but failed acceptance: the native shell launched and, after explicit login/account verification, production list GET repeatedly returned HTTP 200 with 28 items / total 29; one selected detail GET returned HTTP 500 after 30,935.12 ms at response stage before payload parse/render. Initial b8 launch observed 0/0 WebKit cookies. b8 therefore remains evidence, not a Stable baseline.

`DEV-native-read-path-0.1.0-b9`, version `0.1.0 (9)`, is the **Active Candidate**. Product/config source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7` passed run `32978476582`; artifact ID `9610449216`; IPA SHA-256 `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; draft PR #9. b9 is **Code written + CI passed + Artifact produced** only; runtime acceptance is pending.

## Delivery direction

The user wants the client usable as early as possible. Small real-device milestones remain the delivery model:

- **V0.1 read-use**: official-style native shell + conversation list/detail/message rendering + manual latest-message sync/current-conversation reload.
- **V0.2 chat-use**: V0.1 + text send/new conversation + streaming + stop + user-visible reasoning interaction + reasoning-to-final double haptic + manual recovery integration.
- **V0.3 daily-use refinement**: Markdown export, long-conversation tuning, attachments and other daily-use features.

Candidate identity/evidence separation remains mandatory.

## UI / interaction direction

`docs/project/UI_INTERACTION_BASELINE.md` remains authoritative.

- Official ChatGPT iOS interaction is the default where acceptable; use native UIKit/system behavior rather than pixel-perfect copying.
- b8/b9 use the first production `UISplitViewController` sidebar/detail shell.
- Direct `重新加载` on terminal detail error is now implemented in b9 as an explicit user action only.
- `同步最新消息` and loaded-state `重载当前会话` remain broader recovery work; no automatic watchdog/retry/resend chain is accepted.
- Markdown export remains a project enhancement, not official-App evidence.
- Reasoning UI/haptic requirements remain future `DEV-send-stream` work.

## Authentication evidence

- Embedded Google login and default persistent `WKWebsiteDataStore` remain the accepted authentication architecture.
- `AuthSessionStore` remains the in-memory account-context owner; copied WebKit cookies and session bearer are transient only.
- b8 production reads reused `AuthSessionStore.probeAccountContext(... createTransientSession: true)` successfully after explicit login verification.
- b8 initial launch had 0 total / 0 matched WebKit cookies. This shows usable auth was absent in that install/run state, but does not by itself prove whether TrollStore replacement cleared the app container or another persistence issue exists.
- No automatic retry, fallback, User-Agent spoof, Cloudflare bypass or hidden/shadow WebView is accepted.

## Conversation-read evidence

### Accepted b7 protocol evidence

- List `GET /backend-api/conversations?offset=0&limit=28&order=updated`: HTTP 200, 28 items / total 29.
- First detail: HTTP 200, 13,152,411 bytes, mapping 2068 / message nodes 2067, current node present+mapped, returned conversation identity matched.
- End-to-end diagnostic probe `status=ok` in 13,573.66 ms.
- This remains accepted only for its exact tested Plus/personal diagnostic scope.

### Production b8 runtime evidence

- Native shell launched on iPhone / iOS 17.0.
- After explicit login/account verification, production list GET repeatedly returned HTTP 200 with 28 items / total 29.
- One selected detail request returned HTTP 500 after 30,935.12 ms at `stage=response`; no `detail.response`, JSON parse, identity-check or render stage was reached.
- Therefore the production repository/list path is partially runtime-proven; detail/message rendering is not accepted.

### Current b9 discrimination candidate

- `ConversationRepository` remains the authoritative production owner for summaries, selected identity, loaded detail and current visible branch.
- b9 adds a privacy-safe SHA-256-derived 12-hex `conversationHash` and 1-based `listPosition` to selection/detail lifecycle diagnostics. Raw conversation IDs/chat bodies are not logged.
- Terminal detail failure shows `重新加载`; one tap performs exactly one user-triggered same-conversation GET through the authoritative repository and logs `conversation.detailReload.requested`.
- b9 changes no endpoint, header, auth or automatic retry behavior.
- Real-device test goal: compare at least two selected conversations and, on a failed detail, one explicit manual reload. Matching/different hash+position and HTTP outcomes will distinguish conversation-specific vs systematic detail failure.

## Diagnostics state

Diagnostics/logging remains a Stable foundation capability with bounded persistence, redacted export and explicit clearing. Conversation diagnostics must continue to avoid raw IDs, chat bodies, payload dumps and auth secrets.

## Current architecture

- `AppDelegate` owns lifecycle/root setup.
- `RootViewController` owns the production split shell.
- `ConversationRepository` owns production conversation summaries, selected identity, loaded detail and current visible branch.
- `ConversationSidebarViewController` owns list presentation plus settings/login/list reload entry points.
- `ConversationDetailViewController` owns current detail/message presentation and b9 terminal manual reload.
- `AuthWebViewController` owns login UI/navigation.
- Default `WKWebsiteDataStore` is the sole persistent auth-secret authority.
- `AuthSessionStore` owns account context and creates short-lived authorized native transport.
- `ProtocolReadProbe` remains diagnostic-only.

## Durable development plan

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Completed / merged / Stable.
3. `DEV-protocol-read` — Completed / merged / Stable for tested personal-account diagnostic read scope.
4. `DEV-native-read-path` — **Active Candidate b9**; production shell/list/detail/read owner. b8 gave partial runtime evidence; b9 awaits detail discrimination testing before merge/Stable.
5. `DEV-conversation-recovery` — broader manual latest-message sync + current-conversation reload.
6. `DEV-send-stream` — text send/new conversation + streaming + stop + user-visible reasoning UI/detail + reasoning-to-final double haptic + recovery integration.
7. `DEV-markdown-export` — authoritative current-branch Markdown export.
8. `DEV-long-conversation` — measurement-driven long-conversation performance stabilization.
9. `DEV-attachments` — native attachment/upload flows after text-chat ownership stabilizes.

Core state-owner work remains serialized; parallel edges require normal conflict scanning.

## Compatibility direction

Deployment target remains iOS 14.0; artifacts are arm64 and declare iPhone+iPad families. Current runtime evidence covers iPhone / iOS 17.0. Lower iOS versions and iPad remain unverified.

## Known issues / constraints

- No unit/UI test target yet; automated validation remains Release compile, IPA packaging/inspection and artifact upload.
- Detail HTTP 500 may be conversation-specific or systematic; b8 cannot distinguish because it lacked a safe selected identity marker. b9 exists specifically to resolve this uncertainty.
- The evidenced 13.15 MB / 2068-node detail remains a real performance input. Parse-time/memory cannot be judged from the b8 500 because no successful payload reached parsing.
- Persistent WebKit auth across install/update remains Unknown / Unverified after b8 began with 0/0 cookies.
- Send, streaming, attachments, non-personal workspace behavior, lower iOS runtime and iPad runtime remain Unknown / Unverified.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
