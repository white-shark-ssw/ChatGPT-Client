# Project State

_Last updated: 2026-08-27._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: **merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope**. PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.

`DEV-multi-conversation-state-0.1.0-b17` now has accepted real-device evidence for its tested core switching/coalescing/hidden-completion/Sync/rapid-overlap sequences, but the Work is still Active and not Stable/Frozen. The merged Stable baseline remains b15 until this Work completes and merges.

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

## Active Work — DEV-multi-conversation-state

- **Work**: `DEV-multi-conversation-state` on `dev/multi-conversation-state-20260827`; PR not created.
- **Baseline/conflict gate**: `main@f155ddb873540f7c80d6e66ebbfeb59ded26f011`; latest final-Artifact gate found no open PR and no second Active DEV checkpoint.
- **Current Candidate**: `DEV-multi-conversation-state-0.1.0-b17`, version `0.1.0 (17)`.
- **Exact product/config source**: `bc69d58b3245a1ab21b250e16612c11d39ddbf33`; tree `3451585f83c7bac69368709fe6273b90a0294d29`. Later docs-only commits do not change this Candidate identity.
- **Atomic publication**: exact b17 product/config source changed only `ConversationFeature.swift`, Xcode project, workflow and `scripts/build_ipa.sh` from its parent, then branch ref moved once.
- **Static/local**: final ConversationFeature blob `1034cff72dea36d6d7e835bdf52dcfe2cdc8e38d`; exact blob matched local source; `swiftc -frontend -parse` passed.
- **CI**: Run `33045536770`, job `98428537619`, success on macOS15 / Xcode16.4; exact Release target `arm64-apple-ios14.0`; log proves b17 candidate/source inputs and `BUILD SUCCEEDED`.
- **Artifact**: `9635486304`; name `ChatGPTClient-DEV-multi-conversation-state-0.1.0-b17`; ZIP digest `sha256:bf6aed8cebcb08153fbe8fac6868ce60c0ef4bd7876340246912ba8edbed1c33`.
- **IPA**: `ChatGPTClient-0.1.0-b17-dev-multi-conversation-state.ipa`; SHA `ed551deac0335e47da56da36ec2a8a20550613ac072ac1ddf0b84790278318dc`; generated sidecar matches independent hash.
- **Embedded identity**: `0.1.0 (17)`, candidate b17, source `bc69d58b3245`, min iOS14.0, device families `[1,2]`, Mach-O arm64.
- **Implementation scope compiled in b17**: account-scoped per-conversation residents/operations, stale Auth-scope rejection, probe commit revalidation, deterministic waiter termination, same-target cancel-before-replace with synchronous task ownership, operation-first coalescing, target-specific Sync/Reload, selected-operation-derived recovery presentation, ordinary/list presentation freshness, main-thread repository owner, active-resident memory-warning protection, `current_node` retention and privacy-safe residency/selection diagnostics.
- **Real-device core evidence**: exact b17 on iPhone/iOS17 showed resident return without navigation-only refetch, hidden completion retained as resident, same-target in-flight return coalescing, Sync A->B->A rejoining the same active Sync, and rapid different-conversation overlap with up to three active operations; no HTTP429 appears in the supplied export.
- **Return timing**: repeated resident returns logged `resident.firstVisible` around `0.23–0.78 ms` in the supplied run.
- **Observed residency scale**: resident count reached 6; `residentTotalApproximateTextBytes` reached `6724764`, which remains correlation only and is not process-memory/LRU-capacity evidence.
- **Runtime defect found**: per-conversation semantic scroll-anchor restoration is missing in b17. User left A around ~10%, switched to B and scrolled B, then returned A and observed A's position shift. This was already a planned P1 item and is now a reproduced P1 runtime defect.
- **Validation**: `Code written = Yes`; `Static/local = Passed`; `CI = Passed`; `Artifact = Produced and identity accepted`; `Runtime/manual/real-device = Core tested sequences accepted with P1 scroll defect`; `Stable/Frozen = No`.

## Current architecture

### Accepted Stable baseline

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: synchronously built split shell; native compact list/detail navigation owner.
- `ConversationRepository` in b15: authoritative conversation summaries, selected identity/detail/current visible branch, manual recovery, selected-detail generation freshness and selected-detail request lifecycle.
- `ConversationSidebarViewController`: list presentation/initial list request.
- `ConversationDetailViewController`: detail/messages, recovery menu and centered sync feedback.
- Default `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: account context, public warm-up and transient authorized transport.

### Active branch direction, core Runtime-tested but not Stable

- One `ConversationRepository` is the account-scoped conversation authority with per-conversation resident and async-operation state; foreground selection is presentation state only.
- `AuthSessionStore` remains the sole account/auth owner. Request transport contexts may validate against its current verified scope but cannot re-adopt an older scope.
- Current resident scope key is `userID + accountID + conversationID`; non-personal workspace identity remains Unknown / Unverified.
- `current_node` is retained as minimal directly evidenced branch-tip metadata; raw mapping payload is still discarded.
- UIKit controllers consume resident/operation state; they are not authoritative conversation stores.
- Scroll position is presentation state and is not yet preserved per conversation; the required future correction is a semantic/per-conversation scroll anchor, not a second data repository or shared raw offset.

## Delivery / serialized direction

1. `DEV-conversation-recovery` — **Completed / merged / Stable for recorded scope**.
2. `DEV-multi-conversation-state` — **Active**; b17 now has core real-device evidence for the tested switching/coalescing/hidden-Sync/rapid-overlap paths. The next smallest user-visible correction is the reproduced P1 semantic scroll-anchor gap under a new candidate; remaining account-switch/failure/LRU acceptance stays separate before Stable.
3. `DEV-conversation-round-count` / preferences integration.
4. `DEV-send-stream`.
5. Markdown export, long-conversation tuning, attachments and remaining daily-use work.

Semantic per-conversation scroll-anchor restoration remains P1 in architecture priority, but it is no longer hypothetical: exact b17 real-device use reproduced it.

## Known issues / constraints

- No unit/UI test target; current automated validation is static Swift parse, Release Xcode CI, IPA packaging/inspection and artifact upload.
- b17 core multi-conversation runtime behavior is accepted only for the exact tested sequences recorded above; do not generalize that to untested account-switch/failure/LRU cases.
- **Known P1 UI defect**: A's per-conversation scroll position/semantic anchor is not restored after switching to B and scrolling B before returning to A.
- Account-context purge/late-callback isolation requires a real supported account-switch/logout runtime route before that criterion can be accepted.
- Current account-scope implementation is personal-account evidence only; non-personal workspace identity remains Unknown / Unverified.
- Normal-operation resident/LRU bound remains Unknown until real-device/system memory measurement; approximate visible-text bytes are not actual process-memory evidence.
- Runtime below iOS17, iPad, non-personal workspace, send/streaming and attachments remain Unknown / Unverified as applicable.
- Long account/list/detail durations are end-to-end signals, not proof of one bottleneck.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, and Stable/Frozen acceptance. Current user/device evidence outranks older assumptions.
