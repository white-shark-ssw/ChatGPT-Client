# DEV-send-stream

## Status

**Active — b67 protected-Send transport remains Runtime accepted; exact b72 Runtime positively supports the tested A-generating + B-send simultaneous-generation path. Exact b74 is a valid/permanently-reserved package. Exact b74 iPhone/iOS17 Runtime is now partial/rejected for three concrete issues: page-owned external `/resume` request observation can create a false Native `回答失败` before the response is validated; successful explicit Sync/Reload does not clear that stale external terminal presentation; and first/changed long-history geometry can synchronously block the main UI for seconds, including left-edge back interaction. The user also corrected the requested text line-height mapping. b75 is allocated for only these evidence-backed corrections. Stable/Frozen Send remains No; PR #29 stays open/unmerged.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged
- Actual `main`: `d323b9eed2dda75b9986fc06e14014d3e9b365fb`
- Formal head before this checkpoint write: `f883326696676e30719f3e6fbe3c44152d79a0f2` — docs-only descendant of exact b74 product source.
- Exact b74 product/config source: `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`
- b74 Candidate / Version-Build: `DEV-send-stream-0.1.0-b74` / `0.1.0 (74)`
- b74 Push CI: `33420408779 / 99581104920` — success
- b74 PR CI: `33420412792 / 99581117817` — success
- b74 canonical Artifact: `9768668727`
- b74 ZIP: `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`
- b74 IPA SHA: `07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`
- b39-b74 permanently reserved.
- **Allocated next Candidate: `DEV-send-stream-0.1.0-b75` / `0.1.0 (75)`. No b75 Artifact exists at allocation.**
- Stable/Frozen Send: No.

## Retained accepted boundaries

- b67: one local Native Send -> one official-page protected `/backend-api/f/conversation` -> HTTP200 same-response SSE -> Repository reasoning/tool/final -> terminal/reconcile is Runtime accepted.
- b72: tested A-generating + B-send/generate simultaneous-generation is Runtime positive; do not regress per-conversation executor ownership.
- `ConversationRepository` remains sole conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole account authority; default `WKWebsiteDataStore` remains sole persistent auth-secret authority.
- Covered official Web remains browser challenge/protected-Send/page-owned continuation transport only; full Web conversation rendering remains rejected.
- Cross-device continuation may consume only an official-page-owned matching `/backend-api/f/conversation/resume`; Native must not construct resume, derive/choose offset, poll `stream_status`, replay browser/session headers or use WebSocket frames as response-body authority.
- b69 chronological reasoning/tool ordering + exact-parent tool association remain retained.
- b38 deterministic/manual long-message geometry, bounded chunks, semantic rounds, Copy and quick-navigation remain accepted semantics. Performance work may change scheduling, not final geometry/ownership semantics.
- `assistant:thoughts` and `inline_cot_expandable_content` remain non-presentational.
- No retry/polling/timer/watchdog/fallback/compatibility shim/second message or response store.

## Exact b74 Runtime evidence — 2026-09-01

User supplied three screenshots plus exact diagnostics `ChatGPTClient-Diagnostics-20260831-175939.json`. Diagnostics metadata proves `DEV-send-stream-0.1.0-b74`, Build74, source marker `50dd61b8b31c`, Release, iPhone, iOS17.0.

### 1. External-platform response can become false Native `回答失败`

User reproduced: another platform sends a message; entering that conversation in Build74 shows `回答失败`. Even after the external answer has completed, explicit `同步最新消息` and `重载当前会话` continue to leave the failure row visible.

Exact diagnostics for the affected conversation show:

- `17:57:17` `liveResponse.started`, `source=external_resume`, generation 1, phase `thinking`, baseline visible count 9;
- same moment `coveredExecutor.externalResumeObserved`;
- `17:57:18` `coveredExecutor.resumeResponse`: **HTTP404**, `application/json`;
- immediately `coveredExecutor.failed reason=resume_not_sse` and Repository `liveResponse.event=failed`, phase `failed`, zero reasoning/final/tool content.

Current b74 source explains the defect: `external_resume_observed` promotes `observationEvents` to `activeEvents` and Root immediately calls `beginExternalLiveResponse(...)` **before** the page-owned resume response is known to be HTTP200 SSE. A matching request observation therefore incorrectly becomes user-visible response authority.

