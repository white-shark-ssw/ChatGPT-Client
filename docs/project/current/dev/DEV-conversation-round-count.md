# DEV-conversation-round-count

## Status

**Active — exact b37 Runtime accepts long-conversation smoothness/scrollbar geometry correction; b38 reserved to restore genuine continuous round-jump animation**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Phase 8 conversation metadata/settings bundle with compact header, round count, timestamps, Copy, adaptive round navigation, persisted Preferences, first-entry latest placement and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27 open, mergeable, not merged.
- **Branch/product head before this checkpoint write**: exact b37 product/config source `92d9f255f3d2ab993d264bda1a71e92b36b44b6c`.
- **Current main**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Only this development checkpoint is Active. No parallel Work/candidate conflict exists in `docs/project/current/dev/`.
- Stable/Frozen: No/No for this Work.

## Accepted scope that must remain unchanged

- `ConversationRepository` remains sole conversation/list/read/recovery authority.
- `AppPreferences` remains sole persisted presentation-preference owner.
- `ConversationRoundProjection` remains derived round semantics; each visible authoritative user message starts one round.
- Recipient/tool/internal filtering, compact assistant Copy, timestamps/preferences/header, physical-bottom/rubber-band direction, first-entry latest, A/B historical anchors, list/cache reconciliation and Sync/Reload behavior remain.
- b37 `ConversationMessagePresentationProjection` is presentation-only: bounded plain-text chunks, deterministic row metrics/prefix offsets and manual cell layout derive from authoritative `messages`; they are not a second conversation store or semantic authority.
- Copy continues to use the complete authoritative message, not a display chunk.
- Rich Markdown/citation rendering remains future `DEV-message-rendering` and is out of this Work.

## Candidate progression summary

- b24 identity rejected/reserved; b25-b30 Runtime partial/failing.
- b31 accepted precise semantic user-row landing; b32 accepted recipient filtering + compact Copy; b33 accepted physical-bottom direction.
- b34 disproved final correction as sole smoothness cause.
- b35 direct+short-ease retained multi-second long-message stalls.
- b36 exact Runtime proved table/text geometry was the blocker: quick navigation and ordinary right-side scroll-indicator dragging both severely stuttered; direct positioning P50 ~187ms, P90 ~780ms, max ~3952ms, and the 161-row conversation geometry expanded from ~13.8k to ~154.6k points as rows became realized.
- b37 replaced deferred giant-cell self-sizing with bounded message presentation chunks + deterministic derived row geometry/manual layout/O(1) target offsets.

## Exact b37 identity / validation

- **Candidate**: `DEV-conversation-round-count-0.1.0-b37`
- **Version / Build**: `0.1.0 (37)`
- **Exact product/config source**: `92d9f255f3d2ab993d264bda1a71e92b36b44b6c`
- Parent checkpoint source: `757d7fd444bce6032195be4f543a1b868a566eb9`.
- Exact parent→product diff: workflow 2+/2-, Xcode identity 4+/4-, `ConversationFeature.swift` 339+/139- only.
- Static Swift parser and diff checks passed during audited materialization.
- Exact push Run `33210450417` — success on `head_sha=92d9f255...`.
- Runtime Artifact `9701385668`; Artifact ZIP digest `sha256:d4e682f1dcf4b0fa617eb84461078586f26b26f13392b1cae8578491087d4e58`.
- IPA `ChatGPTClient-0.1.0-b37-dev-conversation-round-count.ipa`; independent IPA SHA `7db22b82f3ca131d04b672dec480d2a58fd87fa828c74722a16784bf4397694e`.
- Independent package inspection: `0.1.0 (37)`, Candidate b37, source marker `92d9f255f3d2`, MinimumOSVersion 14.0, arm64.
- Current-main PR merge-view Run `33210453710` succeeded on synthetic merge `73821726c8a514d320096e67ad89386ddabab4ba`, explicitly merging exact b37 source into `main@a6e3b2bc...`.
- Merge-view is CI evidence only and does not replace exact Runtime Artifact `9701385668`.

## Exact b37 Runtime result — 2026-08-29

Latest user real-device feedback on exact b37: **“这次确实不卡了”** and asks to restore the real scrolling animation for another test.

Accepted by this Runtime result:

