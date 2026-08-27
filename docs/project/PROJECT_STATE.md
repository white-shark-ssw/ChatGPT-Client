# Project State

_Last updated: 2026-08-28._

## Current accepted baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation baseline.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account-context baseline for tested iPhone/iOS17 scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted Plus/personal diagnostic list + detail protocol evidence baseline.
- `DEV-native-read-path-0.1.0-b9`: merged Stable production native-read baseline for tested scope.
- `DEV-conversation-recovery-0.1.0-b15`: merged Stable recovery baseline for tested Plus/personal iPhone/iOS17 scope; PR #10 merged at `a089fb0448f1c0282e634e5cccf3d0a47199d81f`.
- `DEV-multi-conversation-state-0.1.0-b21`: merged Stable multi-conversation read-state baseline for tested Plus/personal iPhone/iOS17 scope; PR #23 merged at `2057a6241839afabeaf9b81c9daea24d3a0978f6`.
- `DEV-conversation-list-cache-core-0.1.0-b23`: **merged Stable conversation-list cache-core baseline for the recorded Plus/personal iPhone/iOS17 scope**; PR #24 merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`.

The merged accepted baseline remains b23 for conversation-list cache/read behavior. `DEV-conversation-round-count` is the current Active Work layered on that baseline and is not yet Stable.

## Active development — DEV-conversation-round-count

- **Branch**: `dev/conversation-round-count-20260828`.
- **Activation baseline**: `main@e884afdb36c6e62d54e3c8dfe25ff1765bfb11c2`; resume checks through b25 production found no base advance or competing Active development checkpoint.
- **Scope**: shared derived active-branch round count/answer anchors, authoritative historical message timestamps, visible-text Copy, one adaptive previous/next answer navigation control, and the first centralized persisted Preferences owner.
- **Authority boundary**: `ConversationRepository` remains sole conversation/list authority. `AppPreferences` owns display/interaction booleans only. `ConversationRoundProjection` is derived from authoritative visible `ConversationDetail.messages`; no second mutable counter/index authority and no new network path.
- **Type-prefix evidence boundary**: current source does not expose an evidenced authoritative Chat/Work conversation type. The implementation therefore shows only verified `N轮` and does not guess `聊天`/`工作` from presentation text.
- **Preferences defaults for this Work**: round count On, message timestamps On, answer quick navigation On.

### Rejected b24

`DEV-conversation-round-count-0.1.0-b24` / `0.1.0 (24)` is permanently reserved and **Artifact identity rejected**. Exact product source `3eefc34d9fd279e2913509591446f8f2c4575f41`; Run `33109613596`; Job `98648639389`; uploaded container Artifact `9661977997`, ZIP `sha256:6f24e6bbfee8e7caf1412575df0fd15be0b5ddb57b98c5b54f29317a5dec73c7`. Build logs prove the old package script overrode the intended Candidate with stale `DEV-conversation-list-cache-core-0.1.0-b23` and emitted `ChatGPTClient-0.1.0-b24-dev-conversation-list-cache-core.ipa`, IPA SHA `d635499300b8ab56c23770294d987228ce1af15daf9a436ea867e29c07b665b1`. b24 was not installed/tested and must never be rebuilt or reused.

### Current b25 Runtime Candidate

- **Candidate**: `DEV-conversation-round-count-0.1.0-b25`, `0.1.0 (25)`.
- **Exact product/config source**: `5e6a61a45b5aae1d6d4ddb210a8685094a2e74a8`.
- **Exact CI**: Run `33110228837`, Job `98650799276`, success with Xcode 16.4; target `arm64-apple-ios14.0`.
- **Artifact**: `9662219000`; ZIP `sha256:b6db29921f0b1f2f593611080ffcb8ce6542db820ee73fcf728a124ab25cee57`.
- **IPA**: `ChatGPTClient-0.1.0-b25-dev-conversation-round-count.ipa`; SHA `91ea6b79b67ac06f45771606d425221e10d80e7992c524be697a73bf320c923b`.
- **Embedded identity**: Candidate `DEV-conversation-round-count-0.1.0-b25`; source marker `5e6a61a45b5a`.
- **Packaging correction**: no command-line Candidate override; post-build script reads built app version/build/Candidate, rejects mismatch, derives work slug from the built Candidate and names the IPA accordingly. Workflow Artifact label is not treated as identity authority.
- **Evidence level**: Code written + static/source/package review + exact CI + identity-valid Artifact. **Runtime/manual/real-device: Not tested. Stable/Frozen: No.**