**b75 rule:** a matching page-owned `/resume` request is structural observation only. Repository external live-response ownership begins only after the same page-owned response is validated as exact HTTP200 `text/event-stream` (`responseAccepted`). A page-owned 404/non-SSE before validation must not create a Native response snapshot and must not display `回答失败`. It remains diagnosable and the executor may be released; no retry/polling/fallback is added.

### 2. Successful authoritative Sync/Reload does not clear stale external terminal presentation

The same b74 export proves manual recovery itself succeeds:

- `17:58:01` explicit latest Sync -> `17:58:03` Detail HTTP200, ~635 KB, 128 mappings, 9 visible messages, `latestSync.end status=ok`, 3 changed visible messages;
- `17:58:07` Reload -> `17:58:08` Detail HTTP200, 9 visible messages, `conversationReload.end status=ok`, 4 changed visible messages;
- another Reload at `17:58:15` -> `17:58:17` HTTP200 and authoritative changes again.

So the screenshot is not a Sync/Reload network failure. The stale external failed live snapshot remains layered above the newly authoritative Detail because existing `clearLiveResponseAfterAuthoritativeReconcile` requires a terminal response generation plus `authoritativeVisibleMessageCount > baselineVisibleMessageCount`; here the authoritative content changed while count stayed 9.

**b75 rule:** after a successful explicit authoritative Sync/Reload, a terminal **external** live snapshot may be discarded even when visible message count does not increase, because that fresh Detail is the authority. Do not broadly clear local failed Sends. Under current source, local validation Send always has non-empty `promptText`; external adoption has empty `promptText`, so the correction can stay response-local without a second state owner.

### 3. b74 geometry reuse is positive, but first/changed history can still block back navigation

b74 resident derived-geometry reuse works when identity is unchanged: the supplied export contains multiple `geometryReused=true` resident applies completing in only a few milliseconds (for example a 9-message / 16-row presentation around 3–5 ms).

The new exact defect is the cache-miss/changed-history path. The same Build74 export contains:

- 38 authoritative messages / 77 rows: full geometry around **2452 ms**;
- 74 authoritative messages / 170 rows: `messagePresentation.rebuilt durationMs=10098.53`, `geometryDurationMs=10047.64`, `geometryReused=false`;
- one very large Detail request: ~15.46 MB, 3893 mappings, 51 visible messages, `detailLoad.end durationMs=14803.70`;
- another multi-megabyte Detail with 809 mappings / 74 visible messages also takes multiple seconds before presentation.

User reports that if the conversation is just about to finish loading/displaying, a left-edge right-swipe Back has high latency and feels blocked. Current source performs cache-miss `rebuildPresentationGeometry(...)` synchronously in `apply(_:)` / `rebuildRoundProjection()` on the UI path, looping every presentation row and measuring text before the table is applied. This exact synchronous geometry window matches the Runtime symptom.

**b75 scheduling rule:** preserve the exact b38-derived geometry result and b74 cache, but make a cache-miss/changed historical geometry build cooperative rather than one uninterrupted main-thread loop. Build the same row metrics/offsets in bounded main-queue batches that yield between batches and are guarded by the existing conversation/presentation generation identity before committing. No timer, debounce, watchdog, retry or approximate geometry is authorized. A superseded target must not commit late geometry. Cache hits remain immediate. The goal is specifically to let interactive Back/user navigation regain the run loop instead of waiting behind a multi-second synchronous loop.

## Exact typography correction from user screenshots

Current Build74 source values are now verified:

- reasoning paragraph `minimumLineHeight = 26`;
- tool paragraph `minimumLineHeight = 34`;
- final answer uses plain `UILabel.text` / natural body-font measurement and therefore has no explicit matching line-height contract.

The user explicitly corrected the desired mapping:

1. **Tool message line height = the current reasoning line-height value = 26.**
2. **Reasoning text line height = 26 × 70% = 18.2** (30% reduction).
3. **Formal/final assistant answer line height = the same 18.2.**
4. Final answer measurement and rendering must use the same paragraph line-height style so deterministic geometry remains consistent.
5. User-message bubble typography is not part of this request.
6. Do not reinterpret this as increasing reasoning spacing again. Other tool ordering/filtering/title semantics remain unchanged.

