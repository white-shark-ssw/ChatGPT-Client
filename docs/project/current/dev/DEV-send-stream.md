# DEV-send-stream

## Status

**Active — exact b91 project route identity and official page-owned live continuation are Runtime Positive on iPhone/iOS17. Web -> bridge -> `ConversationRepository` progressive projection works without a second Sync. The remaining visible Web-page trap is the intentionally retained b90 `bringSubviewToFront` diagnostic, not a transport failure. Automatic terminal/final convergence remains Unverified because the app was force-quit while still streaming. Stable/Frozen Send remains No.**

- Work ID: `DEV-send-stream`
- Branch: `dev/send-stream-20260829`
- PR: #29 — open / unmerged
- Actual `main`: `94f0c5777dad262cd1fb22be49082dbd92c962f2`
- b89 Candidate: `DEV-send-stream-0.1.0-b89` permanently reserved; Runtime interactivity-sufficient Rejected
- b90 Candidate / Build: `DEV-send-stream-0.1.0-b90` / `0.1.0 (90)` permanently reserved
- Exact b90 product commit: `5e9d735ddb2f7a2c46dbc43de2525980c86a1c1e`
- Exact b90 product/config package source: `99f1aa15ce49b6abb0ff50e808bd889e381de917`
- b91 Candidate / Build: `DEV-send-stream-0.1.0-b91` / `0.1.0 (91)` permanently reserved
- Exact b91 product commit: `cdab4e091683dc179753ed114c9ab5993a6c2d24`
- Exact b91 product/config package source: `c5985f1e2e5daec7bbc0a011ed70a8dd80904f7c`
- b91 Push CI: `33746881658 / 100621278207` — success
- b91 PR CI: `33746886896 / 100621297087` — success
- b91 canonical Push Artifact: `9890000591`
- b91 IPA SHA-256: `abbd27370665fb97dd1ee5edd239c0a5fa1ea0694cbb329a81c32ee86867c140`
- Stable/Frozen Send: No

## b89 Runtime conclusion

Exact b89 on iPhone/iOS17 proved `isUserInteractionEnabled=true` and first-responder/document focus, yet emitted zero page-owned continuation while the same remote response later advanced only after explicit Sync from timeline `5 -> 28`, tools `4 -> 25`, reasoning `1 -> 3`. Therefore interactivity is rejected as a sufficient continuation condition. Manual authoritative Detail projection remains Runtime Positive.

## b90 Runtime progression

The earlier Native auth `NSURLErrorDomain -1005` sample was transient/inconclusive. Later exact b90 Runtime restored `/api/auth/session`, accounts-check and conversation-list HTTP200; manual Sync then raised the executor from `visibleSiblingCountAbove=1` to `0`, loaded a visible complete page, and achieved `nativeFirstResponder=true` / `documentHasFocus=true`. Therefore the b90 frontmost mechanism itself is Runtime Positive.

That sample still showed no bridge-reported matching `stream_status`, `/resume`, external streaming or project snapshot. This absence is no longer valid evidence against official project-Web continuation because a stronger bridge identity defect is now proven below.

## Project-scoped route-parser root cause — 2026-09-03

User Runtime observation: ordinary non-project conversations do not show the same continuation failure, while the current project conversation does; visible official Web itself appears healthy.

Current source directly explains this split:

- every existing conversation is initially loaded through `https://chatgpt.com/c/{conversationID}`;
- bridge `currentConversationID()` matches only `^/c/([^/?#]+)`;
- known official project canonical form is `/g/{scope}/c/{conversation}`;
- after canonicalization, the current bridge therefore returns `null` for a valid project conversation and classifies that page as `route=other`;
- the bridge uses that parsed `pageConversationID` as a required equality gate for page-owned `stream_status`, `/resume`, plural conversation snapshots, WebSocket exact-target matching and composer conversation identity;
- consequently, correct official project-Web requests can occur while the Native bridge silently treats them as non-target and emits none of the expected external continuation events.

The latest b90 log is consistent with this exact transition: immediately after direct `/c/{id}` reload page diagnostics report `route=conversation`, while later page activation events report `route=other` although the visible official Web remains healthy.

Qualification: **project scoped-route identity parsing is now the strongest evidenced blocker. The b90 no-event interval cannot decide z-order sufficiency for project conversations because the observer can become blind after project canonicalization.**

## b91 exact minimum A/B

Allocate b91 only for the bridge identity parser:

- preserve b90 transport, protected Send ownership, Repository ownership, observation protocol and diagnostic frontmost behavior for causal isolation;
- change `currentConversationID()` so it recognizes both ordinary `/c/{conversation}` and exact evidenced project scoped `/g/{scope}/c/{conversation}`;
- `pageRouteShape`, stream-status matching, resume matching, plural snapshot matching, WebSocket target matching and composer conversation identity then automatically consume the corrected identity through their existing shared helper;
- do not add new route guesses, retry/fallback/timer/watchdog/polling, Native status/resume synthesis, duplicate Send, WebSocket-body authority or second response store.

