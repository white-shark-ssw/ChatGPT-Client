# DEV-send-stream b87 — covered page visible/unfocused, continuation absent — 2026-09-02

## Evidence identity

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b87`
- App: `0.1.0 (87)` Release
- Built source marker: `49cf74f5f97e`
- Canonical Artifact: `9837745187`
- Canonical IPA SHA-256: `02598b5325c65f2ae3402e97812eca5676debc56a475963c0e8e7a9127a2b1ba`
- Device: iPhone / iOS17.0
- Target privacy-safe conversation hash: `sha256:e1e56d1afe93`
- Runtime source: user-exported `ChatGPTClient-Diagnostics-20260902-094529.json`

## Purpose

b86 established that the covered official page did not issue `stream_status` at all after an explicit Sync/re-arm, but it could not distinguish hidden/off-window/readiness state from focus/router activation differences. b87 added diagnostics only; it did not change continuation behavior.

The b87 Runtime gate therefore asks whether the covered official page is structurally visible and ready when continuation fails.

## Timeline

### Target selection and active authoritative tail

- `09:40:35` target conversation selected.
- Covered executor attached using the default persistent WebKit store.
- At attach/before initial observe load, Auto Layout had not yet resolved bounds (`boundsEmpty=true`), which is expected at that instant.
- `09:40:36` the initial target page reached route shape `conversation` and progressed `loading -> interactive -> complete` with `visibilityState=visible`, `document.hidden=false`, and `document.hasFocus=false`.
- `09:40:36` initial authoritative Detail returned HTTP200 with:
  - visible messages: `1`
  - mapping count: `168`
  - trailing timeline: `66`
  - trailing reasoning: `0`
  - trailing tools: `66`
- At page `did_finish`, the WKWebView had:
  - `windowAttached=true`
  - `windowIsKey=true`
  - `hidden=false`
  - `alphaZero=false`
  - `boundsEmpty=false`
  - `intersectsWindow=true`
  - `subviewIndex=0`
  - `visibleSiblingCountAbove=1`
  - `userInteractionEnabled=false`

### One explicit Sync during active generation

- `09:40:43` user requested `同步最新消息` once.
- `09:40:44` authoritative Detail returned HTTP200 with:
  - visible messages: `1`
  - mapping count: `170`
  - trailing timeline: `67`
  - trailing reasoning: `0`
  - trailing tools: `67`
- Repository started `responseGeneration=1` from `external_authoritative_detail` and applied one live presentation row.
- The Detail delta `mapping 168 -> 170` and `trailing 66 -> 67` proves the server-side response was actively evolving at the time of the continuation test.

### Manual re-arm page state

- `09:40:44` manual re-arm began.
- Old navigation emitted `pagehide` followed by one expected transitional `visibilitychange` hidden event on route shape `other`.
- The new target document immediately returned to route shape `conversation` and progressed `loading -> interactive -> complete`.
- All new-document activation events reported:
  - `visibilityState=visible`
  - `document.hidden=false`
  - `document.hasFocus=false`
- `09:40:45` page load completed.
- Native WKWebView at `did_finish` again reported:
  - attached to key window;
  - not hidden;
  - non-zero bounds;
  - intersects window;
  - one visible sibling above it;
  - interaction disabled.

### No continuation during a long clean foreground window

From the completed manual-rearm load at `09:40:45` until the first app `willResignActive` at `09:43:26`, approximately **161 seconds** elapsed with the app foregrounded.

During that clean interval there were zero matching:

- `coveredExecutor.externalStreamStatusRequest`
- `coveredExecutor.externalStreamStatusResponse`
- `coveredExecutor.externalResumeRequest`
- `coveredExecutor.resumeResponse`
- `externalStreamingObserved`
- page-owned external conversation snapshots
- DOM continuation snapshots

Therefore the exact b87 covered page did not enter the official continuation path despite being loaded, Page-Visibility-visible, on the conversation route, attached to the key window and intersecting it.

### Automatic final convergence also absent

- User WebSocket structural frames during the run stayed `hasConversationKey=false` / `targetMatch=false`.
- Foreground/background transitions caused socket error/close/reconnect, but later messages still did not match the target conversation.
- No automatic authoritative completion Sync fired.
- `09:45:21` the user manually requested Sync again.
- `09:45:22` authoritative Detail returned:
  - visible messages: `2`
  - mapping count: `197`
  - trailing timeline: `0`
- `liveResponse.externalDetailReconciled(reason=authoritative_assistant_materialized)` then cleared the live row and materialized the completed assistant.

This confirms that final reconciliation remains correct **once authoritative Detail is fetched**. The failure is automatic discovery/triggering, not the final reconcile operation itself.

## Runtime conclusions

### Proven / rejected hypotheses

- **Proven:** authoritative Detail can expose and project an active external response.
- **Proven:** the covered page can be `visibilityState=visible`, `document.hidden=false`, ready `complete`, route `conversation`, attached to a key window, non-empty and intersecting the window while continuation remains absent.
- **Rejected as primary explanations:** page hidden state, detached WebView, zero/off-window geometry after load, incomplete document readiness, wrong conversation route, or simply insufficient foreground wait.
- **Proven observation:** `document.hasFocus()` remained `false` for every recorded b87 activation event.
- **Proven structure:** the covered WKWebView remains non-interactive and under one visible Native sibling.
- **Not proven:** that focus, interactivity, or occlusion is the causal requirement for official continuation.
- **Still plausible:** the missing trigger is the genuine official SPA/router conversation-entry transition produced by a visible user navigation rather than a programmatic full `/c/<id>` load.
- `/resume` offset remains downstream; no b87 evidence justifies guessing or constructing it.

## Next evidence gate

Do not allocate b88 yet. Use the existing visible Web Rule Lab with the same default persistent WebKit store.

While another official client has a sufficiently long response active:

1. visibly open the official Web page in Web Rule Lab;
2. visibly tap/enter the same active conversation;
3. run a privacy-safe probe returning only `document.visibilityState`, `document.hidden`, `document.hasFocus()`, `document.readyState`, and coarse route shape;
4. return the result.

Interpretation:

- visible known-good path `hasFocus=true` vs covered b87 `hasFocus=false` -> focus/activation A/B becomes evidence-backed for the next candidate;
- visible known-good path also `hasFocus=false` while continuation starts -> reject focus as causal and investigate the SPA/router entry transition instead.

No polling, timer, retry, guessed offset, Native-constructed `stream_status`/`resume`, second response authority, or hidden-thought presentation is authorized by this evidence.

## Evidence classification

- Code written: Yes (b87 diagnostics only)
- PR CI: Passed
- Artifact/package identity: Verified
- Runtime/manual/real-device: **Diagnostic Positive**
- Cross-platform automatic continuation: **Rejected in this exact run**
- Automatic final convergence: **Rejected in this exact run**
- Stable/Frozen Send: **No**
