# DEV-send-stream b40 Runtime protocol evidence

- Candidate: `DEV-send-stream-0.1.0-b40`
- Exact product/config source: `f4a7abbad52f00e10f4c0e0fc14bcb7686187f2b`
- Runtime device: iPhone / iOS 17.0
- Evidence time: 2026-08-29
- Scope: visible official-Web structural protocol probe only; not native production Send acceptance.

## Accepted facts

- Existing and new chat both send via `POST /backend-api/f/conversation` and return HTTP 200 `text/event-stream`.
- Existing request contains `conversation_id`; new-chat request omits it while preserving the same remaining top-level structure.
- SSE begins with `"v1"`, includes early conversation identity (`resume_conversation_token`), user/input and assistant message lifecycle events, patch batches, `message_stream_complete`, post-complete conversation metadata, and terminates with `[DONE]`.
- Text patch structure includes append `/message/content/parts/0`, replace `/message/status`, replace `/message/end_turn`, append `/message/metadata`.
- New-chat capture emitted `title_generation`.
- Real browser Send carries protection/conduit header names including Sentinel requirements/proof/Turnstile and `x-conduit-token`; values were intentionally never captured.

## Not proven

- Protection/conduit value provenance remains Unknown/Unverified.
- Exact safe request enum values and ID relations require b41 evidence refinement.
- Stop route/ack and explicit user-visible reasoning remain Unknown/Unverified.
- Do not implement or replay anti-abuse proof values; do not call this evidence native Send Runtime acceptance.