Because preferred `.body` font natural line height can exceed 18.2, b75 must use an explicit paragraph line-height style for reasoning/final rather than setting only a minimum that has no reducing effect. Keep font size/weight unchanged unless exact compile/runtime evidence requires otherwise.

## b75 minimal implementation scope

Expected product files, subject to source audit:

- `ChatGPTClient/RootViewController.swift`
  - external observation starts Repository generation only on validated `.responseAccepted`;
  - pre-accept non-SSE failure remains non-presentational and releases observation executor;
  - no local Send route/selector/SSE grammar changes.
- `ChatGPTClient/Conversation/ConversationFeature.swift`
  - exact 26 / 18.2 / 18.2 line-height mapping with matching assistant-final measurement/rendering;
  - successful explicit Sync/Reload clears only terminal external live snapshot;
  - cache-miss historical geometry is cooperatively batched with current presentation-generation/target freshness and the same final metrics/offsets.
- `ChatGPTClient.xcodeproj/project.pbxproj` and `.github/workflows/ios-foundation.yml`
  - b75 identity only after product code is audited/compiled.

No auth module, list transport, Web selector, protected-Send route, parser grammar, second cache/store or persistence change is currently authorized.

## b75 acceptance gate

Static/CI before Artifact:

1. exact product diff limited to evidenced files plus Build/workflow identity;
2. `git diff --check`;
3. Xcode 16.4 iOS Simulator compile;
4. retained assertions for local `/backend-api/f/conversation`, verified composer selectors, page-owned matching `/resume`, no Native resume/offset/polling/retry/timer/watchdog;
5. source assertions for external begin only after response acceptance, external-terminal authoritative recovery, and 26/18.2/18.2 line-height contract;
6. geometry batching must keep same deterministic `ConversationMessageCell.metrics` result and reject superseded presentation generation.

Human iPhone/iOS17 Runtime after exact b75 Artifact:

1. external-platform response: enter while still active; only a validated HTTP200 SSE resume may create `正在思考`/reasoning/tool/final. A page-owned 404/non-SSE must not create `回答失败`.
2. after any external terminal/error state, successful explicit Sync and Reload must show authoritative Detail without stale `回答失败` overlay.
3. tool rows use 26 line height; reasoning and final assistant text use the same 18.2 compact line height; chronology and hidden-thought exclusion remain correct.
4. reproduce a multi-second first/changed long-history load and begin left-edge Back near presentation time; Back must remain interactive rather than wait behind one multi-second geometry loop.
5. repeat resident re-entry and confirm b74 `geometryReused=true` fast path remains.
6. regression-test one normal b67 local Send and b72 simultaneous A/B generation.
7. b38 Copy/round/quick-navigation/final geometry correctness remains intact.

## Batch recovery point — b75 allocation

Known baseline before this checkpoint write:

- formal head `f883326696676e30719f3e6fbe3c44152d79a0f2`;
- PR #29 open / mergeable / unmerged at that head;
- actual main `d323b9eed2dda75b9986fc06e14014d3e9b365fb`;
- unique Active dev checkpoint is `DEV-send-stream`;
- b74 immutable Artifact identity above;
- no repository match for `DEV-send-stream-0.1.0-b75` before allocation;
- b75 allocated now, no Artifact.

Deterministic batches:

1. re-read the exact formal docs head created by this checkpoint write;
2. create one isolated b75 assembly/tooling branch from that exact head;
3. implement only the three Runtime corrections above and run source/scope/diff checks plus Xcode 16.4 Simulator build;
4. audit clean product commit parent and exact file scope;
5. final Guard against formal/PR/main/checkpoint/conflicts;
6. non-force fast-forward formal only to the audited b75 product/config source;
7. exact-head Push + PR CI; if green, use Push Artifact as canonical b75 package and independently verify package identity;
8. sync checkpoint/durable docs/PR as docs-only state;
9. hand exact b75 IPA to the user for the Runtime matrix above.

Recovery must not rewrite b74, must not generalize page-owned resume 404 into a Web-rule fallback, must not add retry/polling/timer/watchdog, and must not change b38 semantic geometry/quick-navigation ownership.

## Exact next action

Read the formal branch head created by this checkpoint write, create the isolated b75 assembly branch from that exact head, implement the minimal external-adoption validation/recovery + 26/18.2/18.2 typography + cooperative cache-miss geometry scheduling changes, then compile/audit before any b75 promotion or Artifact production.
