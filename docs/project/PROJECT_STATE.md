# Project State

## DEV-send-stream b89 package-ready override — 2026-09-03

Exact b89 `DEV-send-stream-0.1.0-b89` / `0.1.0 (89)` is now the Human Runtime candidate. Product commit `f39bc9387575028d431b85409780a2f3670b3259`; exact package source `fe45aeadf7ae03bf09aff66a8a05aa2542959676`; guarded staging `33722656297 / 100544857329` passed; Push `33725042383 / 100552047445` and PR `33725044367 / 100552051932` passed. Canonical Push Artifact `9881665748`, ZIP `sha256:2e383a6328f801dd754d6858c3b9a8b71be5d5765a9a612d497b18c91b73988f`, IPA `sha256:c8ad5dcebbfde2131d3fc73c0309a47745f71527ad38b44c5fe3c5fbffe21a55`; package independently verified as Release 0.1.0 (89), Candidate b89, source `fe45aeadf7ae`, iOS14, arm64. b89 tests only covered-Web interactivity plus automatic user-activation diagnostics; real-device continuation causality is Pending and Stable/Frozen remains No.
## DEV-send-stream b82 Runtime override — 2026-09-02

Exact b82 `DEV-send-stream-0.1.0-b82` / `0.1.0 (82)`, product/config source `c7a274786dfd175e8f476fc15c4964840e112a1d`, Artifact `9811406038`, IPA SHA `3ca1686783199a5c7224ce388c0dbbad490266e62c820f2408d14f5a59bdd6d2` is Runtime **Partial**. Automatic final acquisition now works without manual Sync, but the observed current-conversation WebSocket trigger arrived only when authoritative Detail already changed 8 -> 10 (+2 visible messages) and the user reports the remote user message plus assistant answer appeared only after the answer had fully generated. No earlier WebSocket message, `externalStreamingObserved`, external snapshot or Repository external live response was captured. Therefore b82 is a completion/update acquisition path, not live request-start acquisition. b83 is not allocated. The next gate is an already-open visible official-Web comparison before choosing any new discovery mechanism.

## DEV-send-stream b79 candidate override — 2026-09-01

Exact b79 `DEV-send-stream-0.1.0-b79` / `0.1.0 (79)` is now the latest test candidate. Formal exact product/config source is `a3d307b05d70e95568672bc29b0c939b7f3b8141`. The guarded staging path `33488975445 / 99795672696` passed exact scope, `git diff --check` and Xcode 16.4 Simulator build before the validated product blobs were transplanted. Formal Push `33489654106 / 99797864816` and PR `33489658656 / 99797878467` both passed. Canonical Push Artifact `9793240789` has ZIP `sha256:2016508002ae7ff43d803c90fcbb92ba01c45906c885be6f6e50a1e43e1e87fc` and IPA `sha256:39f64dd9146c3a8dc28cb9b733d1c56d4fbf3ff090a442c8ecbd27c672234fb4`; independent unpacking confirms Release 0.1.0 (79), Candidate b79, source marker `a3d307b05d70`, MinimumOSVersion 14.0 and Mach-O arm64.

- b79 gives reasoning/tool transitions one neutral 12-point separator instead of inheriting the preceding item paragraph style.
- After explicit manual Sync, a changed latest user turn may force one same-conversation covered-page reload/re-arm when no live response is active; there is still no timer/poll/watchdog or automatic Sync implementation.
- An external page-owned terminal without a real final body no longer promotes reasoning into final; the local protected-Send compatibility fallback remains limited to local responses. Stopped external reasoning is presented as `已停止思考`.
- b78 remains the Runtime evidence predecessor: external reasoning/tool observation is only page-snapshot granular and external progressive final still has no authorized source. b79 does not fake final streaming.
- Runtime/manual/real-device b79: **Pending / Unverified**. Stable/Frozen Send: **No**. b39-b79 are permanently reserved.

## DEV-send-stream b78 candidate override — 2026-09-01

