# DEV-send-stream

## Status

**Active**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail`
- **Task**: Implement the first evidence-backed production text Send/new-conversation/streaming-response path, including exact response ownership, Stop integration, user-visible reasoning compatibility, follow-tail and new-chat identity handoff.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; predecessor `DEV-conversation-round-count` Stable b38 merged by PR #27.
- **Working branch / PR**: `dev/send-stream-20260829`; PR #29 open + mergeable. Exact b42 product/config source is `e8946e48a0b5ad86b402faf5eabba627e3393adf`; the branch/PR head before this final checkpoint write was docs-only `ba79bca19d07c47a1e40f97cc1303e4e42945ae7`. This checkpoint write may advance that head without redefining the b42 product source. `main` remained unchanged at the recorded baseline through b42 publication. No peer Active development checkpoint exists.
- **State owners remain fixed**: `ConversationRepository` = sole conversation/list/detail/recovery/response authority; `AuthSessionStore` = auth/account authority; default persistent `WKWebsiteDataStore` = sole persistent auth-secret authority; `ConversationDetailViewController` = viewport/scroll/follow-tail presentation owner. No second repository/global `isStreaming`, hidden production WebView transport, copied persistent credentials, retry/watchdog/fallback endpoints, anti-abuse solver/bypass, or hidden-CoT presentation.

## Candidate history / exact evidence

- **b39** `DEV-send-stream-0.1.0-b39`: source `3a957b0a7839b28491a9166b454aec852ab70e76`; Run `33233467811`; Job `99050223061`; Artifact `9709203437`; ZIP `sha256:087d1ab88ed359a22a44ea314771047a159434c5f2c5425e4ee43302f68581d7`; IPA SHA `8768b9bb8e7c9170773cbe8a03214435f05991758e9d7428ae6b59a280668593`. CI/package valid, no Runtime; superseded before Runtime; never reuse.
- **b40** `DEV-send-stream-0.1.0-b40`: source `f4a7abbad52f00e10f4c0e0fc14bcb7686187f2b`; Run `33233754433`; Job `99051001206`; Artifact `9709286294`; ZIP `sha256:e930f312255ff09736151076da1c2b4ab6ec5612f44a64edca323f6f00d7c6e8`; IPA SHA `bfbcf5789bca42463da08486ffe69b2e2dc5ff36235bc87954f49cda44b4d4f7`. Exact real-device protocol-probe Runtime accepted on iPhone/iOS17; not native production Send acceptance.
- **b41** `DEV-send-stream-0.1.0-b41`: source `a2899e8bfdacd9b642c026c14f484735c1ac60fa`; push Run `33234523162`; Job `99053041864`; Artifact `9709515645`; ZIP `sha256:1707aa7d51956ece34301d1143513aeff2358c4ae3ccded2e23a052110811c31`; IPA `ChatGPTClient-0.1.0-b41-dev-send-stream.ipa`; IPA SHA `0941b73ccbaf7552870adc85aa03e631dcb4181ab13df14da6b5041b860acc83`. Exact real-device protocol probe accepted on iPhone/iOS17 and additionally evidenced server Stop; not native production Send acceptance.
- **b41 merge-view**: PR Run `33234687008`; Job `99053473260`; build/inspect/upload success. CI/package evidence only.
- **b42** `DEV-send-stream-0.1.0-b42`: exact product/config source `e8946e48a0b5ad86b402faf5eabba627e3393adf`; push Run `33235622532`; Job `99055977981`; Artifact `9709824510`; Artifact ZIP digest `sha256:28b588f91904cf4a3c79e81d4bfcb8ad2336642729dcd092a4cdfffd38fffcdb`; IPA `ChatGPTClient-0.1.0-b42-dev-send-stream.ipa`; IPA SHA `c6d1d421ab05a2294784223400291f0dc1683b638b2647ae85b2d9d4f3fcb85b`.
- **b42 package identity**: independently inspected embedded `CFBundleShortVersionString=0.1.0`, `CFBundleVersion=42`, `DiagnosticsCandidate=DEV-send-stream-0.1.0-b42`, `DiagnosticsSourceCommit=e8946e48a0b5`, Release package, arm64 executable, `MinimumOSVersion=14.0`, device family `[1,2]`.
- **b42 merge-view**: PR Run `33235623896`; Job `99055982148`; build/inspect/upload success against unchanged main. Merge-view evidence only; exact push Artifact `9709824510` remains the Runtime Candidate.
- **Validation state**: b42 Code written + exact push CI passed + identity-valid Artifact produced + PR merge-view CI passed. **b42 Runtime/manual pending. Stable/Frozen: No.**

## Accepted protocol evidence through b41

### Send / stream

- Existing and new Sends both use `POST /backend-api/f/conversation`, HTTP 200 `text/event-stream`.
- Existing request contains `conversation_id`; new request omits it.
- Existing primary-assistant safe semantics observed in b41: `action=next`, `client_prepare_state=success`, `conversation_mode.kind=primary_assistant`, `model=gpt-5-6-thinking`, `thinking_effort=extended`, `supported_encodings=["v1"]`, `supports_buffering=true`, `enable_message_followups=true`, `force_parallel_switch=auto`, `paragen_cot_summary_display_override=allow`, one user text message, one response contract protocol v1.
- Existing conversation ID shape is opaque; user-message and parent IDs are UUID-shaped and distinct.
- SSE begins with `"v1"`. Normal completion has early `resume_conversation_token`, input/message events, assistant response/message identity, patch-based text/status/end-turn updates, `message_stream_complete`, trailing `conversation_detail_metadata`, then `[DONE]`.
- New authoritative conversation identity appears by `resume_conversation_token`; any repository pending identity must end at first validated server conversation ID via one atomic adoption/re-key.
- New chat emits `title_generation`.
- b41's second new-chat sample was `conversation_mode.kind=gizmo_interaction` with `gizmo_id`; its mode/parent details are **not** default-new-chat authority and must not be generalized.
- System/tool/model-context stream records remain internal unless a separate user-visible contract is evidenced. No hidden chain-of-thought presentation.

### Stop

- Official server Stop is `POST /backend-api/stop_conversation`.
- Observed body: `{ conversation_id: string, exclude_async_types: [] }`.
- Request includes current transient auth/client headers and `x-conduit-token`.
- Observed response: HTTP 200 `application/json`, shape `{ status: string, last_message_id: null }`.
- The stopped Send stream ended with `doneSeen=false` after 21 frames and without normal `message_stream_complete` / `[DONE]` tail.
- Production rule: Stop is an exact response-owner terminal path. Local transport cancellation alone is never server Stop proof. A successful server Stop acknowledgement for the exact owned conversation/response transitions once to `user-stopped`; subsequent stream close must not become a second failure/completion terminal.
- Wire Stop body is conversation-scoped; repository still permits at most one active response per conversation until stronger concurrency evidence exists so Stop maps deterministically to the exact owned active response.

### Precursor / protection chain

- `conversation/init` returns current model/limit metadata structure.
- `/backend-api/f/conversation/prepare` returns `{ conduit_token: string, status: string }`; Send uses `x-conduit-token`.
- Sentinel prepare structure: `{ persona, prepare_token, proofofwork:{required,seed,difficulty}, so:{required,collector_dx,snapshot_dx}, turnstile:{required,dx} }`.
- Sentinel finalize request structure: `{ prepare_token, proofofwork, turnstile }`; response structure: `{ token, persona, expire_after, expire_at }`.
- Successful Send carries Sentinel requirements/proof/turnstile header names. Values are never captured or persisted.
- b41 did **not** reveal the values of the `required` booleans or whether finalize proof/turnstile strings were empty. That ambiguity is the only current P0 blocker to deciding whether native precursor flow is normally implementable without anti-abuse challenge execution.
- Never implement/copy a PoW/Turnstile/Sentinel solver, challenge bypass, browser fingerprint replay, or captured proof/token replay.

## b42 exact scope / Runtime decision gate

b42 changes only the visible diagnostic probe plus Candidate identity. It adds no production Send/Stream code. It records only:

1. `proofofwork.required`, `turnstile.required`, `so.required` booleans and prepare-token presence.
2. Sentinel-finalize `prepare_token` / `proofofwork` / `turnstile` **presence/emptiness only**, never values or reconstructable lengths.
3. Conversation-prepare short non-secret semantics, ID shapes/counts and response `status` + conduit-token presence.
4. Stop response short `status` + last-message-ID shape if naturally exercised.
5. Current init default/intended model short enums.

### Decision after exact b42 Runtime

- **Path A — normal native precursor permitted** only if exact Runtime proves no browser anti-abuse challenge execution is required for the successful path: applicable required flags are false and proof/turnstile submissions are empty/absent as applicable, with all remaining fields sourced normally inside the existing auth boundary. Then immediately implement incremental authenticated transport + Repository response lifecycle/new-chat adoption/Stop/follow-tail under a later unique Candidate.
- **Path B — native transport blocked under current architecture** if any required anti-abuse challenge is true or successful Send depends on non-empty browser-generated PoW/Turnstile/other challenge output. Record the block; do not circumvent. Production Send remains unwritten rather than introducing a prohibited bypass.

## Current human-only gate

Install exact **b42** Runtime Artifact `9709824510` and run one narrow pass:

1. Settings → `Send 协议探测（诊断）`.
2. Use **default ChatGPT / primary assistant**, not a custom GPT/Gizmo.
3. Start one **new** default conversation and send one short non-sensitive text message; allow it to complete normally.
4. Return to Settings and export diagnostics JSON.
5. Stop does not need to be repeated; b41 already evidenced its route/ack/stream-close behavior. If exercised naturally, b42 will safely record only the additional short status/shape fields.

No Cookie, Authorization, prompt/answer text, raw IDs, Sentinel seed/difficulty/dx, proof values, Turnstile values, requirements token values or conduit-token values should be supplied.

## Batch recovery point

- **Current exact product source**: `e8946e48a0b5ad86b402faf5eabba627e3393adf`; exact push Artifact `9709824510`; main remained `34811877896ca88c6656be6676f5466a19931ce6` through publication.
- **Confirmed complete / never replay**: b39-b42 identity emission; b40/b41 Runtime; b41 Stop evidence; b42 atomic product/config commit + fast-forward; b42 push CI/Artifact/package inspection; b42 PR merge-view CI; b41 runtime-evidence file; BUILD_TEST_INDEX b41/b42 update and evidence-transcription correction; PR #29 body refresh.
- **Docs Batch C complete**: checkpoint, runtime evidence, build index and PR body are synchronized. The product source remains `e8946e48...`; all later branch commits are docs-only and must not be treated as new Runtime Candidates.
- **Human gate**: exact b42 default-primary-assistant new-chat diagnostic export.
- **Recovery must not touch/reuse**: b39-b42 identities/Artifacts; Stable b38 behavior/state-owner contracts; other task checkpoints; main branch.
- **Next exact action**: on receipt of exact b42 diagnostics, verify metadata/source identity, read required booleans + proof/turnstile presence facts, choose Path A or Path B immediately, update durable evidence/checkpoint, and continue autonomously where permitted.
