# DEV-send-stream

## Status

**Active — exact b90 auth/list prerequisite has recovered. The b90 frontmost mechanism itself is now real-device Runtime Positive, while frontmost/occlusion sufficiency for automatic cross-platform continuation remains Inconclusive. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b89 Candidate: `DEV-send-stream-0.1.0-b89` permanently reserved; Runtime interactivity-sufficient Rejected
- b90 Candidate / Build: `DEV-send-stream-0.1.0-b90` / `0.1.0 (90)` permanently reserved
- Exact b90 product commit: `5e9d735ddb2f7a2c46dbc43de2525980c86a1c1e`
- Exact b90 product/config package source: `99f1aa15ce49b6abb0ff50e808bd889e381de917`
- Canonical Push Artifact: `9882770072`
- IPA SHA-256: `e75fac1a0c935ddb577fe2361c3fc5add0164d2f555a4fe5e8d7975f5b9fe3ee`
- Stable/Frozen Send: No

## b89 Runtime conclusion

Exact b89 on iPhone/iOS17 proved `isUserInteractionEnabled=true` and first-responder/document focus, yet emitted zero page-owned continuation while the same remote response later advanced only after explicit Sync from timeline `5 -> 28`, tools `4 -> 25`, reasoning `1 -> 3`. Therefore interactivity is rejected as a sufficient continuation condition. Manual authoritative Detail projection remains Runtime Positive.

## b90 exact single-variable A/B

Relative to b89, only explicit manual-Sync rearm changes z-order: before loading the same target, the existing executor `WKWebView` is brought to the front of its current Root host and logs `stage=manual_sync_frontmost_ab`. Existing interactivity=true, first-responder focus, target load, page-owned status/resume/snapshot observation, protected Send path and Repository ownership are unchanged.

## b90 Runtime progression — 2026-09-03

### Earlier prerequisite-blocked sample

An earlier exact b90 sample repeatedly failed Native `/api/auth/session` with `NSURLErrorDomain -1005`, so the frontmost A/B was not reached. That sample remains valid as an Inconclusive prerequisite-blocked observation, not a b90 product regression.

### Latest sample — auth recovered / frontmost mechanism Positive / continuation Inconclusive

Exact diagnostics remain `DEV-send-stream-0.1.0-b90`, Build90, source marker `99f1aa15ce49`, iPhone/iOS17.

Auth/list recovery is directly proven:

- `08:16:00Z` `/api/auth/session` HTTP200; accounts-check HTTP200/verified by `08:16:02Z`;
- `08:16:03Z` real conversation-list response HTTP200, `28` page items / authoritative total `29`;
- the same success repeated at `08:21:21Z` / `08:21:23Z`.

The manual Sync at `08:16:47Z` returned authoritative active Detail at `08:16:55Z` with visible messages `20 -> 21`, trailing timeline `2 = reasoning 1 + tool 1`; Repository external response generation 1 started from that authoritative Detail.

The b90 mechanism then executed exactly as designed:

- before raise: `subviewIndex=0`, `visibleSiblingCountAbove=1`;
- `stage=manual_sync_frontmost_ab`: `subviewIndex=1`, `visibleSiblingCountAbove=0`, non-empty/intersecting key-window bounds, interaction enabled;
- page load completed while route=`conversation`, `visibilityState=visible`;
- `08:16:57Z` focus result: `nativeFirstResponder=true`, `documentHasFocus=true`.

Therefore **frontmost presentation itself is Runtime Positive**.

However the same log contains zero matching `externalStreamStatusRequest/Response`, zero matching `externalResumeRequest/Response`, zero `externalStreamingObserved`, and zero page-owned external snapshot after the frontmost activation. ChatGPTClient left foreground at `08:17:10Z`, only ~13 seconds after focus succeeded, and there is no later explicit Detail Sync proving how far the same remote generation advanced after activation. The user's observation that the visible Web looked normal is consistent with Web presentation/interaction viability, but does not by itself prove page-owned continuation or Native automatic convergence.

Qualification: **b90 frontmost mechanism Runtime Positive; frontmost/occlusion sufficiency for automatic continuation remains Inconclusive. Reuse exact b90; do not allocate b91 or change product code.**

## Validation / package identity

Corrected staging `33727956426 / 100561161422`, Push CI `33728071476 / 100561518990`, and PR CI `33728075476 / 100561530874` passed. Canonical Push Artifact is `9882770072`; exact package source remains `99f1aa15...`; later docs-only heads do not redefine the Runtime package.

Evidence ladder: **Code written / guarded scope+Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / auth prerequisite recovered / frontmost mechanism Runtime Positive / automatic-continuation causality Inconclusive / Stable-Frozen No.**

## Human Runtime gate — next exact action

**Reuse exact b90. Do not allocate b91.** Run one clean long-response continuation A/B:

1. start a deliberately long response on another official client with multiple reasoning/tool steps still ahead;
2. select the same target conversation in exact b90 while that remote generation is clearly still active;
3. press `同步最新消息` exactly once;
4. after the frontmost Web appears, keep ChatGPTClient continuously foregrounded for at least 30–60 seconds without another Sync;
5. during that same interval independently verify the remote official client continues generating after frontmost activation;
6. export diagnostics before any second manual Sync if possible; if Native still has not advanced, then perform one second Sync only after the first export so the remote advancement can be proven from authoritative Detail.

Decision:

- frontmost established + genuine page-owned continuation while remote generation remains active -> frontmost/occlusion differential Runtime Positive for continuation;
- frontmost established + remote generation demonstrably advances but still zero page-owned continuation -> reject z-order/occlusion as sufficient;
- remote response terminal too early or foreground interval is interrupted before sufficient evidence -> Inconclusive; reuse exact b90.

## Batch recovery state

**Open — latest b90 frontmost Runtime documentation batch.** Baseline branch head before this batch: `8fc802e85888b81a8e5eed26aded398400832d2d`. Intended writes: (1) this selected checkpoint, (2) one new runtime-evidence file for the recovered-auth/frontmost-positive continuation-inconclusive sample, (3) final checkpoint closure. No product/config/version/Candidate/Artifact/PR identity may be changed by this batch. Next exact action if interrupted: create the runtime-evidence file only if absent, then close this batch in this checkpoint.

## Preserved boundaries

Official page owns continuation transport; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling/cadence reproduction, retry/watchdog, duplicate Send, WebSocket-body authority, hidden-thought presentation or second response store.

## Session round counter

This user turn is **round 58**.
