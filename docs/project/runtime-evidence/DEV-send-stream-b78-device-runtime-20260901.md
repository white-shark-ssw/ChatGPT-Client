# DEV-send-stream b78 device Runtime — 2026-09-01

## Candidate under test

- Work ID: `DEV-send-stream`
- Candidate: `DEV-send-stream-0.1.0-b78`
- Version / Build: `0.1.0 (78)`
- Exact product/config source: `031b1a1f2c1d01900c2ab79ff14b1f2fb6c7e809`
- Canonical Artifact: `9790836559`
- IPA SHA-256: `726e3c09bcac4eb8a40a8ecb79b8abb0f145d89e41481083bc51941a7978620e`
- Supplied diagnostics metadata reports `0.1.0`, Build `78`, Candidate `DEV-send-stream-0.1.0-b78`, source marker `031b1a1f2c1d`, Release, iPhone / iOS 17.0.

## User Runtime findings

### 1. Tool prominence/line-height change is positive, but transition spacing is still asymmetric

The user confirms b78's stronger tool-operation presentation is visibly active. The supplied screenshot shows the GitHub/tool row styling and larger operation rhythm taking effect.

A remaining detail is rejected: a row such as `读取并检查发送流文档` has visibly different space above and below. Current source explains the asymmetry. The inter-item newline is emitted using `separatorAttributes` inherited from the previous timeline item, so a reasoning -> tool transition uses the 25.2-point reasoning paragraph while a tool -> next-item transition uses the 36-point tool paragraph. The previous item therefore still owns the transition height even though `paragraphSpacingBefore` was removed.

Runtime result: **Partial positive / transition-spacing rejected.**

### 2. Cross-platform final body still has no progressive source; reasoning is only page-snapshot granular

The covered external run beginning around 08:01:13Z proves the page-owned read path is active:

- external response starts and `/resume` returns HTTP404 JSON;
- the official page continues through its own read path;
- Native receives changing external snapshots while reasoning/tools are active.

Reasoning progresses only at the cadence of page-owned snapshots, not SSE/token-delta granularity. In the captured run, reasoning characters move from `131` to `260` while tool count progresses from `2` to `8`; updates arrive in coarse page snapshots, so the UI can visibly look chunked or near-one-shot rather than token-streamed.

The final body remains decisively non-progressive on the current source. After phase changes to `final`, repeated snapshots remain `finalCharacters=0` through 08:02:33Z; at 08:02:39Z the next snapshot jumps directly to `finalCharacters=7006` and terminal occurs at the same timestamp. Another b78 run reproduces the same zero-to-full jump.

Runtime result: **Reasoning/tool page-snapshot adoption positive but coarse; progressive final body rejected/unavailable from the currently authorized source.** No fake typewriter, Native polling/cadence, DOM-body authority or WebSocket-body authority is justified.

### 3. Already-open conversation misses a newly started external response until the covered page is re-entered/reloaded

The user reports this exact sequence: Native is already displaying a conversation; another platform sends a new user turn; explicit `同步最新消息` can reveal that new user message, but Native does not begin the external thinking stream. A later Sync after server completion reveals the completed response.

Diagnostics localize this to the covered-page observation lifecycle, not the Detail parser:

- after one external response terminates, a covered executor is recreated for the same selected conversation and its page remains loaded;
- while the user stays in that same Native conversation, later manual Detail Sync operations add/update authoritative messages, but no `coveredExecutor.externalStreamingObserved` / external-snapshot lifecycle starts for the newly created remote turn;
- after a fresh page load/re-entry, external streaming observation resumes and reasoning/tool snapshots are received again.

Current source matches the evidence: calling `observeExistingConversation` for an already-current conversation only runs `probeComposer(true)` and does not reload/re-enter the page. Therefore the already-loaded official page is not induced to issue its current `stream_status` / plural conversation reads for the newly-started remote turn.

Runtime result: **Rejected; root cause localized.** An explicit user Sync may evidence a new latest user turn and can then perform one event-driven re-arm/reload of the same covered page. This does not authorize a timer/poll loop.

