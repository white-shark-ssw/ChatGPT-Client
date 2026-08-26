# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

`DEV-app-foundation-0.1.0-b1` remains the merged Stable foundation baseline. `DEV-auth-bootstrap-0.1.0-b6` remains the merged Stable authentication/account-context baseline for the tested iPhone / iOS 17.0 environment.

`DEV-protocol-read-0.1.0-b7`, version `0.1.0 (7)`, remains the merged accepted conversation-read evidence baseline. It reached **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** for the current Plus/personal conversation-list + one-detail read path on iPhone / iOS 17.0. Exact product/workflow source is `44a137b973e29e2a313e9114fdacb7727dccefb9`; authoritative push run `32938912018`; artifact ID `9595827498`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`. PR #7 merged at `6208102eb3df79a1916b356cc95ff7916ff8f593`.

`DEV-native-read-path-0.1.0-b8`, version `0.1.0 (8)`, is now the **Active Candidate** for the production native read path. Source `e312acc3dd17cdcdb01746bb76f70556510a0304` passed Release build, IPA inspection and artifact upload in run `32976656499`; artifact ID `9609766005`; IPA SHA-256 `50bfb7453443c41de8661c1ffc3e2a7076fd939fe62453aceacb599371862acd`; draft PR #9. This is **Code written + CI passed + Artifact produced only**. Runtime/manual/real-device acceptance is pending, so b8 is not Stable/Frozen and does not supersede b7 runtime evidence yet.

## Delivery direction

The user wants the client usable as early as possible. The current roadmap therefore uses small real-device milestones rather than waiting for roadmap completeness:

- **V0.1 read-use**: official-style native shell + conversation list/detail/message rendering + manual latest-message sync/current-conversation reload.
- **V0.2 chat-use**: V0.1 + text send/new conversation + streaming + stop + user-visible reasoning interaction + reasoning-to-final double haptic + manual recovery integration.
- **V0.3 daily-use refinement**: Markdown export, long-conversation tuning, attachments and other daily-use features.

Each candidate still requires unique build/artifact identity and explicit evidence labels. This delivery priority changes sequencing, not validation rigor.

## UI / interaction direction

`docs/project/UI_INTERACTION_BASELINE.md` remains the durable interaction baseline.

- Official ChatGPT iOS interaction is the default where acceptable; do not invent a separate UI language merely to be different.
- b8 implements the first UIKit split sidebar/detail shell and compact-width system collapse path. Exact iPhone feel remains real-device acceptance work.
- Explicit project enhancements include manual `同步最新消息`, manual `重载当前会话`, Markdown export and diagnostics/support surfaces.
- `导出 Markdown` visible in the user's reference recording came from the user's injected dylib and is not official-App behavior.
- User-visible reasoning should eventually reproduce the observed official-style gray shimmer/status + tap-to-expand detail behavior when the protocol supplies such user-visible content.
- The user explicitly requires two short haptic pulses on the real-time reasoning -> final-answer transition; exact intensity/spacing remains real-device tuning work, not yet implementation evidence.

## Authentication evidence

- Embedded Google login and persistent default `WKWebsiteDataStore` authentication remain accepted.
- `AuthSessionStore` remains the in-memory account-context owner; copied WebKit cookies and session bearer remain transient only.
- b8 production reads reuse `AuthSessionStore.probeAccountContext(... createTransientSession: true)` and the default WebKit cookie store instead of creating a second persistent auth authority or hidden/shadow WebView.
- Challenge sensitivity remains real. No automatic retry, fallback, User-Agent spoof or Cloudflare bypass is part of the accepted architecture.

## Accepted conversation-read evidence — b7

- Runtime export metadata exactly matches candidate b7/build 7/source `44a137b973e2`, Release, iPhone / iOS 17.0.
- Request context used the accepted transient bearer + copied ephemeral WebKit cookies; no `chatgpt-account-id` or browser-only header set was required in this tested personal-account run.
- Conversation list `GET /backend-api/conversations?offset=0&limit=28&order=updated` returned HTTP 200, 23,697 bytes, 28 items, total 29, response limit 28 and offset 0.
- First returned conversation detail returned HTTP 200 and 13,152,411 bytes with mappingCount 2068 / messageNodeCount 2067. There was one null-message/root node, three branching nodes, max children 2, six observed content types, and role counts user 22 / assistant 1235 / tool 810 / system 0 / other 0. The role counts sum exactly to all message nodes.
- `current_node` was present and mapped. Returned conversation identity was present and matched the list-selected identity.
- The end-to-end list + detail probe finished `status=ok` in 13,573.66 ms. Current diagnostics do not separate transport time from JSON parse/structural-inspection time.
- User screenshot title `会话列表 · 会话详情通过` agrees with the exported result.

## Native conversation candidate — b8

- `ConversationRepository` is now the production owner for conversation summaries, selected conversation identity, loaded detail and current visible branch messages.
- `ProtocolReadProbe` remains diagnostic-only and was not repurposed into production state.
- Native list reads use the accepted b7 list route and detail reads use `/backend-api/conversation/{id}` with returned conversation identity checking when present.
- The visible branch is extracted by walking `current_node -> parent`, then rendering user/assistant text only. Tool/system/unsupported/non-text content is not guessed into visible chat semantics.
- Detail UI uses table-view reuse/virtualization rather than mounting the full mapping tree. The 13.15 MB / 2068-node b7 sample still requires runtime memory/latency acceptance because b8 currently parses the full JSON payload with `JSONSerialization` before branch extraction.
- First b8 CI source `5b4b35287d31b0cf94e74ae927b912255a87ae2c` failed compile on message-cell constraint switching and produced no artifact. The minimal fix at `e312acc3dd17cdcdb01746bb76f70556510a0304` passed run `32976656499` and produced the authoritative b8 artifact.

## Manual recovery requirements

These remain explicit user-requested future features, not yet implemented/runtime validated by b8.

- **`同步最新消息`**: fetch current server conversation detail and reconcile through the authoritative production conversation owner when local thinking/stream state may lag server completion. It never resends/regenerates.
- **`重载当前会话`**: re-request/rebuild the current conversation after load timeout/failure/blank/spinning/unusable state; direct `重新加载` should appear in terminal load-error UI. It never resends existing messages.
- Both remain manual recovery actions. No automatic watchdog/retry/resend chain is accepted.

## Diagnostics state

Diagnostics/logging remains a Stable foundation capability with bounded persistence, redacted export and explicit clearing. b8 lifecycle diagnostics record route/status/timing/byte/count evidence without chat bodies, raw conversation/message IDs, Cookie values, bearer values or Authorization values.

Future recovery/stream work should record safe lifecycle, status, timing, count/diff and terminal evidence sufficient to distinguish server-state, local-store/merge and render problems without logging chat bodies or secrets.

## Current architecture

- `AppDelegate` owns lifecycle/root setup and now launches the production native shell directly.
- `RootViewController` is the b8 `UISplitViewController` shell that connects sidebar selection to the detail surface.
- `ConversationRepository` owns production conversation summaries, selected conversation identity, loaded detail and current visible branch messages.
- `ConversationSidebarViewController` owns list presentation plus explicit settings/login/reload entry points.
- `ConversationDetailViewController` and reusable message cells own current visible message presentation.
- `AppBuildInfo` owns candidate/build/source identity presentation.
- `DiagnosticsLogger` / `DiagnosticsStore` / `DiagnosticsExporter` own diagnostics.
- `AuthWebViewController` owns login UI/navigation and diagnostic sequencing.
- Default `WKWebsiteDataStore` is the sole persistent auth-secret authority.
- `AuthSessionStore` owns current in-memory account context and creates short-lived authorized native transport.
- `ProtocolReadProbe` remains the accepted diagnostic-only list/detail probe; it persists no production conversation payload/model/repository.

## Durable development plan

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Completed / merged / Stable.
3. `DEV-protocol-read` — Completed / merged / Stable for the tested personal-account read scope.
4. `DEV-native-read-path` — **Active Candidate b8**; official App UI main shell + native conversation list/detail/read ownership; Code + CI + Artifact, awaiting iPhone/iOS 17.0 real-device acceptance before merge/Stable.
5. `DEV-conversation-recovery` — manual latest-message sync + current-conversation reload; complete V0.1 recovery loop.
6. `DEV-send-stream` — text send/new conversation + streaming + stop + user-visible reasoning UI/detail + reasoning-to-final double haptic + recovery integration; earliest V0.2 daily-chat candidate.
7. `DEV-markdown-export` — authoritative current-branch Markdown export; may become a safe parallel edge after the production conversation model is stable.
8. `DEV-long-conversation` — measurement-driven long-conversation performance stabilization.
9. `DEV-attachments` — native attachment/upload flows after text-chat state ownership is stable.
10. Daily-use conversation features as separate Work IDs.
11. Advanced capabilities only after the core daily client is usable/stable enough; they must not block V0.1/V0.2.

The core state-owner chain remains serialized. Low-overlap edges may parallelize only after normal conflict scanning and stable shared contracts.

## Compatibility direction

Current deployment target remains iOS 14.0; artifacts are arm64 and declare iPhone+iPad families. Accepted runtime evidence currently covers iPhone / iOS 17.0 through b7; b8 runtime remains unverified. Lower iOS versions and iPad remain unverified.

## Known issues / constraints

- Bundle ID remains accepted but not Frozen as a permanent signing identity.
- No unit/UI test target yet; automated validation remains Release compile, IPA packaging/inspection and artifact upload.
- Direct `/api/auth/session` can return HTTP 403 under challenge-sensitive conditions; preserve exact failure evidence rather than adding speculative recovery.
- The accepted detail example is large: 13.15 MB / 2068 mapping nodes. b8 bounds view materialization but still needs real-device parse/memory/latency evidence.
- b8 currently exposes only simple visible user/assistant text shapes; unsupported visible content types remain Unknown / Unverified rather than guessed.
- Send, streaming, attachments, non-personal workspace behavior, lower iOS runtime and iPad runtime remain Unknown / Unverified.
- Exact current send/stream/reasoning event protocol is still Unknown / Unverified. UI requirements do not make protocol assumptions factual.
- Exact two-pulse haptic implementation/intensity/spacing is not yet runtime validated in this client.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
