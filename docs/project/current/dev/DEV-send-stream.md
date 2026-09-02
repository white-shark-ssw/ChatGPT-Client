# DEV-send-stream

## Status

**Active — Control B is Runtime Positive and materially changes the root-cause ranking. A fresh full document navigation to the exact official project/GPT-scoped `/g/{scope}/c/{conversation}` route, started with transient user activation false, did start the official page-owned continuation loop. This proves trusted target-entry click is not required and proves the current production loss of scoped project route identity is the strongest evidenced defect. Do not synthesize Native `stream_status`/`resume`; the page still owns continuation. Before b89 product code, verify from the current service payload which existing field supplies the scoped route identity (external research strongly suggests `gizmo_id`, but that field is not yet our own Runtime-confirmed contract). Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Verified feature head before this checkpoint write: `aa369ba43c490dca03acbcd168c920cda517e4eb`
- b88 Candidate / Build: `DEV-send-stream-0.1.0-b88` / `0.1.0 (88)`
- b88 exact product source: `31d24e8b9ab4676effd757a793162abbdb0d7012`
- b88 clean package head: `378811691ccbd6f44b232d8cc5564628e9b021e1`
- b88 canonical Artifact: `9848999246`
- b88 IPA SHA-256: `cb89cf51f451252087b2abdd6533407113614b2e9efa072ba84e4877f2d02298`
- b39-b88 permanently reserved
- Stable/Frozen Send: No

## Control B Runtime — exact scoped full navigation Positive

User Web Rule Lab result:

- marker `phase=full_navigation_started`;
- `activationAtNavigation=false`;
- target shape `/g/{x}/c/{x}`;
- current page `/g/{x}/c/{x}`, visible, `hidden=false`, `hasFocus=true`, `readyState=complete`;
- Navigation Timing `type=navigate` and duration about 926 ms, proving a fresh document navigation rather than same-document SPA transition;
- capture elapsed about 149 seconds after navigation request;
- Resource Timing not saturated: 24 total resources, `possiblySaturated=false`;
- page-owned observed counts: `plural_snapshot=9`, `stream_status=8`, `resume=0`, `conversation_detail=0` in this post-load Resource Timing window;
- first observed plural snapshot at ~89.1s; then from ~96.4s through ~145.7s the page repeatedly issued paired `stream_status + plural_snapshot` requests roughly every 6-8 seconds;
- interpretation flags: `bootstrapObserved=true`, `continuationObserved=true`.

This is official page-owned continuation but is **not evidence of resume-SSE** in this run because no `/resume` resource was observed. The current official page can continue the external active response through its own status/snapshot path.

## 2×2 causal matrix — now decisive

| Entry | Route | Result |
|---|---|---|
| Full load | `/c/{id}` | Negative in b88 project samples |
| Full load | exact official `/g/{scope}/c/{id}` | **Positive — Control B; page-owned status/snapshot continuation started** |
| SPA programmatic click | exact official `/g/{scope}/c/{id}` | Router/bootstrap Positive; continuation Negative in Control A |
| SPA trusted click | exact official `/g/{scope}/c/{id}` | Positive — two visible-Web samples |

Interpretation:

1. trusted click is **not required**, because Control B had activation false and still continued;
2. same-document SPA entry is **not required**, because Control B was a fresh `navigate`;
3. correct project/GPT scoped route identity is now the strongest evidenced differentiator versus the failed production `/c/{id}` path;
4. Control A shows that scoped route plus an untrusted SPA transition is not automatically equivalent to a fresh scoped document load; therefore b89 should preserve the currently evidenced full-load behavior rather than invent a router emulation;
5. Native must still not construct `stream_status`, `/resume`, offsets, cadence, polling or a second response authority.

## Confirmed source gap

Current source still has:

- `ConversationSummary`: `id`, `title`, `updateTime` only;
- `ConversationDetail`: no project/GPT scoped route identity;
- list cache persists only `id/title/updateTime`;
- `parseConversationSummary` reads only `id/title/update_time`;
- `CoveredWebSendExecutor.observeExistingConversation` and `sendExistingConversation` both hard-load `https://chatgpt.com/c/<conversationID>`.

Therefore current production cannot reproduce the exact scoped project full-load that Control B proved works.

## Remaining evidence gate before b89 code

External read-only comparison research strongly corroborates `gizmo_id` as the current service field used for `/g/{gizmo}/c/{conversation}` and Project membership. That is useful corroboration but does not satisfy the repository rule against guessing service fields.

Next Human Web Rule Lab gate: on a current project conversation, make one privacy-safe structural read of the current official conversation/list payload and return only booleans/types proving whether the matching current item/detail exposes a non-empty `gizmo_id` (or another existing scoped-route field). Do not return the actual ID, body, title, Cookie, token or auth material.

If `gizmo_id` is Runtime-confirmed, b89 may be narrowly scoped to preserving that existing route identity through `ConversationSummary`/cache (and Detail only if required by actual call flow) and using exact full `/g/<scope>/c/<conversation>` navigation for project targets while leaving ordinary `/c/<conversation>` unchanged. Do not combine router emulation, resume synthesis, polling, WebSocket subscription or unrelated Send changes.

## Batch recovery point — Control B durable sync

Baseline before this write:

- feature head `aa369ba43c490dca03acbcd168c920cda517e4eb`;
- PR #29 open / mergeable / unmerged;
- main `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- b88 product/Candidate/Artifact/IPA identity unchanged.

Planned documentation batches:

1. checkpoint with exact Control B result and next source-field gate — **this batch**;
2. durable Runtime evidence file for Control B;
3. synchronize PR #29 summary;
4. close checkpoint recovery state after verifying actual head.

Do not touch product source, version/build settings, Candidate or Artifact during this docs batch. Durable MODULE_STATUS / TECHNICAL_DECISIONS / WEB_SEND_ADAPTER must be synchronized no later than the first b89 source-field/product milestone; current checkpoint + Runtime evidence outrank their earlier Control-A hypothesis in the interim.

## Evidence ladder / identity

- Control B: Web Rule Lab Runtime Positive for exact scoped full navigation and page-owned status/snapshot continuation.
- No product source changed yet.
- No new Candidate allocated yet.
- No CI/Artifact/IPA produced yet.
- b88 identity remains unchanged.
- Stable/Frozen Send: No.

## Preserved boundaries

- client-owned Send keeps true same-response SSE;
- cross-platform continuation follows genuine official page-owned SSE or page-owned status/snapshot behavior, whichever the official page actually emits;
- `ConversationRepository` remains sole Native response/content authority;
- `AuthSessionStore` remains sole Native auth/account authority;
- default persistent `WKWebsiteDataStore` remains persistent Web auth authority;
- no Native `stream_status`, `/resume`, guessed offset, polling, retry/watchdog, duplicate Send, WebSocket-body authority or second response store;
- hidden thoughts remain non-presentational;
- b80 presentation/final boundaries remain preserved.

## Session round counter

This user turn is **round 43**.
