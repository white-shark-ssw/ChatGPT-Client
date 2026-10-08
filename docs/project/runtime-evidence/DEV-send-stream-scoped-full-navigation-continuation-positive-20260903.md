# DEV-send-stream — scoped project full navigation continuation Positive — 2026-09-03

## Classification

Web Rule Lab Runtime evidence. No product source, Candidate, Artifact or IPA change.

## Question

Can a fresh full document navigation to the exact official project/GPT-scoped route `/g/{scope}/c/{conversation}` activate official page-owned continuation for an externally active response without a trusted target click or SPA router transition?

## Control

The target route was captured from the real official project conversation. The launcher waited for transient `navigator.userActivation.isActive` to become false, then called full navigation to the exact scoped route.

Privacy boundary: the probe returned only route shape, activation state, Navigation Timing, bounded Resource Timing API categories/counts and no raw conversation/scope ID, title/body, Cookie, token or auth material.

## Exact result

Control marker:

- `phase=full_navigation_started`
- `activationAtNavigation=false`
- `targetShape=/g/{x}/c/{x}`
- elapsed since navigation request at export: about 149471 ms

Loaded page:

- route `/g/{x}/c/{x}`
- `visibilityState=visible`
- `hidden=false`
- `hasFocus=true`
- `readyState=complete`

Navigation Timing:

- `type=navigate`
- duration about 926 ms

Resource Timing:

- total resources: 24
- `possiblySaturated=false`
- `plural_snapshot=9`
- `stream_status=8`
- `resume=0`
- `conversation_detail=0` in the post-navigation resource window

Observed progression:

- plural snapshot at about 89094 ms;
- `stream_status + plural_snapshot` at about 96353/96354 ms;
- repeated paired requests around 103241/103242, 110595/110599, 117394/117398, 124472/124473, 131237/131239, 138859/138861 and 145706/145707 ms.

The official page therefore entered a repeated page-owned status/snapshot continuation loop after a fresh scoped full navigation.

## What this proves

1. Exact scoped project full navigation can activate official continuation while transient user activation is false.
2. A trusted target click is not required for continuation.
3. A same-document SPA transition is not required for continuation.
4. The production `/c/{conversation}` full-load failure and exact `/g/{scope}/c/{conversation}` full-load success make project/GPT scoped route identity the strongest evidenced differentiator.
5. This run is not resume-SSE evidence: no `/resume` resource was observed. The official page may continue through its own `stream_status + plural snapshot` path.

## Relationship to Control A

Corrected Control A used the real official scoped anchor with `isTrusted=false` and activation false. It successfully produced same-document `history.pushState`, `/g/{x}/c/{x}`, bootstrap/detail and plural snapshots but no `stream_status` or `/resume` during about 53 seconds.

Control B therefore shows that the missing condition is not simply trusted click. A fresh full document load to the exact scoped route is sufficient in the supplied run, while the untrusted SPA entry was not.

## Product implication

Current production always full-loads `https://chatgpt.com/c/<conversationID>` and Native conversation models/cache currently discard project/GPT scoped route identity. Before product code, verify from current service payload which existing field supplies the scoped identity. External comparison research strongly corroborates `gizmo_id`, but the project must Runtime-confirm that service field rather than guess it.

If confirmed, the next candidate should preserve the existing scoped identity and use exact full `/g/<scope>/c/<conversation>` navigation for project targets while leaving ordinary `/c/<conversation>` behavior unchanged.

## Preserved prohibitions

No Native-constructed `stream_status`, `/resume`, guessed offset, polling/cadence, retry/watchdog, duplicate Send, WebSocket-body authority, hidden-thought presentation or second response store is authorized by this evidence.