## Stable merged multi-conversation baseline — DEV-multi-conversation-state

- **Merged PR**: #23, merge commit `2057a6241839afabeaf9b81c9daea24d3a0978f6`.
- **Final Runtime Candidate**: `DEV-multi-conversation-state-0.1.0-b21`, `0.1.0 (21)`.
- **Exact tested product/config source**: `6b50ead167bfde305d2ad58dd16fee6edaabf597`.
- **Exact Candidate CI**: Run `33070183417`, Job `98510113281`, success.
- **Exact Runtime Artifact**: `9645439329`; IPA SHA `490cce1c1252afc5663c700f10b5fa647365205bc8a692f8a4e7b38c8c07234d`.
- **Accepted scope**: resident return, hidden completion, same-target coalescing/replacement, historical scroll, observed 0→8 resident process-footprint behavior and title lifecycle on tested Plus/personal iPhone/iOS17.
- **Conditional boundaries**: natural failed-resident navigation, supported account-switch purge, non-personal workspace identity and missing-anchor-message discard remain Unknown / Unverified; no arbitrary normal LRU is frozen.

## Stable merged conversation-list cache baseline — DEV-conversation-list-cache-core

### Historical b22

`DEV-conversation-list-cache-core-0.1.0-b22` is permanently reserved and Runtime-partial/failing. Exact source `6eefc0f4d1734feeef17cabdaa4942d0ade14ba0`, Run `33097152104`, Job `98604939953`, Artifact `9656872520`, IPA SHA `f91818079ed1310cef4e7f1d66ceea131a96b450f012d979a9a36d1ca14e2886`.

b22 proved snapshot persistence, 60-second `recent_skip`, stale one-refresh and manual-bypass mechanics, but cache publication occurred only after ~4.4–5.0 seconds of account verification, offline auth failure prevented cache presentation, and manual refresh lacked explicit terminal feedback. Corrected code does not reuse b22.

### Accepted b23 Runtime Candidate

- **Candidate**: `DEV-conversation-list-cache-core-0.1.0-b23`, `0.1.0 (23)`.
- **Exact product/config source**: `d2af0fc157f6e2d037636c55f963c18071a332d5`; corrected product source `7bb6d116d785614dccf0e2a2b412d2823ad583e1`.
- **Exact CI**: Run `33101116431`, Job `98618762016`, success.
- **Artifact**: `9658508764`; ZIP `sha256:fa57e557a484f98b06753ce3f09fe4cdd89d390ea00a8778e052a518a560776b`.
- **IPA**: `ChatGPTClient-0.1.0-b23-dev-conversation-list-cache-core.ipa`; SHA `8f6911616fff1e93885191fcaec0f31a1e3c9488b7f4522fdbdb7dc5518be516`.
- **Package identity**: `0.1.0 (23)`, Candidate b23, source `d2af0fc157f6`, minimum iOS14.0, device family `[1,2]`, arm64.

### b23 real-device evidence

User-supplied iPhone/iOS17 diagnostics identify exact b23 and Plus/personal scope. Observed behavior:

- after first successful b23 verification, stale cache reconciled a returned page of 28 against server total 29 and preserved one real off-page cached row, producing/writing 29 rows;
- rapid relaunch loaded the 29-row provisional list in `4.09 ms` before account verification completed (~4521 ms), then matching verification selected `recent_skip` and issued no list request;
- another process relaunch with network unavailable loaded 29 provisional rows in `4.30 ms`; natural `NSURLErrorDomain -1005` auth failure selected `offline_cache`, completed list load from cache in `31.58 ms`, and did not replace the list with Login/account-verification UI;
- offline manual refresh failed non-destructively while the screenshot kept rows visible and showed the centered navigation prompt `刷新失败 · 当前显示缓存` above the `ChatGPT` title;
- online manual refresh uses `manual_bypass`, emits exactly one list request, returns HTTP200, preserves the off-page item (`28 + 1 -> 29`) and persists the reconciled cache; a second manual refresh repeats the one-request behavior;
- direct user result: `好像没问题了`, with no new functional defect reported in the tested b23 sequence.

