# DEV-send-stream

## Status

**Active — b88 focus A/B remains closed: focus alone is insufficient. Two trusted visible official-Web project/GPT-scoped Runtime samples use canonical `/g/{x}/c/{x}` same-document SPA entry and start official continuation (`stream_status`, page-owned `/resume`, then page-owned status/snapshot fallback in the current 404-resume samples). Corrected Control A now proves an untrusted programmatic click on the real official scoped anchor can reproduce the same SPA `history.pushState`, scoped `/g/{x}/c/{x}` route, conversation bootstrap and plural snapshots while transient user activation is false, but it does not start `stream_status` or `/resume` over the observed ~53-second window. Therefore correct scoped route + official SPA transition are not sufficient in this sample; trusted target-entry activation/lifecycle is now the strongest remaining differential. Control B is next: exact scoped full navigation. Do not allocate b89 before Control B. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Verified PR head before this Runtime-doc write: `88bf1f558cdec762a5609822126913c7d26a67f3`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 canonical Artifact: `9848999246`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Batch recovery point — Control A close

This round contains docs/PR synchronization only; no product/config/version/Candidate/Artifact source changed.

Confirmed complete:

- PR #29 title/body updated to the decisive Control A interpretation.
- This checkpoint records the same Runtime result and next exact action.

Still pending for the same evidence batch:

- create one durable Runtime evidence file for corrected Control A;
- after that, verify actual PR head and leave the checkpoint on Control B as the next Human gate.

Do not touch product source, b88 identity, Candidate allocation, Artifact identity, or ordinary-conversation navigation while recovering this batch.

## Closed b88 Runtime conclusion

Exact b88 proves `WKWebView.becomeFirstResponder()` can make the covered page `document.hasFocus=true`, but the same external generation continued through multiple PC tool rounds while covered production emitted zero matching `stream_status`, `/resume`, external SSE or page-owned snapshot. Focus is rejected as a sufficient activation condition under current direct full `/c/<conversation>` load. Automatic final convergence also required explicit Sync.

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-positive-near-terminal-inconclusive-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-sufficient-rejected-20260902.md`

## Trusted visible project continuation — positive controls

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-visible-web-spa-continuation-20260903.md`.

Two independent project conversations reproduced:

`/ -> trusted official anchor -> history.pushState -> /g/{x}/c/{x} -> plural snapshot + bootstrap -> stream_status -> /resume -> HTTP404 JSON -> repeated page-owned stream_status + plural snapshot`.

Neither current project sample is HTTP200 resume-SSE; continuous-looking UI is official continuation but must not be labelled SSE without `Content-Type: text/event-stream` evidence.

## Confirmed source gap / scope correlation

- Current covered production hard-loads every target as `https://chatgpt.com/c/<conversationID>`.
- Native `ConversationSummary` / `ConversationDetail` do not preserve project/GPT scoped route identity at this boundary.
- User reports prior ordinary non-project cases where Sync exposed the current reasoning block and later progression continued automatically, while recent repeated covered-production failures were project conversations.
- External read-only comparison research strongly corroborates `gizmo_id` as a scoped-route/project discriminator, but that remains external corroboration rather than our own Runtime causality proof.

## 2×2 causal matrix

| Entry | Route | Current result |
|---|---|---|
| Full load | `/c/{id}` | Negative in b88 project samples |
| Full load | exact official `/g/{scope}/c/{id}` | Unknown — Control B |
| SPA programmatic click | exact official `/g/{scope}/c/{id}` | **Router/bootstrap Positive; continuation Negative in corrected Control A** |
| SPA trusted click | exact official `/g/{scope}/c/{id}` | Positive — two visible-Web samples |

## Corrected Control A — decisive Runtime result

The second Control A attempt fixed the earlier missing-anchor problem.

Preconditions/results:

1. root page `/` verified;
2. target project scoped route saved from the real official conversation;
3. returned to `/` in the same document;
4. sidebar/project list expanded;
5. non-mutating anchor probe found `matchCount=1`, `visibleMatchCount=1`;
6. Control A probe installed on `/`;
7. launcher armed for delayed target click;
8. at target-click time `activationAtClick=false`;
9. captured target click was `isTrusted=false`, `userActivationIsActive=false`, target route `/g/{x}/c/{x}`;
10. official page performed `history.pushState` to `/g/{x}/c/{x}`;
11. page issued plural snapshot GET + conversation bootstrap/detail POST; both returned HTTP200 JSON;
12. page issued another plural snapshot GET, also HTTP200 JSON;
13. over the roughly 53 seconds from synthetic target click to final dump, the probe recorded **zero matching `stream_status`, zero `/resume`, and no page-owned continuation chain**;
14. the page visibly entered the project conversation and showed active-response UI/Stop.

A later unrelated trusted click inside the already-entered page did not produce `stream_status`; this does not prove arbitrary trusted interaction is sufficient. The causal difference against the two trusted positive controls is specifically the trusted target-entry activation/lifecycle.

Classification:

- programmatic official-anchor routing: **Runtime Positive**;
- correct scoped `/g/.../c/...` route: **Runtime Positive**;
- bootstrap/plural initial acquisition: **Runtime Positive**;
- page-owned continuation activation under untrusted target entry: **Runtime Negative in this sample**;
- trusted target-entry activation as necessary condition: **Strongest remaining hypothesis, not yet fully proven**.

## Next exact action — Control B Human gate

Do not change product code and do not allocate b89 yet.

Use the same pattern with a deliberately active project response, but instead of SPA clicking the anchor, perform a **fresh full document navigation to the exact official scoped `/g/{scope}/c/{conversation}` URL** and observe whether that fresh load itself starts `stream_status -> /resume/fallback`.

Decision:

- Control B Positive: exact scoped full-load can activate continuation; route identity may be sufficient for a narrow product change without SPA/trusted-click emulation.
- Control B Negative: route alone and untrusted SPA are both insufficient; trusted official target-entry activation/lifecycle becomes the strongest required condition and b89 must not be route-only.

## Preserved boundaries

- client-owned Send keeps true same-response SSE;
- `ConversationRepository` remains sole Native response/content authority;
- `AuthSessionStore` remains sole Native auth/account authority;
- default persistent `WKWebsiteDataStore` remains persistent Web auth authority;
- no Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store;
- hidden thoughts remain non-presentational;
- b80 presentation/final boundaries remain preserved.

## Session round counter

This user turn is **round 41**.
