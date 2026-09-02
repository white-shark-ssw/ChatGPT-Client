# DEV-send-stream

## Status

**Active — b88 focus A/B is closed: focus alone is insufficient. New visible official-Web Rule Lab evidence proves a genuine same-document SPA conversation entry can immediately activate official continuation. In the successful trace a trusted official-anchor click from `/` to `/g/{x}/c/{x}` was followed by `history.pushState`, conversation bootstrap, `stream_status`, page-owned `/resume`, and repeated page-owned `stream_status + plural snapshot` after `/resume` returned HTTP404. Covered production still hard-loads `/c/<conversationID>`. SPA entry and GPT-scoped route context are therefore both strong remaining variables but are not yet causally separated. Next gate is one Web Rule Lab A/B using an untrusted programmatic official-anchor click after transient user activation expires. Do not allocate b89 until that result. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Feature head before this checkpoint close: `5a9c9cebccfc79850bd32f2774c488e49e068189`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 canonical Artifact: `9848999246`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Closed b88 Runtime conclusion

Exact b88 proves `WKWebView.becomeFirstResponder()` can make the covered page `document.hasFocus=true`, but the same remote generation continued through multiple additional PC tool rounds while covered production emitted zero matching `stream_status`, `/resume`, external SSE or page-owned snapshot. Focus is rejected as a sufficient activation condition under the current direct full `/c/<conversation>` load. Automatic final convergence was also rejected; completed assistant still required explicit Sync.

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-positive-near-terminal-inconclusive-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-sufficient-rejected-20260902.md`

## Visible Web SPA continuation evidence — 2026-09-03

Probe installed at route `/` and survived the successful target entry, proving same-document SPA navigation.

Observed sequence:

1. `74,998ms`: trusted official-anchor click, target `/g/{x}/c/{x}`, transient user activation true.
2. `75,065ms`: `history.pushState.before` to `/g/{x}/c/{x}`.
3. `75,068ms`: `history.pushState.after`; route changed without document reload.
4. `75,395ms`: page-owned plural conversation snapshot GET.
5. `75,399ms`: page-owned conversation bootstrap/detail POST.
6. `77,546ms`: page-owned `stream_status` GET -> HTTP200 JSON.
7. `78,459ms`: page-owned `/backend-api/f/conversation/resume` POST -> HTTP404 JSON.
8. `79,123ms`: official page immediately issued `stream_status + plural snapshot`.
9. The same pair then repeated roughly every six seconds while the response progressed.

This exact capture is **not** resume-SSE: `/resume` was 404 JSON. It confirms the current official fallback already documented by the project: genuine progressive blocks may come from the page-owned `stream_status + plural snapshot` path when SSE resume is unavailable. Product must follow the official branch actually observed, never force SSE.

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-visible-web-spa-continuation-20260903.md`.

## Source differential now proven

Current `CoveredWebSendExecutor.observeExistingConversation` and `sendExistingConversation` construct `https://chatgpt.com/c/<conversationID>` and call `WKWebView.load`.

The successful visible sample instead used an official anchor plus same-document `history.pushState` to `/g/{x}/c/{x}` before the page started `stream_status` and continuation traffic.

Remaining entangled variables:

- official SPA/router conversation entry versus full `WKWebView.load`;
- GPT-scoped `/g/{x}/c/{x}` route context versus hard-coded `/c/<conversationID>`;
- trusted/transient browser user activation versus an untrusted programmatic anchor click.

The previous coarse `route=other` visible-Web result is now explained by the `/g/.../c/...` shape; that classifier remains diagnostic-only.

## Next exact action — Web Rule Lab only

Do not change product code and do not allocate b89 yet.

Use the same target conversation to test a product-reproducible official-router entry:

1. save the target conversation URL in a page-local variable;
2. `history.back()` to `/` in the same document;
3. allow transient `navigator.userActivation.isActive` to become false;
4. programmatically call `.click()` on the official anchor whose pathname exactly matches the saved target pathname;
5. require probe evidence that the click was `isTrusted=false` and `userActivationIsActive=false`;
6. observe whether the same `history.pushState -> bootstrap -> stream_status -> resume/fallback` chain starts.

If positive, b89 can test official page/router activation instead of direct full navigation, letting the page preserve `/g/.../c/...` context without Native guessing. If negative, trusted browser activation remains a candidate and requires a separate evidence path.

## Durable sync this round

- checkpoint recorded the new visible-Web SPA trace and causal boundary;
- durable Runtime evidence `DEV-send-stream-visible-web-spa-continuation-20260903.md` created;
- no product source, version/build, Candidate, CI, Artifact or IPA identity changed;
- no `TECHNICAL_DECISIONS.md` / `WEB_SEND_ADAPTER.md` causal rule was promoted yet because SPA entry, GPT route context and trusted activation remain entangled; existing documented 404-resume snapshot fallback already matches this trace.

## Preserved boundaries

- client-owned Send keeps true same-response SSE;
- `ConversationRepository` remains sole Native response/content authority;
- `AuthSessionStore` remains sole Native auth/account authority;
- default persistent `WKWebsiteDataStore` remains persistent Web auth authority;
- no Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store;
- hidden thoughts remain non-presentational;
- b80 presentation/final boundaries remain preserved.

## Session round counter

This user turn is **round 32**.
