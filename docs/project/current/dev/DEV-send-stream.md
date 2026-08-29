# DEV-send-stream

## Status

**Active**

- **Work ID**: `DEV-send-stream`
- **Routing aliases / keywords**: `Send/Stream / 发送 / 流式回复 / 新对话 / Stop / reasoning / follow-tail`
- **Task**: Implement the first evidence-backed production text Send/new-conversation/streaming-response path, including exact response ownership, Stop integration, user-visible reasoning compatibility, follow-tail and new-chat identity handoff.
- **Baseline**: `main@34811877896ca88c6656be6676f5466a19931ce6`; predecessor `DEV-conversation-round-count` Stable b38 merged by PR #27.
- **Working branch / PR / current head**: `dev/send-stream-20260829`; PR #29 open + mergeable; actual branch/PR head verified `048915a089bb8c675648b362cd3c47be5e789b83`. `main` remains unchanged at the recorded baseline. No peer Active development checkpoint exists.
- **State owners remain fixed**: `ConversationRepository` = sole conversation/list/detail/recovery/future-response authority; `AuthSessionStore` = auth/account authority; default persistent `WKWebsiteDataStore` = sole persistent auth-secret authority; `ConversationDetailViewController` = viewport/scroll/follow-tail presentation owner. No second repository/global `isStreaming`, hidden production WebView transport, copied persistent credentials, retry/watchdog/fallback endpoints, anti-abuse solver/bypass, or hidden-CoT presentation.

## Candidate history / exact evidence

- **b39** `DEV-send-stream-0.1.0-b39`: exact source `3a957b0a7839b28491a9166b454aec852ab70e76`; Run `33233467811`; Job `99050223061`; Artifact `9709203437`; ZIP `sha256:087d1ab88ed359a22a44ea314771047a159434c5f2c5425e4ee43302f68581d7`; IPA SHA `8768b9bb8e7c9170773cbe8a03214435f05991758e9d7428ae6b59a280668593`. CI/package valid, no Runtime; superseded before Runtime; never reuse.
- **b40** `DEV-send-stream-0.1.0-b40`: exact product/config source `f4a7abbad52f00e10f4c0e0fc14bcb7686187f2b`; Run `33233754433`; Job `99051001206`; Artifact `9709286294`; IPA SHA `bfbcf5789bca42463da08486ffe69b2e2dc5ff36235bc87954f49cda44b4d4f7`. Exact real-device protocol-probe Runtime accepted on iPhone/iOS17; not native production Send acceptance.
- **b41** `DEV-send-stream-0.1.0-b41`: exact product/config source `a2899e8bfdacd9b642c026c14f484735c1ac60fa`; push Run `33234523162`; Job `99053041864`; Artifact `9709515645`; ZIP `sha256:1707aa7d51956ece34301d1143513aeff2358c4ae3ccded2e23a052110811c31`; IPA `ChatGPTClient-0.1.0-b41-dev-send-stream.ipa`; IPA SHA `0941b73ccbaf7552870adc85aa03e631dcb4181ab13df14da6b5041b860acc83`; package identity `0.1.0 (41)`, Candidate b41, source marker `a2899e8bfdac`, arm64, minimum iOS14.0, device family `[1,2]`.
- **b41 PR merge evidence**: PR #29 mergeable against unchanged `main`; pull-request Run `33234687008`; Job `99053473260`; build/inspect/upload all success. Merge-view CI/package evidence only; exact push Artifact remains Runtime authority.

## b40 accepted protocol baseline

- Existing and new Sends both use `POST /backend-api/f/conversation`, HTTP 200 `text/event-stream`.
- Existing request contains `conversation_id`; new request omits it.
- SSE begins with `"v1"` and normal completion includes early `resume_conversation_token`, input/message events, assistant response identity, patch-based text/status/end-turn updates, `message_stream_complete`, trailing conversation metadata and `[DONE]`.
- New conversation identity appears early; any local pending identity exists only until first validated server conversation ID, then Repository performs one atomic adoption/re-key.
- New chat emitted `title_generation`.
- Successful browser Send carries `openai-sentinel-chat-requirements-token`, `openai-sentinel-proof-token`, `openai-sentinel-turnstile-token`, and `x-conduit-token`; values are never captured.

