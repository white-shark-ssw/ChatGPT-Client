# Project State

_Last updated: 2026-08-29 through exact b38 Runtime acceptance and final Phase 8 merge preparation._

## Current accepted merged baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account context for recorded iPhone/iOS17 Plus/personal scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted diagnostic read evidence.
- `DEV-native-read-path-0.1.0-b9`: merged Stable native read path.
- `DEV-conversation-recovery-0.1.0-b15`: merged Stable recovery; PR #10.
- `DEV-multi-conversation-state-0.1.0-b21`: merged Stable multi-conversation read state; PR #23; Frozen No.
- `DEV-conversation-list-cache-core-0.1.0-b23`: merged Stable list-cache core; PR #24; Frozen No.

`DEV-conversation-round-count` exact b38 is now Runtime accepted and awaiting only final PR merge + post-merge documentation synchronization before promotion to the next merged Stable baseline.

## Phase 8 — DEV-conversation-round-count

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27.
- **Accepted Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`.
- **Exact accepted product/config source**: `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`. Later checkpoint/docs-only commits do not redefine this product source.
- **Runtime Artifact**: `9708425762`.
- **IPA SHA**: `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- **Runtime result**: accepted on recorded iPhone/iOS17 scope; latest user feedback **“没问题了”**.
- **Stable/Frozen before merge**: No/No. Stable promotion waits only for final merge/state sync; Frozen remains No.

## Authority / architecture

- `ConversationRepository` remains sole authoritative conversation/list/read/recovery owner.
- `AuthSessionStore` remains sole verified auth/account owner; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- `ConversationListCacheStore` remains storage-only.
- `AppPreferences` remains sole persisted display/interaction settings owner.
- `ConversationRoundProjection` is derived semantic round data only.
- `ConversationMessagePresentationProjection` is ephemeral derived presentation virtualization/geometry only: bounded display chunks, message→first-row mapping, deterministic row heights and prefix offsets. It is not conversation authority.
- `ConversationMessageCell` uses deterministic manual frame layout for one bounded display chunk. Full-message Copy semantics remain authoritative-message based.
- One transient programmatic target cursor + one cancellable `UIViewPropertyAnimator` own round-jump presentation only.

## Accepted Phase 8 behavior

- b26 authoritative-total list reconciliation cap: stale `30 -> 29`, repeated `29/29`.
- b29 right-top refresh/top blank-region correction.
- b31 semantic landing at the authoritative user-message round start.
- b32 recipient/tool/internal filtering and compact assistant Copy direction.
- b33 physical-bottom/rubber-band direction.
- timestamps/preferences/header, first-entry latest/bottom, independent A/B anchors and Sync/Reload anchor re-derivation.
- b37/b38 deterministic long-message presentation geometry: bounded chunks + exact derived row metrics/prefix offsets + manual frame layout.
- b38 continuous round animation from current viewport offset to the already-derived O(1) target offset for 0.35s `.easeInOut`; no pre-jump teleport and no final correction snap.

## Evidence progression that established the accepted architecture

- b24 package identity rejected/permanently reserved; b25-b35 Runtime partial/failing/superseded.
- b36 Runtime proved the dominant remaining blocker was long-message/table presentation geometry rather than animation alone: ordinary right-side scroll-indicator dragging also severely stuttered; 47 direct-position samples had median ~187ms, P90 ~780ms, max ~3952ms; one 161-visible-message table geometry grew from ~13.8k to ~154.6k points as giant automatic rows became realized.
- b37 replaced deferred giant-row self-sizing with bounded chunks, deterministic row height/prefix geometry and manual cell layout. User exact-device feedback **“这次确实不卡了”** accepted the no-stutter performance direction.
- b38 preserved b37 geometry and restored genuine visible full-distance animation. User exact-device feedback **“没问题了”** accepts the combined performance + continuous-animation result.

## Exact b38 validation

- Candidate `DEV-conversation-round-count-0.1.0-b38`, version/build `0.1.0 (38)`.
- Exact source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Parent checkpoint `73d09cb83c3eda7b255e09b17b2bd9b0897cea49`.
- Exact parent→product diff only: workflow identity 2+/2-, Xcode build/Candidate 4+/4-, `ConversationFeature.swift` 8+/20-.
- Exact push Run / Job `33230823568` / `99043233637` — success.
- Runtime Artifact `9708425762`; ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`; SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: `0.1.0 (38)`, Candidate b38, source `0d1801137e4e`, MinimumOSVersion 14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64.
- Product-head PR merge-view Run / Job `33230825189` / `99043238346` succeeded on synthetic merge `fd1ed7508f04e9045b99239cad88dca8f6e01450` against then-current `main@a6e3b2bc...`.
- Later docs-only commits changed the PR head after product Runtime. Final merge must use a fresh current-head/current-main mergeability check and verify the delta from exact product source is docs-only.

## Current finalization gate

1. Synchronize all durable Phase 8 docs and build/test index to exact b38 Runtime acceptance.
2. Re-check real development head, main, PR #27 and active checkpoint conflict state.
3. Confirm exact product source→current branch delta is docs-only and obtain a fresh current-head/current-main synthetic merge view.
4. Merge PR #27 using the exact expected current PR head only if still mergeable and no parallel conflict appears.
5. On merged `main`, record the actual merge commit/current main, promote the recorded Phase 8 scope to Stable (Frozen No), and remove only `docs/project/current/dev/DEV-conversation-round-count.md`.

## Rendering scope boundary

Current message body remains plain-string presentation. Markdown/code/table/link/citation rendering, including raw `filecite` presentation observed in supplied comparison material, belongs to future `DEV-message-rendering` and must not be speculatively rewritten here.

## Evidence boundaries

- Exact b38 Runtime: accepted on recorded iPhone/iOS17 scope.
- CI/Artifact success remains distinct from Runtime; b38 has both classes of evidence.
- iOS17 success does not prove iOS14–16 or iPad.
- Non-personal workspace identity and other explicitly untested account/cache branches remain Unknown/Unverified.

## Evidence rule

Always distinguish Code written, Static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen.
