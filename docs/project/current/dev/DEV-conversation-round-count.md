# DEV-conversation-round-count

## Status

**Active — exact b38 Runtime accepted; Phase 8 final documentation + fresh merge-view + merge/close pending**

- **Work ID**: `DEV-conversation-round-count`
- **Routing aliases / keywords**: `会话元数据 / 设置 / 会话轮数 / round count / 消息时间 / 上一轮 / 下一轮 / Copy / Preferences / 顶部栏 / 会话列表刷新 / 首次进入底部`
- **Task**: Phase 8 conversation metadata/settings bundle with compact header, round count, timestamps, Copy, adaptive round navigation, persisted Preferences, first-entry latest placement and evidence-backed list/detail presentation corrections.
- **Working branch / PR**: `dev/conversation-round-count-20260828`; PR #27.
- **Exact accepted product/config source**: `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- **Accepted Runtime Candidate**: `DEV-conversation-round-count-0.1.0-b38`, `0.1.0 (38)`.
- **Runtime Artifact**: `9708425762`.
- **IPA SHA-256**: `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- **Main at last product validation**: `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- Stable/Frozen before merge: No/No. The tested Phase 8 scope may be promoted to Stable only after final merge/state sync; Frozen remains No.

## Runtime truth — accepted 2026-08-29

The user tested exact b38 after b37 had already removed long-conversation geometry stutter and replied **“没问题了”**.

This accepts the current b38 behavior for the recorded iPhone/iOS17 scope:

- b37 deterministic message geometry / bounded long-message presentation continues to remove the severe long-conversation and right-side scroll-indicator stutter previously reproduced in b36.
- b38 restores genuine continuous full-distance previous/next animation without reintroducing the reported stutter.
- Previous/next keeps the authoritative user-message round-start target and b37 O(1) deterministic target offset.
- Rapid retargeting remains presentation-only through one transient semantic cursor + one cancellable animator; real drag retakes viewport ownership.
- No hard final correction snap is required by the accepted path.

No new diagnostics export accompanied this acceptance, so do not invent numerical b38 Runtime timing.

## Accepted durable architecture / behavior

- `ConversationRepository` remains sole conversation/list/read/recovery authority.
- `AuthSessionStore` remains sole verified auth/account authority; default persistent `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- `ConversationListCacheStore` remains storage-only.
- `AppPreferences` remains sole persisted settings owner.
- `ConversationRoundProjection` remains derived semantic round data; every visible authoritative user message starts one round.
- b37 `ConversationMessagePresentationProjection` is ephemeral presentation-only virtualization: bounded plain-text chunks, deterministic row metrics/prefix offsets and message→first-row mapping derive from authoritative messages.
- `ConversationMessageCell` uses deterministic manual frame layout for bounded display chunks; Copy still reads the complete authoritative visible message.
- b38 round navigation uses the already-derived target offset and one `UIViewPropertyAnimator(duration: 0.35, curve: .easeInOut)` from current viewport to target; short/long distance use one method.
- Physical-bottom/rubber-band direction, recipient/internal filtering, compact assistant Copy, timestamps/preferences/header, first-entry latest, A/B anchors, list/cache reconciliation and Sync/Reload behavior remain accepted.
- b26 authoritative-total stale-row cap (`30 -> 29`, repeated `29/29`) and b29 right-top refresh/top-blank correction remain part of this Phase 8 accepted scope.
- Rich Markdown/citation rendering remains future `DEV-message-rendering`; do not mix it into this completed Work.

## Candidate / evidence progression

- b24 identity rejected/permanently reserved; b25-b35 Runtime partial/failing/superseded.
- b36 Runtime identified long-message/table geometry as the real blocker: 47 direct-position samples median ~187ms, P90 ~780ms, max ~3952ms; ordinary right-side scroll-indicator dragging also severely stuttered; one 161-visible-message table geometry expanded from ~13.8k to ~154.6k points as giant self-sizing rows were realized.
- b37 replaced deferred giant-row self-sizing with bounded chunks, deterministic row heights/prefix offsets and manual cell layout. User Runtime: **“这次确实不卡了”** — accepted no-stutter performance baseline.
- b38 retained all b37 geometry code and changed only round-jump presentation + Candidate identity: removed ~120pt lead teleport, continuously animated from current offset to O(1) deterministic target for 0.35s ease-in-out.
- Exact b38 parent→product diff: workflow 2+/2-, Xcode identity 4+/4-, `ConversationFeature.swift` 8+/20- only.

## Exact b38 validation evidence

- Exact product source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Exact push Run / Job `33230823568` / `99043233637` — success.
- Runtime Artifact `9708425762`; ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`; SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: `0.1.0 (38)`, Candidate b38, source marker `0d1801137e4e`, MinimumOSVersion 14.0, bundle `com.whitesharkssw.chatgptclient`, Mach-O arm64.
- Product-head merge-view Run / Job `33230825189` / `99043238346` succeeded on synthetic merge `fd1ed7508f04e9045b99239cad88dca8f6e01450` against then-current `main@a6e3b2bc...`. That merge-view predates later docs-only branch commits and must not be reused as the final current-head merge check.
- Runtime/manual/real-device: **Accepted** on the recorded iPhone/iOS17 scope by the user's latest explicit result.

## Finalization batch recovery point

Known state before this checkpoint write:

- Real development branch head: `5ca8e07eaa22864abb23c8385e3290ea556b616d` (docs-only after exact b38 product source).
- Exact accepted product source remains `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Main last verified `a6e3b2bc185b8d5df90b846040387262a64e6154`.
- PR #27 last product-head validation: open / mergeable / not merged.
- `docs/project/current/dev/` contained only this Active Work plus README; no parallel development conflict.

Planned finalization batches:

1. **Batch A — durable acceptance sync**: update current Phase 8 truth in `PROJECT_PROFILE.md`, `PROJECT_STATE.md`, `MODULE_STATUS.md`, `PROJECT_SPECIFIC_RULES.md`, `DEVELOPMENT_PLAN.md`, `TECHNICAL_DECISIONS.md`, and `BUILD_TEST_INDEX.md`. Preserve exact b38 product identity; do not touch product code/config.
2. **Batch B — final merge guard**: re-read real branch head, main, PR #27, active checkpoints; compare docs-only commits against exact product source; obtain a fresh current-head/current-main PR merge view and verify no material product change since accepted source.
3. **Batch C — merge**: merge PR #27 only if the above state is consistent and mergeable, using expected PR head SHA.
4. **Batch D — post-merge completion on main**: record actual merge commit/current main and Stable/Frozen state in durable docs, then remove only `docs/project/current/dev/DEV-conversation-round-count.md`.

Confirmed complete after this write: Runtime acceptance checkpoint only.

Still pending: durable acceptance sync, fresh current-head merge guard, PR merge, post-merge final docs, checkpoint removal.

Recovery must never rebuild/reuse b24-b38 Candidate identities or redefine exact accepted b38 product source.

## Evidence boundary

- Code written: Yes.
- Static/source audit: Passed.
- Exact push CI: Passed.
- Identity-valid Artifact: Produced and independently verified.
- Runtime/manual/real-device: **Accepted** for recorded b38 iPhone/iOS17 scope.
- Stable: Pending final merge/state sync.
- Frozen: No.

## Next exact action

Complete Batch A durable acceptance sync, then re-check current branch/main/PR/active-task state and obtain a fresh current-head merge view before merging PR #27. After merge, record the real merge SHA/current main, promote the tested Phase 8 scope to Stable (Frozen No), and remove only this checkpoint.