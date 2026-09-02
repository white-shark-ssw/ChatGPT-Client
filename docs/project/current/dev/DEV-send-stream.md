# DEV-send-stream

## Status

**Active — b88 focus A/B remains closed: focus alone is insufficient. Two independent visible official-Web project/GPT-scoped Runtime samples use canonical `/g/{x}/c/{x}` same-document SPA entry and then start official continuation (`stream_status`, page-owned `/resume`, and repeated page-owned `stream_status + plural snapshot` when `/resume` returns HTTP404 JSON). Current production still hard-loads every conversation as `/c/<conversationID>`, while Native conversation models/list cache discard project/GPT scoped route identity. External read-only comparison research independently corroborates that `gizmo_id` is used by current third-party implementations to distinguish `/c/{conversation}` from `/g/{gizmo}/c/{conversation}` and Project membership/scope, but this remains external corroboration rather than our own Runtime causality proof. The next gate is a Web Rule Lab 2×2 that separates scoped route, SPA/router lifecycle, and trusted activation. Do not allocate b89 until the two unknown controls are measured. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Latest checkpoint docs head before PR metadata sync: `f46b56a7d2c0904669ca5320d8cfdd3670150ce8`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 canonical Artifact: `9848999246`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Batch recovery point — 2×2 evidence/docs sync

- baseline verified before this docs chain: PR #29 head `da4bf533f6df4d0a4843af19bbee3748d30c4ca6`, base `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- completed: checkpoint updated with external comparison classification, confirmed scoped-identity source gap, and the 2×2 Human Runtime gate;
- pending: sync PR #29 title/body to the same 2×2 gate;
- next exact action after PR sync: user runs Control A in visible Web Rule Lab; no product source/version/Candidate/Artifact changes;
- recovery must not touch b88 product source/package identity or allocate b89.

## Closed b88 Runtime conclusion

Exact b88 proves `WKWebView.becomeFirstResponder()` can make the covered page `document.hasFocus=true`, but the same external generation continued through multiple PC tool rounds while covered production emitted zero matching `stream_status`, `/resume`, external SSE or page-owned snapshot. Focus is rejected as a sufficient activation condition under current direct full `/c/<conversation>` load. Automatic final convergence also required explicit Sync.

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-positive-near-terminal-inconclusive-20260902.md`
- `docs/project/runtime-evidence/DEV-send-stream-b88-focus-sufficient-rejected-20260902.md`

## Visible project/GPT-scoped official-Web continuation — two positive samples

Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-visible-web-spa-continuation-20260903.md`.

Both independent project conversations reproduced:

`/ -> trusted official anchor -> history.pushState -> /g/{x}/c/{x} -> plural snapshot + bootstrap -> stream_status -> /resume -> HTTP404 JSON -> repeated page-owned stream_status + plural snapshot`.

The second sample continued paired status/snapshot requests through the ~45.6 second capture. Neither current project sample is HTTP200 resume-SSE; continuous-looking UI is official continuation but must not be labelled SSE without `Content-Type: text/event-stream` evidence.

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

Do not add `gizmo_id` to production or change ordinary navigation until causality is isolated.

## 2×2 causal matrix

| Entry | Route | Current result |
|---|---|---|
| Full load | `/c/{id}` | Negative in b88 project samples |
| Full load | exact official `/g/{scope}/c/{id}` | Unknown — Control B |
| SPA programmatic click | exact official `/g/{scope}/c/{id}` | Unknown — Control A |
| SPA trusted click | exact official `/g/{scope}/c/{id}` | Positive — two visible-Web samples |

Interpretation after both controls:

- A positive + B positive -> trusted activation and SPA are not required; scoped route becomes strongest candidate.
- A positive + B negative -> trusted activation not required; SPA/router lifecycle becomes strongest candidate.
- A negative + B positive -> scoped route works under full navigation; inspect whether synthetic click actually invokes the official router before blaming activation.
- A negative + B negative while trusted SPA stays positive -> trusted/transient activation becomes a stronger remaining candidate.

## Next exact action — Human Web Rule Lab gate

### Control A — first

Use a project conversation. Preserve the existing privacy-safe entry/network probe. From the target `/g/.../c/...` page, save the exact target pathname locally in the page, return to `/` in the same document, then trigger `.click()` on the matching official anchor only after transient `navigator.userActivation.isActive` is false. Acceptance requires the captured click to show `isTrusted=false` and `userActivationIsActive=false`.

Observe whether the page itself still performs:

`history.pushState -> /g/.../c/... -> bootstrap/plural snapshot -> stream_status -> /resume or official fallback`.

Do not Send a new prompt and do not Native-construct status/resume.

### Control B — only after Control A result

Use the official page's exact scoped href; do not guess the scope ID. Perform a true full document navigation to that exact `/g/.../c/...` URL for another external-active project response, then use a post-navigation privacy-safe resource/state probe to determine whether page-owned bootstrap/status/resume/snapshot traffic starts. This fills the route-vs-SPA control.

## b89 gate

Do not allocate b89 before Controls A and B are known. The eventual b89 must change only the one variable supported by the matrix. In particular do not combine `gizmo_id` model changes, router changes, resume synthesis, WebSocket subscription, retries/polling or ordinary-conversation navigation changes in one Candidate.

## Preserved boundaries

- client-owned Send keeps true same-response SSE;
- `ConversationRepository` remains sole Native response/content authority;
- `AuthSessionStore` remains sole Native auth/account authority;
- default persistent `WKWebsiteDataStore` remains persistent Web auth authority;
- no Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store;
- hidden thoughts remain non-presentational;
- b80 presentation/final boundaries remain preserved.

## Session round counter

This user turn is **round 37**.
