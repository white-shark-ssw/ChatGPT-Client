# DEV-send-stream

## Status

**Active — fresh-root visible-Web `/c/{project-conversation}` control is Runtime Positive: with transient activation false, official Web canonicalized to exact `/g/{scope}/c/{conversation}` and started page-owned continuation. Therefore scoped-route identity alone no longer explains b88. Product code must not be changed to a guessed route fix yet. Remaining differential is between a newly created covered WKWebView and the visible Web Rule Lab runtime/browsing-context state. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 product / Artifact / IPA identity unchanged
- Stable/Frozen Send: No

## Latest fresh-root Runtime result

User production-like Web Rule Lab control:

- marker `phase=unscoped_full_navigation_started`;
- `activationAtNavigation=false`;
- elapsed about 111.5s after navigation request;
- final `currentKind=EXACT_SCOPED_CANONICAL`;
- `currentIsExactScopedCanonical=true`;
- `currentIsExactUnscoped=false`;
- page visible, focused, complete;
- Resource Timing not saturated: 4 resources total;
- observed `plural_snapshot=1`, `stream_status=1`, `resume=0`;
- `canonicalizationObserved=true`;
- `continuationObserved=true`.

This proves that, in the visible Web Rule Lab browsing context after a fresh root document load, directly full-navigating to the unscoped `/c/{project-conversation}` can still recover the exact scoped project route and start genuine official page-owned continuation. The current official page does not require Native to know or synthesize the scope in this tested browsing context.

## Consequence

The earlier root-cause hypothesis “production fails because it hard-loads `/c/<conversationID>` instead of `/g/<scope>/c/<conversationID>`” is now insufficient by itself and must not drive b89.

The remaining evidenced differential is between:

- Web Rule Lab: a newly constructed visible/interactable WKWebView using `.default()` website data store; and
- CoveredWebSendExecutor: a newly constructed covered WKWebView using the same `.default()` store, but `isUserInteractionEnabled=false`, inserted behind Native siblings, with current b88 focus activation available.

b87/b88 already showed covered page visible/complete/attached and b88 can obtain `document.hasFocus=true`; the fresh-root visible control additionally shows transient user activation at navigation is not required.

## Next exact action

Do not allocate a route-fix b89. First close the remaining browsing-context/user-activation differential with the smallest evidence action:

1. on the current fresh-root positive visible page, read only `navigator.userActivation.isActive` and `navigator.userActivation.hasBeenActive` after continuation has already started;
2. if `hasBeenActive=false`, sticky user activation is ruled out for this successful path, and the next code-backed A/B should target the remaining WKWebView presentation/interactivity differential rather than route identity;
3. if `hasBeenActive=true`, do one fresh WKWebView control (new Web Rule Lab controller, same `.default()` store) before product code to distinguish sticky browsing-context activation/state from covered behavior.

No guessed `gizmo_id`, project endpoint, router internals, Native `stream_status`/`resume`, offset, polling, timer/retry/watchdog, WebSocket-body authority, duplicate Send or second response store.

## Batch recovery state

Fresh-root positive evidence batch has checkpoint and durable Runtime evidence written. PR metadata synchronization and final head close remain pending; product source, version/build, Candidate, Artifact and IPA are untouched.

## Preserved boundaries

Official page owns continuation; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store.

## Session round counter

This user turn is **round 52**.