Exact b78 `DEV-send-stream-0.1.0-b78` / `0.1.0 (78)` is the current real-device candidate. Clean product commit `180065e0faf947292a9f21b56c4ea366a5c322fe` changes only `ChatGPTClient/Conversation/ConversationFeature.swift` and `ChatGPTClient.xcodeproj/project.pbxproj`; workflow-only child `031b1a1f2c1d01900c2ab79ff14b1f2fb6c7e809` is the exact product/config source. Final tooling validation `33482721335 / 99775722851` passed exact scope, `git diff --check`, and Xcode 16.4 Simulator build. Formal Push CI `33482983693 / 99776545604` and PR CI `33482987997 / 99776557269` passed. Canonical Push Artifact `9790836559` has ZIP `sha256:7b5900a960ef680cce34642ca6cef232f201a260b182d6b640266e81982b081f` and IPA `sha256:726e3c09bcac4eb8a40a8ecb79b8abb0f145d89e41481083bc51941a7978620e`; independent package inspection confirms Release 0.1.0 (78), Candidate b78, source marker `031b1a1f2c1d`, MinimumOSVersion 14.0, Mach-O arm64.

- b77 device Runtime is partial/rejected: inline tool rows still lacked correct deterministic/prominent presentation; Native user messages could show raw inline Markdown and truncate because rendering and measurement diverged; a route-level list HTTP403 invalidated-and-cancelled the shared transient session, cancelling the selected Detail, whose cancellation path failed to terminalize the current operation and caused permanent coalescing/`正在读取会话…`.
- b78 uses one attributed representation for user rendering and measurement, explicit character wrapping and inline-only Markdown on supported OS versions; it records privacy-safe latest-user character count for integrity evidence.
- b78 retires a 401/403-invalidated transient session with `finishTasksAndInvalidate()` so already-running Detail tasks are not cancelled; any current Detail cancellation is terminalized instead of leaving a zombie operation. No retry/timer/watchdog/polling/fallback was added.
- b78 tool rows are a distinct medium-weight/label-color presentation whose icon/text/separator paragraph geometry is owned by the tool paragraph style instead of mixed reasoning/tool spacing. Runtime visual acceptance remains required.
- b77's structure-only DOM evidence remains negative for an earlier progressive final-body source; b78 does not promote DOM text/WebSocket bodies or fake final streaming.
- Runtime/manual/real-device b78: **Pending / Unverified**. Stable/Frozen Send: **No**. b39-b78 are permanently reserved.

## DEV-send-stream b76 candidate override — 2026-09-01

Exact b76 `DEV-send-stream-0.1.0-b76` / `0.1.0 (76)` is the current test candidate. Exact product/config source `0da5a7577f2cf3b2a6882d8a0ec920b5c8f37c71` passed guarded exact-scope assembly plus Xcode 16.4 Simulator build, formal Push CI `33440101178 / 99645927061` and PR CI `33440098527 / 99645917529`. Canonical Push Artifact `9775920927` has ZIP `sha256:52f94ed7dbfbe311e37656fcce9a60bb5f8cc9c6b2af29434f7020d47729e944` and IPA `sha256:b130c9059ec85d08d95105b32b71157a4be2b2ecea25112963f0a548ec252bcd`. Independent package inspection confirms Release 0.1.0 (76), Candidate b76, source marker `0da5a7577f2c`, MinimumOSVersion 14.0, arm64, iPhone+iPad family.

- Current visible official Web can receive matching page-owned `/resume` HTTP404 JSON and then follow the active response through its own already-issued `stream_status` + plural `/backend-api/conversations/{conversation}` reads.
- The plural rolling `messages[]` window exposes the required service-message family during `IS_STREAMING` and the finished final message after `COMPLETE`; raw message count is not a cursor.
- b76 observes only those page-owned responses, validates target identity, derives entries after the latest user, and atomically projects them into the existing `ConversationRepository` live-response owner. It adds no Native polling/cadence, Native resume/offset request, WebSocket body authority or second state store. Actual page-owned `/resume` HTTP200 SSE support remains strictly validated and retained when it occurs.
- Typography candidate is tool 30 / reasoning 21 / final 21. Runtime visual acceptance is pending.
- Runtime/manual/real-device b76: **Pending / Unverified**. Stable/Frozen Send: **No**. b39-b76 are permanently reserved.

