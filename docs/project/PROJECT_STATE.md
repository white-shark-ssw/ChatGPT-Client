# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

`DEV-app-foundation-0.1.0-b1` remains the merged Stable foundation baseline. `DEV-auth-bootstrap-0.1.0-b6` remains the merged Stable authentication/account-context baseline for the tested iPhone / iOS 17.0 environment.

`DEV-protocol-read-0.1.0-b7`, version `0.1.0 (7)`, is now the merged accepted conversation-read evidence baseline. It reached **Code written + CI passed + Artifact produced + Runtime/manual/real-device tested** for the current Plus/personal conversation-list + one-detail read path on iPhone / iOS 17.0. Exact product/workflow source is `44a137b973e29e2a313e9114fdacb7727dccefb9`; authoritative push run `32938912018`; artifact ID `9595827498`; IPA SHA-256 `64b0cc055bc9da27bc887698ba18ae5cb2cc0fdb9f15a3a59eb09e55c5fcb4ae`. PR #7 merged at `6208102eb3df79a1916b356cc95ff7916ff8f593`.

Production native conversation ownership is intentionally deferred to the next core task, `DEV-native-read-path`.

## Authentication evidence

- Embedded Google login and persistent default `WKWebsiteDataStore` authentication remain accepted.
- `AuthSessionStore` remains the in-memory account-context owner; copied WebKit cookies and session bearer remain transient only.
- Challenge sensitivity remains real. In b7 the first account-context attempt again returned `/api/auth/session` HTTP 403 with 46 total / 27 matched cookies. The user explicitly pressed `重新开始`; the second attempt used 49 / 30 cookies, returned session HTTP 200 + accounts-check HTTP 200, selected the accepted plus/personal context, and ended `status=ok`.
- No automatic retry, fallback, User-Agent spoof or Cloudflare bypass is part of the accepted architecture.

## Accepted conversation-read evidence — b7

- Runtime export metadata exactly matches candidate b7/build 7/source `44a137b973e2`, Release, iPhone / iOS 17.0.
- Request context used the accepted transient bearer + copied ephemeral WebKit cookies; no `chatgpt-account-id` or browser-only header set was required in this tested personal-account run.
- Conversation list `GET /backend-api/conversations?offset=0&limit=28&order=updated` returned HTTP 200, 23,697 bytes, 28 items, total 29, response limit 28 and offset 0.
- First returned conversation detail returned HTTP 200 and 13,152,411 bytes with mappingCount 2068 / messageNodeCount 2067. There was one null-message/root node, three branching nodes, max children 2, six observed content types, and role counts user 22 / assistant 1235 / tool 810 / system 0 / other 0. The role counts sum exactly to all message nodes.
- `current_node` was present and mapped. Returned conversation identity was present and matched the list-selected identity.
- The end-to-end list + detail probe finished `status=ok` in 13,573.66 ms. Current diagnostics do not separate transport time from JSON parse/structural-inspection time.
- User screenshot title `会话列表 · 会话详情通过` agrees with the exported result.

## Diagnostics state

Diagnostics/logging remains a Stable foundation capability with bounded persistence, redacted export and explicit clearing. The b7 export records only safe structural/status/timing/count metadata; no chat bodies, raw conversation/message IDs, Cookie values, bearer values or Authorization values are part of the accepted evidence.

## Current architecture

- `AppDelegate` owns lifecycle/root setup.
- `AppBuildInfo` owns candidate/build/source identity presentation.
- `DiagnosticsLogger` / `DiagnosticsStore` / `DiagnosticsExporter` own diagnostics.
- `AuthWebViewController` owns login UI/navigation and diagnostic sequencing.
- Default `WKWebsiteDataStore` is the sole persistent auth-secret authority.
- `AuthSessionStore` owns current in-memory account context and creates short-lived authorized native transport.
- `ProtocolReadProbe` is an accepted diagnostic-only list/detail probe; it persists no production conversation payload/model/repository.
- `DEV-native-read-path` must establish the production conversation repository, selected-conversation identity and message-tree ownership.

## Durable development plan

1. `DEV-app-foundation` — Completed / merged / Stable.
2. `DEV-auth-bootstrap` — Completed / merged / Stable.
3. `DEV-protocol-read` — Completed / merged / Stable for the tested personal-account read scope.
4. `DEV-native-read-path` — next core task.
5. `DEV-send-stream`.
6. `DEV-long-conversation`.
7. `DEV-attachments`.
8. Daily-use conversation features as separate Work IDs.
9. Advanced capabilities after the core client is stable.

The strongly dependent core remains serialized.

## Compatibility direction

Current deployment target remains iOS 14.0; artifacts are arm64 and declare iPhone+iPad families. Runtime evidence currently covers iPhone / iOS 17.0 only. Lower iOS versions and iPad remain unverified.

## Known issues / constraints

- Bundle ID remains accepted but not Frozen as a permanent signing identity.
- No unit/UI test target yet; automated validation remains Release compile, IPA packaging/inspection and artifact upload.
- Direct `/api/auth/session` can return HTTP 403 under challenge-sensitive conditions; preserve exact failure evidence rather than adding speculative recovery.
- The accepted detail example is large: 13.15 MB / 2068 mapping nodes. This is a real input for native read-path performance/storage/rendering design, but the b7 13.57 s total does not identify which subsystem dominates latency.
- Send, streaming, attachments, non-personal workspace behavior, lower iOS runtime and iPad runtime remain Unknown / Unverified.

## Evidence rule

Always distinguish source written, checks/CI passed, artifact produced, runtime/manual tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