## b41 real-device Runtime — accepted diagnostic facts

User exported exact b41 diagnostics on iPhone / iOS 17.0 at `2026-08-29T05:00:13Z`; metadata matches build 41 / Candidate b41 / source `a2899e8bfdac`. This is protocol-probe Runtime evidence only.

### Existing primary-assistant Send

- `POST /backend-api/f/conversation`, HTTP 200 `text/event-stream`.
- Safe request semantics: `action=next`, `client_prepare_state=success`, `conversation_mode.kind=primary_assistant`, `model=gpt-5-6-thinking`, `thinking_effort=extended`, `supported_encodings=["v1"]`, `supports_buffering=true`, `enable_message_followups=true`, `force_parallel_switch=auto`, `paragen_cot_summary_display_override=allow`, one user text message, one response contract with protocol version 1.
- Existing authoritative conversation ID shape is opaque. First user-message ID and parent-message ID are UUID-shaped and are distinct (`firstMessageEqualsParent=false`).
- Stream first structural frame ~500 ms; 12 frames; normal terminal path retained `message_stream_complete` -> `conversation_detail_metadata` -> `[DONE]`.

### New-conversation Send in this b41 capture

- Request omits `conversation_id`; authoritative conversation identity again appears by `resume_conversation_token`.
- This particular new-chat sample is **not a default primary-assistant sample**: it is `conversation_mode.kind=gizmo_interaction` and the init/prepare shape contains `gizmo_id`. Do not generalize its mode/parent details to ordinary new chat.
- Safe request semantics otherwise match the observed send family: `action=next`, model `gpt-5-6-thinking`, `client_prepare_state=success`, `thinking_effort=extended`, encoding `v1`, buffering/followups enabled, one user text message.
- New-chat user-message ID is UUID-shaped; parent ID is opaque and distinct.
- Stream includes early authoritative conversation ID, system/user/internal/tool records, `title_generation`, visible assistant `in_progress`, text patching and message markers. Internal/system/tool/model-context records remain non-user-visible unless separately evidenced.

### Stop — server operation now evidenced

- Official Stop is a real server request: `POST /backend-api/stop_conversation`.
- Body shape: `{ conversation_id: string, exclude_async_types: [] }`.
- Request carries current transient auth/client headers plus `x-conduit-token`; no Stop proof header values were captured.
- Response: HTTP 200 `application/json`; body shape `{ status: string, last_message_id: null }` in this run.
- The stopped Send stream terminated with `doneSeen=false` after 21 frames and did not emit the normal `message_stream_complete` / `[DONE]` completion tail after Stop.
- Production lifecycle implication: user Stop must be its own response-owner terminal path. Local `URLSessionTask.cancel()` alone remains insufficient; a successful server Stop acknowledgement and the exact owned conversation/response lifecycle drive `user-stopped` once. Stream close after Stop must not be misclassified as network failure or normal `[DONE]` completion.
- Server Stop target is conversation-scoped in the observed wire body. Repository still exposes Stop only for the exact currently owned active response for that conversation; initial guard remains at most one active response per conversation.

### Protection / precursor chain now structurally evidenced

- `conversation/init` returns current model/limit metadata structure.
- `/backend-api/f/conversation/prepare` returns `{ conduit_token: string, status: string }`; successful Send uses `x-conduit-token`.
- Sentinel prepare returns `{ persona, prepare_token, proofofwork:{required,seed,difficulty}, so:{required,collector_dx,snapshot_dx}, turnstile:{required,dx} }`.
- Sentinel finalize receives `{ prepare_token, proofofwork, turnstile }` strings and returns `{ token, persona, expire_after, expire_at }`.
- Successful Send carries Sentinel requirements/proof/turnstile headers.
- **Critical remaining ambiguity**: b41 records structure but not the values of the non-secret `required` booleans, and does not record whether finalize proof/turnstile submissions are empty or non-empty. Therefore current evidence does not yet prove whether the tested account can use a normal no-challenge native precursor path or whether it requires browser-side PoW/Turnstile/other anti-abuse execution.
- Do not implement or copy a PoW/Turnstile/Sentinel solver, challenge bypass, browser fingerprint replay, or captured token/proof replay.

