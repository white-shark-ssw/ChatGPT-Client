# DEV-send-stream

## Status

**Blocked — architecture decision required**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail`
- **Task**: Implement the first evidence-backed production text Send/new-conversation/streaming-response path, including exact response ownership, Stop integration, user-visible reasoning compatibility, follow-tail and new-chat identity handoff.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; predecessor `DEV-conversation-round-count` Stable b38 merged by PR #27.
- **Working branch / PR**: `dev/send-stream-20260829`; PR #29 open + mergeable. Exact b42 product/config source remains `e8946e48a0b5ad86b402faf5eabba627e3393adf`; branch/PR head before this recovery-point write was docs-only `366d03aaf05bb96720a74fbe3cb4bcf29b1d0023`. `main` remained unchanged at the recorded baseline through b42 Runtime review.
- **State-owner boundary remains fixed**: `ConversationRepository` = sole conversation/list/detail/recovery/response authority; `AuthSessionStore` = auth/account authority; default persistent `WKWebsiteDataStore` = sole persistent auth-secret authority. No second repository/global `isStreaming`, hidden production WebView transport, copied persistent credentials, retry/watchdog/fallback endpoints, anti-abuse solver/bypass, browser-fingerprint replay, captured proof/token replay, or hidden-CoT presentation.

## Exact Candidate history

- **b39** `DEV-send-stream-0.1.0-b39`: source `3a957b0a7839b28491a9166b454aec852ab70e76`; Run `33233467811`; Job `99050223061`; Artifact `9709203437`; IPA SHA `8768b9bb8e7c9170773cbe8a03214435f05991758e9d7428ae6b59a280668593`. CI/package valid, no Runtime; superseded before Runtime; never reuse.
- **b40** `DEV-send-stream-0.1.0-b40`: source `f4a7abbad52f00e10f4c0e0fc14bcb7686187f2b`; Run `33233754433`; Job `99051001206`; Artifact `9709286294`; IPA SHA `bfbcf5789bca42463da08486ffe69b2e2dc5ff36235bc87954f49cda44b4d4f7`. Exact protocol-probe Runtime accepted; not native production Send acceptance.
- **b41** `DEV-send-stream-0.1.0-b41`: source `a2899e8bfdacd9b642c026c14f484735c1ac60fa`; Run `33234523162`; Job `99053041864`; Artifact `9709515645`; IPA SHA `0941b73ccbaf7552870adc85aa03e631dcb4181ab13df14da6b5041b860acc83`. Exact protocol-probe Runtime accepted; established primary-assistant Send semantics, precursor structure and real server Stop; not native production Send acceptance.
- **b42** `DEV-send-stream-0.1.0-b42`: exact product/config source `e8946e48a0b5ad86b402faf5eabba627e3393adf`; push Run `33235622532`; Job `99055977981`; Artifact `9709824510`; ZIP `sha256:28b588f91904cf4a3c79e81d4bfcb8ad2336642729dcd092a4cdfffd38fffcdb`; IPA `ChatGPTClient-0.1.0-b42-dev-send-stream.ipa`; IPA SHA `c6d1d421ab05a2294784223400291f0dc1683b638b2647ae85b2d9d4f3fcb85b`; PR merge-view Run `33235623896`; Job `99055982148`, success.
- **b42 package identity**: `0.1.0 (42)`, Candidate b42, source marker `e8946e48a0b5`, Release, arm64, minimum iOS14.0, device family `[1,2]`.

## Exact b42 Runtime — Path B established

User exported exact b42 diagnostics on iPhone / iOS 17.0 at `2026-08-29T05:26:32Z`. Export metadata matches `0.1.0 (42)`, Candidate `DEV-send-stream-0.1.0-b42`, source `e8946e48a0b5`, Release.

Default-new-chat evidence is now authoritative for the tested Plus/personal scope:

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

The original production-native implementation cannot continue safely under the current architecture. A new product/architecture decision is required before code work can resume. Evidence-compatible options are limited to designs that do **not** circumvent the browser anti-abuse system, for example:

1. keep the current native read/recovery client and defer ChatGPT-account Send until an officially supported/non-challenge transport becomes available;
2. explicitly change product architecture to a user-visible official-Web send surface while keeping native read/navigation elsewhere, accepting that this is no longer pure native Send;
3. introduce a separately authenticated officially supported API/product path if the user explicitly wants that different credential/billing/product model; it must not be silently treated as the existing ChatGPT-account session.

Do not choose among these without the user's product decision.

## Batch recovery point — b42 Runtime closure

- **Known branch/PR head before closure chain**: `366d03aaf05bb96720a74fbe3cb4bcf29b1d0023`; PR #29 open/mergeable; exact b42 product source `e8946e48a0b5ad86b402faf5eabba627e3393adf`; main `34811877896ca88c6656be6676f5466a19931ce6`.
- **Confirmed complete / never replay**: b39-b42 Candidate emission; b40/b41/b42 exact device probes; b41 server Stop evidence; b42 push CI/Artifact/package identity; b42 PR merge-view CI. Never reuse b39-b42.
- **Batch A complete by this write**: record exact b42 Runtime + Path B in selected checkpoint before durable-doc chain.
- **Batch B pending**: create b42 runtime-evidence file and update `BUILD_TEST_INDEX.md`.
- **Batch C pending**: update `MODULE_STATUS.md`, `TECHNICAL_DECISIONS.md`, `PROJECT_STATE.md`, and `DEVELOPMENT_PLAN.md` with the current-architecture block; no product/source/config changes.
- **Batch D pending**: refresh PR #29 body and then refresh this checkpoint with actual final docs-only head / next exact action.
- **Recovery must not touch/reuse**: b39-b42 identities/Artifacts; exact b42 product source; Stable b38 product/state-owner contracts; other task checkpoints; main branch.
- **Next exact action**: complete only the pending docs batches, verify GitHub state after each batch, then stop at the architecture-choice human gate. No additional Candidate or product code is justified before that decision.
