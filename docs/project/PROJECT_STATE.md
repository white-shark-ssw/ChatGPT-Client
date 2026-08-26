# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: **merged Stable production native-read baseline for tested scope**. Source `d9c9b4da8bdecd2d6c097d4db2f3789300fc99c7`; run `32978476582`; artifact `9610449216`; IPA SHA `16168a9db6f03e4ab00ddae4149451563a31fe2862cfb7ab18320329d186b99e`; PR #9 merged at `467ea885d120fa59809c95c914b1ac670d76ee05`.

## Current recovery Work

`DEV-conversation-recovery` remains Active on `dev/conversation-recovery-20260826` / PR #10.

### b14 accepted compact startup/navigation scope

`DEV-conversation-recovery-0.1.0-b14`, version `0.1.0 (14)`:

- Product/config head `82d96bf085dbee3877bcb16e27bbf69f4dc0990f`; tested merge `5b2f60dc8b30ae15d56cbe2d49bbe6b61aff0ad6`; exact tree `4d0ddb24ba6e261cdb7a4057ce47e73f199ad481`.
- CI run `33000566633`: success.
- Artifact `9618410313`; IPA `ChatGPTClient-0.1.0-b14-dev-conversation-recovery.ipa`.
- IPA SHA `b9100deb1d59b8ce22e15e72f766f0313be2903ec96ed2cda3d397986ba89182`; ZIP digest `sha256:d8c489159d0c68f315d5c9f9c7920cf6349ab76214c740e07cc30d99fbbbeccf`.
- User tested exact b14 on iPhone/iOS17 and reported the stated b14 gate had no issues.
- Runtime/manual accepted scope: cold start lands on the conversation-list root instead of blank `新对话` detail, duplicate sidebar icons are gone, and native compact list/detail navigation is usable.
- b14 therefore reached **Code + static/source review + CI + Artifact + Runtime/manual accepted for compact startup/navigation**.

Recovery is still **not Stable / not merged** because b13 exposed one unresolved selected-detail replacement lifecycle defect that b14 intentionally did not modify.

## Recovery runtime history

### b12 — accepted warm-up + feedback, startup sequencing rejected

- Public `WKWebsiteDataStore.default()` warm-up restored 0/0 -> 41/22 cookies in `194.97 ms`; unchanged account/list path later succeeded without opening Login.
- Centered sync feedback is accepted.
- Initial list request still waited for lazy compact primary/sidebar loading, so startup sequencing was rejected.

### b13 — list initiation/freshness accepted, compact navigation failed, overlap defect exposed

- Cold launch warm-up 0/0 -> 39/20 in `177.47 ms`.
- `listLoad.start` occurred immediately after warm-up; account context took `17089.96 ms`; whole list load `22005.52 ms`; list HTTP200 28/29.
- Compact startup stayed on secondary `新对话`, duplicate sidebar icons appeared, and custom sidebar reveal was unreliable.
- Recovery actions were available during ordinary detail load.
- Selected-detail generation rejected an older successful completion as `operation_superseded`.
- While ordinary detail remained in flight, manual reload replacement requests returned HTTP429. The generation guard protects state freshness but the old network task is still left active.

## Remaining correction inside `DEV-conversation-recovery`

The next recovery correction remains part of the **same Work**, not a new Work ID, because it directly belongs to the same `ConversationRepository` manual-recovery owner and was exposed by this Work's recovery-during-load contract.

Required direction:

- when explicit manual sync/reload replaces an in-flight selected-detail request, cancel/replace the older selected-detail network task before issuing the replacement;
- retain operation-generation stale-result rejection for late callbacks;
- no retry/timer/watchdog/fallback/resend/regenerate or second state authority;
- allocate a fresh unique candidate/build identity only after rechecking current main, PR #10, all Active checkpoints and `BUILD_TEST_INDEX.md`; do not reuse b14.

## Current architecture

- `AppDelegate`: lifecycle plus accepted b14 sequencing of WebKit warm-up before product-root installation.
- `RootViewController`: synchronously built split shell; native compact primary/list startup and list/detail navigation owner.
- `ConversationRepository`: authoritative conversation summaries, selected identity/detail/current visible branch, manual recovery semantics and selected-detail freshness generation; next correction will remain here as request-lifecycle ownership.
- `ConversationSidebarViewController`: list presentation/initial list request.
- `ConversationDetailViewController`: detail/messages, recovery menu and centered sync feedback.
- Default `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: account context, accepted public data-store warm-up and transient authorized transport.

## Delivery / serialized direction

1. `DEV-conversation-recovery` — **Active; b14 compact shell accepted; selected-detail cancellation/replacement correction pending in the same Work**.
2. `DEV-multi-conversation-state` — only after recovery acceptance/merge.
3. `DEV-conversation-round-count` / preferences integration.
4. `DEV-send-stream`.
5. Markdown export, long-conversation tuning, attachments and remaining daily-use work.

## Known issues / constraints

- No unit/UI test target; automated validation remains Release compile, IPA packaging/inspection and artifact upload.
- The b13 selected-detail replacement overlap/HTTP429 remains unresolved until a fresh candidate is implemented and real-device tested.
- Current generation guard is intentionally single-selected; future multi-conversation Work will generalize freshness/account scoping.
- Long account/list/detail times are observed end-to-end signals, not proof of one bottleneck.
- Send/streaming, multi-conversation residency, attachments, non-personal workspace, lower-iOS runtime and iPad runtime remain Unknown / Unverified as applicable.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. Current user/device evidence outranks older assumptions.