## DEV-send-stream b75 Runtime override — 2026-09-01

Exact b75 `DEV-send-stream-0.1.0-b75`, source `b77303b8870dc25851dbffbf38ffc153a47bbcb2`, Artifact `9772079468`, IPA SHA `a912547a1845cae182d83d551eb51955b5060062f66ec3fbdf14be45954dab9d` is package-verified and permanently reserved. iPhone/iOS17 Runtime is **partial/rejected**, not pending.

- Positive: b75 no longer promotes a page-owned matching resume request into a Native live response before HTTP200 SSE validation; repeated HTTP404 JSON resume responses therefore no longer flash the prior false `回答失败`.
- Rejected: while another platform's response was still active, the covered production page repeatedly issued matching `/backend-api/f/conversation/resume` but every observed response was HTTP404 JSON. Native correctly created no live response, so no `正在思考` / reasoning / tools / incremental final appeared. Successful Detail Sync/Reload only exposed server-backed visible messages later.
- Typography: exact 26 tool / 18.2 reasoning / 18.2 final values are implemented but the user's latest screenshot rejects the visual result as too tight/low. These numbers are not an accepted UI baseline.
- Geometry: supplied diagnostics prove `cooperative_main_queue` cache-miss scheduling and `resident_cache` reuse are executing. This export does not reproduce the former ~10s worst case, so the interactive-Back acceptance gate remains open.
- Next gate: use the existing Web Rule Lab on the same `.default()` WebKit session to determine current page-owned `stream_status -> resume` ordering/status and whether another page-owned transport follows the first resume 404. Do not guess Native resume/offset/polling or WebSocket body authority. b76 is not allocated yet.

_Last updated: 2026-09-01 through accepted b67 production transport Runtime, positive b72 tested cross-conversation simultaneous-generation Runtime, exact b73 real-device defect evidence, and exact b74 Code/scope/Simulator/Push+PR CI/Artifact/package verification. Phase 9 `DEV-send-stream` remains Active at the b74 human Runtime gate. Stable/Frozen Send remains No._

## Current accepted merged baseline

Foundation b1, auth b6, protocol-read b7, native-read b9, recovery b15, multi-conversation b21, list-cache b23 and **Phase 8 b38** remain accepted merged baselines for their recorded scopes. Exact b38 tested source is `0d1801137e4ee2f5889ca718cd8b2e3612bdaa67`; Runtime Artifact `9708425762`; PR #27 merged at `9110c9e893e8a8665c7a58cf27bb42c65a39cc11`. Stable does not mean Frozen.

## Current Work / source identity

`DEV-send-stream` is Active on `dev/send-stream-20260829`; PR #29 remains open / mergeable / unmerged and evidence-only. Current actual `main` last verified this cycle is `d323b9eed2dda75b9986fc06e14014d3e9b365fb`; final target-main synchronization is still required before merge.

Latest exact product Candidate is **`DEV-send-stream-0.1.0-b74` / `0.1.0 (74)`**:

- exact product/config source `50dd61b8b31cdae184353f4b4bfa6aca24e3a50d`;
- final clean-reassembly `33420128454 / 99580192017` passed exact four-file replay/content equality, scope/invariant audit, `git diff --check` and Xcode 16.4 iOS Simulator compile;
- Push `33420408779 / 99581104920` and PR `33420412792 / 99581117817` — success on exact source;
- canonical Push Artifact `9768668727`; ZIP `sha256:6ac4cc97954a0a26ed258a9775921cc4d12b17a1ff29c5e8d65cddf3c5595cb3`;
- IPA `sha256:07c999fd0e9aaa5685725e6a97f066221f1f986cc3e23a99693a91accda285da`;
- independently unpacked package `0.1.0 (74)` / Candidate b74 / source `50dd61b8b31c` / Release / minimum iOS14 / arm64 / iPhone+iPad family.

