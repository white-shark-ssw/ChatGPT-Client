# DEV-send-stream visible Web SPA continuation trace — 2026-09-03

## Evidence class

User-supplied Web Rule Lab Runtime traces from visible official ChatGPT Web using the same default persistent `WKWebsiteDataStore` session authority as covered production. Probe is privacy-safe: it records coarse route shape, trusted-click/user-activation state, history navigation events, matching request families, HTTP status and content type; it does not record message bodies, cookies, tokens or raw conversation IDs.

## First project/GPT-scoped positive sample

### Starting state

- Probe installed at route `/`.
- `visibilityState=visible`, `hidden=false`, `document.hasFocus=true`, `readyState=complete` when the target entry occurred.
- Probe remained installed through the target transition, proving the successful entry was same-document rather than a full document navigation/reload.

### Exact target-entry sequence

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

## Second project/GPT-scoped positive sample

A second independent visible-Web project conversation reproduced the same official route and continuation branch.

1. Probe installed at `/`.
2. `t=6,763ms`: trusted official anchor click (`isTrusted=true`) with masked target `/g/{x}/c/{x}` and transient user activation true.
3. `t=6,826-6,828ms`: same-document `history.pushState` changed the route to `/g/{x}/c/{x}`.
4. `t=7,014-7,015ms`: official page issued plural snapshot GET plus conversation bootstrap/detail POST.
5. `t=10,245ms`: page-owned `stream_status` GET -> HTTP200 JSON at `11,345ms`.
6. `t=11,535ms`: page-owned `/backend-api/f/conversation/resume` POST -> HTTP404 JSON at `12,192ms`.
7. `t=12,356-12,359ms`: official page immediately started paired `stream_status + plural snapshot` fallback.
8. Further paired requests were observed at approximately `19.563s`, `26.657s`, `34.121s` and `40.983s`, all with HTTP200 JSON responses during the capture window.
9. The user reported that the visible project conversation was progressing normally during this period. The capture duration was about 45.6 seconds, long enough to establish the continuation branch even though the user only needed to watch the visible progression for a short interval.

This second sample again is **not** an HTTP200 resume-SSE sample. Its `/resume` response was HTTP404 `application/json`, followed by the official status/snapshot progression path.

## Interpretation

The two current project/GPT-scoped visible-Web samples consistently show:

- canonical visible route `/g/{x}/c/{x}`;
- same-document official SPA entry through an official conversation anchor;
- conversation bootstrap followed by `stream_status`;
- page-owned `/resume` attempt;
- `/resume` HTTP404 JSON in both captures;
- official repeated `stream_status + plural conversation snapshot` fallback that keeps the response visibly progressing.

Therefore a user-visible progression that feels continuous must not automatically be labelled SSE. Product should follow whichever official page-owned continuation branch actually occurs:

- `/resume` HTTP200 `text/event-stream` -> adopt the page-owned SSE;
- `/resume` non-SSE/404 -> adopt only the page-owned status/snapshot fallback already authorized by Runtime evidence.

## New ordinary-vs-project Runtime observation

The user now reports an important historical distinction that was previously not tracked explicitly:

- ordinary conversations outside projects had prior real-device cases where an explicit Sync exposed the current reasoning block and subsequent progression then continued automatically;
- current repeated covered-production failures were project/GPT-scoped conversations;
- the two new visible-Web project positive samples both use `/g/{x}/c/{x}`.

This user Runtime report is evidence of a strong scope correlation, but it is not yet a controlled ordinary-versus-project A/B under one exact candidate and one exact remote generation. Do not promote it to a universal rule until reproduced deliberately.

## New differential against covered production

Current covered executor source uses direct full navigation to `https://chatgpt.com/c/<conversationID>` for `observeExistingConversation` and `sendExistingConversation`.

Current Native `ConversationSummary` / `ConversationDetail` models do not preserve a project/GPT route context field at the conversation entry boundary, and the list parser currently keeps only conversation ID/title/update time.

The successful visible-Web project samples instead enter via an official anchor and same-document `history.pushState` to `/g/{x}/c/{x}`, after which official bootstrap/status/resume/fallback traffic begins.

This raises **project/GPT route-context loss** from a generic variable to a high-priority root-cause candidate for the project-only failures. Remaining entangled variables are still:

1. official SPA/router conversation-entry transition versus direct `WKWebView.load`;
2. preserving the project/GPT-scoped canonical `/g/{x}/c/{x}` route context versus hard-coded `/c/<conversationID>`;
3. trusted/transient browser user activation versus an untrusted programmatic official-anchor click.

The earlier coarse route probe returning `other` for a visibly active conversation is explained by this `/g/.../c/...` shape; that coarse classifier remains diagnostic-only.

## What this proves

- Current official Web can repeatedly activate cross-platform project-conversation continuation under the same WebKit session authority.
- Successful project entry can be same-document SPA navigation.
- That entry is followed by page-owned `stream_status` and continuation traffic without a second Send.
- Two current project samples used official 404-resume status/snapshot fallback rather than HTTP200 resume SSE.
- Focus alone under the current direct full-load `/c/<conversation>` path remains insufficient from b88.
- Project/GPT route context is now a strong evidence-backed candidate, not yet a proven sole cause.

## What remains unverified

- Whether ordinary conversations currently continue correctly under the existing `/c/<conversation>` covered-production path in the same build.
- Whether SPA transition alone is sufficient.
- Whether preserving `/g/<project-or-gpt>/c/<conversation>` route context is required.
- Whether a trusted human click/transient browser user activation is required.
- Whether an untrusted programmatic click on the official project conversation anchor can trigger the same router/status chain.

## Next experiment

Do not allocate b89 yet. Use Web Rule Lab on a project conversation to activate the same official conversation anchor programmatically only after transient `navigator.userActivation.isActive` has become false. Acceptance evidence is `click.isTrusted=false` plus `userActivationIsActive=false`, followed by the same `history.pushState -> bootstrap -> stream_status -> resume/fallback` chain.

A positive result would show that a production-reproducible official-router entry can preserve `/g/.../c/...` context without a trusted human click and would justify a narrowly scoped b89 project-route/router A/B. A negative result would keep trusted browser activation as a separate candidate.
