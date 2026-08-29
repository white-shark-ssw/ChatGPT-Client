# Development Plan — Native iOS ChatGPT Client

_Last updated: 2026-08-29 through valid b43 hybrid CI/Artifact; exact-device Runtime pending._

## Purpose

Durable implementation sequence for the native iOS ChatGPT client. Current real source, exact CI/Artifact evidence, real-device evidence and the user's latest explicit requirements outrank stale plan wording.

Constraints: UIKit native shell/read client, TrollStore IPA, primary tested runtime iPhone/iOS17, deployment target iOS14, private/internal ChatGPT behavior must be evidenced rather than guessed. For ChatGPT-account Send, TD-024 explicitly permits one user-visible official-Web surface after b42 proved the pure-native account-session path is browser-challenge blocked.

## Delivery principles

1. Reach a genuinely usable client early; do not wait for roadmap breadth.
2. Keep one authoritative owner per identity/state domain.
3. Prefer official ChatGPT iOS interaction patterns unless an explicit requirement says otherwise.
4. Do not add speculative retry/fallback/watchdog/duplicate-state machinery.
5. Distinguish Code / Static / CI / Artifact / Runtime / Stable evidence.
6. High-frequency daily-use interactions such as Copy and attachments outrank low-value polish once dependencies exist.
7. Optimize only evidenced bottlenecks, especially for long conversations.
8. The current visible-Web Send exception must remain visible and explicit; it is not pure-native Send and may not be turned into hidden challenge harvesting.

## Usability milestones

- **V0.1 read-use**: native shell + list/detail + manual recovery + accepted cold-start auth warm-up.
- **V0.1 cache-use increment**: account-scoped persistent list snapshot and rapid-relaunch suppression.
- **V0.2 chat-use**: stable multi-conversation ownership + metadata/preferences + Copy + round navigation + usable ChatGPT-account Send. **Option 2 hybrid architecture is selected; b43 is the first valid visible-Web Send Candidate and is awaiting exact-device Runtime.** Native private-API response ownership/Stop/follow-tail remains a separate unimplemented boundary and must not be silently claimed by the Web surface.
- **V0.2 attachment-use increment**: image/file sending + assistant-file tap-download-share. Architecture choice is no longer the blocker, but production attachment transfer still waits for accepted hybrid interaction behavior and evidenced native-picker→official-Web handoff semantics.
- **V0.3 refinement**: Markdown/code/rich-content rendering, conversation previews, export, long-conversation tuning, pagination/search/download manager and remaining daily-use features.

## Completed foundations

