# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: **merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope**. PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.

## Recovery completion

Final candidate: `DEV-conversation-recovery-0.1.0-b15`, version `0.1.0 (15)`.

- Product/config head `159e8ea4f7baf6cd890d1f9bbebeac41feefbf52`.
- Tested synthetic merge `fb0c6d75362e111758b62a98f89696b7f1cb6c92`.
- Exact tested product/config tree `7a988bcad27d023eac77683985c5d7d92b22c176`.
- CI run `33004536664`: success.
- Artifact `9619988065`; IPA `ChatGPTClient-0.1.0-b15-dev-conversation-recovery.ipa`.
- IPA SHA `b2b54905cff2b67604f95d44033efd6b4b98d319b311ac06204ddec359dd905e`; ZIP digest `sha256:cf4e8bce5a80bdd86bd9b8457b86c7a41de65d762c6ee158422760538faa50a7`.
- Embedded identity: `0.1.0 (15)`, candidate b15, source `fb0c6d75362e`, min iOS14.0, arm64.
- Validation: **Code + static/source review + CI + Artifact + Runtime/manual/real-device accepted**.

## Accepted recovery behavior

- `同步最新消息` and full `重载当前会话` operate through authoritative `ConversationRepository`; no resend/regenerate.
- Centered sync feedback is accepted: syncing indicator plus final `已是最新` / `已同步最新消息` result.
- Public `WKWebsiteDataStore.default()` warm-up is accepted for tested persisted cold-start login hydration; no hidden WebView or second persistent credential store.
- Compact iPhone startup lands on the conversation list; duplicate sidebar controls are removed; native list/detail navigation is the single owner.
- Manual recovery remains available during ordinary detail loading.
- A newer manual recovery takes ownership of a new selected-detail generation, cancels the older tracked `URLSessionDataTask`, then starts one replacement request.
- Existing operation-generation stale-result rejection remains for late callbacks.
- Intentional cancellation is recorded as cancellation rather than surfaced as a network failure.
- No automatic retry/timer/watchdog/fallback/resend/regenerate chain was added.

## Final b15 runtime evidence

Two independent real-device replacement cases were accepted:

1. Generation 1 -> 2 manual reload: generation 1 ended `cancelled` after 2451.99 ms; generation 2 returned HTTP200, 168 visible messages, and reload ended `ok` after 3862.17 ms.
2. Generation 3 -> 4 manual latest-sync: generation 3 ended `cancelled` after 2352.66 ms; generation 4 returned HTTP200, 591 visible messages, and latest-sync ended `ok` after 5368.57 ms.
3. No HTTP429 appeared in either accepted sequence.
4. User explicitly reported exact b15 had no issues.

The b13 overlapping-request HTTP429 defect is therefore resolved for the tested b15 scope.

## Current architecture

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: synchronously built split shell; native compact list/detail navigation owner.
- `ConversationRepository`: authoritative conversation summaries, selected identity/detail/current visible branch, manual recovery, operation-generation freshness and selected-detail request lifecycle.
- `ConversationSidebarViewController`: list presentation/initial list request.
- `ConversationDetailViewController`: detail/messages, recovery menu and centered sync feedback.
- Default `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: account context, public warm-up and transient authorized transport; task-handle exposure does not change auth semantics.

## Delivery / serialized direction

1. `DEV-conversation-recovery` — **Completed / merged / Stable for recorded scope**.
2. `DEV-multi-conversation-state` — next serialized development Work when the user asks to continue.
3. `DEV-conversation-round-count` / preferences integration.
4. `DEV-send-stream`.
5. Markdown export, long-conversation tuning, attachments and remaining daily-use work.

## Known issues / constraints

- No unit/UI test target; automated validation remains Release compile, IPA packaging/inspection and artifact upload.
- Current freshness/task lifecycle is intentionally single-selected; future multi-conversation Work will generalize account-scoped per-conversation state.
- Runtime below iOS17, iPad, non-personal workspace, send/streaming and attachments remain Unknown / Unverified as applicable.
- Long account/list/detail durations are end-to-end signals, not proof of one bottleneck.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. Current user/device evidence outranks older assumptions.
