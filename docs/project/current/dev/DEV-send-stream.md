# DEV-send-stream

## Status

**Blocked — architecture decision required**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail`
- **Task**: Implement the first evidence-backed production text Send/new-conversation/streaming-response path, including exact response ownership, Stop integration, user-visible reasoning compatibility, follow-tail and new-chat identity handoff.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; predecessor `DEV-conversation-round-count` Stable b38 merged by PR #27.
- **Working branch / PR**: `dev/send-stream-20260829`; PR #29 open + mergeable. Exact b42 product/config source remains `e8946e48a0b5ad86b402faf5eabba627e3393adf`. Verified PR head before this requirement-record write is docs-only `46f7c4e1c0fe6f79e48a194b25ac1fd6139b91e3`; this checkpoint write may advance branch/PR head but does not redefine b42 product source. PR base remains recorded `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **State-owner boundary remains fixed**: `ConversationRepository` = sole conversation/list/detail/recovery/response authority; `AuthSessionStore` = auth/account authority; default persistent `WKWebsiteDataStore` = sole persistent auth-secret authority. No second repository/global `isStreaming`, hidden production WebView transport, copied persistent credentials, retry/watchdog/fallback endpoints, anti-abuse solver/bypass, browser-fingerprint replay, captured proof/token replay, or hidden-CoT presentation.

## Exact Candidate history

- **b39** `DEV-send-stream-0.1.0-b39`: source `3a957b0a7839b28491a9166b454aec852ab70e76`; Run `33233467811`; Job `99050223061`; Artifact `9709203437`; IPA SHA `8768b9bb8e7c9170773cbe8a03214435f05991758e9d7428ae6b59a280668593`. CI/package valid, no Runtime; superseded before Runtime; never reuse.
- **b40** `DEV-send-stream-0.1.0-b40`: source `f4a7abbad52f00e10f4c0e0fc14bcb7686187f2b`; Run `33233754433`; Job `99051001206`; Artifact `9709286294`; IPA SHA `bfbcf5789bca42463da08486ffe69b2e2dc5ff36235bc87954f49cda44b4d4f7`. Exact protocol-probe Runtime accepted; not native production Send acceptance.
- **b41** `DEV-send-stream-0.1.0-b41`: source `a2899e8bfdacd9b642c026c14f484735c1ac60fa`; Run `33234523162`; Job `99053041864`; Artifact `9709515645`; IPA SHA `0941b73ccbaf7552870adc85aa03e631dcb4181ab13df14da6b5041b860acc83`. Exact protocol-probe Runtime accepted; established primary-assistant Send semantics, precursor structure and real server Stop; not native production Send acceptance.
- **b42** `DEV-send-stream-0.1.0-b42`: exact product/config source `e8946e48a0b5ad86b402faf5eabba627e3393adf`; push Run `33235622532`; Job `99055977981`; Artifact `9709824510`; ZIP `sha256:28b588f91904cf4a3c79e81d4bfcb8ad2336642729dcd092a4cdfffd38fffcdb`; IPA `ChatGPTClient-0.1.0-b42-dev-send-stream.ipa`; IPA SHA `c6d1d421ab05a2294784223400291f0dc1683b638b2647ae85b2d9d4f3fcb85b`; PR merge-view Run `33235623896`; Job `99055982148`, success.
- **b42 package identity**: `0.1.0 (42)`, Candidate b42, source marker `e8946e48a0b5`, Release, arm64, minimum iOS14.0, device family `[1,2]`.
- **Validation ladder**: b42 diagnostic code written; exact push CI passed; identity-valid Artifact produced; PR merge-view CI passed; exact real-device protocol/security Runtime accepted. **Native production Send/Stream remains not implemented / not accepted. Stable/Frozen: No.**

## Exact b42 Runtime — Path B established

User exported exact b42 diagnostics on iPhone / iOS 17.0 at `2026-08-29T05:26:32Z`. Export metadata matches `0.1.0 (42)`, Candidate `DEV-send-stream-0.1.0-b42`, source `e8946e48a0b5`, Release.

