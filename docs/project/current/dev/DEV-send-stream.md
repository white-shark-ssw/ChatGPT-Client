# DEV-send-stream

## Status

**Active — exact b89 Runtime decisively rejects covered-Web interactivity as sufficient. Exact b90 frontmost-presentation A/B is now Code/guarded scope+Simulator/Push+PR CI/Artifact/package verified and ready for Human Runtime. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b89 Candidate: `DEV-send-stream-0.1.0-b89` permanently reserved; Runtime interactivity-sufficient Rejected
- b90 Candidate / Build: `DEV-send-stream-0.1.0-b90` / `0.1.0 (90)` permanently reserved
- Exact b90 product commit: `5e9d735ddb2f7a2c46dbc43de2525980c86a1c1e`
- Exact b90 product/config package source: `99f1aa15ce49b6abb0ff50e808bd889e381de917`
- Corrected b90 staging: `33727956426 / 100561161422` — success
- Push CI: `33728071476 / 100561518990` — success
- PR CI: `33728075476 / 100561530874` — success
- Canonical Push Artifact: `9882770072`
- Canonical Artifact ZIP: `sha256:363c6fdbade5d476eacdee064eec26ed3480c0e7ba1da3b5dcf6b8537af46f6e`
- IPA: `ChatGPTClient-0.1.0-b90-dev-send-stream.ipa`
- IPA SHA-256: `e75fac1a0c935ddb577fe2361c3fc5add0164d2f555a4fe5e8d7975f5b9fe3ee`
- Stable/Frozen Send: No

## b89 Runtime conclusion

Exact b89 on iPhone/iOS17 proved `isUserInteractionEnabled=true` and first-responder/document focus, yet emitted zero page-owned continuation while the same remote response later advanced only after explicit Sync from timeline `5 -> 28`, tools `4 -> 25`, reasoning `1 -> 3`. Therefore interactivity is rejected as a sufficient continuation condition. Manual authoritative Detail projection remains Runtime Positive. Durable evidence: `docs/project/runtime-evidence/DEV-send-stream-b89-interactivity-sufficient-rejected-20260903.md`.

## b90 exact single-variable A/B

Relative to b89, only explicit manual-Sync rearm changes z-order: before loading the same target, the existing executor WKWebView is brought to the front of its current Root host and logs `stage=manual_sync_frontmost_ab`. Existing interactivity=true, first-responder focus, target load, page-owned status/resume/snapshot observation, protected Send path and Repository ownership are unchanged. This is a diagnostic causal A/B, not acceptance of full official-Web daily-chat rendering.

## Validation / package identity

The first staging attempt `33727587238 / 100560009446` passed patch/scope/Simulator but failed before any remote product commit only because the Actions token lacked workflow-file modification permission. The corrected product-only staging `33727956426 / 100561161422` passed guard, exact patch, exact two-product-file scope audit, Xcode Simulator compile, commit and push, producing product commit `5e9d735...`.

Permanent workflow identity commit `99f1aa15...` is the exact package source. Push and PR CI both passed. Canonical Push Artifact `9882770072` was independently downloaded and inspected: ZIP digest matches backend, IPA sidecar and recomputed SHA agree, built Info.plist is `0.1.0 (90)` / Candidate b90 / source `99f1aa15ce49` / minimum iOS14, and executable is arm64.

Evidence ladder: **Code written / guarded scope+Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Runtime pending / Stable-Frozen No.**

## Human Runtime gate — next exact action

Install exact b90 IPA and run one clean early/mid-generation production A/B:

1. start a deliberately long response on another official client with multiple reasoning/tool steps still ahead;
2. select the same target conversation in b90 while that remote generation is clearly still active;
3. press `同步最新消息` exactly once;
4. b90 intentionally brings the official executor WebView frontmost for this diagnostic A/B; keep ChatGPTClient foregrounded for 30–60 seconds without another Sync;
5. independently confirm the other official client continues generating after frontmost activation;
6. export diagnostics before doing a second manual Sync if possible.

Decisive fields/events:

- `coveredExecutor.webViewActivation` with `stage=manual_sync_frontmost_ab`, especially `visibleSiblingCountAbove=0`;
- `coveredExecutor.focusActivationResult`;
- any matching `coveredExecutor.externalStreamStatusRequest/Response`;
- any matching `coveredExecutor.externalResumeRequest/Response`;
- any `coveredExecutor.externalStreamingObserved` or page-owned snapshot;
- Repository live-response progression without a second Sync.

Decision:

- frontmost established + genuine page-owned continuation while remote generation remains active -> frontmost/occlusion differential Runtime Positive; retain only the minimum necessary consequence and separately redesign the final covered form without making full Web the daily-chat UI;
- frontmost established + remote generation demonstrably advances but still zero page-owned continuation -> reject z-order/occlusion as sufficient and continue to the next evidenced WKWebView browsing-context differential;
- remote response terminal before frontmost activation -> Inconclusive; reuse exact b90, do not allocate b91.

## Batch recovery state

**Closed for b90 product/package/docs preparation. The next gate is human-only real-device Runtime.**

No product/config change is permitted before b90 Runtime evidence. b89 and b90 identities remain permanently reserved. Any later docs-only head advancement does not redefine exact b90 package source `99f1aa15...`.

## Preserved boundaries

Official page owns continuation transport; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling/cadence reproduction, retry/watchdog, duplicate Send, WebSocket-body authority, hidden-thought presentation or second response store.

## Session round counter

This user turn is **round 56**.
