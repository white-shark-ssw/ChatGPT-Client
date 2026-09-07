# DEV-send-stream — visible official iOS passive refresh Runtime — 2026-09-02

## Scope

This records a user Runtime observation made after the official-iOS native realtime architecture was identified statically and before b83 allocation.

## Test

- Official ChatGPT iOS app was left visibly open on conversation A.
- A new turn was sent to the same conversation A from ChatGPTClient.
- The user observed the official iOS UI without manually refreshing/navigation.

## Runtime result

The visible official iOS conversation did **not** automatically refresh to show the newly-sent remote turn/response.

Classification: **Negative for passive visible-iOS UI refresh as an acquisition source.**

This is consistent with the earlier visible official-Web result: an already-open official UI cannot be assumed to reconcile cross-platform conversation changes merely because the same conversation is visible.

## What this does and does not prove

It proves only UI behavior for the tested flow. It does **not** prove that the official native WebSocket service received no underlying conversation event. Static evidence already shows a separate `WebSocketConversationEventsService` / `WebSocketConversationObserver`; the UI may choose not to apply an event to the visible conversation, may require another state transition, or the event may not arrive in this flow.

Therefore the research Probe remains useful specifically to distinguish:

1. underlying early native event exists but visible official UI does not consume/reconcile it; versus
2. no useful early target-conversation native event exists for this cross-platform flow.

## Relation to prior b80 Runtime

b80 already proved that after explicit Sync/re-arm, the existing covered-page acquisition path can enter external streaming observation and expose reasoning/tool snapshots. Another conversation in the same b80 test failed to acquire reasoning at all until explicit Sync/re-arm.

Therefore the unresolved defect is primarily **automatic acquisition trigger / timing**, not the already-demonstrated ability of the adopted-response path to expose reasoning snapshots once acquisition has begun.

The current WebSocket research does not promise token-delta reasoning streaming. Its immediate purpose is to find a deterministic early trigger that can start the existing authoritative Sync/re-arm/adoption path without polling or manual Sync.

## Product consequence

- Do not treat visible official iOS auto-refresh as product evidence or as the desired mechanism.
- Continue the native WebSocket Probe only as a transport/event investigation below the UI layer.
- If a target-matching event arrives before completion, it may justify one bounded authoritative acquisition action in a future b83.
- If no useful early event arrives, reject this WebSocket-trigger branch and evaluate the explicitly bounded selected-conversation monitoring branch already supported by official `ConversationPollingManager` static evidence.
- WebSocket bodies remain non-authoritative for message/reasoning/final content until separately proven.

## Evidence classification

- visible official iOS passive refresh: Runtime Negative;
- official native WebSocket service existence: Static Positive;
- underlying early event for this flow: Runtime Pending;
- prior adopted-response reasoning snapshot capability: Runtime Positive once acquisition/re-arm succeeds;
- progressive reasoning token stream: Unverified / unresolved;
- b83: not allocated;
- Stable/Frozen Send: No.
