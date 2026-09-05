# Web Send / Stream Interception Research

_Date: 2026-08-30_

## Scope / status

This note records an architecture hypothesis raised by the user during `DEV-send-stream`. It is **research only** and does not allocate b48 or authorize production code.

User idea: keep official Web for the protected Send, but prevent the Web page from receiving/rendering the long assistant stream so the page does not grow a large answer DOM; remove/avoid local Web message rendering immediately after Send while Native owns presentation.

## Public WebKit boundary

Public native WebKit APIs do not provide a general arbitrary-HTTPS fetch/XHR response-body interception hook for `chatgpt.com` subresource traffic:

- `WKURLSchemeHandler` is for custom schemes WebKit does not already handle, not a public MITM hook for normal HTTPS;
- `WKNavigationDelegate` can allow/cancel navigation requests/responses, but JavaScript `fetch`/XHR SSE traffic is not ordinary top-level navigation response-body interception;
- content rule lists can block matching loads, not transform an SSE response body.

`WKUserScript` at document start can, however, run before the page's later scripts/content and can wrap page JavaScript networking APIs.

## Existing repository proof that the interception point exists

Current `ProtocolHandoffProbe.swift` already installs a `WKUserScript` at `.atDocumentStart`, replaces `window.fetch`, calls the original fetch, clones the returned `Response`, and incrementally reads `text/event-stream` frames from `/backend-api/f/conversation` while returning the untouched original response to the official page.

Therefore the project already has source-level proof that a JS-layer interception point exists **before React consumes the official Send SSE**. This is stronger than DOM scraping and different from the user's prior userscript that merely hid already-loaded history.

Current `NativeResumeParityProbe.swift` also wraps `window.fetch` at document start and parses the official `/backend-api/f/conversation/resume` body `{conversation_id, offset}` before calling `originalFetch`. That proves a future diagnostic could choose not to let the Web page become the network consumer for a particular resume attempt, if an explicit architecture decision permits such an experiment.

## Candidate A — same official Send, siphon/filter the response before React

Conceptual flow:

`visible official Web composer -> official protected /f/conversation Send -> injected fetch wrapper consumes SSE -> Native presentation receives the user-visible stream -> Web page receives only a deliberately minimal/filtered stream or is dismissed`

Potential benefit:

- keeps the browser-generated protected Send/challenge path unchanged;
- avoids a second Native protected Send;
- avoids the b46/b47 duplicated `/resume` 404 path because the original official Web request remains the actual upstream response transport;
- can prevent assistant answer text from entering React/DOM if filtering occurs before the page reads the body.

Important implementation fact: do not use `Response.clone()` and then leave one branch unconsumed for long streams. Clone/tee semantics can buffer unread data. A real experiment should consume one source stream and explicitly construct the stream returned to the Web page while separately forwarding only bounded/required data to Native.

Unverified risks:

- the official page may require stream events to update its branch/current-node/message state; returning an empty or abruptly failed stream may mark the Send failed or leave the next Send attached to stale state;
- the minimum set of structural events the Web state machine needs is Unknown / Unverified;
- forwarding full user-visible text through a JS-to-Native bridge changes the existing diagnostics-only boundary and requires an explicit architecture decision plus bounded streaming/backpressure design;
- removing DOM nodes after React has already incorporated them is insufficient because React/application state may still retain the message.

## Candidate B — deliberately make Native the first/exclusive `/resume` consumer

The b46/b47 Runtime only tested a Native duplicate **after** official Web had already opened a successful `/resume`; Native got HTTP404. First/exclusive Native resume is still Unknown.

A stronger diagnostic could:

1. let the user perform the protected Send in visible official Web;
2. terminate/withhold the Web response path early enough to prevent long assistant rendering;
3. allow the official Web state machine to calculate a real `/resume {conversation_id, offset}` request;
4. intercept that resume call in the existing fetch wrapper **before** `originalFetch` executes;
5. pass only the real conversation ID/offset to Native and prevent the official Web from becoming the first resume network consumer;
6. issue one Native first/exclusive resume using the already accepted transient auth boundary.

This directly tests whether b46/b47 404 was a second-consumer/ownership effect rather than a missing-header effect, without guessing the offset.

Unverified risk: Native may still receive 404 because additional browser/client context is required. Do not copy `x-conduit-token` or observed OAI browser header values merely to force success.

## Pre-Send long-conversation limitation

Post-Send interception alone does **not** solve the exact b47 preparation failure. The long conversation froze while trying to bring up/use the Web composer before Send.

To address that specific failure, the Web page must avoid ingesting/rendering full existing-conversation history **before composer use**.

A distinct, more invasive research hypothesis is data-level Web virtualization:

`native authoritative detail -> visible Web opens existing conversation -> injected fetch wrapper intercepts Web conversation-detail response -> Web receives only a minimal tail/current-node graph sufficient for its composer -> official Send -> response intercepted/handed to Native`

This differs materially from the user's old Tampermonkey-style approach. The old approach loaded the full Web application/conversation state and merely hid most visible turns; data-level virtualization would prevent the full history from entering React/application state in the first place.

However the exact minimal conversation graph required by the Web composer is Unknown / Unverified. Do not synthesize/truncate private response schema in production without a diagnostic proving Send identity/branch semantics remain correct.

## Account/security relation

This architecture would keep the actual protected Send inside the ordinary official Web request/challenge path. It is therefore materially different from Sub2API/Codex subscription-to-Responses experiments and does not require the user's primary account to use a separate API-style OAuth transport.

It also differs from previously rejected hidden synthetic Send if the user genuinely operates a visible official composer and the experiment only changes post-Send response presentation/ownership. Nevertheless, production answer transport through JS interception is outside the currently accepted TD-024 diagnostics-only/visible-Web ownership boundary and requires an explicit architecture decision before product implementation.

No Sentinel/PoW/Turnstile bypass, proof replay, synthetic hidden click, prompt injection or browser-token/header-value replay is justified by this research.

## Recommended evidence order if selected

1. New-conversation diagnostic: prove the official Send still succeeds when assistant content is prevented from reaching React, and measure whether the page avoids answer DOM/state growth.
2. Determine which structural/terminal events, if any, must still reach the Web page for the next user Send to remain attached to the correct conversation/current node.
3. Test Candidate B once: intercept the **first** official resume request before network and let Native be the only resume consumer; do not add header mimicry.
4. Only if post-Send ownership works, investigate the separate pre-Send data-level virtualization of existing-conversation detail needed to solve the long-conversation composer freeze.
5. Existing long conversation must pass exact-device composer and `+` responsiveness before this route can become production architecture.

## Current conclusion

The user's idea is technically stronger than DOM pruning **if interception occurs before React receives history/stream data**. Merely deleting rendered nodes after Send is not sufficient.

The most promising shape is not `full Web -> render -> delete DOM`; it is:

`minimal visible Web Send state -> official protected Send -> response ownership leaves Web before answer rendering -> Native presentation`.

This remains an architecture candidate, not yet an accepted implementation.
