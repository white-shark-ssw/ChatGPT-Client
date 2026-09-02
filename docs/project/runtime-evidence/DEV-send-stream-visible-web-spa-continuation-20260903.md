# DEV-send-stream visible Web SPA continuation trace — 2026-09-03

## Evidence class

User-supplied Web Rule Lab Runtime trace from visible official ChatGPT Web using the same default persistent `WKWebsiteDataStore` session authority as covered production. Probe was privacy-safe: it recorded coarse route shape, trusted-click/user-activation state, history navigation events, matching request families, HTTP status and content type; it did not record message bodies, cookies, tokens or raw conversation IDs.

## Starting state

- Probe installed at route `/`.
- `visibilityState=visible`, `hidden=false`, `document.hasFocus=true`, `readyState=complete` when the target entry occurred.
- Probe remained installed through the target transition, proving the successful entry was same-document rather than a full document navigation/reload.

## Exact target-entry sequence

1. `t=74,998ms`: official Web received a trusted click (`isTrusted=true`) on an anchor whose masked target route was `/g/{x}/c/{x}`. `navigator.userActivation.isActive=true`, `hasBeenActive=true`.
2. `t=75,065ms`: `history.pushState.before`, target `/g/{x}/c/{x}`.
3. `t=75,068ms`: `history.pushState.after`, current route `/g/{x}/c/{x}`.
4. `t=75,395ms`: matching plural conversation snapshot GET.
5. `t=75,399ms`: matching conversation bootstrap/detail POST.
6. `t=76,249ms`: bootstrap/detail response HTTP200 `application/json`.
7. `t=76,827ms`: plural snapshot response HTTP200 `application/json`.
8. `t=77,546ms`: page-owned `stream_status` GET.
9. `t=78,360ms`: `stream_status` response HTTP200 `application/json`.
10. `t=78,459ms`: page-owned `/backend-api/f/conversation/resume` POST.
11. `t=79,057ms`: resume response HTTP404 `application/json`.
12. `t=79,123ms`: official page immediately issued another `stream_status` plus plural snapshot GET.
13. The page then kept issuing paired `stream_status + plural snapshot` requests at roughly six-second intervals while the active response progressed, including starts at approximately `85.244s`, `91.676s`, `98.281s`, `104.385s`, `110.936s`, `117.429s`, `123.840s`, `130.468s`, `136.994s`, `143.343s` and `149.920s`; each observed response was HTTP200 JSON.

## Interpretation

This exact visible-Web run is a positive official continuation sample, but it is **not** an HTTP200 resume-SSE sample. The page attempted `/resume`, received HTTP404 JSON, then used the already-evidenced official page-owned `stream_status + plural conversation snapshot` fallback for genuine progressive response updates.

Therefore a user-visible progression that looks continuous must not automatically be labelled SSE. Product should follow whichever official page-owned continuation branch actually occurs:

- `/resume` HTTP200 `text/event-stream` -> adopt the page-owned SSE;
- `/resume` non-SSE/404 -> adopt only the page-owned status/snapshot fallback already authorized by Runtime evidence.

## New differential against covered production

Current covered executor source uses direct full navigation to `https://chatgpt.com/c/<conversationID>` for `observeExistingConversation` and `sendExistingConversation`.

The successful visible-Web sample instead entered via an official anchor and same-document `history.pushState` to `/g/{x}/c/{x}`, after which official bootstrap/status/resume/fallback traffic began.

This exposes two currently entangled differences:

1. official SPA/router conversation-entry transition versus direct `WKWebView.load`;
2. GPT-scoped route context `/g/{x}/c/{x}` versus hard-coded `/c/<conversationID>`.

The earlier coarse route probe returning `other` for a visibly active conversation is now explained by this `/g/.../c/...` shape; that coarse classifier is diagnostic-only.

## What this proves

- Current official Web can activate cross-platform live continuation under the same WebKit session authority.
- A successful current entry can be same-document SPA navigation.
- That SPA entry is followed by page-owned `stream_status` and continuation traffic without a second Send.
- Focus alone under the current direct full-load path remains insufficient from b88.
- Page-owned 404-resume fallback can keep a response progressing through repeated authoritative snapshots.

## What remains unverified

- Whether SPA transition alone is sufficient.
- Whether preserving `/g/<gpt>/c/<conversation>` route context is required.
- Whether a trusted human click/transient browser user activation is required.
- Whether an untrusted programmatic click on the official conversation anchor can trigger the same router/status chain.

## Next experiment

Before allocating b89, use Web Rule Lab to activate the same official conversation anchor programmatically only after transient `navigator.userActivation.isActive` has become false. Acceptance evidence is `click.isTrusted=false` plus `userActivationIsActive=false`, followed by the same `history.pushState -> bootstrap -> stream_status -> resume/fallback` chain. A positive result would justify a product A/B that asks the official page/router to enter the target conversation rather than Native constructing or guessing a route/protocol request.