Default-new-chat evidence is authoritative for the tested Plus/personal scope:

- conversation prepare is `conversationKind=new`, `conversationModeKind=primary_assistant`, model `gpt-5-6-thinking`, encoding `v1`;
- successful `conversation/prepare` returns `status=ok` and a non-empty conduit token;
- Sentinel prepare returned `proofOfWorkRequired=true`, `turnstileRequired=true`, `soRequired=true`, with non-empty prepare token;
- Sentinel finalize request carried **non-empty** `prepare_token`, **non-empty** `proofofwork`, and **non-empty** `turnstile`;
- Sentinel finalize returned HTTP 200 and a non-empty token;
- successful new Send then used `POST /backend-api/f/conversation` -> HTTP 200 `text/event-stream` with the previously accepted `v1`/resume-token/message-patch/title-generation/`message_stream_complete`/metadata/`[DONE]` lifecycle.

### Decision

This exact successful default-primary-assistant Send depends on browser-generated anti-abuse challenge output. Therefore **Path B is selected**: production native Send under the current pure-native/transient-auth architecture is blocked. Do not implement or copy PoW/Turnstile/Sentinel challenge solvers, challenge bypasses, browser fingerprint replay, or captured token/proof replay. Do not add guessed fallback endpoints.

No b43 is justified merely to repeat the same protection decision.

## Accepted protocol facts retained

- Existing/new Send route: `POST /backend-api/f/conversation`; existing includes `conversation_id`, new omits it.
- Normal stream: marker `"v1"`, early authoritative conversation identity, input/message events, assistant message + text/status/end-turn patches, `message_stream_complete`, trailing `conversation_detail_metadata`, `[DONE]`; new chat emits `title_generation`.
- Official server Stop: `POST /backend-api/stop_conversation`, body `{ conversation_id, exclude_async_types: [] }`, HTTP 200 JSON. Stop can end the Send stream without normal `message_stream_complete` / `[DONE]`; production lifecycle would need an exact-owner `user-stopped` terminal path if a future permitted transport exists.
- Internal/system/tool/model-context records remain non-user-visible unless separately evidenced. Never expose hidden chain-of-thought.

## Current human-only architecture gate

The original production-native implementation cannot continue safely under the current architecture. A new product/architecture decision is required before code work can resume. Evidence-compatible options that do not circumvent browser anti-abuse protections are:

1. keep the current native read/recovery client and defer ChatGPT-account Send until an officially supported/non-challenge transport becomes available;
2. explicitly change product architecture to a **user-visible official-Web send surface** while keeping native read/navigation elsewhere, accepting that this is no longer pure native Send;
3. introduce a **separately authenticated officially supported API/product path** if the user explicitly wants that different credential/billing/product model; it must not be silently treated as the existing ChatGPT-account session.

Do not choose among these without the user's product decision.

## Conditional UX requirement if option 2 is chosen

The user added a hard acceptance requirement for the user-visible official-Web send direction: the Web portion must feel **as close as practical to native iOS controls in responsiveness and smoothness** on the recorded primary device/runtime (iPhone 15 Pro Max / iOS 17.0). Merely making Send functional is not sufficient.

If option 2 is selected, implementation and Runtime acceptance must prioritize:

- no avoidable full-page reload on ordinary send/return flows;
- keep the visible official-Web session warm/resident where lifecycle and memory evidence permit instead of reconstructing it for every tap;
- use native UIKit navigation/container transitions around the Web surface;
- preserve immediate keyboard/input/tap response and smooth touch scrolling;
- avoid JS/native bridge chatter or DOM observation that continuously drives presentation/state and causes frame drops;
- do not hide the WebView solely to harvest challenge output for native transport; the official-Web send surface remains user-visible and owns its own browser-side challenge execution;
- evaluate smoothness by exact real-device Runtime, including repeated enter/return, keyboard show/hide, typing, send, streamed response scrolling, rapid scrolling and ordinary navigation. CI/Artifact or simulator smoothness is not acceptance evidence.