b73 real-device evidence localized long resident re-entry delay to repeated historical geometry rebuild, retained the need for more main tool-row spacing, and exposed the missing external active-response lifecycle. A current Web Rule Lab capture proved official Web uses page-owned matching `POST /backend-api/f/conversation/resume` `{conversation_id, offset}` -> HTTP200 SSE after `stream_status` when entering an externally active conversation. b74 observes only that page-owned matching resume stream, never constructs the request/offset or polls, and feeds it into the existing Repository response runtime. b74 also reuses derived b38 geometry only for unchanged resident presentation identity and increases main tool rhythm. Evidence ladder: **Code / exact scope / Simulator compile / Push+PR CI / Artifact / package verified / Runtime pending / Stable-Frozen No.** b39-b74 are permanently reserved.

## b65 accepted probe predecessor

Exact b65 focused iPhone/iOS17 Runtime passed the verified-composer protected-Send / reasoning-final / exact-parent GitHub tool-detail scope: real Send -> HTTP200 SSE -> terminal, reasoning `14/295`, final `71/2827`, exact-parent matches `10/10`, tool presentation/completion `10/10`, and readable nested `工具输入` / `工具输出`. Remaining spacing/slash escaping was non-blocking.

## Exact b66 production Runtime — failed bridge, Send reached service

b66 was the first TD-029 production existing-conversation slice. Exact identity:

- Candidate `DEV-send-stream-0.1.0-b66`, source `9ce228ad880eaf81fc23ba26fe14f4d2bf524acb`, tree `31ef29457273a44dd202a63a96560563154e8823`;
- Push `33337771534 / 99327694040`, PR `33337774136 / 99327701256` — both success;
- Push Artifact `9739572172`;
- ZIP `sha256:6c6d8e165ed070e88a27abafc57973dc847937826e40c552bf9f0d29bb91bb45`;
- IPA `sha256:7f62e875bbd75d54e2d7bf76340f277d02f03e695d464d818fa5cab664c630e9`.

Exact iPhone/iOS17 export `ChatGPTClient-Diagnostics-20260830-220515.json` matched build66/source. Two generations reproduced:

`composer_ready x2 -> submit_result=submitted x2 -> one send_observed -> send_transport_error`

No `coveredExecutor.sendResponse` occurred and Native response characters stayed zero. The user independently verified that the official ChatGPT app already contained the assistant reply, so the protected Send reached the service; Native lost the same-response transport before receiving the HTTP Response object. This is **not** an SSE parser/Web-rule failure.

Source correlation isolated a production Swift->JS duplicate-submit race: b66 kept `pendingSend` until later `send_observed`, while multiple ready callbacks could schedule asynchronous `evaluateJavaScript(submit(...))` calls before page-local `activeSend` became true. Detailed evidence: `docs/project/runtime-evidence/DEV-send-stream-b66-runtime.md`.

## b67 minimal correction

b67 changes only the executor operation gate:

1. `CoveredWebSendExecutor.isBusy` is owned by existing `activeEvents != nil`, spanning request through terminal/failure.
2. `pendingSend` is consumed immediately before issuing the one JS `submit(...)` evaluation.
3. Later duplicate composer-ready callbacks cannot schedule the same pending operation again.
4. Clearing `pendingSend` does not open a second Send window because `activeEvents` remains active.

Exact Root delta is only `+2/-1`; Xcode/workflow changes only allocate b67 identity. No selector, Web rule, protected route, SSE grammar, Repository ownership, Web Rule Lab, retry, resend, polling, timer, watchdog, fallback or compatibility shim changed.

## Durable Phase 9 architecture/security boundary

