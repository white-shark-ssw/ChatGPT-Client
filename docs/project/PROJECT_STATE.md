# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone / iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: **merged Stable production native-read baseline for tested scope**. Source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`.

## Current active candidate

`DEV-conversation-recovery-0.1.0-b14`, version `0.1.0 (14)`, is the active recovery candidate on `dev/conversation-recovery-20260826` / PR #10.

- Product/config head: `82d96bf085dbee3877bcb16e27bbf69f4dc0990f`.
- CI run `33000566633`: **success**.
- Synthetic merge: `5b2f60dc8b30ae15d56cbe2d49bbe6b61aff0ad6`.
- Head/tested merge exact tree: `4d0ddb24ba6e261cdb7a4057ce47e73f199ad481`.
- Artifact `9618410313`; IPA `ChatGPTClient-0.1.0-b14-dev-conversation-recovery.ipa`.
- IPA SHA `b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`; ZIP digest `sha256:d8c489159d0c68f315d5c9f9c7920cf6349ab76214c740e07cc30d99fbbbeccf`.
- Embedded identity: `0.1.0 (14)`, candidate b14, source `5b2f60dc8b30`, min iOS14, device families `[1,2]`, Mach-O arm64.
- Validation: **Code written + static/source review + CI passed + Artifact produced**. Runtime/manual b14 pending; recovery is not Stable/merged.

## Recovery runtime history

### b12 — accepted warm-up + feedback, startup sequencing rejected

- Public `WKWebsiteDataStore.default()` warm-up on one tested cold start restored 0/0 -> 41/22 cookies in `194.97 ms`; unchanged account/list path later succeeded without opening Login.
- Centered sync feedback is accepted, including unchanged and changed sync results.
- Initial list request still waited for lazy compact-iPhone primary/sidebar loading, so startup sequencing was rejected.

### b13 — list initiation fixed, compact navigation failed

Exact b13 iPhone/iOS17 recording + diagnostics prove:

- Cold launch warm-up 0/0 -> 39/20 in `177.47 ms`.
- `listLoad.start` occurred immediately after warm-up, so the prior delayed-list-initiation defect is fixed.
- Account context took `17089.96 ms`; whole list load took `22005.52 ms`; list HTTP200 28/29.
- User still spent close to a minute trying to reach the list. Initial screen was the secondary `新对话 / 从侧边栏选择一个会话` placeholder, and repeated custom sidebar taps often failed to reveal primary.
- Recording showed two identical top-left sidebar icons because b13 combined UISplitViewController compact navigation with a custom `sidebar.left` button.
- Recovery actions were available during ordinary detail load.
- Freshness generation worked: an older successful detail completion was discarded as `operation_superseded`.
- Separate defect exposed: while ordinary detail generation 1 remained in flight, manual reload generations 2/3 returned HTTP429 in about 1.1 s. Current generation protection prevents stale mutation but does not cancel the replaced network task.

b13 is therefore **Code + CI + Artifact + Runtime/manual tested, partial/failing**.

## b14 product scope

b14 isolates the compact shell/navigation correction:

- `AppDelegate` completes the already accepted public WebKit data-store warm-up before installing the product `RootViewController`.
- `RootViewController` constructs primary/sidebar and secondary/detail columns synchronously before first presentation.
- When no conversation is selected, `UISplitViewControllerDelegate` chooses `.primary` as the compact top column, so the initial product screen should be the conversation list rather than the blank detail placeholder.
- The b13 custom `sidebar.left` button and custom `show(.primary)` action are removed. Native UISplitViewController/navigation is the single compact navigation owner.
- Selecting a conversation still calls `show(.secondary)`; native compact navigation/back is expected to return to the list.
- Sidebar's existing first list load is naturally sequenced after warm-up because the entire root shell is installed only after warm-up completes.
- Auth endpoints/parser/headers, conversation list/detail routes, centered sync feedback and generation guard are unchanged.

## Current architecture

- `AppDelegate`: launch/lifecycle plus b14 sequencing of accepted WebKit warm-up before product-root installation.
- `RootViewController`: synchronously built split shell; native compact primary/list startup and list/detail navigation owner.
- `ConversationRepository`: authoritative production conversation summaries, selected identity/detail/current visible branch, manual recovery semantics and current single-selected-detail freshness generation.
- `ConversationSidebarViewController`: list presentation and existing initial list request owner.
- `ConversationDetailViewController`: detail/messages, recovery menu and centered sync feedback.
- `AuthWebViewController`: explicit visible login/verification fallback only.
- Default `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: account context, accepted public data-store warm-up and transient authorized transport.
- `ProtocolReadProbe`: diagnostic-only.

## Delivery / serialized direction

1. `DEV-conversation-recovery` — **Active b14; Code + static review + CI + Artifact; Runtime pending**.
2. Inside the same Work, the b13 manual-replacement HTTP429 overlap remains pending and requires a fresh candidate if corrected after b14 UI acceptance.
3. `DEV-multi-conversation-state` — after recovery acceptance/merge.
4. `DEV-conversation-round-count` / preferences integration.
5. `DEV-send-stream`.
6. Markdown export, long-conversation tuning, attachments and remaining daily-use work.

## Known issues / constraints

- No unit/UI test target; automated validation remains Release compile, IPA packaging/inspection and artifact upload.
- b14 compact startup/list-detail navigation is Runtime Unverified until exact b14 real-device testing.
- b14 **does not** fix b13's concurrent selected-detail replacement HTTP429; do not call that defect solved.
- Current generation guard is intentionally scoped to single-selected conversation state; future multi-conversation Work will generalize freshness/account scoping.
- Long account/list/detail times remain observed end-to-end performance signals, not proof of one bottleneck.
- Send/streaming, multi-conversation residency, attachments, non-personal workspace, lower-iOS runtime and iPad runtime remain Unknown / Unverified as applicable.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. Current user/device evidence outranks older assumptions.