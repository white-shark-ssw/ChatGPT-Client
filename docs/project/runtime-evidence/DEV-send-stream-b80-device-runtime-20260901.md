# DEV-send-stream b80 device Runtime — 2026-09-01

## Exact tested identity

- Candidate: `DEV-send-stream-0.1.0-b80`
- Version / Build: `0.1.0 (80)`
- Exact product/config source: `b0f51041c2d7b645f152752ea6196526b2e4e0f6`
- Diagnostics metadata: Release / iOS 17.0 / source marker `b0f51041c2d7`
- Canonical Push Artifact: `9801761448`
- IPA: `ChatGPTClient-0.1.0-b80-dev-send-stream.ipa`
- IPA SHA-256: `87c360175a4adc4fa476383b395cffe74c57c5e75db252dd49acdf42be39ce1f`

## User Runtime classification

### 1. Tool/timeline -> reasoning-divider spacing

**Accepted / Frozen for the current Send work.**

The user explicitly reports the b80 spacing result as normal and requests that this presentation boundary be frozen. Do not modify this spacing again without new explicit Runtime evidence/requirement.

### 2. External final materialization after adoption

**Positive for the adopted-response path.**

The supplied b80 diagnostics contain two external adopted-response sequences in which `finalCharacters` remains zero during the reasoning/final waiting phase and then materializes before Native terminal/reconcile:

- one sequence reaches `finalCharacters=5656` and terminal at `13:21:04Z`;
- another reaches `finalCharacters=2874` and terminal at `13:28:45Z`.

This is the intended b80 correction: the covered observation remains alive until a real final body materializes instead of terminalizing on the earlier COMPLETE boundary.

This does **not** establish token/SSE-delta progressive final streaming; the final body still appears as a materialized page snapshot.

### 3. External stopped-thinking semantics

**Accepted / Frozen semantic boundary for the current Send work.**

The user reports that manually stopping reasoning on the other platform is displayed correctly in b80. Stopped external reasoning/tools must remain reasoning/tools and must not be promoted into normal final body text. Do not alter this semantic boundary without new explicit Runtime evidence/requirement.

### 4. Cross-platform response acquisition before manual Sync

**Rejected / intermittent.**

The user tested two conversations and reports that one behaved normally while another failed to acquire even the reasoning stream until explicit Sync was pressed.

The diagnostics localize the remaining failure boundary to **external-response acquisition before Repository adoption**, not to the already-adopted b80 final-materialization gate:

- selection observation can load the covered target page without producing `coveredExecutor.externalStreamingObserved` or any `liveResponse.externalSnapshot`;
- in the `sha256:37824321c607` sequence, selection page load occurs at `13:27:04Z`; explicit Sync at `13:27:19Z` discovers server-side changes, then `manual_sync_rearm` reloads the same target; only after the re-armed page loads does `coveredExecutor.externalStreamingObserved` occur at `13:27:31Z`, followed by reasoning/tool snapshots from `13:27:37Z` onward;
- a prior sequence shows the same shape: selection page -> explicit Sync/re-arm -> external streaming observation -> reasoning/tool snapshots.

Current source confirms why this is an evidence boundary: external observation begins only after the official page itself issues a matching `stream_status` response with `status == IS_STREAMING` (or a validated matching resume SSE). The client does not generate that request. If the selected official page does not emit the target-specific signal, Repository live adoption cannot start.

Therefore no timer/poll/retry/watchdog, guessed Native `stream_status`, duplicate Sync, DOM-body authority, WebSocket-body authority or second response owner is authorized from this evidence.

## Account-wide official signal relevance

Separate user Runtime evidence already proves official PC Web can stay on conversation A while a never-opened conversation B completes and still show an upper-right new-answer bubble; official iOS similarly emits account-wide completion haptics. This now directly matters to the acquisition defect above: the official Web runtime has an account-level signal that is not inherently dependent on the target conversation page being selected.

Its exact transport/schema remains Unknown / Unverified. Before a product change, Web Rule Lab must capture that account-level signal privacy-safely while A remains open and B starts/completes elsewhere.

## b80 overall result

**Runtime partial-positive / partial-rejected.**

Accepted/frozen/preserve:

- b80 final tool/timeline -> divider spacing;
- adopted-response final materialization gate;
- external stopped-thinking semantics;
- explicit manual-Sync re-arm behavior.

Still rejected/open:

- reliable automatic acquisition of a newly-started cross-platform response;
- progressive external final token streaming;
- exact account-wide completion/new-answer transport and automatic Sync/haptic implementation.

Do not allocate or implement b81 until the account-wide Web signal probe identifies an exact evidence-backed event source or another deterministic source-level cause is proven.