- Phase 1 `DEV-app-foundation`: merged Stable.
- Phase 2 `DEV-auth-bootstrap`: merged Stable for tested scope; persistent `WKWebsiteDataStore` is sole persistent auth-secret authority.
- Phase 3 `DEV-protocol-read`: merged accepted diagnostic read scope.
- Phase 4 `DEV-native-read-path`: merged Stable b9; `ConversationRepository` is native conversation owner.
- Phase 5 `DEV-conversation-recovery`: merged Stable b15; PR #10.
- Phase 6 `DEV-multi-conversation-state`: merged Stable b21 for recorded Plus/personal iPhone/iOS17 read-state scope; PR #23; Frozen No.
- Phase 7 `DEV-conversation-list-cache-core`: merged Stable b23 for recorded scope; PR #24; Frozen No.
- **Phase 8 `DEV-conversation-round-count`: merged Stable b38 for recorded iPhone/iOS17 scope; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`; Frozen No.**

### Conversation-entry scroll semantics

- First visible native presentation with **no valid saved reading anchor** defaults to latest/bottom of the current branch without visibly animating through history.
- Loading-placeholder offsets are not reading anchors.
- Once A has a real semantic reading anchor, A -> B -> A restores A.
- Sync/Reload preserve an established resolvable anchor.
- Native active-response follow-tail remains tied to a future authoritative native response owner; do not derive it from hybrid Web DOM observation.

## Phase 8 — `DEV-conversation-round-count` — Completed

### Stable user-facing bundle

- compact detail header: title primary, subdued second-line metadata;
- active-branch round count from authoritative visible user turns;
- historical user/assistant timestamps from authoritative `createTime`;
- assistant visible-text Copy + user native context Copy;
- persisted Preferences for round count, message time and round navigation;
- first-entry latest/bottom when no valid saved reading anchor exists;
- authoritative-total list reconciliation bound and right-top refresh/top-blank presentation corrections;
- one adaptive previous/next round control with accurate semantic user-message targets and genuine continuous animation;
- long-conversation presentation architecture that avoids the severe self-sizing/scrollbar stutter reproduced in b36.

### Stable Phase 8 architecture / interaction

- Round count and navigation share one derived active-branch `ConversationRoundProjection`.
- A visible authoritative user message starts a round. Physical quick-navigation target is the **round-start user message**.
- Tool/reasoning/system/internal-recipient nodes do not create ordinary native chat rounds/rows.
- `ConversationMessagePresentationProjection` is ephemeral presentation-only state: bounded long-message display chunks, deterministic row heights/prefix offsets and message→first-row mapping derive from authoritative messages.
- `ConversationMessageCell` uses deterministic manual frame layout for bounded display chunks. Full-message Copy remains authoritative-message based.
- Real user drag controls viewport intent; programmatic presentation is not user intent.
- Rapid taps advance from the last requested semantic target via one transient cursor; real drag clears/replaces that cursor.
- Physical top/bottom boundaries outrank drag delta, including rubber-band overscroll.
- Short and long jumps use one method.
- Stable b38 presentation: resolve the O(1) deterministic target offset, then continuously animate from the current viewport to that target for 0.35s `.easeInOut` with one cancellable `UIViewPropertyAnimator`.
- Do not reintroduce pre-jump 120pt teleport, `scrollToRow` geometry discovery, end correction snap, debounce, timer, watchdog or retry without new evidence.

### Candidate / Runtime progression

- **b24**: package identity invalid; permanently rejected/reserved.
- **b25-b35**: partial/failing/superseded iterations that established accepted metadata/Copy/list/semantic behavior while exposing navigation defects.
- **b36**: exact Runtime identified the dominant remaining blocker as long-message/table geometry, not animation alone. 47 direct-position samples had median ~187ms, P90 ~780ms, max ~3952ms; ordinary right-side scroll-indicator dragging also severely stuttered; one 161-visible-message table geometry expanded from ~13.8k to ~154.6k points as giant estimated/self-sized rows became realized.
- **b37**: bounded display chunks + deterministic row geometry/prefix offsets + manual frame layout. User exact-device result: **“这次确实不卡了”**. Accepted as the no-stutter geometry/performance baseline.
- **b38**: preserved all b37 geometry and restored genuine continuous full-distance round animation from current viewport to deterministic target. User exact-device result: **“没问题了”**. Accepted and merged as the Stable Phase 8 baseline for recorded scope.

### Exact Stable b38 evidence

- Candidate `DEV-conversation-round-count-0.1.0-b38`, version/build `0.1.0 (38)`.
- Exact tested product/config source `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`.
- Exact push Run/Job `33230823568` / `99043233637`, success.
- Runtime Artifact `9708425762`; ZIP `sha256:50f77adb71bfce20a9fad4b63e4b879db04e23deb257c3810d157e6214730bf6`.
- IPA `ChatGPTClient-0.1.0-b38-dev-conversation-round-count.ipa`; SHA `6dff45ff4b4c0f7edd231fc13ae67720381ecf7c4ecf96899eaf558b59c2185e`.
- Independent package inspection: Candidate b38, `0.1.0 (38)`, source `0d1801137e4e`, iOS14 minimum, arm64.
- Final PR head `57b3efe576dbf187171439a68d6d2dfe2fba0ebc`; exact tested product→final PR head delta was docs-only.
- Fresh pre-merge synthetic merge `8168fc1aad006ab665f13f77972159f633361b61` was clean against then-current `main@a6e3b2bc...`.
- PR #27 actual merge commit `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`.
- Stable / merged for recorded Phase 8 scope; Frozen No.

### Rendering scope boundary

Current native message body remains plain-string presentation. Markdown/table/code/list/link/citation rendering is **not** Phase 8 and belongs future `DEV-message-rendering`. Do not strip raw rich-content markers speculatively.

## Phase 9 — `DEV-send-stream` — Active / b43 Runtime gate

Phase 9 used b39-b42 evidence Candidates to establish current account-session Send behavior and then hit a security/transport boundary. Exact b42 Runtime proved successful default ChatGPT Send requires browser-generated anti-abuse challenge output, so the pure-native/transient-auth route is not being implemented.

### Accepted protocol/security evidence

- Existing and new conversation Web Send use `POST /backend-api/f/conversation`; existing includes `conversation_id`, new omits it.
- Normal response is HTTP 200 `text/event-stream` using `v1`, early authoritative conversation identity, input/message events, assistant patches, `message_stream_complete`, trailing conversation metadata and `[DONE]`; new chat emits `title_generation`.
- Official server Stop is `POST /backend-api/stop_conversation` with `{ conversation_id, exclude_async_types: [] }`, and successful Stop may terminate the Send stream without normal `message_stream_complete` / `[DONE]` tail.
- Exact b42 default-primary-assistant new-chat Runtime shows Sentinel `proofOfWork.required=true`, `turnstile.required=true`, `so.required=true`, followed by non-empty PoW and Turnstile finalize submissions before successful Send.

### Architecture decision — Option 2 selected

- Pure-native/transient-WebKit-auth ChatGPT-account Send remains blocked under TD-023.
- The user explicitly selected TD-024: **native shell/read/navigation + user-visible official-Web Send surface**.
- This is not pure-native Send. The official Web page owns its own normal browser Send/challenge execution while visible.
- Hidden production WebView transport, challenge harvesting, PoW/Turnstile/Sentinel solver/bypass, browser-fingerprint replay/emulation, captured proof/token replay, DOM mirroring/scraping and guessed fallback endpoints remain prohibited.

### First hybrid Candidate — b43

- Candidate `DEV-send-stream-0.1.0-b43`, version/build `0.1.0 (43)`.
- Exact product/config source `f602d68ae95dc6a0f1b32fd996c21f9868c4ec2c`.
- Implementation: one shared process-resident visible `AuthWebViewController.hybridChat` using default persistent WebKit storage, entered explicitly from Settings. It loads official `https://chatgpt.com/` on first visible presentation and ordinarily reuses the resident page after Back -> re-entry without automatic reload.
- No Root or `ConversationFeature.swift` product change; Stable native read/navigation/geometry remains intact in source.
- Push Run/Job `33241032864` / `99070294478`, success.
- PR Run/Job `33241035013` / `99070299776`, success.
- Artifact `9711364573`; ZIP `sha256:1a9516221ec5ece59741f9f2af2483815f09fa47f051ff6a97a67a12d40d4c23`.
- IPA `ChatGPTClient-0.1.0-b43-dev-send-stream.ipa`; SHA `f2de8d02f3da7d9a8a8f58cd3028480a40849095b2b4b21e418e9c2e758d8108`.
- Independent package identity: b43, `0.1.0 (43)`, source `f602d68ae95d`, Release, iOS14 minimum, `[1,2]`, arm64.
- **Evidence status**: Code written / CI passed / Artifact produced / identity verified. Runtime/manual/real-device pending. Stable/Frozen No.