- The severe long-conversation stutter that affected b36 round navigation is no longer reproduced in b37.
- The geometry/long-message virtualization direction is therefore accepted as the current performance baseline and must not be rolled back while testing animation.
- The user's request explicitly reopens only the round-jump presentation style: replace b37's instant lead-position + ~120pt/0.22s finish with a genuine continuous animation now that geometry is deterministic.

Boundary:

- b37 is Runtime-accepted for the reported **no-stutter performance result**. This does not yet make the whole Phase 8 Work Stable because the user explicitly wants a b38 animation trial before final acceptance.
- No new diagnostics file was supplied in this turn; do not invent numerical b37 Runtime timings.

## b38 reserved identity / intended minimal change

- **Reserved Candidate**: `DEV-conversation-round-count-0.1.0-b38`
- **Version / Build**: `0.1.0 (38)`
- Repository code search found no existing exact b38 Candidate before reservation; only this Active checkpoint exists.
- b24-b37 identities are permanently reserved and must not be rebuilt/reused.

b38 must preserve all b37 geometry/cell/projection code unchanged and alter only quick-navigation presentation plus Candidate identity:

1. Use the already-derived `answerTargetOffsetY(for:)` target. Do not call `scrollToRow`, Auto Layout sizing or geometry discovery during a jump.
2. Animate continuously from the **current viewport offset** to the target offset. No pre-jump nonanimated teleport/120pt lead point.
3. Use one unified behavior for short and long distances.
4. Rapid repeated taps keep the existing transient target cursor: stop the current animation at its current presentation position, resolve the next semantic round, then animate from that current offset to the new target.
5. A real user drag immediately stops programmatic animation and clears programmatic intent, preserving accepted user-intent ownership.
6. Do not reintroduce b33/b34 final correction snaps, stale completion correction, timer/debounce/watchdog, alternate row-height cache, second semantic index or any network/state-owner changes.
7. Record privacy-safe request/completion with `presentationMode=continuous_geometry_animation`, target row, distance and landing error only.

Implementation preference: keep the existing single `UIViewPropertyAnimator` owner and animate `tableView.contentOffset` from current offset to the deterministic final offset. This avoids reintroducing the old `UITableView.scrollToRow` geometry path while providing a genuine visible traversal.

## Batch recovery point

- **Batch A — b37 Runtime acceptance + b38 reservation**: complete with this checkpoint commit.
- **Batch B pending**: inspect exact b37 jump code; create one minimal b38 product/config commit changing only workflow/Xcode identity plus round-jump presentation in `ConversationFeature.swift`; exact-diff audit before branch fast-forward.
- **Batch C pending**: exact b38 push CI, Runtime Artifact, independent package identity/SHA verification and current-main PR merge-view.
- **Batch D pending**: synchronize durable docs/index to b36 failure + b37 accepted geometry baseline + b38 evidence, verify docs-only diff, then hand exact b38 IPA to user.
- **Must not replay/touch**: b24-b37 identities; exact b37 geometry/projection/manual-cell architecture; repository/list/cache/network ownership; rendering scope; any other task checkpoint.
- **Next exact action**: implement the smallest b38 continuous-animation patch from exact b37 product source, audit exact diff, then produce and verify the unique b38 Runtime IPA.

## Validation state

- **b36 Runtime/manual/real-device**: Partial/failing.
- **b37 Code/Static/CI/Artifact/merge-view**: Passed/produced.
- **b37 Runtime/manual/real-device**: **Accepted for no-stutter geometry/performance result**.
- **b38 Code written**: No.
- **b38 Static/CI/Artifact/Runtime**: Pending.
- **Stable/Frozen**: No/No.

## b38 Runtime focus

1. In the same long conversation, confirm right-side scroll-indicator dragging remains as smooth as b37.
2. Tap previous/next across short and very long distances: the viewport should visibly traverse content continuously instead of teleporting near the destination.
3. Rapid repeated taps during movement should retarget smoothly from the current visual position and advance one semantic round per tap.
4. Real finger drag during programmatic movement must immediately take control.
5. Final landing remains the intended authoritative user-message round start with no hard correction snap.
6. Long-message completeness/chunk boundaries, first-entry latest, A/B anchors, Copy/timestamps/preferences/filtering/list reconcile/Sync/Reload remain unchanged.