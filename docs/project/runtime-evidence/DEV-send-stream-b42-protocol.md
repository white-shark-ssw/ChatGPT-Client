# DEV-send-stream b42 protocol Runtime evidence

## Identity

- Candidate: `DEV-send-stream-0.1.0-b42`
- Version/build: `0.1.0 (42)`
- Exact product/config source: `e8946e48a0b5ad86b402faf5eabba627e3393adf`
- Push Run / Job: `33235622532` / `99055977981`, success
- Artifact: `9709824510`
- Artifact ZIP digest: `sha256:28b588f91904cf4a3c79e81d4bfcb8ad2336642729dcd092a4cdfffd38fffcdb`
- IPA SHA-256: `c6d1d421ab05a2294784223400291f0dc1683b638b2647ae85b2d9d4f3fcb85b`
- Runtime export: iPhone / iOS 17.0, Release, exported `2026-08-29T05:26:32Z`
- Export metadata matched build 42 / Candidate b42 / source marker `e8946e48a0b5`.

## Default primary-assistant new-chat evidence

The tested new conversation was `conversationKind=new` and `conversationModeKind=primary_assistant`, not a custom GPT/Gizmo.

Observed safe semantics included:

- `action=next`
- model `gpt-5-6-thinking`
- `thinkingEffort=extended`
- `supportedEncodings=["v1"]`
- `supportsBuffering=true`
- no authoritative `conversation_id` in the new-chat request path
- `conversation/prepare` returned `status=ok` plus a non-empty conduit token

The eventual Send used `POST /backend-api/f/conversation`, returned HTTP 200 `text/event-stream`, and followed the previously evidenced `v1` stream lifecycle with early authoritative conversation identity, message/patch events, `title_generation`, `message_stream_complete`, trailing conversation metadata and `[DONE]`.

## Protection-chain decision evidence

Sentinel prepare on the successful path returned:

- `proofOfWorkRequired=true`
- `turnstileRequired=true`
- `soRequired=true`
- non-empty prepare token

The subsequent Sentinel finalize request carried:

- non-empty `prepare_token`
- non-empty `proofofwork`
- non-empty `turnstile`

Finalize returned HTTP 200 with a non-empty final token. The successful Send carried the previously observed Sentinel protection headers and conduit token header.

No challenge value, seed, difficulty, dx value, Cookie/Authorization value, prompt/answer body or raw ID was captured by the diagnostic probe.

## Decision

**Path B is established for the recorded Plus/personal iPhone/iOS17 scope.**

The successful default ChatGPT Send depends on browser-generated anti-abuse challenge output. Production native Send under the current pure-native/transient-auth architecture is therefore blocked.

Do not implement or copy a PoW/Turnstile/Sentinel challenge solver, challenge bypass, browser-fingerprint replay, captured proof/token replay, or guessed fallback endpoint.

This is accepted **protocol Runtime evidence**, not native production Send acceptance. No production Send/Stream implementation was written or Runtime-tested by b42.

## Related accepted b41 Stop evidence

b41 already established official server Stop as `POST /backend-api/stop_conversation` with `{ conversation_id, exclude_async_types: [] }`, HTTP 200 JSON, and a stopped Send stream that can end without the normal `message_stream_complete` / `[DONE]` tail. If a future permitted production transport exists, Stop must be modeled as one exact-owner `user-stopped` terminal path; local transport cancellation alone is not server Stop proof.