### Identity incident

- Product commit `8be4da4e6af3dad146bc43888ddeb3f4cd2037b8` initially auto-built under stale b42 metadata: Run `33238065644`, Artifact `9710515489`, ZIP `sha256:d76747ea3c524f31e9a6e512119ab3a85172c5c7fc3492d4264a57f93bd86f7f`.
- This Artifact is permanently rejected and must never be installed or cited as Runtime. Legitimate b42 remains Artifact `9709824510`.

### b43 Runtime acceptance gate

On the exact primary iPhone/iOS17 device, b43 must prove:

- first visible hybrid entry is prompt and does not stall the native shell;
- native Back -> re-entry reuses the resident controller/WebView with no avoidable full-page reload (`residentReuse=true` diagnostics expected);
- keyboard show/hide and typing are acceptably responsive;
- one normal visible-Web Send works and streamed response scrolling feels acceptably smooth;
- rapid scrolling does not exhibit material WebView-specific jank relative to the accepted native reading surface;
- official Web `+` / attachment entry responds promptly enough to satisfy the user's high-frequency UX requirement;
- returning to native list/detail/round navigation shows no regression;
- diagnostics contain no prompt/answer body, raw IDs, Cookie/Auth or challenge/proof/token values.

Do not merge PR #29 or call the hybrid Send scope Stable until this exact Runtime gate is accepted.