## Decision after b41

Production native Send transport remains **not yet justified**. One final narrow diagnostic distinction is required before choosing the checkpoint's A/B path. Writing an unused native parser/transport before that decision would be speculative.

### Allocated next Candidate

- **`DEV-send-stream-0.1.0-b42` / `0.1.0 (42)`** is now reserved for the final protection-decision probe.
- Allocation evidence: actual `main` unchanged at `34811877896ca88c6656be6676f5466a19931ce6`; PR #29 open/mergeable; only this Active checkpoint exists; repository search found no existing b42 identity; current Xcode/workflow identity is still b41.
- b42 must never be reused once emitted.

### b42 scope — diagnostic only, minimum delta

Extend the existing visible official-Web probe only enough to record:

1. Sentinel prepare **booleans only**: `proofofwork.required`, `turnstile.required`, `so.required`, plus presence (not value) of `prepare_token`.
2. Sentinel finalize request **presence/emptiness only** for `prepare_token`, `proofofwork`, `turnstile`; never values, lengths sufficient to reconstruct values, seeds/difficulty/dx, or raw payload.
3. Conversation-prepare short non-secret protocol semantics needed for a normal precursor decision (`action`, model, client prepare state/source/dispatch, conversation mode kind, encoding/buffering/counts) plus parent/conversation ID shape only.
4. Conversation-prepare response `status` short enum and `conduit_token` presence only.
5. Stop response `status` short enum and `last_message_id` presence/shape if Stop is naturally exercised again.
6. Explicit mode signal already present in Send semantics; the human Runtime pass should use **default ChatGPT / primary assistant new chat**, not a custom GPT/gizmo, so ordinary new-chat mode/parent semantics are not contaminated by `gizmo_interaction`.

No prompt/answer/reasoning text, raw IDs, Cookie/Authorization, raw request/response bodies, Sentinel seeds/difficulty/dx, proof values, Turnstile values, requirements token values, conduit token values or browser fingerprint values.

### Decision after exact b42 Runtime

- **Path A — normal native precursor permitted**: only if current exact Runtime shows no browser challenge execution is required for the observed successful path (required flags false and proof/turnstile submissions empty/absent as applicable), and all required precursor fields have a normal evidence-backed source inside the existing auth boundary. Then implement incremental authenticated transport + Repository-owned response lifecycle/new-chat adoption/Stop/follow-tail under a new unique Candidate.
- **Path B — native transport blocked under current architecture**: if any required anti-abuse challenge is true or successful flow needs non-empty browser-generated PoW/Turnstile/other challenge output. Record the block and do not circumvent. Present only architecture alternatives that preserve the security/governance boundary.

## Batch recovery point

- **Known head before b42 chain**: branch/PR head `048915a089bb8c675648b362cd3c47be5e789b83`; main `34811877896ca88c6656be6676f5466a19931ce6`; exact b41 product source remains `a2899e8bfdacd9b642c026c14f484735c1ac60fa`.
- **Confirmed complete / never replay**: b39-b41 Candidate emission; exact b40 and b41 real-device probes; b41 Stop observation; b41 push CI/Artifact/package identity; PR #29 + merge-view CI; existing b39-b41 build-index/runtime-doc writes.
- **Batch A pending**: make one atomic b42 product/config commit containing only the minimum probe semantic additions + Xcode/workflow identity `41 -> 42`; verify diff before moving branch ref.
- **Batch B pending**: fast-forward branch ref once to the verified b42 commit; verify actual branch head and the single b42 push workflow identity.
- **Batch C pending**: after CI, verify exact b42 Artifact/package identity; update PR/checkpoint/build index/runtime evidence as docs-only writes.
- **Human gate**: exact b42 real-device diagnostic pass using default primary-assistant new chat; no extra approval/`继续` is needed before machine steps.
- **Recovery must not touch/reuse**: b39-b41 identities/Artifacts; Stable b38 product behavior/state-owner contracts; other task checkpoints; main branch.
- **Next exact action**: implement the b42 probe delta atomically with build/Candidate identity 42, audit the commit diff, fast-forward `dev/send-stream-20260829`, obtain and verify the b42 IPA, then hand the exact Artifact to the user for the narrow default-new-chat/protection decision pass.
