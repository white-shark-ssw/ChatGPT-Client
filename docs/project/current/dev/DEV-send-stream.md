# DEV-send-stream

## Status

**Active — b88 focus A/B remains closed: focus alone is insufficient. Two trusted visible official-Web project/GPT-scoped Runtime samples use canonical `/g/{x}/c/{x}` same-document SPA entry and start official continuation (`stream_status`, page-owned `/resume`, then page-owned status/snapshot fallback in the current 404-resume samples). Corrected Control A proves an untrusted programmatic click on the real official scoped anchor can reproduce the same SPA `history.pushState`, scoped `/g/{x}/c/{x}` route, conversation bootstrap and plural snapshots while transient user activation is false, but it does not start `stream_status` or `/resume` over the observed ~53-second window. Therefore correct scoped route + official SPA transition are not sufficient in this sample; trusted target-entry activation/lifecycle is now the strongest remaining differential. Control B is next: exact scoped full navigation. Do not allocate b89 before Control B. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Feature head after durable Control A evidence: `3170e0fefd95865148213a6bec6ea29fb6605b69`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 canonical Artifact: `9848999246`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Durable Control A evidence

`docs/project/runtime-evidence/DEV-send-stream-untrusted-project-spa-no-continuation-20260903.md`

Corrected Control A result:

1. target project scoped route saved from the real official page;
2. returned to `/` in the same document;
3. sidebar/project list expanded;
4. target official anchor present: `matchCount=1`, `visibleMatchCount=1`;
5. delayed programmatic target click occurred with `activationAtClick=false`;
6. captured target click was `isTrusted=false`, `userActivationIsActive=false`;
7. official page performed `history.pushState` to `/g/{x}/c/{x}`;
8. plural snapshot GET + conversation bootstrap/detail POST returned HTTP200 JSON;
9. another plural snapshot GET returned HTTP200 JSON;
10. from target click to final dump (~53s), zero matching `stream_status`, zero `/resume`, and no page-owned continuation chain were observed;
11. page visibly entered the project conversation and showed active-response UI/Stop.

A later unrelated trusted click inside the already-entered page did not produce `stream_status`. That does not prove arbitrary later trusted interaction is sufficient; the strongest remaining differential is trusted **target-entry** activation/lifecycle.

Classification:

- programmatic official-anchor routing: **Runtime Positive**;
- correct scoped `/g/.../c/...` route: **Runtime Positive**;
- bootstrap/plural initial acquisition: **Runtime Positive**;
- page-owned continuation activation under untrusted target entry: **Runtime Negative in this sample**;
- trusted target-entry activation as necessary condition: **Strongest remaining hypothesis, not yet fully proven**.

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
| SPA programmatic click | exact official `/g/{scope}/c/{id}` | **Router/bootstrap Positive; continuation Negative** |
| SPA trusted click | exact official `/g/{scope}/c/{id}` | Positive — two visible-Web samples |

## Next exact action — Control B Human gate

Do not change product code and do not allocate b89 yet.

Use a deliberately active project response on another official client. In Web Rule Lab, perform a **fresh full document navigation to the exact official scoped `/g/{scope}/c/{conversation}` URL** and observe whether that fresh load itself starts `stream_status -> /resume/fallback`.

Decision:

- Control B Positive: exact scoped full-load can activate continuation; route identity may be sufficient for a narrow product change without SPA/trusted-click emulation.
- Control B Negative: route alone and untrusted SPA are both insufficient; trusted official target-entry activation/lifecycle becomes the strongest required condition and b89 must not be route-only.

## Evidence ladder / identity

- Control A: Web Rule Lab Runtime evidence only.
- No product source changed.
- No new Candidate allocated.
- No CI/Artifact/IPA produced.
- b88 identity remains unchanged.
- Stable/Frozen Send: No.

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