This is **Runtime acceptance for the recorded tested cache-core scope**, not proof of every conditional path.

### PR / merge evidence

- **PR**: #24, merged at `3f36e2bddb0c2907e21647c7424d745d2242ef93`.
- **PR merge-view CI**: Run `33103769517`, Job `98628067286`, success.
- **Tested merge view**: `26297ff0683966c2c82fd7a8a95f53f1ad51d3d6`, combining `main@846dad81e382e6b7a862f082ef5bc5d4ce617493` with PR head `6a762f6fc968d1829d548be116776279cc0b7052`.
- **Merge-view Artifact**: `9659600955`; IPA `ChatGPTClient-0.1.0-b23-dev-conversation-list-cache-core.ipa`; IPA SHA `06f8ade97344c54b017cd31c82f87abc8bc33e4c2a4fb277e17f02d0f5b204af`; embedded source marker `26297ff06839`.
- The merge-view Artifact is CI/merge evidence only and does not replace the exact real-device Runtime Artifact `9658508764`.

### Cache ownership / privacy boundary

- `ConversationRepository` remains sole authoritative in-memory list/conversation owner.
- `AuthSessionStore` remains sole verified auth/account owner and is unchanged.
- Default persistent WebKit storage remains sole persistent auth-secret owner.
- `ConversationListCacheStore` is storage-only and may persist schema-1 summaries plus a protected SHA-256 last-verified scope namespace hint. It persists no raw account/user IDs, cookies, tokens, bearer values, Detail mappings or message bodies.
- Before current verification completes, the last successfully verified scope may provisionally provide **list titles only** for fast/offline presentation. It cannot establish transport/account authority; a different verified scope or confirmed unauthenticated result rejects the provisional presentation. Provisional/offline rows cannot start Detail until current scope is verified.
- No retry/timer/watchdog/polling or alternate endpoint was introduced.

### Remaining evidence boundaries

Still Unknown / Unverified unless naturally exercised:

- supported real account switch / verified-scope mismatch transition;
- provisional cached-row tap/Detail-block Runtime path;
- corrupt/schema-incompatible snapshot Runtime rejection;
- iPad, iOS below 17 and non-personal workspace identity.

These are conditional boundaries, not current known defects, and do not justify manufactured account transitions or destructive corruption tests.

## Current architecture

- `AppDelegate`: lifecycle plus accepted WebKit warm-up-before-root sequencing.
- `RootViewController`: native compact list/detail navigation owner.
- `ConversationRepository`: sole authoritative conversation/list/read/recovery owner with account-scoped residents and persistent-list-cache integration.
- `ConversationListCacheStore`: storage-only persistent summary snapshot + privacy-safe last-verified scope namespace hint.
- `ConversationDetailViewController`: detail/messages/recovery presentation plus per-conversation historical scroll metadata and current b25 metadata/Copy/answer-jump presentation.
- `AppPreferences`: centralized persisted display/interaction preference owner; not conversation authority.
- `ConversationRoundProjection`: derived active-branch round/answer projection; not mutable data authority.
- `DiagnosticsLogger`: accepted structured diagnostics authority.
- Default persistent `WKWebsiteDataStore`: sole persistent auth-secret authority.
- `AuthSessionStore`: sole verified auth/account-context owner.

## Roadmap handoff

`DEV-conversation-round-count` is currently Active at identity-valid b25 CI/Artifact and awaits real-device Runtime acceptance. It must not be described as complete or Stable before that gate. After it is accepted/merged, the next serialized development priority is `DEV-send-stream` according to the current development plan.

## Evidence rule

Always distinguish Code written, static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen acceptance. CI/Artifact success is not Runtime proof.