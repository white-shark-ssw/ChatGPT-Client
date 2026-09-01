# DEV-send-stream

## Status

**Active — b81 automatic external acquisition is Runtime-rejected, while its at-document-start WebSocket structural probe is Runtime-positive and supplies an evidence-backed one-shot acquisition trigger. `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)` is now allocated to convert that exact target-conversation event into one bounded authoritative Sync + one covered-page re-arm. Account-wide notification remains deferred. b80 spacing and external stopped-thinking semantics remain Frozen. Stable/Frozen Send as a whole remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / mergeable / unmerged at allocation guard
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- Exact b81 product/config source: `d1d4d197cc5d2a5022a28b332afebe485b216ea1`
- b81 Candidate / Version-Build: `DEV-send-stream-0.1.0-b81` / `0.1.0 (81)`
- b81 canonical Artifact: `9809150111`
- b81 IPA SHA-256: `d48d2398dc5a7ef16b9983021a9173d87ba3b852f4a45c9431dff2ebcf057038`
- Allocated b82 Candidate / Version-Build: `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`
- b39-b82 permanently reserved
- b81 Runtime: **Automatic acquisition rejected / structural trigger positive**
- b82 Runtime: **Not yet produced**
- Stable/Frozen Send: **No**

Durable b81 Runtime evidence: `docs/project/runtime-evidence/DEV-send-stream-b81-device-runtime-20260901.md`.

## b82 allocation guard

Immediately before allocation:

- formal feature head was `68bb0688878c1135399bdc21ceacbfd7f150250e` before the b81 Runtime evidence write;
- PR #29 remained open / mergeable / unmerged, head `dev/send-stream-20260829`, base `main`;
- actual `main` remained `94f0c5777dad262cd1fb22be49082dbd92c962f2`;
- exact repository search returned no `DEV-send-stream-0.1.0-b82`;
- `docs/project/current/dev/` contained only this Active checkpoint plus README;
- no parallel Active candidate/state-owner conflict was found.

Therefore b82 is allocated exactly once here. Do not allocate b83 before b82 Runtime classification.

## Exact b81 Runtime finding

The supplied exact b81 diagnostics prove:

1. selected conversation observation begins at 16:19:14Z and the covered page is loaded by 16:19:15Z;
2. `wss://ws.chatgpt.com/p24/ws/user/{id}` is observed from creation/open at 16:19:18-19Z;
3. while the client shows no external live response and the user does not press Sync, the socket produces a JSON-array frame at **16:22:20Z** with `targetMatch=true` and a second at **16:24:24Z** with `targetMatch=true`;
4. before manual Sync there is no `externalStreamingObserved`, no `externalSnapshot`, and no Repository external live-response start;
5. manual Sync at 16:24:59Z returns authoritative Detail at 16:25:00Z with visible messages **4 -> 8**, four added visible messages, then the existing manual path performs `manual_sync_rearm`.

In b81, `targetMatch=true` means the parsed frame contains an exact string equal to the current page conversation ID in the bounded privacy-safe structural traversal. Raw frame/body/ID content is not exported.

Conclusion: a target-conversation-correlated user-level WebSocket event reaches the covered page **before and independently of** the currently unreliable page-owned `stream_status` acquisition path. The event is sufficient as a discovery trigger; it remains non-authoritative for response content.

## Frozen / preserved boundaries

- b80 final tool/timeline -> reasoning-divider spacing: **Frozen**;
- external stopped-thinking semantics: **Frozen**;
- b80 external final-materialization gate: preserve;
- explicit manual-Sync re-arm: preserve as recovery;
- b67 client-owned protected Send Runtime and b72 tested simultaneous A/B ownership: preserve;
- `ConversationRepository` remains sole production conversation/response owner;
- covered official Web remains transport/observation only;
- account-wide notification/haptic discovery remains deferred;
- progressive external final token streaming remains an evidence gap and must not be faked.

## Exact b82 product scope

Authorized product/config changes only:

1. `ChatGPTClient/RootViewController.swift`
   - introduce a dedicated external-acquisition-hint event from the existing b81 structural WebSocket path only when a `message` frame has `targetMatch=true`, the executor is observing the current conversation, and no response has yet been acquired;
   - consume **only the first** such hint in one observation cycle;
   - on that hint, trigger exactly one `ConversationRepository.syncLatestMessages(id:)` for the selected conversation;
   - after that one authoritative Sync completes, update the selected detail presentation if still selected and perform exactly one covered-page re-arm/reload for the same conversation;
   - after re-arm, existing page-owned `stream_status / plural-read` remains the only external reasoning/tool/final content source;
   - add privacy-safe diagnostics for hint received, Sync result, and re-arm.
2. `ChatGPTClient.xcodeproj/project.pbxproj`
   - Build 82 / Candidate b82 identity only.
3. `.github/workflows/ios-foundation.yml`
   - b82 Artifact identity only.

Explicitly excluded:

- timer/polling/cadence;
- retries/watchdogs/repeated automatic Sync loops;
- WebSocket frame/body content authority;
- Native construction of `stream_status`, resume or plural response bodies;
- fake typewriter/progressive final;
- duplicate Send/resend;
- second response owner;
- account-wide notification/haptic implementation;
- changes to Frozen spacing/stopped-thinking behavior.

## b82 design guard

The one-shot hint state belongs to the covered executor observation cycle, not Repository response state. It prevents the second target-matching frame seen in b81 from causing duplicate automatic Sync. An explicit new observation cycle / newly-created executor may arm one new hint for a later response.

If the one automatic authoritative Sync fails, b82 must record the failure and stop; no automatic retry is authorized. Existing explicit manual Sync remains the recovery path.

## b82 Runtime gate

1. Open conversation A in b82 and leave it selected until covered page load.
2. Start a sufficiently long new turn in the same A from another platform.
3. Do not press Sync.
4. Expected: first target-matching socket event triggers one automatic authoritative Sync and one covered-page re-arm; Native then begins adopting page-owned reasoning/tools without user Sync.
5. Repeat at least twice to check one-shot behavior and no duplicate Sync.
6. After completion export Diagnostics regardless of success.
7. Also confirm b80 Frozen spacing and external stopped-thinking semantics did not regress if naturally exercised.

Progressive external final token streaming is **not** claimed solved by b82; the current authorized final source may still materialize in coarse/final snapshots.

## Evidence classification

- b81 Code/static/Simulator/Push+PR CI/Artifact/package: **Verified**
- b81 Runtime automatic acquisition: **Rejected**
- b81 WebSocket structural trigger evidence: **Positive**
- b82 allocation: **Done**
- b82 Code/static/CI/Artifact/Runtime: **Pending**
- Stable/Frozen Send as a whole: **No**

## Session round counter

Current work is round 19. Continue displaying the current round count at the end of each user-facing response.

## Next exact action

Create an isolated b82 tooling branch from the current formal docs head, apply only the three-file one-shot event-driven acquisition change, validate exact scope / prohibited patterns / `git diff --check` / Xcode 16.4 Simulator, then transplant the validated three product/config blobs to the formal feature branch and continue through Push+PR CI, canonical Artifact, independent package verification, checkpoint/PR update, and exact IPA handoff.

Do not claim CI/Artifact as Runtime success.
