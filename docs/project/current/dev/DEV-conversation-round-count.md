# DEV-conversation-round-count

## Status

**Active — exact b37 Runtime accepts no-stutter geometry/performance baseline; exact b38 Code/Static/CI/Artifact/current-main merge-view complete; Runtime Pending**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Phase 8 conversation metadata/settings bundle with compact header, round count, timestamps, Copy, adaptive round navigation, persisted Preferences, first-entry latest placement and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open, mergeable, not merged.
- **Exact b38 product/config source**: `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- **Current main at b38 validation**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Only this development checkpoint is Active. Stable/Frozen: No/No.

## Accepted baseline that b38 must preserve

- `ConversationRepository` remains sole conversation/list/read/recovery authority.
- `AppPreferences` remains sole persisted settings owner.
- `ConversationRoundProjection` remains derived semantic round data; each visible authoritative user message starts one round and the first presentation row of that user message is the quick-navigation target.
- Recipient/tool/internal filtering, compact assistant Copy, timestamps/preferences/header, physical-bottom/rubber-band direction, first-entry latest, A/B anchors, list/cache reconciliation and Sync/Reload behavior remain.
- b37 `ConversationMessagePresentationProjection` is presentation-only: bounded plain-text chunks, deterministic row heights/prefix offsets and manual cell layout derive from authoritative messages. Copy still reads the complete authoritative message. This is now the accepted performance baseline and must not be rolled back.
- Rich Markdown/citation rendering remains future `DEV-message-rendering`.

## Candidate progression / Runtime truth

- b24 identity rejected/reserved; b25-b30 Runtime partial/failing.
- b31 accepted precise user-message semantic landing; b32 accepted recipient filtering + compact Copy; b33 accepted physical-bottom direction.
- b34 proved final correction was not the remaining smoothness root cause.
- b35 direct+short-ease still had multi-second positioning stalls.
- b36 exact Runtime proved the real blocker was long-message/table geometry: 47 direct-position events had median ~187ms, P90 ~780ms and max ~3952ms; ordinary right-side scroll-indicator dragging also severely stuttered; the same 161-visible-message conversation grew from roughly 13.8k to 154.6k points as giant automatic rows became realized.
- b37 replaced deferred giant-row self-sizing with bounded chunks, deterministic derived geometry/prefix offsets and manual cell layout. Latest exact-device feedback: **“这次确实不卡了”**. Treat this as Runtime acceptance of the geometry/performance direction, not yet final Phase 8 Stable.
- User then explicitly requested restoring genuine visible scrolling animation for another test.

## Exact b37 accepted performance Candidate

- Candidate `DEV-conversation-round-count-0.1.0-b37`, build `0.1.0 (37)`.
- Exact source `92d9f255f3d2ab993d264bda1a71e92b36b44b6c`.
- Push Run `33210450417`; Runtime Artifact `9701385668`; ZIP `sha256:d4e682f1dcf4b0fa617eb84461078586f26b26f13392b1cae8578491087d4e58`; IPA SHA `7db22b82f3ca131d04b672dec480d2a58fd87fa828c74722a16784bf4397694e`.
- Runtime: no-stutter geometry/performance direction accepted by user. No new diagnostics file was supplied with that acceptance, so do not invent numerical b37 timings.

## Exact b38 product correction

- Candidate `DEV-conversation-round-count-0.1.0-b38`, version/build `0.1.0 (38)`.
- Parent checkpoint `73d09cb83c3eda7b255e09b17b2bd9b0897cea49`.
- Exact product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Exact parent→product diff is only three files:
  - `.github/workflows/ios-foundation.yml`: 2+/2-, Candidate/Artifact b37→b38 only;
  - `ChatGPTClient.xcodeproj/project.pbxproj`: 4+/4-, Debug+Release build/Candidate 37→38 only;
  - `ChatGPTClient/Conversation/ConversationFeature.swift`: 8+/20-, round-jump presentation only.
- b37 message chunking, deterministic height/prefix geometry, manual cell layout, semantic round mapping, anchors, Copy and all repository/network code are untouched.
- Removed the nonanimated ~120pt lead teleport and lead-position timing path.
- Uses existing O(1) `answerTargetOffsetY(for:)`; no `scrollToRow`, Auto Layout geometry discovery or final correction snap.
- One cancellable `UIViewPropertyAnimator` continuously animates from the current viewport offset to the deterministic target offset for 0.35s with `.easeInOut`.
- Rapid taps stop the active animator at its current visual position, keep the transient semantic target cursor, resolve the next round and animate from that current position. Real drag still cancels animation and clears programmatic intent.
- Diagnostics use `presentationMode=continuous_geometry_animation` plus target row/role, current offset, travel distance, retargeting and landing error only.
- No timer, debounce, retry, watchdog, persistent geometry cache, second semantic index or state owner.

## Exact b38 CI / Artifact / package identity

- Exact push Run / Job: `33230823568` / `99043233637` — success on `head_sha=0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Runtime Artifact `9708425762`; Artifact name `ChatGPTClient-DEV-conversation-round-count-0.1.0-b38`.
- Artifact ZIP digest `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`; independent SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: `0.1.0 (38)`, Candidate b38, source marker `0d1801137e4e`, MinimumOSVersion 14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64.

