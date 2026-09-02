# DEV-send-stream

## Status

**Active — b88 focus A/B remains closed: focus alone is insufficient. Two independent visible official-Web project/GPT-scoped Runtime samples now show the same canonical `/g/{x}/c/{x}` same-document SPA entry followed by official `stream_status`, page-owned `/resume`, and repeated page-owned `stream_status + plural snapshot` fallback after `/resume` returned HTTP404 JSON. The user also reports that prior ordinary non-project conversations had real-device cases where Sync exposed a reasoning block and later progression continued automatically, while the recent covered-production failures were project conversations. Current production still hard-loads every conversation as `/c/<conversationID>` and Native conversation models do not preserve project/GPT route context. Project/GPT route-context loss is therefore a high-priority root-cause candidate, but SPA entry, scoped route context, and trusted activation are not yet causally separated. Do not allocate b89 until the untrusted official-anchor Web Rule Lab A/B completes. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Feature head after second project visible-Web evidence: `84344593c93f0d561ac706d8be14a5aa3a20eb4e`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 canonical Artifact: `9848999246`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Closed b88 Runtime conclusion

Exact b88 proves `WKWebView.becomeFirstResponder()` can make the covered page `document.hasFocus=true`, but a remote generation continued through multiple additional PC tool rounds while covered production emitted zero matching `stream_status`, `/resume`, external SSE or page-owned snapshot. Focus is rejected as a sufficient activation condition under the current direct full `/c/<conversation>` load. Automatic final convergence also failed and required explicit Sync.

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-positive-near-terminal-inconclusive-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-sufficient-rejected-20260902.md`

## Visible project/GPT-scoped official-Web continuation — two positive samples

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-visible-web-spa-continuation-20260903.md`.

### Sample 1

- trusted official anchor click from `/` to `/g/{x}/c/{x}`;
- same-document `history.pushState`;
- plural snapshot GET + conversation bootstrap/detail POST;
- `stream_status` -> HTTP200 JSON;
- `/backend-api/f/conversation/resume` -> HTTP404 JSON;
- immediate repeated page-owned `stream_status + plural snapshot` fallback roughly every six seconds while the response progressed.

### Sample 2

A second independent project conversation reproduced the same chain:

- `6.763s`: trusted official anchor click to `/g/{x}/c/{x}`;
- `6.826-6.828s`: same-document `history.pushState`;
- `7.014-7.015s`: plural snapshot GET + conversation bootstrap/detail POST;
- `10.245s`: `stream_status` GET -> HTTP200 JSON;
- `11.535s`: `/resume` POST -> HTTP404 JSON;
- `12.356s`: immediate `stream_status + plural snapshot` fallback;
- further paired status/snapshot starts around `19.563s`, `26.657s`, `34.121s`, and `40.983s`, all returning HTTP200 JSON during the roughly 45.6-second capture.

The user reports the visible project conversation progressed normally. This is enough to establish continuation even though the visible observation window after entry was short.

Important: neither current project sample is an HTTP200 resume-SSE sample. Both are official 404-resume snapshot-fallback samples. Continuous-looking UI must not be labelled SSE without `Content-Type: text/event-stream` evidence.

## Ordinary-vs-project scope correlation

New user Runtime report:

- ordinary conversations outside projects previously had real-device cases where explicit Sync exposed the current reasoning block and later blocks then continued automatically;
- the recent repeated covered-production no-continuation failures were project conversations;
- both current known-good visible project samples use canonical `/g/{x}/c/{x}`.

This is a strong scope correlation, not yet a controlled same-build ordinary-vs-project A/B. Do not treat it as universal proof that every ordinary conversation works or every project conversation fails.

## Current source differential

Current `CoveredWebSendExecutor.observeExistingConversation` and `sendExistingConversation` always construct `https://chatgpt.com/c/<conversationID>` and call `WKWebView.load`.

Current Native `ConversationSummary` holds only `id`, `title`, and `updateTime`; `ConversationDetail` has no project/GPT route context; list summary parsing keeps only conversation ID/title/update time. Therefore production currently has no preserved canonical `/g/<project-or-gpt>/c/<conversation>` entry identity at this boundary.

The known-good official project path instead uses an official anchor and same-document SPA transition to `/g/{x}/c/{x}` before the page starts continuation traffic.

## Current causal boundary

Project/GPT route-context loss is now a **high-priority root-cause candidate** for project-only covered failures, but these variables remain entangled:

1. official SPA/router conversation entry versus full `WKWebView.load`;
2. preserving `/g/{x}/c/{x}` project/GPT context versus hard-coded `/c/<conversationID>`;
3. trusted/transient browser activation versus an untrusted programmatic official-anchor click.

Do not change ordinary-conversation navigation or add a generic router workaround yet.

## Next exact action — Web Rule Lab only

Do not change product code and do not allocate b89 yet.

Use a project conversation and test the official conversation anchor programmatically after transient `navigator.userActivation.isActive` has become false. Require evidence that the synthetic click is `isTrusted=false` and `userActivationIsActive=false`, then observe whether the same `history.pushState -> bootstrap -> stream_status -> resume/fallback` chain starts.

If positive, b89 can be narrowly scoped to a product-reproducible **project canonical-router entry** A/B using the official page/router and preserving `/g/.../c/...` without Native guessing. Keep ordinary `/c/...` behavior unchanged unless separate evidence requires modification.

If negative, trusted browser activation remains a separate candidate; do not synthesize protocol requests.

## Preserved boundaries

- client-owned Send keeps true same-response SSE;
- `ConversationRepository` remains sole Native response/content authority;
- `AuthSessionStore` remains sole Native auth/account authority;
- default persistent `WKWebsiteDataStore` remains persistent Web auth authority;
- no Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store;
- hidden thoughts remain non-presentational;
- b80 presentation/final boundaries remain preserved.

## Session round counter

This user turn is **round 35**.
