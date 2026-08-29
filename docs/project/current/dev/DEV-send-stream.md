# DEV-send-stream

## Status

**Blocked — architecture decision required**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail`
- **Task**: Implement the first evidence-backed production text Send/new-conversation/streaming-response path, including exact response ownership, Stop integration, user-visible reasoning compatibility, follow-tail and new-chat identity handoff.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; predecessor `DEV-conversation-round-count` Stable b38 merged by PR #27.
- **Working branch / PR**: `dev/send-stream-20260829`; PR #29 open + mergeable. Exact b42 product/config source remains `e8946e48a0b5ad86b402faf5eabba627e3393adf`. Verified PR head before this final checkpoint write is docs-only `151dc496e44f665a580a8a584aa86e1f8a20a5c5`; this checkpoint write may advance branch/PR head but does not redefine b42 product source. PR base remains recorded `main@34811877896ca88c6656be6676f5466a19931ce6`.
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

## Durable evidence / docs synchronized

- `docs/project/runtime-evidence/DEV-send-stream-b42-protocol.md` records exact b42 Runtime and Path B.
- `BUILD_TEST_INDEX.md` records b42 Runtime protocol/security evidence and current native architecture block; unrelated historical drift discovered during the long-table write was corrected and verified.
- `MODULE_STATUS.md` marks Streaming/Send blocked under current architecture and Attachments dependency-blocked.
- `TECHNICAL_DECISIONS.md` adds TD-023 for the b42 anti-abuse challenge boundary.
- `PROJECT_STATE.md` records Phase 9 Active but architecture-blocked while preserving Stable b38.
- `DEVELOPMENT_PLAN.md` records Phase 9 block and architecture gate; no b43 is planned by default.
- PR #29 body is synchronized to b42 Path B and explicitly states native production Send is not implemented/accepted.

## Batch recovery point — b42 Runtime closure complete

- **Exact product source / Artifact**: `e8946e48a0b5ad86b402faf5eabba627e3393adf` / `9709824510`; these remain the b42 Runtime authority regardless of later docs-only head movement.
- **Verified docs-only PR head before this checkpoint write**: `151dc496e44f665a580a8a584aa86e1f8a20a5c5`; PR #29 open + mergeable.
- **Batch A complete**: exact b42 Runtime + Path B recorded in checkpoint.
- **Batch B complete**: b42 runtime-evidence file + build index updated; historical drift correction verified.
- **Batch C complete**: module status, technical decision TD-023, project state and roadmap updated. Compare from `1ef9d4f67058191c5c1f06f35af74748439a3b69` to `151dc496e44f665a580a8a584aa86e1f8a20a5c5` contains exactly those four durable docs and no product/config files.
- **Batch D complete**: PR #29 body refreshed; this checkpoint is the final recovery/handoff record.
- **Recovery must not touch/reuse**: b39-b42 identities/Artifacts; exact b42 product source; Stable b38 product/state-owner contracts; other task checkpoints; main branch.
- **Next exact action**: wait for the user's explicit architecture choice among the permitted directions above. Before any resumed code work, re-run normal resume identity/base/conflict guard and allocate a fresh Candidate only if the chosen architecture produces new testable product code. No further product code or Candidate is justified before that decision.