## Current-main merge-view evidence

- Main remained `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- PR #27 remained open, mergeable and not merged at exact product head.
- PR Run / Job `33230825189` / `99043238346` — success.
- GitHub synthetic merge `fd1ed7508f04e9045b99239cad88dca8f6e01450` explicitly merges exact b38 source `0d180113...` into current main.
- Merge Artifact `9708423606` is CI/mergeability evidence only and never replaces exact Runtime Artifact `9708425762`.

## Tooling-only assembly evidence

- Temporary b38 assembly branches were used only to materialize/audit Swift/Xcode blobs because the connector has no direct patch-write for the large Swift source.
- An initial temp attempt passed Swift parse/identity steps but could not push a workflow-file mutation because the GitHub App lacked workflow-write permission; no official branch/product change occurred from that failure.
- A clean temp materialization then passed Swift parser and `git diff --check`. A later spacing-only cleanup normalized function separation without changing behavior.
- Both temporary assembly branches were reset to the pre-product b38 checkpoint after blob harvest. They are never Candidate authority.
- Formal b38 source was built directly from the checkpoint tree and exact audited blobs; only the three intended product/config files changed.

## Documentation recovery point

- This checkpoint commit is the recovery point for the post-product documentation chain.
- `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md` and especially `BUILD_TEST_INDEX.md` were stale at b36/b34 before this round and must be synchronized to b36 failure + b37 accepted performance baseline + b38 evidence before final handoff if tooling permits.
- Exact b38 product source remains `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67` regardless of later docs-only commits.
- Do not replay or rebuild b24-b38 identities.

## Validation state

- **b36 Runtime/manual/real-device**: Partial/failing.
- **b37 Runtime/manual/real-device**: Accepted for no-stutter geometry/performance result.
- **b38 Code written**: Yes.
- **b38 Static/source audit**: Passed.
- **b38 exact push CI**: Passed.
- **b38 identity-valid Runtime Artifact**: Produced and independently verified.
- **b38 current-main merge-view CI**: Passed.
- **b38 Runtime/manual/real-device**: Pending.
- **Stable/Frozen**: No/No.

## b38 Runtime focus

1. In the same long conversation, drag the right-side scroll indicator quickly bottom↔top; it must remain as smooth as b37.
2. Previous/next should now visibly traverse the full content continuously instead of teleporting near the destination; test both short and very long distances.
3. Rapid repeated taps during movement should retarget smoothly from the current visual position and advance one semantic round per tap.
4. Real finger drag during programmatic movement must immediately take control.
5. Final landing remains the intended authoritative user-message round start with no hard correction snap.
6. Long-message completeness/chunk boundaries, first-entry latest, A/B anchors, Copy/timestamps/preferences/filtering/list reconcile/Sync/Reload remain unchanged.
7. If b38 is rejected, export diagnostics when useful, record the exact defect first, preserve b37 geometry baseline, and allocate b39 or later; never rebuild b38.

## Next exact action

Human Runtime gate: install/test exact Runtime Artifact `9708425762` / IPA SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`. If accepted, update Runtime truth, re-check current main/PR/active-task conflicts and obtain a fresh exact current-head merge-view as required before merge/close Phase 8. If rejected, record the precise presentation defect first and allocate b39+ while retaining b37 deterministic geometry.