### 4. Externally stopped thinking is incorrectly promoted into final answer text

The user manually stopped an externally-started response during thinking. Official ChatGPT presents that turn as `已停止思考` with the thinking disclosure retained. Native instead shows the thinking text as normal answer-body text.

Diagnostics prove the exact Native transition. Immediately before terminal:

- phase = `reasoning`;
- `reasoningCharacters=263`;
- `finalCharacters=0`;
- four tool items are present.

At terminal in the same timestamp:

- `reasoningCharacters` becomes `0`;
- `finalCharacters` becomes `265`;
- the phase becomes `completed`.

Current `consumeLiveResponseEvent(.terminal)` contains a fallback that, whenever `reasoningEnded == false` and `finalText` is empty, concatenates reasoning timeline text into `finalText` and removes reasoning items. That fallback is valid only for the previously evidenced local protected-Send compatibility path; for an `external_page_owned` response (`promptText` empty), this exact run proves it is wrong.

Runtime result: **Rejected; root cause identified.** External terminal-without-real-final must preserve reasoning rather than synthesize a final body. The local b67 protected-Send fallback must remain unchanged.

### 5. b78 user-message integrity and relaunch Detail lifecycle

The supplied b78 screenshots no longer reproduce the b77 mid-text clipping defect: the long user bubble is shown through to its final line and the link is styled. This is a **positive focused observation for clipping**, not a complete official-rendering parity acceptance.

The old permanent `detail.coalesced` zombie is also not reproduced in the supplied b78 run; multiple Detail operations reach terminal HTTP200 results. However the exact b77 route-403 + concurrent Detail cancellation condition was not clearly reproduced in this evidence, so the secure-session retirement fix remains **not negatively contradicted, but not fully re-qualified under the same 403 condition**.

## Automatic Sync question — architecture answer only

Automatic Sync is technically possible, but no implementation is authorized by this Runtime evidence yet. A blind fixed-period timer/poll/watchdog would violate the current evidence-minimal architecture and add unnecessary traffic.

Preferred future direction is event-driven: use an already-proven page-owned/lifecycle signal to trigger one bounded authoritative Sync. The current b78 evidence shows that an already-loaded covered conversation page does not emit the needed new-turn signal when the turn starts elsewhere, so truly automatic instant Sync needs additional protocol evidence before implementation. For the immediate defect, explicit manual Sync can re-arm the covered page once when it discovers a new latest user turn; that is not automatic polling.

## Evidence-backed next candidate boundary

Allowed minimum next-candidate scope:

1. Give reasoning/tool transitions one deterministic neutral inter-item spacing source instead of inheriting the previous item's line height.
2. After an explicit successful manual `同步最新消息` detects a new latest user turn and there is no current Native live response, re-arm/reload the existing covered official page once for that conversation so page-owned external-response discovery can run again.
3. For external-page-owned terminal with no real final body, preserve reasoning/tool presentation; do not promote reasoning text into final. Retain the local protected-Send terminal fallback.
4. Do not claim or fake progressive final streaming. Do not add automatic Sync, timer, retry, watchdog, polling, duplicate Send, second state owner, DOM body or WebSocket-body authority.

## Evidence classification

- b78 Code/static/Simulator/Push+PR CI/Artifact/package: previously verified.
- b78 Runtime/manual/real-device: **Partial / rejected**.
- Tool prominence: **Positive**.
- Tool transition spacing symmetry: **Rejected**.
- User-message clipping: **Positive for the supplied long-message case; broader parity not fully accepted**.
- Cross-platform reasoning/tool adoption: **Positive at page-snapshot granularity; not token-streaming**.
- Cross-platform progressive final body: **Rejected / no authorized progressive source**.
- Already-open new external turn discovery: **Rejected; root cause localized to covered-page re-arm**.
- External manual-stop phase semantics: **Rejected; root cause identified in terminal fallback**.
- Stable/Frozen Send: **No**.