- Exact b42 proves successful ChatGPT-account protected Send requires browser anti-abuse challenge output. Pure-native/transient-auth account Send remains blocked.
- Separately billed API-product route remains rejected; primary-account Sub2API/Codex-subscription route remains blocked by account-safety policy.
- **TD-029 remains the production Send decision.** Native history/composer/reasoning/tool/final UI is the product surface; one process-resident covered official Web surface may perform browser challenge + exactly one page-owned protected Send.
- Covered Web is transport/challenge execution only, never conversation/message/response/list/draft authority.
- `ConversationRepository` remains sole native conversation/list/detail/recovery/response lifecycle authority.
- `AuthSessionStore` remains sole auth/account authority; `WKWebsiteDataStore.default()` remains sole persistent auth-secret authority. b70 treats exact probe HTTP403 as temporary failure that preserves the last verified identity, while list/detail 401/403 discards stale copied transient transport and never auto-replays the failed operation.
- Full existing-conversation mobile-Web rendering remains rejected by TD-025/TD-028.
- No challenge solving/replay, no second credential store, no duplicate Send to obtain a stream, no automatic Sync/poll loop.
- Sync/Reload never resend/regenerate.

## Web Send maintenance capability

`docs/project/WEB_SEND_ADAPTER.md` remains the durable authority for current evidenced official composer/protected-Send/SSE/reasoning/tool rules and the Web Rule Lab maintenance loop. b66 evidence does **not** change that adapter contract: the failure was local production orchestration, not an official Web rule change.

The in-app Web Rule Lab is now implemented in the current production branch: visible `WKWebView`, `.default()` store, explicit user execution, temporary script/result only, copy/share allowed, no persisted body/log body, never production response owner.

## Current implementation boundary / shortest remaining Phase 9 sequence

Current source contains the Repository-owned existing-conversation production bridge and Web Rule Lab. b67 transport Runtime is accepted; exact b70 daily-chat parity/auth-lifecycle Runtime is the immediate gate.

After that gate, the shortest remaining sequence is:

1. accept/fix existing-conversation production Send/stream;
2. new-chat first Send and pending->authoritative handoff only if actual timing requires it;
3. exact server Stop evidence and one response-scoped Stop implementation;
4. A/B hidden-response ownership + follow-tail/history intent;
5. Sync/Reload active-response safety + b38 geometry/round/time/Copy regression;
6. final daily-chat Runtime matrix, target-main synchronization and Stable/merge decision.

Final Composer hierarchy/dynamic input/attachment staging belongs future serialized `DEV-composer-parity`; current Work keeps only the validation trigger. Background completion and attachments remain subsequent Works after accepted text Send/Stream ownership.

## Current exact Runtime gate

Install exact b74 Artifact `9768668727` / IPA SHA `07c999fd...285da` on the primary iPhone/iOS17 device. Confirm Candidate/source marker, then verify: repeated re-entry into the previously slow long resident materially removes the ~1.4s geometry rebuild stall without breaking geometry/quick navigation; meaningful main tool rows have larger vertical rhythm; an externally initiated still-active response is adopted when entering the conversation via the official page-owned matching `/resume` SSE without duplicate Send or synthetic user bubble; terminal history reconciles once; one normal local Native Send still follows the b67 protected-Send HTTP200 SSE route; b72 A/B simultaneous-generation ownership remains correct; hidden thoughts stay absent. Export diagnostics for the Runtime run.

## Remaining Unknown / Unverified

Exact b74 resident-geometry/tool-spacing/external-adoption Runtime, new-chat authoritative identity timing, exact server Stop mechanism, broader cross-conversation/service concurrency beyond the exact b72 A/B test, connector-detail schemas beyond the evidenced GitHub mapping, Native-constructed first/exclusive resume, 5/15-minute background behavior, WebContent termination recovery, lower iOS/iPad, non-personal workspace/account switching and native attachment handoff remain Unknown / Unverified unless explicitly tested. CI/Artifact success is never Runtime proof.