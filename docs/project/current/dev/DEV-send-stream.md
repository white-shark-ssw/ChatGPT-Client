# DEV-send-stream

## Status

**Active — b88 focus A/B remains closed: focus alone is insufficient. Two independent visible official-Web project/GPT-scoped Runtime samples use canonical `/g/{x}/c/{x}` same-document SPA entry and then start official continuation (`stream_status`, page-owned `/resume`, and repeated page-owned `stream_status + plural snapshot` when `/resume` returns HTTP404 JSON). Current production still hard-loads every conversation as `/c/<conversationID>`, while Native conversation models/list cache discard project/GPT scoped route identity. External read-only comparison research independently corroborates that `gizmo_id` is used by current third-party implementations to distinguish `/c/{conversation}` from `/g/{gizmo}/c/{conversation}` and Project membership/scope, but this remains external corroboration rather than our own Runtime causality proof. The first untrusted-anchor Control A attempt is **Infrastructure/Inconclusive**, not Negative: transient user activation was successfully false, but the target scoped anchor was absent from the root-page DOM (`matchCount=0`), so no synthetic target click or router transition occurred. Do not allocate b89 until Control A is rerun with the official target anchor present and Control B is measured. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Verified PR head before this checkpoint write: `e4fb022fbfbf59904f581fba196f5ee6b7788c32`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 canonical Artifact: `9848999246`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Recovery note

A prior docs-only round emitted multiple sequential checkpoint replacement commits while recording the 2×2 gate. No product/config/version/Candidate/Artifact file changed. Treat the latest checkpoint as authority; do not replay those writes. PR metadata may be temporarily behind and can be synchronized after the Human Runtime matrix without changing experiment validity.

## Closed b88 Runtime conclusion

Exact b88 proves `WKWebView.becomeFirstResponder()` can make the covered page `document.hasFocus=true`, but the same external generation continued through multiple PC tool rounds while covered production emitted zero matching `stream_status`, `/resume`, external SSE or page-owned snapshot. Focus is rejected as a sufficient activation condition under current direct full `/c/<conversation>` load. Automatic final convergence also required explicit Sync.

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-positive-near-terminal-inconclusive-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-sufficient-rejected-20260902.md`

## Visible project/GPT-scoped official-Web continuation — two positive samples

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-visible-web-spa-continuation-20260903.md`.

Both independent project conversations reproduced:

`/ -> trusted official anchor -> history.pushState -> /g/{x}/c/{x} -> plural snapshot + bootstrap -> stream_status -> /resume -> HTTP404 JSON -> repeated page-owned stream_status + plural snapshot`.

Neither current project sample is HTTP200 resume-SSE; continuous-looking UI is official continuation but must not be labelled SSE without `Content-Type: text/event-stream` evidence.

## Ordinary-vs-project scope correlation

User Runtime report:

- ordinary non-project conversations previously had cases where explicit Sync exposed the current reasoning block and later progression then continued automatically;
- recent repeated covered-production no-continuation failures were project conversations;
- both current known-good visible project samples use `/g/{x}/c/{x}`.

This is strong scope correlation, not yet a controlled same-build ordinary-vs-project A/B.

## Confirmed source gap

Current `CoveredWebSendExecutor.observeExistingConversation` and `sendExistingConversation` always construct `https://chatgpt.com/c/<conversationID>` and call `WKWebView.load`.

Current Native `ConversationSummary` preserves only `id`, `title`, `updateTime`; list parsing/cache preserve the same fields; `ConversationDetail` has no project/GPT scoped route identity. Therefore the product currently loses information needed to reproduce canonical `/g/<scope>/c/<conversation>` entry.

Classification:

- scoped identity information loss in current source: **Confirmed**;
- external `gizmo_id` semantics: **Strongly corroborated by read-only comparison research**;
- target project has scoped official anchor `/g/{x}/c/{x}`: **Runtime Positive**;
- scoped identity loss as continuation root cause: **Unverified**.

## 2×2 causal matrix

| Entry | Route | Current result |
|---|---|---|
| Full load | `/c/{id}` | Negative in b88 project samples |
| Full load | exact official `/g/{scope}/c/{id}` | Unknown — Control B |
| SPA programmatic click | exact official `/g/{scope}/c/{id}` | Infrastructure/Inconclusive — first attempt found no target anchor in root DOM |
| SPA trusted click | exact official `/g/{scope}/c/{id}` | Positive — two visible-Web samples |

## Control A attempt 1 — anchor absent / Inconclusive

User followed the intended sequence correctly:

1. root page verified `path=/`, `state=ROOT`;
2. manually entered the target project conversation;
3. save-and-back script returned `ok=true`, `targetSaved=true`, `targetShape=/g/{x}/c/{x}` and used `history.back()`;
4. root verification returned `path=/`, `state=ROOT`, `targetSaved=true`;
5. Control A probe installed successfully with `currentRoute=/`, `targetSaved=true`;
6. launcher armed for an 8-second delayed synthetic click;
7. at click time `activationAtClick=false`, proving transient browser user activation had expired;
8. launcher found `matchCount=0` and terminated as `aborted_anchor_not_found`;
9. probe recorded no synthetic scoped-anchor click, no `history.pushState`, and no continuation request chain.

The screenshots show the root page with the navigation/sidebar collapsed, consistent with the target conversation anchor not being mounted in the current DOM. Therefore this attempt does **not** test whether `isTrusted=false` can activate the official router. It is not evidence against programmatic SPA entry.

## Next exact action — Human Web Rule Lab gate

Repeat Control A, but first ensure the official target project conversation anchor is actually present in the root-page DOM. The simplest controlled path is:

1. return to `/` with the saved target pathname still present;
2. manually expand the official sidebar/navigation so the project conversation list is mounted;
3. run a non-mutating anchor-presence probe and require exactly one matching `/g/.../c/...` target anchor (`matchCount >= 1`) before arming the experiment;
4. then do not touch the page; wait until `navigator.userActivation.isActive=false`;
5. run the same delayed programmatic target-anchor click and capture `isTrusted=false`, activation false, and whether `history.pushState -> bootstrap/plural snapshot -> stream_status -> /resume/fallback` occurs.

Manual sidebar expansion before the activation-expiry wait is allowed; the causal variable is the **target conversation click**. The launcher must still prove activation false at that target click.

After Control A is decisive, Control B will full-navigate to the exact official scoped href and use a post-navigation privacy-safe resource/state probe to separate scoped route from SPA lifecycle.

## b89 gate

Do not allocate b89 before Controls A and B are known. The eventual b89 must change only the one variable supported by the matrix. Do not combine `gizmo_id` model changes, router changes, resume synthesis, WebSocket subscription, retries/polling or ordinary-conversation navigation changes in one Candidate.

## Preserved boundaries

- client-owned Send keeps true same-response SSE;
- `ConversationRepository` remains sole Native response/content authority;
- `AuthSessionStore` remains sole Native auth/account authority;
- default persistent `WKWebsiteDataStore` remains persistent Web auth authority;
- no Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store;
- hidden thoughts remain non-presentational;
- b80 presentation/final boundaries remain preserved.

## Session round counter

This user turn is **round 39**.
