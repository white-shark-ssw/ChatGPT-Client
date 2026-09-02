# DEV-send-stream

## Status

**Active — b88 focus A/B is closed: focus alone is insufficient. New visible official-Web Rule Lab evidence now proves a genuine same-document SPA conversation entry can immediately activate the official continuation runtime. In the captured successful run a trusted anchor click from `/` to `/g/{x}/c/{x}` was followed by `history.pushState`, official conversation bootstrap, `stream_status`, page-owned `/resume`, and then the official repeated `stream_status + plural snapshot` fallback after `/resume` returned HTTP404. This is strong evidence that covered production is missing official Web conversation-entry state, but two variables remain entangled: SPA/router entry and GPT-scoped route context. Do not allocate b89 until one more Web Rule Lab A/B proves a product-reproducible entry mechanism without relying on a trusted human click. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Verified branch/PR head before this docs batch: `d2e6eaf44518736688d845ac79bb3f1635bfcaa8`
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 canonical Artifact: `9848999246`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Closed b88 Runtime conclusion

Exact b88 real-device Runtime proves `WKWebView.becomeFirstResponder()` can make the covered page `document.hasFocus=true`, but the same remote generation continued through multiple additional PC tool rounds while covered production emitted zero matching `stream_status`, `/resume`, external SSE or page-owned snapshot. Focus is therefore rejected as a sufficient activation condition under the current direct full `/c/<conversation>` load. Automatic final convergence was also rejected; the completed assistant still required an explicit Sync.

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-positive-near-terminal-inconclusive-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-sufficient-rejected-20260902.md`

## New visible Web SPA continuation evidence — 2026-09-03

Web Rule Lab probe installed at route `/` and remained in the same document for the successful conversation entry.

Exact observed order:

1. `t=74,998ms`: trusted click on an official anchor, `targetRoute=/g/{x}/c/{x}`, `userActivationIsActive=true`.
2. `t=75,065ms`: `history.pushState.before` to `/g/{x}/c/{x}`.
3. `t=75,068ms`: `history.pushState.after`; route became `/g/{x}/c/{x}`. No document reload occurred; the probe survived.
4. `t=75,395ms`: page-owned plural conversation snapshot GET.
5. `t=75,399ms`: page-owned conversation bootstrap/detail POST.
6. `t=77,546ms`: page-owned `stream_status` GET -> HTTP200 JSON at `78,360ms`.
7. `t=78,459ms`: page-owned `/backend-api/f/conversation/resume` POST -> HTTP404 JSON at `79,057ms`.
8. `t=79,123ms`: official page immediately issued another `stream_status` plus plural snapshot.
9. The page then continued issuing paired `stream_status + plural snapshot` requests approximately every 6 seconds while the active response progressed.

This run did **not** obtain HTTP200 `text/event-stream` from `/resume`; its live progression used the already-evidenced official snapshot fallback. Therefore visible progressive behavior must not be described as SSE for this exact capture.

Important differential with production source: `CoveredWebSendExecutor.observeExistingConversation` still constructs `https://chatgpt.com/c/<conversationID>` and performs a full `WKWebView.load`, while the successful visible sample used an official SPA anchor transition to `/g/{x}/c/{x}`. Current source does not preserve that GPT route context at this entry point.

## Current causal boundary

Proven:

- official visible Web can activate cross-platform continuation under the same persistent WebKit session authority;
- successful current entry can be same-document SPA `pushState`, not full navigation;
- after that entry the page itself starts `stream_status` and page-owned continuation/fallback traffic;
- focus alone with direct full navigation is insufficient;
- `/resume` may be HTTP404 and official page-owned `stream_status + plural snapshot` fallback can still provide genuine progressive blocks.

Not yet proven:

- whether the decisive missing variable is SPA/router entry itself, GPT-scoped route context (`/g/{x}/c/{x}`), or both;
- whether a programmatic/untrusted activation of the official conversation anchor is sufficient;
- whether a trusted human click/browser transient user activation is required.

## Next exact action — Web Rule Lab only

Do not change product code and do not allocate b89 yet.

Use the same successful target flow to test whether the official SPA transition can be triggered **programmatically after transient user activation has expired**:

1. while on the successfully active target conversation, save the current target URL in a page-local variable;
2. use `history.back()` to return to `/` in the same document;
3. from a diagnostic script, wait until `navigator.userActivation.isActive == false`, then call `.click()` on the official anchor whose pathname exactly matches the saved target pathname;
4. verify the probe records `click.isTrusted=false` and `userActivationIsActive=false` at the synthetic click;
5. observe whether the same `history.pushState -> bootstrap -> stream_status -> resume/fallback` chain starts.

If that succeeds, b89 may use the official page's own conversation anchor/router path rather than direct `WKWebView.load`, preserving `/g/.../c/...` route context without Native guessing. If it fails, trusted browser activation remains a candidate and requires a different evidence path.

## Preserved boundaries

- client-owned Send keeps true same-response SSE;
- `ConversationRepository` remains sole Native response/content authority;
- `AuthSessionStore` remains sole Native auth/account authority;
- default persistent `WKWebsiteDataStore` remains persistent Web auth authority;
- no Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store;
- hidden thoughts remain non-presentational;
- b80 presentation/final boundaries remain preserved.

## Batch recovery point — visible Web SPA evidence docs

Baseline before this docs chain: feature/PR head `d2e6eaf44518736688d845ac79bb3f1635bfcaa8`; b88 product/package/Artifact identities above are immutable.

Batches:

1. checkpoint allocation/recovery record — **this write**;
2. create durable Runtime evidence for the supplied Web Rule Lab event sequence;
3. update `WEB_SEND_ADAPTER.md` / `TECHNICAL_DECISIONS.md` with the new entry-path qualification if deterministic;
4. close checkpoint recovery state and synchronize PR metadata if the durable interpretation changes the next gate.

Do not touch product source, build/candidate identity or allocate b89 during this docs chain.

## Session round counter

This user turn is **round 32**.
