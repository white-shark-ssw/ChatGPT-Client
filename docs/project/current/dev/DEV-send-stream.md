# DEV-send-stream

## Status

**Active**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail`
- **Task**: Implement the first evidence-backed production text Send/new-conversation/streaming-response path, including exact response ownership, Stop integration, user-visible reasoning compatibility, follow-tail and new-chat identity handoff.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; predecessor `DEV-conversation-round-count` Stable b38 merged by PR #27.
- **Working branch / PR**: `dev/send-stream-20260829`; PR #29 open and mergeable; current docs/index head before this checkpoint `fc7a055bd6abde0d37d0bbd85d400d017dbaddc6`. Exact current b41 product/config source remains `a2899e8bfdacd9b642c026c14f484735c1ac60fa` because later commits are documentation/index only.
- **State owners remain fixed**: `ConversationRepository` = sole conversation/list/detail/recovery/future-response authority; `AuthSessionStore` = auth/account authority; default persistent `WKWebsiteDataStore` = sole persistent auth-secret authority; `ConversationDetailViewController` = viewport/scroll/follow-tail presentation owner. Do not create a second repository, global `isStreaming`, hidden production WebView transport, copied persistent credentials, retry/watchdog/fallback endpoints, or hidden-CoT presentation.

## Candidate history

- **b39** `DEV-send-stream-0.1.0-b39`: exact source `3a957b0a7839b28491a9166b454aec852ab70e76`; Run `33233467811`; Job `99050223061`; Artifact `9709203437`; ZIP `sha256:087d1ab88ed359a22a44ea314771047a159434c5f2c5425e4ee43302f68581d7`; IPA SHA `8768b9bb8e7c9170773cbe8a03214435f05991758e9d7428ae6b59a280668593`. CI/package valid, **no Runtime; superseded before Runtime; never reuse** because nested structure sanitation boxed dictionary values incorrectly.
- **b40** `DEV-send-stream-0.1.0-b40`: exact product/config source `f4a7abbad52f00e10f4c0e0fc14bcb7686187f2b`; Run `33233754433`; Job `99051001206`; Artifact `9709286294`; ZIP `sha256:e930f312255ff09736151076da1c2b4ab6ec5612f44a64edca323f6f00d7c6e8`; IPA SHA `bfbcf5789bca42463da08486ffe69b2e2dc5ff36235bc87954f49cda44b4d4f7`. Exact real-device protocol-probe Runtime accepted on iPhone/iOS17; not native production Send acceptance.
- **b41** `DEV-send-stream-0.1.0-b41`: exact product/config source `a2899e8bfdacd9b642c026c14f484735c1ac60fa`; push Run `33234523162`; Job `99053041864`; Artifact `9709515645`; Artifact ZIP digest `sha256:1707aa7d51956ece34301d1143513aeff2358c4ae3ccded2e23a052110811c31`; exact IPA `ChatGPTClient-0.1.0-b41-dev-send-stream.ipa`; IPA SHA `0941b73ccbaf7552870adc85aa03e631dcb4181ab13df14da6b5041b860acc83`; embedded identity independently verified as `0.1.0 (41)`, Candidate b41, source marker `a2899e8bfdac`, arm64, minimum iOS14.0, device family `[1,2]`.
- **b41 PR merge evidence**: PR #29 mergeable against unchanged `main`; pull-request Run `33234687008`; Job `99053473260`; build/inspect/upload all success. This is merge-view CI/package evidence only and does **not** replace the exact push Artifact `9709515645` for Runtime.
- **Durable index**: `docs/project/BUILD_TEST_INDEX.md` now records b39, b40 and b41 plus a Phase 9 evidence boundary. `docs/project/runtime-evidence/DEV-send-stream-b40-protocol.md` records the accepted b40 protocol Runtime boundary.

## b40 accepted protocol facts

### Existing vs new conversation request

- Both real Sends are `POST /backend-api/f/conversation` and returned HTTP 200 `text/event-stream`.
- Existing-chat request contained `conversation_id`; new-chat request omitted `conversation_id` while the remaining top-level structure matched.
- The probe's URL-derived `pageKind` had already changed to `existing_conversation` by the new-chat fetch, so URL page kind is not authoritative for new-chat classification. New-chat stream also emitted `title_generation`, independently supporting the classification.
- Shared body keys observed: `action`, `client_contextual_info`, `client_prepare_state`, `conversation_mode`, `enable_message_followups`, `force_parallel_switch`, `local_function_names`, `messages`, `model`, `model_response_contracts`, `paragen_cot_summary_display_override`, `parent_message_id`, `supported_encodings`, `supports_buffering`, `system_hints`, `thinking_effort`, `timezone`, `timezone_offset_min`; existing chat additionally had `conversation_id`.
- Successful browser Send carried protection/conduit header names `openai-sentinel-chat-requirements-token`, `openai-sentinel-proof-token`, `openai-sentinel-turnstile-token`, `x-conduit-token`. Values were intentionally never captured.
- `conversation/init`, Sentinel prepare/finalize and `/f/conversation/prepare` were observed as official-page precursor/support requests with HTTP 200 JSON.

### Stream grammar

- SSE starts with `data: "v1"` and terminates with `[DONE]` in both captures.
- Existing capture first structural frame ~544 ms, 12 frames; new-chat capture ~622 ms, 23 frames.
- Observed lifecycle includes early `resume_conversation_token` with conversation identity, `input_message`, assistant text `in_progress`, message markers, patch batches, `server_ste_metadata`, `message_stream_complete`, post-complete `conversation_detail_metadata`, then `[DONE]`.
- Text patch evidence appends `/message/content/parts/0`, replaces `/message/status`, replaces `/message/end_turn`, and appends `/message/metadata`.
- New chat emitted `title_generation`.
- System/user/model-context stream records can carry message identities but are not automatically user-visible assistant content. Hidden/internal context must not be exposed as chain-of-thought.
- Because `message_stream_complete` precedes post-complete metadata and `[DONE]`, connection close is not the only terminal signal; production parser must commit terminal state exactly once while tolerating evidenced trailing metadata.
- New authoritative conversation identity appears early enough that any local pending identity only needs to survive until first validated server conversation identity, then Repository performs one atomic adoption/re-key.

## b41 evidence refinement

b41 remains visible official-Web **diagnostic only** and is not production chat transport. It adds only privacy-safe evidence needed to choose the implementation path:

- whitelisted short non-secret request protocol values (`action`, model, prepare state, conversation mode kind, thinking effort, encodings and selected booleans/counts);
- opaque ID **shape/equality only**, never raw IDs;
- support-response header **names** and JSON **key/type** structure for init/prepare/Sentinel support calls, never token/proof values;
- stream event/value key names plus enums describing where conversation/message identity first appears (`conversation_id`, `v.conversation_id`, `message.id`, etc.);
- Request-clone body observation so fetches constructed as `Request` are structurally visible without consuming the actual request.

## Still Unknown / blocked

- Exact protection/conduit value provenance is not yet known. Current native `AuthTransientSession` only has copied matching cookies + bearer Authorization and has no evidenced source for the four successful-browser protection/conduit values.
- Do **not** solve/bypass Sentinel/Turnstile/PoW or replay captured browser proof values. If b41 shows the required values depend on browser-only anti-abuse challenge execution, native production Send is blocked under the current auth boundary and must be reported as such rather than circumvented.
- Stop route/target/ack remains Unknown unless naturally exercised during the next probe.
- No explicit user-visible reasoning event was evidenced in b40. `thinking_effort` alone is not visible reasoning evidence.

## Next exact action / Runtime gate

Install exact **b41 Artifact `9709515645`** and use Settings → `Send 协议探测（诊断）`:

1. Send one short non-sensitive message in an existing conversation and wait for completion.
2. Start one new conversation in the same visible official page, send one short non-sensitive message, wait for completion.
3. Return to Settings → export diagnostics JSON and provide that file.
4. Optional only if convenient: during one longer generation press official Stop once; this can add Stop route/shape evidence, but it is not required for the b41 precursor/protection decision.

Do not provide Cookie, Authorization, raw IDs, token/proof values, prompt text or raw network payloads.

After exact b41 diagnostics arrive, choose strictly from evidence: **A)** normal native precursor flow is implementable without bypass → implement incremental authenticated transport + Repository-owned response lifecycle/new-chat adoption/follow-tail in a new unique Candidate; **B)** protection values require browser-only anti-abuse execution → record native Send blocked under current architecture, do not circumvent, and present the supported architectural alternatives.

## Batch recovery point

Complete and do not replay: startup/preflight, durable Send/Stream preflight restoration, b39 supersession, b40 exact CI/package + real-device existing/new protocol probe, b41 evidence-refinement implementation, exact b41 push CI/Artifact/identity verification, PR #29 creation + merge-view CI, BUILD_TEST_INDEX Phase 9 rows and b40 Runtime evidence doc. Current exact b41 product source is `a2899e8bfdacd9b642c026c14f484735c1ac60fa`; later branch changes are docs/index/checkpoint only. Next session/action must inspect the user-provided b41 diagnostics before any production Send code. Never rebuild/reuse b39-b41 under corrected product code.