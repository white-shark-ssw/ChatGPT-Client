# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: **merged Stable production native-read baseline for tested scope**. Source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`.

## Current recovery Work

`DEV-conversation-recovery` remains Active on `dev/conversation-recovery-20260826` / PR #10.

### b14 accepted runtime scope

`DEV-conversation-recovery-0.1.0-b14`, `0.1.0 (14)`, reached Code + static/source review + CI + Artifact + Runtime/manual acceptance for compact startup/navigation on the target iPhone/iOS17:

- product/config head `82d96bf085dbee3877bcb16e27bbf69f4dc0990f`;
- run `33000566633`; artifact `9618410313`;
- IPA SHA `b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`;
- cold start lands on the conversation-list root, duplicate sidebar controls are gone, and native compact list/detail navigation is usable.

### Current b15 test candidate

`DEV-conversation-recovery-0.1.0-b15`, version `0.1.0 (15)`, is the active candidate for the remaining selected-detail replacement lifecycle defect.

- Product/config head `159e8ea4f7baf6cd890d1f9bbebeac41feefbf52`.
- CI run `33004536664`: **success**.
- Synthetic merge `fb0c6d75362e111758b62a98f89696b7f1cb6c92`.
- Head/tested merge exact tree `7a988bcad27d023eac77683985c5d7d92b22c176`.
- Artifact `9619988065`; IPA `ChatGPTClient-0.1.0-b15-dev-conversation-recovery.ipa`.
- IPA SHA `b2b54905cff2b67604f95d44033efd6b4b98d319b311ac06204ddec359dd905e`; ZIP digest `sha256:cf4e8bce5a80bdd86bd9b8457b86c7a41de65d762c6ee158422760538faa50a7`.
- Embedded identity: `0.1.0 (15)`, candidate b15, source `fb0c6d75362e`, min iOS14.0, device families `[1,2]`, Mach-O arm64.
- Validation: **Code written + static/source review + CI passed + Artifact produced; Runtime/manual pending**.

## b15 product scope

b13 runtime proved the current freshness guard protects state but not the network lifecycle: an old selected-detail request remained active while manual replacement requests started and those replacement requests returned HTTP429.

b15 makes the minimum owner-level correction:

- `AuthTransientSession.dataTask(with:completion:)` returns the same `URLSessionDataTask` it already creates/resumes; auth/header/cookie/endpoint semantics are unchanged.
- `ConversationRepository` tracks the current selected-detail task and its operation generation.
- Ordinary detail loads keep existing behavior by default.
- Explicit `同步最新消息` / `重载当前会话` take ownership of a new generation, cancel the older tracked selected-detail task, then start the replacement detail request.
- Intentional `NSURLErrorCancelled` is recorded as `detail.cancelled` rather than surfaced as a network failure.
- Existing operation-generation stale-result rejection remains for late callbacks.
- No retry/timer/watchdog/fallback/resend/regenerate, hidden WebView or second conversation-state authority was added.

The implementation is built and packaged, but **the b13 HTTP429 overlap defect is not yet Runtime-resolved** until exact b15 device evidence shows the cancellation/replacement sequence and successful replacement request.

## Current architecture

- `AppDelegate`: lifecycle plus accepted b14 WebKit warm-up-before-root sequencing.
- `RootViewController`: synchronously built split shell; native compact list/detail navigation owner.
- `ConversationRepository`: authoritative conversation summaries, selected identity/detail/current visible branch, manual recovery semantics, operation generation and b15 selected-detail request lifecycle handle.
- `ConversationSidebarViewController`: list presentation/initial list request.
- `ConversationDetailViewController`: detail/messages, recovery menu and centered sync feedback.
- Default `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: account context, accepted public warm-up and transient authorized transport; b15 only exposes an already-created transient task handle.

## Delivery / serialized direction

1. `DEV-conversation-recovery` — **Active b15; Code + static/source review + CI + Artifact; Runtime pending**.
2. `DEV-multi-conversation-state` — only after recovery acceptance/merge.
3. `DEV-conversation-round-count` / preferences integration.
4. `DEV-send-stream`.
5. Markdown export, long-conversation tuning, attachments and remaining daily-use work.

## Current b15 runtime gate

- During ordinary `正在读取会话…`, invoke one manual sync or reload.
- Diagnostics should show old generation cancellation and one replacement detail request.
- The client must not intentionally keep old and replacement selected-detail requests active concurrently.
- Verify replacement completes without reproducing the b13 overlap-driven HTTP429 in the tested case.
- Confirm accepted centered sync feedback/full reload and b14 compact navigation remain intact.

## Known issues / constraints

- No unit/UI test target; automated validation remains Release compile, IPA packaging/inspection and artifact upload.
- b15 runtime behavior is Unverified until exact real-device testing.
- Current generation/task lifecycle is intentionally single-selected; future multi-conversation Work will generalize freshness/account scoping.
- Long account/list/detail times remain end-to-end signals, not proof of one bottleneck.
- Send/streaming, multi-conversation residency, attachments, non-personal workspace, lower-iOS runtime and iPad runtime remain Unknown / Unverified as applicable.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. Current user/device evidence outranks older assumptions.