## b91 package / validation state

The exact minimum parser change was committed as `cdab4e091683dc179753ed114c9ab5993a6c2d24`. Guarded staging `33746622538 / 100620460993` passed ancestry, exact replacement, exact two-product-file scope and Simulator compile. Formal Push CI `33746881658 / 100621278207` and PR CI `33746886896 / 100621297087` both passed on exact package source `c5985f1e2e5daec7bbc0a011ed70a8dd80904f7c`.

Canonical Push Artifact `9890000591` has backend digest `sha256:6062b02f9f1332744816d01a58e13c1a8c82017ee50828051f014ef79b943350`. Independent unpacking verified IPA `ChatGPTClient-0.1.0-b91-dev-send-stream.ipa`, SHA `abbd27370665fb97dd1ee5edd239c0a5fa1ea0694cbb329a81c32ee86867c140` matching sidecar, built `0.1.0 (91)`, Candidate b91, source `c5985f1e2e5d`, MinimumOS 14.0, iPhone/iPad family `[1,2]` and arm64.

Evidence ladder: **Code written / guarded exact scope + Simulator passed / Push CI passed / PR CI passed / Artifact produced / package identity independently verified / Human Runtime pending / Stable-Frozen No.**

## b91 Human Runtime gate

After b91 package verification, run the same project-conversation test while a remote response is clearly active. Decisive evidence is no longer z-order itself; it is whether, after project canonicalization, the bridge continues to identify the target and reports the official page-owned path:

- page remains classified as conversation after scoped canonicalization;
- matching `coveredExecutor.externalStreamStatusRequest/Response` and/or `externalResumeRequest/Response` appears when official Web issues them;
- `externalStreamingObserved` / page-owned snapshot can advance the existing Repository external generation without another manual Sync.

If b91 makes project continuation observable/functional, route parsing is Runtime Positive; then a later separate candidate may remove the b90 frontmost diagnostic to prove the final covered production form. If b91 still has no page-owned requests while the project page is correctly recognized and the remote response demonstrably advances, continue from that new evidence without speculative protocol work.

## b91 Human Runtime result — 2026-09-03

Exact b91 Runtime is decisive for live continuation. Metadata matches Candidate b91 / Build 91 / source `c5985f1e2e5d`. After one explicit Sync established response generation 1, the official project page remained `route=conversation`, issued matching page-owned `stream_status`, repeatedly returned HTTP200 `IS_STREAMING`, emitted `externalStreamingObserved`, and continued after its own `/resume` offset 0 returned HTTP404 through the already-observed page-owned `stream_status` + plural conversation read path.

Native live state advanced automatically without another Sync: service messages/tools `6 / 2 -> 47 / 14`, reasoning characters `194 -> 909`, with repeated `externalSnapshot`, `liveResponse.externalSnapshot` and `liveResponse.presentationApplied`. Therefore the scoped-route parser and existing page-owned live continuation path are Runtime Positive.

The user could not return from the visible official Web because b91 intentionally retains b90's `hostView.bringSubviewToFront(webView)` diagnostic. That line changes z-order and has no balancing send-to-back in the rearm path; it is now a confirmed diagnostic presentation artifact.

The run does **not** validate automatic terminal/final convergence: the last pre-exit status was still `IS_STREAMING`, last snapshot had `finalCharacters=0`, then the app was force-quit/relaunched.

## Validation / identity state

b90 package remains exact and unchanged: canonical Artifact `9882770072`, exact package source `99f1aa15...`, IPA SHA `e75fac1a0c935ddb577fe2361c3fc5add0164d2f555a4fe5e8d7975f5b9fe3ee`.

b91 identity guard is clean at allocation: repository commit search found no b91 identity, branch search found no b91 branch collision, and actual `main` remains `94f0c5777dad262cd1fb22be49082dbd92c962f2`.

## Batch recovery state

**Closed for b91 Runtime evidence. Next exact action:** allocate the next unique candidate for one isolated presentation cleanup only: retain b91 scoped-route parsing and page-owned continuation, remove b90 `bringSubviewToFront(webView)` so the executor stays covered, then run project live + natural terminal/final Runtime. No retry/polling/timer/watchdog/Native status or resume synthesis.

## Preserved boundaries

Official page owns continuation transport; `ConversationRepository` owns Native response/content. No Native `stream_status`, `/resume`, guessed offset, polling/cadence reproduction, retry/watchdog, duplicate Send, WebSocket-body authority, hidden-thought presentation or second response store.

## Session round counter

This user turn is **round 59**.
