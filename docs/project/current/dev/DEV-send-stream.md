# DEV-send-stream

## Status

**Active**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail`
- **Task**: Implement the first evidence-backed production text Send/new-conversation/streaming-response path, including exact response ownership, Stop integration, user-visible reasoning compatibility, follow-tail and new-chat identity handoff.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; predecessor `DEV-conversation-round-count` Stable b38 merged by PR #27. Current branch `dev/send-stream-20260829`; no peer Active development checkpoint and no open PR as of this checkpoint.
- **State owners remain fixed**: `ConversationRepository` = sole conversation/list/detail/recovery/future-response authority; `AuthSessionStore` = auth/account authority; default persistent `WKWebsiteDataStore` = sole persistent auth-secret authority; `ConversationDetailViewController` = viewport/scroll/follow-tail presentation owner. Do not create a second repository, global `isStreaming`, hidden production WebView transport, copied persistent credentials, retry/watchdog/fallback endpoints, or hidden-CoT presentation.

## Candidate history

- **b39** `DEV-send-stream-0.1.0-b39`: exact source `3a957b0a7839b28491a9166b454aec852ab70e76`; Run `33233467811`; Job `99050223061`; Artifact `9709203437`; ZIP `sha256:087d1ab88ed359a22a44ea314771047a159434c5f2c5425e4ee43302f68581d7`; IPA SHA `8768b9bb8e7c9170773cbe8a03214435f05991758e9d7428ae6b59a280668593`. CI/package valid, **no Runtime; superseded before Runtime; never reuse** because nested structure sanitation boxed dictionary values incorrectly.
- **b40** `DEV-send-stream-0.1.0-b40`: exact product/config source `f4a7abbad52f00e10f4c0e0fc14bcb7686187f2b`; push Run `33233754433`; Job `99051001206`; Artifact `9709286294`; ZIP `sha256:e930f312255ff09736151076da1c2b4ab6ec5612f44a64edca323f6f00d7c6e8`; IPA SHA `bfbcf5789bca42463da08486ffe69b2e2dc5ff36235bc87954f49cda44b4d4f7`; embedded `0.1.0 (40)`, Candidate b40, source marker `f4a7abbad52f`, Release, arm64, minimum iOS14, device family `[1,2]`.
- **b40 Runtime protocol evidence**: user exported diagnostics from exact b40 on **iPhone / iOS 17.0** at `2026-08-29T04:34:36Z`; metadata matches Candidate b40/build 40/source `f4a7abbad52f`. This is accepted real-device **protocol probe Runtime evidence**, not acceptance of a native production Send implementation.

## b40 accepted protocol facts

### Existing vs new conversation request

- Both real Sends are `POST /backend-api/f/conversation` and returned HTTP 200 `text/event-stream`.
- Existing-chat Send request body contained `conversation_id`.
- New-chat Send request body was structurally identical **except `conversation_id` was absent**. The probe's URL-derived `pageKind` had already changed to `existing_conversation` by request time, so `pageKind` is not authoritative for new-chat classification. New-chat stream also emitted `title_generation`, independently supporting the classification.
- Shared top-level body keys observed: `action`, `client_contextual_info`, `client_prepare_state`, `conversation_mode`, `enable_message_followups`, `force_parallel_switch`, `local_function_names`, `messages`, `model`, `model_response_contracts`, `paragen_cot_summary_display_override`, `parent_message_id`, `supported_encodings`, `supports_buffering`, `system_hints`, `thinking_effort`, `timezone`, `timezone_offset_min`; existing chat additionally had `conversation_id`.
- Browser Send carried names including `authorization`, `chatgpt-account-id` when applicable, client/session/device/build/route headers and the protection/conduit headers `openai-sentinel-chat-requirements-token`, `openai-sentinel-proof-token`, `openai-sentinel-turnstile-token`, `x-conduit-token`. Values were intentionally not captured.
- `conversation/init`, Sentinel prepare/finalize and `/f/conversation/prepare` were observed as normal official-page precursor/support requests with HTTP 200 JSON, but response structure/value provenance is not yet captured.

### Stream grammar

- SSE starts with `data: "v1"` marker and terminates with `[DONE]` in both captures.
- Existing-chat capture: first usable structural event ~544 ms; 12 SSE data frames; observed `resume_conversation_token`, `input_message`, assistant `in_progress` text add with authoritative message identity present, `message_marker`, patch batch, `server_ste_metadata`, `message_stream_complete`, `conversation_detail_metadata`, then `[DONE]`.
- New-chat capture: first usable structural event ~622 ms; 23 frames; additionally included initial system/user/model-context events and `title_generation`; visible assistant later entered `in_progress` text. Internal/system/model-context events must not be promoted to user-visible messages merely because they carry message IDs.
- Text delta evidence: patch batch appends `/message/content/parts/0`, replaces `/message/status`, replaces `/message/end_turn`, and appends `/message/metadata`.
- Both streams emitted `message_stream_complete` before `conversation_detail_metadata` and final `[DONE]`. Therefore connection close is not the only terminal signal; production parser must be deterministic and tolerate the evidenced post-complete metadata before `[DONE]`.
- New conversation identity is already present by `resume_conversation_token`; thus a pending local token may be required only until this first authoritative identity event, then one atomic Repository re-key/adoption must occur.
- `title_generation` is evidenced for the new chat; temporary `新对话` remains presentation-only until authoritative title/list state arrives.

### Still Unknown / blocked

- Exact safe values for non-secret protocol enums/strings (`action`, `conversation_mode.kind`, model/mode fields, `client_prepare_state`, `thinking_effort`, supported encoding, etc.) are not captured yet.
- Exact user-message/parent ID shape and relation are not captured yet; raw IDs must remain unlogged.
- Exact JSON/header structure of `conversation/init`, `/f/conversation/prepare`, Sentinel prepare/finalize responses is not captured yet. This matters because current native `AuthTransientSession` only provides cookies + bearer Authorization and has **no evidence-backed source** for the four observed protection/conduit header values.
- Do **not** solve/bypass Sentinel/Turnstile/PoW or replay captured browser proof values. If normal response-structure evidence shows those values require browser-only anti-abuse challenge execution, native production Send is blocked under the current auth boundary and must be reported as such rather than bypassed.
- Stop route/target/ack remains Unknown; no Stop was exercised in b40.
- No explicit user-visible reasoning event was observed. `thinking_effort` request field alone is not evidence of visible reasoning; hidden/system/model-context stream nodes must not be exposed as chain-of-thought.

## Next Candidate / exact action

- **Allocated now**: `DEV-send-stream-0.1.0-b41` / `0.1.0 (41)`. Allocation gate: current `main` unchanged at `34811877896ca88c6656be6676f5466a19931ce6`; only this Active checkpoint exists; open PR list empty; repository search found no b41 identity. b41 is reserved to this Work and must never be reused after emission.
- b41 scope is **diagnostic evidence refinement only**, not production Send: extend the visible official-Web probe to record only (a) whitelisted non-secret Send enum values/booleans/counts, (b) opaque-ID shape/equality relationships without raw IDs, (c) response header names + JSON key/type structure for init/prepare/Sentinel support calls, and (d) direct/nested conversation/message identity source enums for first-seen stream signatures. No prompt/answer text, raw payload, raw IDs, auth/cookie/token/proof values.
- If a Stop action is naturally exercised in b41, keep the existing route/body structural observer and record only safe structure; do not require Stop to proceed with the response-structure evidence pass.
- After b41 structure evidence, decide one of two evidence-backed paths: **A)** normal native precursor flow is implementable without bypass -> implement authenticated incremental transport + Repository response lifecycle in b42+; **B)** protection values depend on browser-only anti-abuse challenge -> mark native Send transport blocked under current architecture and do not circumvent.

## Batch recovery point

Complete and do not replay: startup/preflight; restored `SEND_STREAM_PREFLIGHT.md`; b39 supersession; b40 one-line correction + exact CI/package; exact b40 real-device existing/new Send probe. Current branch head before this checkpoint was docs-only head `6e23d5c8b2289fe101929e45a1892221986cf47b`; exact tested b40 product source remains `f4a7abbad52f00e10f4c0e0fc14bcb7686187f2b`. Next deterministic write chain: implement b41 probe refinement, atomically roll Xcode/workflow identity 40→41 before triggering Candidate CI, then verify exact b41 Artifact identity. `BUILD_TEST_INDEX.md` still needs durable b39/b40/b41 rows; update it in this same development cycle once b41 exact evidence exists. PR may be opened at any point after current branch/head verification; merge-view CI is evidence only and never substitutes for Runtime.