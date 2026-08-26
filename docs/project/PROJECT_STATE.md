# Project State

_Last updated: 2026-08-26._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone / iOS 17.0 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + one-detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`, version `0.1.0 (9)`: **merged Stable production native-read baseline for tested scope**. Product source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA-256 `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`.

## Current active candidate

`DEV-conversation-recovery-0.1.0-b11`, version `0.1.0 (11)`, is the active final recovery UX candidate on `dev/conversation-recovery-20260826` / PR #10.

- Final CI run: **`32988700796` success**.
- PR head tested: `c3490eb67f8d8218281b30560a5c20b3d846c931` through GitHub synthetic merge `7fe8ca7693e9e8daa5fa80c9b8c600215e443cf3`.
- Branch head and tested merge have the same tree SHA: **`80cd8e60977bbcc8dc2dc83881a58afb29a51bde`**. This proves the CI tested the same source/config content as the branch head.
- Artifact ID: **`9613806931`**; artifact name `ChatGPTClient-DEV-conversation-recovery-0.1.0-b11`.
- IPA: `ChatGPTClient-0.1.0-b11-dev-conversation-recovery.ipa`.
- IPA SHA-256: **`6c99a2b34ac5312b82930d1eeaeefb2a373e351325c92b7df7ad37a068316b33`**; sidecar matches independently calculated SHA.
- GitHub ZIP digest: `sha256:70bb214d01bcf7f2a57df25f10c2280f5dce5482d06b545a168b4963f3b2ee2f`.
- Embedded identity verified: `0.1.0 (11)`, candidate `DEV-conversation-recovery-0.1.0-b11`, source `7fe8ca7693e9`, minimum OS `14.0`, device families `[1,2]`, Mach-O arm64.
- Validation: **Code written + static/source diff reviewed + CI passed + Artifact produced**. Runtime/manual b11 feedback confirmation remains pending, so b11 is not Stable/merged yet.
- b11 product behavior only adds non-blocking manual latest-sync feedback: `正在同步最新消息…` then `已是最新` or `已同步最新消息`. Repository/network/auth/recovery semantics remain unchanged.

Intermediate run `32987959118` is rejected as final b11 evidence: it checked out `512a2c...` before final build-number/workflow metadata and produced an inconsistent identity (`CFBundleVersion=10`, candidate b11, artifact named b10). Do not distribute/reuse that artifact.

## Accepted b10 runtime inside the same Work

`DEV-conversation-recovery-0.1.0-b10` remains the accepted core recovery runtime evidence while b11 closes the feedback UX gap.

- Source `89129913cb29a35db9dec7a6d5670d1b3b76bc23`; CI run `32982836557` passed; artifact `9612167843`; IPA SHA-256 `6e600f829fa24cdeb705e9ab104ebb780a8c70dd06871285d06fa30521aecb7e`.
- User tested exact b10 on iPhone / iOS 17.0 and reported no functional recovery problems.
- Full reload visibly cleared the content, showed the reload state, then rebuilt the same conversation.
- Diagnostics confirm two loaded-state latest-syncs and two full reloads all completed `status=ok`; both syncs had zero visible differences. No resend/duplicate observed.

## Delivery direction

- **V0.1 read-use**: native shell + list/detail/message rendering + manual latest-message sync/current-conversation reload. Core recovery runtime is accepted on b10; b11 now has Code+CI+Artifact and needs only the quick feedback UI device check before final merge.
- **V0.2 chat-use**: V0.1 + send/new conversation + streaming + stop + visible reasoning interaction + reasoning-to-final haptics + recovery integration.
- **V0.3 daily-use refinement**: Markdown export, long-conversation tuning, attachments and other daily-use features.

`DEV-conversation-round-count` remains planned serially after recovery unless the latest conflict scan changes ordering.

## Authentication evidence / next separate problem

Embedded Google login and default persistent `WKWebsiteDataStore` remain the accepted architecture. `AuthSessionStore` remains the in-memory account-context owner; copied WebKit cookies/session bearer are transient.

b10 diagnostics give concrete cold-start evidence: default WebKit cookie store starts `0/0`; `/api/auth/session` returns HTTP 200 but lacks required session fields; after a real visible `WKWebView` navigation, the same default store hydrates to dozens of cookies and account verification succeeds. User requires normal cold-start recovery to be background/invisible.

This auth-resume work is separate from recovery. After recovery completes, the first experiment must test public `WKWebsiteDataStore.default()` background data-store warm-up/data-record + cookie-store initialization followed by one normal account probe. No hidden/shadow WebView, no persisted copied Cookie/token/session secrets, no retry/watchdog loop. Visible official verification is fallback only if background warm-up is proven insufficient.

## Current architecture

- `AppDelegate`: lifecycle/root setup.
- `RootViewController`: production split shell.
- `ConversationRepository`: production conversation summaries, selected identity, loaded detail, current visible branch, latest-message sync and full selected-conversation reload semantics.
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
5. `DEV-conversation-recovery` — **Active b11; Code + static review + CI + Artifact; runtime feedback check pending**.
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
- b11 feedback UI still needs one quick real-device confirmation before recovery can be called Stable/merged.
- Cold-start usable-auth persistence/recovery remains Unverified with concrete 0-cookie evidence; separate auth-resume work is planned after recovery.
- b9's large tested conversation took 20.74 s end-to-end; performance decomposition remains Unverified.
- Send, streaming, attachments, non-personal workspace behavior, lower iOS runtime and iPad runtime remain Unknown / Unverified.

## Evidence rule

Always distinguish Code written, checks/CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. Current real-device evidence outranks historical assumptions.
