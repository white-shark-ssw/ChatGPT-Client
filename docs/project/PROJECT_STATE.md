# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone / iOS 17.0 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + one-detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`, version `0.1.0 (9)`: **merged Stable production native-read baseline for tested scope**. Product source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA-256 `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`.

## Current active candidate

`DEV-conversation-recovery-0.1.0-b12`, version `0.1.0 (12)`, is the active recovery candidate on `dev/conversation-recovery-20260826` / PR #10.

- Exact product/config PR head: `fd9fb3ac7a09eafa8dfd33918d114c7d3fee474f`.
- CI run `32993589071`: **success**.
- GitHub synthetic merge used by CI: `4a7380b913ff5bd847c676fceab31adafdeecb3f`.
- Branch head and tested merge share exact tree `81c801284b1e83f68043c30b9c75f47e76640128`.
- Artifact ID `9615588166`; artifact `ChatGPTClient-DEV-conversation-recovery-0.1.0-b12`.
- IPA `ChatGPTClient-0.1.0-b12-dev-conversation-recovery.ipa`.
- IPA SHA-256 `2bd24e1dff89d2c04c82e838b44bf9e584d1587534ab6338b33b23bde0861aab`; generated sidecar matches independently calculated SHA.
- GitHub ZIP digest `sha256:867c256314f7581f5550717287a604f22c6f55ba60ce659638406e5d34082aac`.
- Embedded package identity verified: `0.1.0 (12)`, candidate `DEV-conversation-recovery-0.1.0-b12`, source `4a7380b913ff`, min iOS `14.0`, device families `[1,2]`, Mach-O arm64.
- Validation: **Code written + static/source review + CI passed + Artifact produced**. Runtime/manual/real-device b12 evidence is pending; b12 is not Stable/merged.

### b12 product scope

- Manual latest-sync feedback is now an unmistakable **screen-centered toast** rather than `navigationItem.prompt`.
- Sync progress shows `正在同步最新消息…`; success shows `已是最新` or `已同步最新消息` for 2 seconds.
- `AuthSessionStore` now has a public-API default WebKit data-store warm-up (`WKWebsiteDataStore.default()` + data-record fetch + cookie counts).
- `RootViewController` completes that warm-up before installing the sidebar/detail shell. The sidebar then performs the same single existing account-context probe when its first list load starts.
- Existing auth endpoints, parser, headers, transient-session ownership and default WebKit persistent-secret authority remain unchanged.
- No hidden/shadow WebView, copied persistent token/cookie store, automatic retry/watchdog, resend/regenerate or fallback endpoint path was added.

## Recovery runtime history

### b10 — accepted core recovery behavior

- Source `89129913cb29a35db9dec7a6d5670d1b3b76bc23`; run `32982836557`; artifact `9612167843`; IPA SHA `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- iPhone/iOS 17.0: loaded-state latest-sync and full current-conversation reload worked. Full reload visibly cleared content, showed reload state and rebuilt the same conversation. Diagnostics proved two syncs and two reloads `status=ok`; no resend/duplicate observed.

### b11 — request path accepted, feedback presentation rejected

- Run `32988700796`; artifact `9613806931`; IPA SHA `6c99a2b34ac5312b82930d1eeaeefb2a373e351325c92b7df7ad37a068316b33`.
- Exact b11 export on iPhone/iOS 17.0 proved four latest-sync requests completed `status=ok` with 275 visible messages and zero added/removed/changed messages; one full reload also succeeded.
- User saw no visible sync feedback. The navigation-bar prompt presentation is rejected and superseded by b12's centered toast.
- b11 cold launch still required tapping `登录 / 账户验证`; b11 intentionally did not change auth.

## Cold-start authentication evidence and ownership

Current main governance explicitly assigns cold-start login-state recovery to `DEV-conversation-recovery`; **do not create a separate `DEV-auth-resume` Work**.

Evidence:

- Prior cold launches can expose the default WebKit cookie store as 0/0 and `/api/auth/session` without usable session fields until real WebKit activity hydrates the persistent default store.
- In the b11 export after visible WebKit login navigation, cookie counts were already 47/28 and 49/30; three immediate normal account probes failed at session transport with `NSURLErrorDomain -1005`; a later list-triggered normal probe succeeded with 48/29 cookies, valid session HTTP 200, Plus/personal account context, then list HTTP 200 28/29.
- This does not justify an automatic retry loop. b12 tests only the narrower hypothesis that public default-data-store initialization should happen before the first native probe.
- If b12 background warm-up + one normal probe still fails, preserve diagnostics and keep the existing visible `登录 / 账户验证` UI as explicit fallback. Do not silently navigate a WebView.

## Current architecture

- `AppDelegate`: lifecycle/root setup.
- `RootViewController`: production split shell and b12 cold-start WebKit data-store warm-up sequencing.
- `ConversationRepository`: production conversation summaries, selected identity, loaded detail, current visible branch, latest-message sync and full selected-conversation reload semantics.
- `ConversationSidebarViewController`: list presentation plus settings/login/list reload entry points.
- `ConversationDetailViewController`: detail/message presentation, recovery menu and centered sync feedback.
- `AuthWebViewController`: explicit visible login/verification UI only.
- Default `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: account context, b12 data-store warm-up and short-lived authorized native transport.
- `ProtocolReadProbe`: diagnostic-only.

## Delivery / serial development direction

Latest project planning establishes the post-recovery order:

1. `DEV-conversation-recovery` — **Active b12; Code + static review + CI + Artifact; Runtime pending**. Includes cold-start login-state recovery.
2. `DEV-multi-conversation-state` — planned next to establish stable multi-conversation session/runtime ownership before send/stream.
3. `DEV-conversation-round-count` / preferences integration — after multi-conversation state unless conflict scanning proves otherwise.
4. `DEV-send-stream` — after the state-owner baseline is ready.
5. Markdown export, long-conversation tuning, attachments and remaining daily-use capabilities follow their current dependency plans.

Core state-owner work remains serialized. Parallel edge work requires normal file/state-owner/dependency conflict scanning.

## Known issues / constraints

- No unit/UI test target; automated validation is Release compile, IPA packaging/inspection and artifact upload.
- **b12 cold-start background recovery is not runtime-proven yet.** Code/CI/Artifact does not mean the login issue is solved.
- b12 centered sync toast is also not runtime-proven yet.
- b9's large tested conversation took 20.74 s end-to-end; performance decomposition remains Unverified.
- Send, streaming, multi-conversation runtime ownership, attachments, non-personal workspace behavior, lower iOS runtime and iPad runtime remain Unknown / Unverified as applicable.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. Current user/device evidence outranks older assumptions.
