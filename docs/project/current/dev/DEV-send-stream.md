# DEV-send-stream

## Status

**Active — b80 Runtime is partial-positive / partial-rejected. The b80 spacing boundary is accepted and Frozen for this Work; adopted external final materialization and stopped-thinking semantics are Runtime positive. Reliable automatic acquisition of a newly-started cross-platform response remains rejected/intermittent. The latest account-signal probe is inconclusive, but the official account-wide signal is no longer a prerequisite for completion notification of responses initiated and owned by this client. No b81 is allocated. Stable/Frozen Send as a whole remains No.**

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
- `docs/project/runtime-evidence/DEV-send-stream-account-signal-probe-20260901.md`
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

**Positive / Frozen semantic boundary for this Work.** User confirms manually stopped external reasoning is presented correctly; reasoning/tools are not promoted into normal final body text. Do not alter this semantic boundary without new explicit Runtime evidence/requirement.

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

## Account-wide signal probe classification

The latest privacy-safe Web Rule Lab capture is **inconclusive** for the official account-wide completion/new-answer transport. It contains ordinary page/Sentinel/telemetry traffic and an explicit current-page protected Send, but no clear cross-conversation WebSocket/EventSource/BroadcastChannel/service-worker/window event attributable to a different conversation completing.

Do not infer a transport/schema from this capture and do not continue probing it merely to implement completion notification for this client's own Sends.

## Notification ownership clarification

Completion notification for a response **initiated by this client** does not require the official account-wide signal.

The existing architecture already provides the needed authority:

- every client-owned Send creates/uses the normal `ConversationRepository` response lifecycle for a known conversation;
- multiple owned responses are a set of independently owned response lifecycles, not one global streaming flag;
- a completion notification can be emitted from that response's authoritative terminal transition, with at-most-once deduplication;
- the official account-wide signal is only relevant to activity the client did **not** start and has not yet adopted.

This matches `BACKGROUND_EXECUTION_PLAN.md`; no new notification state owner, polling route or guessed account transport is needed.

## Next exact action — scope decision, not another notification probe

Do **not** allocate b81 solely to chase the account-wide notification transport.

The remaining open b80 issue is specifically **externally initiated cross-platform response auto-acquisition**. Before any further Send product change, classify whether that behavior remains a required blocker for `DEV-send-stream` or is deferred as a separate cross-platform parity enhancement:

1. if it remains required, gather evidence for a deterministic externally-started acquisition source and make only the minimal evidence-backed b81 change;
2. if it is deferred, preserve explicit Sync/manual re-arm as the recovery path and do not let the unresolved official account-wide transport block client-owned Send completion notification/background work.

For future `DEV-background-notify`, use the Repository-owned active-response set and terminal transitions defined in `BACKGROUND_EXECUTION_PLAN.md`; the official account-wide signal is not a prerequisite for client-owned Sends.

## Frozen sub-boundaries for this Work

The following are now frozen unless the user supplies new explicit Runtime evidence requiring change:

- final tool/timeline -> reasoning-divider spacing accepted in b80;
- stopped external reasoning/tools remain reasoning/tools and are not promoted into final body text.

Do not interpret these sub-boundary freezes as `DEV-send-stream` Stable/Frozen as a whole.

## Session round counter

This checkpoint update occurs during round 16. Continue displaying the current round count at the end of each user-facing response in this conversation.

## Write-chain note

Earlier attempted updates to older durable evidence files were rejected by GitHub with SHA mismatch and were not replayed blindly. A later accidental attempt to create a duplicate PR was rejected by GitHub because PR #29 already exists; it made no repository change. No product/config state changed during the account-signal clarification.

Current feature branch has advanced only through documentation commits after the exact b80 product source; product/config source identity remains `b0f51041c2d7b645f152752ea6196526b2e4e0f6`. The next product write is gated by the externally-started acquisition scope/evidence decision, not by client-owned completion notification transport discovery.
