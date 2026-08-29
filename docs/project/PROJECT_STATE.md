# Project State

_Last updated: 2026-08-29 through exact b36 Runtime failure, b37 no-stutter Runtime acceptance, and exact b38 Code/Static/CI/Artifact/current-main merge-view evidence._

## Current accepted merged baseline

- `DEV-app-foundation-0.1.0-b1`: merged Stable foundation.
- `DEV-auth-bootstrap-0.1.0-b6`: merged Stable authentication/account context for recorded iPhone/iOS17 Plus/personal scope.
- `DEV-protocol-read-0.1.0-b7`: merged accepted diagnostic read evidence.
- `DEV-native-read-path-0.1.0-b9`: merged Stable native read path.
- `DEV-conversation-recovery-0.1.0-b15`: merged Stable recovery; PR #10.
- `DEV-multi-conversation-state-0.1.0-b21`: merged Stable multi-conversation read state; PR #23; Frozen No.
- `DEV-conversation-list-cache-core-0.1.0-b23`: merged Stable list-cache core; PR #24; Frozen No.

The merged product baseline remains b23. `DEV-conversation-round-count` is Active and layered on that baseline; it is not Stable/Frozen yet.

## Active Work — DEV-conversation-round-count

- **Branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open, mergeable, not merged at exact b38 product validation.
- **Current main at b38 validation**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- **Latest tested Candidate**: b37; Runtime accepts the no-stutter geometry/performance direction.
- **Current Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`; Runtime Pending.
- **Exact b38 product/config source**: `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`. Later checkpoint/docs-only commits do not redefine this product source.
- **Stable/Frozen**: No/No.

## Authority / architecture

- `ConversationRepository` remains sole authoritative conversation/list/read/recovery owner.
- `AuthSessionStore` remains sole verified auth/account owner; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- `ConversationListCacheStore` remains storage-only.
- `AppPreferences` remains sole persisted display/interaction settings owner.
- `ConversationRoundProjection` is derived semantic round data only.
- b37 `ConversationMessagePresentationProjection` is ephemeral presentation virtualization/geometry only: bounded plain-text display chunks, message→first-row mapping, deterministic row heights and prefix offsets. It is not conversation authority.
- `ConversationMessageCell` uses deterministic manual frame layout for one bounded display chunk. Full-message Copy semantics remain authoritative-message based.
- One transient programmatic target cursor + one cancellable `UIViewPropertyAnimator` own round-jump presentation only.

## Accepted Phase 8 behavior that must remain

- b26 authoritative-total list reconciliation cap: stale `30 -> 29`, repeated `29/29`.
- b29 right-top refresh/top blank-region correction.
- b31 semantic landing at the authoritative user-message round start.
- b32 recipient/tool/internal filtering and compact assistant Copy direction.
- b33 physical-bottom/rubber-band direction.
- timestamps/preferences/header, first-entry latest/bottom, independent A/B anchors and Sync/Reload anchor re-derivation.

## b36 Runtime failure — geometry owner identified

Exact b36 Candidate `DEV-conversation-round-count-0.1.0-b36`, source `8f8614508eef5197f9fff4bb9d10c14354d5821e`, Runtime Artifact `9700254733`.

Exact device evidence:

- Severe round-navigation stutter remained.
- Ordinary right-side scroll-indicator dragging also severely stuttered.
- 47 direct-position samples: median ~187ms, P90 ~780ms, max ~3952ms.
- The same 161-visible-message long conversation initially presented bottom geometry around 13.8k points and later reached about 154.6k points as giant automatic self-sizing rows became realized.
- Source at b36 used one unbounded multiline UILabel per complete message plus deferred estimated/self-sizing row geometry.

Conclusion: b36 is Runtime partial/failing. The dominant remaining blocker was long-message/table presentation geometry, not animation correction alone.

## b37 Runtime accepted performance baseline

Exact b37:

- Candidate `DEV-conversation-round-count-0.1.0-b37`, build `0.1.0 (37)`.
- Source `92d9f255f3d2ab993d264bda1a71e92b36b44b6c`.
- Push Run `33210450417`; Runtime Artifact `9701385668`.
- ZIP `sha256:d4e682f1dcf4b0fa617eb84461078586f26b26f13392b1cae8578491087d4e58`.
- IPA SHA `7db22b82f3ca131d04b672dec480d2a58fd87fa828c74722a16784bf4397694e`.

b37 replaced deferred giant-row self-sizing with bounded display chunks, deterministic height/prefix geometry and manual frame layout. Latest exact-device feedback: **“这次确实不卡了”**.

This accepts b37 as the current **no-stutter geometry/performance baseline**. It does not by itself make all of Phase 8 Stable because the user explicitly requested one further animation trial.

## Exact b38 product / validation

- Candidate `DEV-conversation-round-count-0.1.0-b38`, version/build `0.1.0 (38)`.
- Exact source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Parent checkpoint `73d09cb83c3eda7b255e09b17b2bd9b0897cea49`.
- Exact parent→product diff only:
  - workflow identity 2+/2-;
  - Xcode build/Candidate 4+/4-;
  - `ConversationFeature.swift` 8+/20-.
- b37 geometry/chunk/manual-cell architecture is unchanged.
- Removed b37's nonanimated ~120pt lead teleport/short final-only animation.
- Uses the already-derived O(1) target offset; no `scrollToRow` geometry discovery.
- One `UIViewPropertyAnimator` now continuously animates from current viewport offset to target for 0.35s `.easeInOut`.
- Rapid taps retarget from current visual position using the existing transient semantic cursor; real drag cancels programmatic intent immediately.
- No end correction snap, timer, debounce, retry, watchdog, persistent row-height cache or second semantic/state owner.

### Exact b38 CI / Artifact

- Push Run / Job `33230823568` / `99043233637` — success on exact product source.
- Runtime Artifact `9708425762`.
- ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`.
- IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: `0.1.0 (38)`, Candidate b38, source marker `0d1801137e4e`, MinimumOSVersion 14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64.

