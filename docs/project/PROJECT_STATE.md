# Project State

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