## Phase 10 — `DEV-attachments`

The architecture-choice blocker is resolved by TD-024, but production attachment work remains **dependency-gated by hybrid Runtime and protocol/UI evidence**.

After b43 or a successor hybrid Candidate establishes acceptable text interaction:

- follow `ATTACHMENT_TRANSFER_PLAN.md`;
- native Photos/document picker entry must begin immediately from local UI and must not wait on Web/network/challenge work;
- current native-picker -> official-Web file handoff behavior must be inspected/evidenced before implementation;
- do not assume programmatic Web file-input population is supported;
- assistant file tap-download-share remains part of the dedicated attachment Work and uses evidenced download semantics;
- no automatic retry/watchdog/timer chains.

## Phase 11 — `DEV-message-rendering`

Implement native rich message presentation for Markdown paragraphs/headings/lists/links, emphasis, inline/fenced code, code-block Copy and tables as needed. Also investigate current user-visible rich annotation/citation markers such as `filecite` from real protocol content. Preserve authoritative visible text and do not expose hidden reasoning/tool/system content. Avoid full-conversation reparse/reload on every stream token.

This phase does not intrinsically depend on hybrid Send acceptance and may be reprioritized independently if the user requests it.

## Phase 12 — `DEV-conversation-list-preview`

Reuse accepted cache owner/store. Prefer list-response preview only when evidenced; otherwise bounded preview comes from Detail/Sync/Reload/Send already obtained through normal activity. Never issue one Detail per row merely to manufacture previews.

## Phase 13 — `DEV-markdown-export`

Export authoritative current user-visible native branch; never scrape mounted cells or hybrid Web DOM.

## Phase 14 — `DEV-long-conversation`

Measure native network / parse-model / first-visible-render / rich-layout timing and optimize only evidenced bottlenecks. Preserve the Stable Phase 8 deterministic geometry unless new evidence justifies a change.

## Phase 15 — remaining daily-use features

Isolated Work IDs for download manager, pagination, background completion, search, rename/archive/delete, edit/regenerate/branch switching, model selection/temporary chat and settings/diagnostics refinement.

Background completion remains dependent on an accepted authoritative response lifecycle; merely having visible-Web Send does not establish native background response ownership.

## Phase 16 — advanced capabilities

Projects, web search, image/multimodal generation, Voice, Memory, Deep Research, GPTs and other capabilities, each only with current protocol/UI evidence.

## Current next action

Install and test exact `DEV-send-stream-0.1.0-b43` / Artifact `9711364573` on the primary iPhone/iOS17 device. The next human gate is b43 Runtime acceptance/rejection of visible hybrid interaction and smoothness. Preserve b39-b43 identities, the rejected accidental Artifact `9710515489`, and the Stable b38 native baseline.