### Exact product-head current-main merge-view

- Main `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- PR Run / Job `33230825189` / `99043238346` — success.
- Synthetic merge `fd1ed7508f04e9045b99239cad88dca8f6e01450` explicitly merges exact b38 source into current main.
- Merge Artifact `9708423606` is CI/mergeability evidence only; it never replaces Runtime Artifact `9708425762`.

Later checkpoint/docs commits advance the branch head without changing product source. Before eventual merge, re-check current main, PR/head, active-task conflict state and obtain a fresh current-head/current-main merge-view as governance requires.

## Current Runtime gate

Install/test exact b38 Runtime Artifact `9708425762` / IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e` on the recorded iPhone/iOS17 scope.

Acceptance focus:

1. Right-side scroll-indicator dragging remains as smooth as exact b37; b36 geometry stalls must not return.
2. Previous/next visibly traverses the full content continuously for both short and very long distances.
3. Rapid taps during movement retarget from the current visual offset and advance one semantic round per tap.
4. Real finger drag immediately retakes viewport ownership.
5. Final landing remains the intended authoritative user-message round start with no hard correction snap.
6. b37 chunk completeness, first-entry latest, A/B anchors, Copy/timestamps/preferences/filtering/list reconcile and Sync/Reload remain unchanged.

If rejected, record the exact b38 Runtime defect first, preserve the accepted b37 geometry baseline and allocate b39 or later. Never rebuild b38.

## Rendering scope boundary

Current Phase 8 message body remains plain-string presentation. Markdown/code/table/link/citation rendering, including raw `filecite` presentation observed in supplied comparison material, belongs to future `DEV-message-rendering` and must not be speculatively rewritten here.

## Evidence boundaries

- b36 Runtime: partial/failing.
- b37 Runtime: accepted for the reported no-stutter geometry/performance result.
- b38: Code/Static/CI/Artifact/current-main product-head merge-view complete; Runtime Pending.
- CI/Artifact success is not Runtime proof.
- iOS17 success does not prove iOS14–16 or iPad.
- Non-personal workspace identity and other explicitly untested account/cache branches remain Unknown/Unverified.

## Evidence rule

Always distinguish Code written, Static/local checks, CI passed, Artifact produced, Runtime/manual/real-device tested, Stable and Frozen.
