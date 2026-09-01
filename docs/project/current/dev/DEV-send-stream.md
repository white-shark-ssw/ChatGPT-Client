# DEV-send-stream

## Status

**Active — b80 Runtime is partial-positive / partial-rejected. The b80 spacing boundary is accepted and Frozen for this Work; adopted external final materialization and stopped-thinking semantics are Runtime positive. Reliable automatic acquisition of a newly-started cross-platform response remains rejected/intermittent. No b81 is allocated. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / unmerged
- Exact b80 product/config source: `b0f51041c2d7b645f152752ea6196526b2e4e0f6`
- Candidate / Version-Build: `DEV-send-stream-0.1.0-b80` / `0.1.0 (80)`
- Canonical Push Artifact: `9801761448`
- IPA: `ChatGPTClient-0.1.0-b80-dev-send-stream.ipa`
- IPA SHA-256: `87c360175a4adc4fa476383b395cffe74c57c5e75db252dd49acdf42be39ce1f`
- b39-b80 permanently reserved
- b80 Runtime/manual/real-device: **Partial-positive / partial-rejected**
- b81: **Not allocated**
- Stable/Frozen Send: **No**

Durable evidence:

- `docs/project/runtime-evidence/DEV-send-stream-b79-device-runtime-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-account-wide-web-notification-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b80-build-artifact-20260901.md`
- `docs/project/runtime-evidence/DEV-send-stream-b80-device-runtime-20260901.md`

## Identity / validation retained

Formal b80 source `b0f51041c2d7b645f152752ea6196526b2e4e0f6` changes exactly:

- `.github/workflows/ios-foundation.yml`
- `ChatGPTClient.xcodeproj/project.pbxproj`
- `ChatGPTClient/Conversation/ConversationFeature.swift`
- `ChatGPTClient/RootViewController.swift`

Validation/artifact:

- guarded assembly `33506668882`: exact-scope/static/prohibited-pattern guard + Xcode 16.4 Simulator build **passed**;
- Push `33511327452`: **success**;
- PR `33511332786`: **success**;
- canonical Artifact `9801761448`;
- ZIP SHA-256 `0d6a5ddfa3c05d956708e43fb91acd6bb19988198a5a3cf34e6b72e289091db9`;
- package independently verified as Release `0.1.0 (80)`, Candidate b80, source marker `b0f51041c2d7`, Release, iOS14 minimum, arm64.

## Exact b80 Runtime classification

### Tool/timeline -> reasoning-divider spacing

**Accepted / Frozen for this Work.** User explicitly reports the result as normal and asks to freeze it. Do not alter this spacing without new explicit Runtime evidence/requirement.

### Adopted external final materialization

**Positive.** Supplied b80 diagnostics show adopted external responses remaining alive with `finalCharacters=0` through the waiting phase, then materializing a real final before Native terminal/reconcile (`5656` chars at `13:21:04Z`; another sequence `2874` chars at `13:28:45Z`). The b79 early-terminal race is therefore fixed for the adopted-response path.

This is page-snapshot materialization, not token/SSE-delta progressive final streaming.

### External stopped-thinking semantics

**Positive / preserve.** User confirms manually stopped external reasoning is presented correctly; reasoning/tools are not promoted into normal final body text.

### Manual-Sync re-arm

**Positive / preserve.** Explicit Sync can discover a changed latest remote turn, reload/re-arm the same covered target page once, and then adopt page-owned reasoning/tool snapshots when the page emits the required signal.

### Automatic cross-platform acquisition

**Rejected / intermittent.** User tested two conversations; one behaved normally, while another did not acquire even reasoning until explicit Sync.

Diagnostics localize the failure before Repository live adoption. In a representative sequence for `sha256:37824321c607`:

- selection observation page loaded at `13:27:04Z`;
- no external live response was adopted;
- explicit Sync at `13:27:19Z` discovered server-side change;
- `manual_sync_rearm` reloaded the target page;
- only then did `coveredExecutor.externalStreamingObserved` arrive at `13:27:31Z`, followed by reasoning/tool snapshots from `13:27:37Z` onward and final materialization at `13:28:45Z`.

Current `CoveredWebSendExecutor` bridge activates this path only after the **official page itself** produces a matching `stream_status == IS_STREAMING` response or a validated matching resume SSE. Native does not issue that target-status request. Therefore a selected page that does not emit the signal cannot start Repository live adoption.

No speculative Native polling/status construction, retry/timer/watchdog, duplicate Sync, fake progressive final, DOM/WebSocket body authority or second response owner is authorized.

## Account-wide signal evidence and current gate

User Runtime evidence already proves official Web can remain on conversation A while a never-opened B completes and still show an upper-right new-answer bubble; official iOS also provides account-wide completion haptics. This is now directly relevant to the acquisition defect because official completion awareness is not inherently tied to the target conversation page being selected.

Exact account-wide transport/schema/conversation identity/covered-WKWebView observability remain **Unknown / Unverified**.

## Next exact action — Human Web Rule Lab evidence gate

Before allocating or implementing b81:

1. Keep official Web Rule Lab on conversation A using the same `.default()` logged-in WebKit store.
2. Install a privacy-safe account-signal probe **before** B starts generating.
3. On another platform, start a sufficiently long response in conversation B that has not been opened in the Lab session.
4. Keep A visible; do not enter B and do not send from the Lab.
5. Capture the account-level event path while B starts/reasons/completes and the official Web notification behavior occurs.
6. Return only structural metadata: fetch/XHR paths/status/content-type; WebSocket/EventSource/service-worker/window/BroadcastChannel event type/key shape/length; no Cookie/Authorization/challenge/raw conversation IDs/message bodies/tool bodies.

Required conclusion from the probe:

- identify the exact account-level event source, if any, and whether it exposes a privacy-safe usable conversation identity or a bounded trigger for one authoritative list/detail refresh;
- only then decide the minimal b81 scope for reliable acquisition + optional completion haptic/automatic Sync.

Do **not** allocate b81 merely to guess the transport. If the probe remains ambiguous, stay at Human Gate.
