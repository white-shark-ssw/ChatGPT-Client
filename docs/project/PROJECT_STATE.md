# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone / iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: **merged Stable production native-read baseline for tested scope**. Source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`.

## Current active candidate

`DEV-conversation-recovery-0.1.0-b13`, version `0.1.0 (13)`, is the active recovery candidate on `dev/conversation-recovery-20260826` / PR #10.

- Tested product/config head: `fcc74ac4015449dba6c77f3136eede82cec3ec54`.
- CI run `32997544435`: **success**.
- Synthetic merge: `57187c0d0fd3116f964248a87f1a766268637788`.
- Head/tested merge exact tree: `2068ab4dc8f4bd9f94f1cb89e21b8dab29436ebf`.
- Artifact `9617184873`; IPA `ChatGPTClient-0.1.0-b13-dev-conversation-recovery.ipa`.
- IPA SHA `2af6334278bcb88683cc123d47617e6956c0efb83aceb9b294961827f3e80040`; ZIP digest `sha256:7d7d1faa4e69f8892df2d2c2b944f7ada36cb252c50dd0ddd238ecc05c7baf27`.
- Embedded identity: `0.1.0 (13)`, candidate b13, source `57187c0d0fd3`, min iOS14, arm64.
- All commits after tested product/config head are `docs/project/**` only; current product/config content remains exactly the CI-tested tree.
- Validation: **Code written + static/source review + CI passed + Artifact produced**. Runtime/manual b13 pending; recovery is not Stable/merged.

## b12 real-device result

Exact b12 on iPhone/iOS17 supplied decisive runtime evidence:

- Cold start began with WebKit cookies `0/0`.
- Public `WKWebsiteDataStore.default()` warm-up completed in `194.97 ms`, producing `41/22` total/matched cookies from 7 website-data records.
- The later normal single account probe succeeded without opening Login: session HTTP200, Plus/personal verified; list HTTP200 28/29.
- Therefore the tested b12 cold-start auth hydration path worked. The remaining observed startup defect was not an auth failure.
- `nativeConversationShell.loaded` occurred at `17:43:21Z` but first `listLoad.start` only at `17:45:10Z`; source showed first list load was tied to lazy compact-iPhone sidebar `viewDidLoad`.
- Centered sync feedback is accepted. Runtime exercised unchanged sync (257 ->257, zero diff) and changed sync (562 ->563, +1 visible message).

b12 is **partial runtime acceptance**: auth warm-up + sync feedback accepted; startup/list-navigation sequencing rejected and superseded by b13. TD-017 records the accepted warm-up boundary.

## b13 product scope

- Keep accepted b12 WebKit warm-up unchanged.
- After shell installation, `RootViewController` explicitly loads the sidebar controller so its existing first list request starts immediately rather than waiting for primary-column presentation.
- Detail top-left navigation uses an explicit native sidebar button owned by `RootViewController`; it calls `show(.primary)` directly.
- `同步最新消息` and `重载当前会话` remain enabled while an ordinary selected-conversation detail request is still loading.
- Once one manual recovery action starts, duplicate manual recovery taps are disabled until it ends.
- `ConversationRepository` owns a minimum selected-detail operation generation. A newer manual recovery supersedes an older ordinary detail request; the older completion is discarded as `operation_superseded` instead of overwriting/surfacing stale error over the newer result.
- No automatic retry/timer/watchdog/resend/regenerate, hidden WebView, copied persistent auth store, fallback endpoint or speculative headers were added.

## Current architecture

- `AppDelegate`: lifecycle/root setup.
- `RootViewController`: split shell, accepted WebKit warm-up sequencing, immediate sidebar/list initialization, explicit sidebar presentation action.
- `ConversationRepository`: authoritative production conversation summaries, selected identity/detail/current visible branch, manual recovery semantics and current single-selected-detail freshness generation.
- `ConversationSidebarViewController`: list presentation and existing initial list request owner.
- `ConversationDetailViewController`: detail/messages, recovery menu and centered sync feedback; recovery busy state is presentation/action state only.
- `AuthWebViewController`: explicit visible login/verification fallback only.
- Default `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: account context, public data-store warm-up and transient authorized transport.
- `ProtocolReadProbe`: diagnostic-only.

## Delivery / serialized direction

1. `DEV-conversation-recovery` — **Active b13; Code + static review + CI + Artifact; Runtime pending**.
2. `DEV-multi-conversation-state` — next after recovery acceptance/merge.
3. `DEV-conversation-round-count` / preferences integration.
4. `DEV-send-stream`.
5. Markdown export, long-conversation tuning, attachments and remaining daily-use work.

## Known issues / constraints

- No unit/UI test target; automated validation remains Release compile, IPA packaging/inspection and artifact upload.
- b13 immediate list initiation/sidebar interaction and recovery-during-load remain Runtime Unverified until exact b13 testing.
- b13 freshness generation is intentionally scoped to current single-selected model; multi-conversation Work will later generalize freshness/account scoping.
- b9 large conversation took 20.74 s end-to-end; performance decomposition remains Unverified.
- Send/streaming, multi-conversation residency, attachments, non-personal workspace, lower-iOS runtime and iPad runtime remain Unknown / Unverified as applicable.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. Current user/device evidence outranks older assumptions.