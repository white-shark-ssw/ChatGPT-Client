# DEV-send-stream account-signal probe — 2026-09-01

## Source

User-supplied privacy-safe Web Rule Lab capture from the same logged-in ChatGPT Web session.

## Result

**Inconclusive for an account-wide completion/new-answer signal.**

The capture contains normal page traffic and one explicit protected Send sequence on the currently loaded conversation, including `POST /backend-api/f/conversation` -> HTTP 200 `text/event-stream`, plus ordinary Sentinel/telemetry/prepare/heartbeat traffic. It does not contain a clear WebSocket, EventSource, BroadcastChannel, service-worker-message or other structural event that can be attributed to a different conversation completing while the Lab remains on the current conversation.

The capture therefore does not establish the transport/schema for official account-wide notifications and must not be used to guess one.

## Product-architecture clarification from the same Runtime discussion

The account-wide official signal is **not required** for completion notification of responses that are initiated by this client and already owned by `ConversationRepository`.

Existing project architecture already defines completion notification from the set of client-owned active response lifecycles: each known Send has a conversation/response owner, and completion notification may be emitted from that authoritative terminal transition. Multiple client-owned active responses are tracked as a set; no account-wide official notification transport is needed to know that one of those owned responses completed.

The account-wide signal remains relevant only to **externally initiated** cross-platform activity that the client did not itself start and therefore has not yet adopted. b80 still has an intermittent defect in automatically acquiring such externally started responses before explicit Sync. That defect remains separate from client-owned completion notification.

## Boundary

- Client-owned Send completion notification: can proceed from existing Repository-owned response lifecycle; no official account-wide signal prerequisite.
- Externally started response auto-discovery/adoption: still unresolved/intermittent in b80; account-wide signal is one possible future evidence route, not an authorized implementation yet.
- No polling/timer/retry/watchdog/duplicate Sync/status synthesis is authorized by this capture.