This requirement does not prove that a WKWebView can be pixel-for-pixel or frame-for-frame identical to UIKit. If exact-device testing still exposes material WebView jank or web-specific interaction latency after minimal evidence-backed optimization, option 2 is not accepted merely because it works functionally.

### Attachment-entry responsiveness requirement

The user also requires attachment sending to preserve the same native-grade responsiveness. In particular, tapping the composer `+` must not wait noticeably for a Web page load, network request, Sentinel/Turnstile work, upload preparation, or other remote activity before presenting the next local selection UI.

If option 2 is selected and later attachment support is added:

- the `+` interaction must provide immediate local visual response and begin presenting a native iOS attachment action surface / picker in the same user interaction;
- photo/image choice should use the accepted native Photos/PHPicker path and general files should use the accepted native document picker path where current platform semantics allow;
- picker presentation is a local UI action and must not be blocked on ChatGPT network/challenge/upload work;
- privacy-safe diagnostics should measure tap-to-picker/action-surface presentation duration so exact-device Runtime can identify regressions; do not invent a synthetic spinner to mask latency;
- the exact mechanism for handing a user-selected native file into the user-visible official-Web send surface is **Unknown / Unverified** until current WebKit/official-Web behavior is inspected and tested. Do not assume the app can programmatically populate or drive the Web file-input path;
- if official-Web/WebKit constraints force a materially delayed attachment chooser or require an unsafe hidden-browser/challenge workaround, that implementation is not accepted merely because file sending eventually works.

## Durable evidence / docs synchronized

- `docs/project/runtime-evidence/DEV-send-stream-b42-protocol.md` records exact b42 Runtime and Path B.
- `BUILD_TEST_INDEX.md` records b42 Runtime protocol/security evidence and current native architecture block; unrelated historical drift discovered during the long-table write was corrected and verified.
- `MODULE_STATUS.md` marks Streaming/Send blocked under current architecture and Attachments dependency-blocked.
- `TECHNICAL_DECISIONS.md` adds TD-023 for the b42 anti-abuse challenge boundary.
- `PROJECT_STATE.md` records Phase 9 Active but architecture-blocked while preserving Stable b38.
- `DEVELOPMENT_PLAN.md` records Phase 9 block and architecture gate; no b43 is planned by default.
- PR #29 body is synchronized to b42 Path B and explicitly states native production Send is not implemented/accepted.

## Batch recovery point — attachment UX requirement docs

- **Exact product source / Artifact**: `e8946e48a0b5ad86b402faf5eabba627e3393adf` / `9709824510`; these remain the b42 Runtime authority regardless of later docs-only head movement.
- **Known PR head before this requirement write**: `46f7c4e1c0fe6f79e48a194b25ac1fd6139b91e3`; PR #29 open + mergeable; base remains `main@34811877896ca88c6656be6676f5466a19931ce6`.
- **Confirmed complete / never replay**: b39-b42 identities/Artifacts and b42 Runtime closure; option-2 native-grade Web smoothness requirement already recorded.
- **Current docs batch**: this checkpoint now records the new `+` / attachment-picker responsiveness requirement. Pending writes are `ATTACHMENT_TRANSFER_PLAN.md` and `UI_INTERACTION_BASELINE.md` only; no product/config changes and no Candidate allocation.
- **Recovery must not touch/reuse**: b39-b42 identities/Artifacts; exact b42 product source; Stable b38 product/state-owner contracts; other task checkpoints; main branch.
- **Next exact action**: update the attachment plan and UI interaction baseline with immediate local picker presentation + exact-device latency acceptance, verify the docs-only diff, then refresh this checkpoint to mark the batch complete. The architecture choice among options 1/2/3 remains a human gate; this requirement does not itself silently choose option 2.
